# R-7e/f — Saúde Interna Completa do Setor Escalar 2-DOF: Fase B Sã, No-Go de Classe Retirado

**Data:** 2026-08-12. Scripts: `auditoria/code/r7e_faseB_2dof.py`,
`r7e_autopsia_janela.py`, `r7f_scan_classe_2dof.py` (saídas em
`out/`). Contexto: `erratum_02_reducao_numerica.md` +
`resultado_r7_cascata.md`. Este doc fecha a pergunta de saúde interna
que restava após a cascata R-7a–d e **corrige, com razão declarada, o
veredito impresso da autópsia** (precedente: `resultado_r2_fantasma.md`
— o doc corrige o veredito do script quando a regra codificada é mais
cega que os números).

---

## 1. R-7e — a janela de deslocamento (regime não-fatorado)

Trajetória REF (g=2, m30, v*=1), fundo Heun (âncoras conferem;
M0 = 3.1e-4 — melhora só 3× sobre Euler, cadeia rp ainda 1ª ordem;
limitação declarada), janela |desl| > 0.05 = a ∈ [225, 7086]
(max 0.476), modos kh_janela ∈ {10, 3, 1, 0.3}, V-XREP OK.

**Estrutura (o resultado firme, direto do r7e):**

- **W00 sem NENHUMA troca de sinal** em 4/4 modos, trilha inteira e
  janela — a eliminação de Ψ_f (o vínculo secundário que remove o BD)
  **sobrevive ao deslocamento ordem-1 dos ramos**. Sem FJ-quebra.
- cond(W_XX) ≤ 3.4e5; **zero autovalores cinéticos negativos**
  (4×14000 pontos).

O par de vínculos de Hassan–Rosen aguenta o regime não-fatorado — a
possibilidade estruturalmente mais perigosa da Fase B está descartada
por medida direta.

## 2. A autópsia — as taxas +1.8…+11.6H eram artefato de envelope

O r7e mediu taxas de envelope grandes na janela e o gate SUSPEITO
disparou (como devia). A autópsia decidiu:

- **A1 (mecanismo):** ω²(Ẽ) = W/K é **negativo** na janela inteira e
  varia 5 ordens de magnitude (−1e2 → −1e7 em kh=10). O envelope do
  r7e usava ω²(t) no denominador — a variação fabricava "crescimento"
  sem o campo crescer. Mesma classe de artefato de normalização que
  derrubou R-2 e F-b; desta vez o gate pré-declarado segurou a
  leitura.
- **A2 (ganho de campo, normalização congelada):** G_win através da
  janela:
  | modo | G_win(Ẽ) | G_win(δχ) |
  |---|---|---|
  | kh=10 | −10.2 | −0.51 |
  | kh=3 | −10.7 | −6.0…+0.01 |
  | kh=1 | −10.0…−6.5 | −3.6…−2.7 |
  | kh=0.3 | −8.1…−3.6 | **+0.36…+0.39** |
  O escalar métrico **decai fortemente através da janela** em todos
  os modos. δχ fica entre decaimento e um transiente ≤ e^{+0.4}.
- **A4 (halving):** kh=0.3 — o único modo com G_win > 0 — passou
  (0.115 < 0.3). kh=10 falhou na resolução 14000/7000 (0.687), e a
  1ª versão deste doc fechava por argumento de teto (G_win = −0.51
  com pior caso +0.18 < +0.5). **[ATUALIZADO, mesma data, pós-review]**
  A rodada fina exigida pelo review foi executada
  (`r7e_halving_fino.py`, NPTS 28000/14000): **dG = 0.191 < 0.3 OK**,
  G_win(kh=10) = −0.54 (Ẽ: −10.4). O gate A4 agora passa em todos os
  modos com critério pleno — o veredito não depende mais do argumento
  de teto.

**Veredito: ARTEFATO-DE-ENVELOPE + FASE-B-SÃ (A4 pleno).**

