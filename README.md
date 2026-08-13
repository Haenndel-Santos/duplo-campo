# Teoria do Duplo Campo Primordial / Duplo Campo

This repository organizes and versions the working files for the Teoria do Duplo Campo Primordial (TDCP), including chapters, appendices, technical variants, project-local agent skills, and operational documentation.

## Scientific State (2026-08-13)

The current verdict chain lives in `docs/` and `auditoria/` — **do not
cite v1 manuscript numbers or pre-2026-08-12 result docs without the
supersession filter** in `docs/resultado_r7_cascata.md` §4. A second
filter applies to numbers only: c_s² values in the R-9a/R-10/R-11 docs
carry the value-supersession banner of Erratum-03 (below).

- `auditoria/erratum_02_reducao_numerica.md` — the former scalar-sector
  ghost/no-go was an artifact of a numeric reduction bug (the symbolic
  library was always correct).
- `docs/resultado_r7_cascata.md` + `resultado_r7e_saude_interna.md` —
  the corrected 2-DOF scalar sector is healthy **in the late era**; old
  band/ISW predictions withdrawn. Its coverage was a ≥ 100: those gates
  never probed the early era, and were blind to gradient by
  construction.
- `docs/resultado_r10_consolidado.md` +
  `resultado_r11_nogo_gradiente.md` + `resultado_r12b_teorema_cs2.md` —
  **class no-go by gradient**: in class F1 (β₃ = 0, matter coupled to g
  only, finite branch) the metric scalar has c_s² = −1 exactly as
  r → 0, for any (β₀, β₂, β₄, μ) — 108/108 cells, |c_s²+1| ≤ 1.1e−7 —
  with positive kinetic term (gradient, not ghost), and c_s² = +1
  exactly in the late era; closed form proved in the minimal cell
  (β₂ = β₄ = 0). Of the four known exits, **all four are closed** —
  β₁(φ₋) modulation, Vainshtein screening, β-form, and the infinite
  branch — but the infinite-branch exclusion was **entirely replaced**,
  not confirmed, and the replacement must be stated every time the
  count is quoted.
- `docs/resultado_r13a_criterio_higuchi_fonte.md` +
  `docs/resultado_r13b_ibb_ramo_infinito.md` — **the F1 infinite
  branch (IBB) is EXCLUDED BY THE HIGUCHI GHOST.** Mandatory
  qualification: the original exclusion via the `ξ = 0` crossing
  remains **REVOKED** — that criterion (ξ crosses zero ⟹ vanishing
  lapse in the f sector ⟹ singular point) is, point by point, the
  bounce of `b` that Könnig et al. (1407.4331) §II/§VI treat
  explicitly and defend as physical, on three stated grounds, and
  nothing here revives it. The current exclusion is **independent**:
  the infinite branch violates the Higuchi condition **throughout its
  entire history** in the IBB cells tested. The Higuchi functional of
  Könnig 2015 (1503.07436, eq. 14) was translated at the source and
  **re-verified by CAS along an independent route** — three symbolic
  residues **zero**, general β_n and μ, dust — giving
  **Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0**. Measured: r′ < 0 over 100% of the
  history in **108/108 cells**; Higuchi satisfied at **0 of 64 800
  points**; agreement Higuchi(source) ⟺ r′ ≥ 0 in **64 800/64 800**;
  **positive control** on the finite branch **400/400**. In closed
  form, m_T²/H²|_{r_c} = 1 + 1/(μr_c²) with μr_c² > 1 always, hence
  **1 < sup(m_T²/H²) < 2 strictly** across the whole window; and μ is
  **pure rescaling** in the genuine IBB. Note that m_T² > 0 in 108/108:
  *the IBB branch is not tachyonic in the tensor-mass sense; it is
  excluded by the Higuchi ghost condition.* The finding is the
  complementarity: *within the F1 parameterization, the two standard
  cosmological branches fail for complementary reasons: the finite
  branch violates scalar-gradient stability in the early universe,
  while the genuine infinite branch avoids that instability but
  violates the Higuchi condition throughout its evolution.* The IBB
  gradient channel is **healthy according to the source** (§IV A of
  1503.07436, which **confirms** and does **not** retract 1407.4331);
  it is an independent channel and does not save Higuchi. The R-13b
  gate does not measure gradient, and that blindness stays declared as
  good practice — but it does **not** block the verdict: a physical
  ghost is enough to exclude, regardless of the gradient being healthy.
  A `c_s²` test in the IBB is **desirable additional validation, not a
  requirement**.

  | Exit | Current verdict | Reason |
  |---|---|---|
  | Infinite branch / IBB | **EXCLUDED** | Higuchi ghost, r′ < 0 throughout the history |
  | old `ξ = 0` argument | **REVOKED** | a vanishing lapse / bounce is not by itself a singularity |
  | gradient in the IBB | **HEALTHY** per the source | independent channel; does not save Higuchi |

  Only one door is left ajar: β₃ ≠ 0, which leaves F1.
  **The unstable era covers recombination**, so the linear CMB of F1 is
  not calculable while this picture holds.
- `docs/resultado_r12_instrumento_e_cs2.md` — **Erratum-03
  (instrument)**: Ċ was differentiated with 2nd-order `np.gradient`
  from R-7 to R-12c, and the O(h²) error is amplified by the
  conditioning of the reduction. Demonstrated, not conjectured. It
  contaminated VALUES, not STATEMENTS: the R-7/R-8 domain is
  quantitatively safe (deviation ≤ 4e−4, signs unchanged) and R-8a
  never touches the chain.
- `docs/resultado_r8a_quase_estatico.md` + `resultado_r8b_limite_mH0.md`
  — observational probes: sub-horizon consistent with GR; m_T/H₀ ≈
  2.3–2.4 pinned by the background in the benchmark family (the corpus
  postulate m ~ 30–300 H₀ is unreachable there). Their scope is now
  restricted: there is no linear observational program to run while the
  unstable era covers recombination.
- `manuscript-v2/00_estrutura.md` — the v2 skeleton (updated
  2026-08-13); the v1 manuscript is frozen as historical record
  (`docs/decisao1_congelamento_v1.md`).

What falls is the *sufficiency* of the F1 implementation as a
cosmology — not TDCP as a conceptual hypothesis, and not the background,
the tensor sector, the 2-DOF count, either erratum, or the method.

## Repository Structure

- `Duplo Campo/`: main Portuguese project folder with chapter and appendix `.docx` files.
- `Duplo Campo/.agents/skills/`: project-local Codex skills for TDCP review workflows.
- `Eng Version/`: English version material currently present in the workspace.
- `docs/`: operational project documentation and progress notes.

## Document Handling

The `.docx` files are the main project documents. Do not edit, reformat, or regenerate them unless a future task explicitly asks for that work.

The `.agents/skills` directory contains local instructions for agents working on TDCP material. These instructions should be read before reviews or edits involving theory architecture, equations, chapter continuity, observational claims, or scientific prose.

Backup and archive files such as `.zip` are ignored by default. `Duplo Campo.zip` remains preserved in the workspace for later inspection, but is not part of the default Git baseline.
