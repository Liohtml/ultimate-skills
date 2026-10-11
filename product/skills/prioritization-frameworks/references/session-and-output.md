# Running a Prioritization Session and Writing Up the Result

Read this when preparing or facilitating a prioritization session, handling stakeholder dynamics in one, or writing the output.

## Contents
- Roles
- Pre-work checklist
- 90-minute agenda
- Facilitator lines
- Stakeholder tactics
- Async / remote variant
- Full output template with a filled example
- After the session

## Roles

| Role | Responsibility |
|------|----------------|
| Decision owner | Makes the call if the group does not converge. Named before the session, not during it. |
| Facilitator | Runs the agenda and protects the method; does not score their own items. |
| Scorers | People who hold evidence: PM, design, engineering lead, data/analytics, a customer-facing voice (sales or CS). 4-7 people. |
| Calibration owner | Keeps scales consistent across sessions; often the facilitator or a product ops role. |

## Pre-work checklist (send 2-3 days before)

- [ ] The decision in one sentence ("What we build next quarter in the get-paid-faster bucket").
- [ ] Outcome metric and capacity (person-weeks or person-months).
- [ ] Strategy filters: what the guiding policy rules out. Items failing them are removed before the session, with a note.
- [ ] Candidate list in one shape: all problems or all solutions. Each with a one-line description and its evidence.
- [ ] Method and scales, with two or three calibration items already scored.
- [ ] Independent scoring sheet: each scorer scores alone and submits before the meeting.
- [ ] Known dependencies and fixed dates listed.

## 90-minute agenda

| Time | Block | Output |
|------|-------|--------|
| 0-10 | Frame: decision, outcome, capacity, filters, method; walk through the calibration items | Shared understanding of scales |
| 10-25 | Silent scoring for anyone who did not pre-score; then reveal all scores at once | Score matrix with variance per item |
| 25-60 | Discuss only high-variance items, about 5 minutes each. Each discussion ends with a written assumption ("Reach assumes only accounts with overdue invoices") and an agreed score | Resolved scores with assumptions |
| 60-75 | Dependencies, fixed dates, capacity: draw the cut line | Draft ranked list with cut line |
| 75-85 | Sanity check: top 10 against strategy; run the sensitivity question on fragile items | Fragile items and their tests |
| 85-90 | Decision owner confirms; "not now" list; revisit triggers; owners for tests | Decision record |

## Facilitator lines

- "Scores differ by 3x here. What are you each assuming about who this reaches?"
- "What evidence is this confidence based on? Which row of the ladder?"
- "If this item were half the effort, would it change the cut line? If not, let's not debate the estimate."
- "What would have to be true for #11 to beat #1?"
- "This feels wrong to several people. Which single number creates that feeling?"
- "We have two items within 20% of each other: that's a tie. What breaks it: strategy fit, dependencies, or learning value?"
- "Who will run the test that would settle this, and by when?"

## Stakeholder tactics

| Situation | Tactic |
|-----------|--------|
| Senior opinion overrides the scores | Apply the same scale to their item and ask for the evidence behind each factor. If they still override, record it as a decision-owner call with the reason, not as a score. |
| "Everything is P1" | Force-rank, or use Buy a Feature: each stakeholder gets a budget of about half the total cost of all items, so they must pool budgets to fund anything large. |
| "A big deal needs X" | Quantify as cost of delay: deal size × probability, plus the date. Then it competes openly, usually as a fixed-date item. |
| Pet project scored generously by its sponsor | Score one column at a time with everyone's scores visible; ask the sponsor to name what drops below the cut line if it goes in. |
| Engineering wants debt and platform work in the list | Agree a capacity share for that bucket first; rank debt items against each other, not against features. |
| Persistent disagreement | The decision owner decides; record the dissent and the evidence that would reopen the question. |

## Async / remote variant

1. Share the pre-work and a scoring sheet; each scorer submits independently by a deadline.
2. The facilitator computes variance and posts only high-variance items for a threaded discussion with a 48-hour window.
3. A 30-minute call resolves what is left, draws the cut line and confirms the decision.

## Full output template

```
## Prioritization: [scope], [period]

**Decision:** [one sentence]
**Decision owner:** [name] | **Date:** [date]
**Outcome metric:** [metric and current value]
**Capacity:** [x person-months] | **Buckets:** [e.g. 60% new value / 20% improvements / 20% platform]
**Method:** [framework] because [situation: data available, backlog size, stakeholder dynamics]
**Scales:** [link or summary; calibration items used]

### Removed by strategy filter
- [Item]: [the guiding-policy reason]

### Ranking
| Rank | Item | Inputs (R / I / C / E or equivalent) | Score | Key assumption | Evidence |
|------|------|--------------------------------------|-------|----------------|----------|

**Cut line:** items 1-N fit capacity.
**Dependencies and fixed dates:** [item → blocks / needed by date]

### Fragile rankings
| Item | Estimate that would flip it | Cheapest test | Owner | Due |

### Not now
- [Item]: [why; what evidence would bring it back]

### Revisit
[Date] or when: [triggers: test results, capacity change, strategy change, new evidence on a fragile item]
```

### Filled example (abridged)

```
## Prioritization: Get-paid-faster bucket, Q3
Decision: What we build in Q3 to reduce median days-to-paid.
Outcome metric: median days-to-paid, currently 34 days | Capacity: 6 person-months
Method: RICE, because reach varies widely and usage data exists.

Removed by strategy filter
- Dark mode: no path to days-to-paid.
- Bulk CSV import: activation bucket; ranked there.

Ranking
| 1 | Automated payment reminders | 4,000 / 1 / 80% / 1.5 | 2,133 | Pilot effect generalises | 50-account pilot: 34 → 27 days |
| 2 | Pay-by-card link | 4,000 / 2 / 50% / 4 | 1,000 | Payers want card payment | Sales requests only |
| 3 | Accounting sync | 900 / 3 / 50% / 6 | 225 | Sync shortens reconciliation | Interviews only |
Cut line: item 1 now (1.5 PM); item 2 pending test.

Fragile rankings
| Pay-by-card link | Confidence 50% → 80%, effort 4 → 2 | Fake door on invoice page; 2-day spike on hosted payment page | PM / Eng lead | end of sprint 1 |

Not now
- Accounting sync: last even at 100% confidence and half the effort.

Revisit: after the fake-door test, or at mid-quarter review.
```

## After the session

- Publish the decision record where the people affected will see it, including the "not now" list and its reasons; unexplained "no" answers come back as escalations.
- Feed fragile items into discovery or experiments with owners and dates.
- Re-score when a trigger fires, not on the next loud request.
- After shipping, compare actual reach and impact with the estimates; use the gaps to recalibrate the scales next time.
