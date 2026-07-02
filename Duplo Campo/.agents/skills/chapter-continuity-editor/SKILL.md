---
name: chapter-continuity-editor
description: Check continuity between TDCP chapters. Use when reviewing chapter drafts, transitions, summaries, references to earlier chapters, symbol reuse, definition drift, narrative jumps, or claims that depend on previous TDCP derivations.
---

# Chapter Continuity Editor

## When to Use This Skill

Use this skill when a TDCP chapter is created, reordered, merged, summarized, or revised. Apply it especially to transitions between conceptual chapters and formal chapters, or between formal derivations and observational claims.

## What the Skill Must Check

- Definitions are not changed silently between chapters.
- Symbols keep the same meaning, domain, and assumptions.
- Chapter order remains logically progressive.
- New claims are linked to previous assumptions, derivations, or explicitly marked conjectures.
- References to earlier chapters are valid and specific enough to verify.
- The narrative does not jump from speculation to conclusion without derivation.
- Chapter introductions and conclusions do not overstate what the chapter actually proved.
- Local edits do not conflict with the global TDCP architecture.

## What the Skill Must Not Do

- Do not rewrite a chapter into a different theory.
- Do not hide discontinuities with stylistic transitions.
- Do not normalize inconsistent symbols by silently changing their meaning.
- Do not add references to nonexistent derivations.
- Do not accept "as shown above" unless the referenced result is actually present.

## Required Output Format

Return:

1. **Continuity Verdict:** Continuous / Needs bridge / Discontinuous.
2. **Definition and Symbol Audit:** Any drift or ambiguity.
3. **Dependency Map:** What the chapter depends on from earlier chapters.
4. **Narrative Gaps:** Missing bridges or unsupported transitions.
5. **Revision Instructions:** Specific edits, equations, or cross-references to add.

## Common Failure Modes

- A symbol is reused for a new object without warning.
- A conceptual premise becomes a mathematical result without derivation.
- A later chapter assumes a branch, gauge, or limit not introduced earlier.
- A summary claims the chapter establishes more than it does.
- Observational language appears before the perturbation or effective functions are defined.

## Checklist

- Definitions stable?
- Symbols stable?
- Prior results cited precisely?
- New claims derived or labeled?
- Chapter order coherent?
- Transitions explicit?
- Conclusions calibrated?
