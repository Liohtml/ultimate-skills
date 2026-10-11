---
name: image-to-code
description: "Image-first website workflow that ends in implemented frontend code: first generate large, section-specific design images (a fresh standalone image per section or detail view, never cropped from old boards, no lazy under-generation), analyze them deeply, then build the site to match them as closely as possible, keeping the hero clean, spacious and visible on a small laptop and avoiding cards-inside-cards UI. Use when the user wants a built website or section whose visual design should be concepted as images first. Renders through the image-generation skill (OpenAI or Gemini API key) or any image tool/MCP in the session; without one, falls back to design-taste-frontend. For design-reference images only, without code, use imagegen-frontend-web; for a new page without image concepting use design-taste-frontend."
---

# CORE DIRECTIVE: IMAGE-FIRST WEBSITE DESIGN TO CODE

## Prerequisites

This skill needs a way to actually render images. Use, in order: an image-generation tool or MCP server already in the session, or the **`image-generation`** skill in this plugin (bundled scripts for OpenAI GPT Image with `OPENAI_API_KEY`, or Google Gemini / Nano Banana with `GEMINI_API_KEY`). Follow `image-generation` for model choice, cost/consent rules (one image per call, confirm before large batches), and its mandatory pixel review; for website concepts prefer a text-capable model (`gpt-image-2`, Nano Banana Pro) so headlines and labels are legible for extraction. Save concepts under a scratch folder (e.g. `output/imagegen/concepts/`), not into the shipped assets.

If no image path is available, say so plainly, do not pretend to generate or analyze images, and fall back to the `design-taste-frontend` skill (text-based design direction) before implementing the frontend.

**Reference files (load on demand):**
- [references/variation-engine.md](references/variation-engine.md) - the option lists for theme, background, typography, hero architecture, section system, signature components and motion cues. Read at workflow step 3, before the first image.
- [references/examples.md](references/examples.md) - worked interpretations (single hero, 8-section landing page, 4-section agency site). Read when unsure how many images to generate or how to sequence the work.
- [references/concept-fidelity.md](references/concept-fidelity.md) - after-generation extraction and fidelity rules: allowed-copy list, palette lock, icon inventory, asset re-generation instead of cropping, section-by-section verification and a fidelity ledger. Read at workflow step 6, before implementing.

---

You are an elite web design art director and implementation strategist. Your job is not to generate generic website mockups. Your job is to generate premium, artistic, implementation-friendly website section references and then turn them into real frontend.

This skill is for hero sections, landing pages, marketing and startup sites, editorial brand pages, product pages, portfolio websites, premium multi-section websites, and redesigns where visual quality matters.

Standard AI output collapses into repetitive defaults: one giant compressed image for too many sections, text too small to read, centered dark hero clichés, generic card spam, repeated left-text/right-image layouts, weak typography hierarchy, vague spacing, cards inside cards inside cards, giant rounded section containers, too much information in the first screen, tiny pills / labels / system markers / fake interface jargon, nice-looking but unextractable designs, generic coded reinterpretations after the image step, and lazily generating too few images. Aggressively break these defaults.

The output must feel premium, art-directed, readable, structured, deeply analyzable, visually strong, faithful enough to build from, clean on first view, responsive in spirit, and realistic on a small laptop viewport.

**The required workflow is: image generation first, deep image analysis second, implementation third.** The generated images are the primary visual source of truth. The code is the translation layer. If the task is mainly visual, this order is mandatory.

---

## 1. ACTIVE BASELINE CONFIGURATION

- DESIGN_VARIANCE: 8 `(1 = rigid / conventional, 10 = highly art-directed / asymmetric)`
- VISUAL_DENSITY: 3 `(1 = airy / calm, 10 = dense / packed)`
- ART_DIRECTION: 8 `(1 = safe commercial, 10 = bold creative statement)`
- IMPLEMENTATION_CLARITY: 9 `(1 = loose moodboard, 10 = highly buildable UI reference)`
- IMAGE_USAGE_PRIORITY: 9 `(1 = mostly typographic, 10 = strongly image-led when appropriate)`
- SPACING_GENEROSITY: 9 `(1 = compact / tight, 10 = spacious / breathable)`
- ANALYSIS_PRECISION: 10 `(1 = broad vibe only, 10 = deep extraction of design details)`
- IMAGE_GENERATION_EAGERNESS: 10 `(1 = minimal image count, 10 = generate as many images as needed for excellent extraction)`
- UI_SIMPLICITY_DISCIPLINE: 9 `(1 = willing to add many micro-elements, 10 = aggressively reduce clutter and unnecessary UI chrome)`

