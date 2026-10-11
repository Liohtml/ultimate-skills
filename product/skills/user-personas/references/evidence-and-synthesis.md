# Evidence and Synthesis

Read this when extracting and coding research data (Analysis Steps 1-3),
rating confidence, or working with survey data.

> The thematic-analysis steps, the behaviour-versus-statement guidance, the
> intensity signals and the survey pitfalls are adapted from
> anthropics/knowledge-work-plugins `synthesize-research` (Apache-2.0).
> Modified by ultimate-skills: rewritten for persona work and extended.

## 1. Know what each source can and cannot tell you

| Source | Good for | Bias and limits |
|---|---|---|
| Interviews | Context, motivations, triggers, the "why", language | Small n; recall and social-desirability bias; only people who agreed to talk |
| Contextual inquiry / observation | Real workflows, workarounds people no longer notice | Expensive; small n; observer effect |
| Surveys | Sizing segments, prevalence of a behaviour or need | Stated, not revealed, behaviour; question wording; non-response bias |
| Product analytics | Revealed behaviour, frequency, feature use, cohorts | No "why"; only existing users; tracking gaps |
| Support tickets | Pains, confusion, missing features | Skews to struggling users and problems, not value |
| Reviews and communities | Unprompted language, competitor gaps | Skews to strong opinions and power users |
| Sales and success notes | Buying triggers, objections, alternatives | Second-hand; filtered by what the seller noticed |
| Win/loss and churn interviews | Why people choose, switch or leave | Hindsight rationalisation; hard to reach churned users |
| CRM / firmographics | Company size, industry, plan | Describes accounts, not people or behaviour |

Use at least two source types for a research persona: one that explains (qual)
and one that sizes or confirms behaviour (quant).

## 2. How much evidence is enough

Rules of thumb, not laws:

- **Qualitative, per segment:** about 5-8 interviews before you trust a
  pattern. In a fairly homogeneous group, themes often stop changing (reach
  saturation) at around 12 interviews (Guest, Bunce and Johnson, 2006). A
  heterogeneous population needs more, because each segment needs its own.
- **Saturation test:** if the last 3 interviews in a segment added no new code
  that matters to the decision, you are probably near saturation.
- **Quantitative sizing:** the smallest segment you want to size needs enough
  respondents for a stable share, roughly 30-50 at minimum; under that,
  report a range or "small, size unknown".
- **Proxy data only** (competitor reviews, community posts, analyst reports):
  the persona is Provisional at best. Tag each attribute with its proxy source
  and replace it with first-party evidence as it arrives.

## 3. Extraction sheet

One row per participant or record. Fill it before clustering.

| Field | What to capture |
|---|---|
| ID and descriptor | P07, office manager, 12-person agency (no names) |
| Source and date | Interview, 2026-01-14 |
| Context | When, where, with whom, how often the job happens |
| Trigger | What made them look for a better way, and when |
| Job | What they are trying to get done, in their words |
| Behaviours (did) | Concrete past actions, tools used, frequency |
| Attitudes (said) | Opinions, preferences, feelings |
| Pains | Obstacles, frustrations, costs |
| Workarounds | Spreadsheets, manual steps, hacks: unmet needs in disguise |
| Alternatives | Other products, hiring someone, doing nothing |
| Desired outcomes | What success looks like and how they judge it |
| Forces | Push, pull, anxiety, habit signals |
| Quotes | Verbatim, with timestamp or line reference |
| Surprises | Anything that contradicts the team's assumptions |

### Coding tags

Tag each observation so it can be counted later:
`[CONTEXT]` `[TRIGGER]` `[JOB]` `[BEHAVIOUR]` `[ATTITUDE]` `[PAIN]`
`[WORKAROUND]` `[ALTERNATIVE]` `[OUTCOME]` `[PUSH]` `[PULL]` `[ANXIETY]`
`[HABIT]` `[QUOTE]` `[SURPRISE]`.

Be generous with codes at first; merging is easier than splitting.

## 4. Thematic analysis

1. **Familiarise:** read everything once before coding.
2. **Code:** tag each observation systematically (section 3).
3. **Develop themes:** group related codes into candidate themes that matter
   for the decision.
4. **Review themes:** does each have enough evidence? Are themes distinct? Do
   they hold across sources?
5. **Define:** name each theme and describe it in 1-2 sentences.
6. **Report:** state each theme as a finding with its evidence, frequency and
   confidence.

For each theme record **frequency** (how many of n participants), **intensity**
and **spread** (which segments show it).

### Signals of intensity

- Emotional language: frustration, embarrassment, resignation, excitement.
- Frequency: how often they hit the problem.
- Workaround effort: time, money or people spent to get around it.
- Consequence: what happens when it goes wrong (lost money, missed deadline,
  blame from a boss).
- Unprompted mention: raised before you asked about it.

## 5. Behaviour beats stated preference

What people do often differs from what they say they want.

- Prefer evidence of past behaviour ("last time this happened, I...") over
  hypotheticals ("I would use...").
- If someone says "I need feature X" but their workflow shows they never use
  similar features, record the contradiction; it is often more useful than
  the request.
- Check claims against analytics where possible: "I export every week" versus
  the export logs.
- A request is a solution proposal. Ask what problem it solves, and record the
  problem as the finding.

## 6. Confidence levels

| Level | Criteria |
|---|---|
| **High** | Appears across several participants and at least two source types; raised unprompted; consistent within the segment; behaviour, not only opinion |
| **Medium** | Several participants but one source type; or prompted; or consistent in some sub-groups only |
| **Low** | One or two participants; a single source; possibly an outlier; inferred rather than observed |

Put the level next to each persona section. A finding from two interviews is a
hypothesis, not a conclusion.

## 7. Survey data pitfalls

- **Averages without distributions.** A mean of 3.5 could be everyone lukewarm
  or half love it, half hate it. Bimodal answers often mean two segments.
- **Aggregating before segmenting.** Totals hide segment differences; cut by
  behaviour, plan, tenure or use case first.
- **Non-response bias.** Who did not answer? Churned, busy and unhappy users
  are often missing.
- **Over-reading small differences.** With small samples, a few points'
  difference is noise.
- **Likert scales as interval data.** The gap between "agree" and "strongly
  agree" is not necessarily the gap between "neutral" and "agree".
- **Correlation as causation** in cross-tabs.
- **Leading or double-barrelled questions** that shaped the answer.
- **Open-ended answers ignored.** Code them like short interview notes; themes
  that appear only there are things you did not think to ask.

## 8. Combine qualitative and quantitative

- **Qual first** to find what is happening and why; it generates the
  behavioural variables and hypotheses.
- **Quant to size and confirm:** how many users show each behaviour, and
  whether behaviours co-occur as the qual suggested.
- **Back to qual** to explain surprises in the numbers.
- When sources disagree, check whether they measured different populations or
  stated versus revealed behaviour. Report the disagreement; do not quietly
  pick one source.

## 9. Quotes

- Verbatim only; mark cuts with "...", never stitch two quotes together.
- Attribute to participant ID and type, not name.
- Choose quotes that are representative, and say how representative ("echoed
  by 7 of 12"). Include a counter-quote where the segment is split.
- A quote is evidence, not a finding. State the finding, then the quote.

## 10. Privacy and ethics

- Use participant IDs. Keep the key that maps IDs to people out of the persona
  document and in the research repository with access control.
- Remove details that could identify a person (rare job title plus small
  company plus city).
- Do not use real customers' photos; use none, or an illustration.
- Respect the consent participants gave: if they agreed to internal research
  use only, the persona stays internal.
