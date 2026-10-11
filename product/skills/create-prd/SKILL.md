---
name: create-prd
description: "Create or review an evidence-first Product Requirements Document in 8 sections: summary, contacts and decision owner, background (problem evidence, why now), objective (primary metric with baseline and target, guardrails, non-goals), market segments, value propositions, solution (UX states, MoSCoW requirements with acceptance criteria, edge cases, ranked assumptions) and release (rollout or experiment plan, decision rule, kill criteria, open questions). Includes a review rubric and anti-patterns. Use when writing a PRD, feature brief or one-pager, scoping a feature with goals and non-goals, defining success metrics or acceptance criteria, or reviewing or tightening a PRD. For an engineering spec use spec-driven-development (engineering plugin); to attack the bet use strategy-red-team; for launch risk use pre-mortem; for value proposition and personas in depth use value-proposition and user-personas."
---

# Create a Product Requirements Document

> Includes material adapted from [anthropics/knowledge-work-plugins `write-spec`](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/product-management/skills/write-spec) (Apache-2.0, see `LICENSE.txt`). **Modified by ultimate-skills:** its priority tests, metric, acceptance-criteria and scope guidance were rewritten and merged into this 8-section template (base skill: phuryn/pm-skills, MIT).

## Purpose

You are an experienced product manager responsible for creating, or reviewing, the Product Requirements Document (PRD) for $ARGUMENTS. The PRD is the authoritative statement of **what problem we are solving, for whom, how we will know it worked, and what we will not do**. It aligns stakeholders and guides design and engineering. It is not the engineering spec: it constrains the *how* but does not design it.

## Context

A PRD is a decision document. Its job is to make a bet explicit and testable: *we believe that building X for segment Y will move metric Z from A to B, and here is the evidence*. A well-structured PRD lets engineers, designers, leadership and go-to-market read the same page and reach the same answer.

**Right-size the document** before writing:

| Situation | Format |
|---|---|
| Small, reversible change, one team, a few weeks of work | One-pager: sections 1, 3, 4, 7.2 and 8 only |
| New capability, several teams, customer-facing commitment, or hard to reverse | Full 8-section PRD |
| The problem itself is unproven (no evidence anyone has it) | No PRD yet. Run discovery first with `interview-script` and `opportunity-solution-tree`, then come back |

**Modes:** *Create* (new PRD), *Review* (critique an existing PRD, see "Reviewing an existing PRD" below), *Update* (revise after decisions or new evidence; keep a change log).

## Instructions

### 1. Gather information: evidence before solution

- If the user provides files (research, tickets, analytics exports, earlier PRDs, designs), read them first. If they mention research, URLs or customer data, read those; use web search for market context only where it changes a decision.
- Ask for what is missing, most important first, conversationally rather than as a questionnaire: the user problem and who has it; the evidence; the outcome and how it will be measured today; constraints (hard deadlines, regulation, dependencies); prior attempts; who decides.
- If something is still unknown, keep going and mark it inline as `[ASSUMPTION]` or `[TBD: owner]`. **Never invent data, quotes, customer names or baselines.** A visible gap is better than a plausible fiction.

Label every factual claim with its evidence type:

| Label | Meaning | Must include |
|---|---|---|
| `[Data]` | Measured: analytics, support volume, revenue, logs | Source, date range |
| `[Research]` | Qualitative: interviews, usability tests, sales calls | n, segment, date |
| `[Assumption]` | Believed, not yet shown | An entry in section 7.4 with a validation plan |

### 2. Think step by step before writing

- **Problem:** Can you state the problem without naming the solution? Who has it, how often, how do they cope today, what does it cost them and us?
- **Outcome:** What user behaviour or business metric changes if we succeed? By how much, by when?
- **Bet:** Why is this solution the best way to reach that outcome? Which alternatives were considered and why rejected?
- **Risks:** Which of the four product risks is largest: value (will they want it), usability (can they use it), feasibility (can we build it), viability (does it work for the business: legal, cost, sales, brand)?
- **Scope:** What is the smallest release that tests the bet?

### 3. Apply the PRD template

Create a document with these 8 sections. Read [references/prd-template.md](references/prd-template.md) when drafting, for the copy-ready template; read [references/example-prd.md](references/example-prd.md) when you need to see the expected depth and tone.

