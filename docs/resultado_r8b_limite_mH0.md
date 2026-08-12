# R-8b — m_T/H₀ Está Cravado (~2.3–2.4) pelo Fundo: o Postulado 30–300 H₀ é Inalcançável na Família do Benchmark

**Data:** 2026-08-12. Script: `auditoria/code/r8b_limite_mH0.py`
(saída oficial em `out/`; rodadas intermediárias no histórico —
ensinaram o fold e os fixes do solver). Contexto: alavanca
identificada no R-8a (`resultado_r8a_quase_estatico.md` §3.2);
decisão executada: **m/H₀ tratado como livre, limite derivado** —
o confronto com o postulado virou resultado.

## 1. A família (o dial)

β_n → s·β_n (escala da interação, forma-β preservada) + U0 (vácuo do
χ) resolvido por s para manter o H tardio do benchmark (mesma
história de expansão; Ω_m(a₀)=0.3 define "hoje"). A álgebra fecha no
MESMO cúbico do fundo com ρ̃ → (ρ_m+U0)/(s·m_eff²). Raízes por
continuação (a seleção cega "menor raiz positiva" quebra com ρ̃<0).
m_T pela fórmula do projeto (derivations/02, caixa), avaliada em a₀.

## 2. Os dois resultados

**(a) O fold — obstrução estrutural.** `r²V_f(r) = β₄r²+3β₂+β₁/r`
tem **mínimo positivo** (0.3 em r=1) na forma-β do benchmark
(1, −0.4, 0.5-escalada). Como H*² = s·m_eff²·r²V_f/(3μ) está fixo, a
família **dobra em s ≈ 5.7**: para s ≥ 6 não existe U0 com o H
tardio alvo (g_borda > 0 na borda de existência). Verificado
numericamente (tabela) e analiticamente (s_max = 3μH*²/(0.3·m_eff²)
≈ 6.2).

**(b) A massa é PREVISÃO, não parâmetro.** Ao longo de TODA a família
alcançável (s = 0.25 → 5.5, todos os membros com saúde cinética OK —
gate por membro):

| s | m_T/H₀ (em a₀) | max\|μ−1\| na janela | max\|Σ−1\| |
|---|---|---|---|
| 0.25 | 2.33 | 0.000004 | 0.000004 |
| 1.0 | 2.26 | 0.00001 | 0.00001 |
| 2.0 | 2.30 | 0.00003 | 0.00004 |
| 4.0 | 2.41 | 0.00006 | 0.00008 |
| 5.5 | 2.36 | 0.00009 | 0.00012 |

**m_T/H₀ ∈ [2.26, 2.41]** — a razão m_T²/H² é função só de r ao
longo da família de H fixo, e é plana no alcance. (Nota de época:
m_T/H é função de a — ~2.3 em a₀, ~3.5 no Λ profundo; os docs devem
citar a época.)

Janela observacional (z ≤ 1, k = 0.05–0.15 h/Mpc ⟺ kh ~ 90–450,
toda QS-confiável): desvios ≤ 0.012% — **o crescimento é
trivialmente satisfeito em toda a família**; os limites adotados
(|μ−1| ≤ 0.15, |Σ−1| ≤ 0.10; referências de ordem de grandeza,
declaradas) nunca são atingidos. V-CONSIST (s=1 vs R-8a): OK
(1.000016). Correção herdada: o Ub bimétrico agora subtrai ρ_m
(o R-8a não subtraía; efeito ≤ 0.1%, só era de matéria — anotado
no doc do R-8a).

## 3. Leitura

1. **O postulado m ~ 30–300 H₀ do corpus é INALCANÇÁVEL na família
   do benchmark** — não por dados, mas por existência de fundo
   (fold). Alcançá-lo exige outra forma-β (V_f com zero em r finito,
   i.e., 3|β₂| grande o bastante) — **uma escolha estrutural nova, a
   declarar na v2**, que além disso implica o ajuste fino U0 < 0
   (vácuo-χ cancelando a energia da interação).
2. **Na família do benchmark, m_T ≈ 2.3 H₀ é uma predição.** A
   física bimétrica vive no quase-horizonte — convergindo com o
   R-8a: o teste decisivo é o R-8 completo (kh ≲ 22: baixo-ℓ, ISW,
   Gpc), não o crescimento.
3. O limite observacional de crescimento sobre m_T/H₀ ficou MOOT
   nesta família (o fold chega primeiro); ele voltaria a operar numa
   família com V_f-zero — insumo para quando/se essa escolha for
   feita.

## 4. Fronteiras declaradas

Forma-β do benchmark sob rescala uniforme (o dial canônico que
preserva a classe); ramo conectado ao benchmark (continuação de
raízes); saúde por membro = gate de assinatura (3 épocas × 2 kh);
limites observacionais adotados como referência de ordem de grandeza
(confronto fino com likelihoods = nível paper); m_T avaliada em a₀
pela fórmula do projeto.
