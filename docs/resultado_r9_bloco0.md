# R-9 (Bloco 0) — Resposta aos Três Testes Baratos dos Pareceres

**Data:** 2026-08-13. Scripts: `auditoria/code/r9a_omega2_diagnostico.py`,
`r9b_algebra_vinculos.py` (saídas em `out/`). Contexto:
`docs/pareceres_especialistas/00_sintese_cruzada.md` §7, Bloco 0 —
os três testes de horas que os especialistas pediram antes de
qualquer coisa. Estatuto: resultados internos com critérios
pré-declarados; fronteiras declaradas por item.

---

## Sumário

| Item | Origem | Resultado |
|---|---|---|
| (c) ω² < 0 do R-7e | cosmologia | **RESOLVIDO** — era razão errada; ω²_efetivo > 0. O arquivamento como artefato de envelope se sustenta, agora com a explicação correta |
| (a) p_φ cruza zero ⟹ Dirac degenera | física teórica | **Premissa CONFIRMADA, conclusão NÃO** — p_φ cruza zero 6× após o pouso, mas a estrutura de segunda classe sobrevive |
| (b) 1ª classe do difeomorfismo | física teórica | **NÃO RESPONDIDO** — o teste em minisuperespaço é tautológico; movido para o Bloco 2 |
| bônus: c_s² | cosmologia (A1) | **c_s² > 0** em tudo que foi testado; ≈ 1.01 (métrico) e = 1.000 (espectador) |

---

## 1. Item (c) — o ω² negativo era a razão errada

**A hipótese testada.** O integrador resolve
`K q̈ + (K̇ + C − Cᵀ) q̇ + (Ċ + W) q = 0`. Logo a frequência efetiva
é `(Ċ + W)/K`, **não** `W/K`. O R-7e mediu `W/K`, que omite `Ċ`.

**V-SINAL (medida direta): 16/32 entradas** têm `W/K < 0` **e**
`(Ċ+W)/K > 0` — ou seja, **todas as entradas do modo métrico**, nos
dois fundos, em todas as épocas. Exemplo em a=200: `W/K = −1.5e5 H²`
contra `(Ċ+W)/K = +514 H²`. O sinal se inverte pela inclusão do termo
que faltava.

**V-FREQ (o discriminador).** Se ω² fosse realmente negativo, o modo
**não oscilaria** (exponencial puro); e se a magnitude `|W/K|`
fosse a frequência, haveria ~110 cruzamentos de zero na janela. O que
se mede em a=200 (Etil): **6 cruzamentos**, contra a previsão WKB de
fase acumulada Φ = 20.4 rad ⟹ 6.5 cruzamentos. A hipótese `W/K` é
refutada por duas vias independentes (existência de oscilação e
frequência, esta por fator ~20).

Pelo critério pré-declarado, **V-FREQ FALHOU: 3/4 marcos com
resolução** dentro de 25% (75% < 80%). O quarto (a=452, Etil) dá
Φ_prev = 10.2 vs Φ_med = 6.28. Duas notas honestas:
(i) a amostra testável é minúscula — 4 marcos, porque 12 dos 16 não
têm resolução (Φ < 2π: o modo não completa um ciclo na trilha, limite
físico do IR tardio, não falha de instrumento);
(ii) o critério mede a *concordância quantitativa* com WKB, mas a
*discriminação entre as hipóteses* é de ordens de grandeza e não
depende dela.

**Leitura: item (c) resolvido pela leitura (i) da síntese.** O
"ω² < 0 variando 5 ordens" do R-7e era razão errada, não física nova.
A conclusão de saúde do R-7e não muda; o texto precisa ser corrigido
(ver §5).

**Registro de instrumento (3 comparadores descartados).** O V-OM
original comparava taxas de envelope com a raiz local do oscilador
(56%); a v2 usou o invariante adiabático (31%, pior); a autópsia
achou a causa comum — as ICs do teste não são adiabáticas, então a
taxa de envelope mede transiente, não WKB. A v3 (frequência local)
falhou por resolução (25%); a v4 (fase acumulada, com marcos sem
resolução declarados) é a versão reportada. Todas preservadas no
histórico git. *Lição, para o cap. 02: quando um gate reprova, a
primeira suspeita deve ser o comparador — três vezes seguidas o
problema foi o instrumento, não o objeto.*

## 2. Bônus: c_s² — sem instabilidade de gradiente no benchmark

A mesma máquina dá a velocidade de gradiente por ajuste de
`ω²_ef = c_s²(k/a)² + m²` (3 épocas × 6 valores de kh × 2 fundos):

| modo | c_s² (kh ∈ [30,100]) | calibração |
|---|---|---|
| espectador δφ₋ | **1.0000** | exato — âncora do R-7a |
| métrico (Ẽ) | **≈ 1.010** | — |

**c_s² > 0 em todos os pontos testados** (G-CS OK). O espectador sai
exatamente luminal, o que calibra o método.

**Achado lateral:** a razão `ω²/(k/a)²` do modo métrico sobe de 1.010
(kh=100) para 1.93 (kh=1000) — um termo **~k⁴** com escala
M/H ~ 1.0e3. O `cond(W_XX)` fica entre 3.8 e 18 em toda a faixa, ou
seja **não é perda de condicionamento: é estrutura**. Interpretação
provável: escala de quebra da truncagem de 2 derivadas do sistema
reduzido. Fica registrado como observação a explicar (não como
resultado).

