---
name: prioritization-frameworks
description: "Choose and apply the right prioritization method: Opportunity Score, ICE, RICE, cost of delay (CD3) and WSJF, Kano, MoSCoW, weighted decision matrix, impact/effort. Includes a decision guide by backlog size, evidence and stakeholder dynamics; calibrated scales and worked RICE/ICE examples; Kano and opportunity survey mechanics; a session playbook; pitfalls (false precision, gamed scores, ignored dependencies) and a ranked-output template. Use when ranking a backlog or roadmap candidates, comparing RICE vs ICE vs WSJF, scoring features or opportunities, sequencing work against deadlines, running a prioritization workshop, or challenging a ranking that feels wrong. To map outcome, opportunities and solutions before scoring use opportunity-solution-tree; with no strategy to score against use strategy-kernel first; to choose the metric impact is measured against use north-star-metric."
---

## Prioritization Frameworks Reference

A reference guide to help you select and apply the right prioritization framework for your context, and to produce a ranking that people can trust, argue with and revisit.

### Core Principle

Never allow customers to design solutions. Prioritize **problems (opportunities)**, not features.

Two corollaries:
- **Strategy filters, frameworks rank.** A scoring model ranks options *within* a strategy; it cannot tell you what the strategy is. Remove whatever the guiding policy rules out before scoring anything. If nobody can state what the strategy rules out, fix that first (strategy-kernel).
- **A score is an argument, not an answer.** Every number must trace to evidence or a stated assumption. The value of a framework is the conversation it forces about reach, impact, confidence and cost, not the decimal places it produces.

### Step 1: Frame the Decision

Answer these before picking a method; they decide it more than taste does.

1. **What are the items?** Customer problems (opportunities), solution ideas, requirements for a fixed release, sequencing of committed work, or bets across a portfolio. Never score problems and solutions in the same list.
2. **What outcome are we ranking against?** One metric or objective for the period (north-star-metric, an OKR). Without it, "Impact" means whatever each scorer wants it to mean.
3. **What constraint binds?** Capacity (person-weeks), a date, a budget, a dependency, a skill bottleneck.
4. **What evidence exists?** Usage data, survey data, interview notes, or opinions only.
5. **Who must accept the result?** One team, several teams competing for shared capacity, executives, customers.

### Step 2: Choose the Framework

| Situation | Use | Avoid / caution |
|-----------|-----|-----------------|
| Customer problems from discovery; you can survey ≥ ~30 customers per segment | **Opportunity Score** | ICE/RICE on problems (no solution yet, so no effort) |
| Early stage, < ~20 ideas, little data, speed matters | **ICE** with anchored scales | RICE: reach numbers will be invented |
| 20-200 solution ideas, usage data exists, reach differs a lot between items | **RICE** | Impact/effort 2x2 (throws reach away) |
| Committed work with deadlines, decaying value or queues across teams | **Cost of delay / CD3** (money) or **WSJF** (relative) | RICE: blind to timing |
| Deciding what a feature must include, or which attributes differentiate | **Kano** | Treating Kano categories as a ranking |
| Fixed-scope release negotiated with stakeholders | **MoSCoW**, Musts ≤ ~60% of effort | MoSCoW as a roadmap method |
| A few large, non-comparable options (build vs buy, which market) | **Weighted decision matrix** | Single-number formulas |
| Messy list, one meeting, need triage | **Impact vs effort** 2x2, then a real method on the survivors | Treating the 2x2 as the final answer |
| Bets with very different uncertainty | **Risk vs reward**, then test the highest-value unknowns | Hiding uncertainty inside one score |
| Many stakeholders, political tension | Independent scoring then reveal, or **Buy a Feature** (fixed budget per stakeholder) | Live group scoring (anchoring, loudest voice wins) |
| Personal PM task list | **Eisenhower** | — |

