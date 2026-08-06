# Auditoria — Lote 11 (final): Anexos I, J, K e L (38 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AI.md, AJ.md, AK.md` (`../code/aplica_vereditos_lote11.py`).
O Anexo L não tem equações em destaque (0) — é prosa de ponte
conceitual, nada a auditar.

**Lote final da auditoria sequencial das 856 equações do corpus.**

Território distinto de todos os anteriores: os Anexos I–K são a linha
de pesquisa exploratória (colapso de função de onda cosmológica,
emaranhamento entre domínios, energia escura de emaranhamento),
explicitamente marcados no próprio manuscrito como **não integrados ao
corpo F1**. Não são cobertos por nenhuma âncora D1–D8 — mas são
cobertos por `integration_assessment.md`, que já os avaliou
tecnicamente contra o formalismo HR+F1 (veredito: integrável apenas
parcialmente). Esse documento funciona aqui como âncora equivalente, e
esta auditoria aplica seus vereditos equação a equação.

## Estatística

| Veredito | AI | AJ | AK | Total |
|---|---|---|---|---|
| CONFERE | 8 | 5 | 6 | 19 |
| CONFERE SOB HIPÓTESE | 0 | 1 | 3 | 4 |
| NÃO-DERIVÁVEL | 1 | 3 | 6 | 10 |
| CONFLITA COM | 2 | 2 | 0 | 4 |
| **Total** | **11** | **11** | **16** | **38** |

Zero ERRO nesse lote — o que faz sentido: este material não *erra
contas*, ele **assume formas** sem derivá-las. A distribuição
(10 NÃO-DERIVÁVEL + 4 CONFLITA em 38) reflete exatamente o veredito de
integração parcial já registrado.

## Achados principais

### L1. Os três conflitos técnicos de `integration_assessment.md` estão localizados agora equação a equação

O documento de integração identificou três conflitos concretos com o
corpo F1; esta auditoria os fixou nos IDs específicos:

- **Acoplamento de matéria simétrico** — `[AI.09]`
  (E_tot=E_vac^(1)+E_vac^(2)+E_int) e `[AJ.04]` (E_tot=E1+E2+E_int):
  ambos dão energia própria aos DOIS domínios, conflitando com a
  exigência estrutural do Cap.3 §3.4 (matéria só acopla a g), da qual
  depende a contagem de graus de liberdade livre do fantasma BD
  (Cap.6). CONFLITA COM Cap.3 §3.4 nos dois.
- **L_int genérico** — `[AJ.05]`: λχ(g^(1)−g^(2))² não especifica a
  contração de índices; na leitura literal é ∝h_μνh^μν **sem** a
  subtração −(h^μ_μ)² de Fierz–Pauli, a única combinação quadrática
  que evita o sexto grau fantasma. NÃO-DERIVÁVEL, com o risco técnico
  explicitado.
- **Λ_ent aditivo sem equação de movimento** — `[AJ.07]`:
  Λ_eff=Λ_0+Λ_ent é aditivo e Λ_ent não tem dinâmica declarada, contra
  o η do corpo F1, que é multiplicativo (1/(1−η)) e tem η̇=Γχ̇².
  CONFLITA COM Anexo E/H.

### L2. NOVO — duas sobrecargas de símbolo graves, uma delas sobre a variável mais central do corpus

Achados próprios desta auditoria, não presentes em
`integration_assessment.md`:

- **`[AK.15]`**: P(k)=P_ΛCDM(k)(1+**ξ**e^{−k/k_c}) — ξ usado como
  intensidade de correlação no espectro de matéria, colidindo
  frontalmente com **ξ=N_f/N_g**, a variável estrutural central usada
  em TODAS as âncoras D1–D8 e em praticamente todo o corpo F1. É a
  mesma classe do achado E6 (lote 4, ξ reaproveitado no Cap.20), agora
  em outro anexo — a terceira ocorrência do símbolo mais sobrecarregado
  do corpus.
