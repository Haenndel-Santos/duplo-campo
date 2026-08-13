# R-12 — ERRATUM-03 (instrumento): o Ċ de 2ª ordem, e a confirmação de c_s² = −1

**Data:** 2026-08-13. Scripts: `auditoria/code/r12a_forma_de_k.py`,
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
- as quatro saídas fechadas (R-10c/d, R-11);
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

## 6. Estatuto e fronteiras

Nível 2b, mesmas fronteiras do R-10a/R-11 (classe F1 com β₃ = 0, ramo
finito, matéria só como ρ de fundo, sem radiação, F′ = F″ = 0). O que
mudou é a qualidade do instrumento, não o domínio. Não verificado
aqui: se o defeito do Ċ afeta quantitativamente resultados da cascata
R-7/R-8 (lá cond ≈ 10, e a diferença medida em a = 1000 é ~8e−4 —
irrelevante para conclusões de ordem de grandeza como a banda morta,
mas **as tabelas de precisão do R-8a deveriam ser refeitas**).

## 7. Fila

1. **Prova analítica de c_s² = −1 em r → 0** — agora com alvo **bem
   posto e confirmado numericamente em 1e−7**. Em curso
   (`r12b_prova_simbolica_cs2.py`): redução 2-DOF em forma fechada com
   β₁ eliminado em favor de (r, H).
2. Refazer o R-8a (μ/Σ quase-estáticos) com o instrumento limpo — os
   números lá são sub-percentuais e o defeito é da mesma ordem.
3. Anotar a supersessão nos docs de R-9a/R-10a/R-10b/R-11 e no cap. 07
   da v2 (valor, não enunciado).