Rules of thumb:
- **Allocate capacity before scoring.** Split capacity into investment buckets by strategy (for example new value / improvements / platform and tech debt / bugs), then rank within each bucket. Platform work rarely wins a RICE contest against customer features, and losing it is a category error, not a verdict.
- **Match effort to backlog size.** Under ~10 items: discuss and stack-rank directly. 10-50: one scoring method. Over 50: triage first (strategy filter or 2x2) and score only the survivors; scoring 200 items produces lazy, uniform scores.
- **Combine methods across levels, never inside one list.** Opportunity Score picks which problems; ICE or RICE picks solutions for a chosen problem; CD3 or WSJF sequences committed work.

### Opportunity Score (Dan Olsen, *The Lean Product Playbook*)

The recommended framework for prioritizing customer problems.

Survey customers on **Importance** and **Satisfaction** for each need (normalize to 0-1 scale; on a 1-5 scale use (x − 1) / 4).

Three related formulas:
- **Current value** = Importance × Satisfaction
- **Opportunity Score** = Importance × (1 − Satisfaction)
- **Customer value created** = Importance × (S2 − S1), where S1 = satisfaction before, S2 = satisfaction after

High Importance + low Satisfaction = highest Opportunity Score = best opportunities. Plot on an Importance vs Satisfaction chart; the upper-left quadrant is the sweet spot. Prioritizes customer problems, not solutions.

Expert notes:
- **Cut by segment before averaging.** A need that is critical for one segment and irrelevant for another averages into the middle and disappears.
- **Phrase needs as outcomes, solution-free:** "Know which invoices are overdue without opening each one", not "Overdue dashboard".
- Tony Ulwick's Outcome-Driven Innovation variant uses the share of respondents rating 4-5 of 5 (top-2-box), divided by 10 to give a 0-10 scale: Opportunity = Importance + max(Importance − Satisfaction, 0). Pick one formula per study; never compare scores across formulas.

Read [references/survey-methods.md](references/survey-methods.md) when designing or analysing an opportunity or Kano survey (question wording, sample size, normalization, worked tables).

### ICE Framework

Useful for prioritizing initiatives and ideas. Considers not only value but also risk and economic factors.

- **I** (Impact) = Opportunity Score × Number of Customers affected (or a 1-10 anchored scale when no survey exists)
- **C** (Confidence) = How confident are we? (1-10). Accounts for risk.
- **E** (Ease) = How easy is it to implement? (1-10). Accounts for economic factors.

**Score** = I × C × E. Higher = prioritize first.

Calibration: anchor every 1-10 scale to something observable before scoring (Impact to expected metric movement, Confidence to the evidence ladder below, Ease to person-weeks). The product form punishes any single low factor; some teams average (I + C + E) / 3 instead, which is more forgiving. Pick one and never mix them.

### RICE Framework

Splits ICE's Impact into two separate factors. Useful for larger teams that need more granularity.

- **R** (Reach) = Number of customers affected per fixed time window (for example per quarter)
- **I** (Impact) = Opportunity Score (value per customer), or Intercom's scale: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal
- **C** (Confidence) = How confident are we? (0-100%); use 100 / 80 / 50%, and treat anything below 50% as a bet to test, not to rank
- **E** (Effort) = How much effort to implement? (person-months across all functions: design, engineering, QA, data, rollout)

**Score** = (R × I × C) / E

Worked mini-example (quarterly reach): automated payment reminders, R 4,000 accounts × I 1 × C 80% / E 1.5 = **2,133**; pay-by-card link, R 4,000 × I 2 × C 50% / E 4 = **1,000**. The pay-by-card link has twice the impact but low confidence and nearly three times the effort; a fake-door test (raises C) and a spike on a hosted payment page (could halve E) are cheaper than debating the score.

Read [references/scoring-calibration.md](references/scoring-calibration.md) when scoring a real backlog with RICE or ICE: anchored scales, the full worked example (including how a strategy filter changes the ranking), sensitivity checks and calibration items.

### Cost of Delay and WSJF

When timing matters, ask "what does it cost us per week not to have this?" (Don Reinertsen: if you quantify only one thing, quantify cost of delay).

