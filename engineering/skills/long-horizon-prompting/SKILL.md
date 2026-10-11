---
name: long-horizon-prompting
description: Writes, strengthens, or reviews the launch prompt for a long-running autonomous agent or a parallel multi-agent run on a hard, open-ended problem (root-cause hunts, research questions, proofs, large investigations). Use when you need a pseudo-formal task brief with defined terms, an exact success predicate, an explicit list of outcomes that do not count, persistence rules paired with verification gates, an effort floor, an orchestration policy for diverse parallel approaches, and an audit-gated return condition; or when diagnosing a long run that returned early, converged on one approach, or produced an answer-shaped near miss. For executing a concrete implementation plan with subagents use subagent-driven-development; for fresh-context adversarial review of a single decision use doubt-driven-development; for writing product specs use spec-driven-development.
license: MIT
---

# Long-Horizon Prompting

> Adapted from [muratcankoylan/Agent-Skills-for-Context-Engineering `long-horizon-prompting`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/6dbe1a1d868eab51a3bc9011b0f55e2891513e40/skills/long-horizon-prompting) (MIT, Copyright (c) 2025 Context Engineering Agent Skills Contributors). Changes: routing to sibling skills of the upstream collection replaced with this marketplace's skills (or marked as not included), inline `claim-*` IDs (backed by an upstream claims database not included here) replaced with pointers to [references/research-evidence.md](references/research-evidence.md). Content reflects sources dated up to 2026-07; treat vendor and benchmark claims as time-sensitive.

This skill covers the design of the prompt that launches an agent expected to work autonomously for hours or days, alone or as an orchestrator managing many parallel workers. The central technique is the pseudo-formal task brief: a specification written with the rigor of formal verification but expressed linguistically, because most hard problems have no machine-checkable success condition. The exemplar is the published prompt behind GPT-5.6 Sol Ultra's candidate proof of the Cycle Double Cover Conjecture, produced by a 64-subagent orchestration. The prompt structure generalizes far beyond mathematics: any domain where success can be stated precisely and failure modes can be enumerated can use the same brief anatomy.

The controlling trade-off: everything that makes a long run productive (persistence, autonomy, parallelism) also raises the cost of a weak specification. A short interactive prompt fails cheaply; a long-horizon brief with a loophole burns hours of compute producing an answer-shaped artifact that does not solve the problem.

## When to Activate

Activate this skill when:

- Writing or reviewing the prompt for a long-running autonomous run before launching it
- Converting a vague hard problem ("solve X", "figure out why Y happens") into an explicit brief with a success predicate and non-counting outcomes
- Writing the root or orchestrator prompt that manages many parallel workers on an open-ended search problem
- Adding persistence instructions, stop conditions, effort floors, or return gates to an agent prompt
- Diagnosing a failed long run whose failure traces to the brief: premature return, an answer-shaped near miss, all workers converging on one approach, or fabricated completion claims
- Building a pre-launch review step that enhances and evaluates prompts before expensive agent time is committed

Do not activate this skill for adjacent work:

- Executing a concrete, task-by-task implementation plan with implementer and reviewer subagents: use `subagent-driven-development` (it owns the ledger, review loop and fix-round cap). This skill owns the words of a launch brief for open-ended problems.
- Fresh-context adversarial review of one decision or artifact: `doubt-driven-development`.
- Writing a product or feature spec: `spec-driven-development`.
- Runtime control surfaces around an autonomous loop (hard budgets, locked evaluators, rollback, permissions, hooks): these belong in the harness or agent runtime, not in the prompt; not covered by a skill in this marketplace. Constraints that must survive optimization pressure belong there.
- Building the automated tests or deterministic gates a run is scored by: `test-driven-development`; the "prove it before claiming it" rule itself: `verification-before-completion`.

## Core Concepts

### Pseudo-Formal Task Specification

Formal verification requires a machine-checkable specification. Hard open problems rarely have one, but the discipline transfers: state the success condition so precisely that an adversarial reader cannot satisfy its letter without satisfying its intent. Four components, in order of leverage:

