---
name: bimetric-hr-formalism-guardian
description: Protect correct use of Hassan-Rosen ghost-free bimetric formalism in TDCP. Use when reviewing two-metric equations, K=sqrt(g^{-1}f), the HR potential sum beta_n e_n(K), matter coupling, Bianchi constraints, FLRW bimetric variables, or phi modulation of the interaction potential.
---

# Bimetric HR Formalism Guardian

## When to Use This Skill

Use this skill whenever TDCP material uses two metrics, Hassan-Rosen bimetric gravity, the square-root matrix, bimetric FLRW cosmology, or phi-dependent modulation of the interaction potential.

## What the Skill Must Check

- Two dynamical metrics g_{mu nu} and f_{mu nu} are treated consistently.
- K = sqrt(g^{-1} f) is the matrix entering the elementary symmetric polynomials.
- The potential has the HR form V(K) = sum beta_n e_n(K), or an explicitly stated TDCP modulation of it.
- Matter is minimally coupled only to g unless a ghost analysis justifies another coupling.
- No double matter coupling is introduced without a BD ghost discussion.
- Bianchi constraint consistency is maintained.
- FLRW variables a(t), b(t), r=b/a, and xi=N_f/N_g are defined and used consistently.
- beta_n(phi) or F(phi)V modulation does not destroy the HR potential structure.
- The GR limit, massive and massless tensor sectors, and branch choices are not conflated.

## What the Skill Must Not Do

- Do not replace HR structure with a generic bimetric interaction.
- Do not assume ghost freedom survives arbitrary phi-dependent couplings.
- Do not approve matter coupling to both metrics without an explicit constraint analysis.
- Do not ignore lapse or Bianchi equations in FLRW reductions.
- Do not treat g and f as merely symbolic dualities once equations are introduced.

## Required Output Format

Return:

1. **HR Verdict:** HR-preserving / Needs constraints / HR-breaking.
2. **Formalism Checks:** g, f, K, e_n(K), beta_n, matter coupling, Bianchi.
3. **FLRW Checks:** a, b, r, xi, branch, lapse consistency.
4. **Phi-Modulation Risk:** Whether beta_n(phi) or F(phi)V is safe as stated.
5. **Required Corrections:** Minimal formal changes needed.

## Common Failure Modes

- Writing a potential that is not built from e_n(K).
- Letting matter couple to f without analysis.
- Dropping the Bianchi constraint after choosing r=b/a.
- Using beta_n(phi) as if it were automatically ghost-free.
- Mixing algebraic and dynamical branches.

## Checklist

- g and f both defined?
- K=sqrt(g^{-1}f) used?
- Potential in HR e_n form?
- Matter coupling controlled?
- Bianchi constraint present?
- FLRW variables consistent?
- Phi modulation constrained?
