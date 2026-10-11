---
name: design-taste-frontend
description: "Anti-slop frontend design for new landing pages, marketing sites, portfolios and other greenfield UIs: reads the brief, infers the right design direction, uses real design systems where applicable and runs a strict pre-flight check so the result does not look templated. Use when building a new website or page from scratch and its look matters. To upgrade an existing UI codebase use redesign-existing-projects; for dashboards, admin panels and other product UI use interface-design; for a deliberately raw Swiss/terminal aesthetic use industrial-brutalist-ui; for image-first concepts use imagegen-frontend-web or image-to-code."
---

# tasteskill: Anti-Slop Frontend Skill

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI (use `interface-design` for those).
> Every rule below is **contextual**. None of it fires automatically. First read the brief, then pull only what fits.

**Reference files (load on demand):**
- [references/design-systems.md](references/design-systems.md) - install commands, canonical docs per design system, honest Apple Liquid Glass web approximation. Read when Section 2 picks a real system or the brief asks for glass.
- [references/motion-skeletons.md](references/motion-skeletons.md) - canonical GSAP sticky-stack, horizontal-pan and Motion scroll-reveal code. Read before building any pinned / scrubbed / revealed scroll section.
- [references/pattern-vocabulary.md](references/pattern-vocabulary.md) - named hero, nav, grid, card, scroll, gallery, type and micro-interaction patterns. Read when choosing or naming a signature pattern.
- [references/production-tells.md](references/production-tells.md) - the full production-test tell catalog with examples and exceptions. Read when auditing copy, labels and micro-UI before shipping.
- [references/redesign-protocol.md](references/redesign-protocol.md) - audit, preservation rules, modernisation levers, evolution-vs-redesign decision tree. Read for any redesign.

---

## 0. BRIEF INFERENCE (Read the Room Before Anything Else)

Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

### 0.A Read these signals first
1. **Page kind** - landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog.
2. **Vibe words** the user used - "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** - URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** - B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio. The audience picks the aesthetic, not your taste.
5. **Brand assets that already exist** - logo, color, type, photography. For redesigns, these are starting material, not optional input (see Section 8).
6. **Quiet constraints** - accessibility-first audiences, public-sector, regulated industries, trust-first commerce, kids' products. These constraints OVERRIDE aesthetic preference.

### 0.B Output a one-line "Design Read" before generating
Before any code, state in one line: **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

Example reads:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with an editorial / kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography."*
- *"Reading this as: redesign of a public-sector service site, with a trust-first language, leaning toward GOV.UK Frontend or USWDS."*

### 0.C If the brief is ambiguous, ask one question, do not guess
Ask exactly **one** clarifying question - never a multi-question dump - and only when the design read genuinely diverges. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"* If you can confidently infer from context, **do not ask**. Declare the design read and proceed.

### 0.D Anti-Default Discipline
Do not default to: AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism on everything, infinite-loop micro-animations everywhere, Inter + slate-900. These are the LLM defaults. Reach past them deliberately based on the design read.

---

## 1. THE THREE DIALS (Core Configuration)

After the design read, set three dials. Every layout, motion, and density decision below is gated by these. Use these exact variable names - never invent aliases like `LAYOUT_VARIANCE` or `ANIM_LEVEL`.

* **`DESIGN_VARIANCE: 8`** - 1 = Perfect Symmetry, 10 = Artsy Chaos
* **`MOTION_INTENSITY: 6`** - 1 = Static, 10 = Cinematic / Physics
* **`VISUAL_DENSITY: 4`** - 1 = Art Gallery / Airy, 10 = Cockpit / Packed Data

**Baseline:** `8 / 6 / 4`. Use these unless the design read overrides them. Do not ask the user to edit this file - overrides happen conversationally.

### 1.A Dial Inference and Presets (design read → dial values)
| Signal / use case | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "minimalist / clean / calm / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / Dribbble / Awwwards / experimental / agency" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing site (default)" | 7-9 | 6-8 | 3-5 |
| "trust-first / public-sector / regulated / accessibility-critical" | 3-4 | 2-3 | 4-5 |
| Landing (SaaS, mainstream) | 7 | 6 | 4 |
| Landing (Agency / creative) | 9 | 8 | 3 |
| Landing (Premium consumer) | 7 | 6 | 3 |
| Portfolio (Designer / studio) | 8 | 7 | 3 |
| Portfolio (Developer) | 6 | 5 | 4 |
| Editorial / Blog | 6 | 4 | 3 |
| Public-sector service | 3 | 2 | 5 |
| Redesign - preserve | match existing | match +1 | match existing |
| Redesign - overhaul | +2 | +2 | match existing |

