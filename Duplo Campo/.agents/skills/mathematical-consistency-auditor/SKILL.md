---
name: mathematical-consistency-auditor
description: Audit mathematical consistency in TDCP text, equations, and derivations. Use when checking signs, dimensions, symbols, assumptions, limits, contradictions, proportionalities, derivation steps, and whether mathematical conclusions are justified.
---

# Mathematical Consistency Auditor

## When to Use This Skill

Use this skill before accepting equations, derivations, parameter restrictions, limits, or statements introduced with "therefore", "implies", "follows", or equivalent mathematical language.

## What the Skill Must Check

- Signs and factors in equations and definitions.
- Dimensional consistency of all terms.
- Undefined symbols and repeated symbols with conflicting meanings.
- Missing assumptions, branch choices, gauges, or approximation regimes.
- Invalid limits or singular limits.
- Equations that contradict earlier equations or stated definitions.
- Whether conclusions follow from the displayed equations.
- Whether proportionalities are being treated as equalities.
- Whether the same symbol denotes a function, constant, perturbation, or background quantity in different places.

## What the Skill Must Not Do

- Do not fix a derivation by inventing unstated assumptions.
- Do not approve an equation because it is plausible by analogy.
- Do not conflate dimensional consistency with correctness.
- Do not simplify away terms unless the approximation is explicitly stated.
- Do not treat notation changes as harmless when they alter meaning.

## Required Output Format

Return:

1. **Math Verdict:** Consistent / Needs assumptions / Inconsistent.
2. **Equation-by-Equation Audit:** Focus on only the equations under review.
3. **Symbol Table Issues:** Undefined or overloaded symbols.
4. **Dimensional and Limit Checks:** Include failures and required assumptions.
5. **Derivation Gaps:** State what must be proven or added.

## Common Failure Modes

- Missing lapse, scale factor, or branch dependence in cosmological equations.
- Switching between cosmic time, conformal time, and relational time without conversion.
- Treating beta_n, beta_n(phi), and F(phi) beta_n as interchangeable without stating the model.
- Using a late-time limit inside a primordial argument.
- Claiming stability from positive energy alone.

## Checklist

- All symbols defined?
- Dimensions match?
- Signs checked?
- Assumptions stated?
- Limits valid?
- Branch/gauge specified?
- Conclusions logically follow?
