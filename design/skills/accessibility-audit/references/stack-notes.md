# Per-stack remediation notes

> Adapted from [84emllc/claude-wcag-skill](https://github.com/84emllc/claude-wcag-skill) `SKILL.md` ("Per-stack remediation notes") at commit `792755f` (MIT, (c) 2026 84EM LLC). Moved out of the main skill; client/agency framing removed. Generic HTML/CSS and React/Tailwind notes stay in `SKILL.md`.

## WordPress (block themes)

Contrast lives in `theme.json` color palette - validate every text/background preset pair, don't inline-style. Patterns use block markup (`<!-- wp:group -->`), so semantics come from block choice: use Heading blocks in order, Button blocks (not styled paragraphs), Navigation block for menus. Check the active theme's skip-link and focus styles; many themes ship weak focus rings. Plugin admin UIs need the same four passes - form labels, `aria-describedby` on errors, nonce-guarded but still labeled controls.

## Hugo (and other static-site generators)

Accessibility is authored in templates/partials, not content - but content vs template separation still holds: alt text comes from front matter or page resources, never hardcoded in the partial. Ensure the base template sets `<html lang>`, one `<h1>` per page, a skip link partial, and that shortcodes producing media require an `alt` param. Check generated markup with axe against the built site, not the source.

## Vue / Svelte / Angular

The React notes in `SKILL.md` carry over: manage focus on route change and on dialog open/close, keep the accessible primitives of your component library intact (do not strip their ARIA), announce async state through a polite live region, and give icon-only buttons an accessible name.
