---
name: create-prd
description: "Create or review an evidence-first Product Requirements Document in 8 sections, lean by default (1-2 pages), full on request: summary, contacts and decision owner, background (problem evidence, why now), objective (primary metric with baseline and target, guardrails, non-goals), market segments, value propositions (6-part JTBD, one per segment), solution (UX states, MoSCoW requirements with acceptance criteria, edge cases, ranked assumptions) and release (rollout or experiment plan, decision rule, kill criteria, open questions). Includes a review rubric and anti-patterns. Use when writing a PRD, feature brief or one-pager, scoping a feature with goals and non-goals, defining success metrics or acceptance criteria, or reviewing or tightening a PRD. For an engineering spec use spec-driven-development (engineering plugin); to attack the bet use strategy-red-team; for launch risk use pre-mortem; for value proposition and personas in depth use value-proposition and user-personas."
---

# Create a Product Requirements Document

> Includes material adapted from [anthropics/knowledge-work-plugins `write-spec`](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/product-management/skills/write-spec) (Apache-2.0, see `LICENSE.txt`). **Modified by ultimate-skills:** its priority tests, metric, acceptance-criteria and scope guidance were rewritten and merged into this 8-section template (base skill: phuryn/pm-skills, MIT).

## Purpose

You are an experienced product manager responsible for creating, or reviewing, the Product Requirements Document (PRD) for the product or feature the user describes. The PRD is the authoritative statement of **what problem we are solving, for whom, how we will know it worked, and what we will not do**. It aligns stakeholders and guides design and engineering. It is not the engineering spec: it constrains the *how* but does not design it.

## Context

A PRD is a decision document. Its job is to make a bet explicit and testable: *we believe that building X for segment Y will move metric Z from A to B, and here is the evidence*. A well-structured PRD lets engineers, designers, leadership and go-to-market read the same page and reach the same answer.

**Lean by default.** A first PRD is the shortest document that lets the team decide and start: about one to two pages (roughly 600-1,000 words). That length is a guide, not a limit; a PRD with two or three segments can run longer, but every section stays as short as it can be. Write the full version when the user asks for it.

- **Complete means no gap that blocks a decision about the first version**, not every question answered. The prompts under each section below are a checklist to pick from: answer the ones that matter for this initiative and skip the rest.
- **A section with little to say gets a line or two.** If you do not know the contacts, leave that section out rather than listing roles to fill in later. Never pad a section or fill it with a bare "TBD"; a specific unknown value gets an inline `[TBD: owner]` and an entry in the open questions.
- **Market segments (5) and value propositions (6) are always included**, even in the shortest version: they say who has the problem and why they would care.

**Right-size the document** before writing:

| Situation | Format |
|---|---|
| Default: a first draft, or a small, reversible change | Lean PRD: all 8 sections, each a line or a short table; Contacts optional; requirements are the first version's Musts, a line or two each with one acceptance criterion |
| The user asks for detail | Full PRD: every subsection below, with the tables in the template |
| New capability across several teams, a customer-facing commitment, or hard to reverse | Lean PRD first unless the user asked for detail; in your reply, recommend the full version and say which sections it would add |
| The problem itself is unproven (no evidence anyone has it) | No PRD yet. Run discovery first with `interview-script` and `opportunity-solution-tree`, then come back |

**Modes:** *Create* (new PRD), *Review* (critique an existing PRD, see "Reviewing an existing PRD" below), *Update* (revise after decisions or new evidence; keep a change log).

## Instructions

### 1. Gather information: evidence before solution

- **Start from what the user gave you.** If they provide files (research, tickets, analytics exports, earlier PRDs, designs), read them first.
- **Ask before drafting when a core input is missing.** If the problem, the target users, or how success will be measured is missing, stop and ask first: up to three short questions in one message, most important first, and no PRD in that reply. Ask only what only the user knows (their evidence of the problem, their users, their success metric, hard constraints, who decides); research what the web can answer. Write the PRD after the answers. Write it without them only if the user tells you to go ahead, and then mark those gaps as `[Assumption]` with entries in 7.4.
- **Research freely when it helps.** Search the web for the market, competitors and alternatives, regulations, or what changed recently, and read any sources the user points to. Use what you find to sharpen decisions: why now, who the segment is, what we do better than the alternatives. Cite the source next to the claim. A finding goes into the document only if it changes a decision; anything else useful goes in your reply as notes, so the PRD stays lean.
- **Never invent data, quotes, customer names or baselines.** A visible gap is better than a plausible fiction. Mark a specific unknown inline as `[Assumption]` or `[TBD: owner]` and carry it into 7.4 or the open questions.

