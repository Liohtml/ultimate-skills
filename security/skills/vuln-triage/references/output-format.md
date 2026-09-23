# Output formats (Phase 6)

> Part of the `vuln-triage` skill. Adapted from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145/.claude/skills/triage) (Apache-2.0); modified by ultimate-skills (split out of the upstream SKILL.md).

## 6b. Write `./TRIAGE.json`

```json
{
  "triage_completed": true,
  "triage_context": {
    "mode": "interactive|auto",
    "environment": "...",
    "threat_model": ["..."],
    "scoring": "...",
    "noise_tolerance": "...",
    "votes_per_finding": 3,
    "repo": "..."
  },
  "summary": {
    "input_count": 0,
    "duplicates": 0,
    "false_positives": 0,
    "true_positives": 0,
    "needs_manual_test": 0,
    "by_severity": {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
  },
  "findings": [
    {
      "id": "f001",
      "source": "VULN-FINDINGS.json#0",
      "title": "...",
      "file": "...",
      "line": 0,
      "category": "...",
      "claimed_severity": "HIGH",
      "verdict": "true_positive|false_positive|duplicate",
      "verify_verdict": "exploitable|mitigated|needs_manual_test|null",
      "confidence": 0.0,
      "severity": "HIGH|MEDIUM|LOW|null",
      "severity_label": "...",
      "severity_alignment": 0,
      "preconditions": ["..."],
      "access_level": "...",
      "threat_match": "...|null",
      "rationale": "file:line-cited prose: reachability, protections, why each held or didn't; then ranking rationale",
      "vote_breakdown": {"true_positive": 0, "false_positive": 0, "cannot_verify": 0},
      "refute_reasons": ["..."],
      "exclusion_rule": null,
      "first_links": ["file:line", "..."],
      "duplicate_of": null,
      "absorbed": ["..."],
      "owner_hint": "...",
      "missing_fields": ["..."]
    }
  ]
}
```

Every input finding appears exactly once (duplicates reference their
canonical via `duplicate_of`). Do not silently drop anything. Do not print
this JSON to the terminal; write to file only.

## 6c. Write `./TRIAGE.md`

Reviewer-facing report. Build it **incrementally**. Do NOT emit the whole
file in one Write. One chunk per finding; a stalled chunk loses that one
section, not the file.

**Step 1 — header.** Write tool → `./TRIAGE.md` (clobbers any prior file)
containing only the title block, summary, and `## Act on these` heading:

```
# Triage Report

{summary line: N in -> D duplicates, F false positives, T confirmed (H high / M med / L low), X need manual test}

Context: {mode}; environment = {environment}; scoring = {scoring}; {votes}-vote verification.

## Act on these
```

**Step 2 — per finding.** For each true_positive in severity order:
1. Write tool → `./.triage-state/_chunk.tmp` containing ONE finding's section:

```
### [{severity}] {title}  ({id})
`{file}:{line}` | {category} | claimed {claimed_severity} (alignment {severity_alignment:+d}) | confidence {confidence}/10
**Owner:** {owner_hint}
**Verdict:** {verify_verdict}, votes {vote_breakdown}
**Preconditions ({n}):** {bulleted}
**Threat-model match:** {threat_match or "none"}
**Why:** {rationale}
**Reachability evidence:** {first_links}
{if verify_verdict == needs_manual_test:}
> Recommend a human build a PoC; static reasoning hit its limit.
```

2. Bash:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py append ./TRIAGE.md --from ./.triage-state/_chunk.tmp`

Repeat for each true_positive.

**Step 3 — footer.** Write tool → `./.triage-state/_chunk.tmp` containing the
Dropped table, then `checkpoint.py append` it the same way:

```
## Dropped

| id | title | file:line | why dropped |
{false_positives: refute_reasons + exclusion_rule}
{duplicates: "duplicate of {duplicate_of}"}
{unlocatable: "no source location in input"}
```

**Checkpoint (final):** Bash:
`python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py done ./.triage-state 6`
The next invocation's resume check sees `status == "complete"` and starts
fresh.

