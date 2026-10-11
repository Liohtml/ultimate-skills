# Scoring Calibration: RICE, ICE and Other Scored Methods

Read this when scoring a real backlog. It covers anchored scales, two fully worked examples, sensitivity checks and calibration notes for the other scored methods. All products, numbers and outcomes below are illustrative.

## Contents
- Shared calibration rules
- RICE: scales and a worked example
- ICE: anchored scales and a worked example
- Sensitivity check procedure
- Weighted decision matrix, MoSCoW and impact/effort calibration

## Shared calibration rules

1. **One outcome per scoring session.** Write the outcome metric at the top of the sheet. "Impact" is impact on that metric, nothing else.
2. **One time window and one entity for reach.** Per quarter is the usual window. Count accounts *or* users *or* events; never mix. Use a number you can query, or write down the assumption that produced it.
3. **Effort covers everyone.** Design, engineering, QA, data, legal, docs, rollout, support enablement, migration. Engineering-only estimates systematically over-rank items with hidden non-engineering work.
4. **Discrete values only.** Fewer allowed values means less false precision and faster scoring.
5. **Evidence column is mandatory.** For every score, one line: the source (query, interview count, test result) or "assumption".
6. **Score one column at a time across all items**, not one item at a time across all columns. Relative judgements within a column are more consistent than absolute judgements per item.
7. **Calibration items first.** Score two or three shipped items whose outcome you know. If a shipped item that moved the metric by 2 points scores lower than a speculative one, the scale is being used inconsistently.

## RICE

### Scales

| Factor | Unit / allowed values | Anchors |
|--------|------------------------|---------|
| Reach | Entities per quarter (number) | Query it: accounts that hit the relevant step, page or state last quarter. For new surfaces, use the funnel stage that will feed it. |
| Impact | 3 / 2 / 1 / 0.5 / 0.25 | 3 massive: changes whether the job gets done at all. 2 high: removes a major step or failure. 1 medium: noticeable improvement. 0.5 low. 0.25 minimal: cosmetic. Or use Opportunity Score per customer if surveyed. |
| Confidence | 100% / 80% / 50% | See the evidence ladder in SKILL.md. Below 50%: do not rank; send to discovery or a test. |
| Effort | Person-months, all functions | Round to 0.5 below 1 month, whole months above. Estimate a range; score the midpoint and note the high end. |

### Worked example

Context: a B2B invoicing product, 12,000 active accounts. Quarter outcome: **reduce median days-to-paid for invoices sent through the product**. Capacity: about 6 person-months.

| Item | Reach / qtr | Impact | Conf. | Effort (PM) | RICE | Evidence |
|------|-------------|--------|-------|-------------|------|----------|
| A. Automated payment reminders | 4,000 | 1 | 80% | 1.5 | 2,133 | Reach: accounts with ≥ 1 overdue invoice last quarter. Conf.: manual-reminder pilot with 50 accounts cut median days-to-paid from 34 to 27 |
| B. Pay-by-card link in invoice | 4,000 | 2 | 50% | 4 | 1,000 | Requests from sales; no usage data |
| C. Dark mode | 6,000 | 0.25 | 80% | 1 | 1,200 | Top-voted request on the feedback board |
| D. Bulk CSV client import | 1,800 | 1 | 80% | 2 | 720 | Funnel: 40% of new accounts stall at manual client entry |
| E. Accounting-software two-way sync | 900 | 3 | 50% | 6 | 225 | Reach: accounts with the integration connected one-way |

Arithmetic check for A: 4,000 × 1 × 0.8 / 1.5 = 2,133.

**Lesson 1: filter by strategy before ranking.** Unfiltered, dark mode ranks second: broad and shallow beats deep. It has no plausible path to days-to-paid, so it leaves this list. CSV import is real value for a different outcome (activation); move it to that bucket and rank it there.

**Lesson 2: read the ranking as a set of questions.** In the "get paid faster" bucket, the order is A (2,133), B (1,000), E (225).
- B is fragile. At 80% confidence it scores 1,600; if a hosted payment page halves effort to 2 PM it scores 2,000 (2,000 vs 2,133 is a tie under the ~20% rule). Two cheap actions decide B: a fake-door test on the invoice page and a two-day spike on the hosted approach.
- E is robust. Even at 100% confidence and half the effort it scores 900 (900 × 3 × 1 / 3), still last. Put it on the "not now" list with that reason.

