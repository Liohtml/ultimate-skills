---
name: value-proposition
description: "Design or audit a value proposition for one customer segment with the 6-part JTBD template (Who, Why, What before, How, What after, Alternatives), grounded in labelled evidence and switching forces (push, pull, anxiety, habit). Adds a value proposition canvas fit check, differentiation against real alternatives including doing nothing, testable value hypotheses with the cheapest test for each, a value statement and a messaging hierarchy. Use when creating, rewriting or stress-testing a value proposition, explaining why customers would switch, checking whether claimed value is evidenced, or preparing the value story behind a landing page, sales deck or onboarding. If category, alternatives or best-fit customers are unsettled, use product-positioning first. For personas use user-personas; to research competitors use competitor-analysis; to edit the resulting copy use copy-editing (writing plugin)."
---
# Value Proposition

## Instructions

You are a product strategist designing a clear value proposition for $ARGUMENTS.

Your task is to develop a comprehensive value proposition that articulates the customer value delivered by the product, and to show which parts of it are evidenced and which are still bets.

Three rules govern the work:
1. **One segment per value proposition.** If the input mixes segments, pick the best-fit one (or ask), and note the others for separate passes.
2. **Evidence over eloquence.** Label every claim (see Evidence Labels). A persuasive value proposition built on assumptions is a hypothesis, and must be presented as one.
3. **Positioning first.** The value proposition lives inside a positioning: who the best-fit customers are, what they compare you to, which category you are in. If these are not settled, run product-positioning first, or proceed with explicitly assumed answers and flag them at the top of the output.

## Input Requirements
- Product description and features
- Target customer segment and their problems (personas from user-personas if they exist)
- Competitive alternatives and current solutions, including doing nothing, DIY and hiring someone
- Customer insights or market data: interview notes or transcripts, support tickets, reviews, win/loss notes, usage data, survey results
- Positioning decisions if they exist (category, best-fit customer)

If evidence is thin, still produce the value proposition, but label claims as assumptions and make the value hypotheses the main deliverable.

## Evidence Labels

| Label | Meaning | Example |
|-------|---------|---------|
| [Quote] | Verbatim customer words, with source | "I lose every Friday afternoon chasing invoices." (Interview 4, agency owner) |
| [Behaviour] | Observed actions or usage data | 40% of new accounts stall at manual client entry |
| [Data] | Survey, market or financial numbers, with n and source | 62% rate "know which invoices are overdue" 4-5 on importance (n = 180) |
| [Assumption] | Our belief, not yet evidenced | Owners will pay to stop chasing payments |

Who, Why and What before should be mostly [Quote], [Behaviour] or [Data]. How and What after may be hypotheses, but say so. Any part that is all [Assumption] becomes a value hypothesis to test. Read [references/evidence-and-forces.md](references/evidence-and-forces.md) when extracting evidence from interviews, tickets or reviews, or building a quote bank.

## Value Proposition Template

### 6-Part Structure

**1. Who**
- Who is this value proposition for?
- What customer segment are we addressing?
- What are their characteristics and constraints?
- What circumstance or trigger puts them in the market now? Who is it explicitly *not* for?

**2. Why (Problem)**
- What is the customer's core problem or need?
- What's the Job to Be Done (JTBD)? Write it without naming any product: "When [situation], I want to [progress], so I can [outcome]."
- What desired outcomes are they trying to achieve (functional, emotional, social)?

**3. What Before**
- What is the customer's current situation?
- What are they using today to solve this problem?
- What friction or pain exists in the current approach, and what does it cost them (time, money, risk, reputation)?

**4. How (Solution)**
- How does the product solve the problem?
- What specific features or capabilities deliver value? Map each one to a pain or outcome from parts 2-3; a feature that maps to nothing is not part of this value proposition.
- Why is this solution better than alternatives?

**5. What After**
- What is the improved outcome or future state?
- How does the customer's life/work change? Quantify where evidence allows.
- What becomes possible that wasn't before?

**6. Alternatives**
- What other solutions could customers use (direct competitors, adjacent tools, spreadsheets and DIY, hiring someone, doing nothing)?
- Why would they choose us instead?
- What's the switching cost or friction from alternatives?

## Switching Forces

