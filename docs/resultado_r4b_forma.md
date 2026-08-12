# R-4b — A Forma da Banda e o lnA de Passagem por Modo — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r4b_forma_da_banda.py`
(saída em `auditoria/code/out/r4b_forma_da_banda.txt`). Execução:
autor (.venv). Bloco 2 do R-4 — entrega os insumos quantitativos do
confronto observacional (bloco 3, com o autor).

**Portões:** R4b-NULL **PASSA** (GR, passagem completa kh 20→0.2:
lnA = **−4.33** — dilui líquido); R4b-AUTOSIM **PASSA**
(|lnA(k)−lnA(3k)| = 0.33 < 0.5 — auto-similaridade em fundo estático
confirmada: uma medida por fundo vale para todo k). negK=1 em todas
as âncoras de todos os braços (silencioso = 1 por desenho).

---

## 1. O número central: amplificação de passagem universal

lnA de passagem (Δln|y_met| entre kh=20 e kh=0.2, máx. sobre ICs
métricas):

| fundo | lnA_passagem | fator em amplitude |
|---|---|---|
| GR (null) | **−4.33** | ×0.013 |
| β-const β₁=1 | **+3.97** (k×3: +3.64) | ×53 (×38) |
| β-const β₁=4.47 | **+3.62** | ×37 |

**Cada modo métrico da classe ganha ~e^{3.6–4.0} ≈ 40–55× em
amplitude ao atravessar a banda — independente de β₁ e de k** (nas
esquinas testadas). Contraste líquido contra o GR no MESMO
instrumento: e^{~8} em amplitude (~10⁷ em potência).

**Caveat de fronteira (declarado):** [20→0.2] é um **limite
inferior** por modo — a janela kh40–20 já cresce (+2.7 a +4.1,
componente E_f), e o R-4a viu ~nada em kh≳70. A banda completa
(kh ~ 50→0.3) adiciona ~+2–3 ao total por modo (≈ e^{6–7}). O corte
em 20 foi deliberado (excluir o transiente de IC); refinamento é uma
rerodada trivial se o bloco observacional precisar.

## 2. A forma: rajadas com rotação de componentes — e o que NÃO ler

1. **Os máximos por janela sobrecontam.** Σ(metMAX×ΔN) das janelas da
   passagem dá ~8.7 para β₁=1 — mais que o dobro da passagem líquida
   (+3.97). Causa visível nas tabelas: o crescimento alterna entre o
   par E_f e o par Ψ_f janela a janela (rotação de componentes) — o
   máximo por janela captura sempre o par da vez. **A estatística
   robusta por modo é a passagem líquida por IC**, não a soma de
   janelas.
2. **O próprio GR tem positivos de janela** (até +1.25 em kh 6–4, o
   freeze-out do espectador massivo) com passagem líquida −4.33.
   Janela-positiva isolada não distingue nada; líquido distingue.
3. A estrutura grossa confirma o R-4a: crescimento de kh~40 até
   kh~0.5–0.7, componente E_f dominando kh alto, Ψ_f perto do
   cruzamento; abaixo de kh~0.45 as janelas ficam ruidosas/alternadas
   (rotação profunda no super-horizonte) com líquido ~0/negativo.

## 3. Pousado: a época de cruzamento modula a banda

| a_cross | época | lnA_passagem |
|---|---|---|
| 500 | pré-rolagem (U₀ domina) | **−0.21** |
| 1000 | início da rolagem | +3.26 |
| 1600 | meio da rolagem | **+1.57** |
| 2500 | anel inicial | +3.17 |
| 4000 | anel/pouso | **+4.80** |
| 8000 | pousado | +4.03 |
| 15000 | pousado profundo | +4.52 |
| 30000 | (passagem incompleta no range) | — |

- **Supressão pré/durante a condensação** (−0.2 a +3.3; vale médio
  +1.6): leitura mecânica (nível 3, nomeada): a amplificação
  acompanha a **fração bimétrica do orçamento de energia** — na
  pré-rolagem U₀ responde por ~95% de H² e o setor de interação é
  espectador; ainda assim −0.21 fica ~4 e-folds ACIMA do GR (−4.33) —
  supressão parcial, não desligamento.
- **Realce no anel** (+4.80 em a_cross=4000) e bursts época-fixos
  gigantes nas janelas que caem sobre o anel (+8.8, +11.4 em janelas
  de a∈[3700,6100]) — a componente de anel do R-3b reaparece aqui
  como modulação aditiva sobre a banda.
- Pousado profundo converge para ~+4.0–4.5 ≈ estático 4.47 + resíduo
  de anel ✓ (herança do ponto da classe, consistente com R-3c).

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| lnA_passagem ≈ +3.6–4.0 universal (β₁, k) nos estáticos | 2b (AUTOSIM ✓; esquinas β₁={1,4.47}) |
| GR no mesmo instrumento: −4.33 (contraste e^~8) | 2b |
| Máximos por janela sobrecontam (rotação de componentes) | 2b (demonstrado: Σjanelas ≈ 2× líquido) |
| Passagem [20→0.2] é limite inferior (banda vai a kh~50) | 2b (kh40-20 medido; total ≈ e^{6–7} estimado) |
| Modulação por época no pousado (supressão pré; realce no anel) | 2b (tabela); leitura por fração bimétrica: nível 3 |
| lnA em base comóvel | caveat herdado — comparações RELATIVAS |

## 5. Fila

- **Bloco 3 do R-4 (DECISÃO DO AUTOR):** o dicionário de épocas —
  mapear o modelo-brinquedo (RHO0=0.3, H~1, a admensional) na
  história cósmica real para confrontar e^lnA com vínculos
  (Comelli/Könnig; rota de escape de Akrami; a fresta μ=0.1 do R-1).
  Os insumos estão prontos: forma da banda + lnA por modo/época.
- **Gate F-a** (próximo script da trilha, não bloqueado pelo autor):
  a constraint secundária linearizada — decide se a direção K<0 é
  vínculo disfarçado (H-CONSTRAINT), com a evidência acumulada agora
  incluindo negK=1 universal até a=70000.
- Anomalia IR do pousado (k=1250): segue aberta, fora do quadro.
- Enunciado do cap. 07: o rascunho do R-4a §4 ganha os números deste
  doc (e^{3.6–4.0} por modo, e^{6–7} com a banda completa).
