# R-7 — Reexecução da Cascata no Sistema 2-DOF Corrigido: Banda Morta, Espectador Saudável, Enunciado Observacional v4

**Data:** 2026-08-12. Scripts: `auditoria/code/r7a_dinamica_2dof.py`,
`r7b_banda_estatica_2dof.py`, `r7c_banda_pousado_2dof.py` (saídas
oficiais em `out/`). Execução: em sessão. Contexto:
`auditoria/erratum_02_reducao_numerica.md` — o `reduz_ponto` numérico
usado de D-2 a R-5 dobrava Ċ nas entradas off-diagonais de `W_XX`; o
3º DOF escalar (e o fantasma do Gate F) era artefato. Este documento
consolida a reexecução e **substitui** os resultados da dinâmica
reduzida de D-2/R-1 (classe β-constante), R-4a/b/c e R-5.

---

## 0. Maquinaria corrigida (R-7a) — o que muda de método

1. **Redução em 2 estágios**: E1 (absorção one-shot com S simétrica,
   Ċ contado uma vez por par) + Schur em `W_XX` → 3×3; gate **G1**
   certifica o zero estrutural da linha cinética de Ψ_f
   (canal-S: 8e-16/2e-15) e só então a linha é zerada; E2 elimina
   Ψ_f (auxiliar legítima, `W00` resolvido) → 2×2 (Ẽ = k²E_f, δχ).
2. **Equilibração** `B̃ = kB`, `Ẽ = k²E_f` (congruência constante no
   tempo): sem ela `W00` nasce de cancelamento de profundidade 1e-14
   da escala ambiente — irresolúvel em float64. Com ela,
   `min|W00|/esc = 0.09–0.15`.
3. **V-XREP-a** (nomenclatura corrigida pós-review; ver nota no
   erratum-02 §6): a redução roda com dois canais independentes de
   Ċ — gradiente de grade (produção) e `dt_background` simbólico
   (exato; estendido com as taxas de 2ª ordem do fundo) — dentro da
   representação Γ–Γ. Concordância no interior da trilha: **5.2e-8**
   (estático), e primeira validação na trilha dinâmica no R-7c.
   Bordas do estêncil one-sided isoladas e substituídas (declarado).
   O **V-XREP-b** (Γ–Γ vs ADM, a definição original do erratum) foi
   executado no r6c/r6d e é obrigatório a cada mudança da maquinaria.
4. **Envelope** para taxas/lnA (robusto a cruzamentos de zero);
   halving com critério de Richardson (RK4: erro ≈ dif/15).

## 1. R-7a — dinâmica 2-DOF β-constante: SAUDÁVEL (substitui D-2/R-1 na classe)

| Medida | β₁=1 | β₁=4.47 |
|---|---|---|
| Autovalores cinéticos negativos (24000 pts) | **0** | **0** |
| Acoplamento K₂/C₂/W₂ entre Ẽ e δχ | **exatamente 0** | **exatamente 0** |
| Taxa física tardia δχ (medida) | −0.381/H | −0.088/H |
| Âncora analítica −3/2+√(9/4−0.3/H²) | −0.368 ✓ | −0.082 ✓ |
| Taxa tardia Ẽ (medida) | −2.5…−2.6 | −2.7 |
| Dispersão δχ: ω/H vs √(kh²+0.3/H²) | exata (5 k) | exata (5 k) |
| Halving (erro Richardson) | ≤0.020 | ≤0.021 |

Leituras:

- **O σ_can ≈ 1.13/1.41 do Gate F-b era a normalização a^{3/2} do
  espectador saudável** — a âncora dinâmica fecha em 0.01–0.02. O
  "CONF-BANDA" do F-b previa a banda porque ambos eram o mesmo
  artefato/re-escala, não física.
- O único escalar métrico físico (Ẽ) é **overdamped e decai** (sem
  frequência própria tardia; `W_Ẽ` chega a ser negativo tardio com a
  fricção dominando — nenhum modo crescente na evolução real).
- O QEP congelado fica rotulado como *dispersão-apenas* (só C
  antissimétrica entra — lição do D2 mantida).

