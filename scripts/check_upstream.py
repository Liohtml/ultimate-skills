#!/usr/bin/env python3
"""Report skills whose upstream source changed since the commit we vendored.

Usage:
    python3 scripts/check_upstream.py [--clone-dir DIR] [--diff] [--skill NAME ...]

For every row in PROVENANCE.csv this clones (or fetches) the upstream repo
https://github.com/<source_repo>.git into --clone-dir (default: a temp dir;
pass a persistent dir to reuse clones between runs), then compares
<source_path>/SKILL.md at `source_commit` with upstream HEAD. Only SKILL.md is
compared; references/ etc. are listed as "other files changed" if the skill
directory differs.

  source_path   first segment is the upstream repo name, the rest is the path
                inside that repo (upstream dir names can differ from ours; see
                NOTICE.md).
  source_commit upstream commit our SKILL.md was taken from, or "unmatched".

Output per skill: UP-TO-DATE, CHANGED (with commit count and the one-line log
of upstream commits touching the skill since source_commit), MISSING upstream,
or UNKNOWN (source_commit unmatched). --diff also prints the SKILL.md diff.
Exit code: 0 = nothing changed, 1 = at least one skill changed/missing,
2 = usage/clone error. Requires git and network access to github.com.

After syncing a skill, update its source_commit / upstream_status row in
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--clone-dir", type=Path)
    ap.add_argument("--diff", action="store_true", help="print SKILL.md diffs")
    ap.add_argument("--skill", action="append", help="only check these skills")
    a = ap.parse_args()

    clone_dir = a.clone_dir or Path(tempfile.mkdtemp(prefix="upstream-"))
    clone_dir.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(ROOT / "PROVENANCE.csv", encoding="utf-8")))
    if a.skill:
        rows = [r for r in rows if r["skill"] in a.skill]

    cloned, changed = {}, 0
    for r in rows:
        repo = r["source_repo"]
        name, sub = r["source_path"].split("/", 1)
        dest = clone_dir / name
        if repo not in cloned:
            try:
                ensure_clone(repo, dest)
                cloned[repo] = True
            except RuntimeError as e:
                print(f"error: cannot clone {repo}: {e}", file=sys.stderr)
                return 2
        base = r.get("source_commit", "")
        label = f"{r['plugin']}/{r['skill']}"
        if git("cat-file", "-e", f"HEAD:{sub}/SKILL.md", cwd=dest, check=False).returncode:
            print(f"MISSING     {label}: {sub}/SKILL.md no longer exists upstream")
            changed += 1
            continue
        if not base or base == "unmatched":
            print(f"UNKNOWN     {label}: no source_commit recorded")
            continue
        log = git("log", "--oneline", f"{base}..HEAD", "--", sub, cwd=dest).stdout.strip()
        skill_diff = git("diff", "--quiet", base, "HEAD", "--", f"{sub}/SKILL.md", cwd=dest, check=False).returncode
        if not log:
            print(f"UP-TO-DATE  {label}")
            continue
        changed += 1
        what = "SKILL.md changed" if skill_diff else "other files changed"
        print(f"CHANGED     {label}: {len(log.splitlines())} commit(s), {what} "
              f"({base[:10]}..HEAD in {repo}:{sub})")
        for line in log.splitlines():
            print(f"              {line}")
        if a.diff and skill_diff:
            print(git("diff", base, "HEAD", "--", f"{sub}/SKILL.md", cwd=dest).stdout)
    print(f"\n{changed} of {len(rows)} skill(s) have upstream changes. Clones in {clone_dir}")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
