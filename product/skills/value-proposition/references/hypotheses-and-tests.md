# Value Hypotheses and the Cheapest Test

Read this when turning the assumptions in a value proposition into hypotheses, choosing how to test them, setting thresholds, or interpreting results.

## Contents
- Where hypotheses come from
- Writing a good hypothesis
- Which risk each hypothesis carries
- Ranking hypotheses
- The test ladder in detail
- Setting thresholds
- Reading results
- Examples

## Where hypotheses come from

Collect every load-bearing assumption from the draft:
- Claims labelled [Assumption] in the 6 parts.
- Fit-check scores of 1 that lack evidence.
- A forces balance that depends on reducing anxiety or habit.
- Differentiation claims ("customers rank X in their top three", "the alternative fails at Y").
- Willingness to pay at the intended price.

A claim is load-bearing if the value proposition, or the business case behind it, fails when the claim is false.

## Writing a good hypothesis

Template:

> We believe [segment] in [situation] will [observable behaviour] because [value driver]. We will know we are right when [metric] reaches [threshold] within [timeframe].

| Weak | Why weak | Strong |
|------|----------|--------|
| "Agencies want automated reminders." | No behaviour, no threshold, untestable | "Agency owners with 10+ open invoices will enable automated reminders for most clients within 2 weeks of setup, because tone presets remove the fear of upsetting clients. Right if ≥ 7 of 10 pilot agencies do so." |
| "Users will love the dashboard." | Feeling, not behaviour | "Owners will open the overdue view at least weekly in the first month. Right if median weekly opens ≥ 1 across pilot accounts." |
| "Customers will pay for this." | No price, no commitment | "At least 5 of 15 qualified agencies sign a letter of intent at 49 per month after a demo." |

## Which risk each hypothesis carries

Marty Cagan's four product risks help pick the right test:

| Risk | Question | Typical tests |
|------|----------|---------------|
| Value | Will they choose it, use it, pay for it? | Interviews on past behaviour, fake door, concierge, pre-sale |
| Usability | Can they figure out how to get the value? | Prototype usability tests |
| Feasibility | Can we build and run it? | Technical spike, prototype |
| Viability | Does it work for the business (pricing, cost, legal, channel)? | Pricing tests, unit-economics model, stakeholder review |

A value proposition mostly carries **value** and **viability** risk. Do not spend the first test on feasibility if nobody has shown they want the outcome.

## Ranking hypotheses

Score each hypothesis on **impact if wrong** (1-5) and **uncertainty** (1-5, from the evidence labels). Test the highest products first. This is the same logic as the assumptions map in David Bland and Alex Osterwalder's *Testing Business Ideas*, which plots importance against the amount of evidence: the important, little-evidence quadrant (top right in their layout) is where the first tests go.

## The test ladder

| Test | Cost and time | Signal strength | A pass looks like | Watch out for |
|------|---------------|-----------------|-------------------|---------------|
| Evidence mining: tickets, reviews, CRM notes, usage queries | Hours, near zero | Medium for problem, none for solution | Problem appears in multiple independent sources for the segment | Complainer bias; count sources, not mentions |
| Problem interviews (5-8, past behaviour) | Days | Strong for problem and forces | Most interviewees describe a recent, specific instance and a costly workaround | Leading questions, future-tense answers |
| Message test (ads, emails, social) | Days, small budget | Weak to medium for pull | One framing of the value clearly out-clicks the others in the same audience | Clicks measure curiosity, not need |
| Landing page or fake door with a clear call to action | Days, small budget | Medium for pull | Sign-up or "request access" rate above the pre-set threshold among qualified visitors | Unqualified traffic; always tell people who clicked what happens next |
| Concierge (deliver the outcome by hand) | 1-3 weeks | Strong for value | Customers keep using it and ask for more; outcome metric moves | Does not test whether software can deliver the same outcome |
| Wizard of Oz (looks automated, done by people) | 1-3 weeks | Strong for value and usability | Behaviour matches what the product would need | Operational effort; keep the pilot small |
| Pre-sale, letter of intent or deposit | 1-3 weeks | Strongest pre-build signal for willingness to pay | Commitments at the intended price above threshold | Discounts that buy a "yes" |
| Pilot with outcome measurement | Weeks to months | Strong for outcome size | Outcome metric improves versus baseline or a comparison group | No comparison group makes before/after misleading |
| A/B test in product | Weeks, needs traffic | Strong for causal effect | Statistically meaningful lift on the primary metric | Too little traffic; use ab-test-analysis to read results |

Pick the **cheapest test that could change the decision**. If a positive result would not change what you do, the test is not worth running.

### Commitment is the currency

Evidence strength rises with what the customer gives up: time (a second meeting, a pilot), reputation (introducing you to a boss or peer), money (deposit, pre-order, letter of intent). Compliments and "I would use it" cost nothing and prove nothing.

## Setting thresholds

- Set pass and fail thresholds **before** the test, in writing.
- Derive them from the business case where possible: if the model needs 5% of qualified visitors to start a trial, a fake door that converts 1% of them is a fail, however encouraging the comments are.
- Define a grey zone between pass and fail and decide in advance what you will do if the result lands there (run a sharper test, narrow the segment, change the offer).
- With small samples, treat results as direction, not precision.

## Reading results

| Result | Next step |
|--------|-----------|
| Pass | Upgrade the claim's label to evidence; move to the next riskiest hypothesis |
| Fail | Do not move the goalposts. Revisit the segment (is the push strong enough?), the value driver, or the offer (anxiety and habit) |
| Grey zone | Run the pre-agreed sharper test; change one variable at a time |
| Mixed by segment | Split the value proposition by segment; one may be strong, the other weak |

## Examples

**H1, value (anxiety):** "Agency owners with 10+ open invoices will enable automated reminders for most clients within 2 weeks, because tone presets and a preview remove the fear of upsetting clients." Test: concierge pilot with 10 agencies (we draft reminders in their tone; they approve). Pass: ≥ 7 of 10 approve sending for most clients. Fail: ≤ 4.

**H2, viability (willingness to pay):** "Qualified agencies will commit at 49 per month." Test: demo plus letter of intent to 15 agencies from the waitlist. Pass: ≥ 5 sign. Fail: ≤ 2. Grey zone 3-4: test a price with a 60-day money-back guarantee.

**H3, value (outcome size):** "Automated reminders cut median days-to-paid by at least 5 days within 60 days." Test: pilot with before/after comparison plus a matched group of non-pilot accounts. Pass: difference ≥ 5 days versus the comparison group. Fail: < 2 days.