- **`[AK.11]`**: P(k)=P_0(k)(1+**η**sin(k/k_*)) — η como amplitude de
  modulação do espectro primordial. É o **terceiro** uso distinto de η
  no corpus: separação estrutural acumulada (Cap.1/Anexo E/H, com as
  duas leis conflitantes do achado A2) e η_slip (Cap.18) são os outros
  dois.

### L3. As previsões numéricas de K não vêm de nenhum cálculo mostrado

`[AK.04]` (|w+1|∼10⁻²–10⁻³) e `[AK.10]` (Δγ∼0.01) são apresentadas
como "previsão da TDCP", mas não são derivadas de nenhum parâmetro —
nem dos desta linha exploratória (χ, S_ent, κ), nem dos do corpo F1
(m_S0, α₀, p, q). NÃO-DERIVÁVEL nas duas. É exatamente o que
`integration_assessment.md` chama de "dois conjuntos de observáveis
paralelos, não uma previsão unificada".

### L4. O que este material tem de formalmente correto

Não é pouco: a notação de estado quântico (`[AI.01]`, `[AI.02]`,
`[AJ.02]`) é bem formada; a entropia de von Neumann `[AJ.03]`
(S=−Tr(ρlnρ)) está correta; o tempo de Planck `[AI.03]` confere
numericamente; E=mc² e sua aplicação `[AI.10]` são triviais e
corretas; a parametrização f=Ω_m^γ com γ≈0.55 (`[AK.07]`/`[AK.08]`) é
padrão e bem transcrita; e a relação de dispersão ω²=k²+m_g²
(`[AK.13]`) segue corretamente da equação de onda massiva. O problema
deste bloco nunca foi erro de conta — é ausência de derivação e
conflito estrutural com o que o corpo F1 já demonstrou.

### L5. O Anexo L faz exatamente o que deveria

Sem equações (0), o Anexo L registra apenas a reinterpretação
absorvível: "dois domínios correlacionados" já é o Cap.1 (Φ₁,Φ₂);
"energia escura como remanescente de interação" já é o ramo algébrico
+ η. E é explícito sobre o que continua fora (colapso quântico, L_int
independente, matéria em ambos os setores). Nada a auditar
matematicamente — e, do ponto de vista de controle de claims, é o
documento mais bem calibrado do corpus.

## Encerramento da auditoria sequencial

Este lote fecha a auditoria das **856 equações** do corpus TDCP
(Cap.1–26 + Anexos A–L). Distribuição global final:

| Veredito | Qtde | % |
|---|---|---|
| CONFERE | 599 | 70,0% |
| CONFERE SOB HIPÓTESE | 75 | 8,8% |
| ERRO (76) + DE CÁLCULO (27) + DE FORMULAÇÃO (12) | 115 | 13,4% |
| INCOMPLETA | 21 | 2,5% |
| NÃO-DERIVÁVEL | 20 | 2,3% |
| ARTEFATO DE CONVERSÃO | 18 | 2,1% |
| POSTULADO registrado | 4 | 0,5% |
| CONFLITA COM (isolado) | 4 | 0,5% |
| **Total** | **856** | **100%** |

Quase 79% do corpus (CONFERE + SOB HIPÓTESE) está matematicamente em
ordem. Os 13,4% de erro concentram-se de forma muito desigual: o
Cap.16 (15/28), o Cap.18 (32/48) e o cluster do "ramo dinâmico" no
Cap.14 (11 equações encadeadas) respondem sozinhos por mais da metade
de todos os erros do corpus — e quase todos derivam de três raízes
únicas já com correção fechada pelas âncoras (m_T² sem ξ / D2, ansatz
Yukawa de 1 polo / D6, constraint trocada no ramo dinâmico / D5).

Os sumários por lote estão em `auditoria/lotes/lote_01…lote_11`; a
tabela de progresso completa, no `registro_formulas.md`.
