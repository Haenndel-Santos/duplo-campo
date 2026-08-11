# Gate 1 (2ª geração) — A Identidade do Grau Relacional

**Data:** 2026-08-10. Origem: releitura conceitual do manuscrito v1
pós-veredito (usuário) + confronto com a evidência da v2. Formaliza as
hipóteses R1/R2 e o protocolo de teste, no método do
`plano_v2_reconstrucao.md` (níveis epistêmicos; critérios de falha
pré-declarados).

---

## 1. O problema

O corpus usa "modo relativo" para **quatro objetos distintos**, ligados
por interpretação, nunca por derivação:

| Objeto | O que é | Onde vive |
|---|---|---|
| Φ₋ = (Φ₁−Φ₂)/√2 | modo diferencial primordial (o que bifurca) | Cap.1–2 (ontologia) |
| φ / χ (modulador) | campo que modula β_n / F·V | Cap.3+ / anexos (v1 nunca fixou a identidade) |
| r = b/a | separação geométrica de fundo | cosmologia FLRW |
| σ / S | grau escalar propagante da deformação relativa g–f, pós-vínculos | perturbações F1 |

A cadeia narrativa Φ₋ → bifurcação → (g,f) → σ é **identificação
interpretativa**, não resultado. A v2 deu um passo além ao **decretar**
(dicionário de símbolos, decisão normativa) que o modulador é φ₋ — e
testou esse braço via β₁(φ₋): **não cura o setor escalar** (veredito
consolidado).

## 2. Hipóteses de trabalho

> **R1 — Desacoplamento entre o modo primordial e sua realização F1.**
> O no-go do setor escalar é um resultado sobre a REPRESENTAÇÃO
> (helicity-0/setor de vínculos da realização bimétrica HR-F1), não
> sobre o grau relacional primordial. Nada demonstrado até aqui exige
> que δΦ₋ e σ_HR sejam o mesmo grau de liberdade.

> **R2 — Natureza efetiva/coletiva.**
> O grau relacional primordial pode ser parâmetro de ordem/variável
> coletiva de um estado conjunto dos dois setores (𝓡); o escalar
> macroscópico seria variável efetiva (σ_eff), não campo elementar.

**Suporte já existente para R1 (nível 2b, dentro do repo):**
`estrutura_par_relativo.md` — a composição dos autovetores patológicos
é dubleto de shifts B_g±B_f (μ~1) e lapso Φ_f (μ→0), com δφ₋
desacoplado (F′=0) e SEM dominância da direção "diferença de métricas"
Ψ_f−Ψ_g. O modo que adoece é estrutural-de-vínculo — não é o portador
óbvio da memória primordial nem o δΦ₋.

## 3. O trilema da seta Φ₋ → (g,f)

Prior estrutural (nível 3 — declarado como prior, não como teorema;
dois priors de literatura já caíram por cálculo neste projeto): um
segundo spin-2 não se compõe de escalares (obstruções tipo
Weinberg–Witten; gráviton exige termo cinético próprio). Se o prior
segura, as únicas saídas são:

- **(a) f fundamental; Φ₋ = modulador.** É o braço da v2 — já
  instanciado por decreto e TESTADO: β₁(φ₋) não cura (piora).
- **(b) g e f efetivas, emergentes de 𝓡** (R2). Programa novo; conecta
  com a "condensação dinâmica" da fila (p_φ≠0, constraint não fatora).
- **(c) grau relacional sem segunda métrica** (outra classe de teoria;
  perde o setor tensorial da v2 — Higuchi automático, m_T²/H²→12).

Nota sobre a analogia de condensados (R2): o modo de fase relativa
(Josephson) em condensados acoplados pode ser gapeado OU dinamicamente
instável (contrafluxo) — a analogia organiza, não garante saúde.

## 4. Protocolo do Gate 1

### G1-a (documental; custo ~zero; nível 1)
Tabela de identidade da cadeia {Φ₋, φ, χ, φ₋-v2, σ, S, r}: cada
ocorrência no corpus classificada como *identificada-por-decreto /
distinta / indefinida*, estendendo o `dicionario_simbolos.md` com a
flag epistêmica explícita ("identificação normativa, não derivada") na
linha "φ₋ modula β_n".
**Critério:** zero ocorrências sem classificação.

### G1-b (quantitativo; barato; nível 2b) — o teste central
Com `modulacao_qep.py` (F′≠0, δφ₋ acoplado), computar a projeção
|⟨v, δφ₋⟩|² e |⟨v, direções-métricas-relativas⟩|² para TODOS os modos
(sadios e patológicos), na varredura μ ∈ {0.1, 0.3, 1, 3, 10}, no ponto
fixo, em k=1 E k=10 (regra: saúde/identidade sempre em σ E kN, dois k).
- **R1 passa** se |⟨v_patológico, δφ₋⟩|² < 0.05 em toda a varredura
  (a patologia é espectadora de δφ₋ ⇒ o grau primordial NÃO é o modo
  doente, mesmo dentro da F1).
- **R1 falha** se em algum regime o modo patológico for
  δφ₋-dominado (⇒ a doença alcança o próprio grau primordial nessa
  realização; o trilema colapsa para (b)/(c) imediatamente).

