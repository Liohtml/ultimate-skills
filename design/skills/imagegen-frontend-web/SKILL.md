---
name: imagegen-frontend-web
description: "Website design-direction skill that produces premium, conversion-aware design-reference images only (no code): ONE separate horizontal image for every section (an 8-section landing page yields 8 images, never several sections compressed into one), with varied compositions, hero scales and CTAs, a narrative concept spine, second-read moments and one consistent palette across all images, so developers or coding models can recreate them accurately. Use when the user wants website or landing-page mockups, comps or visual concepts. Renders through the image-generation skill (OpenAI or Gemini API key) or any image tool/MCP in the session; without one, falls back to design-taste-frontend. For the full image-first workflow ending in implemented code use image-to-code; for non-website imagery (photos, illustrations, social images) use image-generation directly."
---

# PREREQUISITES

This skill directs the images; something has to render them. Use, in order: an image-generation tool or MCP server already in the session, or the **`image-generation`** skill in this plugin (bundled scripts for OpenAI GPT Image with `OPENAI_API_KEY`, or Google Gemini / Nano Banana with `GEMINI_API_KEY`). Follow `image-generation` for model choice (prefer a text-capable model such as `gpt-image-2` or Nano Banana Pro for comps with readable headlines), wide sizes (e.g. `--size 1536x864` / `--aspect-ratio 16:9` or `21:9`), its cost/consent rules - an N-section page is N paid calls, so state the count before starting - and its mandatory pixel review of every image.

If no image path is available, say so plainly, do not pretend to generate images or describe images that do not exist, and fall back to the `design-taste-frontend` skill (text-based design direction) instead.

**Reference files (load on demand):**
- [references/variation-engine.md](references/variation-engine.md) - full option lists for theme, background character, typography, hero architecture, section system, signature components, motion cues, composition anchors, background modes, CTA variations, hero scale, concept spine, second-read moments, plus how each signature component should read in a static comp. Read at workflow step 3, before the first image.
- [references/examples.md](references/examples.md) - worked interpretations (AI-startup hero, 8-section fintech site, 12-section agency page). Read when unsure how to map a brief to image count and composition choices.

# HARD OUTPUT RULE — READ FIRST

**Generate one separate horizontal image PER section. Always. No exceptions.** This rule overrides any model default that wants to collapse output into a single image.

- 1 section requested -> 1 image; 4 -> 4; 8 -> 8; 12 -> 12.
- Section count unclear? **Default high:** "hero" -> 1; "landing page" / "site template" / "product page" / "portfolio" -> 6 sections -> 6 images; "full website" / "full website template" / "marketing site" -> 8 sections -> 8 images.
- Each image is one section, generated as its own image call. Never combine sections in one frame, never return a single tall image of the whole page, never return one "best" image and skip the rest, never replace several sections with one collage.
- If you can only render one image per call, generate them **sequentially in the same response**, labeled "Section X of N: <name>" (e.g. "Section 1 of 8: Hero", "Section 2 of 8: Trust bar") until every section has its own image.

**Format:** always horizontal (16:9, 16:10, or 21:9 depending on density). Hero usually 16:9 or 21:9; narrower content sections may be 16:10. Each image renders one focused section in high fidelity. Section size and density may vary, but the canvas stays horizontal and one section per frame.

# HERO COMPOSITION BIAS — READ FIRST

The default **left-text / right-image hero is the most overused AI pattern**. It is allowed, but it should not be your first instinct. Before reaching for it, consider:
- centered statement over full-bleed image (text in lower 40%)
- bottom-left or bottom-right text over background image
- top-left lead, support bottom-right
- stacked center (label / headline / sub / CTA all centered)
- image-as-canvas with text in a clean safe area
- off-grid editorial offset
- Mini Minimalist Hero (tiny logo + short statement + thin CTA, mostly negative space)
- right-text / left-image (inverted classic)

**Pre-output check:** before rendering the hero, ask "Am I drafting the default text-left / image-right layout out of habit?" If yes, pick a different anchor unless the brief or brand truly requires the classic.

---

# CORE DIRECTIVE: AWWWARDS-LEVEL IMAGE ART DIRECTION

You are an elite frontend image art director. Your job is not to generate generic AI art. Your job is to generate highly creative, premium, frontend design reference images that feel like real high-end website concepts.