## 2. R-7b — a banda estática: **MORTA** (substitui R-4b estático)

lnA de passagem (kh 20 → 0.2), componente métrica (envelope de Ẽ):

| fundo | antigo (3-DOF espúrio) | reauditoria externa | **este (2-DOF)** |
|---|---|---|---|
| β₁=1 | +3.97 | −8.07 | **−8.37** |
| β₁=4.47 | +3.62 | −7.96 | **−8.39** |

Controles: NULL interno (espectador δχ na mesma passagem): −3.7/−3.2
(critério ≤ +0.5; GR ≈ −4.3). AUTOSIM v2: em regime decadente o lnA
de passagem é sensível ao estado de entrada (mix dos dois ramos
overdamped) e não é invariante de k; o invariante é o sinal e a
ordem — k e 3k dão −8.4 e −10.6 (ambos < −4 ✓; diferença reportada).

**Φ_g reconstruído com os blocos corrigidos** (o elo do R-5):
Δln|Φ_g| na passagem = **−8.30…−8.32** (externa: −6.9…−8.3);
mediana |Φ_g|/A_met = 0.040/0.085 — *finita porque ambos decaem
juntos*. A "razão sustentada 0.160" do R-5A era real como razão, mas
era razão entre duas quantidades **caindo** — lida como transferência
de amplificação porque o numerador vinha do sistema espúrio (e do
`W_XX` errado).

## 3. R-7c — a banda no pousado (β₁(φ₋)): **MORTA** (substitui R-4b dinâmico/R-4c)

lnA de passagem (kh 20 → 0.2) da componente métrica, por época de
cruzamento; 0 autovalores cinéticos negativos em 8/8 braços
(14000 pts cada):

| a_cross | antigo (3-DOF) | externa | **este (2-DOF)** |
|---|---|---|---|
| 500 | −0.21 | −12.94 | **−10.96** |
| 1000 | +3.26 | −14.27 | **−13.00** |
| 1600 | +1.57 | −13.21 | **−12.39** |
| 2500 | +3.17 | −14.01 | **−14.71** |
| 4000 | +4.80 | −14.33 | **−11.40** |
| 8000 | +4.03 | −13.52 | **−11.42** |
| 15000 | +4.52 | −12.33 | **−12.70** |
| 30000 | (incompleto) | (incompleto) | **−10.72** (parcial, até kh=0.38) |

Δln|Φ_g| na passagem: **31/32 combinações IC×época negativas**
(−0.02…−8.8). A exceção é dchi(vel) em a_cross=500: **+2.695** — um
log de componente única cujo valor de entrada (em kh=20) está perto
de um zero (a Φ_g sourced por δχ nasce minúscula ali); a norma
métrica da MESMA IC decai (lnA_met = −4.59), como em todas as 32.
É exatamente a sensibilidade a zero-crossings que a reauditoria
externa já advertira para logs de componente — o enunciado robusto é:
*a norma métrica decai em 32/32; Φ_g das ICs métricas decai em
16/16 (−2.1…−8.8)*. Na trilha dinâmica E_f e δχ **acoplam** (F′≠0) —
as ICs de δχ também carregam conteúdo métrico.

**POUSADO-BANDA-MORTA**: nenhuma época de cruzamento amplifica. O
R-4 dinâmico (amplificação por época; "supressão-matéria" do R-4c)
era artefato do 3º DOF espúrio. **R-4 COMPLETO substituído.**

Registro de método (2 rodadas): a 1ª rodada teve os 8 braços
**bloqueados pelo V-XREP** (G3 = 6e-3…7e-2) — o gate pegou uma
inconsistência real do *fundo*: o pousado é integrado por Euler
explícito, e as taxas armazenadas (χ̈ analítico; ξ com rp de 1ª
ordem) não fecham com as derivadas dos splines dos valores — em
particular a identidade `ḃ = bξH_f` que o canal-S assume. Corrigido
tornando todas as taxas derivadas-de-spline (ξ recomputado para
fechar a identidade por construção); G3 caiu para 3–8e-5. A
inconsistência Euler do fundo existia desde o R-3/R-4 antigo, sem
detector.

