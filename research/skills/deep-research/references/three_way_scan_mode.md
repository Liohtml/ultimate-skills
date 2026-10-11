Moved verbatim from SKILL.md section 'Three-Way Scan Mode (WHY / HOW / WHAT)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`, `templates/...`, `examples/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill.

# Deep Research — Three-Way Scan Mode

## Three-Way Scan Mode (WHY / HOW / WHAT)

Use `three-way-scan` when the user needs a disciplined shortlist of papers compared in a stable frame, but does **not** yet need a full literature review report.

- **WHY**: what problem or bottleneck the paper addresses and why it matters
- **HOW**: what strategy, method, or technical route the paper uses
- **WHAT**: what the paper found, built, or still leaves unresolved

This mode is intentionally lighter than `lit-review`. It prioritizes:

1. candidate retrieval
2. deduplication
3. compact per-paper extraction
4. cross-paper synthesis of shared WHY, divergent HOW, and remaining gaps

Recommended per-paper output:

```markdown
## <paper title>
Source: <provider> | Year: <year> | Link: <url>

- WHY: ...
- HOW: ...
- WHAT: ...
```

Then add:

- common `WHY`
- divergent `HOW`
- strongest `WHAT`
- unresolved global gap

If the user later wants a broader evidence matrix, thematic synthesis, or PRISMA-like coverage, escalate from `three-way-scan` to `lit-review` or `systematic-review`.
