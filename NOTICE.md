# NOTICE: Attribution & Provenance

`ultimate-skills` is a **curated compilation**. Every skill is the work of its
original authors, copied or adapted here under that work's license. No claim of
authorship is made over the upstream material. Machine-readable provenance is
in [`PROVENANCE.csv`](./PROVENANCE.csv): one row per upstream source of every
skill. `role=base` is the source a skill was built on; `role=merged` is
material merged into it from another source. Each row also records the
upstream commit and the upstream paths used.

## Source repositories

34 source repositories. "Skills" counts the skills that were built on the
repo (`base`); "merged into" lists skills that took material from it.

| Source repo | Copyright holder / author | License | Plugin(s) | Skills (base) / merged into | License file |
|---|---|---|---|---|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | MIT | `engineering`, `design` | 16 (15 engineering + `frontend-ui-engineering`); also the vendored `engineering/references/` and `design/references/` checklists | `agent-skills.LICENSE` |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | forrestchang / multica-ai | MIT (README-asserted, see below) | `engineering` | 1 (`karpathy-guidelines`) | `andrej-karpathy-skills.LICENSE` |
| [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent | MIT | `engineering` | 2 (`verification-before-completion`, `subagent-driven-development`) / merged into `iterate-pr` (receiving-code-review), `debugging-and-error-recovery` (`find-polluter.sh`) | `superpowers.LICENSE` |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock | MIT | `engineering` | merged into `debugging-and-error-recovery` (diagnosing-bugs, `hitl-loop.template.sh`) | `mattpocock-skills.LICENSE` |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic, PBC | Apache-2.0 (per-skill `LICENSE.txt`) | `engineering` | 1 (`mcp-builder`) | `anthropics-skills-mcp-builder.LICENSE` |
| [getsentry/skills](https://github.com/getsentry/skills) | Functional Software, Inc. dba Sentry | Apache-2.0 | `engineering`, `security` | 3 (`iterate-pr`, `gha-security-review`, `skill-scanner`) | `getsentry-skills.LICENSE` |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | Supabase | MIT | `engineering` | 1 (`postgres-best-practices`, renamed from `supabase-postgres-best-practices`) | `supabase-agent-skills.LICENSE` |
| [neondatabase/postgres-skills](https://github.com/neondatabase/postgres-skills) | Neon | Apache-2.0 | `engineering` | merged into `postgres-best-practices` (backup/restore, major-version upgrades, migration-safety table) | `neondatabase-postgres-skills.LICENSE` |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | Context Engineering Agent Skills Contributors | MIT | `engineering` | 1 (`long-horizon-prompting`) | `Agent-Skills-for-Context-Engineering.LICENSE` |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Paweł Huryn | MIT | `product` | 13 | `pm-skills.LICENSE` |
| [wondelai/skills](https://github.com/wondelai/skills) | Wondel.ai sp. z o.o. | MIT | `product` | 2 (`product-positioning` ← obviously-awesome, `strategy-kernel` ← good-strategy-bad-strategy) | `wondelai-skills.LICENSE` |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Anthropic | Apache-2.0 | `product` | 1 (`validate-data`) / merged into `create-prd` (write-spec), `user-personas` (synthesize-research) | `knowledge-work-plugins.LICENSE` |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Alireza Rezvani (skill author: Abbas Mir) | MIT | `product` | 1 (`saas-metrics-coach`) | `alirezarezvani-claude-skills.LICENSE` |
| [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) | Ferdinando Bons | MIT | `product` | merged into `competitor-analysis` (honesty protocol, verification pass) | `startup-skill.LICENSE` |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx | MIT | `design` | 5 | `taste-skill.LICENSE` |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Vercel Labs | MIT | `design` | 1 (`web-interface-review`) | `web-interface-guidelines.LICENSE` |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Emil Kowalski | MIT | `design` | 1 (`motion-craft` ← animate + review-animations) | `emilkowalski-skills.LICENSE` |
| [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) | Damola Akinleye | MIT | `design` | 1 (`interface-design`) | `interface-design.LICENSE` |
| [84emllc/claude-wcag-skill](https://github.com/84emllc/claude-wcag-skill) | 84EM LLC | MIT (the W3C-licensed spec file was **not** taken) | `design` | 1 (`accessibility-audit`, renamed from wcag-2.2-aa) | `claude-wcag-skill.LICENSE` |
| [masuP9/a11y-specialist-skills](https://github.com/masuP9/a11y-specialist-skills) | masuP9 | MIT | `design` | merged into `accessibility-audit` (review/conformance modes, mockup review) | `a11y-specialist-skills.LICENSE` |
| [openai/skills](https://github.com/openai/skills) | OpenAI | Apache-2.0 (per-skill `LICENSE.txt`) | `design` | 1 (`image-generation` ← imagegen) | `openai-skills-imagegen.LICENSE` |
| [jezweb/claude-skills](https://github.com/jezweb/claude-skills) | Jeremy Dawes (Jezweb) | MIT | `design` | 1 (`icon-set-generator`) / merged into `image-generation` (provider routing) | `jezweb-claude-skills.LICENSE` |
| [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | Wuyoscar | MIT | `design` | merged into `image-generation` (prompt craft; gallery prompts **not** taken) | `GPT-Image2-Skill.LICENSE` |
| [replicate/skills](https://github.com/replicate/skills) | Replicate, Inc. | Apache-2.0 | `design` | merged into `image-generation` (model-agnostic prompting) | `replicate-skills.LICENSE` |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | Zara Zhang | MIT | `design` | 1 (`frontend-slides`) | `frontend-slides.LICENSE` |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus | Apache-2.0 | `design` | merged into `redesign-existing-projects` (craft floor, heuristic critique) | `impeccable.LICENSE` (+ `impeccable.NOTICE.md`) |
| [millwright-labs/minto-pyramid-skill](https://github.com/millwright-labs/minto-pyramid-skill) | Millwright Labs | MIT | `writing` | 1 (`minto-pyramid`) | `minto-pyramid-skill.LICENSE` |
| [tyroneross/pyramid-principle](https://github.com/tyroneross/pyramid-principle) | Tyrone Ross | Apache-2.0 | `writing` | merged into `minto-pyramid` (`references/audit-report.md`) | `pyramid-principle.LICENSE` |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | MIT | `writing` | 1 (`copy-editing`) | `marketingskills.LICENSE` |
| [blader/humanizer](https://github.com/blader/humanizer) | Siqi Chen | MIT | `writing` | 1 (`humanizer`) | `humanizer.LICENSE` |
| [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) | Anthropic PBC | Apache-2.0 | `security` | 3 (`threat-model`, `static-vuln-scan` ← vuln-scan, `vuln-triage` ← triage) | `defending-code-reference-harness.LICENSE` |
| [briiirussell/cybersecurity-skills](https://github.com/briiirussell/cybersecurity-skills) | Bri Russell | MIT | `security` | 2 (`web-pentest` incl. recon, `llm-app-security-audit` ← prompt-injection) | `cybersecurity-skills.LICENSE` |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Trail of Bits | **CC-BY-SA-4.0** | `security-cc-by-sa` | 2 (`supply-chain-risk-auditor`, `variant-analysis`) | `trailofbits-skills.LICENSE` |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Cheng-I Wu | **CC-BY-NC-4.0** | `research` | 4 (+ vendored `research/shared/`) | `academic-research-skills.LICENSE` |

All license files are in [`LICENSES/`](./LICENSES/). Each plugin carries copies
of the licenses of its own sources, so an installed plugin keeps its notices
on its own: `<plugin>/LICENSES/` for `engineering`, `product`, `design`,
`writing` and `security`, and `<plugin>/LICENSE` for `research` and
`security-cc-by-sa`. Apache-2.0 and CC-BY-SA skills also ship the license next
to the material (`LICENSE.txt` in the skill folder, or
`LICENSE-neon-apache-2.0.txt` / `audit-report.LICENSE.txt` /
`redesign-existing-projects/references/impeccable.LICENSE.txt` next to merged
files).

The license files are verbatim upstream copies, with one exception.
[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
ships **no standalone LICENSE file**; its MIT grant appears only in the
upstream README ("License: MIT"). `andrej-karpathy-skills.LICENSE` is
therefore a reconstruction of the standard MIT text under that grant, not a
verbatim upstream copy; its copyright line is inferred because upstream names
no holder.

One file was taken from a more specific upstream location:
`knowledge-work-plugins.LICENSE` (and `validate-data/LICENSE.txt`) is the
verbatim `data/LICENSE` of anthropics/knowledge-work-plugins, the license of
the `data` plugin that `validate-data` comes from. The repo-root `LICENSE` at
the pinned commit is the same Apache-2.0 text followed by stray non-license
lines, which were not copied. `create-prd/LICENSE.txt` and
`user-personas/LICENSE.txt` are the same file: upstream
`product-management/LICENSE`, the license of the plugin that `write-spec` and
`synthesize-research` come from, is byte-identical to `data/LICENSE`.

## Apache-2.0 notice obligations

Material under Apache-2.0: `mcp-builder`, `iterate-pr`, `gha-security-review`,
`skill-scanner`, `threat-model`, `static-vuln-scan`, `vuln-triage`,
`image-generation` (openai base and replicate reference), `validate-data`, the
knowledge-work-plugins material merged into `create-prd` (from `write-spec`)
and `user-personas` (from `synthesize-research`) and the reference files built
on it, the Neon-derived `postgres-best-practices/references/ops-*` files, the impeccable
references in `redesign-existing-projects`, and
`minto-pyramid/references/audit-report.md`. This compilation meets §4 as
follows:

- **§4(a) license copy:** the Apache-2.0 text is shipped next to the material and in `LICENSES/`.
- **§4(b) modification notices:** every modified Apache-2.0 file or skill says "Modified by ultimate-skills" (or has a change note at the end of `SKILL.md`, or a notice in the script docstring) and lists what changed.
- **§4(c) retained notices:** upstream copyright, patent, trademark and attribution notices are kept. Each skill names its source in an attribution line.
- **§4(d) NOTICE files:** none of the Apache-2.0 upstreams used here ships a NOTICE file that covers material we took.
  - `anthropics/skills`, `getsentry/skills`, `neondatabase/postgres-skills`, `replicate/skills`, `tyroneross/pyramid-principle`, `anthropics/knowledge-work-plugins`, `anthropics/defending-code-reference-harness` have no NOTICE file, and the `openai/skills` imagegen skill has none (the NOTICE files in that repo belong to other skills).
  - `pbakaus/impeccable` has a `NOTICE.md`. It covers only `ios.md` and `android.md` (derived from ehmo/platform-design-skills, MIT), and neither file was taken. A copy is kept as [`LICENSES/impeccable.NOTICE.md`](./LICENSES/impeccable.NOTICE.md) and in `design/LICENSES/` for completeness.
  - `anthropics/skills` has a repo-level `THIRD_PARTY_NOTICES.md`. It concerns bundled fonts and other third-party files, not `mcp-builder`.

## Excluded third-party material

We deliberately did **not** take the following, because they are under a different license or have unclear rights:

- the W3C WCAG 2.2 spec copy in `84emllc/claude-wcag-skill` (W3C Document License); `accessibility-audit` links to w3.org instead;
- `long-horizon-prompting`'s `cdc-prompt-annotated.md`, which reproduces OpenAI's published prompt verbatim; the skill links to it upstream;
- the third-party gallery prompts in `wuyoscar/GPT-Image2-Skill`;
- `copy-editing`'s plain-English alternatives list (derived from the Plain English Campaign list);
- `tyroneross/pyramid-principle`'s `docs/source-anchors.md`, which holds verbatim book excerpts; our audit reference uses plain page references to Minto (2009) instead;
- the upstream `humanizer` before/after examples, which were quoted from Wikipedia's "Signs of AI writing" page (CC BY-SA 4.0); they were replaced with original examples.

`humanizer`'s pattern categories are informed by Wikipedia's "Signs of AI
writing" (WikiProject AI Cleanup, CC BY-SA 4.0). We replaced the upstream
before/after examples, which were quoted from that page, with original
examples, and reworded the pattern descriptions and watch lists. A check
against the current page and 17 revisions from June 2025 to October 2026 found
no shared sequence of 6 or more words. What remains in common is the taxonomy
and a few very short phrases that are the tells themselves (for example
"nestled", "in the heart of", "I hope this helps"). These are ideas and stock
phrases, not share-alike text, so no CC BY-SA material remains in the MIT
`writing` plugin.

## ⚠️ Mixed licensing: read before commercial use

- **`engineering/`, `product/`, `design/`, `writing/`, `security/` are permissive.** Each skill is MIT or Apache-2.0 (plugin license `MIT AND Apache-2.0`), and commercial use is allowed. Keep the license files and the modification notices when you redistribute.
- **`security-cc-by-sa/` is CC-BY-SA-4.0** (Trail of Bits). Attribution is required, and commercial use is allowed. **Share-alike:** adapted versions you distribute must be CC-BY-SA-4.0. Never copy these skills into an MIT or Apache-2.0 plugin.
- **`research/` is CC-BY-NC-4.0** (© 2026 Cheng-I Wu). Attribution is required, **non-commercial use only**, and it may not be relicensed. Each research `SKILL.md` names the source, the license and the fact that it was modified (CC BY-NC 4.0 §3(a)); `research/shared/README.md` does the same for the vendored files. The `references/` files split out of the four research skills (wave 3 and upstream sync 2) are upstream text moved verbatim and say so in their first line; [`research/MERGE_MAPS.md`](./research/MERGE_MAPS.md) maps them back to upstream.
- `scripts/validate.py` enforces this split: a `PROVENANCE.csv` row whose license is not part of its plugin's `plugin.json` license fails validation.
- **For a fully permissive marketplace**, delete `research/` and `security-cc-by-sa/` and remove their entries from `.claude-plugin/marketplace.json`.

## What the curation changed

- **Selection.** Wave 1 kept 39 of 109 skills from five repos. Wave 2 scouted about 90 repos and added 29 skills (9 of them security, from a separate security scout), plus material merged into existing skills. Wave 3 added no skills; it deepened existing ones (see below). Thin one-shot generators, near-duplicates, unlicensed repos and license-laundered copies were dropped. The ranked candidate list, with an integration status for each, is in [`docs/value-bombs.md`](./docs/value-bombs.md).
- **Names.** Each skill **directory matches its `SKILL.md` frontmatter `name:`**. Several skills were renamed so the names are vendor-neutral or clearer:
  - `supabase-postgres-best-practices` → `postgres-best-practices`
  - `obviously-awesome` → `product-positioning`
  - `good-strategy-bad-strategy` → `strategy-kernel`
  - `wcag-2.2-aa` → `accessibility-audit`
  - `vuln-scan` → `static-vuln-scan`
  - `triage` → `vuln-triage`
  - `prompt-injection` → `llm-app-security-audit`
  - `imagegen` → `image-generation`
- **Local modifications.** Details are in [`CHANGELOG.md`](./CHANGELOG.md), and `PROVENANCE.csv` marks each source as `identical-to-head` or `modified-locally`.
  - Frontmatter `description:` fields were rewritten with specific "Use when …" triggers and "For X use Y" pointers between neighbouring skills.
  - Links to upstream skills that are not part of this curation were rewritten or marked.
  - Vendor, harness and runtime specifics were generalised: Codex tooling, `superpowers:*` sibling skills, Sentry-only bots and harness pipelines.
  - Skills over 500 lines were split into `SKILL.md` plus `references/`: three design skills in wave 2; `deep-research`, `academic-paper` and `academic-pipeline` in wave 3; and `academic-paper-reviewer` in upstream sync 2, which also moved further sections out of the other three as upstream grew. Research sections are moved verbatim (map: [`research/MERGE_MAPS.md`](./research/MERGE_MAPS.md)).
  - Offensive-security skills gained written authorization and scope gates.
  - Wave 3 deepened `create-prd`, `user-personas`, `prioritization-frameworks` and `value-proposition` with mostly original text plus new `references/`; only `create-prd` and `user-personas` merge outside material (anthropics/knowledge-work-plugins, Apache-2.0, rewritten). The new text names the people behind the methods it uses (for example Olsen, Ulwick, Reinertsen, Kano, Osterwalder, Moesta, Cagan) and explains the methods in its own words.
  - `humanizer`'s before/after examples, pattern descriptions and watch lists are original text (see above). Upstream sync 2 adopted the upstream 3.1.0 rules and taxonomy (for example §26 and the new family F) in original wording with original examples; Wikipedia remains credited for the pattern categories only.
  - `security-and-hardening` was narrowed to code being built, with pointers to the `security` plugin for auditing and testing.
  - Bundled scripts were fixed where they were broken or stale:
    - `mcp-builder` `evaluation.py`: a retired model ID, and parallel `tool_use` handling.
    - `image-generation` `image_gen.py`: model and size guards.
    - `find-polluter.sh`: the test command is now configurable, test paths with spaces are kept intact, and it exits 2 instead of reporting "clean" when no test file matches or the artifact already exists.
    - `frontend-slides` `export-pdf.sh`: Playwright pinned, the preview server bound to 127.0.0.1 with a path-traversal fix, relative output paths fixed.
    - `skill-scanner` `scan_skill.py`: `--help`, a JSON error when PyYAML is missing, no following of symlinks out of the skill directory, masked secrets in evidence, no crash on YAML dates, a working HTTP-exfiltration pattern and reporting of `!`-fenced load-time blocks (output keys unchanged).
  - Every change to Apache-2.0 material is noted in the file it changed.
  - `research/`: the upstream `shared/` files the skills reference were vendored into `research/shared/` (verbatim except rewritten relative links and "not included here" markings for upstream-only material; see `research/shared/README.md`). Upstream helper scripts, design docs, slash commands and the fifth upstream skill `sr-screener` are not included.
  - Upstream syncs re-merge upstream changes into the curated skills and keep these local modifications; the commit each source is synced to is in `PROVENANCE.csv`, and what each sync took is in [`CHANGELOG.md`](./CHANGELOG.md).
- **Structure.** Skills are regrouped by discipline into seven plugins. The marketplace and plugin manifests and the READMEs were written fresh.