Label every factual claim with its evidence type:

| Label | Meaning | Must include |
|---|---|---|
| `[Data]` | Measured: analytics, support volume, revenue, logs | Source, date range |
| `[Research]` | Qualitative: interviews, usability tests, sales calls | n, segment, date |
| `[Assumption]` | Believed, not yet shown | An entry in section 7.4 with a validation plan |

### 2. Think step by step before writing

This thinking stays out of the document.

- **Problem:** Can you state the problem without naming the solution? Who has it, how often, how do they cope today, what does it cost them and us?
- **Outcome:** What user behaviour or business metric changes if we succeed? By how much, by when?
- **Bet:** Why is this solution the best way to reach that outcome? Which alternatives were considered and why rejected?
- **Risks:** Which of the four product risks is largest: value (will they want it), usability (can they use it), feasibility (can we build it), viability (does it work for the business: legal, cost, sales, brand)?
- **Scope:** What is the smallest first version that tests the bet?

### 3. Apply the PRD template

Write these 8 sections. The lean version answers only the prompts that matter for this initiative; the full version works through all of them. Read [references/prd-template.md](references/prd-template.md) when drafting, for the copy-ready template; read [references/example-prd.md](references/example-prd.md) when you need to see the expected depth and tone.

**1. Summary** (2-3 sentences)
- Problem, for whom, why now, the proposed bet, and the one metric that will tell us. A busy executive should get the gist in 30 seconds.
- Status (draft / in review / approved), version, last updated.

**2. Contacts** (optional in the lean version; leave it out rather than listing placeholder roles)
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
- In the lean version: one primary metric, one guardrail, and the non-goals as a short list.
- Read [references/metrics-and-rollout.md](references/metrics-and-rollout.md) when setting baselines, targets, guardrails or leading versus lagging indicators.

**5. Market Segment(s)** (always included)
- For whom are we building this? Define segments by the problem or job, not demographics. Note primary versus secondary segments and, just as important, who this is **not** for.
- Focus the first version on two or three segments at most; the rest can wait for later versions.
- Segment size with source, and constraints: platform, region, plan tier, accessibility, regulation.
- Link the relevant personas (`user-personas`) rather than re-describing them.

**6. Value Proposition(s)** (always included; one per segment from section 5)
- Use the 6-part JTBD value proposition template by Paweł Huryn and Aatir Abdul Rauf. It starts from the customer, not the product, and makes you name the alternatives:
  - **Who:** the segment from section 5
  - **Why:** the job they are trying to get done, and the problem in the way
  - **What before:** how they do it today, and what hurts about it
  - **How:** how our solution gets the job done (the key capability; section 7 has the features)
  - **What after:** the improved outcome, and what becomes possible that was not before
  - **Alternatives:** what they would use without us, including doing nothing, and why they would choose us instead
- Finish with a value proposition statement of one or two sentences. In the lean version each part is a line or two; the full version labels the evidence for each part and can add a value curve against the alternatives. Use `value-proposition` for the full method (evidence labels, switching forces, fit check, worked example).
- **This section is the spine of the PRD:** section 7 delivers the How, and the primary metric in section 4 measures the What after. If they do not line up, fix that before anything else.

**7. Solution**
- **7.1 UX / prototypes:** key user flows and links to designs. Cover empty, loading, error, success and permission-denied states, not only the happy path.
- **7.2 Key features and requirements:** user stories grouped by persona, prioritised with **MoSCoW**, each with an ID (R1, R2...) and testable **acceptance criteria** (Given / When / Then or a checklist). Must test: *"If we cut this, does the release still solve the core problem for the primary segment?"* If yes, it is not a Must. Musts should be at most about 60% of the estimated effort so there is room to cut. In the lean version, list the first version's Musts, a line or two each with one acceptance criterion; the full version adds the Shoulds, Coulds and Won'ts. Read [references/requirements-and-acceptance-criteria.md](references/requirements-and-acceptance-criteria.md) when writing stories, criteria, non-functional requirements or edge cases.
- **7.3 Technology and non-functional requirements** (only what constrains the solution): performance, reliability, security, privacy and data retention, accessibility, localisation, analytics instrumentation, compliance. State the constraint ("p95 under 500 ms"), not the design.
- **7.4 Assumptions and risks:** table of assumption, risk type (value / usability / feasibility / viability), confidence, impact if wrong, how we will validate it, by when, owner. Riskiest first. The cheapest test of the riskiest assumption often belongs before build.
- **7.5 Edge cases:** boundaries, concurrency, migration of existing data, abuse, accessibility, offline and failure behaviour. Each one either gets a requirement or is listed as a non-goal.

