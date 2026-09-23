# engineering

## Overview
Production-grade engineering workflow skills for AI coding agents: the full loop from **spec → plan → build incrementally (or via reviewed subagents) → test-drive → debug from a red feedback loop → verify before claiming done → review → iterate the PR to green → harden → optimize → ship**, plus database, MCP-server and long-horizon-prompting specialisms and lightweight behavioral guardrails.

Curated from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT) and [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (MIT), extended with material from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT), [obra/superpowers](https://github.com/obra/superpowers) (MIT), [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0), [getsentry/skills](https://github.com/getsentry/skills) (Apache-2.0), [supabase/agent-skills](https://github.com/supabase/agent-skills) (MIT), [neondatabase/postgres-skills](https://github.com/neondatabase/postgres-skills) (Apache-2.0) and [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) (MIT).

## Install
```bash
/plugin marketplace add Liohtml/ultimate-skills
/plugin install engineering@ultimate-skills
```

## Skills
22 skills (see the table in the [root README](../README.md#engineering)):

| Stage | Skills |
|---|---|
| Define and plan | `spec-driven-development`, `planning-and-task-breakdown`, `api-and-interface-design` |
| Build | `incremental-implementation`, `subagent-driven-development`, `test-driven-development`, `karpathy-guidelines`, `doubt-driven-development` |
| Debug and verify | `debugging-and-error-recovery`, `verification-before-completion`, `browser-testing-with-devtools` |
| Review and ship | `code-review-and-quality`, `code-simplification`, `iterate-pr`, `git-workflow-and-versioning`, `ci-cd-and-automation`, `documentation-and-adrs` |
| Harden and optimize | `security-and-hardening`, `performance-optimization`, `postgres-best-practices` |
| Specialisms | `mcp-builder`, `long-horizon-prompting` |

Skills trigger automatically on matching tasks, or invoke one by name (e.g. "run code-review-and-quality on this diff").

Some skills bundle helper scripts; their requirements:
- `iterate-pr`: authenticated `gh` CLI, Python 3.9+. Optional `PR_REVIEW_BOTS` / `PR_INFO_BOTS` (comma-separated regexes of bot logins).
- `mcp-builder`: `pip install -r scripts/requirements.txt`; `ANTHROPIC_API_KEY` for the evaluation harness; optional `MCP_EVAL_MODEL`.
- `subagent-driven-development`: bash + git; writes a git-ignored workspace under `.sdd/` in the target repo.
- `debugging-and-error-recovery`: bash; `find-polluter.sh` reads `TEST_CMD` (default `npm test`).

## License
MIT, except `mcp-builder` and `iterate-pr` (Apache-2.0, `LICENSE.txt` in each skill folder) and the Neon-derived operations references in `postgres-best-practices` (Apache-2.0, `LICENSE-neon-apache-2.0.txt`). Apache-2.0 material is marked "Modified by ultimate-skills" where changed. Copies of every upstream license used by this plugin are in [`LICENSES/`](./LICENSES/); see [`../NOTICE.md`](../NOTICE.md) for attribution and [`../PROVENANCE.csv`](../PROVENANCE.csv) for per-skill sources.
