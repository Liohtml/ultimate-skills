---
name: variant-analysis
description: >-
  Finds the other instances of a bug you already found — the variants of one
  root cause across a codebase. Five steps: extract the root cause, write an
  exact-match pattern that must hit the known instance, generalize one element
  at a time (stop when more than half the matches are noise), triage survivors
  with a severity, and write up including the patterns that failed and a CI
  regression rule. Ships CodeQL and Semgrep starter queries for C/C++, Go, Java,
  JavaScript and Python. Use right after a vulnerability or bad pattern turns up
  in a specific file and the question becomes "are there others like this?", or
  to turn one known instance into a query for its whole pattern family. Not for
  initial discovery with no bug in hand — for that use static-vuln-scan; to
  weed out false positives from a scan use vuln-triage (both in the MIT security
  plugin).
---

# Variant Analysis

> Adapted from [trailofbits/skills](https://github.com/trailofbits/skills/tree/32e34f8173796e3566a51aee877dc96bc5191f64/plugins/variant-analysis) (CC-BY-SA-4.0). Modified by ultimate-skills; this whole plugin is licensed CC-BY-SA-4.0. See the change note at the end.

Find the other instances of a bug you have already found. One root cause usually has several
manifestations, and they are rarely in the module where you found the first one.

## When to Use

- A vulnerability has been found and you need to search for similar instances
- Building or refining CodeQL/Semgrep queries for security patterns
- Performing systematic code audits after an initial issue discovery
- Analyzing how a single root cause manifests in different code paths

## When NOT to Use

- Initial vulnerability discovery with no bug in hand — use `static-vuln-scan`
- General code review with no known pattern to search for — use `code-review-and-quality`
- Weeding out false positives from a scan — use `vuln-triage`

## The Five Steps

Read the reference for a step when you reach it.

**1. Understand the original issue.** Extract the root cause — why the code is wrong, not
what it does — and enumerate the directions a variant could hide in: related identifiers,
other manifestations of the same mistake, data-type edge cases.
→ [references/root-cause.md](references/root-cause.md)

**2. Create an exact match.** Write a pattern matching ONLY the known instance and confirm
it hits. A pattern that matches nothing means you have misunderstood the bug, and every
search built on it is calibrated against the wrong code.

**3–4. Generalize one element at a time.** Climb from the exact match toward the pattern
family, running and reading all matches after each single change. Stop when more than half
the matches are noise.
→ [references/searching.md](references/searching.md) — abstraction ladder, tool selection,
false-positive filters

**5. Triage.** Decide which candidates are real, and say so with a severity attached.
→ [references/triage.md](references/triage.md)

**Then write it up**, including the patterns that failed and a CI rule to prevent regression.
→ [references/reporting.md](references/reporting.md)

## Running it across subagents

When the codebase is large or the root cause has many manifestations, fan the five steps
out across parallel subagents — one per expansion axis — looping until the sweep stops
finding anything new. Each subagent reads the reference above that matches its job. Work
the steps directly when the search is narrow or you want a say in each generalization.

(Upstream ships this as a `/variant-analysis:variants` workflow command; it is not bundled
here — the five steps above are self-contained.)

## What Makes Hunts Fail

1. **Narrow scope** — searching only the module the original bug was in
2. **Pattern too specific** — searching one attribute and missing the family around it
3. **One vulnerability class** — chasing a single manifestation of the root cause
4. **Happy-path testing** — never trying the null, empty, and boundary cases
5. **Generalizing too fast** — abstracting several elements at once, so noise cannot be
   attributed to any one of them

The first three are covered in root-cause.md and searching.md, the fourth in triage.md.

## Resources

**CodeQL** (`resources/codeql/`): `python.ql`, `javascript.ql`, `java.ql`, `go.ql`, `cpp.ql`

**Semgrep** (`resources/semgrep/`): `python.yaml`, `javascript.yaml`, `java.yaml`, `go.yaml`, `cpp.yaml`

**Report**: `resources/variant-report-template.md`

## Change note

Modified from upstream commit `32e34f8`: description rewritten with cross-pointers into this marketplace; "When NOT to Use" and the workflow section rewritten to drop references to upstream skills not imported here (`audit-context-building`, `issue-writer`) and the `/variant-analysis:variants` workflow command; the `agents/openai.yaml`, brand asset, tests and evals removed. The five-step method and the CodeQL/Semgrep starter queries under `resources/` are unchanged.