### 1.B Dial Definitions
* **DESIGN_VARIANCE** - **1-3 (Predictable):** symmetrical CSS Grid (12-col, equal fr-units), equal paddings, centered alignment. **4-7 (Offset):** `margin-top: -2rem` overlaps, varied image aspect ratios (4:3 next to 16:9), left-aligned headers over center-aligned data. **8-10 (Asymmetric):** masonry, fractional grids (`grid-template-columns: 2fr 1fr 1fr`), massive empty zones (`padding-left: 20vw`). **MOBILE OVERRIDE:** for levels 4-10, asymmetric layouts above `md:` MUST collapse to strict single-column (`w-full`, `px-4`, `py-8`) below 768px.
* **MOTION_INTENSITY** - **1-3 (Static):** no automatic animations, CSS `:hover` / `:active` only. **4-7 (Fluid CSS):** transitions on explicitly listed properties (never `transition: all`), e.g. `transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ...`, `animation-delay` cascades for load-ins, `transform` and `opacity` only. **8-10 (Advanced Choreography):** scroll-triggered reveals, parallax, scroll-driven animation (CSS `animation-timeline` or GSAP ScrollTrigger), Motion hooks. `window.addEventListener('scroll')` is a hard ban at every level (Section 5.A).
* **VISUAL_DENSITY** - **1-3 (Art Gallery):** huge section gaps (`py-32` to `py-48`), expensive and clean. **4-7 (Daily App):** `py-16` to `py-24`. **8-10 (Cockpit):** tight paddings, no card boxes, 1px lines separate data, `font-mono` for all numbers.

---

## 2. BRIEF → DESIGN SYSTEM MAP

Once you have the design read and dials, pick the right foundation. Do not invent CSS for things that have an official package. Do not pretend an aesthetic trend is an official system. Install commands and canonical docs: [references/design-systems.md](references/design-systems.md).

