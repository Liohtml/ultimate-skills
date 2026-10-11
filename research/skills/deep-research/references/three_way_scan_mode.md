Moved verbatim from SKILL.md section 'Three-Way Scan Mode (WHY / HOW / WHAT)' by ultimate-skills (progressive disclosure).

> **Path note (Ultimate Skills):** as in SKILL.md, paths in the moved text are relative to the skill root (`references/...`, `agents/...`, `templates/...`, `examples/...`); `shared/...` means this plugin's vendored [`../../../shared/`](../../../shared/) directory; `scripts/*.py` and `docs/design/...` exist only in the upstream repo and are optional/advisory, not required to run this skill. The `/ars-mark-read` command named in the method-weaknesses rules is an upstream slash command (upstream academic-research-skills, not included here: https://github.com/Imbad0202/academic-research-skills/blob/ebc21bf2429643fe4c2495aa99e1bbacd926772b/commands/ars-mark-read.md).

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
  - Method weaknesses: ...
```

The WHAT field's method weaknesses follow these rules:

<!-- method-weaknesses:begin -->
**Method weaknesses (per source, #916).** Information only. Nothing here blocks, gates, scores, or asks the scholar a question.

1. **Named design and failure condition.** Name the specific design, measure, sample, or analysis choice, and the condition under which it would distort the result. "Small sample" alone is not enough; "n = 24 from one site, so the site effect cannot be separated from the treatment" is.
2. **Provenance label on every item.** Mark each item `author-acknowledged` or `reader-inferred`. An `author-acknowledged` item carries a locator in one of the v3.7.3 anchor kinds (`quote`, `page`, `section`, `paragraph`). A `reader-inferred` item is an untested inference and says so.
3. **Bounded absence claims.** A statement that the authors do not address X names the sections that were checked (the #548 search-bounded pattern). If those sections cannot be named, do not make the absence claim.
4. **Fixed aspect checklist.** Use the source's paper-type table in `academic-paper-reviewer/references/review_criteria_framework.md` §2 (empirical, theoretical, review / meta-analysis, case study, policy). Mark each criterion in that table `checked: found`, `checked: none found`, or `not checked`. Stop at the end of the table; do not keep adding items until the list feels complete.
5. **No method-level weakness without the text.** When only the abstract or table of contents is available, or the recorded read scope (`/ars-mark-read --scope`) is `abstract_only`, `toc_only`, or `unknown`, write `not assessed (read scope: <scope>)` and no inferred weaknesses. For `sections`, stay within the declared sections.

Do not turn a weakness into an improvement suggestion or research direction; that step stays with the scholar. Keep the entry short:

```
- **Method weaknesses** (<paper type>; read: <what was read>)
  - checked: found: <criterion>, ... | checked: none found: <criterion>, ... | not checked: <criterion>, ...
  - <design choice>; distorts the result when <condition>. [author-acknowledged, <anchor kind>: <locator>] or [reader-inferred]
```

or, when rule 5 applies, `- **Method weaknesses**: not assessed (read scope: <scope>)`.
<!-- method-weaknesses:end -->

Then add:

- common `WHY`
- divergent `HOW`
- strongest `WHAT`
- unresolved global gap

If the user later wants a broader evidence matrix or thematic synthesis, escalate from `three-way-scan` to `lit-review`. Escalate to `systematic-review` only when the author chooses a systematic review (§ Review-form note, #921).
