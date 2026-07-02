---
name: tdcp-f1-parameter-guardian
description: Protect the TDCP-F1 parameter family (beta_0, beta_1, beta_2, 0, beta_4). Use when reviewing F1 equations, algebraic branch claims, r_star, beta_1 beta_2 sign constraints, positive U(r_star), late-time effective dark energy, beta_4 sector-f consistency, and scalar/tensor sector dependence.
---

# TDCP F1 Parameter Guardian

## When to Use This Skill

Use this skill whenever a TDCP draft, equation, numerical setup, or claim invokes the F1 family, especially claims about late-time acceleration, GR recovery, algebraic branches, scalar mass, tensor mass, or parameter tuning.

## What the Skill Must Check

- The F1 family is (beta_0, beta_1, beta_2, 0, beta_4).
- beta_3 = 0 unless the text explicitly changes model family.
- r_star = - beta_1/(2 beta_2) when using the algebraic branch tied to beta_1 + 2 beta_2 r = 0.
- beta_1 beta_2 < 0 is required for positive r_star.
- U(r_star) > 0 is required for positive late-time effective dark energy when F(phi) > 0.
- beta_4 is treated as a sector-f consistency parameter, not a free observational decoration.
- Scalar and tensor dependence on beta_1 + 2 beta_2 r is preserved.
- Claims about F1 do not imply independent tuning of scalar and tensor sectors unless justified.

## What the Skill Must Not Do

- Do not silently reintroduce beta_3.
- Do not treat the algebraic branch as automatic for all backgrounds.
- Do not claim late-time acceleration from F1 without checking U(r_star) and signs.
- Do not separate scalar and tensor tuning if both depend on the same beta combination.
- Do not infer observational viability from parameter counting alone.

## Required Output Format

Return:

1. **F1 Verdict:** Compatible / Needs constraints / Outside F1.
2. **Parameter Audit:** beta_0, beta_1, beta_2, beta_3, beta_4 status.
3. **Branch and Sign Checks:** r_star, beta_1 beta_2, U(r_star), F(phi).
4. **Sector Coupling Check:** Scalar/tensor dependence on beta_1 + 2 beta_2 r.
5. **Required Fixes:** Exact constraints or wording changes.

## Common Failure Modes

- Calling a model F1 while beta_3 is nonzero.
- Using r_star without stating the algebraic branch.
- Forgetting beta_1 beta_2 < 0 for positive r_star.
- Claiming positive dark energy without U(r_star)>0.
- Treating beta_4 as observationally arbitrary.

## Checklist

- beta_3 equals zero?
- r_star formula used only on correct branch?
- beta_1 beta_2 sign checked?
- U(r_star)>0 checked when needed?
- beta_4 role stated?
- Scalar/tensor tuning dependency preserved?
