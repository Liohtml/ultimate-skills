---
name: competitor-analysis
description: "Research and profile a product's direct competitors (typically 5, plus status-quo and adjacent alternatives): positioning, strengths, weaknesses, pricing and go-to-market, per-competitor threat rating, differentiation opportunities and a positioning recommendation, with every claim labelled [Data]/[Estimate]/[Assumption]/[Opinion], a mandatory red/yellow flags section and a verification pass for contradictions, stale data and false corroboration. Use when doing competitive research, preparing a competitive brief or landscape, comparing pricing across competitors, or looking for differentiation gaps. For choosing the market category and positioning itself use product-positioning; for the customer-value statement use value-proposition; for setting your own prices use pricing-strategy."
---

# Competitor Analysis

## Purpose
Conduct a comprehensive competitive analysis to understand the landscape, identify 5 direct competitors, and uncover differentiation opportunities. This skill maps competitive positioning, synthesizes competitor strengths and weaknesses, and highlights opportunities for strategic differentiation.

## Instructions

You are a strategic product analyst and competitive intelligence expert specializing in competitive positioning and market landscape mapping.

### Input
Your task is to analyze the competitive landscape for **$ARGUMENTS** in the **[market/industry segment]** (if specified).

Conduct web research to identify direct competitors. If the user provides market research, competitor data, pricing sheets, feature comparisons, or customer feedback about competitors, read and analyze them directly. Synthesize data into a comprehensive competitive view.

### Analysis Steps (Think Step by Step)

1. **Market Scoping**: Define the market, industry, and addressable customer base for $ARGUMENTS
2. **Competitor Identification**: Use web search to identify 5 primary direct competitors
3. **Competitive Intelligence**: Research each competitor's positioning, features, pricing, go-to-market strategy
4. **Strengths & Weaknesses**: Assess competitor capabilities, limitations, and market positioning
5. **Differentiation Mapping**: Identify gaps, overlaps, and opportunities for $ARGUMENTS to differentiate
6. **Strategic Synthesis**: Develop insights about competitive dynamics and future threats

### Output Structure

**Market Overview & Definition**
- Market size and growth trends
- Primary customer segments and use cases
- Key success factors in this market
- Market dynamics and competitive intensity

**Competitive Set Summary**
- 5 primary direct competitors identified
- Market positions: leaders, challengers, niche players
- Estimated market share or positioning
- Notable adjacent or indirect competitors
- Status-quo alternatives (doing nothing, spreadsheets, agencies, in-house builds) and what triggers a switch

For each of the 5 competitors:

**Competitor Profile**
- Company name, founding date, funding/status
- Primary market focus and customer segments served
- Estimated market share or customer base size
- Market positioning and go-to-market strategy

**Core Product Strengths**
- Key features and capabilities
- Unique competitive advantages
- Customer value proposition
- Technology differentiation or moats
- Customer satisfaction and retention signals

**Product Weaknesses & Gaps**
- Missing features or use cases
- Known limitations or pain points for customers
- Technical or operational weaknesses
- Market positioning gaps
- Customer dissatisfaction areas

**Business Model & Pricing**
- Pricing structure (per-seat, per-usage, flat-fee, freemium, etc.)
- Price point(s) in market
- Go-to-market channels and sales motion
- Revenue model and growth stage

**Competitive Threats & Advantages**
- How this competitor threatens $ARGUMENTS
- Existing customer base and switching costs
- Strategic partnerships or ecosystems
- Recent product updates or strategic moves
- Threat rating: High / Medium / Low, with the evidence behind it

**Differentiation Opportunities for $ARGUMENTS**

- Unmet customer needs across competitive set
- Feature/pricing/UX opportunities to stand out
- Target segments underserved by competitors
- Jobs-to-be-done not effectively solved by competitors
- Channel or go-to-market approaches not yet deployed
- Potential partnerships or integrations competitors lack

**Competitive Positioning Recommendation**
- Recommended competitive positioning for $ARGUMENTS
- Key differentiators to emphasize
- Segments or use cases to target or avoid
- Competitive threats to monitor
- 12-18 month competitive risks and opportunities

**Flags and Verification**
- Red flags and yellow flags
- Data gaps (what could not be found)
- Verification note (see Evidence and Verification below)

## Evidence and Verification

> Includes material adapted from ferdinandobons/startup-skill `startup-competitors` (MIT); see [references/evidence-and-verification.md](references/evidence-and-verification.md).

Load [references/evidence-and-verification.md](references/evidence-and-verification.md) before writing the report. In short:

- Label every major claim **[Data]** (with source and date), **[Estimate]** (with assumptions), **[Assumption]** or **[Opinion]**. Write "not found" rather than guess; mark data older than 18 months.
- Acknowledge real competitor strengths, look for disconfirming evidence, represent review sentiment proportionally, and include the status quo ("do nothing", spreadsheets, in-house) as an alternative.
- Rate each competitor's threat High / Medium / Low with the reason.
- End with **Red flags** and **Yellow flags** (write "No flags identified" if there are none).
- Before presenting, run the verification pass (unlabelled claims, contradictions, confidence vs. evidence, stale data, same-source "corroboration", every opportunity backed by two pieces of evidence) and fix or surface critical issues.

## Best Practices

- Research current competitor websites, pricing pages, and customer reviews
- Use web search to identify product launches, funding, executive moves
- Distinguish between direct competitors and adjacent alternatives
- Validate competitive insights across multiple sources
- Identify both obvious and subtle differentiation opportunities
- Consider customer pain points not yet addressed in market
- Look for emerging competitors or new market entrants
- Flag competitors gaining traction or gaining market share
- Consider long-term competitive dynamics and market shifts

## Related skills

- **product-positioning**: turn the landscape into a positioning decision (alternatives, only-we attributes, best-fit customers, category).
- **value-proposition**: articulate the customer value you will deliver against these alternatives.
- **pricing-strategy**: set your own pricing using the competitive pricing collected here.
- **strategy-red-team**: attack the strategy that this analysis leads to.

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
