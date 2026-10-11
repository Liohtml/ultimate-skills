# Persona Templates

Read this when writing the final output. It contains the persona set
overview, the research persona template, the proto-persona template, the
anti-persona template and a condensed worked example.

Keep labels such as `[High]`, `[Medium]`, `[Low]` and `[Assumption]` in the
delivered personas so readers can see how solid each part is.

## 1. Persona set overview

```markdown
# Personas: <product or area>

Owner: <name> | Version: <1.0> | Last updated: <YYYY-MM-DD> | Next review: <date>
Evidence base: <e.g. 14 interviews (Jan 2026), survey n=412 (Feb 2026), 6 months of product analytics>
Decision these personas inform: <e.g. onboarding redesign>

| Persona | Type | Est. share (source) | Primary job | Distinguishing behaviour | Confidence | Primary for |
|---|---|---|---|---|---|---|
| <name> | Research / Provisional / Proto | <~40% of new accounts (analytics)> | <job statement, short> | <the 2-3 variables that set it apart> | High / Med / Low | <decisions> |
| <anti-persona> | | | | | | Not designed for |
```

## 2. Research persona

```markdown
## <Behavioural name>: "<one-line essence in their words>"

**Type:** Research persona | **Confidence:** <High / Medium / Low>
**Evidence:** <sources, n, dates>   **Estimated share:** <range, source>

### Context
- Role / title range: <...>
- Company size and type (B2B): <...>
- Where and when the job happens: <...>
- Tools and alternatives used today: <...>
- Descriptors that genuinely differ from other personas: <only if relevant>

### Primary job-to-be-done
When <situation>, I want to <motivation>, so I can <expected outcome>.
- Functional: <...>  Emotional: <...>  Social: <...>
- Frequency: <...>
- Triggers that start the search: <...>
- Current alternatives (including doing nothing): <...>

### Forces of progress
- Push: <...> [confidence]
- Pull: <...> [confidence]
- Anxiety: <...> [confidence]
- Habit: <...> [confidence]

### Top 3 pain points
1. <Pain> - severity <high/med/low>; <n of N>; "<verbatim quote>" (P0x)
2. ...
3. ...

### Top 3 desired gains
1. <Outcome> - how they measure success: <...>
2. ...
3. ...

### One unexpected insight
<Counterintuitive pattern from the data> - why it matters: <decision impact>

### Product fit assessment
- Where <product> serves this persona today: <...>
- Friction points: <...>
- Unmet needs: <...>
- Decisions this persona should drive: <design / roadmap / messaging / channel>

### Evidence and gaps
- Quotes: "<...>" (P03, <descriptor>); "<...>" (P09, <descriptor>)
- Data: <metric, value, source>
- Unknown: <gap> -> next step: <research method, owner>
```

## 3. Proto-persona (assumption-based)

Use when there is no user data yet. The format is deliberately different so
nobody mistakes it for research.

```markdown
## PROTO-PERSONA (assumption-based, not research): <working name>

Created by: <team, workshop date> | Status: hypothesis | Validate by: <date>

| Attribute | Our assumption | Confidence | Why we believe it | How we will test it |
|---|---|---|---|---|
| Who they are | <...> | Low / Med | <anecdote, sales notes, proxy data> | <interviews with n=6 in segment> |
| Job and trigger | <...> | | | |
| Top pains | <...> | | | |
| Desired gains | <...> | | | |
| Alternatives used today | <...> | | | |
| Where to find them | <...> | | | |

Riskiest assumption (test first): <...>
Research questions for interview-script: <list>
```

Rules: no invented quotes, no percentages, no photo, no "day in the life".
When research arrives, update each row to confirmed / changed / rejected, and
remove the proto label only when the research-persona evidence gate is met.

## 4. Anti-persona

```markdown
## Anti-persona: <name>

Who: <description>
Why we do not design for them: <economics, strategy, conflicting needs>
How to recognise them: <signals in sign-up, sales or usage data>
What we do instead: <refer elsewhere, self-serve docs only, decline>
```

## 5. Condensed worked example (fictional)

Everything below is invented to show depth and tone. Do not reuse the content.

```markdown
## The Month-End Catch-Up: "I'll do the invoices on Sunday."

**Type:** Research persona | **Confidence:** Medium
**Evidence:** 7 of 14 interviews (Jan 2026); analytics, 6 months
**Estimated share:** 35-45% of active accounts (accounts with 1-2 invoicing
sessions per month, analytics)

### Context
- Sole traders and micro-agencies (1-5 people); the owner does all admin.
- Invoices in one batch at month-end, evenings or weekends, on a laptop.
- Today: invoicing app plus a spreadsheet to track who has paid.

### Primary job-to-be-done
When the month closes, I want to get every invoice out and know who still owes
me, so I can stop thinking about money and get back to client work.
- Emotional: relief from a nagging task; Social: look professional to clients.
- Trigger to look for help: a month when cash ran short because of one late payer.

### Forces of progress
- Push: chasing is awkward and often forgotten (5 of 7) [High]
- Pull: "it just goes out by itself" (4 of 7) [Medium]
- Anxiety: an automatic email could sound rude to a long-time client (3 of 7) [Medium]
- Habit: the spreadsheet feels under control (4 of 7) [Medium]

### Top 3 pain points
1. Forgetting to chase until weeks later - high; 5 of 7; "I only notice when
   the rent is due." (P03)
2. Re-typing invoice details into reminder emails - medium; 4 of 7
3. Not knowing at a glance who has paid - medium; 4 of 7; analytics shows the
   paid-status filter is rarely used by this group

### Top 3 desired gains
1. Paid within terms without thinking about it - measured by "no money worries
   at month-end"
2. One place that shows who owes what
3. Reminders that sound like them

### One unexpected insight
They do not want fewer tasks at month-end; they want **nothing between**
month-ends. Notifications mid-month were described as stressful (4 of 7).
Implication: default to a monthly digest, not real-time alerts.

### Product fit assessment
- Serves today: fast batch invoice creation.
- Friction: payment status buried; no reminders.
- Unmet: automatic, editable, polite reminders; month-end summary.
- Drives: onboarding defaults, reminder tone options, digest notifications.

### Evidence and gaps
- Gap: unknown whether they would pay more for reminders -> pricing survey
  (owner: PM, next quarter).
```

## 6. Delivery checklist

- [ ] Each persona states its type (research / provisional / proto) and evidence base.
- [ ] Segments are defined by behaviour; demographics are descriptors only.
- [ ] Each persona has a job statement, triggers and forces.
- [ ] Pains and gains carry frequency, a quote or data point, and confidence.
- [ ] Every persona names the decisions it should drive.
- [ ] No invented quotes, numbers or identifying details.
- [ ] Gaps, next research step, owner and review date are stated.
