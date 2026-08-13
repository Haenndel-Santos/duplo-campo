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

- **A1 (mecanismo):** **[CORRIGIDO — 2026-08-13, R-9 (Bloco 0),
  item (c)]** a razão medida aqui era **a razão errada**. `W/K`
  **não é a frequência efetiva do sistema**: o integrador resolve
  `K q̈ + (K̇ + C − Cᵀ) q̇ + (Ċ + W) q = 0`, logo a frequência efetiva
  é `(Ċ + W)/K`, e o `W/K` do r7e **omite o Ċ**. Medido diretamente,
  **16/32 entradas têm `W/K < 0` e `(Ċ+W)/K > 0`** — ou seja **todas
  as entradas do modo métrico**, nos dois fundos, em todas as épocas;
  em a = 200, `W/K` = −1.5e5 H² contra `(Ċ+W)/K` = **+514 H²**. **A
  frequência efetiva é positiva.** O discriminador de frequência
  concorda: se `|W/K|` fosse a frequência haveria ~110 cruzamentos de
  zero na janela, e medem-se **6** em a = 200, contra 6.5 previstos
  por WKB a partir da frequência correta.
  *O texto original desta linha dizia:* "ω²(Ẽ) = W/K é **negativo** na
  janela inteira e varia 5 ordens de magnitude (−1e2 → −1e7 em
  kh=10)" — **a medida está certa; a identificação dela com ω², não.**
  **A leitura de artefato de envelope se mantém, agora com a
  explicação correta:** o envelope do r7e usava aquela razão como
  ω²(t) no denominador, e a variação dela fabricava "crescimento" sem
  o campo crescer. Mesma classe de artefato de normalização que
  derrubou R-2 e F-b; desta vez o gate pré-declarado segurou a
  leitura. Fonte: `docs/resultado_r9_bloco0.md` §1 (V-SINAL e
  V-FREQ).
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

---

> **[NOTA — 2026-08-13, pós-R-9/R-10a/R-11/R-12: o A1, o prior e o
> desfecho]** O R-9 (Bloco 0) registrou que o **A1** — o teste de
> instabilidade de gradiente do Bloco 1 — passava a partir dali de um
> **prior favorável**: `c_s² > 0` em todos os pontos então testados do
> benchmark β-constante, com o espectador δφ₋ calibrando em 1.0000
> (`docs/resultado_r9_bloco0.md` §2). O registro fica, com o
> desenlace: **o prior não se confirmou.**
>
> O A1 rodou no mesmo dia (`docs/resultado_r10a_gradiente.md`) e
> encontrou **c_s² < 0 em todo o regime r → 0** — a instabilidade de
> gradiente do ramo finito que Könnig–Akrami–Amendola–Motta–Solomon
> ([arXiv:1407.4331]) prevêem **se reproduz na nossa implementação**.
> O R-11 elevou o achado a **NO-GO DE CLASSE POR GRADIENTE** (108/108
> células da forma-β, zero com sinal positivo) e o R-12, com
> instrumento limpo, fixou o valor: **c_s² = −1 exato** em r → 0,
> **+1 exato** na era tardia, com troca de sinal em **a_cross = 0.578
> ⟹ z_cross = 0.61** — isto é, a era instável **cobre a
> recombinação**. Ver `docs/resultado_r10_consolidado.md` e
> `docs/resultado_r12_instrumento_e_cs2.md`.
>
> **O que isto faz com este documento.** Os itens 1–4 do §6 —
> estrutura de vínculos válida, nenhuma direção cinética negativa,
> decaimento da dinâmica métrica — **continuam de pé nos regimes
> medidos**, e o Erratum-03 confirma que o domínio do R-7
> (a ∈ [100, 8e4], kh ≤ 45) é **seguro** quanto ao instrumento:
> desvio ≤ 4e−4 e os sinais de (λK₂¹, λK₂², W00) inalterados
> (`docs/resultado_r12_instrumento_e_cs2.md` §6). O que **não** se
> sustenta como escrita é a **"Consequência"** acima: toda a cascata
> R-7 rodou em a ∈ [100, 8e4], que nesta família é a **era tardia**
> (r = r_∞), e os gates aqui usados são **cegos a instabilidade de
> gradiente por construção**
> (`docs/pareceres_especialistas/00_sintese_cruzada.md` §2). O
> "TODOS os regimes que o sustentavam" era literalmente verdadeiro e
> materialmente enganoso — a < 100 nunca foi testado aqui
> (`docs/resultado_r10a_gradiente.md` §3). A viabilidade da F1
> **não** é, portanto, pergunta exclusivamente observacional: o setor
> métrico tem um problema teórico aberto em alto redshift.
