# design

## Overview
Design and frontend-craft skills that fight generic "AI slop" output and turn taste into checkable rules: brief-aware direction for marketing pages, craft rules for dashboards and product UI, real image generation (OpenAI GPT Image or Google Gemini / Nano Banana) feeding an image-first concept-to-code workflow, redesign audits with heuristic scoring, decidable motion rules, a lint-style UI code review, WCAG 2.2 audits, consistent SVG icon sets, HTML slide decks, and production UI engineering.

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install design@ultimate-skills
```

## Skills
13 skills (see also the table in the [root README](../README.md#design)):

| Need | Skill |
|---|---|
| Visual direction for a **new** landing page, portfolio, marketing site | `design-taste-frontend` |
| **Dashboards, admin, SaaS, settings, data tables** (product UI) | `interface-design` |
| Upgrade or critique an **existing** site/app | `redesign-existing-projects` |
| Distinct raw/brutalist aesthetic | `industrial-brutalist-ui` |
| Actually **generate or edit images** (OpenAI / Gemini / any image MCP) | `image-generation` |
| Website design-concept comps, one image per section (no code) | `imagegen-frontend-web` |
| Image-first concepts → implemented frontend | `image-to-code` |
| Animation and micro-interactions (build + strict review) | `motion-craft` |
| Lint-style `file:line` review of UI code | `web-interface-review` |
| WCAG 2.2 A/AA audit (axe, keyboard, screen reader; Pass/Fail/NT) | `accessibility-audit` |
| Engineering discipline for accessible, responsive components | `frontend-ui-engineering` |
| Custom, consistent SVG icon set | `icon-set-generator` |
| HTML presentation / pitch deck (or PPTX → web) | `frontend-slides` |

(`image-generation` is the render step used by `imagegen-frontend-web` and `image-to-code`.)

## Prerequisites
- **Image generation** needs one of: an image-generation MCP server/tool in the session, `OPENAI_API_KEY` + `pip install openai` (GPT Image), or `GEMINI_API_KEY` (Gemini, standard library only). Without any of them the image skills say so and fall back to text-based direction via `design-taste-frontend`. Live calls are billed to the user's API account; the skill asks before batches.
- `accessibility-audit` injects axe-core from a public CDN into the page under test (or a locally vendored copy).
- `frontend-slides` PDF export needs Node.js (installs Playwright + Chromium into a temp dir); PPTX import needs `python-pptx`.

## License
MIT for most skills; Apache-2.0 for material from `openai/skills` (`image-generation`, which ships its own `LICENSE.txt`), `replicate/skills` (an `image-generation` reference) and `pbakaus/impeccable` (two `redesign-existing-projects` references), each marked as modified. Copies of every upstream license used by this plugin are in [`LICENSES/`](./LICENSES/); see [`../NOTICE.md`](../NOTICE.md), [`../PROVENANCE.csv`](../PROVENANCE.csv) and each skill's attribution line for sources.
