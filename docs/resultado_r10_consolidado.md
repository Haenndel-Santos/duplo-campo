# R-10 — Consolidado: a Instabilidade de Gradiente e o Que Sobrou da F1

> **[SUPERSESSÃO DE VALOR — 2026-08-13, R-12]** Enunciado
> **confirmado**; números de c_s² superados (Ċ por `np.gradient` de
> 2ª ordem). Limpo: **c_s² = −1 exato** em r → 0 (108/108 células,
> |c_s²+1| ≤ 1.1e−7), **+1 exato** na era tardia, a_cross = 0.578,
> z_cross = 0.61. As quatro saídas continuam fechadas e a era
> instável continua cobrindo a recombinação. Ver
> `docs/resultado_r12_instrumento_e_cs2.md`.

> **[REABERTURA — 2026-08-13, R-12i]** *Nota acrescentada; o texto
> original deste documento permanece intacto.* Onde este documento diz
> "as quatro saídas continuam fechadas", leia-se **três fechadas e uma
> REABERTA**. A exclusão do ramo infinito (linha do R-10c na tabela
> do §2) por "ξ cruza zero ⟹ lapso do setor f se anula ⟹ ponto
> singular" **não se sustenta**: como `b = ra`, o nosso
> `ξ = r + dr/dN` é `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al.
> (1407.4331) — **mesmo sinal, mesmo zero** —, e aquele paper trata
> esse quique de `b` **explicitamente** (§II e §VI, com nota de rodapé
> 9), defendendo-o como físico por três razões declaradas: f não
> acopla à matéria e não tem interpretação geométrica; nenhuma
> variável de fundo ou perturbada apresenta singularidade;
> `√(−det f)·R̄(f)` permanece finita e não-nula, de modo que as
> equações de movimento existem em todo instante. A *infinite-branch
> bigravity* (IBB) é o **único** modelo estável em todos os tempos
> daquele paper.
>
> **Estado:** nem "fechada" nem "aberta e viável" — **reaberta,
> exigindo reavaliação**, com o alvo no ramo infinito da F1 **com
> β₄ ≠ 0** (o IBB viável exige `0 < β₄ < 2β₁`; a nossa célula mínima
> tem β₄ = 0, logo não é ela o alvo). **[ATUALIZADO 2026-08-13 —
> 1503.07436 verificado na fonte pelo autor.]** Há um argumento
> independente candidato, de outra natureza: Higuchi em universo em
> expansão exige **r′ > 0**, e o ramo infinito tem **r′ < 0**. As duas
> linhas do `posicionamento_literatura.md` sobre esse paper **não eram
> contraditórias** — são o mesmo enunciado em ramos diferentes; a
> tensão é entre as duas fontes e dissolve-se pela separação de canais
> (gradiente ≠ Higuchi/helicidade-0 ≠ setor tensorial). **Segue
> REABERTA:** nível 3, sem tradução para as nossas convenções; o teste
> está na fila. **O que não muda:**
> o no-go de gradiente do ramo finito e as outras três saídas
> (modulação β₁(φ₋) — R-10c; screening — R-10d; forma-β — R-11)
> seguem de pé. *Fonte:
> `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b).*

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

*[R-12i, 2026-08-13: a segunda metade da frase perdeu uma das quatro
saídas. Três seguem fechadas; a do **ramo infinito está reaberta** e
sob reexame, com o alvo em β₄ ≠ 0 — ver o banner de REABERTURA no topo
deste documento.]*

## 2. A cadeia de quatro testes

| Teste | Pergunta | Resultado |
|---|---|---|
| **R-10a** | c_s² em toda a história (não só a ≥ 100) | c_s² ≈ −1.0 a −1.26 para r ≲ 0.05; +1.01 tardio. Cinética **positiva** (é gradiente, não fantasma); espectador calibra em 1.00000; independente de condicionamento |
| **R-10b** | Quão grave? | a_cross = 0.574 (β₁=1) ⟹ **z_cross ≈ 0.62**. Modos com k/aH ≳ 8 saem do linear (lnA até 32); os de k/aH ~ 1–7 ficam lineares e crescem 2–10⁴× |
| **R-10c** | Ramo infinito? Modulação salva? | Ramo infinito: **não conecta** (ξ cruza zero) — exclusão correta, justificativa do corpus precisa de qualificação de época; existe 2ª solução tardia inexplorada. **[R-12i, 2026-08-13: REABERTA]** a exclusão por ξ cruzar zero não se sustenta — é o quique de `b` que 1407.4331 §II/§VI trata e defende como físico, com três argumentos; reexame pendente, alvo é o ramo infinito **com β₄ ≠ 0** (IBB viável exige 0 < β₄ < 2β₁; a célula mínima tem β₄ = 0). Ver o banner acima. Modulação β₁(φ₋): **não salva** — 3.07 e-folds instáveis, lnA = 85.7 |
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
