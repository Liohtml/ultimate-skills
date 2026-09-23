# Evidence Labels, Honesty Rules and the Verification Pass

> Adapted from [ferdinandobons/startup-skill `startup-competitors`](https://github.com/ferdinandobons/startup-skill/tree/a5f97c317b93caedbb49d28f20e9ec283b2ec087/startup-competitors) (`references/honesty-protocol.md` and `references/verification-agent.md`; MIT, Copyright (c) 2026 Ferdinando Bons). Changes: merged into one reference for `competitor-analysis`; founder- and startup-specific framing generalized; the multi-file deliverable set (battle cards, matrix, pricing landscape files) reduced to the sections of this skill's single report; the verification step works as a self-review or an optional fresh-context subagent.

Competitive intelligence fails in predictable ways: confident guesses presented as facts, cherry-picked weaknesses, stale pricing, and two claims "corroborating" each other from the same blog post. These rules apply to every section of the report.

## 1. Label every major claim

| Label | Meaning |
|---|---|
| **[Data]** | Sourced finding; give the citation (URL, report, review site) and its date |
| **[Estimate]** | A calculation or projection; state the assumptions |
| **[Assumption]** | An unverified belief that needs testing |
| **[Opinion]** | Your analytical judgment |

- Never present an estimate as a fact. Market share, revenue and customer counts for private companies are almost always estimates.
- When data is missing, write "not found" in the cell. A blank cell is better than a guess; a confident fabrication is worse than "I don't know."
- Mark any data point older than 18 months as potentially outdated, with its date.

## 2. Honesty rules for competitive work

1. **Acknowledge competitor strengths.** If a competitor is objectively better at something, say so directly. An analysis that only lists their weaknesses is useless in a real sales conversation.
2. **Challenge confirmation bias.** When research confirms what the user already believes about a competitor, look for disconfirming evidence before accepting it.
3. **Don't cherry-pick reviews.** Represent sentiment proportionally: three angry forum posts do not outweigh 500 reviews averaging 4.5 stars.
4. **Flag intelligence gaps.** If pricing, traction or funding could not be found, say so.
5. **Treat the status quo as a competitor.** Spreadsheets, an agency, an in-house build and "doing nothing" are alternatives. Ask what triggers someone to switch at all.
6. **Challenge the user's assumptions, politely.** "There's no competition," "we're better at everything" and dismissals of a competitor all need evidence. If the user's assumption contradicts research, say "You assumed X; the data shows Y."
7. **Rate threat honestly**, per competitor:
   - **High**: strong product, growing fast, well funded, overlapping target customers
   - **Medium**: competitive on some dimensions, gaps on others
   - **Low**: weak product, stagnant, or targeting a different segment
   Don't inflate threats to create urgency or deflate them to reassure.

### Anti-patterns

| Anti-pattern | What it looks like | What to do instead |
|---|---|---|
| Cherry-picking weaknesses | Only competitor flaws are listed | Ask what they are actually good at; that is what sales will face |
| Dismissing competitors | "They're not real competition" | Their customers chose them; find the job they do well |
| Confirmation bias | Only confirming evidence found | Search explicitly for contradicting evidence |
| Outdated intelligence | Two-year-old pricing in a fast market | Date every data point; flag stale ones |
| Vanity comparisons | Your best feature against their worst | Compare on the dimensions buyers weigh |
| Ignoring the status quo | Inertia missing from the set | Add "do nothing / current workaround" as an alternative |

## 3. Flags section (mandatory)

End the report with:

- **Red flags**: issues that could undermine the analysis or the business (e.g., a well-funded entrant targeting the same segment; a claimed differentiator a competitor already ships).
- **Yellow flags**: concerns that need investigation or monitoring.

If there are none, write "No flags identified"; do not drop the section.

## 4. Verification pass (before presenting)

After the report is drafted, audit it once, either yourself with fresh eyes or by handing the finished report (not your notes) to a fresh-context subagent if your environment supports one. Check:

1. **Claims without labels**: every number, percentage or factual assertion carries [Data], [Estimate], [Assumption] or [Opinion].
2. **Internal contradictions**: the same metric or price with different values in two sections; strengths in one profile contradicted in the positioning section; threat levels that disagree.
3. **Confidence vs. evidence**: a claim resting on one weak source is not rated high confidence; every major section states its confidence.
4. **Data gaps declared**: thin sections say they are thin.
5. **Flags present**, and not "No flags identified" when the content clearly shows risks.
6. **Stale data** older than 18 months is marked.
7. **False corroboration**: two claims citing the same source are not independent confirmation.
8. **Coherence**: every competitor in the summary has a profile; pricing figures match between the profile and the pricing comparison; every differentiation opportunity is backed by evidence from at least two places (e.g., a pricing gap plus a customer complaint).

Output the result as a short verification note:

```markdown
## Verification
- Critical issues: {n}  (could mislead a decision)
- Warnings: {n}
- Info: {n}

### Critical issues
- {issue}: {section} | problem | suggested fix
```

If there are critical issues, fix them before delivering or show them to the user and ask whether to fix or proceed. If there are only warnings, deliver with a one-line summary of them.
