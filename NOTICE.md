# NOTICE — Attribution & Provenance

`ultimate-skills` is a **curated compilation**. Every skill is the work of its
original author, copied here under that work's license. No claim of authorship is
made over the upstream skills. Full machine-readable provenance (one row per
skill) is in [`PROVENANCE.csv`](./PROVENANCE.csv).

## Source repositories

| Source repo | Author | License | Plugin(s) it feeds | Skills taken |
|---|---|---|---|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | MIT | `engineering`, `design` | 16 (15 eng + frontend-ui-engineering) |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | forrestchang / multica-ai | MIT | `engineering` | 1 (karpathy-guidelines) |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Paweł Huryn | MIT | `product` | 13 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx | MIT | `design` | 5 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Cheng-I Wu | **CC-BY-NC-4.0** | `research` | 4 |

Verbatim copies of each upstream LICENSE are in [`LICENSES/`](./LICENSES/).

## ⚠️ Mixed licensing — read before commercial use

- `engineering/`, `product/`, `design/` → **MIT** (permissive, commercial OK).
- `research/` → **CC-BY-NC-4.0** (© 2026 Cheng-I Wu): **attribution required,
  NON-COMMERCIAL only, no relicensing.** It is isolated in its own plugin so you
  can drop it cleanly. To produce a fully-permissive marketplace, delete the
  `research/` directory and remove its entry from
  `.claude-plugin/marketplace.json`.

## What the curation changed

- Selected **39 of 109** upstream skills; dropped thin one-shot generators and
  near-duplicates (e.g. the `brainstorm-*` / `identify-assumptions-*` clusters,
  classic-framework fill-ins, redundant taste-style presets).
- Renamed each skill **directory to match its `SKILL.md` frontmatter `name:`**
  (Claude Code plugin requirement). SKILL.md bodies are otherwise unmodified.
- Regrouped skills by discipline into four plugins; authored fresh
  marketplace/plugin manifests and READMEs.