**8. Release**
- How long could it take? Use relative timeframes ("about 6 weeks after design sign-off") rather than exact dates, unless a date is a hard external constraint; then state it as one.
- **Phasing:** what goes into the first version (the smallest release that tests the bet), what comes later, and what we are explicitly not doing (point to the non-goals).
- **Rollout or experiment plan:** A/B test, staged feature-flag rollout, beta or holdout; the evaluation date; the decision rule (ship / iterate / roll back) with thresholds and kill criteria written before launch; rollback triggers tied to the guardrails.
- **Dependencies and launch readiness:** other teams, support, docs, sales enablement, legal review.
- **Open questions:** question, owner, blocking or non-blocking, needed by. Only genuinely open questions; answer the ones you can from context.

### 4. Write it well

- **Use accessible language.** Write so that anyone in the company can follow it: plain words, short sentences, no unexplained jargon or acronyms.
- **Make it scannable.** Headers and bold text should carry the gist; use tables for metrics, requirements, risks and open questions.
- **Be specific.** Numbers, named segments, concrete examples: a number or a named user group beats an adjective. Ranges with a source beat false precision.
- **Trace everything to the problem.** Every requirement should serve the problem statement and objective; anything that does not is a candidate non-goal. Any scope added after approval comes with a scope removal or a new timeline.

### 5. Quality gate before delivering

Check each item; fix it or flag it as an open question. In the lean version an item can be met in a single line.

- [ ] The problem statement does not mention the solution and cites at least one `[Data]` or `[Research]` item.
- [ ] "Why now" is answered.
- [ ] One primary metric with baseline, target, timeframe and source; at least one guardrail.
- [ ] 3-5 non-goals with reasons.
- [ ] Market segments are present (two or three at most for the first version), each with a 6-part value proposition; the Solution delivers each How and the primary metric measures the What after.
- [ ] Every Must passes the Must test; Musts take no more than about 60% of the estimated effort.
- [ ] Every requirement has acceptance criteria a tester could verify without asking the author.
- [ ] Error, empty and edge states are covered or explicitly out of scope.
- [ ] Assumptions are labelled, ranked and each has a validation step.
- [ ] The rollout plan has a decision rule and rollback triggers.
- [ ] Open questions have owners; blocking ones are marked.
- [ ] The summary stands alone; nothing is invented.
- [ ] No section is padded or filled with placeholders; the lean version is about one to two pages, and anything longer earns its length.

### 6. Save the output

Save the PRD as a markdown document named `PRD-[product-name].md`. When updating an existing PRD, bump the version and add a dated change-log entry at the end.

### 7. Say what you left out

In your reply, not in the document, add one short line listing what you skipped on purpose (for example: competitive analysis, detailed UX flows, the rollout plan, sections cut to a line), so the user can ask you to expand any of it. Research notes that did not change a decision go in the reply too.

## Reviewing an existing PRD

1. Read the whole document before commenting.
2. Reconstruct, in one sentence each, the **problem**, the **outcome** and the **bet**. If you cannot, that is finding number one.
3. Run the quality gate above and the anti-pattern list below. Rate each section Missing / Weak / Adequate / Strong.
4. Return a verdict (**Ready for build**, **Ready with fixes**, **Needs rework**), then the 3-7 most important issues ranked by impact, gaps that block a decision about the first version first. Each issue gets the quote or location, why it matters, and a concrete rewrite or question. Then list what could be cut without losing anything the team needs. Close with what is already strong.
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
| Padded PRD | Placeholder roles, sections of "TBD", boilerplate in every section; pages no decision needs | Cut to the shortest document that lets the team decide; move unknowns into 7.4 or the open questions |
| Broken spine | The value proposition's How is not in the Solution, or no metric measures its What after | Realign sections 4, 6 and 7 before polishing anything else |

## Notes

- Be specific and data-driven where possible; link each section back to the overall strategy.
- Flag assumptions clearly so the team can validate them.
- Lean is the default; detail is on request. A long PRD that nobody reads aligns no one.
- Non-goals matter as much as goals: say what the first version will not do.
- Related skills: `spec-driven-development` (engineering plugin) turns an approved PRD into an engineering spec; `strategy-red-team` attacks the bet; `pre-mortem` triages launch risk; `value-proposition`, `user-personas` and `product-positioning` deepen sections 5-6; `north-star-metric` supplies the metric tree; `prioritization-frameworks` scores a larger backlog; `ab-test-analysis` reads out the experiment.

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
