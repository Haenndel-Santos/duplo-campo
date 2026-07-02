# Duplo Campo Project Master

## Objective

Maintain a local Git baseline for the Duplo Campo / TDCP project so chapters, appendices, English-version material, local agent skills, and operational documentation can be tracked safely over time.

## Repository Structure

- `Duplo Campo/`: primary `.docx` chapters and appendices.
- `Duplo Campo/.agents/skills/`: local Codex skills and agent workflow instructions.
- `Eng Version/`: English-version working material.
- `docs/`: project coordination, baseline notes, and progress records.
- Root Git files: `.gitignore`, `.gitattributes`, and `README.md`.

## Rules for Future Agents

- Read `Duplo Campo/.agents/skills/README.md` before work involving TDCP theory, chapter continuity, equations, or scientific claims.
- Preserve existing `.docx` files unless the user explicitly requests document edits.
- Do not run formatters or automated document conversion on Office files without explicit approval.
- Do not create remotes or push changes without explicit approval.
- Keep commits small, descriptive, and scoped to the requested work.

## Safety Criteria

The chapter and appendix `.docx` files are treated as primary source documents. They should not be edited, reformatted, renamed, moved, or regenerated unless requested directly.

## Versioning Criteria

Use Git for local tracking. Prefer focused commits that clearly describe the operational or content change. Archive files are ignored by default unless the user explicitly chooses to version them.
