# Teoria do Duplo Campo Primordial / Duplo Campo

This repository organizes and versions the working files for the Teoria do Duplo Campo Primordial (TDCP), including chapters, appendices, technical variants, project-local agent skills, and operational documentation.

## Scientific State (2026-08-12)

The current verdict chain lives in `docs/` and `auditoria/` — **do not
cite v1 manuscript numbers or pre-2026-08-12 result docs without the
supersession filter** in `docs/resultado_r7_cascata.md` §4:

- `auditoria/erratum_02_reducao_numerica.md` — the former scalar-sector
  ghost/no-go was an artifact of a numeric reduction bug (the symbolic
  library was always correct).
- `docs/resultado_r7_cascata.md` + `resultado_r7e_saude_interna.md` —
  corrected 2-DOF scalar sector is healthy in all tested regimes; old
  band/ISW predictions withdrawn.
- `docs/resultado_r8a_quase_estatico.md` + `resultado_r8b_limite_mH0.md`
  — first observational probes: sub-horizon consistent with GR;
  m_T/H₀ ≈ 2.3–2.4 pinned by the background in the benchmark family
  (the corpus postulate m ~ 30–300 H₀ is unreachable there).
- `manuscript-v2/00_estrutura.md` — the v2 skeleton (updated
  2026-08-12); the v1 manuscript is frozen as historical record
  (`docs/decisao1_congelamento_v1.md`).

## Repository Structure

- `Duplo Campo/`: main Portuguese project folder with chapter and appendix `.docx` files.
- `Duplo Campo/.agents/skills/`: project-local Codex skills for TDCP review workflows.
- `Eng Version/`: English version material currently present in the workspace.
- `docs/`: operational project documentation and progress notes.

## Document Handling

The `.docx` files are the main project documents. Do not edit, reformat, or regenerate them unless a future task explicitly asks for that work.

The `.agents/skills` directory contains local instructions for agents working on TDCP material. These instructions should be read before reviews or edits involving theory architecture, equations, chapter continuity, observational claims, or scientific prose.

Backup and archive files such as `.zip` are ignored by default. `Duplo Campo.zip` remains preserved in the workspace for later inspection, but is not part of the default Git baseline.
