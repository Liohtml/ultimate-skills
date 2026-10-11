# Reviewing an Existing PRD

Read this when the user asks you to review, critique, score or tighten a PRD,
feature brief or one-pager.

## 1. Before commenting

1. Read the whole document, including linked research if it is provided.
2. Write three one-sentence reconstructions:
   - **Problem:** who has which problem, how often, at what cost.
   - **Outcome:** which metric moves from what to what, by when.
   - **Bet:** why this solution is expected to move it.
   If any of the three cannot be reconstructed from the document, that is the
   first and most important finding.
3. Identify the document's purpose and stage. A discovery one-pager is not
   judged by the standard of a build-ready PRD. Say which standard you apply.

## 2. Section rubric

Rate each section **Missing / Weak / Adequate / Strong**.

| Section | Strong looks like | Weak looks like |
|---|---|---|
| 1. Summary | Problem, segment, bet and primary metric in 2-3 sentences; stands alone | Describes the feature; no metric |
| 2. Contacts | One decision owner; a named owner per function | A list of names with no roles; nobody can say "approved" |
| 3. Background | Problem stated without the solution; labelled evidence with sources; counter-evidence; why now | "Customers have asked for X"; anecdotes; no dates or n |
| 4. Objective | One primary metric with definition, baseline, target, time, source; guardrails; 3-5 reasoned non-goals | "Increase engagement"; output goals; no non-goals |
| 5. Segments | Defined by problem or job; sized; who it is not for | "All users"; demographics only |
| 6. Value proposition | Compared with the real alternative, including doing nothing | Feature list restated as benefits |
| 7. Solution | Prioritised stories with testable criteria; states and edge cases; NFRs as constraints; ranked assumptions with validation | Everything a Must; "should be intuitive"; implementation details; no assumptions listed |
| 8. Release | Smallest release that tests the bet; rollout method, decision rule, rollback triggers; owned open questions | A date and "launch"; no way to tell success from failure |

## 3. Anti-pattern detection cues

| Anti-pattern | Look for | Ask or suggest |
|---|---|---|
| Solution-first | The problem statement contains the feature name; "users need a ..." | "What is the user trying to do, and what happens today when they try?" |
| Unmeasurable goal | Verbs like improve, enhance, delight, streamline with no number | "Which metric, from what baseline, to what target, by when?" |
| Output goal | Objective is a launch, a release or a feature count | "If we ship it and nothing changes for users, did we succeed?" |
| Everything a Must | No Should, Could or Won't; more than about two-thirds of stories are Musts | Apply the Must test to each; propose which to demote |
| Missing non-goals | No out-of-scope list, or one that only says "everything else" | Suggest 3-5 concrete non-goals from adjacent ideas in the doc |
| No guardrails | One metric that can be gamed | Name the counter-metric that the primary could damage |
| Assumption as fact | "Users will...", "This will increase..." with no source | Label `[Assumption]`, add to 7.4 with a validation step |
| Evidence theatre | Many numbers, none connected to the problem; vanity metrics | "Which of these would change the decision if it were different?" |
| Spec in disguise | Tables, schemas, API shapes, specific widgets | Keep the constraint, move the design to the engineering spec |
| Vague acceptance criteria | Fast, easy, seamless, intuitive, robust | Rewrite as observable behaviour with a threshold |
| Happy path only | No error, empty, permission or migration states | Walk the edge-case catalogue in `requirements-and-acceptance-criteria.md` |
| Fake precision | Exact baselines or market sizes with no source | Ask for the source; otherwise use a range or `[TBD: owner]` |
| Orphan requirement | A requirement that serves no stated problem or metric | Cut it or add it to the parking lot |
| Unowned questions | Open questions with no owner or date | Assign owner, blocking flag, needed-by |
| Frozen document | Meeting decisions missing; stale dates | Add version and change log; update the decisions |

## 4. Output format

```markdown
## PRD review: <document name>

**Verdict:** Ready for build / Ready with fixes / Needs rework
**Standard applied:** <discovery one-pager / build-ready PRD>

**Reconstruction**
- Problem: <one sentence, or "cannot be reconstructed">
- Outcome: <one sentence>
- Bet: <one sentence>

**Section ratings**
| Section | Rating | Note |
|---|---|---|
| 1. Summary | Adequate | |
| ... | | |

**Top issues (ranked by impact on the decision)**
1. **<Issue>** (section, quote or location)
   Why it matters: <consequence if unfixed>
   Fix: <concrete rewrite, or the question the author must answer>
2. ...

**What is already strong**
- <specific strengths, so the author keeps them>

**Questions for the author**
- <only questions the document cannot answer>
```

Guidelines:

- Rank by impact on the decision, not by order in the document. Three issues
  that change the outcome beat twenty wording nits.
- Quote the text you criticise; give a rewrite, not just a complaint.
- Do not invent weaknesses. If a section is sound, say so.
- If the core doubt is whether the bet is right, recommend `strategy-red-team`;
  if it is whether the launch will go well, recommend `pre-mortem`.
- Offer to apply the fixes, but do not rewrite the whole document unasked.