### 2.A When to reach for a real design system (use official packages)
| Brief reads as… | Reach for | Why |
|---|---|---|
| Microsoft / enterprise SaaS / dashboards | `@fluentui/react-components` or `@fluentui/web-components` | Official Fluent UI, Microsoft tokens, accessibility done |
| Google-ish UI, Material-flavored product | `@material/web` + Material 3 tokens | Official, theme-able via Material Theming |
| IBM-style B2B / enterprise analytics | `@carbon/react` + `@carbon/styles` | Official Carbon, mature data-density patterns |
| Shopify app surfaces | `polaris.js` web components / Polaris React | Required for Shopify admin UI |
| Atlassian / Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` | Official Atlassian DS |
| GitHub-style devtool / community page | `@primer/css` or `@primer/react-brand` | Official Primer; Brand variant for marketing |
| Public-sector UK service | `govuk-frontend` | Legally / regulatorily expected |
| US public-sector / trust-first | `uswds` | Same |
| Fast local-business / agency MVP | Bootstrap 5.3 | Boring, fast, works |
| Modern accessible React foundation | `@radix-ui/themes` | Primitives + polished theme |
| Modern SaaS where you own the components | shadcn/ui (`npx shadcn@latest add ...`) | You own the code, easy to customise; never ship default state |
| Tailwind-based modern SaaS / AI marketing | Tailwind v4 utilities + `dark:` variant | Default for indie + small team builds |

**Honesty rule:** if the brief reads as one of the systems above, install and use the **official** package. Do not recreate its CSS by hand. Do not import a system's tokens but then override 90% of them. **One system per project.** Do not mix Fluent React with Carbon in the same tree. Do not import shadcn/ui components into a Material 3 app.

### 2.B When the brief is an aesthetic, not a system
There is **no single official package** for these. Build with native CSS + Tailwind + a maintained component library. Be honest in code comments about what is borrowed inspiration vs. official material.

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism / "frosted glass" | `backdrop-filter`, layered borders, highlight overlays. Solid-fill fallback for `prefers-reduced-transparency`. |
| Bento (Apple-style tile grids) | CSS Grid with mixed cell sizes. No single library owns this. |
| Brutalism | Native CSS, monospace, raw borders. No library. |
| Editorial / magazine | Serif type, asymmetric grid, generous whitespace. No library. |
| Dark tech / hacker | Mono + accent neon, terminal motifs. No library. |
| Aurora / mesh gradients | SVG or layered radial gradients. No library. |
| Kinetic typography | Native CSS animations, scroll-driven animations, GSAP for hijacks. No library. |
| **Apple Liquid Glass** | Apple documents this for Apple platforms only. **There is no official `liquid-glass.css`.** Web versions are approximations (`backdrop-filter` + layered borders + highlights). Label clearly as approximation; skeleton in [references/design-systems.md](references/design-systems.md). |

---

## 3. DEFAULT ARCHITECTURE & CONVENTIONS

Unless the design read picks a real design system (Section 2.A), these are the defaults.

### 3.A Stack
* **Framework:** React or Next.js. Default to Server Components (RSC).
  * **RSC SAFETY:** Global state works ONLY in Client Components. In Next.js, wrap providers in a `"use client"` component.
  * **INTERACTIVITY ISOLATION:** Any component using Motion, scroll listeners, or pointer physics MUST be an isolated leaf with `'use client'` at the top. Server Components render static layouts only.
* **Styling:** **Tailwind v4** (default). Tailwind v3 only if the existing project demands it. For v4: do NOT use the `tailwindcss` plugin in `postcss.config.js`; use `@tailwindcss/postcss` or the Vite plugin.
* **Animation:** **Motion** (formerly Framer Motion), imported from `motion/react`. `framer-motion` still works as a legacy alias - prefer `motion/react` in new code. GSAP + ScrollTrigger only for full-page scrolltelling and scroll hijacks; Three.js / WebGL for canvas backgrounds and 3D. Isolate GSAP / Three.js in dedicated leaf components with `useEffect` cleanup. **NEVER mix GSAP / Three.js with Motion in the same component tree.** They fight over the same frames.
* **Fonts:** Always `next/font` (Next.js) or self-host with `@font-face` + `font-display: swap`. Never link Google Fonts via `<link>` in production.

### 3.B State
* Local `useState` / `useReducer` for isolated UI. Global state ONLY for deep prop-drilling avoidance - Zustand, Jotai, or React context.
* **NEVER** use `useState` to track continuous values driven by user input (mouse position, scroll progress, pointer physics, magnetic hover). Use Motion's `useMotionValue` / `useTransform` / `useScroll`. `useState` re-renders the React tree on every change and collapses on mobile.

### 3.C Icons
* **Allowed libraries (priority order):** `@phosphor-icons/react`, `hugeicons-react`, `@radix-ui/react-icons`, `@tabler/icons-react`.
* **Discouraged:** `lucide-react`. Acceptable only when the user explicitly asks for it or the project already depends on it.
* **NEVER hand-roll SVG icons.** If a glyph is missing, install a second library or compose from primitives.
* **One family per project.** Standardize `strokeWidth` globally (e.g. `1.5` or `2.0`).

### 3.D Emoji Policy
Discouraged by default in code, markup, and visible text. Replace symbols with icon-library glyphs. **Override:** only when the user explicitly asks for a playful / chat-style / social-native vibe - and even then sparingly, with intent.

### 3.E Responsiveness & Layout Mechanics
* Standardize breakpoints (`sm 640`, `md 768`, `lg 1024`, `xl 1280`, `2xl 1536`). Contain page layouts with `max-w-[1400px] mx-auto` or `max-w-7xl`.
* **Viewport Stability:** NEVER `h-screen` for full-height heroes. ALWAYS `min-h-[100dvh]` (iOS Safari address bar).
* **Grid over Flex-Math:** NEVER `w-[calc(33%-1rem)]`-style flexbox math. ALWAYS CSS Grid (`grid grid-cols-1 md:grid-cols-3 gap-6`).

### 3.F Dependency Verification (mandatory)
Before importing ANY 3rd-party library, check `package.json`. If the package is missing, output the install command first. **Never** assume a library exists.

---

## 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)

LLMs default to clichés. Override these defaults proactively. Each rule has a context-aware override path.

### 4.1 Typography
* **Display / Headlines:** default `text-4xl md:text-6xl tracking-tighter leading-none`. Control hierarchy with weight + color, not raw scale; no oversized H1s that just scream.
* **Body:** default `text-base text-gray-600 leading-relaxed max-w-[65ch]`.
* **Sans choice:** `Inter` is discouraged as default. Pick `Geist`, `Outfit`, `Cabinet Grotesk`, `Satoshi`, or a brand-appropriate face first. **Override:** Inter is fine when the user asks for a neutral / standard / Linear-style feel, or for public-sector / accessibility-first sites. Pairings to know: `Geist` + `Geist Mono`, `Satoshi` + `JetBrains Mono`, `Cabinet Grotesk` + `Inter Tight`, `GT America` + `IBM Plex Mono`.
* **SERIF DISCIPLINE (VERY DISCOURAGED AS DEFAULT):** "It feels creative / premium / editorial" is NOT a reason to reach for serif; "creative brief = serif" is the single most-tested AI tell in production rounds. Serif only when the brand brief literally names a serif, OR the aesthetic is genuinely editorial / luxury / publication / manuscript / heritage / vintage AND you can articulate why this specific serif fits this brand. Never for dashboards. Everything else (agency, studio, modern brand, premium consumer, portfolio, lifestyle) gets a **sans display** (Geist Display, ABC Diatype, Söhne Breit, Cabinet Grotesk Display, Migra Sans, GT Walsheim, Inter Display, PP Neue Montreal). **Banned as defaults:** `Fraunces` and `Instrument_Serif`. If a serif is justified, rotate (never the same one on consecutive projects): PP Editorial New, GT Sectra Display, Cardinal Grotesque, Reckless Neue, Tiempos Headline, Recoleta, Cormorant Garamond, Playfair Display, EB Garamond, IvyPresto, Migra, Editorial Old, Saol Display, Söhne Breit Kursiv, Domaine Display, Canela, Schnyder, Tobias, NB Architekt, ITC Galliard.
* **EMPHASIS RULE:** emphasize a word inside a headline with italic or bold of the SAME font. Never inject a random serif word into a sans headline (or vice versa).
* **ITALIC DESCENDER CLEARANCE (mandatory):** italic display words with `y g j p q` clip at `leading-none`. Use `leading-[1.1]` minimum plus `pb-1` / `mb-1` reserve on the wrapper. Audit every italic headline word.

### 4.2 Color Calibration
* Max 1 accent color. Saturation < 80% by default. No oversaturated accents; desaturate to blend with neutrals. One palette per project; do not fluctuate between warm and cool grays.
* **THE LILA RULE:** "AI Purple / Blue glow" is discouraged as a default. No automatic purple button glows, no random neon gradients. Use neutral bases (Zinc / Slate / Stone) with high-contrast singular accents (Emerald, Electric Blue, Deep Rose, Burnt Orange, etc.). **Override:** if the brand or brief explicitly asks for purple / violet / lila, embrace it with a consistent palette, harmonised neutrals, restrained gradients.
* **COLOR CONSISTENCY LOCK (mandatory):** once an accent is chosen it is used on the WHOLE page. A warm-grey site does not get a blue CTA in section 7; a rose-accented site does not get a teal footer badge.
* **PREMIUM-CONSUMER PALETTE BAN (mandatory, second-most-recurring AI tell):** for premium-consumer briefs (cookware, wellness, artisan, luxury, heritage craft, DTC home goods) the LLM default is warm beige/cream + brass/clay/oxblood/ochre + espresso text. Banned as default:
  - Backgrounds: `#f5f1ea`, `#f7f5f1`, `#fbf8f1`, `#efeae0`, `#ece6db`, `#faf7f1`, `#e8dfcb`
  - Accents: `#b08947`, `#b6553a`, `#9a2436`, `#9c6e2a`, `#bc7c3a`, `#7d5621`
  - Text: `#1a1714`, `#1a1814`, `#1b1814`
  - **Rotate instead (never the same family twice in a row):** Cold Luxury (silver-grey + chrome + smoke), Forest (deep green + bone + amber), Black and Tan (true off-black + warm tan, no beige), Cobalt + Cream (no brass), Terracotta + Slate (no brass), Olive + Brick + Paper, Pure monochrome + single saturated pop.
  - **Override:** only when the brief names those colors, or the identity is genuinely vintage / artisan / warm-craft AND you can articulate why. "This is a cookware brief" is not a reason.

