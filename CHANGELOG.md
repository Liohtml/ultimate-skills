# Changelog

## Unreleased

### Fixed
- `research`: vendored the 81 upstream `shared/` files the skills reference into
  `research/shared/` (upstream `Imbad0202/academic-research-skills@95929c0`), fixed
  all broken relative links, and noted that upstream `scripts/` and `docs/design/`
  are optional and not included. Removed generic triggers ("research",
  "help me think through", …) from `deep-research`.
- `design`: `image-to-code` and `imagegen-frontend-web` are no longer Codex-specific,
  document the image-generation prerequisite, fall back to `design-taste-frontend`
  without one, and are delimited from each other.
- Trigger collisions: `pre-mortem` ↔ `strategy-red-team`,
  `design-taste-frontend` ↔ `redesign-existing-projects`; narrowed the
  "any change" triggers of `git-workflow-and-versioning`, `test-driven-development`,
  `incremental-implementation` and `code-review-and-quality`; added disambiguators
  between overlapping engineering skills.
- Marked dead references to upstream-only skills (`context-engineering`,
  `deprecation-and-migration`, `source-driven-development`).

### Added
- `scripts/validate.py` (frontmatter, manifests, relative links, SKILL.md size warnings)
  and `.github/workflows/validate.yml` (also runs `claude plugin validate --strict`).
- `scripts/check_upstream.py` to report upstream changes since the recorded commit.
- `PROVENANCE.csv`: `source_commit` and `upstream_status` columns.
- `docs/value-bombs.md`: ranked candidates from other skill repositories for future waves.

## 1.0.0
- Initial curated release: 39 skills in 4 plugins.