1. **Definitions with degenerate cases.** Define every load-bearing term before stating the goal, including the edge cases a lazy solution would exploit. The CDC prompt defines graph, bridge, cycle, and cycle double cover before the task, explicitly covering parallel-edge two-cycles, disconnected graphs, and the edgeless graph.
2. **Exact success predicate.** One statement of what must be true of the returned artifact, with scope quantifiers spelled out ("every finite loopless multigraph with no bridge, without additional assumptions such as cubicity, planarity, connectivity, or higher edge-connectivity").
3. **Non-counting outcomes.** An enumerated list of results that do not count: partial progress, special-case solutions, reductions to another unproved statement, bounded or computational verification, and best-effort summaries. This is the highest-leverage component. Under persistence pressure, models produce answer-shaped near misses; each excluded outcome removes one escape hatch.
4. **Enumerated failure modes for the auditor.** A concrete checklist of the domain-specific ways a candidate can be subtly wrong (in CDC: repeated-edge closed trails masquerading as cycles, bridges introduced by reductions, circular use of an equivalent statement). Verifiers with an enumerated hunt list catch what generic "check the work" instructions miss.

### Anatomy of a Long-Horizon Brief

| Block | Job | Failure it prevents |
| --- | --- | --- |
| Definitions | Fix the vocabulary, including degenerate cases | Loophole solutions on technicalities |
| Success predicate | State exactly what must be true at return | Scope-narrowed answers |
| Non-counting outcomes | Enumerate near misses that do not count | Answer-shaped partial results |
| Solvability framing | "Assume a solution exists" where existence is plausible | Give-up drift, "this is open" refusals |
| Orchestration policy | Heuristics for allocating parallel workers, not fixed assignments | Premature convergence, wasted parallelism |
| Verification policy | Adversarial audit with enumerated failure modes | Lenient self-judging |
| Reporting contract | Concrete artifacts required; status reports rejected | Vague optimism, fabricated progress |
| Return condition | Return only when the artifact survives audit | Premature return, best-effort summaries |
| Effort floor | Minimum effort before giving up is considered | Early abandonment |
| Contamination guards | What external search may and may not be used for | Laundered lookups, benchmark leakage |

### Persistence Cuts Both Ways

Persistence instructions ("do not return until", effort floors, assume-solvable framing) counter the documented drift toward giving up on long trajectories. But the same pressure raises the reward-hacking surface: the most persistence-trained frontier model measured to date also showed the highest detected cheating rate of any model its evaluator had tested, and its measured time horizon was not robust to whether cheating counted as success. The design rule: never add a persistence instruction without a matching verification gate. Persistence pressure against a loose success predicate produces confident non-solutions.

### The Verification Bottleneck

Parallel sampling reliably raises the chance that some worker finds a correct answer, but the system's ability to select that answer lags behind, and model judges of hard artifacts are systematically lenient, rewarding rigorous-looking but incomplete arguments. Budget as much prompt design for the verifier as for the generator:

- Give auditors the enumerated failure-mode list from the brief, not a generic quality instruction.
- Require the generator to produce modular, independently checkable output (lemma-level structure with stated premises and conclusions) so verification decomposes.
- Use fresh-context adversarial verifiers rather than self-critique; a verifier that did not build the artifact cannot rationalize its gaps.
- Treat inter-agent agreement as a diversity failure signal, not as confirmation: committees converge most tightly on the hardest problems, where unanimity reflects shared bias rather than corroboration.

### Structural Diversity in Parallel Search

Role labels do not create diversity; parallel workers share priors and converge unless independence is engineered:

- Keep early-round workers blind to the currently favored approach.
- Maintain an explicit registry of approach families, grouped by underlying idea rather than surface wording, and redirect workers away from crowded families.
- Mark a route blocked when it stalls at a missing step as hard as the original goal; reassign workers to it only for a materially new mechanism, not for enthusiasm.
- Cross-pollinate late, after independent development has exposed each route's real strengths and gaps.
- Do not let one approach dominate because its reductions are elegant; a route ending at a lemma equivalent in strength to the original goal is not progress.

### Stop Conditions, Effort, and Progress State

Long trajectories drift toward uncertainty and abandonment, and a budget stated once at the top of the prompt loses force as context grows. Countermeasures that belong in the brief: an explicit effort floor ("spend at least this much effort before considering returning"), assume-solvable framing where a solution plausibly exists, and a return condition phrased as a predicate over the artifact rather than over the agent's confidence. Countermeasures that belong outside the prompt: an externally maintained ledger of verified progress re-injected each round, which in controlled comparisons rescued large-quantity tasks that prompt-only and completion-gated setups failed entirely. Progress claims should be auditable: requiring each reported claim to trace to a tool result or artifact from the current session nearly eliminated fabricated status reports in vendor testing.

