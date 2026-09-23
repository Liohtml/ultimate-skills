# Dedupe and ranking prompts (Phases 2b and 4a)

> Part of the `vuln-triage` skill. Adapted from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145/.claude/skills/triage) (Apache-2.0); modified by ultimate-skills (split out of the upstream SKILL.md).

## Phase 2b — semantic dedupe prompt (one subagent, only if >1 cluster survives)

Spawn ONE Task with `subagent_type: "general-purpose"` and this prompt:

```
You are deduplicating security findings before expensive verification. Two
findings are DUPLICATES if fixing one would also fix the other. Two findings
are DISTINCT if they have genuinely independent root causes, even if they
share a category or file.

Treat as DUPLICATE:
- Same root cause described with different wording or by different scanners
- A shared vulnerable helper function reported once per call site
- A missing global protection (auth check, output encoding) reported once
  per endpoint that lacks it
- A cause ("missing input validation on `name`") and its consequence
  ("SQL injection via `name`") in the same code path

Treat as DISTINCT:
- Different categories in the same file region (an "ssrf" near a
  "buffer_overflow" is not a duplicate just because the lines are close)
- Same file, same category, but different tainted variables reaching
  different sinks
- Same helper, but two independent bugs inside it
- Two endpoints missing the same check, where the fix is per-endpoint
  rather than a shared gate

Below are the candidate findings (one per line: id | file:line | category |
title). Group them. Respond with ONLY lines of the form:

  GROUP: <canonical_id> <- <dup_id>, <dup_id>, ...

One line per group that has duplicates. Omit singletons. Pick the most
specific / best-described finding as canonical. No prose.

CANDIDATES:
{one line per surviving finding: "f003 | src/auth.py:112 | sql_injection | User lookup concatenates name into query"}
```


## Phase 4a — ranking prompt (one subagent per confirmed finding)

Spawn one Task per confirmed finding (`subagent_type: "general-purpose"`,
all in one message) with:

```
You are assigning severity to a CONFIRMED security finding. Verification
already happened; assume the finding is real. Your only job is to derive
how bad it is, independently of what the scanner claimed.

You may Read/Grep the codebase at {REPO_PATH} to check preconditions. Do
NOT execute code.

ENVIRONMENT: {context.environment}
THREAT MODEL (operator-stated, may be empty):
{context.threat_model as bullets, or "(none provided)"}
SCORING STANDARD: {context.scoring}

FINDING:
  id:        {id}
  file:      {file}:{line}
  category:  {category}
  claimed severity: {severity}
  reachability evidence: {first_links from Phase 3}
  verifier rationale: {rationale from Phase 3}

────────────────────────────────────────────────────────────────────────
STEP 1: Enumerate EVERY precondition that must hold for exploitation.
Be concrete: required auth state, configuration, prior request, race
window, attacker position. Then state the minimum ACCESS LEVEL required
(unauthenticated remote / authenticated / local / physical).

STEP 2: Derive severity from the precondition count and access level:

  | Preconditions | Access required          | Severity |
  |---------------|--------------------------|----------|
  | 0             | Unauthenticated remote   | HIGH     |
  | 1-2           | Authenticated            | MEDIUM   |
  | 3+            | Local-only / no demo path| LOW      |

  Evaluate each column independently and take the LOWER result. Example:
  0 preconditions but authenticated-only is MEDIUM, not HIGH; 1
  precondition but local-only is LOW. Cross-check: if your preconditions
  list has 3+ items, HIGH is almost certainly wrong.

STEP 3: Threat-model match. If the THREAT MODEL is non-empty and this
finding maps onto one of its entries, note which one. A match may raise
severity by ONE step (LOW to MEDIUM or MEDIUM to HIGH), never two. If the
threat model is empty, skip this step.

STEP 4: Judge the scanner's claimed severity. From the perspective of an
engineer who has reviewed two hundred scanner findings this week and is
allergic to inflation: would the CLAIMED severity contribute to alert
fatigue? Is it comparable to a real CVE at that level? Is the code in test
fixtures or dev-only config? Score in -5..+5:
  +3..+5  claimed severity is justified or understated
   0..+2  roughly right
  -1..-3  inflated by one level
  -4..-5  badly inflated (LOW dressed as HIGH)

STEP 5: verify_verdict. Exactly one of:
  exploitable        preconditions are realistically satisfiable
  mitigated          real, but a deployed control reduces it below the
                     derived severity (name the control)
  needs_manual_test  severity hinges on something only a runtime test can
                     settle; recommend a human build a PoC

STEP 6: If SCORING STANDARD is a CVSS or OWASP variant, emit a
`severity_label` in that format (vector string + base score for CVSS;
likelihood x impact for OWASP). Otherwise set it equal to the derived
HIGH/MEDIUM/LOW.

────────────────────────────────────────────────────────────────────────
Respond with ONLY this block:

  PRECONDITIONS:
  - <one per line>
  ACCESS_LEVEL: <unauthenticated_remote|authenticated|local|physical>
  SEVERITY: <HIGH|MEDIUM|LOW>
  SEVERITY_LABEL: <per scoring standard>
  THREAT_MATCH: <matched threat-model entry, or none>
  SEVERITY_ALIGNMENT: <-5..+5>
  VERIFY_VERDICT: <exploitable|mitigated|needs_manual_test>
  RANK_RATIONALE: <2-4 sentences>
```

