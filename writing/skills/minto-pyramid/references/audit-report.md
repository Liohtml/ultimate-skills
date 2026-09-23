# Audit mode: a structured Pyramid review with a verdict

> Adapted from [tyroneross/pyramid-principle `pyramid-audit`](https://github.com/tyroneross/pyramid-principle/tree/e6c6a123bf69efb5964f4e767ce585ef37545031/skills/pyramid-audit) (Apache-2.0, see [audit-report.LICENSE.txt](audit-report.LICENSE.txt)). **Modified by ultimate-skills:** condensed into one reference for `minto-pyramid`; routing to the upstream sibling skills removed; the upstream source-anchor IDs (which point to a file of verbatim book excerpts that is not included) replaced with plain page references to Barbara Minto, *The Pyramid Principle*, 2009 revised edition; the quick checklist and heading checks folded in from the upstream `diagnostic-checklist.md`.

Use this when the user asks for a **review, diagnosis or verdict** on a draft rather than a rewrite: "is this ready to send?", "audit this against the pyramid principle", "what's structurally wrong with this memo?". The gate in SKILL.md still applies first: if the document is a timeline, runbook, tutorial or note, say so and stop.

This mode audits. It does not rewrite the content, draft a replacement, or explain the whole framework. If the user then asks for the rewrite, switch to operation 1 (Restructure) in SKILL.md.

## Identify the inputs

1. **Content:** the exact text or file to audit. Do not audit without user-supplied content.
2. **Reader question:** use the user's when given; otherwise infer one from the content and label it *inferred*.
3. **Medium:** email, memo, report, deck or fragment. Infer only when the content makes it clear.

The reader question and medium are audit metadata. They cannot supply a missing Situation, Complication, claim or evidence.

## Run five checks, in order

### 1. Governing thought (always run)
- Quote the single main claim verbatim, or write `Not stated`.
- Does it directly answer the reader question?
- Separate the answer from its evidence: when one sentence recommends and another gives the reason, the recommendation is the governing thought even if the evidence comes first.
- Does it appear before the supporting detail? If the reader must process support before learning the claim, flag a **buried governing thought**.
- Is it a claim or a container label ("This memo covers...")? A label is a finding. (Minto p. 5)

### 2. SCQA introduction (only if there is an opening preamble)
- A governing thought followed directly by support is pyramid body, not an implied preamble.
- For a fragment, list, section or continuation with no preamble write: `Not applicable: the supplied content contains no opening preamble.`
- Otherwise rate Situation, Complication, Question and Answer as `Pass`, `Weak` or `Fail`, using only the supplied text. Do not infer a Situation or Complication from the reader question or assumed shared knowledge. (Minto pp. 22-23)

### 3. Vertical logic
For each major point, state the question it raises (`Why?`, `How?`, `Why do you say that?`) and check that the material directly below answers that question. Flag a violation only when the text shows a different answer, information arriving before its question, or an unsupported hanging assertion. Quote the break. (Minto pp. 17-18)

### 4. Horizontal logic (only for a peer set of two or more siblings)
A single sentence, statistic or fact is not a peer set. For each real peer set:
1. Write the candidate parent question.
2. Name the role every peer plays under it (reasons, findings, controls, risks, steps...). Peers on different topics are fine if they answer the same parent question in the same role; do not classify them by their nouns.
3. Check mutual exclusivity from the supplied text.
4. Check collective exhaustiveness **only** when the content or cited domain evidence defines the universe. "Three controls" asserts completeness; it does not prove it. For an excerpt with no defined universe the required result is `Exhaustiveness is not verifiable from the supplied content.` Never declare a set complete or invent the missing item.
5. Check that the set uses one reasoning mode: deductive or inductive, not both. (Minto p. 63)
6. Check that the parent is an inference that summarizes the children, not a topic label. (Minto pp. 5, 96)

### 5. Ordering
Assign an order only when the text shows one: deductive, chronological (explicit time or process sequence), structural (explicit parts of a whole) or comparative (explicit ranking criterion). List position alone does not establish comparative order. If no order is discernible, say so and judge whether it materially harms comprehension. Do not invent an ordering rationale. (Minto p. 5)

**Long documents and decks only:** headings should assert the section's point ("Churn is concentrated in the SMB tier"), not name a topic ("Churn analysis"), and peer headings should be grammatically parallel.

## Keep the audit honest

Every finding must quote or describe evidence in the supplied content and cite the rule it breaks. A comment with no rule behind it is an editorial observation, not a Pyramid violation, and gets no severity label.

Audit structure, not factual truth. A scoped factual statement ("all requests received this quarter") is not a MECE violation. If the user also wants the numbers checked, report that in a separate `SOURCE INTEGRITY` section (for analytical work, the `validate-data` skill in the product plugin covers this), and keep it apart from `STRUCTURE`.

Do not:
- copy names, facts, scenarios or fixes from examples into the report
- invent missing context, evidence, domain facts or reader knowledge
- declare a peer set exhaustive without evidence that defines the universe
- assign a logical order the text does not show
- add fixes for problems the audit did not find
- rewrite the content unless the user separately asks for a rewrite

## Choose the verdict

Finish all five checks first, then choose by effect on the reader, not by counting findings:

- **Restructure:** the governing thought is missing or answers the wrong question, or structural breaks stop the reader following the central argument.
- **Minor edits:** the argument and its support hold, but localized problems reduce clarity.
- **Share as-is:** the governing thought is clear and comes before support, vertical logic holds, peer groups each play one role, and no finding would change the reader's understanding.

Verdict and fixes must agree. No material finding and no structural fix means the verdict is `Share as-is`; `Minor edits` requires at least one named localized finding with its fix.

Severity labels per finding: `Strong checkpoint` only when the missing or false central structure prevents reliable use; `Guidance` for a material but localized logic problem; `Polish` for a minor, non-blocking improvement.

## Report format

Return these headings in order and nothing else:

1. **OVERALL VERDICT**: start with `Share as-is`, `Minor edits` or `Restructure`, then the highest-leverage reason.
2. **GOVERNING THOUGHT**: the quote or `Not stated`, and whether it answers the reader question.
3. **SCQA CHECK**: the four ratings, or the single `Not applicable` line.
4. **FINDINGS**: only demonstrated vertical, horizontal or ordering violations. For each: rule type, quoted or described text, why it breaks, severity. If none, write exactly `None identified.`
5. **RANKED FIXES**: only fixes tied to findings, highest leverage first. If none: `None: no structural fix is required.`

No placeholder brackets, drafting instructions, rewritten artifact or self-check in the output.

## Verify before returning

1. Every violation maps to supplied text and a named rule.
2. SCQA is `Not applicable` when there is no opening preamble.
3. Every mixed-kind finding fails both the parent-question and shared-role tests.
4. No exhaustiveness or ordering claim goes beyond the supplied evidence.
5. Every fix maps to a reported finding, and the verdict agrees with the fixes.
6. The response contains only the audit report.

## Quick checklist (rapid review)

Mark each Pass or Fail; any Fail becomes a finding.

- **Governing thought:** stated explicitly · appears in the opening · answers the reader's question · is a claim, not a container label
- **SCQA** (skip for continuations): Situation grounded in shared, undisputed context · Complication present and specific · Question implied or stated correctly · Answer explicit and at the opening
- **Vertical:** each major claim raises a clear question · the material below answers that question · no information before its question · no hanging assertions
- **Horizontal:** peers can be named with one plural noun · mutually exclusive · exhaustive relative to the parent (when verifiable) · one logic mode · parent is an inference, not a label
- **Ordering:** a valid order is applied · one order per peer set · the order fits the kind of set
- **Headings** (long form and decks): assert the point, not the topic · peers are parallel
