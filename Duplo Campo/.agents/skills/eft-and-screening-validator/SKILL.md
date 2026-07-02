---
name: eft-and-screening-validator
description: Validate TDCP EFT and nonlinear screening consistency. Use when reviewing EFT-regime claims, cutoff hierarchy, Lambda_3 ~ (m^2 M_eff)^(1/3), F(phi) modifications, BD ghost avoidance, matter coupling, Vainshtein screening, r_V estimates, PPN claims, or fifth-force risks.
---

# EFT and Screening Validator

## When to Use This Skill

Use this skill when TDCP material discusses validity range, UV completeness, strong coupling, nonlinear screening, local tests, PPN constraints, fifth forces, or Boulware-Deser ghost avoidance.

## What the Skill Must Check

- TDCP is treated as an EFT unless the text explicitly and defensibly claims UV completeness.
- The hierarchy H << Lambda_TDCP is stated where EFT validity matters.
- Lambda_3 ~ (m^2 M_eff)^(1/3) is used as the bimetric strong-coupling scale, modified by F(phi) only when the modification is derived or stated.
- HR potential structure is preserved as the BD ghost avoidance mechanism.
- Matter coupling does not reintroduce the BD ghost.
- Vainshtein screening is used in the correct nonlinear regime.
- r_V ~ (GM/(m^2 F_0))^(1/3), up to order-one coefficients, is used carefully.
- PPN statements are not overclaimed without gamma and beta estimates or a clear screening argument.
- phi does not introduce an unscreened fifth force unless explicitly modeled and constrained.

## What the Skill Must Not Do

- Do not claim UV completion from EFT consistency.
- Do not treat Vainshtein screening as a universal fix for every instability.
- Do not accept arbitrary matter coupling as ghost-free.
- Do not make Solar System claims without PPN or screening estimates.
- Do not ignore F(phi) when it changes masses, couplings, or cutoff estimates.

## Required Output Format

Return:

1. **EFT Verdict:** Valid in stated regime / Needs cutoff or screening analysis / Overclaimed.
2. **Cutoff Audit:** H, Lambda_TDCP, Lambda_3, F(phi) dependencies.
3. **Ghost and Coupling Audit:** HR structure, matter coupling, BD risk.
4. **Screening and Local Tests:** Vainshtein radius, PPN, fifth-force status.
5. **Required Corrections:** Minimal constraints or wording changes.

## Common Failure Modes

- Presenting TDCP as fundamental without evidence.
- Using linear perturbation equations inside the Vainshtein region.
- Ignoring phi-mediated fifth forces.
- Treating r_V estimates as exact predictions.
- Claiming PPN safety from cosmological viability alone.

## Checklist

- EFT status explicit?
- H << Lambda_TDCP checked?
- Lambda_3 scale discussed?
- HR structure preserved?
- Matter coupling safe?
- Vainshtein regime correct?
- PPN claims calibrated?
- Fifth-force risk addressed?