**1. Summary** (2-3 sentences)
- Problem, for whom, the proposed bet, and the one metric that will tell us. A busy executive should get the gist in 30 seconds.
- Status (draft / in review / approved), version, last updated.

**2. Contacts**
- Name, role and comment for key stakeholders.
- Name **one decision owner** (approves scope and launch) and a directly responsible person per function: product, design, engineering, data, go-to-market, support, legal/privacy where relevant.

**3. Background**
- **Problem statement** in the user's terms, without the solution: who, what, when, how often, current workaround, cost of not solving it.
- **Evidence:** the 2-5 strongest labelled facts. Include disconfirming evidence; hiding it is how teams build the wrong thing.
- **Why now?** What changed: customers, market, technology, regulation, strategy? Is this something that just recently became possible?
- **Prior art:** earlier attempts, competitor approaches, what we learned.

**4. Objective**
- What is the objective and why does it matter? How does it benefit customers and the company, and how does it align with vision and strategy (link the north-star metric if one exists)?
- **Success metrics:** one primary metric, 1-3 leading or secondary metrics, and 1-3 **guardrails** that must not get worse. Each row: definition, baseline, target, timeframe, data source. Outcomes, not outputs ("cut median time to first invoice from 3 days to 1", not "ship onboarding wizard").
- **Non-goals:** 3-5 things this work will explicitly not do, each with the reason and where it goes instead (later phase, other team, never).
- Read [references/metrics-and-rollout.md](references/metrics-and-rollout.md) when setting baselines, targets, guardrails or leading versus lagging indicators.

**5. Market Segment(s)**
- For whom are we building this? Define segments by the problem or job, not demographics. Note primary versus secondary segments and, just as important, who this is **not** for.
- Segment size with source, and constraints: platform, region, plan tier, accessibility, regulation.
- Link the relevant personas (`user-personas`) rather than re-describing them.

**6. Value Proposition(s)**
- Which customer jobs or needs are we addressing? What will customers gain, which pains will they avoid?
- Compared with the current alternative, including doing nothing, what do we do better? Consider the value curve. Use `value-proposition` for depth.

**7. Solution**
- **7.1 UX / prototypes:** key user flows and links to designs. Cover empty, loading, error, success and permission-denied states, not only the happy path.
- **7.2 Key features and requirements:** user stories grouped by persona, prioritised with **MoSCoW**, each with an ID (R1, R2...) and testable **acceptance criteria** (Given / When / Then or a checklist). Must test: *"If we cut this, does the release still solve the core problem for the primary segment?"* If yes, it is not a Must. Musts should be at most about 60% of the estimated effort so there is room to cut. Read [references/requirements-and-acceptance-criteria.md](references/requirements-and-acceptance-criteria.md) when writing stories, criteria, non-functional requirements or edge cases.
- **7.3 Technology and non-functional requirements** (only what constrains the solution): performance, reliability, security, privacy and data retention, accessibility, localisation, analytics instrumentation, compliance. State the constraint ("p95 under 500 ms"), not the design.
- **7.4 Assumptions and risks:** table of assumption, risk type (value / usability / feasibility / viability), confidence, impact if wrong, how we will validate it, by when, owner. Riskiest first. The cheapest test of the riskiest assumption often belongs before build.
- **7.5 Edge cases:** boundaries, concurrency, migration of existing data, abuse, accessibility, offline and failure behaviour. Each one either gets a requirement or is listed as a non-goal.

**8. Release**
- How long could it take? Use relative timeframes ("about 6 weeks after design sign-off") rather than exact dates, unless a date is a hard external constraint; then state it as one.
- **Phasing:** what goes into the first version (the smallest release that tests the bet) versus later versions.
- **Rollout or experiment plan:** A/B test, staged feature-flag rollout, beta or holdout; the evaluation date; the decision rule (ship / iterate / roll back) with thresholds and kill criteria written before launch; rollback triggers tied to the guardrails.
- **Dependencies and launch readiness:** other teams, support, docs, sales enablement, legal review.
- **Open questions:** question, owner, blocking or non-blocking, needed by. Only genuinely open questions; answer the ones you can from context.