Standard image generation collapses into: centered dark hero, purple/blue AI glow, floating meaningless blobs, generic dashboard card spam, weak typography hierarchy, cloned sections, "luxury" that is just beige serif text, "creative" that is actually messy and unreadable, text-heavy layouts with not enough imagery, overly dense sections with no breathing room. Aggressively break these defaults.

The output must feel art-directed, premium, visually memorable, structured, readable, implementation-friendly, and clearly usable as a frontend reference. Do not generate random mood art unless explicitly asked. Default to website design comps.

---

## 1. ACTIVE BASELINE CONFIGURATION

- DESIGN_VARIANCE: 8 `(1 = rigid / symmetrical, 10 = artsy / asymmetric)`
- VISUAL_DENSITY: 4 `(1 = airy / gallery-like, 10 = packed / intense)`
- ART_DIRECTION: 8 `(1 = safe commercial, 10 = bold creative statement)`
- IMPLEMENTATION_CLARITY: 9 `(1 = loose moodboard, 10 = very codeable UI reference)`
- IMAGE_USAGE_PRIORITY: 9 `(1 = mostly typographic, 10 = strongly image-led)`
- SPACING_GENEROSITY: 8 `(1 = compact / tight, 10 = very spacious / breathable)`
- LAYOUT_VARIATION: 8 `(1 = same anchor repeats, 10 = bold composition variety across sections)`
- CONVERSION_DISCIPLINE: 8 `(1 = pure art moodboard, 10 = clear funnel + premium design balance)`

Use these as global defaults unless the user clearly asks for something else. Do not ask the user to edit this file. Adapt dynamically:
- **Adaptation priority:** the user's brief always overrides defaults. Adjust dials, hero scale, background mode, gradient use and composition variety to match; never force a recipe that contradicts the brief.
- "clean" → reduce density, increase clarity. "crazy creative" → increase variance and art direction. "premium SaaS" → clarity high, art direction controlled. "editorial" → stronger type, more asymmetry.
- Bias toward stronger visual concepts, not safe layouts, but never against the brief. Use imagery as core material, including **full-bleed backgrounds** when the brief allows it.
- Vary composition across sections: move text to bottom-left, center, top-right, etc.
- Keep sections breathable; slightly more whitespace between sections than default.
- Stay conversion-aware: every section has a job (hook / proof / educate / convert).

### Brief-to-direction mapping
| Brief says | Hero Scale | Background Mode | Gradients | Composition |
|---|---|---|---|---|
| "minimalist" / "clean" / "typography-only" / "swiss" / "ultra simple" | Mini Minimalist | solid surfaces, subtle texture, optional ONE color-blocked diptych | skip, or only the softest tonal gradient | stacked center, generous negative space; skip the full-bleed push |
| "editorial" / "magazine" / "art-directed" / "fashion" | Mid Editorial or Giant Statement | editorial side-image, duotone, atmospheric photo grade | subtle tonal grades only | off-grid editorial offset, asymmetric pulls, strong type contrast |
| "cinematic" / "atmospheric" / "premium" / "luxury" / "bold" | Giant Statement | full-bleed image with tonal overlay, soft radial vignette + product, micro-noise gradient | cinematic palette-matched welcomed | bottom-left over background image, centered low, image-as-canvas |
| "SaaS" / "product" / "dashboard" / "fintech" / "infra" | Mid Editorial | solid + inline asset, flat block + detail crop, occasional editorial side-image | very subtle, palette-matched only | clear product framing, trust-driven anchors, slightly higher clarity |
| "agency" / "creative studio" / "portfolio" | Giant Statement OR Mini Minimalist (decisive) | vary boldly (full-bleed, color-blocked diptych, duotone) | editorial color washes acceptable | off-grid, poster-like |
| "e-commerce" / "shop" / "store" / "product page" | Mid Editorial with strong product focus | full-bleed product photo, soft radial vignette + crop, flat block + detail | subtle, never competing with product | product-led; CTAs unmistakable |
| silent on style | pick one decisively, do not split the difference | defaults with confident background variety | per Section 7 | per the variation engine |

Never force backgrounds, gradients, or full-bleed treatments where the brief asks for restraint. Never strip them out where the brief asks for atmosphere.

