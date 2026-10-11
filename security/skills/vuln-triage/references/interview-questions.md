# Phase 0 interview questions

> Part of the `vuln-triage` skill. Adapted from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145/.claude/skills/triage) (Apache-2.0); modified by ultimate-skills (split out of the upstream SKILL.md).

Ask these in one structured-question call (AskUserQuestion where available; otherwise as one short numbered message). Expect free-text answers; the options are prompts, not constraints.

## Round 1

1. **Environment & trust boundary** (header `Environment`, single-select)
   `What kind of system are these findings from, and where does untrusted
   input enter it?`
   Options: `Internet-facing web service (HTTP is untrusted)`,
   `Internal service (callers are authenticated peers)`,
   `Library / SDK (caller is the trust boundary)`,
   `CLI / batch tool (operator inputs trusted, file inputs not)`,
   `Embedded / firmware (physical access in scope)`.
   Reachability is judged against this boundary; "command injection from env
   var" is a true positive in a multi-tenant web service and a rule-8 false
   positive in an operator CLI.

2. **Threat model** (header `Threat model`, multi-select)
   `What does a worst-case attacker look like for this system, and what
   must never happen? Free text is best.`
   Options: `Unauthenticated remote code execution`,
   `Tenant-to-tenant data leakage`, `Privilege escalation to admin`,
   `Supply-chain compromise of downstream users`,
   `Denial of service against a paid SLA`,
   `Compliance-scoped data exposure (PII / PCI / PHI)`.
   Phase 4 boosts findings that map onto a stated threat.

3. **Scoring standard** (header `Scoring`, single-select)
   `How should severity be expressed in the output?`
   Options: `Derived HIGH/MEDIUM/LOW from preconditions (default)`,
   `CVSS v3.1 vector + base score`, `CVSS v4.0 vector + base score`,
   `OWASP Risk Rating (likelihood x impact)`,
   `Organization bug-bar (describe in Other)`.
   The precondition rule is always computed; this controls what
   `severity_label` additionally shows.

4. **Noise tolerance** (header `Noise tolerance`, single-select)
   `When verifiers disagree, which way should ties break?`
   Options:
   `Precision: drop anything not majority-confirmed (fewer FPs, may miss real bugs)`,
   `Recall: keep split votes as needs_manual_test (more to review, fewer misses)`,
   `Ask me per-finding when it happens`.