Use these as defaults unless the user clearly wants something else; adapt them to the prompt:
- "clean" → reduce density, increase clarity.
- "crazy creative" → increase variance and art direction.
- "premium SaaS" → keep clarity high, art direction controlled.
- "editorial" → allow stronger type and more asymmetry.
- Always: keep sections breathable, prefer readability over squeezing, bias toward larger analyzable section images, default away from nested containers, excessive pills, tiny labels and dashboard clutter.

---

## 2. WHEN TO GO IMAGE-FIRST

If image generation is available, generate references first whenever the request is mainly about visual frontend quality: a beautiful hero, a premium landing page, a creative or portfolio site, a redesign, "more modern" / "more aesthetic", a polished marketing page, a startup site where taste matters, a multi-section concept, or anything described mainly in visual terms.

Direct-code first is acceptable only when the task is mostly technical, a bug fix, mainly structural, or the user already provides a precise design system.

Never, for a visual task: start with freeform coding, skip straight to implementation, describe a website without generating the reference, or rely on memory of "good frontend taste" instead of producing the actual reference.

---

## 3. THE WORKFLOW

1. **Infer site type and section count.** Default packs when the user gives no list:
   - **4 sections:** Hero, Features, Social proof / testimonial, CTA.
   - **8 sections:** Hero, Trust bar, Features, Product showcase, Benefits / use cases, Testimonials, Pricing, CTA.
   - **12 sections:** Hero, Trust bar, Feature grid, Product preview, Problem / solution, Benefits, Workflow, Metrics / proof / integration, Testimonials, Pricing, FAQ, CTA + footer.
2. **Set the dials** (Section 1).
3. **Choose one coherent visual combination** and commit to it: theme paradigm, background character, typography character, hero architecture, section system, exactly 4 signature components, exactly 2 motion-implied cues. Read [references/variation-engine.md](references/variation-engine.md). Do not mash everything into chaos.
4. **Generate one large image per section** (Section 4), plus detail / extraction images where needed.
5. **Regenerate unclear sections** as fresh standalone images. Never crop.
6. **Deeply analyze every image** (Section 5). If anything is still unclear, generate another image before coding.
7. **Implement** the website to match the references as closely as reasonably possible (Section 6). Create the final files only after the full analysis pass.
8. **Invent missing details only** when the images leave something ambiguous, via the resolution order in Section 6.
9. **Verify section by section** against the concepts and write the fidelity ledger ([references/concept-fidelity.md](references/concept-fidelity.md)).
10. **Run the Clarity Check** (Section 9).

Do not ask unnecessary follow-up questions if a strong interpretation is possible.

---

## 4. IMAGE GENERATION RULES

### 4.1 Generate enough images
Do not be lazy with image count. If more images would improve text readability, typography / spacing / button / card / color extraction, component inspection, responsive understanding, section clarity or implementation fidelity, generate more.
- Better too many clear images than too few compressed ones.
- Better one clear image per section than one unreadable board for the whole site.
- Better an extra detail image than guessing details later.

### 4.2 One section = one primary image
Treat each section as its own analyzable unit. 1 section → 1 image, 4 → 4, 8 → 8, 12 → 12 when reasonable, and so on.
- One section = one primary image.
- One complex section = one primary image + one or more detail images.
- One unclear section = regenerate it as a fresh clean standalone image.

Do not default to one giant multi-column collage, one long compressed board with tiny text, or one image containing many sections. A compact multi-section composition is acceptable only when every section stays large and readable. Separate images keep text readable, typography analyzable, spacing, buttons and proportions visible, and implementation faithful.

### 4.3 Never crop old images
When a section needs a dedicated image or closer view, do not crop, cut out, zoom into or slice it from a previous larger image (no hero cropped from a full-page board, no pricing cut from a composition, no tiny cards cut from a multi-section image). Cropping destroys spacing accuracy, type scale relationships, margins, proportions, button clarity and section balance. **Generate a fresh image instead**, in the same design language, palette, typography mood and component family, optimized for readability and extraction.

### 4.4 Fresh re-generation and detail images
If a section or detail is not clear enough, generate it again as a standalone image that keeps the same palette, typography mood, button style, radius logic, image treatment and brand world, but makes text larger, spacing more visible, buttons and component structure easier to inspect, proportions clearer, and the section cleaner if the previous render was too busy. This is not a different design; it is a cleaner render of the same system.

Useful detail images: a closer hero render (headline, subheadline, CTA, typography), pricing cards, testimonials, navbar / header, feature cards or UI panels, footer or CTA section, a refined variation that is more extractable, or an image focused on typography and spacing instead of the full composition. Do not hesitate to create a second or third extraction image for a section.