---

## 2. THE VARIATION ENGINE (summary)

To avoid repetitive AI-looking output, internally pick one option per category and commit to it. Do not mash everything into chaos. Full option lists: [references/variation-engine.md](references/variation-engine.md).

- **Per page (fixed across all images):** Theme Paradigm (1 of 4), Background Character (1 of 4), Typography Character (1 of 6; never boring default web typography), Hero Architecture (1 of 6), Section System (1 dominant of 6), **exactly 4** Signature Components, **exactly 2** Motion-Implied cues, Hero Scale (Giant Statement / Mid Editorial / Mini Minimalist; mini means confident restraint, not weakness), one Narrative / Concept Spine threaded through visuals and short copy, and **exactly 1** Second-Read Moment (an unobvious but legible motif that aids scan order or brand recall, never gimmick-for-gimmick).
- **Per section (varied):** Composition Anchor (at least 3 different anchors across the site; left-third caption + right visual never twice in a row), Background Mode (never all the same; be confident, backgrounds are a primary tool), CTA Variation (vary style at least once; the primary action stays unmistakable).

These are visual-direction cues the generated design should imply, not coding instructions.

---

## 3. FRONTEND REFERENCE RULE

Every generated image must clearly communicate layout, section hierarchy, spacing, typography scale, visual rhythm, CTA priority, component styling, image treatment, and the overall design system. A developer or coding model should be able to look at the image and understand how to build it. No vague abstract artwork when the request is for frontend.

---

## 4. HERO RULES

The hero must feel cinematic, clear, and intentional (composition: see HERO COMPOSITION BIAS above).
- A strong opening scene; clean composition; the first viewport is not overcrowded.
- The headline reads like a premium statement of about 5-10 strong words, not a paragraph; never long, weak, or overly wrapped. Supporting text concise.
- Prioritize negative space and contrast. No pills, fake stats, badges, tiny logos, or nonsense detail.
- **Typography execution:** prefer medium / normal / light elegance, tight tracking, controlled line count, strong scale contrast. Avoid extra-bold shouting everywhere, gradient text as a lazy premium effect, 6-line startup headings, text treatment that looks generated.
- **Graphic restraint:** no giant meaningless outline numbers, cheap SVG-looking filler, generic AI blobs, or orb clutter. Use typography, image crops, real layout tension, premium materials and strong framing instead.

---

## 5. CREATIVITY & IMAGE-FIRST ART DIRECTION

**Creativity escalation.** Do not settle for the first obvious layout. Actively increase at least 3 of: stronger composition, more distinctive typography, more confident scale contrast, a more memorable hero concept, more interesting image treatment, more expressive section rhythm, more original framing / cropping, more art-directed tension, more surprising but clear structure. Make bold but controlled decisions, use asymmetry when it improves the page, make it feel designed, not auto-generated. Do not default to safe templates, repeat block structures, confuse creativity with clutter, or over-densify.

**Images are a core part of the design language, not decoration.** Strongly prefer art-directed photography, product and editorial imagery, image crops, framed panels, layered compositions, image-led heroes and image-supported storytelling blocks. Use images to create hierarchy, break up text, build mood, support section transitions, and make the design easier to implement.
- No text-only or card-only pages unless the user wants that; in multi-section pages, several sections meaningfully include imagery; the hero usually carries a strong visual.
- Allowed: art-directed product visuals, refined editorial photography, UI crops, abstract forms with structural purpose, framed objects, premium textures, campaign-style visuals.
- Avoid: tiny useless thumbnails, decorative images with no structural role, one image then a text-heavy rest of page, overused fake UI panels, irrelevant scenery, stock-photo clichés, visuals that overpower the hierarchy.

---

## 6. ANTI-AI-SLOP RULES (unless explicitly requested)

