#!/usr/bin/env python3
"""Validate the ultimate-skills marketplace (stdlib only).

Usage:  python3 scripts/validate.py [repo_root]

Checks
  * every <plugin>/skills/<name>/SKILL.md has YAML frontmatter, `name` equal to
    the directory name, and a non-empty `description` of <= 1024 chars
  * every plugin's .claude-plugin/plugin.json exists, parses, and has
    "skills": "./skills"; every skill dir contains a SKILL.md
  * every plugin `source` in .claude-plugin/marketplace.json exists and every
    plugin dir on disk is listed in the marketplace
  * relative markdown links in all *.md files resolve (http(s)/mailto/#anchor
    links are ignored; see LINK_ALLOWLIST for known placeholders)
Warnings (non-fatal)
  * SKILL.md longer than 500 lines

Exit code 1 if any error was found, 0 otherwise.
"""
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent).resolve()
MAX_DESC = 1024
MAX_LINES = 500
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}

# (file relative to ROOT, link target) pairs that are intentional placeholders
# / illustrative examples inside upstream skill text, not real links.
LINK_ALLOWLIST = {
    ("research/skills/academic-paper/agents/formatter_agent.md", "url"),
    ("research/skills/academic-paper/agents/formatter_agent.md", "path"),
}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(p):
    return str(Path(p).relative_to(ROOT))


def parse_frontmatter(text):
    """Minimal YAML-frontmatter reader: top-level `key: value` pairs, with
    support for quoted scalars and folded/literal block scalars (> / |)."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None
    fm, key, block = {}, None, None
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            key, val = m.group(1), m.group(2).strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):
                fm[key], block = "", key
                continue
            block = None
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            fm[key] = val
        elif block and line.strip():
            fm[block] = (fm[block] + " " + line.strip()).strip()
    return fm


def check_skills():
    plugins = sorted(p.parent.parent for p in ROOT.glob("*/.claude-plugin/plugin.json"))
    for plugin in plugins:
        pj = plugin / ".claude-plugin" / "plugin.json"
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            err(f"{rel(pj)}: invalid JSON ({e})")
            continue
        if data.get("name") != plugin.name:
            err(f"{rel(pj)}: name '{data.get('name')}' != directory '{plugin.name}'")
        if data.get("skills") != "./skills":
            err(f"{rel(pj)}: expected \"skills\": \"./skills\", got {data.get('skills')!r}")
        skills_dir = plugin / "skills"
        if not skills_dir.is_dir():
            err(f"{rel(plugin)}: missing skills/ directory")
            continue
        for sd in sorted(d for d in skills_dir.iterdir() if d.is_dir()):
            if not (sd / "SKILL.md").is_file():
                err(f"{rel(sd)}: skill directory without SKILL.md")
    for skill_md in sorted(ROOT.glob("*/skills/*/SKILL.md")):
        name = skill_md.parent.name
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        r = rel(skill_md)
        if fm is None:
            err(f"{r}: missing or unterminated YAML frontmatter")
            continue
        if fm.get("name") != name:
            err(f"{r}: frontmatter name '{fm.get('name')}' != directory '{name}'")
        desc = fm.get("description", "")
        if not desc:
            err(f"{r}: missing description")
        elif len(desc) > MAX_DESC:
            err(f"{r}: description is {len(desc)} chars (max {MAX_DESC})")
        n = text.count("\n") + (0 if text.endswith("\n") else 1)
        if n > MAX_LINES:
            warn(f"{r}: {n} lines (> {MAX_LINES}; consider moving detail to references/)")
    return plugins


def check_marketplace(plugins):
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        data = json.loads(mp.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        err(f"{rel(mp) if mp.exists() else '.claude-plugin/marketplace.json'}: {e}")
        return
    listed = set()
    for p in data.get("plugins", []):
        src = p.get("source")
        if isinstance(src, str) and src.startswith("./"):
            path = (ROOT / src).resolve()
            listed.add(path)
            if not (path / ".claude-plugin" / "plugin.json").is_file():
                err(f"marketplace.json: plugin '{p.get('name')}' source {src} has no .claude-plugin/plugin.json")
    for plugin in plugins:
        if plugin.resolve() not in listed:
            err(f"marketplace.json: plugin directory '{plugin.name}' is not listed")


LINK_RE = re.compile(r"(?<!!)\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_RE = re.compile(r"!\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def strip_code(text):
    out, fence = [], None
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif m.group(1) == fence:
                fence = None
            out.append("")
            continue
        out.append("" if fence else re.sub(r"`[^`\n]*`", "", line))
    return "\n".join(out)


def check_links():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            f = Path(dirpath) / fn
            r = rel(f)
            text = strip_code(f.read_text(encoding="utf-8", errors="replace"))
            for rx in (LINK_RE, IMG_RE):
                for m in rx.finditer(text):
                    target = m.group(1)
                    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                        continue  # http(s), mailto, other schemes, anchors
                    if (r, target) in LINK_ALLOWLIST:
                        continue
                    path = target.split("#", 1)[0].split("?", 1)[0]
                    if not path:
                        continue

                    dest = (ROOT / path.lstrip("/")) if path.startswith("/") else (f.parent / unquote(path))
                    if not dest.exists():
                        line = text.count("\n", 0, m.start()) + 1
                        err(f"{r}:{line}: broken link -> {target}")


def main():
    plugins = check_skills()
    check_marketplace(plugins)
    check_links()
    n_skills = len(list(ROOT.glob("*/skills/*/SKILL.md")))
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\nChecked {len(plugins)} plugins, {n_skills} skills: "
          f"{len(errors)} error(s), {len(warnings)} warning(s).")
    print("FAILED" if errors else "OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