### 4.3 Layout Diversification
* **ANTI-CENTER BIAS:** centered hero / H1 sections are avoided when `DESIGN_VARIANCE > 4`. Use split screen (50/50), left content / right asset, asymmetric white-space, or scroll-pinned structures. **Override:** centered is fine for editorial / manifesto / launch-announcement briefs where the message itself is the design.
* **NO 3-column equal feature cards.** Use 2-column zig-zag, asymmetric grid, scroll-pinned, or horizontal-scroll alternatives.

### 4.4 Materiality, Shadows, Cards
* Cards ONLY when elevation communicates real hierarchy. Otherwise group with `border-t`, `divide-y`, or negative space. For `VISUAL_DENSITY > 7`, generic card containers are banned.
* Tint shadows to the background hue. No pure-black drop shadows on light backgrounds, no neon / outer glows by default (use inner borders or tinted shadows).
* **SHAPE CONSISTENCY LOCK (mandatory):** ONE corner-radius scale per page: all-sharp (0), all-soft (12-16px), or all-pill (interactive). Mixed systems only with a documented rule ("buttons full-pill, cards 16px, inputs 8px") followed everywhere.

### 4.5 Interactive UI States
LLMs default to "static successful state only." Always implement full cycles:
* **Loading:** skeletal loaders matching the final layout's shape, not generic spinners. **Empty:** composed, indicating how to populate. **Error:** inline (forms) or contextual (toasts only for transient). **Tactile:** `:active` → `-translate-y-[1px]` or `scale-[0.98]`.
* **BUTTON CONTRAST CHECK (mandatory, a11y):** every CTA label passes WCAG AA against its background (4.5:1 body, 3:1 for 18px+). White-on-white, borderless transparent buttons, ghost buttons over photos without scrim / stroke are banned.
* **CTA BUTTON WRAP BAN (mandatory):** CTA text fits on one line at desktop. Shorten the label (3 words max for primary, ideally 1-2) or widen the button; never constrain `max-width` on CTAs.
* **NO DUPLICATE CTA INTENT (mandatory):** one label per intent per page. "Get in touch" / "Contact us" / "Let's talk" / "Start a project" / "Reach out" are all "contact"; "Try free" / "Get started" / "Sign up free" are all "signup"; "View work" / "See selected work" / "Browse projects" are all "portfolio". Pick one and use it in nav, hero and footer.
* **FORM CONTRAST CHECK (mandatory, a11y):** inputs, placeholders, focus rings, helper and error text all pass WCAG AA against the section background.
* **Forms:** label ABOVE input, helper text present in markup, error text BELOW input, `gap-2` for input blocks. No placeholder-as-label. Ever.

