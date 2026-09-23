# Checkpointing protocol

> Part of the `vuln-triage` skill. Adapted from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145/.claude/skills/triage) (Apache-2.0); modified by ultimate-skills (split out of the upstream SKILL.md).

Runs before Phase 0 and after every phase.

On large finding batches a full run can exhaust context or hit rate limits
mid-way — particularly Phase 3, which spawns `candidates × votes` verifiers.
Phase state persists to `./.triage-state/` so a fresh `vuln-triage` session can
resume without re-asking the interview or re-spawning verifiers.

All checkpoint I/O goes through `python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py`
(atomic writes, JSON-validated). Never use the Write tool for `progress.json`
directly. Never pass payload via heredoc or stdin; target-derived strings
could collide with the heredoc delimiter and break out to shell. The
Write→`--from` pattern keeps repo-derived bytes out of Bash argv.

State files in `./.triage-state/`:
- `progress.json` — **single source of truth** for resume position:
  `{"status": "running"|"complete", "phase_done": N, "shards_done": [...]}`.
  Resume decisions read ONLY this file, never a glob of `phase*.json` or
  shard files (stale files from a prior run must not be trusted).
- `phaseN.json` — data payload for phase N (schemas at the tail of each phase
  section below).
- `_chunk.tmp` — transient payload buffer; overwritten before every
  `save`/`shard`/`append` call.

**Start of run — resume check.** Bash:
`python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py load ./.triage-state`

- `status == "absent"` OR `"complete"`, OR `--fresh` in the invocation arguments →
  **fresh start.** Bash:
  `python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py reset ./.triage-state`,
  then proceed to Phase 0.
- `status == "running"` with `phase_done == N` → **resume.** Read
  `./.triage-state/phase0.json` through `phaseN.json` **in order** (and any
  `shard_*.json` files listed in `shards_done`), merging keys into working
  state (later files override earlier — checkpoints may be deltas). Print
  `Resuming from checkpoint: Phase N complete (./.triage-state/phaseN.json)`,
  and **skip directly to Phase N+1**.

**End of every phase N.** Two tool calls:
1. Write tool → `./.triage-state/_chunk.tmp` containing the phase's output
   JSON (schema at the tail of each phase section).
2. Bash → `python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py save ./.triage-state <N> <name> --from ./.triage-state/_chunk.tmp`

**End of run.** After writing `TRIAGE.json` and `TRIAGE.md`, Bash:
`python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py done ./.triage-state 6`

## Phase 3 per-candidate shards

This is the most expensive checkpoint. When `len(candidates) * votes` exceeds
~40 and verifier spawns are sharded into sequential batches, additionally
checkpoint **per candidate** as its votes are tallied:

1. Write tool → `./.triage-state/_chunk.tmp` = that finding's post-tally dict.
2. Bash:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/checkpoint.py shard ./.triage-state <id> --from ./.triage-state/_chunk.tmp`

On resume at `phase_done == 2`, the Phase-3 entry point reads
`progress.json:shards_done` (default `[]` — do **not** glob shard files on
disk; stale shards from a prior run may exist), loads the corresponding
`shard_{id}.json` files, and spawns verifiers only for `candidates[]` ids
from `phase2.json` that are NOT in `shards_done`. Once every candidate is in
`shards_done`, write the consolidated `phase3.json` checkpoint as above.