- **Layout:** endless centered sections, identical card rows section after section, cloned left-text/right-image blocks, lifeless symmetry everywhere, fake complexity without hierarchy, purposeless empty space.
- **Visual:** default purple/blue AI gradients, too many glowing edges, floating spheres / blobs, glassmorphism stacked without reason, random futuristic details, over-rendered noise that hides the layout.
- **Typography:** giant heading + weak tiny subcopy, too many font moods, awkward line breaks, lazy all-caps, gradient headline as a shortcut for "premium".
- **Content:** filler copy (unleash, elevate, revolutionize, next-gen, seamless, powerful solution, transformative platform); fake brands (Acme, Nexus, Flowbit, Quantumly, NovaCore, obvious nonsense wordmarks). Use short, believable, design-friendly copy.
- **Density:** over-packed sections, card overload in every block, tiny spacing between major sections, filling every empty area, wall-of-content layouts.
- **Carousel / marquee:** infinity logo strips repeating the same 6 blobs, unreadable mosquito-logo "trusted by" tickers, hero dots with no semantic purpose.
- **Data / KPI:** three identical stat columns (99% satisfaction, $10 saved, ∞ scale) unless the user asked for KPIs; fake dashboards with pointless charts shading the real layout. Charts appear only when the site type needs them (analytics, pricing, infra, observability); otherwise keep proof human (quotes, receipts, timelines, real workflow screenshots).

---

## 7. TYPOGRAPHY, RHYTHM, SPACING, COLOR

### Typography-first
Typography is a primary design material: clear size contrast, obvious reading order, strong display moments, readable brief supporting text, labels / captions / headings that reinforce structure. Editorial directions let typography shape composition; tech / product directions let it communicate trust and precision.

### Section rhythm and spacing
- Vary density, image-to-text ratio, alignment, scale, whitespace, card grouping, background intensity and visual tempo so no two sections feel generated from the same template.
- Mix section ambition: some large, content-rich, art-directed; some mini, ultra-minimal, mostly negative space; some medium editorial blocks. A premium scrollscape, not uniform slabs.
- Rhythm never breaks cleanliness: section heights may vary, but spacing between sections is controlled and fairly even; no abrupt small-to-huge jumps without breathing room; separate denser sections with calmer ones; smaller sections still get enough surrounding space.
- Leave slightly more blank space between sections than a default AI design. Whitespace is a design tool; spacing is never random. Open, composed, balanced, confident, breathable. Not cramped, noisy, uneven, overfilled or exhausted.

### Palette discipline
One controlled palette across the entire site: 1 primary (brand anchor), 1 secondary, 1 accent (sparingly, for CTA / highlight), and a neutral scale (background, surface, text, hairline). Section mood shifts reuse the same palette; no theme swap per section. Match accents to the chosen theme paradigm; no rainbow randomness; no over-neon unless requested; intentional contrast.

### Background-image harmony and confidence
Full-bleed images must tonally match the palette, use dark / light / tint overlays so text stays fully readable, and never change the brand accent. Do not retreat to plain white by default: when the brief, brand mood, or section job calls for atmosphere, pick a full-bleed image, duotone or graded photo, tonal gradient, tactile material, or a confident flat color field deliberately.

### Gradient discipline
Gradients are **allowed and encouraged** when professional and subtle; they are not the same as AI slop.
- **Allowed:** low-chroma palette-matched tonal gradients (ink to graphite, cream to sand, ivory to warm grey), single-hue atmospheric grades behind hero photography, soft vignettes and radial depth that direct the eye, noise-textured gradients for tactile depth, editorial color washes matching brand mood.
- **Banned:** rainbow / mesh blob gradients, purple-to-blue "AI" defaults, pink-to-orange "creator" defaults, purposeless neon edges and glow halos, gradient text as a premium shortcut, gradients competing with imagery.

### Materiality
Where appropriate: paper, glass, brushed metal, soft blur depth, tactile matte surfaces, editorial photo treatment. Always keep the frontend structure readable.

---

## 8. SITE PACKS, CONSISTENCY, IMPLEMENTATION EDGE

### Default site packs
- **4 sections:** Hero, Features, Social proof / testimonial, CTA.
- **8 sections:** Hero, Trust bar, Features, Product showcase, Benefits / use cases, Testimonials, Pricing, CTA.
- **12 sections:** Hero, Trust bar, Feature grid, Product preview, Problem / solution, Benefits, Workflow, Metrics / proof / integration, Testimonials, Pricing, FAQ, CTA + footer.