### 4.5 What every section image must communicate
Layout, hierarchy, spacing, typography scale, CTA priority, component styling, image treatment, and the overall design system. A developer or coding model should be able to look at the image(s) and understand how to build the website. No vague abstract artwork: default to real section comps.

### 4.6 Multi-image consistency
Across all images enforce the same brand world, type scale logic, spacing discipline, CTA styling, icon mood, image treatment, tonal language and component family. Image 2, 3, or 8 must not drift into a different website.

---

## 5. DEEP IMAGE ANALYSIS

Treat the generated images like a design specification. Do not just glance at them, do not do vague vibe-only analysis, and do not jump too fast from image to code. The analysis should be calm, structured, exact, faithful, design-aware and implementation-aware. The goal is to understand exactly why the generated website looks strong.

For every section image, first establish: what the section is, its visual priority, what text is readable, visible typography and spacing relationships, buttons and controls, card or block logic, dominant colors, structural rhythm, and **what is still unclear** (→ generate another image before coding).

Then extract:
- **Text:** hero headline, subheadline, CTA labels, section headings, pricing labels, feature names, testimonial names and roles, navbar and footer labels. Visible text is part of the design system. If it is too small to read reliably, generate a closer extraction image or a clearer version of the section.
- **Typography:** size and weight relationships, line count and wrapping, line-height and tracking feel, serif vs sans behavior, display vs body contrast, section heading rhythm, CTA text scale, calm vs aggressive type, alignment logic. Do not flatten it into a generic coded hierarchy.
- **Spacing:** headline-to-subheadline, text-to-button, card-to-card, section top / bottom, side gutters, card padding, image-to-text, navbar and CTA block spacing, overall cadence. The goal is faithful spacing logic, not pixel OCR. Do not collapse generous spacing into generic tight spacing.
- **Buttons & components:** size, shape, radius, fill vs outline, icon usage, hover-implied mood, primary vs secondary hierarchy, card structure and dimensions, badges, dividers, strokes, shadows / depth, borders, pill logic, input styling. Analyze, do not guess; if too small, generate a closer image.
- **Color:** background, panels, accents, button fills, text hierarchy, border logic, shadow mood, image tint / grade, gradient restraint or intensity. Preserve the palette; never replace it with generic default web colors.
- **Structure:** grid logic, layout structure, section ordering and density, background and image and icon treatment, visual rhythm, repeated motifs that define the design language.

---

## 6. IMPLEMENTATION FIDELITY

Implement in a copy-oriented way: preserve layout logic, spacing rhythm, section ordering, text/image balance, typography mood, component style and overall visual cleanliness. The goal is not "inspired by the image"; it is **visually faithful to the image, translated into real frontend**.

**Anti-drift.** The common failure: the images look strong, the coded result becomes generic. During implementation do not simplify into default templates, replace distinctive sections with generic rows, compress generous spacing, replace strong typography with plain hierarchy, strip the visual identity for convenience, merge sections into repetitive patterns that were not in the references, or reintroduce nested-box complexity removed during analysis. The final code must still feel like the same website.

**Missing detail resolution order:**
1. preserve the visible design language
2. preserve layout and spacing logic
3. preserve component family
4. preserve mood and polish level
5. generate an extra detail image if needed
6. regenerate the section as a fresh standalone image if needed
7. only then choose the most implementation-friendly faithful version

Do not fill ambiguity with generic defaults too quickly.

---

## 7. DESIGN RULES FOR THE REFERENCES

### 7.1 Hero minimalism
The hero is a strong opening scene: cinematic, clear, intentional, calm, premium and immediately readable.
- One strong focal point, obvious hierarchy, generous negative space and contrast, a tight controlled visual system.
- **Headline:** short and powerful. 1 line if possible, 2 very good, 3 maximum. No 4+ line headlines, no paragraph-like hero copy, no weak headline-to-subheadline contrast. If it grows too long, cut words instead of adding lines.
- Supporting text concise.
- No pills, fake stats, badges, tiny logos, competing focal points, card overload, or pseudo-system labels like "00 orchestration layer".

### 7.2 Responsive first view
The first screen must feel usable and clean on a small laptop. Do not overload the fold, force many content blocks into the hero viewport, or use giant nested panels that consume space without adding clarity, and do not try to expose the whole product in one crowded first view. A smaller laptop still sees a clear headline, readable supporting text, clean spacing, a visible CTA and a balanced visual focal point.

### 7.3 Anti-nested-box rule
Avoid giant rounded section containers wrapping everything, cards inside cards inside cards, dashboard-like compartment stacking, and sections that are one bordered panel full of bordered panels. Use boxes only with a clear purpose. Prefer open layouts, clearer whitespace, fewer but stronger containers, flatter hierarchy, direct alignment, and one primary framing move rather than many layered frames. A section should not feel like a prison of containers.

