# Investigação 2 — Fase A: o Fundo de Rolagem — Resultado

**Data:** 2026-08-11. Script: `auditoria/code/investigacao2_fundo_rolagem.py`
(saída em `auditoria/code/out/investigacao2_fundo_rolagem.txt`; duas
rodadas — a primeira, janela curta, motivou o endurecimento dos
critérios registrado no cabeçalho do script). Primeiro contato do
programa com o regime p_φ≠0 (constraint não-fatorada) — a saída nº 5 do
veredito e o caminho para o teste de R2.

---

## 1. Placar

| Critério | Resultado |
|---|---|
| G2a-SIMB (2a) — fatoração e resíduo simbólicos | **PASSA** (resíduo em H=rH_f é exatamente −m²M_eff²a³χ̇β₁′; controle negativo detecta) |
| G2a-CONTROLE (2b) — âncora r(a=10)=0.332259 + halving | **PASSA** (1.2e-7) |
| G2a-EXISTE (2b) | **PASSA** — 7/8 trajetórias completas |
| G2a-CONDENSA (2b) | **PASSA** — 3/7 completam (m_χ²∈{10,30}) |
| G2a-PREVISAO (poder) | **FALHOU como codificado; limiar confirmado na releitura** — ver §3 |
| G2a-DESLOCA (poder) | **PASSA** — \|desl\| até **0.48** (ordem 1) durante condensação completa |
| G2a-POUSO (2b) | **PASSA** — todas as rodadas ok com pouso <1e-2 (melhor caso: 4.8e-5) |

## 2. O arco da condensação (g=2, m_χ²=30, v*=1, célula REF μ=1)

| a | r | ξ | χ/v | \|H−rH_f\|/H | fase |
|---|---|---|---|---|---|
| 0.01–1 | 0.00→0.03 | ≈r | 0.001 | ~1e-9 | matéria; U₀ prende r baixo |
| ~100–900 | 0.03→0.05 | ≈r | 0.01→0.49 | 1e-3→0.29 | **rolagem: sai dos ramos** |
| ~1800 | 0.24 | 0.75 | 0.91 | **0.45** | pico do regime não-fatorado |
| ~3500–5e4 | 0.47–0.50 | oscila | 0.93 | ±0.17→±0.001 | oscilações + pouso |
| 1e5 | 0.4979 | 0.5013 | 0.932 | 6e-5 | **pousou no ramo finito** |

**Três fatos estruturais:**

1. **A transição estrutural é dirigida pela condensação: r salta de
   0.031 para 0.498 (×16).** Pré-rolagem, U₀=μ₋²v²/4=15 domina como
   energia de vácuo e comprime r; a condensação converte essa energia
   em β₁eff (1→4.47) e em separação estrutural. É o primeiro fundo do
   programa em que a bifurcação de φ₋ **produz** a evolução de r — a
   narrativa do Cap.1 da v1 realizada dinamicamente (com a saúde do
   setor escalar ainda em aberto — é a Fase B).
2. **O regime não-fatorado é genuíno e de ordem 1**: no pico,
   \|H−rH_f\|/H ≈ 0.45 com B(r)≈4 — longe de ambos os ramos. Não é
   perturbação da estrutura fatorada; é outra estrutura.
3. **O pouso é limpo e é o previsto**: χ̇→0 devolve a trajetória ao
   ramo finito (deslocamento final 6e-5), com χ* dado pela
   estacionariedade. **Conferência quantitativa pós-hoc:** o mínimo
   efetivo previsto, χ*²/v² = 1 − Δ(fim)/μ₋² com
   Δ(fim)=2m²M_eff²b1₀(ξ+3r)_fim/v*² = 1.995, dá χ*/v = 0.931;
   o observado é 0.932.

## 3. O achado da fase: a interação HR resiste à condensação

A fonte da EOM de χ perto da origem é linear em χ:
$$-m^2M_{\rm eff}^2\beta_1'(\chi)(\xi+3r) = -\underbrace{\frac{2m^2M_{\rm eff}^2 b_1^0(\xi+3r)}{v_*^2}}_{\Delta}\,\chi$$

ou seja, a interação **soma Δ à massa² da origem** — o mesmo termo que
produz a separação estrutural penaliza energeticamente ⟨φ₋⟩≠0. Limiar
(célula REF, v*=1): **m_χ² ≳ 2.7**.

