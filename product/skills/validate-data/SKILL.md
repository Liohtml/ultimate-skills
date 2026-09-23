---
name: validate-data
description: "QA gate for a data analysis before it is shared: reviews question framing, population and metric definitions, runs a pre-delivery checklist, hunts a pitfall catalog with detection steps (join explosion, survivorship bias, incomplete periods, denominator shift, average of averages, timezone mismatch, selection on the outcome, Simpson's paradox), recomputes key numbers, checks chart integrity and whether the narrative follows from the data, and returns a Ready to share / Share with caveats / Needs revision verdict with required caveats. Use when reviewing an analysis, dashboard, SQL result, notebook or metrics report before a stakeholder presentation or decision, or when numbers look off. For experiment significance and ship/stop calls use ab-test-analysis; for SaaS unit economics (MRR, churn, LTV:CAC) use saas-metrics-coach."
license: Apache-2.0 (complete terms in LICENSE.txt)
---

# Validate Analysis Before Sharing

> From [anthropics/knowledge-work-plugins `data/skills/validate-data`](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/data/skills/validate-data), licensed under Apache-2.0 (see `LICENSE.txt`). **Modified by ultimate-skills:** description rewritten; connector note, slash-command usage and example blocks removed; the pitfall catalog, sanity checks and documentation standards moved to `references/` for progressive disclosure; related-skill pointers added.

Review an analysis for accuracy, methodology, and potential biases before sharing with stakeholders. Generates a confidence assessment and improvement suggestions.

## Input

The analysis can be:
- A document or report in the conversation
- A file (markdown, notebook, spreadsheet)
- SQL queries and their results
- Charts and their underlying data
- A description of methodology and findings

If you can run queries or code against the data, spot-check by re-running; otherwise reason from what is shown and say which checks you could not execute.

## Workflow

### 1. Review Methodology and Assumptions

Examine:

- **Question framing**: Is the analysis answering the right question? Could the question be interpreted differently?
- **Data selection**: Are the right tables/datasets being used? Is the time range appropriate?
- **Population definition**: Is the analysis population correctly defined? Are there unintended exclusions?
- **Metric definitions**: Are metrics defined clearly and consistently? Do they match how stakeholders understand them?
- **Baseline and comparison**: Is the comparison fair? Are time periods, cohort sizes, and contexts comparable?

### 2. Run the Pre-Delivery QA Checklist

Work through the checklist below — data quality, calculation, reasonableness, and presentation checks.

### 3. Check for Common Analytical Pitfalls

Systematically review against the pitfall catalog in [references/pitfalls-and-sanity-checks.md](references/pitfalls-and-sanity-checks.md) (join explosion, survivorship bias, incomplete period comparison, denominator shifting, average of averages, timezone mismatches, selection bias, and other statistical traps). Load it for every validation.

### 4. Verify Calculations and Aggregations

Where possible, spot-check:

- Recalculate a few key numbers independently
- Verify that subtotals sum to totals
- Check that percentages sum to 100% (or close to it) where expected
- Confirm that YoY/MoM comparisons use the correct base periods
- Validate that filters are applied consistently across all metrics

Apply the result sanity-checking techniques in [references/pitfalls-and-sanity-checks.md](references/pitfalls-and-sanity-checks.md) (magnitude checks, cross-validation, red-flag detection).

### 5. Assess Visualizations

If the analysis includes charts:

- Do axes start at appropriate values (zero for bar charts)?
- Are scales consistent across comparison charts?
- Do chart titles accurately describe what's shown?
- Could the visualization mislead a quick reader?
- Are there truncated axes, inconsistent intervals, or 3D effects that distort perception?

### 6. Evaluate Narrative and Conclusions

Review whether:

- Conclusions are supported by the data shown
- Alternative explanations are acknowledged
- Uncertainty is communicated appropriately
- Recommendations follow logically from findings
- The level of confidence matches the strength of evidence

### 7. Suggest Improvements

Provide specific, actionable suggestions:

- Additional analyses that would strengthen the conclusions
- Caveats or limitations that should be noted
- Better visualizations or framings for key points
- Missing context that stakeholders would want

### 8. Generate Confidence Assessment

Rate the analysis on a 3-level scale:

**Ready to share** -- Analysis is methodologically sound, calculations verified, caveats noted. Minor suggestions for improvement but nothing blocking.

