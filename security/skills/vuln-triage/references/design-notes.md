# Design notes

> Part of the `vuln-triage` skill. Adapted from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145/.claude/skills/triage) (Apache-2.0); modified by ultimate-skills (split out of the upstream SKILL.md).


- **Checkpoints are per-phase JSON**, not conversation state. Resuming a
  session restores transcript history but doesn't help when the
  orchestrator's context window itself fills; file-backed checkpoints let a brand-new session pick up from the last
  completed phase. `./.triage-state/` is scratch — add to `.gitignore`.
- **Dedupe runs before verify** to cut verifier spend by the duplication
  factor (often 2-4x on multi-scanner input) at the cost of one cheap
  subagent.
- **Semantic dedupe is one agent**, given only id/file/line/category/title:
  enough to cluster, not enough to leak one scanner's reasoning into
  another finding's verification.
- **Shell is used narrowly** for `git log` (owner hints), `jq`/`find`
  (ingest), and `scripts/checkpoint.py` (state I/O).
  The actual safety property is "no execution of target code," which is
  preserved.
- **`CANNOT_VERIFY`** exists so verifiers aren't forced into a false
  binary. It maps to `needs_manual_test` under recall policy and to a drop
  under precision policy.
- **Threat-model boost is capped at one step** so a stated threat can't
  re-inflate a LOW back to HIGH and defeat the precondition rule.
- **`severity_label` is separate from `severity`.** Sorting always uses the
  precondition-derived HIGH/MEDIUM/LOW; the label is presentation-layer for
  whatever standard the reviewer's tooling expects.
- **Sharding at ~40 parallel Tasks** is a conservative ceiling for typical
  agent-spawn limits; tune up if your runtime allows.
- **No network**, deliberately. CVE-database enrichment and upstream-fix
  checks would help ranking but break the air-gapped-review property.

## Runtime recovery for backgrounded subagents

**If any subagent call returns `status: "async_launched"` instead of the
verifier's text**, the runtime backgrounded it (some runtimes do this
automatically for large parallel batches). Pick one recovery and use it for
the whole batch:
  - If completion notifications arrive in your conversation: parse each
    verifier's VERDICT block from its notification `result` as it lands.
    Do not end your turn until every vote is accounted for.
  - If notifications do not arrive: do not poll transcript files. Re-spawn
    the missing verifiers in a fresh subagent batch (smaller shard size, e.g.
    10) and use the synchronous results.
The same recovery applies to the dedupe subagent in 2b and the ranking
subagents in 4a.