## 4. O que fica dos R-antigos (estratificação)

| Resultado antigo | Estado pós-R-7 |
|---|---|
| D-2 "diluição tardia; transiente limitado" | **Substituído**: a diluição tardia CONFIRMA no sistema físico (R-7a); o "transiente lnA~4" era o artefato — não existe no 2-DOF (R-7b/c) |
| R-1 "no-go congelado é vácuo; tudo dilui" | Conclusão qualitativa sobrevive no sistema físico; números antigos descartados |
| R-2 fantasma estrutural | **Caiu** (erratum-02) |
| R-3/3b/3c (rolagem, mecanismo do pouso — *fundo*) | Fundo intocado (reintegrado e conferido no R-7c; nota: taxas Euler internamente inconsistentes ~1e-3, detectadas pelo V-XREP e tratadas — §3); dinâmica perturbativa reduzida antiga descartada |
| R-4a/b/c banda + supressão-matéria + enunciado v3 | **Substituídos**: BANDA-MORTA (estática −8.4; pousado −11.0…−14.7 em 8/8 épocas) |
| Gate F-a/F-b (fantasma, ω₀/Λ₃, H-SC) | **Caíram** (erratum-02); o σ_can era o espectador re-escalado (R-7a fecha a conta) |
| R-5 (ISW 2–8×; dispersão p=0.44; canto-Akrami) | **Substituído** — ver §5 |
| Setor tensorial, background, Bianchi/erratum-01, Gate 1, lib simbólica | Ficam de pé |

## 5. Enunciado observacional v4 (substitui o v3 do R-4c e o R-5)

1. **Não há previsão de excesso ISW em baixo-ℓ.** A cadeia
   banda → Φ_g → ISW perdeu os dois primeiros elos no pipeline
   corrigido (Φ_g **decai** ~e⁻⁸ na passagem; não há banda). A
   "tensão real na direção errada" do R-5 está **retirada** — não
   porque a observação mudou, mas porque a previsão era artefato.
2. **A dispersão p=0.44 (R5-B) e a localização da tensão-Akrami
   (R5-C) estão retiradas** — ambas eram medidas sobre o ramo
   congelado-canônico do sistema espúrio.
3. O que o setor escalar corrigido diz no benchmark: **2 DOFs (1
   escalar métrico overdamped que decai + espectador δχ com
   ω² = k²/a² + U″)** — nenhuma assinatura observacional exótica no
   regime linear tardio deste brinquedo. Consistente com Hassan–Rosen
   e Comelli–Crisostomi–Pilo.
4. **A viabilidade observacional da F1 fica REABERTA e não-decidida**:
   sem fantasma e sem banda, o teste decisivo passa a ser o cálculo
   honesto de C_ℓ/P(k) com matéria+radiação acopladas sobre o sistema
   2-DOF (o "R-8"/CLASS-TDCP da fila). Nenhum enunciado de excesso ou
   de supressão é afirmado antes disso.

## 5b. Adendo (mesma data, sessão continuada): R-7e/f

A saúde interna foi FECHADA em `docs/resultado_r7e_saude_interna.md`:
Fase B sã (janela de deslocamento estruturalmente limpa; σ/H≈13 era
artefato; transiente δχ ≤ e^{0.4} autocurável), no-go de classe
retirado (scan μ×β₁ + fresta, zero violações). O no-go escalar da F1
está revogado em todos os regimes que o sustentavam; resta o R-8.

## 6. Fila

1. **R-8 (próximo gate legítimo)**: perturbações acopladas
   (γ, ν, b, CDM) + potenciais de Bardeen sobre a redução 2-DOF
   corrigida → C_ℓ^{TT,TE,EE}, P(k). Pré-requisito: dicionário de
   épocas fora do brinquedo (decisão de desenho com o autor).
2. Propagar erratum-02 aos docs históricos (banner de supersessão em
   resultado_d2/r1/r2/r3*/r4*/r5, gate F) — feito via este doc; os
   docs antigos permanecem como registro com o aviso do índice.
3. V-XREP vira obrigatório em qualquer redução numérica nova (já
   codificado nos R-7).
