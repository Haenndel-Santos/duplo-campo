# R-12 — ERRATUM-03 (instrumento): o Ċ de 2ª ordem, e a confirmação de c_s² = −1

**Data:** 2026-08-13. Scripts: `auditoria/code/r12a_forma_de_k.py`,
`r12h_raio_de_alcance.py`,
`r12c_varredura_plato.py` (**ambos retratados**, preservados no git),
`r12d_plato_alta_precisao.py`, `r12e_confronto_canais.py`,
`r12f_veredito_instrumento.py`, `r12g_isola_ruido_e_classe.py`
(saídas em `out/`).

Este documento faz três coisas: **(i)** retrata duas conclusões que eu
mesmo emiti nesta sessão; **(ii)** identifica e demonstra um defeito do
instrumento numérico usado de R-7 a R-12c; **(iii)** confirma, com
instrumento limpo, o enunciado central do R-11.

---

## 1. O resultado, em uma frase

**c_s²(r → 0) = −1 na classe F1 — o R-11 estava certo** — e o desvio
que eu havia interpretado como "estrutura em kh" era **erro de
truncamento do `np.gradient` de 2ª ordem no Ċ, amplificado pelo
condicionamento da redução**.

## 2. O arco (e por que ele importa mais que o número)

| Passo | O que fez | Conclusão |
|---|---|---|
| **R-12a** | varreu kh de 1 a 3e4 no canal do repositório | "há vale em kh≈100 e platô em −0.687; o par (30,100) do R-11 não determina o limite" — **ERRADO** |
| **R-12c** | repetiu as 108 células do R-11 medindo o platô | "platô = −0.6867, dispersão 4.8e−4" — **ERRADO** (herdou o mesmo canal) |
| **R-12d** | canal novo: mpmath dps=60, fundo em **forma fechada** | c_s² → −1.0000000 — **conflito** |
| **R-12e** | arbitragem | **não é precisão de máquina**: float64 e mpmath concordam a 1e−9 quando ambos usam estêncil de 8ª ordem. V-D confirma invariância pela reescala D (4e−55) |
| **R-12f** | V-DERIV | as formas fechadas de Ḧ, Ḧ_f, ξ̈ batem com diferença de 8ª ordem a **6.7e−45**; e emular o `fundo_ext` (h=1e−5, float64) no canal limpo **não muda nada** |
| **R-12g** | V-ORDEM | trocando **só** a ordem do estêncil de Ċ₃/Ċ₂, a 2ª ordem reproduz a tabela do R-10a **dígito a dígito** |

**A causa está demonstrada, não conjecturada.** Com tudo o mais exato,
o estêncil de 2ª ordem (= `np.gradient`) dá:

| a | kh | ordem 2 | ordem 8 | tabela R-10a |
|---|---|---|---|---|
| 0.01 | 30 | −1.01033852661 | −0.997161671714 | −1.010339 |
| 0.01 | 100 | −1.2608602308 | −0.999743555243 | −1.260860 |
| 0.01 | 300 | −0.585509139414 | −0.999966216469 | −0.585509 |
| 0.01 | 1000 | −0.679679171181 | −0.999991499897 | −0.679679 |
| 1000 | 30 | +1.00962144784 | +1.00880162812 | +1.009620 |

E o teste de refino separa os dois definitivamente (a = 0.01, kh = 100):

| h | ordem 2 | ordem 8 |
|---|---|---|
| 1e−3 | −1.2608602308045 | −0.99974355524312 |
| 3e−4 | −1.0130902044276 | −0.99974355524313 |
| 1e−4 | −1.0011722096624 | −0.99974355524313 |

A 2ª ordem **move com h** e converge para o valor da 8ª; a 8ª é estável
em 14 dígitos. O erro é O(h²) ≈ 1e−7 no Ċ, amplificado pelo
condicionamento da redução (cond(W_XX) ≈ 1e11 em a = 0.01, com K₂ ≈
1e−26 depois do E2).

## 3. O resultado com o instrumento limpo

**Perfil em k** (célula benchmark, a = 1e−4 ⟹ r ≈ 1.7e−12):

| kh | 30 | 100 | 1000 | 10000 |
|---|---|---|---|---|
| c_s² | −0.99716770 | −0.99974956 | −0.99999750 | −0.99999997 |

O desvio de −1 escala **exatamente** como 1/kh²:

> **ω²/H² = −kh² + 5/2 + O(r)** — ou seja, `c_s² = −1` e o resto é
> **massa** (m_ef² → (5/2)H²). **Não há termo k⁴ e não há estrutura em
> kh.** O "termo k⁴" registrado no R-9a (c_s² = 1.929 em kh = 1000 na
> era tardia) era o mesmo artefato: o valor limpo é 1.0000079.

**Varredura de classe** (as mesmas 108 células do R-11, β₃ = 0):

| grade | |c_s² + 1| máximo | células |
|---|---|---|---|
| a = 0.01, kh = 1e4 | 2.4e−5 (é o O(r), com r ≈ 1e−6) | 108/108 |
| a = 1e−4, kh = 1e6 | **1.1e−7** | 108/108 |

