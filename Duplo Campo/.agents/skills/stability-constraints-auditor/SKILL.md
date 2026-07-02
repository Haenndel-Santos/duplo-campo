---
name: stability-constraints-auditor
description: Audit TDCP physical stability constraints. Use when reviewing no-ghost, no-gradient, no-tachyon, controlled primordial tachyonic bifurcation, scalar isocurvature suppression, the Higuchi bound, c_T=1, late-time scalar-mass hierarchy, and GR or local consistency claims.
---

# Stability Constraints Auditor

## When to Use This Skill

Use this skill before accepting stability claims, perturbation equations, tensor-sector statements, scalar-sector statements, or any argument that says a TDCP background is physically viable.

## What the Skill Must Check

- No-ghost condition for the relevant scalar, vector, or tensor modes.
- No-gradient condition and correct sign of sound-speed squared.
- No-tachyon condition in the late-time regime.
- Primordial tachyonic behavior is allowed only when explicitly controlled and described as a bifurcation mechanism.
- Scalar isocurvature modes are suppressed or shown to be observationally acceptable.
- Higuchi condition m_T^2 >= 2H^2 in quasi-de Sitter regimes.
- c_T = 1 for the massless tensor mode when comparing with gravitational-wave constraints.
- m_S^2 >> H^2 after the primordial or bifurcation phase when suppressing isocurvature.
- Recovery of GR and local consistency are not assumed from background expansion alone.

## What the Skill Must Not Do

- Do not infer stability from a positive background energy density.
- Do not treat the Higuchi condition as optional in quasi-de Sitter.
- Do not use a primordial instability as a late-time feature unless explicitly justified.
- Do not ignore isocurvature modes when phi is dynamical.
- Do not claim GR recovery without checking perturbative and local behavior.

## Required Output Format

Return:

1. **Stability Verdict:** Stable as stated / Conditionally stable / Unstable or unproven.
2. **Mode Audit:** Scalar, vector, tensor, and isocurvature status as applicable.
3. **Bound Checks:** Higuchi, c_T, m_S/H, tachyon, gradient, ghost.
4. **Regime Separation:** Primordial, bifurcation, late-time, and local regimes.
5. **Required Evidence:** Missing derivations, inequalities, or numerical checks.

## Common Failure Modes

- Applying a late-time stability inequality to the primordial phase.
- Forgetting that controlled tachyonic bifurcation must end.
- Treating c_T=1 as automatic for all tensor modes.
- Ignoring the massive tensor Higuchi bound.
- Suppressing isocurvature by assertion rather than by mass or coupling hierarchy.

## Checklist

- No ghost?
- No gradient instability?
- No late-time tachyon?
- Primordial instability controlled?
- Higuchi satisfied?
- c_T=1 stated for massless tensor?
- Isocurvature controlled?
- GR/local recovery addressed?
