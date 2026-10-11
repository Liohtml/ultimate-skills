# Success Metrics, Guardrails and Rollout

Read this when filling in section 4 (success metrics) or section 8 (rollout or
experiment plan).

> The leading and lagging indicator lists and the target-setting rules are
> adapted from anthropics/knowledge-work-plugins `write-spec` (Apache-2.0).
> Modified by ultimate-skills: rewritten and extended with guardrails,
> measurement plans and rollout decision rules.

## 1. The metric set

| Role | How many | Purpose | Example |
|---|---|---|---|
| **Primary** | 1 | The outcome that defines success. The one number in the summary. | Share of new accounts that send a second invoice within 60 days |
| **Leading / secondary** | 1-3 | Move within days; tell you early whether the primary will move | Reminder set-up rate in week 1; task completion rate |
| **Guardrail** | 1-3 | Must not get worse; protects what the primary could be "won" against | Unsubscribe rate of invoice emails; support tickets per 100 accounts; p95 latency |

Rules:

- **Outcome, not output.** "Ship the wizard" is a task. "Cut median time to
  first invoice from 3 days to 1" is an outcome.
- **One primary.** Two primaries invite cherry-picking after launch.
- **Link up.** Show how the primary feeds the product's north-star or
  company-level metric (`north-star-metric` builds that tree).
- **Every metric is computable on day one.** If the events do not exist yet,
  instrumentation is a Must requirement in 7.3.

### Leading indicators (days to weeks)
- **Adoption:** share of eligible users who try the feature.
- **Activation:** share who complete the core action.
- **Task success:** share who achieve their goal; time to complete.
- **Error rate:** how often users hit errors or dead ends.
- **Repeat use:** how often users come back to it.

### Lagging indicators (weeks to months)
- **Retention:** does the feature change cohort retention?
- **Revenue:** upgrades, expansion, conversion, reduced churn.
- **Satisfaction:** CSAT, NPS or task-level satisfaction (watch distributions,
  not only averages).
- **Support load:** tickets per active account on the topic.
- **Win rate:** for B2B, deals won where this was a stated factor.

### Guardrail ideas
Retention of the core action, revenue per user, latency and error rates,
support volume, unsubscribes or complaints, accessibility regressions,
fairness across segments (does one segment get worse while the average
improves?), and the primary metric of any feature this one might cannibalise.

## 2. Define each metric precisely

A metric definition answers:

1. **Population:** who is counted (new accounts? all active? one plan tier?)
   and who is excluded (internal, test, bots).
2. **Event and window:** what exactly counts, over which time window
   ("second invoice sent within 60 days of sign-up"). The window must be long
   enough for the change to act: reminders that fire only once an invoice is
   overdue cannot move a 30-day metric when payment terms are 30 days.
3. **Unit:** per user, per account, per session; ratio or count.
4. **Source:** tool, table or saved query, and who owns it.
5. **Baseline:** current value over a stable recent period, with the date range.
   If there is no baseline, the first task is to measure one; write
   `[TBD: owner]`, never a guess.

## 3. Set targets

- Base targets on the baseline plus evidence: a comparable past launch, a
  benchmark, or an explicit hypothesis ("if half of owners who chase manually
  switch on reminders, second-invoice rate rises about 6 points").
- Give a **success threshold** (worth keeping) and a **stretch target**.
- Give the **evaluation time**: for example 2 weeks after full exposure for
  leading metrics, one full cycle (30 or 90 days) for lagging ones.
- For guardrails, state the tolerance: "no worse than +0.2 points" or "no
  statistically significant decrease".
- Use ranges when uncertainty is real. False precision ("+7.3%") signals
  invented numbers.

## 4. Choose how to learn

| Method | Use when | Watch out for |
|---|---|---|
| **A/B test** | Enough traffic to detect the target effect in a few weeks; users can be randomised; the change is reversible | Sample size: estimate the minimum detectable effect first. Run full weeks. One primary metric decided before launch. Read out with `ab-test-analysis` |
| **Staged rollout behind a feature flag** | Too little traffic for a test, operational risk, or infrastructure change | Before/after comparisons are confounded by seasonality and other launches; compare against a not-yet-exposed group where possible |
| **Holdout** | You need the long-term effect of a launched feature (retention, revenue) | Keep the holdout small (for example 5%) and time-boxed; document who is held out |
| **Beta / design partners** | B2B, high-touch, or the main risk is usability or value | Small n: treat results as qualitative evidence, not a measured effect |
| **Fake door / concierge / prototype test** | The main risk is value and building is expensive | Ethics and expectation-setting with users; measure intent, not usage |

If the traffic cannot detect the target effect within about 4 weeks, do not
pretend an A/B test will settle it. Say so in the PRD and choose a staged
rollout plus qualitative evidence, or a larger, more detectable change.

## 5. Write the rollout plan

```markdown
- Method: staged feature-flag rollout (traffic too low for a test at a 3-point effect)
- Stages: internal (1 week) -> 10 beta accounts (2 weeks) -> 25% of new accounts
  (2 weeks) -> 100%
- Advance to the next stage when: no Sev-1/Sev-2 bugs open, guardrails within
  tolerance, support tickets on the topic under 2 per 100 exposed accounts
- Decision at evaluation date (+4 weeks at 100%):
  - Ship and keep investing if the primary reaches the success threshold and guardrails hold
  - Iterate if the leading metrics move but the primary does not
  - Roll back or remove if a guardrail breaks its tolerance, or nothing moves
- Rollback triggers (any stage): email complaint rate above 0.1%; error rate
  above 1%; any data exposure across accounts
- Owner of the readout: <name>; readout shared with: <decision owner, team>
```

Decide the rules **before** launch and write them down. Rules invented after
seeing the data are rationalisations.

## 6. Kill criteria

A kill criterion is the result at which you stop investing, written before
launch:

- "If fewer than 15% of eligible accounts switch reminders on within 4 weeks of
  full rollout, we stop building phase 2 and revisit the problem."
- "If late-payment days do not improve by at least 2 days for adopters after 60
  days, we remove the feature from the roadmap."

`strategy-red-team` produces kill criteria for each load-bearing assumption;
copy the ones that apply into section 7.4 and section 8.
