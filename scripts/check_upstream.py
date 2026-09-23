#!/usr/bin/env python3
"""Report skills whose upstream source changed since the commit we vendored.

Usage:
    python3 scripts/check_upstream.py [--clone-dir DIR] [--diff]
                                      [--skill NAME ...] [--repo OWNER/REPO ...]

For every row in PROVENANCE.csv this clones (or fetches) the upstream repo
https://github.com/<source_repo>.git into --clone-dir/<owner>__<repo> (default
clone dir: a temp dir; pass a persistent dir to reuse clones between runs) and
compares each tracked upstream path at `source_commit` with upstream HEAD.

PROVENANCE.csv columns
  plugin, skill     where the skill lives here (<plugin>/skills/<skill>/).
  source_repo       upstream GitHub "owner/repo".
  source_license    SPDX id of the upstream material.
  source_path       one or more upstream paths separated by ";". Each path
                    starts with the upstream repo name, the rest is the path
                    inside that repo (upstream dir names can differ from ours;
                    a bare repo name means the repo root). A path may be a
                    skill directory, any other directory, or a single file.
  source_commit     full upstream SHA the material was taken from, or
                    "unmatched".
  upstream_status   identical-to-head (our files equal upstream at
                    source_commit) or modified-locally.
  role              "base" (the skill was built on this source) or "merged"
                    (material from this source was merged into the skill).
                    A skill has exactly one base row and any number of merged
                    rows; --skill NAME selects all of them.

Output per row: UP-TO-DATE, CHANGED (with commit count and the one-line log of
upstream commits touching the tracked paths since source_commit), MISSING
upstream, or UNKNOWN (source_commit unmatched). For a directory containing a
SKILL.md the report says whether SKILL.md itself changed. --diff prints the
diff of changed single files and SKILL.md files.
Exit code: 0 = nothing changed, 1 = at least one row changed/missing,
2 = usage/clone error. Requires git and network access to github.com.

After syncing, update the row's source_commit / upstream_status in
PROVENANCE.csv.
"""
import argparse
import csv
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args, cwd=None, check=True):
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.strip()}")
    return p


def ensure_clone(repo, dest):
    if (dest / ".git").is_dir():
        if git("rev-parse", "--is-shallow-repository", cwd=dest).stdout.strip() == "true":
            git("fetch", "-q", "--unshallow", "--filter=blob:none", cwd=dest, check=False)
        git("fetch", "-q", "origin", cwd=dest)
        git("reset", "-q", "--hard", "FETCH_HEAD", cwd=dest)
    else:
        # full history (blob-less) so source_commit is always reachable
        git("clone", "-q", "--filter=blob:none", f"https://github.com/{repo}.git", str(dest))


def normalize_repo(repo):
    repo = repo.strip().removesuffix(".git").rstrip("/")
    for prefix in ("https://github.com/", "http://github.com/", "github.com/"):
        if repo.startswith(prefix):
            repo = repo[len(prefix):]
    return repo


def split_paths(row):
    """Yield in-repo paths ("." for the repo root) of a PROVENANCE row."""
    for entry in row["source_path"].split(";"):
        entry = entry.strip().strip("/")
        if not entry:
            continue
        _, _, sub = entry.partition("/")
        yield sub or "."


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--clone-dir", type=Path)
    ap.add_argument("--diff", action="store_true", help="print diffs of changed files / SKILL.md")
    ap.add_argument("--skill", action="append", help="only check these skills (all their rows)")
    ap.add_argument("--repo", action="append", help="only check rows from these owner/repo")
    a = ap.parse_args()

    clone_dir = a.clone_dir or Path(tempfile.mkdtemp(prefix="upstream-"))
    clone_dir.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(ROOT / "PROVENANCE.csv", encoding="utf-8")))
    if a.skill:
        rows = [r for r in rows if r["skill"] in a.skill]
    if a.repo:
        wanted = {normalize_repo(x) for x in a.repo}
        rows = [r for r in rows if normalize_repo(r["source_repo"]) in wanted]
    if not rows:
        print("no matching rows in PROVENANCE.csv", file=sys.stderr)
        return 2

    per_skill = {}
    for r in rows:
        per_skill[(r["plugin"], r["skill"])] = per_skill.get((r["plugin"], r["skill"]), 0) + 1

    cloned, changed = {}, 0
    for r in rows:
        repo = normalize_repo(r["source_repo"])
        dest = clone_dir / repo.replace("/", "__")
        if repo not in cloned:
            try:
                ensure_clone(repo, dest)
                cloned[repo] = True
            except RuntimeError as e:
                print(f"error: cannot clone {repo}: {e}", file=sys.stderr)
                return 2
        base = r.get("source_commit", "").strip()
        label = f"{r['plugin']}/{r['skill']}"
        if per_skill[(r["plugin"], r["skill"])] > 1 or r.get("role", "base") != "base":
            label += f" [{r.get('role') or 'base'}: {repo}]"
        subs = list(split_paths(r))

        missing = [s for s in subs if s != "." and
                   git("cat-file", "-e", f"HEAD:{s}", cwd=dest, check=False).returncode]
        if missing:
            print(f"MISSING     {label}: {', '.join(missing)} no longer exist(s) upstream in {repo}")
            changed += 1
            continue
        if not base or base == "unmatched":
            print(f"UNKNOWN     {label}: no source_commit recorded")
            continue
        if git("cat-file", "-e", f"{base}^{{commit}}", cwd=dest, check=False).returncode:
            print(f"UNKNOWN     {label}: source_commit {base[:10]} not found in {repo}")
            continue

        log = git("log", "--oneline", f"{base}..HEAD", "--", *subs, cwd=dest).stdout.strip()
        if not log:
            print(f"UP-TO-DATE  {label}")
            continue
        changed += 1
        # which tracked files changed: SKILL.md of skill dirs, or single files
        focus = []
        for s in subs:
            is_dir = git("cat-file", "-t", f"HEAD:{s}", cwd=dest, check=False).stdout.strip() == "tree"
            f = (f"{s}/SKILL.md" if s != "." else "SKILL.md") if is_dir else s
            if is_dir and git("cat-file", "-e", f"HEAD:{f}", cwd=dest, check=False).returncode:
                continue  # plain directory without SKILL.md
            if git("diff", "--quiet", base, "HEAD", "--", f, cwd=dest, check=False).returncode:
                focus.append(f)
        what = f"{', '.join(focus)} changed" if focus else "other files changed"
        print(f"CHANGED     {label}: {len(log.splitlines())} commit(s), {what} "
              f"({base[:10]}..HEAD in {repo}: {'; '.join(subs)})")
        for line in log.splitlines():
            print(f"              {line}")
        if a.diff:
            for f in focus:
                print(git("diff", base, "HEAD", "--", f, cwd=dest).stdout)
    print(f"\n{changed} of {len(rows)} provenance row(s) have upstream changes. Clones in {clone_dir}")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