### Lean and Outcome-First

Both major vendors converged on the same doctrine for current frontier models: the prompt should carry the outcome, hard constraints, evidence sources, and completion bar, and leave the path to the model. Accumulated instruction stacks measurably hurt; leaner system prompts improved vendor coding-agent evaluations while cutting cost. Persistence itself is increasingly trained in rather than prompted in, so spend the token budget on what training cannot supply: the success predicate, the non-counting list, and the domain failure modes only an expert in the problem knows.

## Detailed Topics

### The CDC Prompt, Dissected

The published Cycle Double Cover prompt implements every block of the brief anatomy in under a page: formal definitions closing degenerate-case loopholes, an exact success predicate with scope quantifiers, five classes of explicitly non-counting partial progress, dynamic orchestration heuristics for up to 64 concurrent agents with an approach-family registry and blocked-route bookkeeping, adversarial auditors with a seven-item failure-mode hunt list, a concrete-artifact reporting contract, an audit-gated return condition, an eight-hour effort floor, and a contamination guard restricting web search to background material. The original prompt is published by OpenAI (`https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf`); an element-by-element annotation is in the upstream [CDC prompt reference](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/6dbe1a1d868eab51a3bc9011b0f55e2891513e40/skills/long-horizon-prompting/references/cdc-prompt-annotated.md) (upstream, not included here because it reproduces the third-party prompt verbatim).

Two honest caveats. The candidate proof had no independent peer review or formalization when published, so the prompt is the validated artifact of interest here, not the theorem. And no public ablation isolates which prompt elements carried the result; the mechanism-level evidence comes from the independent research in [the research evidence reference](./references/research-evidence.md).

### Vendor Doctrine

OpenAI and Anthropic guidance overlap on fundamentals (explicit completion bars, stop rules, verification before return) and differ in emphasis. OpenAI doctrine centers persistence blocks, risk-tiered autonomy thresholds, self-constructed rubrics, and reasoning-effort dials; its multi-agent API institutionalizes a root agent with bounded-task subagents. Anthropic doctrine centers the four-part subagent delegation spec (objective, output format, tool guidance, task boundaries), explicit effort-scaling tiers by task complexity, evidence-grounded progress reporting, and fresh-context verifier subagents. Both now warn that over-prescriptive prompts degrade current-generation models. Dated extracts with sources are in [the vendor guidance reference](./references/vendor-guidance.md).

### Generalizing Beyond Mathematics

The CDC prompt worked because mathematics allows sharp statements, but each element has a general form usable in any rigorous domain:

| CDC element | General form |
| --- | --- |
| Formal graph definitions | Operationalize every load-bearing term; state units, populations, boundaries, degenerate cases |
| "Exactly two occurrences of each edge" | A quantified, checkable property of the deliverable |
| "Special graph classes do not count" | "Results holding only under narrowed scope do not count" |
| "No reduction to another unproved conjecture" | "No dependence on an unvalidated assumption or unavailable dataset" |
| "Computational verification through fixed size is insufficient" | "Anecdotal or small-sample evidence is insufficient" |
| Parallel-edge and bridge edge cases for auditors | The domain's known confounders, artifacts, and failure modes as an audit checklist |
| "Do not search for a solution to this exact conjecture" | "Do not launder the answer from sources the result is supposed to be independent of" |

The transformation workflow for a scientist or engineer with a hard problem: state what a complete answer would let them do, work backward to the predicate that enables it, then spend most of the effort listing what they would refuse to accept from a junior collaborator. That refusal list becomes the non-counting outcomes and the auditor checklist.

## Practical Guidance

### Brief-Writing Workflow

