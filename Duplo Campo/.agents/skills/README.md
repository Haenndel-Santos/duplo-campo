# TDCP Repository Skills

This directory contains project-local Codex Skills for the Teoria do Duplo Campo Primordial (TDCP). They are scoped to this repository and are intended to help Codex review theoretical architecture, mathematical consistency, bimetric formalism, stability, EFT validity, observational tests, and scientific prose.

## Skills

- `tdcp-theory-architecture-guardian`: Protects the global TDCP architecture: two correlated regimes, bifurcation, dynamic vacuum, relational time, g/f metrics, phi, GR recovery, and testability.
- `chapter-continuity-editor`: Checks continuity between chapters, including definition drift, symbol reuse, logical ordering, and unsupported narrative jumps.
- `mathematical-consistency-auditor`: Audits equations, signs, dimensions, symbols, assumptions, limits, and derivation logic.
- `bimetric-hr-formalism-guardian`: Guards correct use of Hassan-Rosen bimetric structure, K=sqrt(g^{-1}f), V(K)=sum beta_n e_n(K), matter coupling, Bianchi constraints, and FLRW variables.
- `tdcp-f1-parameter-guardian`: Protects the F1 family (beta_0, beta_1, beta_2, 0, beta_4), including beta_3=0, r_star, sign conditions, U(r_star), and linked scalar/tensor tuning.
- `stability-constraints-auditor`: Checks no-ghost, no-gradient, no-tachyon, controlled primordial tachyonic behavior, isocurvature, Higuchi, c_T=1, and GR/local recovery.
- `eft-and-screening-validator`: Reviews EFT validity, cutoff hierarchy, Lambda_3, BD ghost avoidance, matter coupling, Vainshtein screening, PPN claims, and fifth-force risks.
- `observational-pipeline-designer`: Converts theory into observables and computational tests: mu(k,a), Sigma(k,a), eta_slip, f sigma_8, P(k,z), BAO, RSD, weak lensing, CLASS/CAMB, and degeneracies.
- `scientific-writing-and-claim-control`: Calibrates scientific prose by separating hypothesis, assumption, derivation, result, prediction, and speculation.

## When to Invoke Explicitly

Invoke a skill explicitly when the automatic trigger may be ambiguous or when a review must be strict:

- Use `tdcp-theory-architecture-guardian` for conceptual or chapter-level changes.
- Use `mathematical-consistency-auditor` for equations and derivations.
- Use `bimetric-hr-formalism-guardian` for any Hassan-Rosen or two-metric material.
- Use `stability-constraints-auditor` before accepting viability claims.
- Use `observational-pipeline-designer` when moving from formalism to predictions.
- Use `scientific-writing-and-claim-control` before treating text as article- or thesis-ready.

## Recommended Workflows

### Writing a New Chapter

1. Start with `tdcp-theory-architecture-guardian`.
2. Use `chapter-continuity-editor` to connect the chapter to previous definitions.
3. Use `scientific-writing-and-claim-control` for final prose calibration.

### Revising a Chapter

1. Use `chapter-continuity-editor` to find definition drift and missing bridges.
2. Use the relevant technical skill for the chapter content.
3. Use `scientific-writing-and-claim-control` to align conclusions with what was established.

### Checking Equations

1. Use `mathematical-consistency-auditor`.
2. Add `bimetric-hr-formalism-guardian` when equations use g, f, K, e_n(K), beta_n, or bimetric FLRW variables.
3. Add `tdcp-f1-parameter-guardian` when the F1 parameter family is involved.
4. Add `stability-constraints-auditor` when equations imply physical viability.

### Preparing Article-Style Text

1. Use `scientific-writing-and-claim-control` to classify claims.
2. Use `tdcp-theory-architecture-guardian` to verify that the article still represents TDCP.
3. Use `mathematical-consistency-auditor` for displayed equations and derived claims.

### Preparing a Computational or Observational Pipeline

1. Use `observational-pipeline-designer` to define observables and implementation targets.
2. Use `stability-constraints-auditor` to restrict benchmarks to viable regions.
3. Use `eft-and-screening-validator` to state the validity range.
4. Use `tdcp-f1-parameter-guardian` if the pipeline is based on the F1 model.

## Example Invocations

- "Use tdcp-theory-architecture-guardian and mathematical-consistency-auditor to review Chapter 13."
- "Use stability-constraints-auditor before accepting this new equation."
- "Use observational-pipeline-designer to turn this section into testable predictions."
- "Use bimetric-hr-formalism-guardian to check whether this action preserves Hassan-Rosen structure."
- "Use scientific-writing-and-claim-control to prepare this conclusion for article-style prose."
