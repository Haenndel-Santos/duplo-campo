# Duplo Campo Project Master

## Objective

Maintain a local Git baseline for the Duplo Campo / TDCP project so chapters, appendices, English-version material, local agent skills, and operational documentation can be tracked safely over time.

## Repository Structure

- `Duplo Campo/`: primary `.docx` chapters and appendices (original source;
  to be regenerated from `manuscript/` once the editing pass below is
  finalized — see "Current Editorial Pass").
- `Duplo Campo/.agents/skills/`: local Codex skills and agent workflow instructions.
- `Eng Version/`: English-version working material (original; CHAPTER 1.docx
  is, despite its name, a condensed English version of Chapters 1–14).
- `manuscript/`: working copy of the full corpus in Markdown, converted from
  the `.docx` files so edits are text-diffable and reviewable in git.
  - `manuscript/capitulos/`: Cap.1–Cap.26 (main numbered F1 body) plus
    Cap.6.2 (a real revision of Cap.6, per the "X.2 = revision only"
    convention in `renumbering_log.md`).
  - `manuscript/apendices/`: Appendix A–H (technical support material),
    Appendix I–K (exploratory research line — cosmological wave-function
    collapse / entanglement / dark energy, translated from the English
    chapters, evaluated as only partially integrable to the F1 body — see
    `integration_assessment.md`), Appendix L (short conceptual bridge
    between I–K and the main body).
  - `manuscript/eng-version/`: the English CHAPTER 1 material, unchanged.
- `hygiene_log.md`, `renumbering_log.md`, `integration_assessment.md`:
  deliverables of the 2026-08-05 editorial pass (see `docs/progress.md`).
- `docs/`: project coordination, baseline notes, and progress records.
- Root Git files: `.gitignore`, `.gitattributes`, and `README.md`.

## Current Editorial Pass (started 2026-08-05)

An explicit, user-requested editing pass is underway: hygiene (removing
chat-origin residue), structural reconstruction of incomplete chapters,
translation of the final English chapters, an integration assessment,
and renumbering. This is being done in `manuscript/` (Markdown) rather
than directly on the `.docx` files so the work stays reviewable in git.
**The `.docx` files in `Duplo Campo/` will be regenerated from the
finished `manuscript/` content and renamed to match** once editing is
complete — this is expected, approved, in-scope work for this pass, not
a violation of the safety rule below. The rule below governs *unrelated*
future work.

## Sincronização entre cópias de trabalho (GitHub)

Existem DUAS cópias de trabalho deste repositório, em máquinas
diferentes, ambas commitando em `master` de
`https://github.com/Haenndel-Santos/duplo-campo` (público):

- `C:\Haenndel Projects\Duplo Campo` (máquina 1 — tem `.venv` criado)
- `C:\Haenndel Projects 2\Duplo Campo` (máquina 2 — origem da v2)

**Regra obrigatória de sessão:** `git pull` ao ABRIR qualquer sessão de
trabalho e `git push` ao FECHAR (ou após cada lote commitado). Nunca
trabalhar sobre estado desatualizado; em caso de divergência, resolver
com merge explícito — nunca force-push.

**Saídas oficiais são evidência e são versionadas**: o `.gitignore`
tem exceções para `derivations/code/out/` e `auditoria/code/out/`.
Pendência conhecida: as saídas da v2 (scans do no-go etc.) existem só
na máquina 2 — na próxima sessão lá, `git add auditoria/code/out/` +
commit + push (após o pull, o git passará a listá-las como untracked).

**Ambiente Python:** `requirements.txt` fixado (sympy 1.14.0,
numpy 2.5.1, scipy 1.16.3). Rodar scripts oficiais SEMPRE pelo
`.venv` (`python -m venv .venv` + `pip install -r requirements.txt`).

O repositório GitHub `Haenndel-Santos/TDCP` (privado) está vazio e foi
arquivado para evitar confusão — o repositório canônico é
`duplo-campo`.

## Rules for Future Agents

- Read `Duplo Campo/.agents/skills/README.md` before work involving TDCP theory, chapter continuity, equations, or scientific claims.
- Outside of an explicitly requested editorial pass (see above), preserve existing `.docx` files unless the user explicitly requests document edits.
- Do not run formatters or automated document conversion on Office files without explicit approval.
- Do not create remotes or push changes without explicit approval.
- Keep commits small, descriptive, and scoped to the requested work.
- When editing chapter/appendix content, work in `manuscript/` (Markdown) first; treat `.docx` as a generated artifact of that source once the current editorial pass establishes this workflow.

## Safety Criteria

The chapter and appendix `.docx` files are treated as primary source documents. They should not be edited, reformatted, renamed, moved, or regenerated unless requested directly — which is the case for the editorial pass described above.

## Versioning Criteria

Use Git for local tracking. Prefer focused commits that clearly describe the operational or content change. Archive files are ignored by default unless the user explicitly chooses to version them.