**O que isto NÃO é:** não substitui o A1 do Bloco 1. Aqui só foi
testado o benchmark β-constante, sem o fundo dinâmico e sem o
confronto com o resultado de instabilidade de gradiente do finite
branch da literatura ([arXiv:1407.4331]). O A1 continua com
prioridade máxima — mas parte agora de um prior favorável.

## 3. Item (a) — a premissa do parecer está certa; a conclusão, não

**M-A1 (premissa): CONFIRMADA.** Após o pouso (a ≈ 1709), `p_φ`
cruza zero **6 vezes** na trilha (a = 2353, 4538, 8432, 15706, 29168,
54221) — o campo oscila amortecido, exatamente como o parecer previu.

**M-A2 (conclusão): NÃO CONFIRMADA.** A degenerescência exigiria que
o par `D_g = {Ω, ℋ_g}` e `D_f = {Ω, ℋ_f}` se anulasse *junto* (é o
que deixaria a razão de lapsos indeterminada e faria nascer um
vínculo terciário). Medido nos cruzamentos:

| a | χ̇ | D_g | D_f | Δ_local | ξ_impl = −D_g/D_f |
|---|---|---|---|---|---|
| 2353 | +5.6e−05 | +2.23e11 | −2.03e11 | 0.378 | 1.097 |
| 8432 | +3.1e−05 | +8.30e12 | −7.21e12 | 0.238 | 1.152 |
| 54221 | −2.0e−05 | +2.15e15 | −1.86e15 | 0.223 | 1.159 |

Nem `D_g` nem `D_f` são pequenos, e a razão de lapsos implicada é
**finita e estável (ξ_impl ≈ 1.158)**. A estrutura de segunda classe
sobrevive aos cruzamentos.

**Por quê.** O resíduo da Bianchi *na raiz* é ∝ `p_φ β₁′` — esse sim
se anula. Mas `D_g` e `D_f` são brackets de Ω com as hamiltonianas, e
**não têm `p_φ` como fator global**: os termos de derivada trazem
outras contribuições que não se anulam junto. A intuição do parecer
(o resíduo some quando p_φ = 0) está correta; a inferência (logo a
matriz de Dirac degenera) não se sustenta neste fundo.

**Correção de instrumento declarada:** a 1ª rodada normalizava por um
máximo **global** da trilha. Como |D| cresce ~4 ordens ao longo da
evolução, isso fazia todo ponto inicial parecer degenerado e produziu
um falso "DEGENERESCÊNCIA CONFIRMADA" (Δ = 1.7e−5 no primeiro
cruzamento, onde D_g = +2.2e11). A medida correta usa escala **local**
(janela móvel de ±0.5 e-fold). Preservada no git.

**Fronteira:** minisuperespaço, uma trajetória, célula REF.

## 4. Item (b) — o teste era tautológico; sai do Bloco 0

`{ℋ_g+ℋ_f, ℋ_g−ℋ_f} = −2{ℋ_g,ℋ_f} = −2Ω` é **identidade algébrica**,
verdadeira para quaisquer duas funções. Como Ω já é um vínculo, a
combinação diagonal é fracamente de primeira classe em
minisuperespaço **por construção** — o teste não tem conteúdo. (Serviu
como verificação de que a máquina de brackets está correta: o resíduo
saiu em nível de roundoff.)

A pergunta real do parecer — se o **difeomorfismo espacial** continua
de primeira classe sob β_n(φ₋) — exige k ≠ 0 e é o mesmo cálculo de
campo do Gate 2B. **Item (b) movido do Bloco 0 para o Bloco 2**, a ser
feito junto com o Gate 2B.

## 5. Correções a aplicar no corpus

1. `docs/resultado_r7e_saude_interna.md` §2 e
   `docs/pareceres_especialistas/00_sintese_cruzada.md` §3: o
   "ω²(Ẽ) < 0 variando 5 ordens" deve ser reescrito como *razão W/K,
   que não é a frequência efetiva do sistema*; a frequência correta é
   positiva e a leitura de artefato de envelope se mantém.
2. Registrar em `docs/resultado_r7e_saude_interna.md` que o A1 tem
   agora um prior favorável (c_s² > 0 no benchmark), sem substituir o
   teste.
3. Cap. 02 da v2: acrescentar a lição dos três comparadores
   descartados.

## 6. Fila após o Bloco 0

Inalterada no essencial — o Bloco 0 não desbloqueou o R-8, mas
removeu dois riscos e reordenou um item:

- **Bloco 1 (prioridade máxima): A1** — teste de gradiente no fundo
  dinâmico + confronto com 1407.4331. Prior favorável, teste
  mantido.
- Bloco 1: A2 (w_eff vs DESI), escopo de época com radiação, varredura
  de μ, paredes de domínio.
- **Bloco 2 (agora com mais um item): Gate 2B + primeira classe do
  difeomorfismo espacial** — o mesmo cálculo de campo; Vainshtein/PPN
  e buracos negros; V-EXT.