- **CD3** = Cost of Delay ÷ Duration. Do the highest CD3 first; this minimizes total delay cost when items compete for the same capacity.
- **Urgency profiles**: *standard* (value lost at a steady rate), *fixed date* (little cost until a deadline, then a cliff: contract, regulation, event), *expedite* (steep, immediate: outage, security), *intangible* (low now, rising later: tech debt, platform). Fixed-date items need explicit scheduling, not just a score.
- **WSJF** (SAFe) = (User-Business Value + Time Criticality + Risk Reduction / Opportunity Enablement) ÷ Job Size, each scored relatively on a modified Fibonacci scale (1, 2, 3, 5, 8, 13, 20), one column at a time, with the smallest item in each column set to 1.

Example: X (CoD 20k/week, 4 weeks, CD3 5), Y (8k/week, 1 week, CD3 8), Z (30k/week, 10 weeks, CD3 3). Order Y-X-Z costs 558k in delay; "biggest value first" (Z-X-Y) costs 700k.

Read [references/cost-of-delay-wsjf.md](references/cost-of-delay-wsjf.md) when sequencing committed work, estimating cost of delay in money, or running WSJF across teams.

### Kano Model (Noriaki Kano)

Classifies attributes by how their presence or absence affects satisfaction: **Must-be** (absence enrages, presence is expected), **Performance** (more is better, linearly), **Attractive** (delights when present, not missed when absent), **Indifferent**, **Reverse**. Ask each respondent a paired functional ("If the product had X, how would you feel?") and dysfunctional ("If it did not have X...") question, classify with the Kano evaluation table, take the most frequent category, and compute Better/Worse coefficients.

Use Kano for **understanding expectations and shaping scope**, not for ranking: ship Must-bes to parity, invest in the Performance attributes your segment weights most, add one or two Attractives to differentiate. Categories decay over time (today's delighter is tomorrow's must-be), so re-survey periodically (about yearly in fast-moving markets). Read [references/survey-methods.md](references/survey-methods.md) for the question pair, evaluation table, coefficients and sample sizes.

### Frameworks at a Glance

| Framework | Best For | Key Insight |
|-----------|----------|-------------|
| Eisenhower Matrix | Personal tasks | Urgent vs Important, for individual PM task management |
| Impact vs Effort | Tasks/initiatives | Simple 2x2 for quick triage, not rigorous for strategic decisions |
| Risk vs Reward | Initiatives | Like Impact vs Effort but accounts for uncertainty |
| **Opportunity Score** | Customer problems | **Recommended.** Importance × (1 − Satisfaction). Normalize to 0-1. |
| Kano Model | Understanding expectations | Must-be, Performance, Attractive, Indifferent, Reverse. For understanding, not prioritizing. |
| Weighted Decision Matrix | Multi-factor decisions | Assign weights to criteria, score each option. Useful for stakeholder buy-in. |
| **ICE** | Ideas/initiatives | Impact × Confidence × Ease. Recommended for quick prioritization. |
| **RICE** | Ideas at scale | (Reach × Impact × Confidence) / Effort. Adds Reach to ICE. |
| Cost of Delay / CD3 | Sequencing committed work | Cost of delay per week ÷ duration. Makes timing and urgency explicit. |
| WSJF | Cross-team backlogs (SAFe) | Relative cost of delay ÷ job size. Small, urgent items float up. |
| MoSCoW | Requirements | Must/Should/Could/Won't. Caution: project management origin; keep Musts ≤ ~60% of effort. |

### Calibrating Scores

False precision is the most common failure. Before scoring:
- **Fix the units.** Reach per the same time window and the same entity (accounts or users or events, never mixed). Effort in person-weeks or person-months across every function, not engineering only.
- **Use discrete values.** 3 / 2 / 1 / 0.5 / 0.25 for impact and 100 / 80 / 50% for confidence. A 73% confidence is a guess pretending to be a measurement.
- **Score confidence from evidence, not feelings:**

