# R-4c — O Confronto por Épocas: Supressão na Matéria, Dano Confinado ao Horizonte — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r4c_confronto_epocas.py`
(2ª rodada — oficial — em `out/r4c_confronto_epocas.txt`; 1ª
preservada em `out/r4c_confronto_epocas_rodada1.txt`). Execução:
autor (.venv). Bloco 3 do R-4, opções B+C (decisão do autor);
**fecha o arco R-4** (R-4a mapa → R-4b forma → R-4c confronto).

**Portões (2ª rodada):** R4c-BASE OK (passagem completa +3.97 =
R-4b ao centésimo); R4c-C-NULL PASSA no critério corrigido
(unilateral: GR dá −2.26/−14.86 — decaimento puro, sem crescimento
espúrio). Registro de instrumento: a 1ª rodada teve dois defeitos de
especificação meus, ambos provados na própria saída (NULL bilateral
disparando sobre decaimento esperado; residência dos braços parciais
capturando o transiente de acomodação — prova aritmética: residência
+5.49 > soma das janelas contíguas +1.12). A v2 corrige (burn-in de
0.3 e-fold; estatística primária = janela matéria) e a validação
fecha: **a aditividade voltou** (kh_max=8: −1.15+0.05+2.09≈+0.99 vs
residência +0.86 ✓).

---

## 1. Braço B — a era Λ real (integral parcial)

lnA acumulado em 0.7 e-fold (a aceleração real até hoje) terminando
na escala kh_hoje:

| kh_hoje | lnA_parcial | fator |
|---|---|---|
| 6.0 | **+1.88** | ×6.6 |
| 4.0 | +1.66 | ×5.3 |
| 2.5 | +1.69 | ×5.4 |
| 1.6 | +1.34 | ×3.8 |
| 1.0 | +1.17 | ×3.2 |
| 0.7 | +0.70 | ×2.0 |
| 0.45 | +0.40 | ×1.5 |
| 0.3 | +0.04 | ×1.0 |
| 0.2 | −0.50 | ×0.6 |

**B_max = +1.88 (×6.6 em amplitude)**, na escala kh~6 (k ≈ 6·a₀H₀ —
ainda multi-Gpc). No horizonte (kh=1): ×3.2. Super-horizonte: ~nada.
O dano da era acelerada real é ORDEM UNIDADE-A-POUCOS, confinado a
escalas ~horizonte — território ISW/baixo-ℓ, dominado por variância
cósmica.

## 2. Braço C — a entrada na era de matéria: a banda DESLIGA

A pergunta decisiva para LSS (modos entrando no horizonte sob domínio
de poeira, regime nunca sondado). Resultado, com f_bi = fração
bimétrica do orçamento de energia:

| kh_max | matéria (f_bi≈0) | lambda (f_bi≈1) | residência (diag.) |
|---|---|---|---|
| 0.5 | **−0.78** | −0.15 | −7.08 |
| 1 | **−8.70** | −1.44 | −12.59 |
| 2 | **−10.10** | −0.93 | −10.36 |
| 4 | **−2.20** | +1.06 | −2.78 |
| 8 | **−1.15** | +2.09 | +0.86 |

**C_ent = −0.78 ≤ +0.5 → SUPRESSÃO-MATÉRIA.** Nenhum braço amplifica
na janela de matéria — modos de LSS passam ilesos pela entrada no
brinquedo. E a estrutura interna é exatamente a previsão mecânica do
R-4b §3, agora **2b no regime decisivo**: crescimento só onde
f_bi ≈ 1 (as janelas lambda dos braços kh_max=4 e 8, onde o modo
re-cruza a banda já sob Λ: +1.06/+2.09 — a física do braço B
reaparecendo como conferência interna, OK).

**A banda de amplificação é um fenômeno da era de domínio bimétrico,
com chave de liga/desliga em f_bi.**

## 3. O enunciado observacional consolidado (v3 — para o cap. 07)

> O setor escalar tardio da TDCP-F1 β-constante tem UMA instabilidade
> dinâmica real: a **amplificação transiente de banda** (modos com
> k_phys/H ~ 0.5–30; ~e^4 por passagem completa, e^6–7 com a cauda;
> classe inteira; GR-limpa; física — certificada na superfície do
> candidato a vínculo). Sua chave é a **fração bimétrica** do
> orçamento de energia: desliga sob domínio de matéria (LSS ileso na
> entrada do horizonte) e sob domínio de energia escalar
> (pré-rolagem), e opera só em eras de domínio da interação. No
> dicionário mínimo com a história cósmica real, o dano observável
> acumulado é **≤ ×6.6 em amplitude, confinado a escalas ~horizonte
> hoje** (kh 1–6; ISW/baixo-ℓ) — um alvo observacional, não um óbito.
> O antigo no-go congelado permanece vácuo (D2/R-1); o infravermelho
> profundo dilui; a direção cinética negativa estrutural permanece
> universal com letalidade em aberto (→ F-b); o modo de condensação
> δφ₋ realiza a condensação com assinatura tipo-massa e assenta
> (candidato do Cap. 1, nível de mecanismo).

Caveats do dicionário mínimo (declarados): brinquedo dust+Λ sem
radiação; **sem perturbações de matéria** (limitação de todo o
programa — o acoplamento da banda ao setor de matéria perturbada não
foi medido); lnA em base comóvel (comparações relativas); uma célula
(β₁=1) como representante com universalidade estabelecida em
β₁∈[1,4.47]; k-grid finito; janela Λ real ~0.7 e-fold (sensibilidade
~linear em ΔN).

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Curva lnA_parcial(kh_hoje); B_max=+1.88 | 2b (fundo β₁=1; BASE ✓) |
| C_ent = −0.78: nenhuma amplificação na janela matéria (5 braços) | 2b (NULL unilateral ✓) |
| Chave f_bi (liga/desliga da banda) | **2b** (matéria/pré-rolagem/Λ — três regimes medidos) |
| Aditividade restaurada pós-burn-in | 2b (validação da correção) |
| "LSS ileso na entrada" | 2b no brinquedo; caveat: sem perturbações de matéria acopladas |
| Dano total ≤ ×6.6 em escalas ~horizonte | 2b no dicionário mínimo (caveats §3) |
| Confronto fino com vínculos ISW/baixo-ℓ e literatura (Comelli/Könnig/Akrami) | pendente — nível paper, com o autor |

## 5. Fila

- **R-4 COMPLETO** (a: mapa; b: forma/lnA; c: confronto). O enunciado
  §3 é o candidato final para o cap. 07.
- **F-b** (próximo da trilha de cálculo): normalização canônica
  simplética por ponto — decide H-CONSTRAINT/H-NORM/H-SC (o fantasma),
  com o F-a como "antes" do par. Único item de cálculo restante antes
  do enunciado final do setor escalar.
- Nível paper (com o autor): confronto fino ISW/baixo-ℓ; comparação
  quantitativa com a instabilidade de gradiente da literatura; a
  fresta μ=0.1 e a rota de Akrami (tensão anotada desde a R-1).
- Sub-estruturas abertas (não bloqueiam): anomalia IR do pousado;
  par E_f cedo.
