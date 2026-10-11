# Cost of Delay, CD3 and WSJF

Read this when sequencing committed work, when deadlines or decaying value matter, or when several teams pull from one backlog. All numbers below are illustrative.

## Contents
- Why cost of delay
- Estimating cost of delay in money
- CD3: worked sequencing example
- Urgency profiles and how to schedule each
- WSJF: rules and a worked example
- Pitfalls

## Why cost of delay

Most scoring methods ask "how valuable is this?". Cost of delay asks "how much value do we lose for every week this is not done?". The question exposes two things value scores hide: **timing** (a feature worth a lot in March may be worth little in June) and **queues** (every week an item waits, its value is not being earned). Don Reinertsen's advice in *The Principles of Product Development Flow*: if you quantify only one thing, quantify cost of delay.

## Estimating cost of delay in money

Order of magnitude is enough; ranges are fine. Add up the components that apply, per week:

| Component | Question | Typical inputs |
|-----------|----------|----------------|
| Revenue gained | What new or expansion revenue starts once it ships? | Deals blocked on it × probability × value, conversion lift × traffic × price |
| Revenue protected | What churn or downgrade does it prevent? | Accounts at risk × churn reduction × lifetime value |
| Cost avoided | What cost do we keep paying until it ships? | Support hours, manual operations, infrastructure, penalties |
| Risk reduced | What expected loss does it remove? | Probability of the event per week × impact |
| Option value | What does it unlock that is otherwise blocked? | Value of the items it enables, discounted for their own uncertainty |

Example, automated payment reminders for an invoicing product:
- Revenue protected: churn interviews name late payment as a reason to leave; estimate a 0.2-point monthly churn reduction on 4,000 affected accounts, so about 8 accounts a month, roughly 2 a week. At about 960 lifetime value each, about 1.8k per week.
- Cost avoided: about 60 support tickets a week on chasing payments, about 10 minutes each at 40 per hour, about 0.4k per week.
- **Cost of delay ≈ 2.2k per week.** The uncertainty is in the churn estimate; state it as an assumption.

## CD3: cost of delay divided by duration

Do the item with the highest CD3 first. When items compete for the same capacity, this ordering minimizes total delay cost (it is the weighted-shortest-job-first rule from scheduling theory).

| Item | Cost of delay / week | Duration (weeks) | CD3 |
|------|----------------------|------------------|-----|
| X | 20k | 4 | 5 |
| Y | 8k | 1 | 8 |
| Z | 30k | 10 | 3 |

Total delay cost by sequence (each item accrues cost of delay until it is done):

| Sequence | Finish weeks | Delay cost | Total |
|----------|--------------|------------|-------|
| Y, X, Z (by CD3) | 1, 5, 15 | 8 + 100 + 450 | **558k** |
| X, Y, Z | 4, 5, 15 | 80 + 40 + 450 | 570k |
| Z, X, Y (biggest value first) | 10, 14, 15 | 300 + 280 + 120 | 700k |

"Biggest value first" feels right and costs 142k more than CD3 order. Small, urgent items go first because they stop accruing cost quickly.

Duration means calendar time with the staffing you will actually use. If an item can be split so that part of its value ships early, split it: each slice gets its own, usually higher, CD3.

## Urgency profiles

| Profile | Shape | Examples | How to schedule |
|---------|-------|----------|-----------------|
| Standard | Value lost at a steady rate | Most product improvements | Rank by CD3 |
| Fixed date | Near-zero cost until a date, then a cliff | Regulation deadline, contract term, trade show, a deal closing | Work back from the date: latest start = date − duration − buffer. Schedule explicitly, then rank the rest around it |
| Expedite | Steep and immediate | Outage, security incident, data loss | Interrupts planned work; cap expedites in progress (for example one at a time) or everything becomes "expedite" |
| Intangible | Low now, rising later | Tech debt, platform, tooling | Fund from a fixed capacity share; re-estimate when the curve starts to rise (every change getting slower, incidents increasing) |
| Short-life / peak | Value concentrated in a window | Seasonal feature, competitor's launch window | Cost of delay includes the lost peak; missing the window can make the item worthless |

## WSJF (Scaled Agile Framework)

**WSJF = Cost of Delay ÷ Job Size**, with Cost of Delay = User-Business Value + Time Criticality + Risk Reduction / Opportunity Enablement.

Rules that keep it honest:
- Score with a modified Fibonacci scale: 1, 2, 3, 5, 8, 13, 20.
- Score **one column at a time** across all items. In each column, set the smallest item to 1 and score the others relative to it.
- Job size stands in for duration. That only works if items are staffed similarly; if a large item can be parallelized across teams, use expected duration instead.
- Scores are relative to this backlog and this session; never compare WSJF across sessions or teams.

### Worked example

| Item | Business value | Time criticality | RR / OE | Cost of delay | Job size | WSJF |
|------|----------------|------------------|---------|---------------|----------|------|
| Onboarding checklist | 3 | 1 | 1 | 5 | 1 | 5.0 |
| Automated payment reminders | 8 | 3 | 2 | 13 | 3 | 4.3 |
| Enterprise SSO (deal closes in 6 weeks) | 5 | 13 | 1 | 19 | 5 | 3.8 |
| Data platform migration | 1 | 2 | 13 | 16 | 13 | 1.2 |

Read-outs:
- **Check fixed dates against the order.** SSO is third. If the two items ahead of it push SSO's finish past the deal date, schedule SSO explicitly; WSJF does not know about the cliff.
- **Big enablers sink.** The migration has high risk reduction and opportunity enablement but a large size, so it ranks last and will keep ranking last. Either split it into slices that each remove a specific risk (smaller size, higher WSJF) or fund it from the platform capacity bucket. Do not let WSJF silently starve it.
- **Small items float up.** That is the point (smaller batches flow faster), but check that the top of the list is not just a pile of small, low-value tasks.

## Pitfalls

- **Everything is time-critical.** If most items score 8+ on time criticality, the column carries no information. Ask "what specifically gets worse, and when?"
- **Inventing money.** A cost of delay with no stated inputs is a disguised opinion. Show the components and their assumptions.
- **Ignoring the cliff.** CD3 and WSJF rank standard items; fixed-date items need calendar scheduling as well.
- **Mixing estimation units.** Job size from two teams' story points is not comparable; use a shared relative scale or duration.
- **Re-scoring too rarely.** Cost of delay changes as dates approach and evidence arrives; re-sequence at every planning boundary.