### 4.6 Layout Discipline (Hard Rules. Failing any of these is shipping broken work)
* **Hero MUST fit the initial viewport.** Headline max 2 lines on desktop, subtext max **20 words** AND max 3-4 lines, CTAs visible without scroll. Too long → reduce font scale or cut copy. If the value-prop does not fit in 20 words, the value-prop is unclear, not the rule too tight.
* **Hero font-scale discipline.** Plan font size and image size together. Large asset + headline over 6 words → do not start at `text-7xl/8xl`. Default `text-4xl md:text-5xl lg:text-6xl`; `text-6xl md:text-7xl` only for 3-5 word headlines. A 4-line hero headline is always a font-size error.
* **HERO TOP PADDING CAP:** max `pt-24` at desktop. Need more room? Increase font scale or asset size, not padding.
* **HERO STACK DISCIPLINE (max 4 text elements):** (1) eyebrow OR brand strip OR neither, (2) headline, (3) subtext, (4) CTAs (1 primary + max 1 secondary). **Banned in the hero:** tagline below CTAs, trust micro-strip ("Used by engineering teams at..."), pricing teaser, feature bullets, avatar social-proof row. They move to sections below. One small text element per hero, max.
* **Logo walls ("Used by" / "Trusted by") live UNDER the hero**, never in the hero's flex row.
* **Navigation on a single line at desktop** (condense, drop secondary items, or hamburger at `lg`). Height 64-72px default, 80px max.
* **Section-Layout-Repetition Ban.** Each layout family (3-column image cards, full-width quote, split text-image...) appears at most ONCE. 8 sections → at least 4 different families.
* **ZIGZAG ALTERNATION CAP:** max 2 consecutive image+text-split sections. Break the third with full-width, vertical stack, bento, marquee, or another family.
* **Bento rhythm and cell count:** no 6 stacked left-image / right-text rows; vary with full-width rows, asymmetric tiles, vertical breaks. A bento has EXACTLY as many cells as content items (3 items → 3 cells, 5 → 5). No empty cells; reshape the grid. At least 2-3 cells need real visual variation (image, brand-appropriate gradient, pattern, tint); never 6 white-on-white text cards.
* **EYEBROW RESTRAINT (the #1 violated rule in production tests).** An eyebrow is the small uppercase wide-tracking label above a section headline (`text-[11px] uppercase tracking-[0.18em]`, `FOUR COLORWAYS`, `SELECTED WORK`). **Max 1 eyebrow per 3 sections** (hero counts). After an eyebrow, the next 2 sections have none. Mechanical check: count `uppercase tracking` labels above headlines; must be ≤ ceil(sectionCount / 3). Instead of an eyebrow: drop it. The headline is enough.
* **SPLIT-HEADER BAN:** "left big headline + right small explainer paragraph" section headers are banned as default. Stack headline over body (max-w 65ch). Split only when the right column carries a real visual or interactive element. A tiny paragraph floating in the top-right corner of a section header is the same Tell.
* **Mobile collapse explicit per section.** Every multi-column layout declares its `< 768px` fallback in the same component.

### 4.7 Image & Visual Asset Strategy
Landing pages and portfolios are **visual products**. Text-only pages with fake-screenshot divs are slop.
1. **Image-generation tool first.** If ANY image-gen tool is available (`generate_image`, MCP image tool, IDE-integrated gen, OpenAI image tools, etc.) you MUST use it for section-specific assets (hero photography, product shots, textures, mood images) at the right aspect ratio. For a full image-first build, see the image-to-code skill.
2. **Real web images second.** `https://picsum.photos/seed/{descriptive-seed}/{w}/{h}` (seed describes the section, e.g. `marrow-cookware-kitchen`), actual stock / brand URLs from the brief, open-license sources if allowed. No broken Unsplash links.
3. **Last resort: tell the user.** Leave labeled slots (`<!-- TODO: hero product photo, 1600x1200 -->`) and end with: *"This page needs real images at: \[list of placements\]. Please generate or provide them."*

* **Even minimalist sites need real images** (at least 2-3: hero, one product/lifestyle shot, one supporting). Generate B&W minimalist photography for restrained briefs. **Hero needs a real visual**; text + gradient blob is a placeholder.
* **Logo walls use real SVG logos:** Simple Icons (`https://cdn.simpleicons.org/{slug}/ffffff` or the `simple-icons` package), devicon for tech stacks. Invented brand → invent a simple SVG mark too (monogram, ligature, abstract glyph), never a plain text wordmark. Logos must work in light and dark. **LOGO-ONLY:** no category labels under logos (no `Stripe` + `payments`); alt text and an optional link only.
* **Hand-rolled decorative SVGs** (illustrations, logos, marks) strongly discouraged; only when the brief asks, it is a single simple geometric mark, and you are confident in quality.
* **Div-based fake screenshots are banned** (fake task lists, dashboards, terminals from styled divs). Use a real screenshot, a generated image, a real mini component preview, or editorial photography instead.

### 4.8 Content Density & Copy
Landing pages live on the **first impression**, not the full read. Cut ruthlessly.
* **Default section shape:** headline ≤ 8 words + sub-paragraph ≤ 25 words + one visual OR one CTA. More must be justified by the section's job.
* **No data-dump sections** (20-row publication tables, 30-row award lists, giant pricing matrices). Top 3-5 highlights + "View full list", marquee / carousel for breadth, or a separate page.
* **Lists over 5 items need a different component:** 2-column grouped split, card grid with image + label, tabs / accordion, scroll-snap pills, carousel, or marquee. Never `border-t` + `border-b` on every row.
* **Spec sheets** (the cookware / hardware / apparel default of a long hairlined table) are banned. Use a 2-col card grid (name, large display value, one-line "why it matters"), scroll-snap pills, 3 grouped clusters with one soft divider each, or 3-4 featured spec tiles + "View full specifications" disclosure.
* **COPY SELF-AUDIT (mandatory before ship):** re-read every visible string (headlines, eyebrows, buttons, body, captions, alt text, footer, errors). Rewrite anything grammatically broken ("free on its past"), with unclear referents ("we plan to stay that way"), AI-hallucinated wordplay, or LLM fake-thoughtfulness (mock humility, fake-craftsman labels, mock-poetic micro-meta). When unsure, write a plain functional sentence. AI-cute copy is worse than boring copy.
* **Fake-precise numbers** (`92%`, `4.1×`, `5.8 mm`) must come from real data or be explicitly labeled mock. Invented spec aesthetics are banned.
* **One copy register per page.** No mixing technical mono stats, editorial prose and marketing punch unless the brand voice calls for it.
* **Quotes & testimonials:** max 3 lines of quote body (cut longer ones; tiny footer-style quotes may stretch slightly), attribution = name + role (+ company), never name only. Real typographic quotes or none, not straight ASCII quotes. No em-dashes (Section 7.D).

### 4.9 Page Theme Lock
The page has ONE theme. Sections do not invert. Pick light, dark, or auto (`prefers-color-scheme`) at page level and lock it; tints within one family are fine (`bg-zinc-950` next to `bg-zinc-900`), flipping to `bg-amber-50` mid-page is broken. Exception: a deliberate "Color Block Story" / "Theme Switch on Scroll" the brief asks for, once per page with a strong transition. With themed design systems (Radix Themes, shadcn/ui `<Theme>`), set the theme ONCE at the root.

---

## 5. MOTION: CONTEXT-AWARE PROACTIVITY

These are tools, not defaults. **None of these fire automatically.** Canonical code: [references/motion-skeletons.md](references/motion-skeletons.md). Named patterns: [references/pattern-vocabulary.md](references/pattern-vocabulary.md). For UI micro-interactions (buttons, popovers, modals, toasts) the exact curves, duration budgets and review rules in `motion-craft` apply.

* **Liquid Glass / Glassmorphism:** premium consumer, Apple-adjacent, luxury, media overlays. Not for dashboards, public-sector, or boring B2B. Go beyond `backdrop-blur`: 1px inner border (`border-white/10`), subtle inner shadow (`shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`), solid-fill fallback under `prefers-reduced-transparency`.
* **Magnetic micro-physics:** only when `MOTION_INTENSITY > 5` AND the brief reads premium / playful / agency. EXCLUSIVELY via `useMotionValue` / `useTransform` outside the render cycle. Never `useState`.
* **Perpetual micro-interactions** (pulse, typewriter, float, shimmer, carousel): only when `MOTION_INTENSITY > 5` AND the section benefits (status, live feeds, AI-feel). Informational sections stay still. Spring physics (`type: "spring", stiffness: 100, damping: 20`), no linear easing.
* **"Motion claimed, motion shown."** If `MOTION_INTENSITY > 4`, the page must move: hero entry, scroll-reveal on key sections, hover physics on CTAs at minimum. If you cannot ship working motion, drop the dial to 3 and ship a clean static page. Never half-build motion (cut-off ScrollTriggers, jumpy enters, missing cleanups).
* **MOTION MUST BE MOTIVATED (mandatory).** Every animation answers "what does this communicate?" with hierarchy, storytelling, feedback, or state transition. "It looked cool" is invalid. If you cannot say why in one sentence, drop it.
* **MARQUEE MAX-ONE-PER-PAGE (mandatory).**
* **GSAP sticky-stack / horizontal-pan:** must pin at the viewport top (`start: "top top"`, `pin: true`), never `"top center"` / `"top 80%"`. Sticky-stack pins every card but the last and drives the shrink from the NEXT card's trigger; horizontal-pan pins the wrapper and scrubs the inner track over `end: "+=${distance}"`. Use the skeletons in the reference file.
* **Simple enter-on-scroll** (feature lists, testimonials, logo walls): Motion `whileInView`, not GSAP.

### 5.A Forbidden Animation Patterns
* **`window.addEventListener("scroll", ...)`** is banned. Use Motion `useScroll()`, GSAP `ScrollTrigger`, IntersectionObserver, or CSS scroll-driven animations (`animation-timeline: view()`).
* No scroll progress from `window.scrollY` in React state; no `requestAnimationFrame` loops that touch React state. Use motion values.
* **Layout transitions:** Motion `layout` / `layoutId` for visible state changes only; do not wrap static content "for safety".
* **Staggered orchestration:** `staggerChildren` (parent `variants` and children in the same Client Component tree) or CSS `animation-delay: calc(var(--index) * 100ms)`.
* **NO custom mouse cursors.** Outdated, accessibility-hostile, perf-hostile.

---

## 6. PERFORMANCE, ACCESSIBILITY & DARK MODE GUARDRAILS

* **Hardware acceleration:** animate ONLY `transform` and `opacity`, never `top` / `left` / `width` / `height`. `will-change: transform` sparingly, only on elements that animate.
* **Reduced motion (mandatory):** anything at `MOTION_INTENSITY > 3` honors `prefers-reduced-motion` (Motion `useReducedMotion()`; CSS `@media (prefers-reduced-motion: no-preference)` gating or a `reduce` override). Loops, parallax, scroll-hijack and magnetic physics collapse to static.
* **Core Web Vitals:** LCP < 2.5s (hero image `next/image priority` or preloaded), INP < 200ms (heavy work off main thread), CLS < 0.1 (reserve space for images, fonts, embeds). Run Lighthouse before declaring done.
* **DOM cost:** grain / noise filters ONLY on fixed `pointer-events-none` pseudo-elements (`fixed inset-0 z-[60] pointer-events-none`), never on scrolling containers. Lazy-load Motion-heavy, Three.js and anything below the fold.
* **Z-index restraint:** no arbitrary `z-50` / `z-10` spam. Z-index only for systemic layers (sticky nav, modals, overlays, grain), documented in a constants file.
* **Dark mode (mandatory for consumer-facing pages):** design both modes from the start; light-only only when the brief is print-emulating editorial or the user says so. Pick ONE token strategy: Tailwind `dark:` pairs (`bg-white dark:bg-zinc-950`) for utility-first projects, or CSS variable semantic tokens (`--surface`, `--text-primary`, `--accent`) swapped under `[data-theme="dark"]` / `prefers-color-scheme` for shadcn/ui, Radix Themes and themed libraries. Do not prescribe specific colors; the brief decides. Enforce: WCAG AA body contrast (AAA target for hero copy), hierarchy parity (a CTA that pops in light pops in dark), brand fidelity (do not desaturate the brand), **no pure `#000000` or `#ffffff`**. Respect `prefers-color-scheme` unless the brand insists; add a manual toggle if either mode would lose brand expression. Open the page in both modes before finishing.

---

## 7. AI TELLS (Forbidden Patterns)

Avoid these signatures unless the brief explicitly asks for them.

### 7.A Visual, CSS & Components
* No neon / outer glows, no pure black, no oversaturated accents, no excessive gradient text on large headers, no custom cursors.
* No hand-rolled SVG icons (Phosphor / HugeIcons / Radix / Tabler; Lucide on request only). No div-based fake screenshots.
* **shadcn/ui** allowed, but NEVER in default state: customize radii, colors, shadows, typography to the project.
* Layout: mathematically consistent padding, no floating elements with awkward gaps.

### 7.B Content & Data ("Jane Doe" Effect)
* **NO generic names** ("John Doe", "Sarah Chan", "Jack Su") → creative, realistic, locale-appropriate names.
* **NO generic avatars** (SVG "egg", Lucide user icons) → believable photo placeholders or specific styling.
* **NO fake-perfect numbers** (`99.99%`, `50%`, `1234567`) → organic, messy data (`47.2%`, `+1 (312) 847-1928`).
* **NO startup-slop brand names** ("Acme", "Nexus", "SmartFlow", "Cloudly") → contextual, premium names that sound real.
* **NO filler verbs** ("Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize") → concrete verbs.

### 7.C Production-Test Tells (banned outright)
Signatures the model defaults to when it tries to "look designed." Full examples and the narrow exceptions: [references/production-tells.md](references/production-tells.md).
* **Hero:** version labels (`V0.6`, `BETA`, `INVITE-ONLY`) unless it is a launch; "Brand · No. 01" sub-eyebrows; decoration text strips at hero bottom (`BRAND. MOTION. SPATIAL.`); div-based fake product UI and fake version footers inside it.
* **Numbering & micro-labels:** section-number eyebrows (`00 / INDEX`, `001 · Capabilities`); `01 / 4` pagination on tiles; "Index of Work, 2018 - 2026" range labels; generic step labels ("Step 1", "Phase 01") instead of the verb itself; micro-meta sentences under eyebrows.
* **Separators & dots:** middle-dot max 1 per line; zero decorative status dots (only real semantic state, one per section).
* **Typography flourishes:** `<br>`-broken italic headline splits as a default move; vertical rotated text; decorative crosshair / hairline grid lines.
* **Copy:** "Quietly in use at / trusted by"; poetic section labels ("Field notes", "On our desks"); mock-humble industry references.
* **Pills & stamps:** pills / labels overlaid on images; decorative photo-credit captions for stock images; version footers (`v1.4.2`, `Build 0048`) on marketing pages; fake "Reservation 412 of 800" counters.
* **Lists & scoring:** hairlines on every row; scoring bars with filled background tracks.
* **Locale & scroll:** locale / city / time / weather strips (unless the brief is genuinely place- or timezone-driven; one footer address is fine); scroll cues of any kind (`Scroll`, `↓ scroll`, mouse-wheel icons).

### 7.D EM-DASH BAN (the single most-violated Tell)
**Em-dash (`—`) is COMPLETELY banned** in everything visible: headlines, eyebrows, labels, pills, buttons, captions, nav, alt text, body copy, quotes and attribution. No "limited use" or "in body copy is fine" allowance. Restructure with a period, comma, parentheses, colon, or line break; attribution uses ` - ` or a line break. The en-dash (`–`) as a separator is banned too: ranges use a hyphen (`2018-2026`, `€40-80k`). The ONLY permitted dash characters are the hyphen `-` and the math minus (`-5°C`). A single visible `—` or `–` fails the Pre-Flight Check. The phrasing is binary because "use sparingly" has historically been ignored: zero em-dashes.

---

## 8. REDESIGN MODE

This skill handles **greenfield builds AND redesigns**. Detect the mode first:
* **Greenfield** - no existing site, or full overhaul approved. Dial baseline from Section 1.
* **Redesign - Preserve** - modernise without breaking the brand. Audit first, extract brand tokens, evolve gradually.
* **Redesign - Overhaul** - new visual language on existing content. Greenfield for visuals; preserve content and IA.

If ambiguous, ask **once**: *"Should this redesign preserve the existing brand, or are we starting visually from scratch?"* Then read [references/redesign-protocol.md](references/redesign-protocol.md) for the audit, preservation rules, modernisation levers (typography → spacing → color → motion → recomposition → block replacement) and the evolution-vs-redesign decision tree.

**Never change without explicit approval:** URL structure / route slugs, primary nav labels, form field names or order, brand logo or wordmark, legal / consent / cookie copy. A brand that is already purple stays purple (LILA RULE override); SEO migration is the #1 redesign risk.

---

## 9. OUT OF SCOPE

This skill is NOT for: dashboards / dense product UI / admin panels (use Fluent, Carbon, Atlassian, or Polaris from Section 2.A), data tables (TanStack Table or AG Grid), multi-step forms / wizards, code editors (Monaco / CodeMirror with official skinning), native mobile (Apple HIG / Material directly), realtime collab UIs (presence, cursors, OT). If the brief is one of these, **say so explicitly**, point to the right tool, and apply this skill only to the marketing / about / landing surfaces.

---

## 10. FINAL PRE-FLIGHT CHECK

Run this matrix before outputting code. **THIS IS NOT OPTIONAL. If any box fails, the output is not done.**

**Direction**
- [ ] **Design Read** one-liner declared (0.B)? **Dial values** reasoned from the brief, not silently baseline?
- [ ] **Design system** chosen from Section 2 or aesthetic labeled honestly? **One system** per project?
- [ ] **Redesign mode** detected and audit performed (if applicable)?

**Hard bans**
- [ ] **ZERO em-dashes / en-dash separators** anywhere visible (7.D)?
- [ ] **No 7.C production tells** (version labels, numbered eyebrows, decorative dots, pills on images, photo-credit captions, version footers, micro-meta sentences, hero decoration strips, floating corner sub-text, filled-track scoring bars, locale strips, scroll cues, hairline-every-row lists)?
- [ ] **No AI tells** from Section 7 (Inter as default, AI-purple, three equal cards, Jane Doe, Acme, "Quietly in use at")?

**Consistency locks**
- [ ] **Page Theme Lock** (4.9), **Color Consistency Lock** (4.2), **Shape Consistency Lock** (4.4)?
- [ ] **Serif discipline**: no Fraunces / Instrument_Serif without brand justification; different serif from the previous project?
- [ ] **Premium-consumer palette**: not the beige+brass+oxblood+espresso default; different family from the previous premium-consumer project?
- [ ] **Italic descender clearance**: `leading-[1.1]` min + `pb-1` on italic words with `y g j p q`?

**Hero & layout**
- [ ] **Hero fits the viewport**: headline ≤ 2 lines, subtext ≤ 20 words and ≤ 4 lines, CTA visible, font scale planned with the image, top padding ≤ `pt-24`?
- [ ] **Hero stack** ≤ 4 text elements; no tagline under CTAs, no trust strip in the hero; logo wall UNDER the hero with real SVG logos, logo-only?
- [ ] **Eyebrow count** ≤ ceil(sectionCount / 3), hero included?
- [ ] **Split-Header Ban**, **Zigzag cap** (no 3 consecutive splits), **Section-layout repetition** (≥ 4 families across 8 sections)?
- [ ] **Bento**: rhythm, exact cell count, 2-3 cells with real visual variation?
- [ ] **Navigation** on one line at desktop, ≤ 80px?
- [ ] **Mobile collapse** explicit for every multi-column / high-variance layout; `min-h-[100dvh]`, never `h-screen`?

**Buttons, forms, content**
- [ ] **Button contrast** WCAG AA; **no CTA wraps** at desktop; **no duplicate CTA intent**?
- [ ] **Form contrast** WCAG AA; labels above inputs; empty / loading / error states provided?
- [ ] **Copy Self-Audit** done; density sane (≤ 25-word subs, no data dumps, no fake-precise specs); long lists use the right component; quotes ≤ 3 lines with clean attribution?
- [ ] **Real images** (gen tool → Picsum seed → labeled slots); no div fake screenshots, no hand-rolled decorative SVGs, no pure-text minimalism?
- [ ] **Cards omitted** in favor of spacing where possible; icons from an allowed library only?

**Motion & engineering**
- [ ] **Motion motivated** (one-sentence reason each); **motion claimed = motion shown**; marquee max one?
- [ ] **Sticky-stack / horizontal-pan** per the canonical skeletons (`start: "top top"`, `pin: true`, correct scrub)?
- [ ] **No `window.addEventListener('scroll')`**; reduced motion honored above `MOTION_INTENSITY 3`; `useEffect` animations have cleanup?
- [ ] **Motion isolated** in memoized `'use client'` leaf components; no GSAP / Three.js mixed with Motion in one tree?
- [ ] **Dark mode** tokens defined and tested in both modes?
- [ ] **Core Web Vitals** plausibly hit (LCP < 2.5s, INP < 200ms, CLS < 0.1)?

If a single checkbox cannot be honestly ticked, the page is not done. Fix it before delivering.
