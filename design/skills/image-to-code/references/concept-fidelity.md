# Concept fidelity: from generated image to faithful code

Written for ultimate-skills (MIT). The checklist ideas (copy lock, palette lock, icon inventory, fidelity ledger) are informed by the public "website concepts" guidance in OpenAI's `build-web-apps` plugin; no text was copied from it.

Read this after the concept images exist and before writing code (workflow step 6), and again when verifying (step 9). The failure it prevents: strong concepts, generic implementation.

## 1. Accept or reject each concept first

Reject and regenerate (fresh image, same design language - never a crop) when a concept is: header-only for a full-page ask, unreadable at normal zoom, cluttered with fake UI jargon, generic (could be any product), or impossible to build without guessing. A rejected concept is cheaper than an implementation built on it.

## 2. Extract a spec per section

For every accepted section image write down, briefly:

- **Purpose and focal point** - what the section is for and the one thing that leads.
- **Readable copy** - every headline, subline, label, button text, nav item, price, name. This becomes the **allowed-copy list** (see 3).
- **Type relationships** - display vs body contrast, weights, line counts, tracking feel, alignment.
- **Spacing rhythm** - gutters, gaps, section padding, text-to-button distance (relative, not pixel OCR).
- **Components** - buttons (fill/outline, radius, size), cards or open layout, dividers, inputs, badges.
- **Container model** - open bands, full-bleed media, lists, rails, cards. Record it; do not add containers the concept doesn't have.
- **Palette** - background, surfaces, text tiers, accent, borders; name each background precisely: *pure white, off-white, cream, light gray, dark, tinted*.
- **Imagery** - what each image shows, its crop/aspect, treatment (grade, mask, cutout, overlay or none).
- **Unclear details** - anything you would have to guess. Each one triggers a new detail image before coding.

## 3. Locks - what implementation may not change

- **Copy lock.** Visible text comes from the allowed-copy list plus copy the user supplied. Do not add eyebrows, kickers, pills, badges, subtitles, stats or CTA text that are not in the concept. Changing a heading level for semantics is fine; inventing visible explanatory copy is not. Any deviation is recorded in the ledger.
- **Palette lock.** Do not "improve" the palette: no white turning into cream, no warming or cooling neutrals, no accent shift, no gradient that isn't there. Sample colors from the image and name them as tokens.
- **No invented overlays.** Do not lay a tint, gradient wash or dark scrim over a hero image unless the concept shows one. If text needs contrast, solve it with the image asset (regenerate with calmer negative space) or with an edge fade/mask the concept supports.
- **Container lock.** Keep the concept's container model; no extra cards, bordered tiles or floating panels.

## 4. Icon inventory

List every icon, glyph, chevron, logo-like mark and status symbol: meaning, outline vs filled, stroke weight, size, color, container, alignment. Then match it: use the project's icon set if it matches, otherwise author a small consistent SVG set (see `icon-set-generator`) - never swap in a generic nearby icon that changes the metaphor or weight.

## 5. Assets: regenerate, don't crop

Product shots, brand scenes, hero photography, textures and cutouts used in the page are generated as **standalone assets** with `image-generation` (transparent cutouts where they layer over UI), matching the accepted concept's palette, light and style. Do not crop them out of the concept comps - the crops are low-resolution and carry the comp's baked-in UI. Keep UI text in HTML/CSS; bake text only into genuine artwork (packaging, posters, signage).

## 6. Build and verify one section at a time

1. Implement one section (or one contiguous viewport).
2. Screenshot it in a browser at the concept's aspect/width where practical, plus one mobile width.
3. Open the concept image and the screenshot together and compare: hierarchy, type scale, spacing, palette, imagery, components, copy.
4. Fix visible drift before moving on. Use that section's own concept as evidence, not only a full-page overview.

## 7. Fidelity ledger (required before claiming a match)

Before saying the build matches the concepts, write a short ledger with **at least five concrete comparison points** across the page:

| # | Section | Concept shows | Build shows | Action |
|---|---|---|---|---|
| 1 | Hero | Headline 2 lines, tight tracking, off-white bg `#F6F4EF` | 3 lines, default tracking, `#FFFFFF` | Fixed: max-width 14ch, `-0.02em`, token `--paper` |
| 2 | Pricing | Recommended tier set apart by color only | Taller card + badge | Fixed: removed badge and height difference |
| ... | | | | |

Include intentional deviations (accessibility contrast fixes, semantic changes, responsive behavior the image cannot show) with the reason. If a point cannot be fixed, say why. Then ask the honest question: would a demanding design lead sign off on this as the same design? If not, keep iterating or name the blocker.

## 8. Clean up

Delete scratch screenshots, rejected concepts and unused generated assets unless the user asked to keep them. Ship only the assets the page references, optimized for the web.