| Confidence | Evidence that justifies it |
|------------|----------------------------|
| ≤ 20% | One person's conviction, a pitch-deck idea, "competitor X has it" |
| 50% | Anecdotes: a few customer requests, sales feedback, analogous products |
| 80% | Systematic evidence of the problem (consistent across ≥ 5 interviews, or usage data) plus some signal on the solution (prototype test, fake door, survey) |
| 100% | Experiment or pilot result, or launch data from a comparable change |

- **Anchor with calibration items.** Score two or three already-shipped items whose outcome you know; new scores are relative to those.
- **Run a sensitivity check.** Which items change rank if any single estimate is off by 2x? Robust items are decided; fragile ones need a cheaper test, not a longer meeting.

### Running a Prioritization Session

1. **Pre-work (async):** state the decision, the outcome metric, the strategy filters and the capacity; list candidates as problems or as solutions (not both); attach the evidence for each.
2. **Independent scoring:** each scorer scores alone, then reveal together (as in planning poker). This defeats anchoring and the loudest-voice effect.
3. **Discuss only the variance.** Spend the meeting on items where scores diverge; divergence usually means different assumptions about reach, the segment or scope. Write the resolved assumption down.
4. **Check dependencies and fixed dates.** An item that unblocks three others or has a hard deadline may jump the ranking; record why.
5. **Sanity-check the top 10** against strategy and gut. If the ranking "feels wrong", find which estimate creates the feeling and examine that estimate; do not override silently.
6. **Draw the cut line** at capacity, publish the "not now" list with reasons, and set revisit triggers.

Read [references/session-and-output.md](references/session-and-output.md) when facilitating a session or writing up the result: agenda, facilitator script, stakeholder tactics and the full output template.

### Pitfalls

- **False precision:** RICE 1,247 vs 1,198 is a tie. Treat scores within ~20% as equal and decide on strategy fit, dependencies or learning value.
- **Gaming:** scorers inflate reach and impact for their own items. Counter with evidence-linked scores, a calibration owner, and published assumptions people can challenge.
- **Ignoring strategy fit:** a broad, shallow item (dark mode for everyone) outranks a deep one that moves the quarter's outcome. Filter by strategy first.
- **Ignoring dependencies and sequencing:** scores assume independent items; real work has enablers, shared components and fixed dates.
- **Effort = engineering only:** forgets design, data, legal, rollout, support and migration; small-looking items get systematically over-ranked.
- **Confidence as a fudge factor:** low confidence should trigger a test, not just a lower score. The most valuable action is often to raise confidence on a high-potential item.
- **Comparing scores across teams or quarters:** scales drift; scores only rank within one scoring session.
- **Scoring solutions before validating problems:** a perfectly ranked list of features for a problem nobody has.
- **Never revisiting:** rankings decay as evidence arrives. Re-score at defined triggers, not on the loudest request.

### Output Template

```
## Prioritization: [scope], [period]
Decision: [what we are deciding] | Outcome metric: [metric] | Capacity: [x person-weeks]
Method: [framework] because [situation from Step 2]
Strategy filters applied: [what was removed and why]
| Rank | Item | Scores (inputs) | Score | Key assumption | Evidence |
Cut line: items 1-N fit capacity. Dependencies / fixed dates: [...]
Fragile rankings (sensitivity): [item: estimate that would flip it, cheapest test]
Not now, and why: [...]
Revisit when: [date or trigger]
```

---

### Templates

- [Opportunity Score intro (PDF)](https://drive.google.com/file/d/1ENbYPmk1i1AKO7UnfyTuULL5GucTVufW/view)
- [Importance vs Satisfaction Template — Dan Olsen (Google Slides)](https://docs.google.com/presentation/d/1jg-LuF_3QHsf6f1nE1f98i4C0aulnRNMOO1jftgti8M/edit#slide=id.g796641d975_0_3)
- [ICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1LUfnsPolhZgm7X2oij-7EUe0CJT-Dwr-/edit?usp=share_link&ouid=111307342557889008106&rtpof=true&sd=true)
- [RICE Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1S-6QpyOz5MCrV7B67LUWdZkAzn38Eahv/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