## 3. O transiente δχ ≤ e^{0.4} é física conhecida — e sã

Os cruzamentos de zero de ω²(δχ) na janela (kh=1: 2; kh=0.3: 1) são o
trânsito de sinal de U″ durante a rolagem (χ: 0 → v com U″(0) < 0 →
U″(v) > 0): **a instabilidade de condensação da Fase A**, que já se
sabia autocurável ("δφ₋-dominada e sara ao assentar"). No sistema
corrigido ela é medida: transiente limitado (≤ e^{0.4} no IR
profundo), sem contaminação métrica (Ẽ decai junto), decaimento
pós-pouso em tudo (−0.7…−2.5 H).

**O σ/H ≈ 13.08 da Fase B antiga está encerrado:** era QEP congelado
(inválido como veredito dinâmico desde o D-2) sobre o sistema espúrio
de 3 DOFs (erratum-02), lido com normalização variável (a armadilha
de envelope agora instrumentada). A medida de campo corrigida dá
G ≤ +0.4.

## 4. R-7f — o no-go de classe retirado

Scan de assinatura: μ ∈ {0.3, 1, 3, 10} × β₁ ∈ {0.6, 1, 2.2, 4.47}
(REF) + fresta (μ=0.1, β₁=0.2, β₂=−1.0) + μ=0.1 REF (sem fundo
válido, como no antigo); 3 épocas × 3 kh por célula, redução
corrigida, G1 < 1e-10.

**Zero violações** — nenhum autovalor de K₂ ≤ 0, nenhuma
instabilidade de W00, em todas as células válidas. Inclusive a fresta
μ=0.1, que hospedava o "fantasma quase-nulo" (lapso Φ_f) do no-go
antigo. **O sweep de ~1500 pontos media o sistema espúrio.**

## 5. Sensibilidade de fundo (A5/E3) — nota honesta

Fundos Heun vs Euler diferem ~2e-3 na janela (r, χ, H). O lnA de
passagem do pousado, que cruza a janela, herda ±O(1) por essa via
(E3: dif 1.39 no braço a_cross=4000). **Não afeta BANDA-MORTA**
(margens de 10+ unidades log em 8/8 épocas), mas os valores da tabela
do R-7c carregam ±O(1) de sistemática de integrador de fundo.
Housekeeping na fila: fundo com integrador de ordem ≥ 2 completo
(a cadeia rp do Heun atual ainda é 1ª ordem — M0 3e-4).

## 6. ENUNCIADO DE SAÚDE INTERNA (o deliverable; insumo do cap. 07 v2 e do R-8)

No sistema físico de 2 DOFs escalares (redução corrigida, V-XREP):

1. **Estrutura de vínculos válida em todos os regimes testados** —
   benchmarks estáticos (R-7a), classe β-constante ampla (R-7f,
   incl. fresta), trajetória completa de rolagem/pouso incl. janela
   de deslocamento ordem-1 (R-7e). Sem BD, sem FJ-quebra.
2. **Nenhuma direção cinética negativa em lugar nenhum** (≈ 2×24k +
   8×14k + 4×14k pontos + 17 células × 9 amostras).
3. **Toda a dinâmica métrica escalar DECAI em todos os regimes**;
   única exceção: transiente δχ limitado (≤ e^{0.4}), autocurável,
   no IR profundo durante a rolagem — física de condensação já
   conhecida da Fase A, agora quantificada e sã.
4. Pendências declaradas: ramo algébrico (deferido — porte do arranjo
   da investigacao1; prior de artefato, sem afirmação);
   fronteira da trajetória (uma REF, como a Fase B original);
   scan de classe é de assinatura (3×3 por célula).

**Consequência:** o "no-go do setor escalar da F1" está revogado em
TODOS os regimes que o sustentavam. A viabilidade da F1 é, a partir
daqui, uma pergunta exclusivamente observacional — R-8
(`docs/r8_dicionario_epocas_opcoes.md`, recomendação C → A).