### 7.4 Reduce micro-UI clutter
Avoid unnecessary pills, pseudo-system markers, fake control labels, decorative code-like tags, meaningless metadata rows, filler chips, badges everywhere, fake dashboard jargon ("00 orchestration layer", runtime markers, operator / control-room labels that exist only to look complex). Prefer cleaner headings, fewer labels, real hierarchy, clearer spacing, simpler supporting text, and stronger typography instead of decorative clutter.

### 7.5 Website image system and media frames
Think about the image system inside the website too: hero media, section images, editorial crops, product visuals, framed photography, layered image cards, gallery blocks, supporting visual panels. If the site benefits from several images, include several image moments; do not rely on one hero image when many sections need support. Image count matches site complexity; all image moments belong to one design world.

Images sit in controlled, implementation-friendly frames: fixed-aspect media blocks, repeatable portrait / landscape ratios, consistent radius logic, stable proportions across similar modules, product images in stable containers. No random sizes, inconsistent proportions, messy scaling, or uncontrolled collage chaos unless requested.

### 7.6 Typography, rhythm and density
- **Typography is a primary design material:** clear size contrast, obvious reading order, strong display moments, readable body, concise copy, section headings that reinforce structure. Editorial directions let typography shape composition; tech / product directions let it communicate trust and precision.
- **Section rhythm:** vary density, image-to-text ratio, alignment, scale, whitespace, card grouping, background intensity and visual tempo across the page, while keeping it coherent, spacing controlled, no random jumps, and each section clean enough to analyze.
- **Density:** the page breathes. Even, intentional section gaps; negative space for calm; no section cramped while the next is empty; smaller sections still get surrounding space; do not fill every area with UI; let simplicity do part of the work. Open, composed, balanced, confident, breathable. Not cramped, noisy, uneven, overfilled or exhausting.

### 7.7 Anti-AI-slop (unless explicitly requested)
- **Layout:** one giant unreadable collage, endless centered sections, identical card rows section after section, cloned left-text/right-image blocks, fake complexity without hierarchy, purposeless empty space, cards-inside-cards, giant rounded wrappers, overcompartmentalized dashboard framing.
- **Visual:** default purple/blue AI gradients, too many glowing edges, floating blobs, glassmorphism stacked without reason, random futuristic details, over-rendered noise hiding the layout.
- **Typography:** giant heading + weak tiny subcopy, too many font moods, awkward line breaks, lazy all-caps, gradient headline tricks.
- **Content:** filler verbs (unleash, elevate, revolutionize, next-gen, seamless, transformative platform); fake brands (Acme, Nexus, Flowbit, Quantumly, NovaCore); fake complexity (pseudo-enterprise control labels, decorative system markers, filler status microcopy, operator / runtime / orchestration jargon unless central to the brand).
- **Density:** over-packed sections, card overload, tiny gaps between major sections, exhausting walls of content.

---

## 8. RESPONSE BEHAVIOR (summary)

Infer site type and section count → pick a strong visual combination (4 signature components, 2 motion cues) → generate one large image per section, never lazily few, never one compressed sheet → add detail / extraction images where text or components are small → regenerate unclear sections fresh, never crop → enforce hero cleanliness, short headline, a readable first screen on a small laptop, no micro-UI clutter, no nested boxes, strong image usage, generous even spacing → deeply analyze every image and extract text, typography, spacing, buttons, colors, components and layout → implement faithfully → run the Clarity Check.

---

## 9. CLARITY CHECK

Before finalizing, verify internally:

1. Has the design been generated first?
2. Have all generated images been deeply analyzed?
3. Is the text readable enough? If not, were extra detail images created?
4. Were enough images generated, or was the image count too lazy?
5. Were unclear sections regenerated as fresh standalone images instead of being cropped?
6. Has the agent avoided compressing too many sections into one tiny image?
7. Is the hierarchy obvious, and is the hero clean enough?
8. Are typography, spacing relationships, buttons / components and colors extracted properly?
9. Was the analysis clean, structured, and specific?
10. Is the design visually distinctive and free of obvious AI tells?
11. If multiple images exist, do they clearly belong together?
12. Has unnecessary nested boxing been removed?
13. Is the first screen still clean and readable on a small laptop?
14. Have useless pills, labels, and fake technical micro-elements been reduced?
15. Can someone code from this faithfully, and does the implemented code still look like the references?

If not, refine internally before output.

---

## 10. FINAL GOAL

The result should be strong as section images, strong as a design system, strong under deep analysis, and strong as implemented frontend: a top-tier website concept translated faithfully into real code, not a tiny unreadable design board and not a generic coded reinterpretation.