Zero células com c_s² > 0. O desvio residual é inteiramente massa +
O(r) e **desaparece no limite**.

**Época de troca de sinal:** a_cross = **0.57808** (canal antigo:
0.574) ⟹ z_cross = **0.6105** (antes 0.62). A era tardia tem
**c_s² = +1 exato**.

## 4. O que fica retratado, e o que fica de pé

**Retratado (meu, desta sessão):** o R-12a e o R-12c inteiros — o
"platô em −0.687", o "vale não-monotônico em kh ≈ 100" e a afirmação
de que `c_s² = −1` era artefato de extrapolação. Os arquivos ficam no
git como registro; os documentos não devem citá-los como resultado.

**Corrigido quanto ao valor (não quanto ao enunciado):** as tabelas de
c_s² de `resultado_r9a`, `resultado_r10a`, `resultado_r10_consolidado`
e `resultado_r11_nogo_gradiente`. O −1.010 ± 6e−6 do R-11 era o valor
**contaminado** em kh = 30; o valor verdadeiro é −0.99716 em kh = 30 e
**−1 exato** no limite sub-horizonte.

**De pé, e agora mais forte:**

- o **NO-GO DE CLASSE POR GRADIENTE** — confirmado em 108/108 com
  instrumento limpo, e com valor exato em vez de aproximado;
- a severidade do R-10b (a_cross e z_cross praticamente inalterados;
  a era instável **cobre a recombinação**);
