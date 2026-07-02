---
name: scientific-writing-and-claim-control
description: Improve TDCP scientific writing and prevent overclaiming. Use when revising theoretical physics text for academic rigor, separating hypothesis, assumption, derivation, result, prediction, and speculation, calibrating terms like proved or suggests, and preparing article, thesis, or technical appendix prose.
---

# Scientific Writing and Claim Control

## When to Use This Skill

Use this skill when rewriting TDCP prose, abstracts, introductions, conclusions, chapter summaries, article-style sections, or technical appendices where claim strength and scientific tone matter.

## What the Skill Must Check

- Separate hypothesis, assumption, derivation, result, prediction, and speculation.
- Mark unsupported or under-supported claims.
- Avoid "proved" unless a mathematical proof is actually present.
- Prefer calibrated phrases such as "the model suggests", "under these assumptions", "within the EFT regime", or "this motivates".
- Preserve the hybrid style: conceptual clarity plus technical rigor.
- Make claims conditional on branch choice, parameter regime, approximation, or observational pipeline when needed.
- Keep conclusions aligned with what the section actually established.
- Prepare text for future article, thesis, or technical appendix use.

## What the Skill Must Not Do

- Do not erase the conceptual motivation of TDCP.
- Do not make speculative text sound established.
- Do not add unsupported citations or claims of agreement with data.
- Do not turn a heuristic into a theorem.
- Do not weaken precise mathematical statements that are actually derived.

## Required Output Format

Return:

1. **Claim-Control Verdict:** Publication-ready / Needs calibration / Overclaims.
2. **Claim Labels:** Hypothesis, assumption, derivation, result, prediction, speculation.
3. **Risky Phrases:** Identify wording that overstates the case.
4. **Revised Text:** Provide a tighter replacement when requested.
5. **Remaining Evidence Needed:** What would be required for stronger claims.

## Common Failure Modes

- "This proves" used for a model-dependent argument.
- "Observed" used where only "predicted" or "testable" is justified.
- "Necessarily" used without a theorem or derivation.
- Conclusions omit EFT, stability, or observational caveats.
- Conceptual prose uses technical terms without operational definitions.

## Checklist

- Claims labeled by status?
- Unsupported claims marked?
- Strong verbs justified?
- Assumptions visible?
- Regime caveats included?
- Technical clarity preserved?
- Article/thesis tone maintained?