**A varredura confirmou o limiar dos dois lados — mas o critério
codificado errou de alvo, e o registro disso importa:**

- m_χ²=0.3 (2 rodadas): origem **estável**, campo congelado ✓;
- m_χ²=10, 30 (3 rodadas ok): origem instável, **condensação
  completa** ✓;
- m_χ²=3 (2 rodadas): origem instável e o campo **está rolando**
  (χ/v: 0.001→0.039 e 0.050, crescendo no corte) — mas a margem
  m_χ²−m_crit≈0.3 dá rolagem de ~80 e-folds, maior que a janela
  (a≤1e5). O critério `condensou = |χ/v|>0.5` classificou como "não",
  gerando o FALHA formal.

**Reclassificação (declarada como pós-hoc):** o que o limiar prevê é
a **estabilidade da origem**, não a conclusão da condensação dentro de
uma janela arbitrária. Nesse critério — o correto — a previsão acerta
**8/8**. Fica registrado que o critério pré-declarado era defeituoso
(conflacionava as duas coisas) e que a correção foi feita na leitura,
não no número.

**Consequência física (nível 2b nesta célula):** a bifurcação de φ₋
não é livre — compete com a back-reaction do setor gravitacional. Isso
adiciona um vínculo de design a qualquer realização da narrativa TDCP:
o potencial precisa vencer Δ, e Δ cresce com a própria separação
estrutural ((ξ+3r) cresce com r).

## 4. Pendências e avisos desta fase

1. **Abort de g=1, m_χ²=30** ("raiz perdida" em a=15.5, durante
   overshoot χ/v=1.06, desl=−0.60): **indeterminado** — pode ser
   numérico (janela do root-finder no balanço mais violento) ou
   genuíno (a secundária não-fatorada perde solução real — o fundo de
   rolagem deixar de existir seria um resultado). O análogo g=2
   completou; a Fase B não depende deste caso, mas ele deve ser
   revisitado se a Fase B promover o regime.
2. **Adiabaticidade na janela-alvo: até ~2.4** (e maior nas
   oscilações tardias, onde o indicador diverge nos pontos de
   retorno de χ̇). A Fase B **não pode** usar ponto congelado como
   juiz: o método é o rastreio denso com leitura de tendência
   (`evolucao_temporal_escalar.py`), com a adiabaticidade impressa
   ponto a ponto e k≫H como região confiável.
3. O integrador é Euler explícito com validação (âncora + halving
   1.2e-7) — adequado para existência/estrutura; a Fase B reusa as
   trajetórias mas qualquer afirmação de precisão fina exigiria
   upgrade declarado.

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Resíduo da secundária = −m²M_eff²a³χ̇β₁′ (coeficiente e sinal) | **2a** (simbólico, duas verificações + controle negativo) |
| Fundo de rolagem existe, desloca ordem-1 e pousa no ramo finito | 2b (célula REF μ=1, knobs varridos declarados) |
| Limiar de condensação Δ e sua confirmação | 2b (com a reclassificação do §3 declarada) |
| χ* pela estacionariedade (previsto 0.931 vs 0.932) | 2b (conferência pós-hoc, um caso) |
| "r dirigido pela condensação = narrativa da bifurcação" | **3** (interpretativa, rotulada; a saúde escalar decide se sobrevive) |

## 6. Fase B — o que ela é, agora com alvo concreto

Perturbações (QEP 7×7 com χ̇≠0, F′≠0 via fatias por coeficiente) ao
longo da trajetória g=2/m_χ²=30, **janela-alvo a∈[~760, ~2050]**
(deslocamento ≥50% do pico), k=1 e 10, com:

- contagem de modos (o teste barato do fantasma BD: 3→4 modos finitos
  no regime não-fatorado = BD de volta — falsificação do Gate 2 Parte
  B por rota numérica, com o caveat de cegueira declarado no
  `gate2_ghost.md` §4: 10 modos falsifica; 9 não certifica);
- saúde σ E kN ao longo da janela (leitura de tendência, não juiz
  pontual);
- **o diagnóstico do balanço rI da C1** ponto a ponto: p_φ≠0 muda o
  lado EH do balanço quebra×EH — a pergunta central é se o balanço se
  move qualitativamente no regime não-fatorado.

Critérios pré-declarados ficam para o script da Fase B.
