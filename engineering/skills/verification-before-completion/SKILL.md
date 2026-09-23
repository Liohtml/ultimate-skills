---
name: verification-before-completion
description: Evidence gate before any success claim. Use when you are about to say work is done, fixed, passing, green, or ready; before committing, pushing, opening a PR, marking a task complete, moving to the next task, or reporting a delegated agent's result. Requires identifying the command that proves the claim, running it fresh and in full, reading the output and exit code, and only then stating the claim with its evidence. For finding the cause of a failure use debugging-and-error-recovery; for writing the tests themselves use test-driven-development; for a full pre-merge review use code-review-and-quality.
license: MIT
---

# Verification Before Completion

> Adapted from [obra/superpowers `verification-before-completion`](https://github.com/obra/superpowers/tree/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/verification-before-completion) (MIT, Copyright (c) 2025 Jesse Vincent). Tone and wording condensed for this marketplace.

## Overview

**Core principle:** evidence before claims, always. A success claim without fresh verification output is an unverified guess, whatever words it is phrased in.

## The Rule

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you have not run the verification command since your last change, you cannot claim it passes.

## The Gate

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: Which command proves this claim?
2. RUN:      Execute the FULL command, fresh and complete
3. READ:     Full output, exit code, count of failures/errors/warnings
4. VERIFY:   Does the output confirm the claim?
             - NO  -> state the actual status, with the evidence
             - YES -> state the claim, with the evidence
5. ONLY THEN make the claim
```

Skipping a step turns a report into a guess. Say so plainly if you could not run something ("not verified: no DB in this environment") instead of implying success.

## What Each Claim Requires

| Claim | Requires | Not sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | A previous run, "should pass" |
| Linter clean | Linter output: 0 errors | A partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs "look good" |
| Bug fixed | The original symptom's reproduction now passes | Code changed, assumed fixed |
| Regression test works | Red-green-revert cycle verified (below) | Test passes once |
| Agent / subagent completed | VCS diff shows the expected changes | The agent reporting "success" |
| Requirements met | Line-by-line checklist against the spec or plan | Tests passing |
| CI is green | The current CI run for the current head commit | A green run for an older commit |

## Key Patterns

**Tests**
```
OK:  [run test command] [see: 34/34 pass] "All tests pass"
BAD: "Should pass now" / "Looks correct"
```

**Regression tests (red-green-revert)**
```
OK:  write test -> run (pass) -> revert the fix -> run (MUST FAIL) -> restore fix -> run (pass)
BAD: "I've written a regression test" (without seeing it fail without the fix)
```

**Build**
```
OK:  [run build] [see: exit 0] "Build passes"
BAD: "Linter passed" (a linter does not check compilation)
```

**Requirements**
```
OK:  re-read plan -> make checklist -> verify each item -> report gaps or completion
BAD: "Tests pass, phase complete"
```

**Delegated work**
```
OK:  agent reports success -> inspect the VCS diff -> run the checks yourself -> report actual state
BAD: forward the agent's report as fact
```

## Red Flags: Stop and Verify

- Words like "should", "probably", "seems to", "I believe this fixes"
- Expressing satisfaction ("Done!", "Perfect!", "All good") before running anything
- About to commit, push or open a PR without a fresh run
- Trusting a subagent's or tool's success summary
- Relying on a partial check (one test file, one package) for a whole-repo claim
- "Just this once" or "it's a trivial change"

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Should work now" | Run the verification. |
| "I'm confident" | Confidence is not evidence. |
| "Linter passed" | Linter is not the compiler, and neither is the test suite. |
| "The agent said success" | Verify independently: diff plus checks. |
| "Partial check is enough" | A partial check proves only the part it covered; claim only that part. |
| "I phrased it differently, so it isn't a claim" | Any wording that implies success is a claim. |

## When to Apply

**Always before:**
- Any success or completion statement, including paraphrases and implications
- Committing, pushing, PR creation, marking a task complete
- Moving on to the next task in a plan
- Reporting on work you delegated

## See Also

- `test-driven-development`: produces the failing-then-passing tests this gate reads.
- `debugging-and-error-recovery`: its Step 1 feedback loop is the command that proves "bug fixed".
- `incremental-implementation` and `subagent-driven-development`: run this gate at the end of every slice or task.
- `iterate-pr`: applies the same rule to CI and review state on an open PR.