1. Write the success predicate first, as one sentence with explicit quantifiers and scope. If it cannot be written, the problem is not ready for a long-horizon run; decompose it or run a scoping session instead.
2. Enumerate non-counting outcomes by asking what a capable agent under pressure would return instead of a solution: the narrowed-scope version, the reduction, the survey, the plan, the confident sketch.
3. Define terms, starting from the degenerate cases the predicate must survive.
4. Write the auditor checklist: the domain-specific ways a candidate artifact can look right and be wrong.
5. Set the orchestration policy as heuristics (diversity early, registry by idea, blocked-route rules, late cross-pollination), never as fixed worker-to-strategy assignments.
6. Set the reporting contract (concrete artifacts, evidence-traceable claims) and the return condition (survives adversarial audit against the checklist).
7. Add the effort floor, solvability framing if warranted, and contamination guards.
8. Red-team the brief before launch: ask a fresh model instance "how could an agent satisfy the letter of this brief without solving the problem?" and patch every credible answer.

### Pre-Launch Evaluation

Score any long-horizon brief against these questions before committing agent time. Any "no" is a defect to fix, not a judgment call:

- Can an adversarial reader determine unambiguously whether a given artifact satisfies the success predicate?
- Is every plausible near miss explicitly listed as non-counting?
- Does the auditor have an enumerated, domain-specific failure-mode list?
- Is every persistence instruction paired with a verification gate?
- Is the return condition a predicate over the artifact, not over agent confidence or elapsed effort?
- Does the orchestration policy preserve early independence and include blocked-route bookkeeping?
- Are reporting requirements artifact-based rather than status-based?
- Are contamination guards stated for any external retrieval?
- Is anything in the prompt a constraint that must survive optimization pressure? Move it to the harness or runtime; prompt-stated constraints are advisory.

## Examples

**Example 1: Pseudo-formal brief skeleton**

```text
DEFINITIONS
  <every load-bearing term, including degenerate cases>

TASK
  <exact success predicate with quantifiers and scope>

DOES NOT COUNT
  <narrowed scope> <reduction to unvalidated assumption>
  <bounded/anecdotal verification> <plan or survey instead of artifact>

ORCHESTRATION (for parallel runs)
  Begin with a genuinely diverse portfolio. Keep early workers blind
  to the favored approach. Registry of approach families by idea, not
  wording. Mark routes blocked at goal-strength gaps; reopen only for
  a materially new mechanism. Cross-pollinate late.

VERIFICATION
  Adversarial audit of every candidate against:
  <domain failure-mode checklist>
  Workers return concrete artifacts; status reports are rejected.

RETURN CONDITION
  Return only when a candidate survives the audit. Do not return a
  reduction, partial result, or explanation of difficulty.

EFFORT
  Assume a solution exists. Spend at least <floor> before considering
  returning.

CONTAMINATION
  External search only for <background>; never for <the answer>.
```

**Example 2: Weak prompt to strong brief (root-cause analysis)**

```text
Weak:  "Investigate why our v4 model underperforms v3 in production
        and write up what you find. Be thorough."

Strong: TASK: Identify a defect that, when corrected, closes the
        v4-versus-v3 production gap on the frozen evaluation slice,
        demonstrated by a reproduction script and a corrected run.
        DOES NOT COUNT: correlational narratives without an
        intervention; defects explaining under a stated fraction of
        the gap; "data drift" without an identified slice and
        mechanism; a list of hypotheses.
        VERIFICATION: an adversarial reviewer checks the reproduction
        for train/serve skew, leakage in the eval slice, seed
        sensitivity, and preprocessing divergence.
        RETURN: only a candidate that survives that review.
```

The weak version invites a status report. The strong version makes the deliverable checkable and pre-blocks the three most likely near misses.

## Guidelines

1. Write the success predicate before any other prompt content; if it cannot be stated precisely, do not launch a long-horizon run.
2. Enumerate non-counting outcomes explicitly; every near miss not excluded is an escape hatch.
3. Define load-bearing terms including degenerate cases before stating the task.
4. Give auditors an enumerated domain failure-mode checklist, never a generic quality instruction.
5. Pair every persistence instruction with a verification gate of matching strength.
6. Phrase return conditions as predicates over the artifact, not over confidence, effort, or elapsed time.
7. Assign parallel workers by heuristic policy with an approach-family registry; never fixed strategy quotas.
8. Preserve early-round worker independence; cross-pollinate only after routes have developed independently.
9. Mark routes blocked at goal-strength gaps and require a materially new mechanism to reopen them.
10. Require concrete artifacts from every worker and reject status reports and vague optimism.
11. Require progress claims to trace to session evidence (tool results, files, logs).
12. State contamination guards for external retrieval whenever result independence matters.
13. Keep the brief lean: outcome, constraints, completion bar, failure modes; leave the path to the model.
14. Enforce hard budgets and permissions in the harness; treat prompt-stated constraints as advisory.