**Resulting plan:** build A (1.5 PM); run the B test and spike in the same sprint; decide B with the new numbers; E not now; D goes to the activation bucket review.

## ICE

### Anchored 1-10 scales

| Score | Impact (expected lift on the target metric, e.g. weekly activation rate) | Confidence (evidence) | Ease (all-function effort) |
|-------|------------------|------------|------|
| 9-10 | ≥ +5 points | Experiment or launch result | ≤ 1 day |
| 7-8 | +2 to +5 points | Systematic evidence (≥ 5 consistent interviews, usage data) plus a solution signal | ≤ 1 week |
| 5-6 | +1 to +2 points | Anecdotes: several requests, sales or support reports | ≤ 2 weeks |
| 3-4 | +0.5 to +1 point | Trend, competitor has it, stakeholder consensus | ≤ 1 month |
| 1-2 | < +0.5 points | One person's conviction | > 1 month |

Confidence ladders of this kind follow the spirit of Itamar Gilad's Confidence Meter: confidence is earned by the type of evidence, not asserted.

Upstream variant: Impact = Opportunity Score × number of customers. Multiplying every item's impact by the same constant does not change an I × C × E ranking, so raw values are fine for the product form; for the average form, rescale impact to 1-10 first.

### Worked example

Context: a consumer habit-tracking app; outcome: week-1 activation.

| Idea | I | C | E | I × C × E | Average |
|------|---|---|---|-----------|---------|
| Pre-fill the first habit from onboarding answers | 7 | 6 | 8 | 336 | 7.0 |
| Day-2 push notification with streak preview | 5 | 7 | 9 | 315 | 7.0 |
| Social login | 3 | 8 | 8 | 192 | 6.3 |
| Onboarding rebuilt as a 3-step checklist | 7 | 5 | 4 | 140 | 5.3 |
| AI coach chat | 8 | 2 | 2 | 32 | 4.0 |

Read-outs:
- The first two ideas tie on the average form and separate slightly on the product form; treat them as a tie and run both (both are cheap).
- The product form crushes the AI coach (32) because one factor is 2. That is correct if the goal is to avoid untested big bets this cycle, and wrong if the team has protected capacity for learning. If it does, move the idea to discovery and ask what the cheapest test of "users want coaching inside a habit app" is, rather than ranking it.
- Social login has high confidence but low impact on activation: it helps sign-up conversion, a different metric. Check that each idea's impact really is on the stated outcome.

## Sensitivity check procedure

1. For each item in the top ~10, vary each estimate by 2x in the unfavourable direction (halve reach, impact or confidence; double effort) one at a time.
2. Mark an item **robust** if it stays above the cut line under every single change, **fragile** if one change moves it across the line.
3. For each fragile item, name the estimate that flips it and the cheapest way to firm it up (query, five interviews, fake door, spike).
4. Report fragile items explicitly in the output. Deciding robust items now and testing fragile ones is usually faster than debating all of them.

## Other scored methods

### Weighted decision matrix
- Choose 4-6 criteria tied to strategy; set weights (summing to 100) **before** anyone sees the options, otherwise weights get reverse-engineered to favour a preferred option.
- Separate **gates** (must-pass: legal, security, budget ceiling) from weighted criteria; an option failing a gate is out regardless of score.
- Score 1-5 with a written anchor for 1, 3 and 5 per criterion.
- Test weight sensitivity: if moving any weight by 10 points changes the winner, the decision rests on that weight; discuss the weight, not the scores.

### MoSCoW
- Define "Must" strictly: the release is pointless, unsafe or illegal without it.
- Keep Musts at or below ~60% of estimated effort (DSDM guidance) so Shoulds and Coulds act as contingency.
- Record Won'ts explicitly with "this release" or "ever"; an unrecorded Won't comes back every meeting.

### Impact vs effort 2x2
- Use only for triage. Place items relative to each other, not on absolute scales.
- Be suspicious of a crowded "quick wins" quadrant: it usually means effort is underestimated or impact is overestimated. Spot-check two items with a real estimate.