- as quatro saídas fechadas (R-10c/d, R-11) — *[R-12i, 2026-08-13:
  são **três fechadas e uma reaberta**. A exclusão do ramo infinito
  por "ξ cruza zero" não se sustenta: `ξ = X/a` com o `X ≡ ḃ/ℋ` de
  Könnig et al. (mesmo sinal, mesmo zero), e é o quique de `b` que
  1407.4331 §II/§VI trata e defende como físico, com três argumentos.
  Reexame pendente, alvo é o ramo infinito **com β₄ ≠ 0** (IBB viável
  exige 0 < β₄ < 2β₁; a célula mínima tem β₄ = 0). Ver
  `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6]* **[R-13a +
  R-13b, 2026-08-13: o reexame foi feito e voltam a ser QUATRO
  FECHADAS — mas com a exclusão do ramo infinito INTEIRAMENTE
  SUBSTITUÍDA. O argumento `ξ = 0` permanece REVOGADO; o que exclui o
  ramo é o GHOST DE HIGUCHI (`Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0`; `r′ < 0` em
  108/108 células, Higuchi 0 de 64 800 pontos, controle positivo do
  ramo finito 400/400). Nunca citar a contagem sem a substituição.
  Ver `docs/resultado_r13a_criterio_higuchi_fonte.md` e
  `docs/resultado_r13b_ibb_ramo_infinito.md`.]**;
- tudo o que não passa pela redução numérica: Erratum-01, Erratum-02,
  fundo, setor tensorial, espectador, contagem 2-DOF, Gate 1.

## 5. A lição de método (e as duas regras novas)

Este é o **terceiro** caso em que um artefato numérico foi tomado por
física neste programa — e desta vez ele não criou um resultado falso,
**inflou um resultado verdadeiro** e depois me levou a "refutá-lo".
Duas regras entram para o cap. 02:

1. **Derivadas ao longo do fundo em forma fechada.** Onde não for
   possível, estêncil de ordem ≥ 8 **com teste de refino obrigatório**
   (dois h, exigir estabilidade). `np.gradient` é proibido em qualquer
   cadeia que passe por uma redução mal condicionada.
2. **Declaração de cegueira do gate** (regra já proposta pelos
   pareceres, §2 da síntese cruzada, agora com caso concreto): o
   calibrador do espectador δχ — usado como prova de calibração de
   R-9a a R-12c — **não tem poder de detecção sobre o canal Ċ**,
   porque δχ não tem termo giroscópico (C₂ e Ċ₂ são nulos nesse
   canal). Ele deu `1.00000` em todos os pontos enquanto o modo
   métrico errava na primeira casa. Todo calibrador deve declarar o
   que **não** consegue ver.

## 6. Raio de alcance do defeito (R-12h)

A cadeia defeituosa está em **toda** a cascata R-1…R-12c (`grep
np.gradient`). Pior: nos scripts de R-1 a R-8b o **próprio Ċ₇** também
é `np.gradient` de 2ª ordem — o defeito entra duas vezes. A pergunta
que decide o que precisa ser refeito é se ele **morde** no domínio de
cada resultado. Medido em `r12h_raio_de_alcance.py`, com três variantes
no mesmo ponto: **A8** (Ċ₇ simbólico + estêncil 8ª, referência),
**A2** (= R-10a…R-12c), **N2** (= R-1…R-8b).

**No domínio do R-7/R-8** (a ∈ [100, 8e4] × kh ∈ [0.2, 20]):

| grandeza | desvio máx. A2 | desvio máx. N2 |
|---|---|---|
| ω² | 3.6e−4 | 1.9e−4 |
| autovalores de K₂ | 1.5e−5 | 2.3e−4 |
| W00 | — | 2.0e−6 |

E os **sinais** de (λK₂¹, λK₂², W00) são idênticos nas três variantes em
todos os pontos — sempre `++−`. Logo:

> **Os enunciados estruturais do R-7 (no-ghost; W00 nunca cruza zero)
> não dependem do defeito, e a cascata R-7/R-8 é quantitativamente
> segura** — as margens lá são de 10+ unidades log e o erro é ≤ 4e−4.
> Controle positivo em a = 0.01, kh = 30: desvio 3.9e−2 (o harness
> reproduz o defeito onde ele existe).

**A fronteira não é só em `a` — é em kh também.** Na era tardia
(a = 1000):

| kh | 20 | 30 | 100 | 300 | 1000 |
|---|---|---|---|---|---|
| c_s² (A8) | 1.01972 | 1.00880 | 1.00079 | 1.00009 | 1.00001 |
| c_s² (A2) | 1.02009 | 1.00962 | 1.00980 | 1.08123 | 1.92869 |
| desvio | 3.6e−4 | 8.1e−4 | 9.0e−3 | 8.1e−2 | **9.3e−1** |

O defeito fica abaixo de 1e−2 até **kh ≈ 100**; acima disso morde.

**Mapa final por resultado:**

| Resultado | domínio usado | veredito |
|---|---|---|
| R-7a/b/c/e/f | a ∈ [100, 8e4], kh ≤ 45 | **seguro** (≤ 4e−4) |
| R-9a Parte A (ω²_ef = (Ċ+W)/K) | kc = 45·H(100)·100 ⟹ kh ≤ 45 | **seguro** |
| R-9a Parte B ("termo k⁴") | kh até 1000 | **contaminado** — artefato, já retratado |
| R-8b (m_T/H₀) | headline vem do tensor + fundo | **não passa pela cadeia** |
| R-8a (μ/Σ/η) | resolve `−W q + J = 0`, sem Ċ e sem `np.gradient` | **não passa pela cadeia** |
| R-10a/b/c/d, R-11, R-12a/c | a ≤ 0.05, cond ≫ 1 | **contaminado no valor** (enunciados intactos) |
| R-1…R-6 | — | já superados pelo Erratum-02; não requerem revisão |

Ou seja: **o item "refazer o R-8a" da fila cai** — ele nunca usou a
cadeia defeituosa. E não há nada do R-7 a refazer.

## 7. Estatuto e fronteiras

Nível 2b, mesmas fronteiras do R-10a/R-11 (classe F1 com β₃ = 0, ramo
finito, matéria só como ρ de fundo, sem radiação, F′ = F″ = 0). O que
mudou é a qualidade do instrumento, não o domínio.

O alcance do defeito **foi** medido (§6): no domínio do R-7/R-8 o
desvio é ≤ 4e−4 e os sinais de (λK₂¹, λK₂², W00) não mudam; o R-8a
sequer passa pela cadeia (resolve `−W q + J = 0`, sem Ċ). Nada da
cascata R-7/R-8 precisa ser refeito.

**Não verificado aqui:**

- o mapa do §6 é uma **amostragem em 16 pontos** (a ∈ {100, 1e3, 1e4,
  8e4} × kh ∈ {0.2, 1, 5, 20}), mais um corte em kh na era tardia —
  não é um escaneio contínuo;
- a **faixa intermediária a ∈ (0.05, 100)** ficou sem sondar: entre a
  era inicial contaminada (cond ≫ 1) e a região tardia segura não há
  medida da transição;
- os docs de R-9a/R-10a/R-10b/R-11 seguem com as **tabelas antigas sob
  banner de supersessão** — aqueles valores não foram regerados um a
  um com o instrumento limpo. O que foi refeito com ele é o que está
  no §3 (perfil em k, as 108 células, a_cross/z_cross).

## 8. Fila

1. ~~Prova analítica de c_s² = −1 em r → 0~~ — **FEITA** no mesmo dia:
   `docs/resultado_r12b_teorema_cs2.md`. Forma fechada
   `c_s²(r) = −(3r+1)(9r⁵−6r³+3r²−10r+2)/(2(3r²+1)²)`, com −1 exato em
   r → 0 e **+1 exato** no atrator tardio; m_ef²/H² → 5/2, batendo com
   a medida desta nota.
2. ~~Refazer o R-8a com o instrumento limpo~~ — **desnecessário**
   (§6): o R-8a resolve `−W q + J = 0` e nunca toca o Ċ.
3. Anotar a supersessão nos docs de R-9a/R-10a/R-10b/R-11 e no cap. 07
   da v2 (valor, não enunciado) — **feito**.
4. Restante: generalizar a fórmula de c_s² em (β₀, β₂, β₄, μ);
   confrontar com Könnig et al.; cap. 09 (validade restrita).