**Share with noted caveats** -- Analysis is largely correct but has specific limitations or assumptions that must be communicated to stakeholders. List the required caveats.

**Needs revision** -- Found specific errors, methodological issues, or missing analyses that should be addressed before sharing. List the required changes with priority order.

## Output Format

```
## Validation Report

### Overall Assessment: [Ready to share | Share with caveats | Needs revision]

### Methodology Review
[Findings about approach, data selection, definitions]

### Issues Found
1. [Severity: High/Medium/Low] [Issue description and impact]
2. ...

### Calculation Spot-Checks
- [Metric]: [Verified / Discrepancy found]
- ...

### Visualization Review
[Any issues with charts or visual presentation]

### Suggested Improvements
1. [Improvement and why it matters]
2. ...

### Required Caveats for Stakeholders
- [Caveat that must be communicated]
- ...
```

---

## Pre-Delivery QA Checklist

Run through this checklist before sharing any analysis with stakeholders.

### Data Quality Checks

- [ ] **Source verification**: Confirmed which tables/data sources were used. Are they the right ones for this question?
- [ ] **Freshness**: Data is current enough for the analysis. Noted the "as of" date.
- [ ] **Completeness**: No unexpected gaps in time series or missing segments.
- [ ] **Null handling**: Checked null rates in key columns. Nulls are handled appropriately (excluded, imputed, or flagged).
- [ ] **Deduplication**: Confirmed no double-counting from bad joins or duplicate source records.
- [ ] **Filter verification**: All WHERE clauses and filters are correct. No unintended exclusions.

### Calculation Checks

- [ ] **Aggregation logic**: GROUP BY includes all non-aggregated columns. Aggregation level matches the analysis grain.
- [ ] **Denominator correctness**: Rate and percentage calculations use the right denominator. Denominators are non-zero.
- [ ] **Date alignment**: Comparisons use the same time period length. Partial periods are excluded or noted.
- [ ] **Join correctness**: JOIN types are appropriate (INNER vs LEFT). Many-to-many joins haven't inflated counts.
- [ ] **Metric definitions**: Metrics match how stakeholders define them. Any deviations are noted.
- [ ] **Subtotals sum**: Parts add up to the whole where expected. If they don't, explain why (e.g., overlap).

### Reasonableness Checks

- [ ] **Magnitude**: Numbers are in a plausible range. Revenue isn't negative. Percentages are between 0-100%.
- [ ] **Trend continuity**: No unexplained jumps or drops in time series.
- [ ] **Cross-reference**: Key numbers match other known sources (dashboards, previous reports, finance data).
- [ ] **Order of magnitude**: Total revenue is in the right ballpark. User counts match known figures.
- [ ] **Edge cases**: What happens at the boundaries? Empty segments, zero-activity periods, new entities.

### Presentation Checks

- [ ] **Chart accuracy**: Bar charts start at zero. Axes are labeled. Scales are consistent across panels.
- [ ] **Number formatting**: Appropriate precision. Consistent currency/percentage formatting. Thousands separators where needed.
- [ ] **Title clarity**: Titles state the insight, not just the metric. Date ranges are specified.
- [ ] **Caveat transparency**: Known limitations and assumptions are stated explicitly.
- [ ] **Reproducibility**: Someone else could recreate this analysis from the documentation provided.

## References

- [references/pitfalls-and-sanity-checks.md](references/pitfalls-and-sanity-checks.md): pitfall catalog with detection SQL and prevention, magnitude checks, cross-validation techniques, red flags
- [references/documentation-template.md](references/documentation-template.md): analysis documentation template, code docstring standard, versioning analyses

## Related skills

- **ab-test-analysis**: statistical significance, sample size and ship/extend/stop decisions for experiments. Validate the analysis with this skill, decide the experiment with that one.
- **saas-metrics-coach**: computes and benchmarks SaaS health metrics; run this skill on its outputs before they go to a board.
- **north-star-metric**: when the problem is that the metric definition itself is wrong, not the calculation.
- **minto-pyramid** (writing plugin): once validated, write the findings conclusion-first.

## Tips

- Run this validation before any high-stakes presentation or decision
- Even quick analyses benefit from a sanity check -- it takes a minute and can save your credibility
- If the validation finds issues, fix them and re-validate
- Share the validation output alongside your analysis to build stakeholder confidence
