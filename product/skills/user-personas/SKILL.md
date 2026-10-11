---
name: user-personas
description: "Create, validate or refresh evidence-based user personas from interview, survey, support, review or analytics data: behavioural (not demographic) segmentation, a jobs-to-be-done statement with switching forces (push, pull, anxiety, habit), pains, gains, an unexpected insight and product implications per persona, every claim tied to evidence with a confidence level. Labels assumption-based proto-personas as such and adds a plan to validate them. Use when building personas or user profiles from research, synthesising interviews or survey responses into segments, auditing whether existing personas still hold, or when a team wants personas but has no data yet. To plan the interviews that feed personas use interview-script; for the value proposition to a persona use value-proposition; for best-fit customers and positioning use product-positioning; to put personas into a PRD use create-prd."
---

# User Personas

> Includes material adapted from [anthropics/knowledge-work-plugins `synthesize-research`](https://github.com/anthropics/knowledge-work-plugins/tree/1bd42820da111e5f0206e570bf5228a1c35839c7/product-management/skills/synthesize-research) (Apache-2.0, see `LICENSE.txt`). **Modified by ultimate-skills:** its thematic-analysis, behaviour-versus-statement, survey-pitfall and persona-mistake guidance was rewritten and merged into this skill (base skill: phuryn/pm-skills, MIT).

## Purpose

Create detailed, actionable user personas from research data that capture the true diversity of your user base. This skill generates research-backed personas with jobs-to-be-done, pain points, desired outcomes, and unexpected behavioral insights to guide product decisions.

A persona is a compact model of a **behavioural segment**: people who do the same job in a similar situation, want similar outcomes, and get stuck on similar things. Its only value is that it changes decisions. If no product, design or go-to-market decision would differ between two personas, they are one persona.

## Instructions

You are an experienced product researcher specializing in persona development and user research synthesis. You never invent a persona: every attribute is either backed by data or visibly labelled as an assumption.

### Input

Your task is to create refined user personas for **$ARGUMENTS**: as many as the data supports, usually 2-4. Three is a good default when the data supports it; never pad or merge personas just to hit a number.

If the user provides CSV, Excel, survey responses, interview transcripts, support tickets, reviews, CRM or analytics exports, or other research data files, read and analyze them directly using available tools. Extract key patterns, behaviors, motivations, and context.

Ask which **decision** the personas should inform (onboarding redesign, roadmap, messaging, sales targeting). It decides which variables matter.

**Privacy:** anonymise. Refer to participants by ID and descriptor ("P07, office manager, 12-person firm"), never by real name, email or employer, and keep identifying details and real photos out of personas.

### Step 0: Evidence gate

Classify the evidence before analysing, and say which class the output belongs to:

| Persona type | Evidence | How to present it |
|---|---|---|
| **Research persona** | At least 2 source types (for example interviews plus analytics or a survey); about 5-8 or more participants per segment with patterns repeating; segment size estimable from quantitative data | As a validated persona, with a confidence level per claim |
| **Provisional persona** | One source type, fewer than about 5 participants per segment, or proxy data only (competitor reviews, community posts, sales notes) | Labelled "Provisional", with the gaps listed |
| **Proto-persona** | No user data: team knowledge and assumptions | Title says "PROTO-PERSONA (assumption-based, not research)"; every attribute is a hypothesis with a validation step; never the sole basis for a roadmap decision |

If the user asks for personas and has no data, offer a proto-persona set plus a research plan (`interview-script`). Do not fabricate quotes, percentages or "typical day" details.

### Analysis Steps (Think Step by Step)

1. **Data collection and framing:** Read and review all provided research data and documents. Note for each source: what it is, n, dates, segments covered, how it was collected and who is missing (non-responders, churned users, non-customers).
2. **Extraction and coding:** For each participant or record, extract context, trigger, job, behaviours (what they did), attitudes (what they say), pains, workarounds, alternatives, desired outcomes and verbatim quotes. Keep behaviour and stated preference apart: behaviour is stronger evidence. Read [references/evidence-and-synthesis.md](references/evidence-and-synthesis.md) when coding data, rating confidence or analysing surveys: it has the extraction sheet, coding tags, evidence thresholds and survey pitfalls.
3. **Pattern recognition:** Group codes into themes. For each theme record **frequency** (how many of n), **intensity** (emotion, workaround effort, money or time spent) and **contradictions**; contradictions often mark a segment boundary.
4. **Segmentation (behavioural, not demographic):** List the behavioural variables that differ across participants (goals, activities, frequency, expertise, attitude, context, trigger). Place every participant on every variable, then look for groups that sit together on several variables at once. Each group is a candidate persona. Use demographics only as descriptors, and only when they genuinely differ between segments. Keep a segment only if it is distinct, sizeable, actionable and reachable. Read [references/segmentation-and-jtbd.md](references/segmentation-and-jtbd.md) when segmenting or writing jobs and forces: it has the variable-mapping method, a worked example, quantitative clustering pitfalls and the forces model.
5. **Jobs and forces:** For each segment write the job statement ("When <situation>, I want to <motivation>, so I can <outcome>") with its functional, emotional and social sides; the **trigger events** that start the search; and the **forces of progress**: push of the current situation, pull of a new solution, anxiety about switching, habit of the present.
6. **Enrichment:** For each persona, synthesize the data into a coherent profile. Attach evidence references and a confidence level (High / Medium / Low) to each section.
7. **Size and prioritise:** Estimate each segment's share from quantitative data; qualitative data can show that a segment exists, not how big it is. Name the **primary persona** for the decision at hand, and optionally an **anti-persona** (who we deliberately do not design for).
8. **Validation:** Cross-reference insights to ensure personas are grounded in actual research findings: analytics, sales and support recognition, and users themselves (see "Validation and refresh"). List the gaps.

### Output Structure

Start with a **persona set overview**: persona, type (research / provisional / proto), estimated share and source, primary job, the behaviour that distinguishes it, confidence, and which decisions it should drive. Then, for each persona, the sections below. Read [references/persona-template.md](references/persona-template.md) when writing the output: it has copy-ready research, proto- and anti-persona templates and a worked example.

**Persona Name and Context**
- A descriptive name based on behaviour ("The Month-End Catch-Up"), optionally with a first name; avoid cute alliteration.
- Role/title, company size (if B2B), context of use, key characteristics. Age range only if it matters to the decision.
- Evidence base: sources, n, dates, confidence.

**Primary Job-to-be-Done**
- The job statement and the core outcome the persona is trying to achieve.
- Context and frequency of the job; trigger events; current alternatives, including doing nothing.

**Forces of Progress**
- Push, pull, anxiety, habit: one or two evidence-backed lines each.

**Top 3 Pain Points**
- Specific challenges or obstacles preventing job completion.
- Impact and severity of each, with frequency ("8 of 12 participants") and a verbatim quote.

**Top 3 Desired Gains**
- Benefits, outcomes, or solutions the persona seeks.
- How they measure success, in their own words where possible.

**One Unexpected Insight**
- A counterintuitive behavioral pattern or motivation derived from the data.
- Why this matters for product decisions.

**Product Fit Assessment**
- How $ARGUMENTS addresses (or could address) this persona's needs.
- Potential friction points or unmet needs.
- The decisions this persona should drive: design, roadmap, messaging, channel.

**Evidence and Gaps**
- 2-3 verbatim quotes with participant IDs; key data points with source.
- What is still unknown, and the cheapest way to find out.

Close with the research gaps across the set, the next research step, and the refresh date.

## Validation and Refresh

Run four checks before calling a persona set done:

| Check | Question | Pass |
|---|---|---|
| Data | Do the behaviours match analytics? Can each segment be sized? | Each persona maps to an identifiable group in product or CRM data |
| Team | Do sales, support and success recognise each persona? | They can name real customers who fit, and none who fit two |
| User | Shown to 3-5 people from the segment: "What is wrong with this?" | Corrections are minor, not "that's not me" |
| Decision | Which decision does this persona change? | At least one concrete decision per persona |

**Refresh cadence:** give every persona set an owner, a version and a last-updated date. Review it every 6-12 months, and immediately when you enter a new market or segment, change pricing or packaging, ship a major product change, see a metric shift the personas cannot explain, or new research contradicts them. Keep an evidence log; retire personas that no longer match a meaningful segment instead of letting them linger.

**Turning a proto-persona into a research persona:** each assumption becomes a research question, the questions feed `interview-script`, and the results confirm, change or retire each attribute. Remove the proto label only when the evidence gate for a research persona is met.

## Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Demographic persona | Age, gender, income, hobbies; nothing about jobs or behaviour | Segment on behaviour and goals; keep demographics as minimal descriptors |
| Invented persona | Quotes, percentages or "a day in the life" with no source | Label as proto-persona or remove the detail; leave unknowns blank |
| Elastic persona | One persona stretched to cover everyone ("wants simple but powerful") | Split along the contradiction; a persona for everyone serves no one |
| Aspirational persona | Describes the users you want, not the ones you have | Base it on actual users; put the target in positioning (`product-positioning`) |
| Committee persona | Every stakeholder added a trait | One owner, data-driven attributes only |
| Averaged persona | Opposite behaviours averaged into a lukewarm middle | Look at distributions; bimodal data means two segments |
| Too many personas | Six or more, nobody remembers them | Merge personas that would get the same decision; 2-4 is usual |
| Decorative persona | Nice poster, no decision changes | Add the decisions each persona drives, or retire it |
| Quote-mining | Only the most dramatic quotes, chosen to support a view | Representative quotes plus counter-examples, with frequency |
| Stale persona | "Last updated" years ago; the product has changed | Owner, version, refresh triggers |

## Best Practices

- Ground all insights in actual data; where you must assume, label it.
- Use direct quotes from research when available: verbatim, attributed to participant ID and type, never stitched together.
- Identify behavioral patterns, not just demographic categories.
- Make personas distinct and non-overlapping where possible; fewer, sharper personas beat many.
- Flag any data gaps or areas requiring additional research.
- Related skills: `interview-script` plans the research that feeds or validates personas; `value-proposition` builds the value proposition for a persona; `product-positioning` defines best-fit customers for go-to-market; `opportunity-solution-tree` turns persona pains into opportunities; `create-prd` uses personas in its market-segment section.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
