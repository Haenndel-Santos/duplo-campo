# R-8a — μ, Σ, η Quase-Estáticos: Alvo Subpercentual no Sub-Horizonte; a Janela Quase-Horizonte é o Alvo do R-8 Completo

**Data:** 2026-08-12. Script: `auditoria/code/r8a_quase_estatico_mu_sigma.py`
(saída oficial em `out/`; 1ª rodada no histórico git — ensinou o
modelo de erro QS). Contexto: opção C de
`docs/r8_dicionario_epocas_opcoes.md`, sobre o sistema 2-DOF são
(`resultado_r7e_saude_interna.md`).

## 1. O método (o que o torna limpo)

- **Gauge Newtoniano no setor g** (lib nativa): os potenciais de
  crescimento (Φ, de g₀₀) e lensing ((Φ+Ψ)/2) são lidos direto.
- **Resposta quase-estática**: q* = W⁻¹J, fonte unitária na linha de
  Φ_g (densidade de dust; T^ij = 0). Termos K/C e massa-ρ̄ caem como
  (aH/k)² — descartados **nos dois ramos**.
- **μ e Σ como razões bimétrico/GR** com a mesma fonte e o mesmo
  fundo H(a) (ramo GR: EH+χ com Ub = 3H²−ρ̄ fazendo o papel de Λ):
  toda convenção e normalização **cancela**.

Gates: **V-GR-ETA v2** — η_GR−1 = C/kh² com C ≈ 9.2 (resíduo 6.5%;
fit em kh≥10): é a física subdominante QS da equação de traço
(termos H², Ḣ), medida e usada para **definir a região QS-confiável
kh ≥ 22** (erro < 2%). **V-IR-MASSA** — μ(kh=300)−1 = 6.7e-5 ✓ (o
setor massivo desliga em k ≫ m). Expoente de queda: |μ−1| ∝ kh^−1.86
≈ kh^−2 — o termo líder (m·a/k)² está presente, sem cancelamento.

## 2. Resultado

**Correção pós-review (2026-08-12):** o "a_eq ≈ 0.84" impresso pelo
script estava ERRADO (estimativa grosseira hard-coded; o próprio
output mostra ρ ≠ Λ_eff ali). Valores corretos da igualdade
ρ_m = ρ_Λ = 3H*²: **a_eq = 0.686** (β₁=1) e **a_eq = 0.429**
(β₁=4.47) — dependem do fundo. O grid a = 0.1…75000 cobre as duas
eras nos dois casos; a rotulagem de época nas tabelas deve usar
esses valores. (A física das tabelas μ/Σ não usa a_eq — era rótulo
interpretativo; script corrigido para runs futuras.)

Na **região QS-confiável (kh ≥ 22)**, nas duas eras e nos dois
fundos (β₁ = 1, 4.47):

| | máximo |
|---|---|
| \|μ−1\| | 0.66% (a=0.1, kh=30; cai como kh⁻²) |
| \|Σ−1\| | 0.66% (idem) |
| em kh ≥ 100 | ≤ 0.06% |

**Precisão (fraseado honesto, pós-review):** o piso de erro da
própria sonda QS na fronteira da região confiável é ~2% (por
construção de kh_QS). O enunciado FORTE deste resultado é portanto
"**nenhum desvio acima do piso QS foi detectado**" — os 0.66% são o
valor central computado, não uma previsão de precisão; a previsão
fina do desvio sub-horizonte exige o tratamento dinâmico (ou QS de
ordem seguinte).

Nenhum ponto singular (sem ressonâncias no grid). Desvios **crescem
para a era de matéria** (r pequeno → setor-f responde mais) e caem
como kh⁻² — assinatura padrão de gravidade massiva sub-Compton.

**Fora da região confiável (kh ≲ 22)** os números crus chegam a 17%
(a=0.1, kh=5) — mas ali a própria série QS está a ~50% e **nada se
afirma**: a janela quase-horizonte fica INDECIDIDA por esta sonda.

## 3. Leitura (enunciado v1 do confronto observacional)

1. **ALVO-SUBPERCENTUAL no sub-horizonte profundo**: no benchmark, o
   setor escalar da F1 é indistinguível de GR (< 1%) em todas as
   escalas kh ≥ 22 — que, via kh = k/aH (adimensional,
   independente do dicionário), cobre TODA a janela de
   crescimento/lensing observável (RSD, cisalhamento: k ≳ 0.01
   h/Mpc ⟺ kh ≳ 30 hoje). *No benchmark, a F1 passa
   trivialmente pelos vínculos de crescimento.*
2. **A alavanca do dicionário**: o desvio escala como
   (m/aH)²/kh²-estrutura. O benchmark tem m/H ~ 3.5; o corpus
   POSTULA m ~ 30–300 H₀. Se o dicionário adotar esse postulado, a
   escala de Compton entra na janela observável e os desvios em
   k ~ 0.1 h/Mpc deixam de ser subpercentuais — **os dados de
   crescimento viram um limite direto sobre m/H₀, confrontando o
   postulado 30–300 H₀**. Este é o item de maior alavancagem da
   decisão do dicionário (insumo 1 de
   `r8_dicionario_epocas_opcoes.md`).
3. **O alvo do R-8 completo** fica definido: a janela quase-horizonte
   kh ≲ 22 (⟺ ℓ baixo no CMB, ISW, escalas ≳ Gpc) — exatamente onde
   a sonda QS não alcança e onde o sistema dinâmico 2-DOF validado
   (R-7a) é a ferramenta certa.

## 4. Fronteiras declaradas

Benchmark β-constante (F′=F″=0); matéria só como fonte (sem termos
massa-ρ̄, válido na região confiável); unidades de código; χ̄ parado.
O mapeamento fino para (z, k físicos) e o confronto numérico com
fσ₈/RSD exigem os 4 insumos do autor (dicionário).

## 5. Fila

1. Decisão do autor: dicionário (em particular m/H₀ — item de maior
   alavancagem, ver §3.2).
2. R-8b (com a decisão): confronto μ(a,k) vs vínculos de crescimento
   reais + limite sobre m/H₀.
3. R-8 completo (dinâmico): a janela kh ≲ 22 + C_ℓ de baixo-ℓ.