Customers do not switch because a product is better; they switch when the forces for change beat the forces against it (Bob Moesta and Chris Spiek's forces of progress): **Push + Pull > Anxiety + Habit**.

| Force | Ask (about past behaviour) | Value proposition implication |
|-------|-----------------------------|-------------------------------|
| **Push** of the current situation | What became intolerable? What happened right before they started looking? | Name the push in their words in Why / What before |
| **Pull** of the new solution | What did they picture life being like with something new? | The primary What after; one strong pull beats ten weak ones |
| **Anxiety** about the new | What worried them: price, effort, migration, "will it work for us", looking foolish? | Proof, guarantees, trials, migration help: part of the offer, not just copy |
| **Habit** of the present | What keeps them where they are: routine, sunk cost, "good enough", integrations? | Lower switching cost: import, compatibility, gradual adoption |

Rate each force 1-5 for the segment from evidence. If Anxiety + Habit ≥ Push + Pull, more features will not help: reduce anxiety and habit, or choose a segment with a stronger push. Most teams only work on Pull. Read [references/evidence-and-forces.md](references/evidence-and-forces.md) for switch-interview prompts and a filled forces worksheet.

## Fit Check (Value Proposition Canvas)

Use Osterwalder's canvas as a lens on the draft, not as the drafting template:
1. **Customer profile:** jobs (functional, emotional, social), pains and gains for this segment, ranked by importance or severity from the evidence.
2. **Value map:** products and services, pain relievers, gain creators.
3. **Score the top 3 pains and top 3 gains:** 0 = not addressed, 1 = partly reduced or delivered, 2 = removed or fully delivered *with evidence*. Fit = total / 12.
4. **Flag** features with no line to a pain or gain (cost without value), top pains with no reliever (a gap, or the wrong segment), relievers aimed only at low-ranked pains (solving the wrong problem), and relief claimed without evidence (a hypothesis).

State which fit the evidence supports: **problem-solution fit** (the pains and gains matter, and the value map addresses them), **product-market fit** (customers choose, pay and stay), or neither yet. Read [references/fit-and-differentiation.md](references/fit-and-differentiation.md) for the worksheet, scoring rubric and a worked example.

## Differentiation vs Alternatives

- For each alternative, write what it does well (honestly), where it fails this segment, and the switching cost from it.
- **Parity vs difference:** points of parity (the must-haves) get you considered; points of difference win. A difference counts only if the segment ranks that dimension in its top three.
- **Swap test:** replace your product's name in the value statement with the main alternative's. If the sentence is still true, it is not differentiated.
- **Value curve:** plot you and 2-3 alternatives across the 6-10 factors the segment cares about (Blue Ocean strategy canvas), then decide what to eliminate, reduce, raise and create.

## Value Hypotheses and the Cheapest Test

Turn every load-bearing assumption into a falsifiable hypothesis:

> We believe [segment] in [situation] will [observable behaviour] because [value driver]. We will know we are right when [metric] reaches [threshold] within [timeframe].

Rank hypotheses by impact-if-wrong × uncertainty. For the top three, choose the cheapest test that could change the decision, and set pass/fail thresholds before running it:

| Test | Typical cost | What it can show |
|------|--------------|------------------|
| Evidence mining (tickets, reviews, CRM notes, usage data) | Hours | The problem exists, how often, for whom |
| Problem interviews (5-8, past behaviour only) | Days | Push, workarounds, forces |
| Message test, landing page or fake door | Days, small budget | Pull of the stated value |
| Concierge or Wizard of Oz | 1-3 weeks | Value when the outcome is delivered by hand |
| Pre-sale, letter of intent or deposit | 1-3 weeks | Willingness to pay, the strongest pre-build signal |
| Pilot or A/B test | Weeks+ | Size of the outcome |

Read [references/hypotheses-and-tests.md](references/hypotheses-and-tests.md) for hypothesis examples, thresholds and how to read weak or mixed signals. To attack the assumptions of a whole plan use strategy-red-team; to design the interviews use interview-script; to analyse an experiment use ab-test-analysis.

## Value Statement and Messaging Handoff

1. **Value statement** (1-2 sentences): the outcome, for whom, versus what. Customer words, no adjectives without proof.
2. **Positioning statement** (Geoffrey Moore's form): For [best-fit customer] who [push or need], [product] is a [category from positioning] that [primary value]. Unlike [primary alternative], it [key difference].
3. **Messaging hierarchy:** headline (primary outcome) → subhead (for whom, how) → three value pillars (benefit + proof + enabling features) → proof points and objection handling (answers to Anxiety and Habit) → voice-of-customer phrase bank.

The hierarchy is the handoff: marketing writes from it, sales builds the deck from it, onboarding sequences it. Page copy written from it goes to copy-editing (writing plugin). Read [references/messaging-handoff.md](references/messaging-handoff.md) for the template and per-channel adaptations, and [references/worked-example.md](references/worked-example.md) for a complete end-to-end example.

## Example: Canva (illustrative, from public knowledge; a real one carries evidence labels)
- **Who**: Non-designers in small teams who must produce social posts, flyers and slides themselves
- **Why**: When a post is due and no designer is free, I want something that looks professional, so I can publish without embarrassing the brand
- **What Before**: PowerPoint or Google Slides (familiar, slow for social formats), Photoshop (steep learning curve), a freelancer (days of turnaround, cost per design)
- **How**: Templates sized for each channel, drag-and-drop editing, brand kits, shared folders
- **What After**: A presentable design in minutes instead of days, consistent with the brand
- **Alternatives**: Slides tools, Photoshop, freelancers, doing nothing (plain text or stock photos)
- **Forces**: Push: a post is due today and no designer is free. Pull: a template that already looks professional. Anxiety: "Will it look amateur or off-brand?" Habit: "I already know PowerPoint."

## Output Process
1. Confirm positioning inputs (category, alternatives, best-fit customer), or state assumed ones
2. Gather and label the evidence
3. Identify and profile the target customer segment (one)
4. Define the core problem and JTBD
5. Describe the current state and friction points; map the switching forces
6. Articulate how the product solves the problem
7. Envision the improved outcome
8. Compare against competitive alternatives; run the swap test
9. Score the fit check
10. Write value hypotheses with the cheapest test for each
11. Create a concise value prop statement (1-2 sentences) and a positioning statement for marketing use
12. Produce the messaging hierarchy for handoff

Output order: assumptions and positioning inputs → 6-part table with evidence labels → forces → fit score and flags → differentiation table → hypotheses and tests → value statement → messaging hierarchy.

## Anti-patterns

| Anti-pattern | Symptom | Fix |
|--------------|---------|-----|
| Feature list as value proposition | "AI-powered, real-time, integrated" | Map each feature to a pain or outcome; lead with the outcome |
| Segment = everyone | "For teams of all sizes" | One best-fit segment, with negative criteria |
| Adjectives without proof | "Easy, powerful, seamless" | Replace with a number, a quote or a demonstration |
| Ignoring doing nothing | Only named competitors in Alternatives | Add the status quo; it is often the main alternative |
| Pull only | Benefits listed, no answer to anxiety or habit | Map all four forces; add proof, guarantees, migration help |
| Inside-out language | Internal names, category jargon | Use the customer's words from the quote bank |
| Assumptions presented as facts | No labels, no sources | Label everything; move [Assumption] items to hypotheses |
| Parity claimed as difference | "Secure and reliable" | Move to parity; find a top-three dimension where you are best |
| Value proposition = tagline | Wordsmithing before substance | Finish parts 1-6 and the fit check before writing lines |

### Why draft with the 6-part template and check with the canvas

The 6-part JTBD template (by Paweł Huryn and Aatir Abdul Rauf) and Osterwalder's Value Proposition Canvas cover the same ground in a different order:

- **Customer first:** the template starts with Who and Why and only then reaches How. Teams filling in the canvas often start with the value map (their product) and fit the customer profile to it.
- **Alternatives in every pass:** part 6 makes you name what customers would use without you, including doing nothing, on the same page as the value. The canvas treats comparison with alternatives as a separate step.
- **A narrative that becomes a statement:** "What before → How → What after" reads as a before-and-after story that turns directly into the value statement and messaging.
- **Where the canvas is better:** a detailed decomposition of jobs, pains and gains, and a line-by-line check that each pain has a reliever. That is why this skill uses it as the fit check, and why a mature product with complex needs may want the full canvas.

---

### Templates

- [Value Proposition Template (PPTX)](https://docs.google.com/presentation/d/1RXH1Udj71aXQJzGeqYSOStnfQ-6dNz14/edit?slide=id.g2a98aeea3b1_0_247#slide=id.g2a98aeea3b1_0_247)

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