### 4. Write it well

- **Use accessible language.** Write so that anyone in the company can follow it: plain words, short sentences, no unexplained jargon or acronyms.
- **Make it scannable.** Headers and bold text should carry the gist; use tables for metrics, requirements, risks and open questions.
- **Be specific.** Numbers, named segments, concrete examples. Ranges with a source beat false precision.
- **Trace everything to the problem.** Every requirement should serve the problem statement and objective; anything that does not is a candidate non-goal. Any scope added after approval comes with a scope removal or a new timeline.

### 5. Quality gate before delivering

Check each item; fix it or flag it as an open question.

- [ ] The problem statement does not mention the solution and cites at least one `[Data]` or `[Research]` item.
- [ ] "Why now" is answered.
- [ ] One primary metric with baseline, target, timeframe and source; at least one guardrail.
- [ ] 3-5 non-goals with reasons.
- [ ] Every Must passes the Must test; Musts take no more than about 60% of the estimated effort.
- [ ] Every requirement has acceptance criteria a tester could verify without asking the author.
- [ ] Error, empty and edge states are covered or explicitly out of scope.
- [ ] Assumptions are labelled, ranked and each has a validation step.
- [ ] The rollout plan has a decision rule and rollback triggers.
- [ ] Open questions have owners; blocking ones are marked.
- [ ] The summary stands alone; nothing is invented.

### 6. Save the output

If the PRD is substantial (which it usually is), save it as a markdown document named `PRD-[product-name].md`. When updating an existing PRD, bump the version and add a dated change-log entry at the end.

## Reviewing an existing PRD

1. Read the whole document before commenting.
2. Reconstruct, in one sentence each, the **problem**, the **outcome** and the **bet**. If you cannot, that is finding number one.
3. Run the quality gate above and the anti-pattern list below. Rate each section Missing / Weak / Adequate / Strong.
4. Return a verdict (**Ready for build**, **Ready with fixes**, **Needs rework**), then the 3-7 most important issues ranked by impact. Each issue gets the quote or location, why it matters, and a concrete rewrite or question. Close with what is already strong.
5. Do not rewrite the whole PRD unless asked. If the main doubt is the bet itself, hand off to `strategy-red-team`; if it is launch readiness, to `pre-mortem`.

Read [references/prd-review.md](references/prd-review.md) when reviewing, for the section rubric, the detection cues for each anti-pattern and the review output format.

## Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Solution-first PRD | "Users need a dashboard"; the problem is the feature restated | Rewrite as the user's problem plus evidence; list the alternatives considered |
| Unmeasurable goals | "Improve engagement", "delight users" | Metric, baseline, target, timeframe, source |
| Output goals | "Launch X by Q3" as the objective | State the behaviour change X should cause |
| Everything is a Must | No Shoulds or Coulds; nothing can be cut | Apply the Must test; keep Musts at or under ~60% of effort |
| No non-goals | Scope grows in every review | Write 3-5 non-goals with reasons |
| No guardrails | The primary metric can be "won" by hurting something else | Add counter-metrics (retention, support load, latency, revenue) |
| Assumptions as facts | Confident claims with no source | Label them, move them into 7.4, plan validation |
| Spec in disguise | Database schemas and widget choices in the PRD | Keep constraints; move design to `spec-driven-development` |
| Vague acceptance criteria | "Fast", "intuitive", "seamless" | Observable behaviour with thresholds |
| Fake precision | Invented baselines or market sizes | Ranges with a source, or `[TBD: owner]` |
| Frozen PRD | Decisions made in meetings never reach the document | Version, change log, single source of truth |

## Notes

- Be specific and data-driven where possible; link each section back to the overall strategy.
- Flag assumptions clearly so the team can validate them.
- Keep the document concise but complete: a long PRD that nobody reads aligns no one.
- Related skills: `spec-driven-development` (engineering plugin) turns an approved PRD into an engineering spec; `strategy-red-team` attacks the bet; `pre-mortem` triages launch risk; `value-proposition`, `user-personas` and `product-positioning` deepen sections 5-6; `north-star-metric` supplies the metric tree; `prioritization-frameworks` scores a larger backlog; `ab-test-analysis` reads out the experiment.

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
