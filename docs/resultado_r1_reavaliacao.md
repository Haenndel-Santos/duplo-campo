# R-1 — Reavaliação do No-Go β-Constante por Evolução Real — Resultado

**Data:** 2026-08-11 (noite). Script:
`auditoria/code/r1_reavaliacao_nogo_evolucao.py` (saída em
`auditoria/code/out/r1_reavaliacao_nogo_evolucao.txt`). Primeiro item
da fila de reavaliação pós-D2 (`resultado_d2_evolucao.md` §6).
Execução em sessão autorizada pelo autor (.venv). Controle GR ✓.

---

## 1. Veredito

**14/14 células amostradas: TARDIA-DILUI. Nenhuma cresce.** O no-go
tardio congelado (σ/H≈2.5–3.1 persistente, 6.8 em k alto — previsto
pelo instrumento antigo em TODAS as células) é **vácuo em todo o
espaço amostrado**: a dinâmica real tardia dilui em todas (taxas
−0.28 a −5.4 por H). No nível linear dinâmico, **o setor escalar
tardio da TDCP-F1 β-constante é estável nas células testadas.**

Amostra (fronteira declarada): escada de μ da célula REF
(1,−0.4)×μ∈{0.3,1,3,10,30,100}; célula da lei de escala (0.5,−0.84)
×{0.3,1}; célula da fresta (0.2,−1.0)×{0.1,1} — incluindo a célula do
fantasma quase-nulo; três cantos do retângulo (β₁,β₂) em μ=1; k_c=10
em todas + k_c=100 na REF. Uma trajetória por célula, a∈[0.2,2000].

## 2. Os dois achados estruturais da tabela

**(a) negK = 1 UNIVERSAL.** Em todas as 14 células, a matriz cinética
reduzida em a=400 tem exatamente **uma** direção negativa. O fantasma
estrutural (D1) não é peculiaridade da fresta — é **propriedade da
classe** no ramo finito tardio. A evolução linear não o testa (direção
de energia negativa não gera crescimento linear sem acoplamento); sua
letalidade — no nível de interação, ou como sintoma de representação
(o debate "breakdown of linear PT" da literatura) — é agora **A**
pergunta do setor escalar. → R-2.

**(b) A amplificação transiente varia por 5 ordens de magnitude em
e-folds:** lnA_max de 3.9 (canto (2,−0.05)) a **14.6 na fresta μ=0.1**
(≈2×10⁶ em amplitude) — com 9–10 na lei-de-escala μ=0.3 e no k alto.
A instabilidade real da classe é a **transiente da era de transição**
(tipo-gradiente, taxa ∝ k — consistente com a literatura do ramo
finito), e seu dano depende fortemente da célula e de k. A viabilidade
observacional da F1 passa a depender de mapear lnA(k, célula) contra
os vínculos — → R-4 (k grandes; comparação quantitativa com
Comelli/Könnig; a rota de escape de Akrami et al. 1503.07521 na
direção μ pequeno é relevante e nossa fresta μ=0.1 tem o MAIOR lnA da
amostra — tensão a investigar).

Primordial: taxas reais ≈ 0 nestes k (levemente positiva só na fresta,
+1.4) — o "taquião primordial" congelado de σ/H~6–8 também não se
realiza dinamicamente nestes k.

## 3. O estado do setor escalar da F1 após D2+R-1

| Pergunta | Estado |
|---|---|
| Taquião tardio (o centro do antigo no-go) | **vácuo** — dilui em 14/14 células |
| Instabilidade primordial congelada | não se realiza nestes k (reais ≈ 0) |
| Instabilidade REAL da classe | transiente de transição, tipo-gradiente, lnA 4–15 conforme célula/k |
| Fantasma estrutural (negK) | **universal na amostra** — letalidade em aberto (R-2) |
| Viabilidade linear tardia | **estável** nas células testadas |

O no-go do programa, como enunciado, **não sobrevive à dinâmica**. O
que o substitui como questão de viabilidade: (i) o fantasma
estrutural universal; (ii) o dano observacional do transiente
(k-dependente). Ambos têm dono na fila (R-2, R-4).

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| 14/14 células diluem no tardio (taxas medidas; controles ✓) | 2b (amostra e k declarados) |
| negK=1 em todas (a=400, redução validada pelo D1) | 2b |
| lnA_max por célula (transiente) | 2b (uma trajetória/célula; k_c limitado) |
| "O setor tardio da F1 β-constante é linearmente estável" | 2b — **não** é teorema; amostra de 13 células do retângulo + escada de μ |
| Fantasma letal ou não | **aberto** (R-2) |

## 5. Fila atualizada

- **R-2** (próximo): a direção de K negativa — caracterizar
  (composição, acoplamentos, energia; conexão com o cutoff/strong
  coupling da literatura). É o que resta do no-go.
- **R-3**: janela não-fatorada da Investigação 2 por evolução real
  (as tendências congeladas de σ/H≈13 da Fase B são suspeitas pelas
  mesmas razões).
- **R-4**: k grandes + comparação quantitativa com a instabilidade de
  gradiente da literatura + mapa de lnA vs vínculos observacionais.
- Depois: enunciado final do setor escalar → cap. 07 → paper (com o
  eixo novo: o aviso metodológico + a reconciliação + o que sobrou).