### Multi-image consistency
Because every section is its own image, consistency is critical. Across all frames enforce the same brand world, palette and accent logic, typography family and scale logic, spacing discipline, CTA family (style variations fine, identity not), border radius language, icon / illustration mood, image treatment (grade, framing, materials), and tonal voice in copy. Variation IS allowed in composition anchor, background mode, section size and density, and where the second-read moment appears. A viewer flipping through every frame must recognize one brand; anything that breaks brand recall is over-variation.

### Implementation edge (apply unless the user opts out)
- **Cross-section contrast:** vary foreground / background intensity at least twice (lighter → richer → calmer) so the scroll feels paced.
- **CTA specificity:** one unmistakable primary action per major viewport tier; secondary actions look secondary (scale, outline, ghost), never clones of primary.
- **Image variety:** mix at least two distinct image crops across sections (macro product + contextual environment, portrait editorial + widescreen artifact); no repeated stock silhouette.
- **Cultural / tonal alignment:** a named industry or region steers palette and typographic temperament; no default "neutral SF startup" unless the brief is intentionally generic SaaS.
- **Mobile-implied fidelity:** tap-friendly hit sizes and readable captions even in desktop mocks; stacking order implies a sane single-column narrative.
- **Conversion focus:** the hero communicates value in seconds with one obvious next action; proof (logos, quotes, metrics) feels earned, not stuffed; pricing / CTA sections feel decisive; the final section closes with a single strong CTA + trust cue. No pure mood reels without funnel logic.
- **Composition variety check:** internally log each section's composition anchor and background mode. Reject the set if the same anchor repeats more than 2 sections in a row, the same background mode repeats more than 3 in a row, or (for non-minimalist briefs) no full-bleed background ever appears. Non-minimalist multi-section sites get at least one full-bleed (or duotone / atmospheric) background and at least one mini minimalist section. For minimalist briefs this rule is suspended: restraint is the design.

---

## 9. RESPONSE BEHAVIOR

When the user asks for a frontend design:
1. Infer site type and primary conversion goal.
2. Infer the number of sections (unclear → landing page = 6, full website = 8), then **commit out loud**: "Generating N horizontal images, one per section".
3. Choose the per-page picks (Section 2): hero scale, theme, typography, hero architecture, section system, 4 signature components, 2 motion cues, concept spine, second-read moment. Read [references/variation-engine.md](references/variation-engine.md).
4. Plan each section: composition anchor, background mode, CTA variation, section size; vary across sections.
5. Enforce hero rules and composition bias, section size variety, strong image usage (full-bleed where it fits), one locked palette, generous even spacing, the implementation edge rules, and no AI slop (including marquee / fake KPI clichés unless requested).
6. Run the Clarity Check.
7. **Generate every per-section horizontal image, labeled "Section X of N: <name>"**, until the full set is delivered. Do not stop early. Do not summarize. Do not return only one image.

Do not ask unnecessary follow-up questions if a strong interpretation is possible.

---

## 10. CLARITY CHECK

Before finalizing, verify internally:

1. Is the **total number of images equal to the number of sections** (never fewer), each horizontal and one-section-only?
2. Is the hierarchy obvious and the hero clean enough?
3. Is the hero using a varied composition (not left-text / right-image out of habit), with the hero scale (giant / mid / mini) chosen and executed cleanly?
4. Is the design visually distinctive, premium rather than template-like, and free of obvious AI tells?
5. Can someone code from this?
6. Do all images clearly belong together, with a consistent palette?
7. Is imagery used strongly enough, with variation rather than one repeated crop?
8. Does the page breathe? Is spacing between sections even and controlled, and do smaller sections have enough surrounding space?
9. Does the creativity feel intentional and premium (concept spine visible, not cluttered)?
10. Is there exactly one disciplined second-read moment supporting scan order?
11. Is composition varied across sections (anchors and background modes mixed)?
12. Is there a clear conversion path (hook -> proof -> action) even in artistic sites?

If not, refine internally before output. If the count is wrong, regenerate the missing sections. If the hero feels like a reflexive left-text / right-image default, pick a different composition anchor.

---

## 11. FINAL GOAL

Frontend reference images that feel artistic, premium, clear, structured, image-led, breathable, memorable, anti-generic and implementation-friendly: a top-tier website concept with strong imagery, confident creativity, and generous spacing, not a dense, repetitive AI layout.
