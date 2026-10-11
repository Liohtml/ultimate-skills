# Worked Example: Compact PRD

Read this when you need to see the expected depth and tone. The product, the
people and every number below are **fictional and illustrative**; never copy
them into a real PRD.

The example is a full 8-section PRD kept short. A real one would link designs,
dashboards and research notes instead of describing them.

---

# PRD: Automatic payment reminders

| Status | Version | Last updated | Decision owner |
|---|---|---|---|
| In review | 0.3 | 2026-03-02 | Head of Product (A. Example) |

## 1. Summary

Owners of very small businesses who invoice through our app spend hours each
month chasing late payments by hand, and many stop using the app after their
first few invoices. We will let them switch on automatic, polite reminders for
overdue invoices. Success means the share of new accounts that send a second
invoice within 60 days rises from 52% to at least 58%.

## 2. Contacts

| Name | Role | Responsibility |
|---|---|---|
| P. Example | Product manager | Driver; maintains this PRD |
| A. Example | Head of Product | Decision owner |
| D. Example | Product designer | Flows, usability tests |
| E. Example | Engineering lead | Estimates, technical design |
| M. Example | Data analyst | Metric definitions, readout |
| S. Example | Support lead | Help content, ticket tagging |
| L. Example | Legal counsel | Email consent and wording review |

## 3. Background

**Problem statement.** Sole traders and micro-businesses who invoice clients
monthly often get paid late. To get paid they re-open each invoice, copy the
details into an email and write a reminder by hand, usually several times per
invoice. This takes time they do not bill for and feels awkward, so many
reminders are sent late or not at all, and cash flow suffers.

| # | Evidence | Type | Source |
|---|---|---|---|
| E1 | 52% of accounts created in Q4 sent a second invoice within 60 days | [Data] | Activation dashboard, Oct-Dec 2025 cohorts |
| E2 | 31% of sent invoices are paid after the due date; median 9 days late | [Data] | Payments table, last 6 months |
| E3 | 9 of 14 interviewed owners chase payments by hand; 6 called it "the worst part of invoicing" | [Research] | Discovery interviews, n=14, Jan 2026 |
| E4 | "Payment reminder" is the 2nd most common tag in feature requests | [Data] | Support tool, last 12 months |
| E5 | Two interviewed owners said automatic reminders felt "pushy" to their clients | [Research] | Same study; complicates the bet |

**Why now?** Our email delivery provider now supports per-account sender
domains, so reminders can come from the owner's own address rather than ours,
which interviewees said matters for tone.

**Prior art.** A 2024 manual "Send reminder" button is used on 4% of overdue
invoices. Most competing tools offer scheduled reminders; few let owners edit
the tone per client.

## 4. Objective

Help owners get paid on time without awkward manual chasing, so they keep
invoicing with us. Supports the company north-star metric "invoices paid
through the app per month".

| Role | Metric | Definition | Baseline | Target | By when | Source |
|---|---|---|---|---|---|---|
| Primary | Second-invoice rate | New accounts sending a 2nd invoice within 60 days of sign-up (60 because reminders start only once the first invoice is overdue) | 52% | 58% success, 61% stretch | 12 weeks after 100% rollout (lets the first cohorts complete their 60-day window) | Activation dashboard |
| Leading | Reminder adoption | Eligible accounts with reminders on, week 1 | n/a (new) | at least 25% | 2 weeks after 100% | Feature events |
| Leading | Days late | Median days past due for paid invoices with reminders on | 9 days | 6 days or fewer | 8 weeks | Payments table |
| Guardrail | Complaint rate | Spam complaints per reminder email | 0.02% (invoice emails) | no more than 0.1% | Every stage | Email provider |
| Guardrail | Support load | Tickets tagged "reminders" per 100 exposed accounts | n/a | fewer than 2 | Every stage | Support tool |

**Non-goals**

| Non-goal | Why not now | Where it goes |
|---|---|---|
| SMS or messenger reminders | Consent rules differ by country; email answers most of the need | Revisit after v1 readout |
| Late fees or interest | Legal review per market; changes the tone owners want | Separate initiative |
| Collections or escalation to agencies | Different job, different users | Never in this product |
| Reminders for quotes or estimates | Different problem (conversion, not collection) | Parking lot |

