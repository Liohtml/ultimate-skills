---
name: accessibility-audit
description: WCAG 2.2 Level A/AA accessibility audit and remediation for web UI - four evidence passes (injected axe-core scan, keyboard-only pass, contrast/zoom/reflow, screen-reader/semantics), the six criteria new in 2.2 checked first, the 55-criterion A/AA scan list, per-stack fixes, and two output modes - a severity-ranked issue review (code, live page, or design mockup) or a formal conformance table with Pass/Fail/NT/NA per criterion. Never claims conformance without evidence. Use for "is this accessible", a11y/WCAG/ADA/508/EAA audits, contrast/keyboard/focus/ARIA/alt-text/target-size/screen-reader issues, VPAT/ACR preparation, or before shipping user-facing UI. For a fast lint-style pass over UI code (which includes some a11y rules) use web-interface-review; for building accessible components in the first place use frontend-ui-engineering.
---

# Accessibility Audit (WCAG 2.2 A/AA)

> Adapted from [84emllc/claude-wcag-skill](https://github.com/84emllc/claude-wcag-skill) (MIT, (c) 2026 84EM LLC) at commit `792755f`, with the review/audit split, the "NT instead of guessing" rule and the mockup-review path from [masuP9/a11y-specialist-skills](https://github.com/masuP9/a11y-specialist-skills) (MIT, (c) 2025 masuP9) at commit `6615e6e`. Changes: agency/client and WordPress/Hugo framing moved to [references/stack-notes.md](references/stack-notes.md); the verbatim W3C spec file is **not** bundled (it is under the W3C Document License, not MIT) - link to the official spec instead; masuP9's `npx` CLI and Playwright-MCP tool bindings dropped.

## Overview

WCAG 2.2 is a W3C Recommendation (12 December 2024). Conformance is measured against 86 success criteria organized under four principles - **Perceivable, Operable, Understandable, Robust (POUR)** - at three levels (A, AA, AAA). The usual target, and this skill's default, is **Level A + AA** (55 criteria: 31 A + 24 AA). AAA is aspirational, not required.

Core principle: **accessibility is a build requirement verified with tooling, never a self-assessed claim.** Automated scanners catch roughly a third of AA failures. A green axe run is necessary, not sufficient. Every conformance claim needs an automated scan **plus** a manual keyboard-only pass.

Normative text of every criterion (definitions, exceptions, notes): <https://www.w3.org/TR/WCAG22/>. Understanding docs: <https://www.w3.org/WAI/WCAG22/Understanding/>. Quick reference: <https://www.w3.org/WAI/WCAG22/quickref/>. Quote the spec when wording matters; do not paraphrase normative wording into a deliverable.

## When to Use

- Auditing a page, component, theme, or app UI for accessibility
- Remediating reported a11y defects (contrast, focus, keyboard trap, missing labels)
- Building new user-facing UI that must ship WCAG 2.2 AA
- Preparing a VPAT / Accessibility Conformance Report
- Any request mentioning "accessible", "a11y", "WCAG", "screen reader", "508", "ADA", "EAA"

**When NOT to use:** back-end-only work with no rendered UI; a quick UI-code lint (use `web-interface-review`); deciding to *exceed* AA (a scope decision, not an audit).

## Pick the mode first

| | **Issue review** (default) | **Conformance audit** |
|---|---|---|
| Trigger words | review, check, find issues, fix, "is this accessible" | audit, conformance, compliance, VPAT, ACR, formal report |
| Output | Severity-ranked findings (Critical / Major / Minor) with fixes | Pass / Fail / NT / NA for **every** A/AA criterion, with evidence |
| Scope | Practical issues in the target | Full 55-criterion coverage of an agreed page set |

If the goal is unclear, ask once: "Do you want an issue list with fixes, or a formal conformance report?"

**Targets.** Live page or local dev server → run all four passes below. Source code only → static review (semantics, names, roles, focus handling, contrast from tokens); mark runtime-only criteria **NT**. Design mockup / Figma / screenshot → follow [references/design-mockup-review.md](references/design-mockup-review.md) (reviews design intent; contrast values are flagged for measurement, behavior becomes questions for the design team).

**Conformance audit only - agree the scope contract up front:** target level (default 2.2 AA), page set (all / representative / listed URLs, plus complete processes such as checkout), limitations (which assistive tech was actually used), and output format.

## Method: four passes

Run all four. No single pass is sufficient.

1. **Automated scan.** axe-core (axe DevTools, `@axe-core/cli`, `@axe-core/playwright`), Lighthouse, or WAVE. Records the machine-detectable third. Zero violations here is the floor, not the ceiling. If the project has no scanner installed, do not add one as a dependency - inject axe-core into the running page instead. Runnable snippets for a single page, a whole-sitemap run, and validating the harness before trusting its output: [references/running-axe.md](references/running-axe.md). Always report axe's `incomplete` items alongside `violations` - incomplete means "could not decide", not "passed".
2. **Keyboard-only pass.** No mouse. Tab through the entire flow: every interactive element reachable, visible focus ring at each stop, logical order, no trap, Esc closes overlays, focus not hidden behind sticky headers (2.4.11). Skip link works (2.4.1). Focus moves into and back out of dialogs correctly.
3. **Contrast + zoom.** Text 4.5:1 (large text 3:1) - 1.4.3; UI components and focus indicators 3:1 against adjacent colors - 1.4.11. Reflow at 320 CSS px / 400% zoom with no horizontal scroll (1.4.10). Text-spacing overrides don't clip content (1.4.12). Resize text to 200% (1.4.4).
4. **Screen-reader / semantics pass.** VoiceOver, NVDA, or Orca where available; otherwise inspect the accessibility tree (browser DevTools) and say so. Correct headings, landmarks, list/button/link semantics; every image has meaningful or empty alt; every control has a programmatic name that includes its visible label (2.5.3); dynamic changes announce via live regions (4.1.3). Semantic HTML first - ARIA only to fill gaps native elements cannot.

**No evidence, no verdict.** When a pass could not run (no browser, no screen reader, no access to the flow), mark the affected criteria **NT (not tested)** and list them. Never convert missing evidence into Pass or Fail. **NA** only when the content type genuinely does not exist on the page (e.g. no prerecorded video → 1.2.x NA).

## New in WCAG 2.2 (commonly missed - check these first)

WCAG 2.2 added six A/AA criteria over 2.1 and **removed 4.1.1 Parsing** (now always satisfied - do not report it). The additions are the most-often-overlooked failures:

| # | Name | Level | Check |
|---|------|-------|-------|
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Focused element not fully hidden by sticky header/footer/overlay |
| 2.5.7 | Dragging Movements | AA | Any drag action has a single-pointer alternative (tap/click) |
| 2.5.8 | Target Size (Minimum) | AA | Pointer targets ≥ 24×24 CSS px, or adequately spaced (44×44 is the AAA / platform best practice) |
| 3.2.6 | Consistent Help | A | Help mechanisms appear in the same relative order across pages |
| 3.3.7 | Redundant Entry | A | Don't force re-entering info already given in the same process |
| 3.3.8 | Accessible Authentication (Minimum) | AA | No cognitive-function test (transcription, memorization, puzzle) as the only auth path; allow paste and password managers |

## Level A / AA criteria checklist (55)

This is the scan list - every item must pass for AA. Full text: <https://www.w3.org/TR/WCAG22/>.

**1. Perceivable** - 1.1.1 Non-text Content · 1.2.1 Audio/Video-only (Prerecorded) · 1.2.2 Captions (Prerecorded) · 1.2.3 Audio Description or Media Alternative · 1.2.4 Captions (Live) · 1.2.5 Audio Description (Prerecorded) · 1.3.1 Info & Relationships · 1.3.2 Meaningful Sequence · 1.3.3 Sensory Characteristics · 1.3.4 Orientation · 1.3.5 Identify Input Purpose · 1.4.1 Use of Color · 1.4.2 Audio Control · 1.4.3 Contrast (Minimum) · 1.4.4 Resize Text · 1.4.5 Images of Text · 1.4.10 Reflow · 1.4.11 Non-text Contrast · 1.4.12 Text Spacing · 1.4.13 Content on Hover or Focus

**2. Operable** - 2.1.1 Keyboard · 2.1.2 No Keyboard Trap · 2.1.4 Character Key Shortcuts · 2.2.1 Timing Adjustable · 2.2.2 Pause, Stop, Hide · 2.3.1 Three Flashes or Below Threshold · 2.4.1 Bypass Blocks · 2.4.2 Page Titled · 2.4.3 Focus Order · 2.4.4 Link Purpose (In Context) · 2.4.5 Multiple Ways · 2.4.6 Headings & Labels · 2.4.7 Focus Visible · 2.4.11 Focus Not Obscured (Minimum) · 2.5.1 Pointer Gestures · 2.5.2 Pointer Cancellation · 2.5.3 Label in Name · 2.5.4 Motion Actuation · 2.5.7 Dragging Movements · 2.5.8 Target Size (Minimum)

**3. Understandable** - 3.1.1 Language of Page · 3.1.2 Language of Parts · 3.2.1 On Focus · 3.2.2 On Input · 3.2.3 Consistent Navigation · 3.2.4 Consistent Identification · 3.2.6 Consistent Help · 3.3.1 Error Identification · 3.3.2 Labels or Instructions · 3.3.3 Error Suggestion · 3.3.4 Error Prevention (Legal, Financial, Data) · 3.3.7 Redundant Entry · 3.3.8 Accessible Authentication (Minimum)

**4. Robust** - 4.1.2 Name, Role, Value · 4.1.3 Status Messages

## Per-stack remediation notes

**Generic HTML/CSS.** Semantic elements before ARIA (`<button>` not `<div role=button>`, `<nav>`/`<main>`/`<header>` landmarks, real headings in order). `:focus-visible` styling meeting 3:1 against adjacent colors. `prefers-reduced-motion` guards on animation. Decorative images `alt=""`; informative images described. Labels via `<label for>` or `aria-label`, never placeholder-as-label. `<html lang>` set; `lang` on foreign-language passages (3.1.2).

**React / Tailwind.** Manage focus on route change and modal open/close (trap inside, return on close, Esc to dismiss). shadcn/Radix/React Aria primitives are accessible by default - don't strip their ARIA. Tailwind `focus-visible:` utilities must hit 3:1; the default `outline-none` without a replacement is a 2.4.7 failure. Announce async state with a polite live region. Icon-only buttons need `aria-label`. Verify target size (2.5.8) - `h-6 w-6` (24px) is the floor.

WordPress block themes, Hugo/static-site generators and other frameworks: [references/stack-notes.md](references/stack-notes.md). Quick component-level checklist for builders: [../../references/accessibility-checklist.md](../../references/accessibility-checklist.md).

## Reporting

**Issue review.** Group by severity, highest first. Each finding: `criterion number + name → failing element (file:line, selector, or frame) → impact → fix`.
- **Critical** - blocks access (keyboard trap, unlabeled form control on a key flow, missing alt on functional image, auth that requires a cognitive test).
- **Major** - creates a barrier (low contrast, focus not visible, color-only state, target too small).
- **Minor** - best-practice improvement (heading order polish, redundant ARIA).
Close with what was **not** verified (NT list) and the passes that ran.

**Conformance audit.** A table with one row per A/AA criterion: `Criterion | Level | Status (Pass/Fail/NT/NA) | Evidence | Notes`. Then a summary: counts per status and level, scope and page set, tools and assistive tech actually used, limitations, and the open NT items. A single Fail at A or AA means the page set does not conform.

## Common mistakes

| Mistake | Reality |
|---|---|
| "axe passed, so it's AA." | axe covers ~a third of AA. Manual keyboard + SR passes are required. |
| "I loaded the page, looks fine." | Passive load misses keyboard traps, focus order, SR announcements, state changes. Exercise the flow. |
| Reporting 4.1.1 Parsing | Removed in WCAG 2.2. Never cite it. |
| Guessing a status without evidence | Use NT and list it; a wrong Pass in an ACR is worse than an honest gap. |
| Color alone signals state | 1.4.1 fails. Add text/icon/pattern. |
| Placeholder used as the label | Vanishes on input, fails 3.3.2 Labels or Instructions. Use `<label>`. |
| `role="button"` on a `<div>` | Loses keyboard + focus for free. Use `<button>`. |
| Paraphrasing criterion text into a deliverable | Quote the W3C spec verbatim; paraphrase invents normative meaning. |
| "Focus ring removed for design" | `outline:none` with no replacement fails 2.4.7. Provide a visible `:focus-visible` style. |

## Do not claim compliance without evidence

Never state "meets WCAG 2.2 AA" until an automated scan **and** a manual keyboard-only pass have both run and their output is in hand. Report what was tested, at which level, with which tool. A hedged "not yet verified" beats a confident wrong conformance claim in a client-facing ACR.
