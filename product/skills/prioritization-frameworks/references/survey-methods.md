# Survey Methods: Opportunity Score and Kano

Read this when designing or analysing an importance/satisfaction (opportunity) survey or a Kano survey. All data below is illustrative.

## Contents
- Opportunity Score survey: need list, questions, sample, analysis, worked table
- Ulwick's opportunity algorithm (ODI variant)
- Kano survey: attributes, question pair, evaluation table, classification, coefficients, worked table
- Pitfalls shared by both

## Opportunity Score survey

### 1. Build the need list
- Source needs from interviews or the opportunity layer of an opportunity solution tree, not from the feature backlog.
- 15-30 statements per survey. More causes fatigue and uniform answers.
- Phrase each as a solution-free outcome, in the customer's vocabulary, one outcome per statement, starting with a verb: "Know which invoices are overdue without opening each one", "Minimize the time it takes to reconcile incoming payments with invoices".
- Test the list with three customers before sending: every statement should be understood the same way and none should name your product.

### 2. Questions
- Importance: "How important is it to you to [outcome]?" 1 = not at all important ... 5 = extremely important.
- Satisfaction: "How satisfied are you with how well you can [outcome] today, with whatever you use now?" 1 = not at all satisfied ... 5 = extremely satisfied.
- Add screening questions so only people who actually do the job answer, and segment questions (role, company size, current tool) so you can cut the results.

### 3. Sample
- About 30 qualified responses per segment is the minimum for comparing segments; 100+ in total gives stable rankings for one segment.
- Include non-customers who do the job with alternatives; customers-only samples over-weight what you already do well.

### 4. Analysis (Olsen variant)
- Normalize each mean to 0-1: (mean − 1) / 4.
- Opportunity = Importance × (1 − Satisfaction).
- Plot Importance (y) against Satisfaction (x); the upper-left area (important, poorly satisfied) holds the opportunities.

| Need | Importance mean | Satisfaction mean | I (0-1) | S (0-1) | Opportunity |
|------|-----------------|-------------------|---------|---------|-------------|
| Reconcile incoming payments with invoices | 4.2 | 1.8 | 0.80 | 0.20 | 0.64 |
| Know which invoices are overdue | 4.6 | 2.2 | 0.90 | 0.30 | 0.63 |
| Send an invoice from a phone | 3.0 | 2.6 | 0.50 | 0.40 | 0.30 |
| Customize invoice branding | 3.4 | 4.2 | 0.60 | 0.80 | 0.12 |

Read-outs: the top two are a tie (0.64 vs 0.63); decide between them on strategy fit and solution ideas, not on the third decimal. Branding is well satisfied: maintain parity, do not invest. Then re-cut by segment; an average can hide a need that is critical for your best-fit segment.

## Ulwick's opportunity algorithm (Outcome-Driven Innovation)

- Importance and Satisfaction are the **percentage of respondents rating 4 or 5** (top-2-box) on a 5-point scale, divided by 10, giving 0-10.
- Opportunity = Importance + max(Importance − Satisfaction, 0).
- Common reading: above about 10 is underserved, above about 15 strongly underserved; where satisfaction exceeds importance the outcome is overserved, which can signal room for a simpler or cheaper offer.
- Example: 85% rate importance 4-5 and 30% rate satisfaction 4-5: 8.5 + (8.5 − 3.0) = **14.0**, underserved. Importance 6.0 with satisfaction 7.5: 6.0 + 0 = **6.0**, overserved.

Do not compare Olsen and Ulwick scores with each other; pick one per study.

## Kano survey

### 1. Choose attributes
- 10-20 concrete attributes a respondent can picture ("Two-factor login", "PDF generated in under two seconds"), not vague qualities ("better performance").
- Add a one-line description or image where the attribute may be unfamiliar.

### 2. Question pair per attribute
- Functional: "If the product had [attribute], how would you feel?"
- Dysfunctional: "If the product did not have [attribute], how would you feel?"
- Answers for both: I like it / I expect it / I am neutral / I can tolerate it / I dislike it.
- Optional: self-stated importance of the attribute (1-9), useful for weighting performance attributes.

### 3. Evaluation table

Rows: functional answer. Columns: dysfunctional answer.

| Functional \ Dysfunctional | Like | Expect | Neutral | Tolerate | Dislike |
|----------------------------|------|--------|---------|----------|---------|
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

A = Attractive, O = One-dimensional (Performance), M = Must-be, I = Indifferent, R = Reverse, Q = Questionable (contradictory answer).

### 4. Classify
- Classify each respondent's answer pair, then take the **most frequent category** per attribute.
- Tie-break by impact on dissatisfaction: M > O > A > I.
- Q above roughly 10% of answers means the attribute wording is confusing; fix and re-ask.
- A sizable R share means a sub-segment actively does not want the attribute; cut the data by segment before deciding.

### 5. Coefficients
- **Better** (satisfaction potential) = (A + O) / (A + O + M + I)
- **Worse** (dissatisfaction if absent) = −(O + M) / (A + O + M + I)
- Plot Better (y) against |Worse| (x) to see attributes on a continuum instead of in hard categories.

### Worked table (40 respondents)

| Attribute | A | O | M | I | R | Q | Category | Better | Worse |
|-----------|---|---|---|---|---|---|----------|--------|-------|
| Two-factor login | 4 | 10 | 22 | 3 | 1 | 0 | Must-be | 0.36 | −0.82 |
| Faster invoice PDF generation | 3 | 19 | 6 | 11 | 0 | 1 | Performance | 0.56 | −0.64 |
| AI summary of overdue invoices | 18 | 7 | 2 | 12 | 1 | 0 | Attractive | 0.64 | −0.23 |

Read-outs:
- Two-factor login: little upside, severe downside if missing. Ship it at parity, no further investment.
- PDF speed: performance attribute; invest in proportion to how much the best-fit segment weights it.
- AI summary: delights a large share and is barely missed when absent; a candidate differentiator, not a must-have for launch. Note that 12 respondents are indifferent, so check which segment the 18 A answers come from.

### Interpreting Kano for scope
- Must-bes: meet the bar, then stop.
- Performance: the competitive battleground; invest where your segment cares most.
- Attractive: one or two well-chosen ones differentiate; they decay into must-bes as the market copies them.
- Indifferent: cut or deprioritize.
- Re-survey about yearly in fast-moving markets.

## Pitfalls shared by both
- **Customers-only samples** over-represent what you already do well.
- **Averaging across segments** hides the needs that matter most to your best-fit customers.
- **Solution-shaped statements** turn an opportunity survey into a feature poll.
- **Too many items** produce fatigue: answers drift towards the middle in the second half.
- **Reporting decimals as decisions:** scores rank opportunities; strategy fit and evidence quality still decide.