## 5. Market segment(s)

- **Primary:** owners who invoice 3-30 clients per month and do their own
  admin (about 70% of new accounts) [Data].
- **Not for (v1):** accounts with a dedicated bookkeeper user; they already run
  their own chasing process and asked for reports, not automation [Research].
- **Constraints:** email only; English, German and French templates; works on
  the mobile web app.

## 6. Value proposition(s)

Owners want to get paid on time without feeling like debt collectors. Today the
alternative is manual emails or doing nothing. Reminders go out on time, in the
owner's own voice and from their own address, and stop automatically on
payment, so there is no embarrassing reminder for an invoice already paid.

## 7. Solution

**7.1 UX.** Toggle in invoice settings and per client; three editable
templates (friendly, neutral, firm); timeline entry on each invoice. States:
first-run explainer, no email on file, bounced, paused, all paid.

**7.2 Requirements**

| ID | Story | Priority | Acceptance criteria |
|---|---|---|---|
| R1 | As an owner, I want overdue invoices to trigger reminders automatically so I don't have to remember | Must | Given reminders are on and an invoice is 3 days overdue, when the daily job runs, then one reminder is sent and logged on the invoice timeline; none is sent if the invoice is paid or voided |
| R2 | As an owner, I want to turn reminders off for specific clients so I protect sensitive relationships | Must | Per-client toggle overrides the account default; change applies to the next scheduled run |
| R3 | As an owner, I want to edit the reminder wording so it sounds like me | Should | Three templates editable; preview with real invoice data; placeholders validated before save |
| R4 | As an owner, I want to see which reminders bounced so I can fix the address | Should | Bounce shown on the invoice within 1 hour; banner on the dashboard |
| R5 | As an owner, I want to choose the schedule | Could | Choose from preset schedules; maximum 3 reminders per invoice |

**7.3 Non-functional.** Reminders sent from the owner's verified domain or a
reply-to of their address; transactional content only (no marketing), so
reminders carry no unsubscribe link and the client replies to the owner; no more than one
email per invoice per day; templates WCAG 2.2 AA in the editor; events
`reminder_enabled`, `reminder_sent`, `reminder_bounced` live before beta.

**7.4 Assumptions and risks**

| # | Assumption | Type | Confidence | Validation | By when |
|---|---|---|---|---|---|
| A1 | Owners trust automation with client communication | Value | Medium | Beta with 10 accounts; measure opt-out rate and interview 5 | Before 25% stage |
| A2 | Faster payment makes owners keep invoicing (not just a nice-to-have) | Value | Low | Compare second-invoice rate of exposed accounts vs the 5% holdout (adopters vs non-adopters is biased by self-selection) | 12-week readout |
| A3 | Reminder emails will not hurt sender reputation | Viability | Medium | Monitor complaint rate per stage; rollback trigger | Every stage |

**7.5 Edge cases.** Invoice partly paid (remind for the remaining amount);
client has no email (skip, show warning); invoice edited after a reminder
(next reminder uses new amount); owner's time zone differs from client's (send
at 10:00 client local time where known).

## 8. Release

| Phase | Scope | Timing | Exit criteria |
|---|---|---|---|
| v1 | R1-R4 | About 6 weeks after design sign-off | Guardrails hold through 25% stage |
| v1.1 | R5, more languages | After the 12-week readout | Primary reaches success threshold |

**Rollout.** Feature flag: internal (1 week) -> 10 beta accounts (2 weeks) ->
25% of new accounts (2 weeks) -> 100% with a 5% holdout for 12 weeks.
**Decision rule:** ship and continue if the second-invoice rate reaches 58% and
guardrails hold; iterate if adoption is above 25% but the primary does not
move; roll back if complaint rate exceeds 0.1% at any stage.

**Open questions**

| Question | Owner | Blocking? | Needed by |
|---|---|---|---|
| Do German recipients need explicit consent for reminder emails? | Legal | Yes | Before beta |
| Can the holdout be excluded from the onboarding email series? | Data | No | Before 100% |

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-02-20 | 0.2 | Added guardrails and holdout after data review |
| 2026-03-02 | 0.3 | SMS moved to non-goals; R4 promoted to Should |
