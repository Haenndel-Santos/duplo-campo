# R-10 — Consolidado: a Instabilidade de Gradiente e o Que Sobrou da F1

**Data:** 2026-08-13. Scripts: `r10a_gradiente_alto_z.py`,
`r10b_severidade_instabilidade.py`, `r10c_saidas_ramo_e_dinamico.py`,
`r10d_screening.py` (saídas em `auditoria/code/out/`). Este documento
substitui, como referência, os parciais `resultado_r10a_gradiente.md`
e `resultado_r10c_saidas.md` (que permanecem como registro).

---

## 1. O resultado, em uma frase

**O escalar métrico da F1 tem instabilidade de gradiente
(c_s² ≈ −1, cinética positiva) durante toda a era que precede
z ≈ 0.6–3, incluindo a recombinação — e nenhuma das saídas
conhecidas a cura.**

## 2. A cadeia de quatro testes

| Teste | Pergunta | Resultado |
|---|---|---|
| **R-10a** | c_s² em toda a história (não só a ≥ 100) | c_s² ≈ −1.0 a −1.26 para r ≲ 0.05; +1.01 tardio. Cinética **positiva** (é gradiente, não fantasma); espectador calibra em 1.00000; independente de condicionamento |
| **R-10b** | Quão grave? | a_cross = 0.574 (β₁=1) ⟹ **z_cross ≈ 0.62**. Modos com k/aH ≳ 8 saem do linear (lnA até 32); os de k/aH ~ 1–7 ficam lineares e crescem 2–10⁴× |
| **R-10c** | Ramo infinito? Modulação salva? | Ramo infinito: **não conecta** (ξ cruza zero) — exclusão correta, justificativa do corpus precisa de qualificação de época; existe 2ª solução tardia inexplorada. Modulação β₁(φ₋): **não salva** — 3.07 e-folds instáveis, lnA = 85.7 |
| **R-10d** | Screening protege? | **Não.** δ_screen = (4π/3)(m_T/H)² ≈ **20–60** em todas as eras: o Vainshtein só opera dentro de estruturas não-lineares. *O λ cancela na conta* — não existe escala linear protegida |

## 3. A distinção que decide (R-10d)

O argumento de Akrami et al. ([arXiv:1503.07521]) tem duas versões,
que costumam ser confundidas:

- **(V1) "a instabilidade está abaixo da escala de Vainshtein"** —
  **MORTA** nesta implementação. A condição de screening,
  δ ≳ (4π/3)(m/H)², **não depende da escala** (o λ cancela): é uma
  condição sobre o *contraste*. Com m_T/H ≈ 2.3–3.9, exige δ ≳ 20–60,
  ou seja, halos. Perturbações lineares cosmológicas nunca são
  screened.
- **(V2) "o crescimento leva ao não-linear, logo o linear não decide"**
  — **VIVA**, e é o que o R-10b mediu. Mas isto **não é proteção**: é
  ignorância. Impede de *refutar* a teoria pela instabilidade linear,
  e impede igualmente de *calcular* qualquer observável linear na era
  instável.

**E a era instável cobre a recombinação** (z = 1100 ⟹ a = 8.5e−4,
dentro da janela instável nos dois fundos). Logo: **o CMB da F1 não
é calculável linearmente** enquanto este quadro valer.

## 4. O que isto faz com o programa

**Cap. 07 (v2):** já revisado — o enunciado de saúde vale para a era
tardia; a instabilidade em r → 0 está declarada.

**Cap. 09 (v2) — precisa de revisão:** o "teste decisivo" proposto
(C_ℓ de baixo-ℓ sobre o sistema 2-DOF) **não pode ser executado como
planejado**. Não por falta de máquina, mas porque o objeto que ele
calcularia é linearmente indefinido na época em que o CMB se forma.

**As três opções reais que restam** (nenhuma testada):

1. **Varredura de FORMA-β** procurando c_s² > 0 em r → 0. O R-8b
   mostrou que a forma do benchmark é rígida sob *rescala* (fold em
   s ≈ 5.7) — mas nunca varremos a *forma* (β₂/β₁, β₄/β₁, β₃ ≠ 0). É
   o caminho mais barato e o único que pode salvar a implementação
   dentro do programa atual.
2. **Tratamento não-linear** da era instável — fora do alcance do
   projeto hoje.
3. **Declarar validade restrita**: a F1 como implementação com
   domínio z ≲ 3, sem previsão de CMB. Honesto, publicável como
   estudo de classe, mas abandona o objetivo cosmológico.

## 5. O que NÃO mudou

O Erratum-02 continua válido (o fantasma do Gate F era artefato
numérico); a contagem 2-DOF continua válida; o espectador δφ₋ continua
saudável em toda a história (calibrador c_s² = 1.00000 em todos os
pontos); o fundo, o setor tensorial, a constraint de Bianchi
(Erratum-01) e o Gate 1 não são tocados. A predição m_T ≈ 2.3 H₀
segue de pé — e, ironicamente, é ela que mata o screening (δ_screen
∝ (m/H)²).

## 6. Estatuto e fronteiras

Nível 2b com fronteiras declaradas: benchmark β-constante + uma
trajetória dinâmica (célula REF), sem era de radiação (o mapa a ↔ z
usa a âncora a₀ = 0.931 do R-8b e muda com radiação), kh ∈ {30, 100},
δ_i = 1e−5 como referência. O acoplamento à matéria perturbada — que
decide o observável final — nunca foi calculado; é concebível (não
demonstrado) que ele altere o quadro.

**O que este resultado NÃO é:** uma refutação da TDCP como hipótese
conceitual. É uma refutação da *suficiência* da implementação F1 no
ramo finito com esta forma-β, para fins cosmológicos, no estado
atual.

## 7. Fila

1. **Varredura de forma-β** (novo item nº 1): c_s²(r → 0) como função
   de (β₂/β₁, β₄/β₁, β₃, μ). Critério pré-declarado: existe célula com
   c_s² > 0 em r → 0 e fundo viável? É barato — a máquina do R-10a já
   faz o cálculo por ponto.
2. Se existir: refazer a cascata nessa célula.
3. Se não existir: escrever o enunciado de validade restrita (opção 3)
   e reorientar o cap. 09.
4. Pendências herdadas: Gate 2B + difeomorfismo espacial (Bloco 2),
   Vainshtein/PPN astrofísico, paredes de domínio (μ₋), radiação,
   varredura de μ.
