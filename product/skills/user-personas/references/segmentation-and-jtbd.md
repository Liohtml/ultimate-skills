# Behavioural Segmentation and Jobs-to-be-Done

Read this when grouping participants into personas (Analysis Step 4) or
writing the job, trigger and forces sections (Step 5).

## 1. Why behaviour, not demographics

Two people of the same age and job title can need very different things, and
people with nothing in common demographically often do the same job the same
way. Behaviour, goals and context predict what someone needs from a product;
demographics rarely do. Use demographics as **descriptors** of a behavioural
segment, and only where they actually differ between segments (for example
company size in B2B when it changes who does the work).

## 2. Behavioural-variable mapping (qualitative)

This method follows the behavioural-variable approach of goal-directed design
(Alan Cooper and colleagues, *About Face*).

1. **List the variables** on which participants differ. Typical kinds:
   - *Activities:* what they do and how often.
   - *Goals and motivations:* why they do it; what "done well" means.
   - *Attitudes:* how they feel about the job, the tools, change, risk.
   - *Aptitude:* expertise with the domain and with tools.
   - *Context:* where, under what pressure, alone or with others.
   - *Trigger:* what starts the job or the search for a better way.
   Aim for roughly 6-12 variables that matter to the decision.
2. **Define each variable as a range** with two ends ("does own admin" to
   "delegates admin"; "weekly" to "quarterly").
3. **Place every participant** on every range, from the evidence.
4. **Look for co-location:** participants who sit near each other on several
   variables at once. A group that clusters on 3 or more significant variables
   is a candidate segment.
5. **Name what distinguishes each group:** the 2-3 variables that set it apart
   are the persona's defining behaviours.
6. **Check for gaps and redundancy:** a participant who fits nowhere may signal
   a missing segment (or an outlier); two groups that would get the same design
   decision should merge.

### Worked example (fictional)

Research on an invoicing app, 14 interviews plus analytics. Selected
variables and placements:

| Variable | Range | P01 | P02 | P03 | P04 | P05 | P06 |
|---|---|---|---|---|---|---|---|
| Invoices per month | 1-5 ... 30+ | 3 | 25 | 4 | 30 | 2 | 22 |
| Who does admin | Self ... Delegated | Self | Bookkeeper | Self | Bookkeeper | Self | Self |
| When invoicing happens | As work finishes ... Month-end batch | Batch | As done | Batch | As done | Batch | As done |
| Attitude to chasing payment | Avoids ... Systematic | Avoids | Systematic | Avoids | Systematic | Avoids | Systematic |
| Tool sophistication | Email + spreadsheet ... Accounting suite | Spreadsheet | Suite | Spreadsheet | Suite | Spreadsheet | Suite |

Co-location: P01, P03 and P05 cluster on low volume, self-managed, month-end
batching and avoiding chasing. P02, P04 and P06 cluster on high volume,
systematic chasing, invoicing as work finishes; P02 and P04 also delegate
admin, P06 does not. Candidate personas: "The Month-End Catch-Up" (P01, P03,
P05) and "The Systematic Biller" (P02, P04, P06), with a possible split of
the second on "who does admin" if it changes a decision (for example
multi-user permissions). Analytics then sizes the groups by invoice volume and
batching pattern.

## 3. Quantitative segmentation

Use when a survey or product data covers enough users.

- **Needs- or behaviour-based clustering** of survey answers (for example
  k-means on standardised behaviour items, or latent class analysis on
  categorical answers). Choose input variables from the qualitative work.
- **Behavioural cohorts** in analytics: frequency, features used, sequence,
  team size, time to value.
- **Pitfalls:** clustering on demographics because they are easy to collect;
  too many input variables (noise dominates); clusters that change with every
  random seed or sample (unstable, so not real); naming clusters before
  reading what is in them; treating cluster output as personas without the
  qualitative "why".
- Always pair quantitative clusters with qualitative evidence before turning
  them into personas.

## 4. Is this a real segment?

| Test | Question |
|---|---|
| Distinct | Does it differ in need or behaviour, not just in description? |
| Sizeable | Is it large or valuable enough to matter to the decision? |
| Actionable | Would we design, build, price or message differently for it? |
| Identifiable | Can we find these people in our data or in the market? |
| Stable | Will it still exist in a year, or is it a temporary state of another segment? |

Fail "actionable" means merge. A segment that passes everything except
"sizeable" may still deserve a persona if it is strategically important; say so.

## 5. How many personas, and which is primary

- Usually 2-4. More than about 5 and teams stop using them.
- For each decision, pick a **primary persona**: the one whose needs must be
  fully met. Secondary personas are served by the same design with additions.
  If two personas both need to be primary for the same decision with
  conflicting needs, the decision probably needs to be split.
- An **anti-persona** (negative persona) describes who the product
  deliberately does not serve. It prevents scope creep and wasted
  acquisition spend.

## 6. Jobs-to-be-done

A job is the progress someone is trying to make in a particular situation. It
is stable over time; solutions change.

**Job statement:**
"When <situation>, I want to <motivation>, so I can <expected outcome>."

Example: "When a client hasn't paid on time, I want to remind them without
sounding desperate, so I can get paid and keep the relationship."

Each job has three sides:

- **Functional:** the practical task (get the invoice paid).
- **Emotional:** how they want to feel (not anxious about cash, not awkward).
- **Social:** how they want to be seen (professional, not needy).

Keep levels apart: *job* (get paid on time) is not *task* (send an email) is
not *solution* (automatic reminders). Personas hold jobs; PRDs hold solutions.

**Desired outcome statements** (from Tony Ulwick's outcome-driven innovation)
make jobs measurable: direction + metric + object of control, for example
"minimise the time it takes to chase a late payment", "reduce the chance
that a client is reminded about an invoice they already paid". These feed success metrics in `create-prd`.

## 7. Forces of progress

Four forces decide whether someone switches to a new solution (the forces
model from Bob Moesta and Chris Spiek's switch interviews):

| Force | Direction | Ask about |
|---|---|---|
| **Push** of the situation | Toward change | "What was going wrong? What finally made you act?" |
| **Pull** of the new solution | Toward change | "What did you hope would be different? What attracted you?" |
| **Anxiety** about the new | Against change | "What worried you about switching? What almost stopped you?" |
| **Habit** of the present | Against change | "What did you like about the old way? What was hard to give up?" |

A switch happens when push plus pull outweigh anxiety plus habit. For product
work: anxiety and habit are often cheaper to reduce (migration help, trial,
undo, social proof) than pull is to increase.

## 8. Triggers and the switching timeline

People move through: **first thought** (something feels off), **passive
looking** (noticing alternatives), a **trigger event** that turns it into
**active looking**, **deciding**, **first use**, and **ongoing use**.
Common triggers: growth (new hires, more clients), a painful incident (missed
payment, failed audit), a change of role or boss, a deadline, a competitor or
peer doing something visible, a price change in the current tool.

Record for each persona: typical triggers, how long they stay in each stage,
and what they compare against while deciding. These feed onboarding,
messaging and channel decisions.