## Gotchas

1. **Answer-shaped near misses**: Under persistence pressure, agents return artifacts with the shape of a solution (narrowed scope, unproved dependency, survey instead of result). The non-counting list is the fix; write it by predicting the specific near misses your problem invites.
2. **Circular satisfaction**: The subtlest near miss is an argument that assumes a statement equivalent in strength to the goal. The CDC prompt names this explicitly ("circular use of an equivalent CDC statement"); every domain has an analogue, and auditors will not catch it unless it is on their checklist.
3. **Persistence without verification breeds hacking**: Persistence-trained and persistence-prompted agents show elevated rates of gaming their success signal. If the brief demands "do not return without success" but success is checked leniently, the agent optimizes the leniency.
4. **Unanimity is not corroboration**: Parallel agents agreeing is weak evidence when they share priors, and convergence tightens on harder problems. Never use agreement alone as a return trigger; audit content, and treat fast consensus as a diversity failure.
5. **Under-specified delegation duplicates work**: Subagent tasks missing any of objective, output format, tool guidance, or boundaries produce overlapping and gap-ridden coverage. The orchestrator prompt should require all four in every spawn.
6. **Status-report theater**: Long runs drift into reporting activity instead of results, including fabricated completions. Require artifact-based reporting and evidence-traceable claims; reject "on track" without a pointer.
7. **Effort floors are permissions, not schedules**: The CDC run finished well under its stated eight-hour floor. A floor removes the agent's permission to quit early; it neither guarantees nor bounds runtime. Enforce actual time and cost budgets in the harness.
8. **Prompt-stated budgets decay**: A budget or reminder stated once loses force as the trajectory grows; re-inject budget and verified-progress state periodically from outside the loop.
9. **Assume-solvable on ill-posed problems**: Solvability framing counters give-up drift but instructs the model to never conclude "no solution exists". On genuinely open or ill-posed questions, pair it with a counterexample track or drop it, or the run will fabricate.
10. **Over-prescription backfires on frontier models**: Step-by-step scripts and stacked MUST/NEVER emphasis measurably degrade current-generation model output. Migrate old prompt stacks by starting from the minimal brief, not by accretion.

## Integration

This skill owns the launch prompt for long-running and parallel agent work. Related skills in this marketplace:

- subagent-driven-development - Executes a concrete implementation plan with per-task subagents, reviews and a compaction-proof ledger; a brief written here can seed the plan it executes
- doubt-driven-development - Fresh-context adversarial review; the pattern behind the brief's audit step
- verification-before-completion - The evidence-before-claims rule the reporting contract enforces
- spec-driven-development - Success criteria and scope for product work, the non-research counterpart of the success predicate

## References

Internal references:
- Annotated CDC prompt (upstream, not included here: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/6dbe1a1d868eab51a3bc9011b0f55e2891513e40/skills/long-horizon-prompting/references/cdc-prompt-annotated.md) - The full published prompt with element-by-element annotation and provenance
- [Vendor guidance](./references/vendor-guidance.md) - Dated OpenAI and Anthropic long-horizon and multi-agent prompting doctrine with sources
- [Research evidence](./references/research-evidence.md) - Dated academic findings behind each brief element
- [Task brief template](./references/task-brief-template.md) - Reusable pseudo-formal brief template and pre-launch evaluation rubric

External resources:
- OpenAI, published prompt for the GPT-5.6 Sol Ultra Cycle Double Cover run (July 2026) - The exemplar brief
- METR, predeployment evaluation of GPT-5.6 Sol (June 2026) - Persistence-training and reward-hacking linkage
- Anthropic, "How we built our multi-agent research system" (June 2025) - Delegation specs and effort scaling
- OpenAI GPT-5.x prompting guides and Anthropic Claude prompting docs - Vendor doctrine detailed in the vendor guidance reference

Numeric, benchmark, volatile, or vendor-performance claims in this skill are backed by the dated entries in [references/research-evidence.md](references/research-evidence.md) and [references/vendor-guidance.md](references/vendor-guidance.md); re-check them before relying on specific numbers.