### G1-c (teórico; curto; nível 3→2a)
Nota formalizando a obstrução do trilema (§3): ou uma prova adaptada ao
contexto (sobe a 2a), ou a demolição do prior (também informação). Em
qualquer caso, o trilema vira decisão documentada, não default tácito.

## 5. Sequenciamento (não muda a fila da v2)

1. **Investigação 1 da fila (ramo algébrico pós-erratum)** continua
   primeiro — barata, fecha a última porta interna da F1, e o G1-b
   pega carona nas MESMAS rodadas (os autovetores já saem).
2. G1-a em paralelo (documental).
3. G1-c depois do resultado de G1-b.
4. Se G1-b passar E o ramo algébrico pós-erratum também reprovar:
   R1 vira o enquadramento oficial do no-go ("a F1 escolheu a
   representação errada para a relação física correta") e a
   investigação 2 (condensação dinâmica) é promovida a teste direto
   de R2.

## 6. O que este gate NÃO é

Não é quantização de σ. A pergunta "σ é quântico?" é prematura
enquanto não se souber SE σ_HR é a realização correta do grau
relacional. Este gate decide a pergunta anterior.

## 7. Resultado (2026-08-11) — G1-b PASSA, R1 é o enquadramento oficial

Script: `auditoria/code/investigacao1_ramo_algebrico.py` (Parte 2).
Detalhe completo em `docs/resultado_investigacao1_ramo_algebrico.md`.

**G1-b:** projeção de todos os modos em δφ₋ (campo `dchi`), ponto fixo
do ramo finito, μ∈{0.1,0.3,1,3,10} (μ=0.1 na célula da "fresta", única
com fundo físico válido ali), k=1 E k=10, β_n constante. **17/17**
instâncias de modo patológico (taquiônico ou fantasma) na varredura
têm \|⟨v,δφ₋⟩\|² = 0.0000 — muito abaixo do critério de 0.05, e
identicamente zero, não apenas pequeno. Cross-validado contra
`docs/estrutura_par_relativo.md`/`modulacao_qep.py`: a célula da fresta
reproduziu o kN=−1.6e-5 já documentado (e sua inversão de sinal entre
k=1 e k=10), confirmando a maquinaria de projeção de autovetores.

**R1 PASSA.**

Na mesma sessão, a Investigação 1 da fila (§5 item 1) também reprovou o
ramo algébrico (`docs/resultado_investigacao1_ramo_algebrico.md` §2):
degenerado E taquiônico na raiz exata, sem corredor saudável em
$\delta\in[-0.30,+0.30]$. Isso satisfaz as duas condições do §5 item 4
deste documento — G1-b passou E o ramo algébrico também reprovou.

**R1 vira o enquadramento oficial do no-go**: o problema demonstrado
até aqui é da REPRESENTAÇÃO F1 (setor de vínculos da realização
bimétrica HR — dubleto de shifts $B_g\pm B_f$ em μ≳1, lapso $\Phi_f$
quase-nulo em μ→0), não do grau relacional primordial δΦ₋ enquanto
tal. O trilema do §3 permanece aberto entre (b) g/f efetivas de um
coletivo 𝓡 (R2) e (c) grau relacional sem segunda métrica — (a) já foi
testado e reprovado (`docs/veredito_setor_escalar_final.md`).

**Próximo passo da fila:** G1-a (tabela documental, custo ~zero), depois
G1-c (nota do trilema), depois a Investigação 2 (condensação dinâmica,
$p_\phi\neq0$) — agora promovida a teste direto de R2.

## 8. Resultado (2026-08-11) — G1-a CONCLUÍDO

`docs/gate1a_tabela_identidade.md`: 19 clusters de ocorrência
classificados (Cap.1–19 + Anexos B–L), zero sem classificação
(critério ✔). **Veredito: a cadeia Φ₋ → φ/χ → r → σ tem ZERO elos de
identidade derivados** — toda identificação entre dois dos quatro
objetos é decreto (por vezes auto-declarado: "como glosa narrativa […]
Nenhuma equação muda", Anexo L §L.2) ou indefinida. As únicas linhas
derivadas são propriedades internas (EOM de σ; m₋²<0) ou um
acoplamento (m_S²∝r−r★), nunca "X é Y". A flag epistêmica foi
adicionada ao `dicionario_simbolos.md` §3 na linha "φ₋ modula β_n".

Subprodutos: terceira colisão de χ (modo reduzido no Cap.6 §6.4 antigo),
sobrecarga do rótulo "modo relativo" (σ, S, h₋ tensorial), e uma quarta
fórmula de tempo relacional (η̇=Γχ̇² do Anexo H, além das três já
listadas no `plano_v2_reconstrucao.md` Passo 10) — registrados no
dicionário e na tabela §5.

G1-a e G1-b fechados no mesmo dia, convergentes: nem o texto deriva a
identificação (G1-a, nível 1), nem a dinâmica a sustenta na F1 (G1-b,
nível 2b — projeção zero). **Falta só o G1-c** (nota do trilema) para
fechar o Gate 1 por completo.
