# Requirements, Acceptance Criteria and Edge Cases

Read this when writing section 7.2 (key features and requirements), 7.3
(non-functional requirements) or 7.5 (edge cases).

> Parts of this file (the priority tests, user-story mistakes, acceptance
> criteria tips and scope rules) are adapted from anthropics/knowledge-work-plugins
> `write-spec` (Apache-2.0). Modified by ultimate-skills: rewritten and extended.

## 1. Prioritise with MoSCoW

| Priority | Meaning | Test |
|---|---|---|
| **Must** | The release does not solve the core problem without it | "If we cut this, does the release still solve the core problem for the primary segment?" No = Must |
| **Should** | Important, painful to leave out, but there is a workaround | "Would we delay launch for this?" No = not a Must |
| **Could** | Desirable; cut first when time runs short | "Would anyone outside the team notice its absence at launch?" |
| **Won't (this time)** | Agreed out of scope for this release | Moves to non-goals or a later phase |

Rules:

- **If everything is a Must, nothing is.** Challenge each one: "Would we
  really not ship without this?"
- Keep Musts at or below about **60% of the estimated effort** (the DSDM
  guideline), with Coulds around 20%. That buffer is what makes a date credible.
- Shoulds are things you expect to build soon, not a wish list.
- "Won't" items are useful architecture insurance: naming them stops the team
  making a design choice that blocks them later.
- When a larger backlog needs scoring (RICE, Kano, opportunity score), use
  `prioritization-frameworks`; MoSCoW is for scoping one release.

## 2. Write user stories

Format: **As a** <specific user>, **I want** <capability> **so that** <benefit>.

- The user is specific enough to design for ("workspace admin with SSO
  enabled", not "user").
- The capability describes what they want to achieve, not the widget.
- The benefit says why it matters; if you cannot write it, question the story.
- Group stories by persona and order by priority.

Good stories follow **INVEST**: Independent, Negotiable, Valuable, Estimable,
Small (fits in one iteration), Testable.

Common mistakes:

| Mistake | Example | Better |
|---|---|---|
| Too vague | "I want the product to be faster" | "I want the invoice list to load in under a second so I can check status between calls" |
| Prescribes the UI | "I want a dropdown of clients" | "I want to pick the client I invoiced last without typing" |
| No benefit | "I want to click Export" | "...so that I can send figures to my accountant" |
| Too large | "I want to manage my team" | Split: invite, remove, change role, see activity |
| Internal task | "As engineering we want to refactor billing" | Not a user story; track as a technical task linked to the requirement it enables |

## 3. Acceptance criteria

Every requirement needs criteria that a tester can verify without asking the
author. Two formats:

**Given / When / Then**

```
R3. Automatic payment reminder
Given an invoice is 3 days past its due date and reminders are on
When the daily reminder job runs
Then the client receives one reminder email using the account's template
And the invoice timeline shows "Reminder sent" with the timestamp
And no reminder is sent if the invoice was paid or voided before the job ran
```

**Checklist**

```
- [ ] Owner can switch reminders on or off per client
- [ ] Reminder schedule: 3, 7 and 14 days overdue; no more than 3 per invoice
- [ ] Each reminder includes the pay link and outstanding amount in the invoice currency
- [ ] A bounced email shows a warning on the invoice within 1 hour
```

Tips:

- Cover the happy path, the main error paths and the edge cases.
- Include what must **not** happen (negative cases): no duplicate sends, no
  data shown to users without permission.
- Replace vague words with observable thresholds. "Fast" becomes "p95 under
  500 ms"; "intuitive" becomes "8 of 10 test users complete the task unaided
  on the first try".
- One behaviour per criterion so each can pass or fail on its own.
- Describe behaviour, not implementation.

## 4. Non-functional requirements checklist

Ask each question; record only the ones that constrain this release.

| Area | Questions |
|---|---|
| Performance | Response time targets (p50 / p95)? Data volume limits? Batch sizes? |
| Reliability | Availability target? What happens on partial failure, retry, timeout? Idempotency? |
| Security | Who may see or change what? Audit trail? Abuse and rate limits? |
| Privacy | Which personal data is collected, why, for how long? Consent? Deletion and export? Data residency? |
| Accessibility | Target standard (for example WCAG 2.2 AA)? Keyboard, screen reader, contrast, motion? |
| Localisation | Languages, currencies, time zones, date and number formats, right-to-left? |
| Compatibility | Browsers, OS versions, devices, API versions, backward compatibility of data? |
| Instrumentation | Which events and properties are needed to compute every metric in section 4? Who verifies them before launch? |
| Supportability | What do support staff need to see or do? Admin tools? Error messages users can act on? |
| Compliance | Regulations, contracts or certifications affected? Review needed? |

## 5. Edge-case catalogue

Walk this list for each key flow. Each case either gets a requirement or is
listed as a non-goal.

- **Empty and first-run:** no data yet, first visit, nothing to show.
- **Boundaries:** zero, one, maximum, just over the maximum; very long text;
  special characters; large files.
- **Permissions:** viewer versus editor versus admin; revoked access mid-flow;
  shared or delegated accounts.
- **State changes:** item deleted, edited or paid by someone else while open;
  concurrent edits; stale data.
- **Time:** time zones, daylight-saving change, end of month or year, leap
  day, scheduled jobs that run late.
- **Money and units:** currencies, rounding, taxes, refunds, partial payments.
- **Failure:** network loss, third-party outage, timeout, retry duplicates,
  partial success in a batch.
- **Migration:** existing customers and data created before this feature;
  default settings for them; rollback with new data already written.
- **Abuse:** spam, scraping, enumeration, using the feature to harass others.
- **Accessibility and devices:** small screens, zoom, keyboard only, screen
  readers, low bandwidth.
- **Notifications:** opt-outs, bounces, duplicates, quiet hours.

## 6. Manage scope

Scope creep shows up as requirements added after approval, "small" additions
that add up, features nobody asked for ("while we're at it"), and a launch date
that moves without an explicit re-scope.

- Write explicit non-goals in every PRD.
- Any addition after approval comes with a removal or a new date, agreed by the
  decision owner and recorded in the change log.
- Separate v1 from later phases clearly.
- Check every requirement against the problem statement: does it serve it?
- Time-box investigations: "If we cannot answer X in 2 days, we cut it."
- Keep a parking lot for good ideas that are out of scope.
