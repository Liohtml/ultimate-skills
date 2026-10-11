# PRD Template (copy-ready)

Copy the block below into `PRD-[product-name].md` and fill it in. Text in
`<angle brackets>` is guidance: replace or delete it. Keep the labels
`[Data]`, `[Research]`, `[Assumption]`, `[TBD: owner]` in the final document so
readers can see what is known and what is not.

For a **one-pager** keep only sections 1, 3, 4, 7.2 and 8, and cut each to its
first bullet or table.

```markdown
# PRD: <Product or feature name>

| Status | Version | Last updated | Decision owner |
|---|---|---|---|
| Draft / In review / Approved | 0.1 | <YYYY-MM-DD> | <name, role> |

## 1. Summary

<2-3 sentences: the problem, for whom, the bet we are making, and the one
metric that will tell us whether it worked.>

## 2. Contacts

| Name | Role | Responsibility | Comment |
|---|---|---|---|
| <name> | Product manager | Driver; writes and maintains this PRD | |
| <name> | <title> | Decision owner: approves scope and launch | |
| <name> | Design lead | UX, research | |
| <name> | Engineering lead | Feasibility, estimates, technical design | |
| <name> | Data / analytics | Metric definitions, instrumentation, readout | |
| <name> | Go-to-market / support / legal | Launch readiness, enablement, review | |

## 3. Background

### Problem statement
<Who> struggles to <do what> when <situation>, about <how often>. Today they
<current workaround>, which costs <time / money / risk / churn>. <Do not name
the solution here.>

### Evidence
| # | Evidence | Type | Source and date |
|---|---|---|---|
| E1 | <e.g. 38% of new accounts never send a second invoice> | [Data] | <dashboard, date range> |
| E2 | <e.g. 7 of 12 interviewed owners chase late payments by hand> | [Research] | <study, n, segment, date> |
| E3 | <disconfirming or complicating evidence> | | |

### Why now?
<What changed: customers, market, technology, regulation, strategy. Has this
just recently become possible?>

### Prior art
<Earlier attempts and what we learned; how competitors and substitutes handle
it.>

## 4. Objective

### Objective
<The outcome and why it matters to customers and the company. How it aligns
with vision, strategy and the north-star metric.>

### Success metrics
| Role | Metric | Definition | Baseline | Target | By when | Source |
|---|---|---|---|---|---|---|
| Primary | <metric> | <exact definition, population, window> | <value [Data]> | <success / stretch> | <date or +N weeks> | <tool, query> |
| Leading | <metric> | | | | | |
| Guardrail | <metric that must not get worse> | | <value> | <no worse than X> | | |

### Non-goals
| Non-goal | Why not now | Where it goes |
|---|---|---|
| <thing we will not do> | <low impact / too complex / separate initiative / premature> | <phase 2 / team X / never> |

## 5. Market segment(s)

- **Primary segment:** <defined by problem or job; size with source>
- **Secondary segment:** <if any>
- **Not for:** <who we deliberately do not serve with this release, and why>
- **Constraints:** <platforms, regions, plan tiers, accessibility, regulation>
- **Personas:** <links>

## 6. Value proposition(s)

- **Jobs addressed:** <the customer job in their words>
- **Gains:** <what they get>
- **Pains avoided:** <what goes away>
- **Versus the current alternative:** <including doing nothing; why better>

## 7. Solution

### 7.1 UX / prototypes
<Links to flows and designs. List the states covered: empty, loading, error,
success, no permission, first-run.>

### 7.2 Key features and requirements
| ID | User story | Priority | Acceptance criteria | Notes / dependencies |
|---|---|---|---|---|
| R1 | As a <specific user>, I want <capability> so that <benefit> | Must | Given <context>, when <action>, then <observable result> | |
| R2 | | Should | | |
| R3 | | Could | | |
| R4 | | Won't (this release) | | Moved to non-goals |

### 7.3 Technology and non-functional requirements
| Area | Requirement (constraint, not design) |
|---|---|
| Performance | <e.g. p95 response under 500 ms for lists up to 1,000 rows> |
| Reliability | <availability, data durability, retries> |
| Security and privacy | <auth, permissions, PII handling, retention, consent> |
| Accessibility | <e.g. WCAG 2.2 AA for all new UI> |
| Localisation | <languages, currencies, date formats> |
| Instrumentation | <events needed to compute every metric in section 4> |
| Compliance | <regulations, audits> |

### 7.4 Assumptions and risks
| # | Assumption | Risk type | Confidence | Impact if wrong | Validation | By when | Owner |
|---|---|---|---|---|---|---|---|
| A1 | <we believe...> | Value / Usability / Feasibility / Viability | Low / Med / High | <what breaks> | <cheapest test> | <date> | <name> |

### 7.5 Edge cases
| Case | Expected behaviour | Requirement ID or non-goal |
|---|---|---|
| <e.g. customer has no email address> | <behaviour> | R5 |

## 8. Release

### Timeline and phasing
| Phase | Scope | Relative timing | Exit criteria |
|---|---|---|---|
| v1 (smallest release that tests the bet) | R1-R3 | <~N weeks after design sign-off> | <metric threshold or learning> |
| Later | <R4, ...> | | |

### Rollout or experiment plan
- **Method:** <A/B test / staged flag rollout / beta / holdout>, and why
- **Stages:** <internal -> beta -> 5% -> 25% -> 100%>, with the minimum time at each
- **Decision rule:** ship if <primary metric reaches X and guardrails hold>;
  iterate if <...>; roll back if <...>
- **Evaluation date:** <date or +N weeks after full exposure>
- **Rollback triggers:** <guardrail thresholds, error rates, support volume>

### Dependencies and launch readiness
<Other teams, support training, docs, sales enablement, legal or privacy
review, marketing.>

### Open questions
| Question | Owner | Blocking? | Needed by |
|---|---|---|---|
| <question> | <name / function> | Yes / No | <date or milestone> |

## Change log
| Date | Version | Change | By |
|---|---|---|---|
| <YYYY-MM-DD> | 0.1 | First draft | <name> |
```
