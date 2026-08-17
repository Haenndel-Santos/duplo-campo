# R-13a — O CRITÉRIO DE HIGUCHI NA FONTE: Könnig 2015 (arXiv:1503.07436), extraído e traduzido

> ## ✔ BANNER DE CONFIRMAÇÃO — 2026-08-17 (`docs/auditoria_r13.md`)
>
> **Nada deste documento cai. O que era sua única fronteira epistêmica
> real fecha, e duas alegações ganham confirmação independente.**
>
> - **O item 1 da fila (§6) — "verificação simbólica do §2" — está
>   FEITO, e por rota independente da que ele pedia.** O mapa
>   `r_K = √μ r`, `β_n^K = A μ^{−n/2} β_n` foi re-derivado da
>   **redundância da ação** sob `f → λ²f`, com os `e_n` calculados pela
>   raiz matricial de Sylvester de `tdcp_pert_lib.py` — **sem tocar nas
>   Friedmann**. Resíduos simbólicos zero em todos os cinco `β_n`, e
>   solução única. Mapas errados (`c = μ`; `β_n ~ μ^{−n}`) reprovam.
> - **A alegação de sobredeterminação do §2.1 está EXIBIDA, não só
>   afirmada.** Com `r_K = c·r` e `β_n^K = A_n β_n` incógnitos: a
>   Friedmann-g fixa `A_0..A_3 = A c^{−n}` e deixa `c` **livre**; a
>   Friedmann-f impõe **duas** condições independentes (o bloco
>   `β₁/β₂/β₃` e o termo `β₄`) que dão o **mesmo** `c = √μ` e
>   `A_4 = Aμ^{−2}`. O padrão `μ^{−n/2}` no `n = 4` **saiu, não foi
>   imposto**. E as eqs. **(12)** e **(13)** — que não entraram na
>   construção — batem com a nossa `𝒲(r)` e com `√μ·dr/dN` (resíduos 0),
>   esta última com **`w` geral**.
> - **A cadeia vale para todo `w > −1`, não só poeira.** O fator
>   `(1+w)` é positivo e comum. Extensão além do que o R-13b verificou.
> - **A armadilha de sinal do §1.7 está VERIFICADA NA FONTE,
>   verbatim**, nos dois papers, por extração própria do ar5iv. E a
>   leitura do §1.5 — de que 1503.07436 §IV A **mantém** o resultado de
>   gradiente do IBB — também: *"stable modes are guaranteed if
>   `3β₁r² < β₁+β₄r³`"*, condição que a fonte diz ser *"equivalent to
>   the condition ρ>0 on that branch"*. Nas nossas variáveis essa
>   condição **é** `ρ̃ > 0` (resíduo 0), com generalização em `μ`.
> - **`w_mg ≤ −1` (§4.3) confirmado por rota própria**: derivando da
>   conservação de `ρ_mg = m²M_ef²V_g(r)` sai `w_mg = −1 − ℬ(r)r′/V_g`,
>   idêntico à tradução da eq. (20) deles. Resíduo 0.
> - **Uma ressalva NOVA sobre a hipótese 2 do §2.2** (modulação): o que
>   ela quebra é a **equivalência com o sinal de `r′`**, não a
>   inequação (15). Sob `β_n(φ₋)` o diagnóstico correto é `𝒲′(r) > 0`.
>   Ver `auditoria_r13.md` §6.2. **E o que continua não sabido por
>   ninguém — inclusive pela auditoria — é se a própria eq. (14)
>   sobrevive intacta sob modulação.** Isso substitui o item 1 desta
>   fila como o item mais caro.
> - **Não fechado:** o §5 registra que **1308.1647 não foi aberto**. A
>   auditoria também não o abriu. O caveat do fator `1/2` no potencial
>   permanece declarado e não verificado.
>
> *Fonte: `docs/auditoria_r13.md` §§1–3 e §6;
> `auditoria/code/r13aud_a_mapa_e_traducao.py`,
> `auditoria/code/r13aud_b_armadilha_de_sinal.py`.*

**Data:** 2026-08-13. Fonte primária: Frank Könnig, *Higuchi ghosts and
gradient instabilities in bimetric gravity*, **PRD 91, 104019 (2015)** =
[arXiv:1503.07436] (Preprint NORDITA-2015-44; 13 pp., 2 figuras; a
versão do arXiv é declarada como *"version published in PRD"*).

Fecha a **terceira lacuna declarada** do `docs/posicionamento_literatura.md`
§2b (bloco "Desfecho parcial — 2026-08-13"), que listava como *não
sabido da fonte*: (i) a forma explícita do funcional/inequação de
Higuchi nas variáveis dela; (ii) se o paper emite veredito próprio
sobre o IBB; (iii) como os enunciados se mapeiam nas nossas variáveis
(`ξ`, `r`, `N`, normalização β, `μ`, `M_ef²`). **Os três estão
respondidos abaixo.**

**Sem script novo no repositório.** Nenhum cálculo de física foi
rodado. A extração é leitura de fonte; a tradução (§2) é álgebra de
substituição feita **à mão**, passo a passo e auditável, **não**
verificada por CAS — e assim declarada.

**O que este documento NÃO faz.** Não emite nenhum veredito sobre o
ramo infinito / IBB da família F1. Ele entrega o **critério**; quem
mede é outro processo. Toda frase abaixo sobre o IBB é *relato do que a
fonte afirma sobre o IBB dela*, não conclusão sobre o nosso.

**Veredito em uma linha.** A tradução **fechou, e fechou exatamente,
para `μ` arbitrário**: a inequação de Higuchi de Könnig (eq. 14) é,
nas nossas variáveis, **`m_T²|_{ξ→r} ≥ 2H²`** — a caixa do cap. 06 /
`derivations/02` com **ξ substituído por r**. Igual à nossa quando
`ξ = r` (isto é, `r′ = 0`); **diferente** de todo o resto da história,
com o desvio em forma fechada.

---

## 0. Nível de acesso à fonte

Disciplina de `docs/posicionamento_literatura.md`: **VERIFICADO-NA-FONTE**
vs **NÍVEL-DE-BUSCA**. Nada aqui é snippet de busca.

| Item | Nível |
|---|---|
| Título, autor, abstract, referência de periódico, DOI | **VERIFICADO** (arxiv.org/abs/1503.07436) |
| Texto integral | **VERIFICADO por duas rotas independentes**: HTML do ar5iv (`ar5iv.labs.arxiv.org/html/1503.07436`, 378 nós `<math>` com `alttext` LaTeX) **e** PDF de `arxiv.org/pdf/1503.07436` (6 pp. em dois colunas, texto extraído por decodificador `zlib`+`TJ/Tj` próprio) |
| Eqs. (1)–(19) — ação, fundo, **Higuchi** | **VERIFICADO nas duas rotas** |
| Eqs. (20)–(24), (28)–(40) — EOS, tensorial, escalar | **VERIFICADO** (ar5iv; (22)–(24) e (40) conferidas também no PDF) |
| §V (branches viáveis), §VI (conclusões), notas de rodapé 3 e 6 | **VERIFICADO nas duas rotas** |
| Bibliografia das duas ressalvas sobre o IBB | **VERIFICADO** (entradas completas, §1.5) |
| **A tradução do §2 para as nossas variáveis** | **ÁLGEBRA DESTE DOCUMENTO**, feita à mão, **não** verificada por CAS. É original, não está na fonte. |
| §3 (comparação com `m_T² ≥ 2H²`) | **ÁLGEBRA DESTE DOCUMENTO**, idem |

**Numeração.** Diferente do caso de 1407.4331 (onde o ar5iv estava
deslocado de +3 em relação à PRD), aqui **as duas rotas dão a mesma
numeração de equações** — a versão do arXiv é a publicada. Numeração de
seções: o PDF publicado usa `III. HIGUCHI GHOSTS` / `A. Higuchi bound`
/ `B. Phantom dark energy` / `C. Tensor ghosts` / `D. Consequences of
the existence of ghosts`; o ar5iv renderiza como III.1–III.4. Cito no
formato **§III A**, etc.

**Testes de integridade da extração** (o mais forte: as equações
extraídas fecham *entre si* por identidade algébrica feita à mão):

1. **(14) ⟹ (15)** — expandindo `(3/2)(β₁+2β₂r+β₃r²)(1+r²) − (β₁+3β₂r+3β₃r²+β₄r³)`
   e multiplicando por 2, sai **letra por letra** o lado esquerdo de
   (15). Resíduo zero.
2. **(15) ⟺ (16)** — derivando a (12), `ρ_{,r} = −β₁r⁻² + 3(β₃−β₁) + 2(β₄−3β₂)r − 3β₃r²`;
   multiplicando por `−r²` sai **exatamente** o lado esquerdo de (15).
   Logo `LHS(15) ≥ 0 ⟺ ρ_{,r} ≤ 0`. Resíduo zero.
3. **(11) ⟹ o "= 3r(ℋ/a)²" da (14)** — trivial e verificado.
4. **(40) confirma a (69) de 1407.4331** — ver §4.1: um erratum que o
   R-12i registrou é confirmado por este paper.

Nenhuma dessas quatro é afirmação da fonte: são conferências minhas
sobre o que extraí. Todas fecham.

---

## 1. O que a fonte de fato afirma

### 1.1 A condição de Higuchi exata (pergunta 1) — **§III A, eq. (14)**

**Não** é `m_FP² ≥ 2H²`. Não aparece nenhuma massa na inequação: ela é
escrita **inteiramente em `r` e nos `β_n`**. Verbatim, com todos os
fatores (§III A, eq. 14):

$$\frac{3}{2}\left(\beta_{1}+2\beta_{2}r+\beta_{3}r^{2}\right)\left(1+r^{2}\right)\;\geq\;\beta_{1}+3\beta_{2}r+3\beta_{3}r^{2}+\beta_{4}r^{3}\;=\;3r\left(\frac{\mathcal H}{a}\right)^{2}
\qquad (14)$$

A igualdade final **não** faz parte da condição: é a Friedmann-f (eq.
11) reescrita. Isto é, o lado direito da desigualdade **é** `3rH²` (com
`H = ℋ/a` = Hubble cósmico), e a inequação tem a forma
"algo(β,r) ≥ 3rH²".

**Atribuição declarada pela própria fonte** (§III A, e é importante
para o nosso rastro): a condição para ausência do fantasma de Higuchi
em bigravidade em torno de FLRW foi derivada em **Fasiello & Tolley,
JCAP 1312, 002 (2013) [arXiv:1308.1647]**. A eq. (14) é a versão
*"nas nossas notações"* dela. Nota de rodapé 3, verbatim no essencial:
Fasiello–Tolley usam um fator global `1/2` na frente do termo de
potencial, *"which can be compensated for by a redefinition of the
β-couplings"*. **Quem for citar 1308.1647 diretamente herda esse fator
2 nos β.**

Formas equivalentes, todas da §III A:

$$\beta_{1}+3r^{2}\left(\beta_{1}-\beta_{3}\right)+2r^{3}\left(3\beta_{2}-\beta_{4}\right)+3r^{4}\beta_{3}\;\geq\;0
\qquad (15)$$

$$\rho_{,r}\;\leq\;0 \qquad (16)$$

$$\rho_{,r}=-3\left(1+w_{tot}\right)\frac{\rho}{r'} \qquad (17)$$

$$r'\;\geq\;0 \qquad (18)$$

$$B_{2}\equiv\beta_{1}+2\beta_{2}r+\beta_{3}r^{2}\;\geq\;0 \qquad (19)$$

A cadeia lógica, exatamente como a fonte a monta:

- **(14) ⟺ (15)**: álgebra pura (conferida, §0).
- **(15) ⟺ (16)**: usando (12)–(13); `−r²ρ_{,r}` é o LHS de (15)
  (conferido, §0). A fonte credita (16) a trabalho anterior:
  *"already derived in"* **Yamashita & Tanaka, JCAP 1406, 004 (2014)
  [arXiv:1401.4336]**, *"see also"* **De Felice, Gümrükçüoğlu,
  Mukohyama, Tanahashi & Tanaka, JCAP 1406, 037 (2014)
  [arXiv:1404.0008]**.
- **(16) ⟺ (18)**: por (17), **sob duas hipóteses explícitas** —
  `ρ > 0` **e** `1 + w_tot > 0`. A fonte declara a segunda como
  *"we are usually considering a combination of pressureless and
  relativistic matter"*.
- **(19)** é condição **necessária** separada: o lado direito de (14)
  é `3r(ℋ/a)² ≥ 0` e, com `r ≥ 0` (adotado sem perda de generalidade,
  §II, pela redefinição `β_{2n+1} → −β_{2n+1}`), a (14) força `B₂ ≥ 0`.

**Envolve `r`? sim, centralmente. Envolve os `β_n`? sim, todos os cinco
(β₀ só indiretamente, via ρ). Envolve massas de Planck? NÃO — porque a
fonte fixou `M_f = M_g` (§1.2). Envolve ângulo de mistura? NÃO — o
termo "mixing angle" não ocorre no paper.**

**Nota (imprecisão menor da fonte, registrada).** §III A diz que `B₂`
*"is simply the derivative of ρ_mg"*, a parte modificada da Friedmann
(10). De fato `d/dr(β₀+3β₁r+3β₂r²+β₃r³) = 3B₂` — **fator 3**. Sem
consequência (só o sinal é usado), mas quem citar "B₂ = ∂_r ρ_mg"
herda o erro.

### 1.2 A convenção de variáveis (pergunta 2)

**A letra é `r`, e a definição é a nossa.** §II, logo após a eq. (7):
*"Here we introduced the ratio of the scale factors `r ≡ b/a`."* Não
existe `y` no paper (verificado por varredura: nenhuma ocorrência de
`y` como variável).

| Objeto | Könnig 1503.07436 | TDCP | Batem? |
|---|---|---|---|
| razão de escalas | `r ≡ b/a` (§II) | `r = b/a` | **sim** |
| tempo | `t` = **e-folding time**, `'` = d/dt (§II) | `N = ln a`, `'` = d/dN | **sim** (mesma variável, letra diferente) |
| Hubble | `ℋ` = Hubble **conforme** adimensional; `H = ℋ/a` cósmico | `H` cósmico | conversível, e ele já usa `(ℋ/a)²` na (14) |
| razão de lapsos | `X ≡ N_f^{(t)}/N_g^{(t)}`-like, com `X = 1 + r'/r` (eq. 9) | `ξ = N_f/N_g = r + dr/dN` | **ver §2.3 — é o mesmo objeto**, `ξ = rX` |
| potencial na Friedmann-g | `β₀+3β₁r+3β₂r²+β₃r³` (eq. 10) | `V_g(r)` idêntico | **sim, letra por letra** |
| potencial na Friedmann-f | `(1/r)(β₁+3β₂r+3β₃r²+β₄r³)` (eq. 11) | `V_f = β₄+3β₃r⁻¹+3β₂r⁻²+β₁r⁻³` | **sim**, com `(1/r)(…) = r²V_f(r)` — identidade exata |
| massas de Planck | **`M_f` posto igual a `M_g`** (§I e nota 6) | `μ = M_f²/M_g²` **livre** | **NÃO** — é a única diferença estrutural, e é resolúvel (§2.1) |
| fluido | `w_tot` genérico, inclusive radiação | poeira nas células fechadas | escopo maior do lado dele |

As duas equações de fundo, verbatim (§II):

$$3\mathcal H^{2}=a^{2}\left(\rho+\beta_{0}+3\beta_{1}r+3\beta_{2}r^{2}+\beta_{3}r^{3}\right) \qquad (10)$$

$$3\mathcal H^{2}=\frac{a^{2}}{r}\left(\beta_{1}+3\beta_{2}r+3\beta_{3}r^{2}+\beta_{4}r^{3}\right) \qquad (11)$$

$$\rho=\beta_{1}r^{-1}-\beta_{0}+3\beta_{2}+3\left(\beta_{3}-\beta_{1}\right)r+\left(\beta_{4}-3\beta_{2}\right)r^{2}-\beta_{3}r^{3} \qquad (12)$$

$$r'=\frac{\rho'}{\rho_{,r}}=-3\left(1+w_{tot}\right)\frac{\rho}{\rho_{,r}} \qquad (13)$$

**A eq. (13) é, letra por letra, o nosso `dr/dN = −3ρ̃/ρ̃′` para poeira**
(o mesmo que o R-12i já verificara contra 1407.4331). E `ξ`: `X = 1 + r'/r`
(eq. 9).

**Sobre `M_f = M_g`.** §I: *"we already set the Planck mass for `f_{μν}`
to `M_g`"*, com as massas expressas em unidades de `M_g²` e a escala de
massa do gráviton `m` absorvida nos `β_n`. E a **nota de rodapé 6** é
explícita sobre o custo: `M_f` foi posto igual a `M_g`, *"which is
allowed due to a redundancy in the parameters but is, however, not the
most natural choice"* — e ele remete a **Akrami, Hassan, Könnig,
Schmidt-May & Solomon [arXiv:1503.07521]** para o caso de `M_f`
pequeno. **É essa redundância que o §2.1 explora para reintroduzir o
nosso `μ`.**

### 1.3 "Universo em expansão + saúde ⟹ r′ > 0" (pergunta 3)

**Onde exatamente:** três lugares, com o mesmo conteúdo.

1. **Abstract:** em universos em expansão a razão dos fatores de escala
   tem de **crescer em todos os tempos**; e isso *"automatically implies
   a ghost-free helicity-2 and helicity-0 sector and enforces a phantom
   dark energy"*.
2. **§III A, imediatamente após a eq. (18)** — o enunciado técnico, com
   a ressalva de que vale mesmo para `r` negativo.
3. **§VI (Conclusões):** a condição para ausência de fantasmas é
   *"surprisingly equivalent to `r′ > 0`"*, e satisfazê-la garante lapso
   positivo de `f`, ligado à ausência do fantasma de helicidade-2.

**Sob que hipóteses** (todas declaradas na §III A, e todas necessárias):

- **`ρ > 0`** e **`1 + w_tot > 0`** — sem a segunda, (17) inverte o
  sinal e a equivalência (16)⟺(18) **cai**. Note que isto é uma
  condição sobre o fluido de matéria, não sobre a energia escura
  efetiva (que o próprio paper conclui ser **phantom**, `w_mg < −1`,
  eq. 20 — a §III B).
- **universo em expansão**: `t = ln a` cresce. Em contração, `dt < 0` e
  o mesmo `ρ_{,r} ≤ 0` dá `r` decrescente em tempo cósmico. O paper usa
  isso explicitamente na §V.
- **`r ≥ 0`** (§II, sem perda de generalidade).

**O que "saúde" significa ali — precisamente dois canais, e NÃO três:**

| Canal | Está dentro do "r′ > 0"? | Onde |
|---|---|---|
| **Higuchi / helicidade-0** | **SIM** — é *a* condição, por construção | §III A |
| **helicidade-2 (tensorial)** | **SIM, mas por implicação, não por identidade** | §III C |
| **gradiente escalar** | **NÃO** — é condição *separada e adicional* | §IV |

O elo helicidade-2 é este (§III C, e é curto): o único fator do lapso
de `f_{μν}` que não é estritamente positivo é **`r + r′`**; logo o
único jeito de ter lapso negativo é `r′` negativo; logo Higuchi ⟹ lapso
positivo. E o lapso de `f` é, por **Cusin, Durrer, Guarato & Motta
[arXiv:1412.5979]**, o fator relativo entre os cinéticos tensoriais de
`g` e `f` — lapso negativo ⟹ fantasma de helicidade-2. **Portanto, na
fonte, a saúde tensorial NÃO é uma condição de massa: é o sinal do
lapso de f.** (Ver §3.3 — isto atinge diretamente o uso que o
repositório faz de `m_T² ≥ 2H²`.)

### 1.4 O infinite branch (pergunta 4)

**Definição, §I, verbatim no essencial:** em soluções de *finite branch*
a razão evolui de zero para um valor assintótico finito; em *infinite
branches* `r` *"becomes infinitely large at early times and decreases
with time"*. Tudo o mais é chamado de *exotic branch* (quiques,
universo estático no passado/futuro assintótico).

**A afirmação de que `r` decresce aparece em dois níveis:**

- **Como fato citado** (§III A): *"`r′` is negative on all infinite
  branches"*, atribuído a **Könnig, Patil & Amendola, JCAP 1403, 029
  (2014) [arXiv:1312.3208]**.
- **Como derivação própria** (§V): as eqs. (13) e (12) dão o limite
  **`r′ ∝ −r`** quando `r → ∞` — **"as long as the density does not
  vanish"**. É esta a hipótese que sustenta a exclusão; ela está
  declarada e é verificável caso a caso.

Disso a §V tira a **conclusão numerada 5**: os limites `r → 0` e
`r → ∞` **não são pontos assintóticos viáveis** — o segundo
explicitamente *"due to the violation of the Higuchi bound"*.

### 1.5 O que a fonte diz sobre o IBB (pergunta 5) — **e os trabalhos citados**

*(Relato da fonte. Este documento não conclui nada sobre o IBB da F1.)*

**§I, o parágrafo inteiro, que é o mapa que o R-b pedia:**

- *"It seems that only one specific class of models, the
  infinite-branch bigravity (IBB), is free of scalar instabilities"* —
  atribuído a **Könnig, Akrami, Amendola, Motta & Solomon, PRD 90,
  124014 (2014) [arXiv:1407.4331]**, que é exatamente a fonte do R-12i.
  Definição repetida ali: IBB = soluções de ramo infinito com
  **β₂ e β₃ nulos**.
- IBB concorda bem com observações no fundo e no nível linear —
  1407.4331 e **Enander, Akrami, Mörtsell, Renneby & Solomon
  [arXiv:1501.02140]**.
- **Ressalva 1 — violação do Higuchi no limite inicial:**
  *"Unfortunately, the authors in Ref. […] noted that the Higuchi bound
  is generally violated in the early time limit."* →
  **⇒ MACARENA LAGOS & PEDRO G. FERREIRA, JCAP 1412, 026 (2014)
  [arXiv:1410.0207].**
- **Ressalva 2 — ghost de helicidade-2 em tempos iniciais:**
  *"it was found that cosmological solutions on this infinite branch
  suffer from a ghost in the helicity-2 sector at early times"* →
  **⇒ G. CUSIN, R. DURRER, P. GUARATO & M. MOTTA [arXiv:1412.5979].**
- Ressalva 3, menos citada e vale registrar: mesmo com o IBB bem
  comportado no nível linear, *"the appearance of the Higuchi ghost may
  only be visible at higher orders or maybe even only in the full
  solution"* — **R. P. Woodard, Lect. Notes Phys. 720, 403 (2007)
  [astro-ph/0601672]**.

**O paper emite veredito próprio sobre o IBB? SIM — e é mais forte que
as duas ressalvas que ele cita.** Duas vezes:

- §III A: como `r′ < 0` em todo ramo infinito, esses ramos sofrem do
  fantasma de Higuchi **em todos os tempos** — e isso *"confirms the
  findings"* de Lagos–Ferreira de que o limite é violado **ao menos**
  em tempos iniciais. Ou seja: **ele promove "early times" a "all
  times".**
- §VI: *"all infinite branches suffer from the Higuchi ghost at all
  times and a ghost in the helicity-2 sector at early times"*.

E na §IV A ele **mantém** o resultado de gradiente do IBB: usando a
condição (31) e a identidade (35), os modos escalares do IBB são
estáveis, e a condição (36) é *"equivalent to the condition `ρ > 0` on
that branch and, therefore, trivially satisfied at all times"*.
**Isto é decisivo para a leitura correta: o paper NÃO retrata o
resultado de gradiente de 1407.4331 — ele o confirma, e mata o IBB por
outro canal.** É exatamente a "separação de canais" do §1.6.

**Registro de escopo obrigatório.** Este parágrafo é o que a fonte diz
sobre o IBB **dela** (β₂ = β₃ = 0, `M_f = M_g`, matéria acoplada só a
`g`, fundo FLRW nos dois setores). A F1 do repositório com β₄ ligado
**não foi medida aqui**, e nada acima autoriza a medi-la por analogia.

### 1.6 A separação de canais (pergunta 6) — **sim, e é a arquitetura do paper**

Três perguntas distintas, em seções distintas, com pesos epistêmicos
**diferentes**:

| Canal | Seção | Critério | Peso que a fonte lhe dá |
|---|---|---|---|
| Higuchi / helicidade-0 | §III A | eq. (14) ⟺ `r′ ≥ 0` | **fatal** |
| Tensorial / helicidade-2 | §III C | **sinal do lapso de f** = sinal de `r + r′` | **fatal** (mas implicado pelo anterior) |
| Gradiente escalar | §IV | `ω² < 0` no limite sub-horizonte | **NÃO fatal** |

A articulação é feita explicitamente em duas frases da §VI: a
existência de um fantasma torna o modelo não-físico e obriga a
descartá-lo, enquanto modos escalares instáveis *"will not necessarily
rule out the theory"* — blindagem de Vainshtein pode impedir a
instabilidade, e ela não está presente em todos os tempos. E a §III D
justifica a assimetria: fantasma ⟹ Hamiltoniano ilimitado por baixo ⟹
decaimento do vácuo (Woodard 2007); e, citando **Sbisà, Eur. J. Phys.
36, 015009 (2015) [arXiv:1406.4550]**, nem sequer o argumento de
teoria efetiva salva — só modos de energia positiva desacoplam.

O **teorema da §V** é a costura dos três: toda solução física não
equivalente a ΛCDM tem uma época em que **ou** há instabilidade de
gradiente **ou** aparece o fantasma de Higuchi. A demonstração é por
classificação exaustiva de tipos de ramo (conclusões numeradas 1–8),
e o passo final (conclusão 8) é: `B_{2,r}` negativo em torno de um polo
⟹ instabilidade de gradiente; positivo ⟹ viola Higuchi ou dá escalares
instáveis.

> **Consequência direta para o corpus.** A "separação de canais" que o
> `posicionamento_literatura.md` §2b registrou como *inferência* está
> **VERIFICADA NA FONTE**: é a estrutura declarada do paper, não uma
> leitura nossa. E a assimetria de peso (fantasma fatal, gradiente
> não) é **da fonte**, e reforça o risco **R-a** do R-12i §6 (a nossa
> palavra "no-go" para o gradiente é mais forte do que a da
> literatura sobre o mesmo cálculo).

### 1.7 Formas fechadas (pergunta 7)

**Para `m_T²` ou `m_FP²`: NENHUMA. Resultado negativo, e é firme.** O
paper **não escreve** a massa do gráviton em lugar nenhum. A única
ocorrência de massa numa inequação é a citação histórica da §I —
Higuchi mostrou que um spin-2 com `0 < m² < 2H²` em de Sitter tem norma
negativa. **A condição de Higuchi do paper está escrita só em `r` e
`β_n`.** Quem quiser a forma "massa ≥ 2H²" tem de construí-la — é o que
o §2.2 faz.

**Para a condição de Higuchi em função de `r` e dos `β_n`:** eqs. (14),
(15), (19) acima. Mais a forma independente dos β: `ρ_{,r} ≤ 0` (16),
`r′ ≥ 0` (18).

**Para o setor escalar (bônus, fora do pedido mas conferido):**

$$\omega^{2}_{\beta_0\beta_1\beta_4}=\left(\frac{k}{\mathcal H}\right)^{2}\frac{r''}{3r'} \qquad (24)$$

válida para `β₂ = β₃ = 0` e matéria escura só; e

$$\omega^{2}_{\beta_{1}}=\frac{1+2w-6r^{2}(w+2)-9r^{4}}{\left(3r^{2}+1\right)^{2}}\left(\frac{k}{\mathcal H}\right)^{2}\;\simeq\;\frac{1+2w}{\left(3r^{2}+1\right)^{2}}\left(\frac{k}{\mathcal H}\right)^{2} \qquad (40)$$

**ARMADILHA DE SINAL, declarada.** Este paper usa o ansatz
`Ξ_i ∝ e^{ωt}` (§IV) — **exponencial real**, não `e^{iωN}`. Logo
**`ω² < 0` ⟹ oscilante ⟹ estável**, o oposto da convenção de
1407.4331. Confirmação: `ω²(24) = +(k/ℋ)²r''/(3r')`, enquanto o R-12i
extraiu de 1407.4331 `c_s² = −r''/(3r')`. **São a mesma física com o
sinal de ω² trocado.** Quem importar (24) sem notar isso troca estável
por instável — é a mesma classe de erro do "0.28".

---

## 2. A TRADUÇÃO — o entregável central

**Status: álgebra deste documento, feita à mão, não verificada por CAS.**
Está escrita passo a passo abaixo justamente para poder ser auditada.

### 2.1 O mapa de convenções — e ele é único

Não traduzo pela ação (onde os sinais de `R` diferem e o risco de erro
é alto). Traduzo pelas **duas equações de Friedmann**, que os dois
lados escrevem explicitamente.

**Do lado de Könnig**, dividindo (10) e (11) por `a²` (`H = ℋ/a`):

$$3H^{2}=\rho_K+V_g^K(r_K),\qquad
3H^{2}=\frac{1}{r_K}\big(\beta_1^K+3\beta_2^Kr_K+3\beta_3^Kr_K^2+\beta_4^Kr_K^3\big)=r_K^{2}V_f^K(r_K)$$

**Do nosso lado** (fonte: `auditoria/code/ramo_dinamico_correto.py`,
`m²M_ef²·W(r) = ρ` com `W = (M_g²/M_f²)r²V_f − V_g`, e
`derivations/04`):

$$3M_g^{2}H^{2}=\rho+m^{2}M_{\rm ef}^{2}V_g(r),\qquad
3H^{2}=\frac{m^{2}M_{\rm ef}^{2}}{M_f^{2}}\,r^{2}V_f(r)$$

com `V_g = β₀+3β₁r+3β₂r²+β₃r³`, `V_f = β₄+3β₃r⁻¹+3β₂r⁻²+β₁r⁻³`,
`M_ef⁻² = M_g⁻² + M_f⁻²`, `μ = M_f²/M_g²`.

**Ansatz de tradução:** `r_K = c·r` e `β_n^K = A·c^{−n}·β_n` com
`A ≡ m²M_ef²/M_g²`, `ρ_K = ρ/M_g²`. A forma de `β_n^K` é **forçada**
pela Friedmann-g: substituindo, o termo `n` dá
`A c^{−n}β_n·c^n r^n = Aβ_n r^n`, e a soma reproduz `A·V_g(r)`
para qualquer `c` — que é exatamente `(m²M_ef²/M_g²)V_g`. ✔

**`c` é então fixado, e sobredeterminado, pela Friedmann-f.**
Substituindo na (11'):

$$\frac{1}{cr}\Big[Ac^{-1}\big(\beta_1+3\beta_2 r+3\beta_3 r^{2}\big)+\beta_4^K c^{3}r^{3}\Big]$$

Para o primeiro bloco casar com `(A/μ)(β₁+3β₂r+3β₃r²)/r` é preciso
`c^{−2} = 1/μ`, ou seja

$$\boxed{\,c=\sqrt{\mu}\;\Longrightarrow\;r_K=\sqrt{\mu}\,r,\qquad
\beta_n^{K}=\frac{m^{2}M_{\rm ef}^{2}}{M_g^{2}}\,\mu^{-n/2}\beta_n,\qquad
\rho_K=\frac{\rho}{M_g^{2}}\,}$$

e o termo `n = 4`, que a Friedmann-g não fixava, sai
`β₄^K = Aμ^{−2}β₄` — **exatamente o padrão `μ^{−n/2}`**. O mapa é
único e a sobredeterminação fecha: é isso que autoriza chamá-lo de
tradução e não de ajuste.

**Conferência independente do mapa** (recomputada do zero):

$$\frac{1}{r_K}\sum_n \beta_n^K r_K^{\,n-1}\Big|_{n=1..4}
= A\mu^{-1/2}\frac{\beta_1+3\beta_2r+3\beta_3r^{2}+\beta_4r^{3}}{\sqrt\mu\,r}
= \frac{A}{\mu}\,r^{2}V_f(r)=\frac{m^{2}M_{\rm ef}^{2}}{M_f^{2}}r^{2}V_f(r)\;✔$$

usando `β₁+3β₂r+3β₃r²+β₄r³ = r³V_f(r)` (identidade imediata) e
`A/μ = m²M_ef²/M_f²`.

**Interpretação:** o mapa é a redundância que a nota de rodapé 6 do
paper declara — reescalar `f → μf` leva `M_f → M_g` e, como
`b = ra`, **leva `r → √μ r`**. **O `μ` do repositório não some na
tradução: ele reaparece como um reescalamento de `r`.** Quem comparar
`r` nosso com `r` deles sem esse fator, em `μ ≠ 1`, compara coisas
diferentes.

**Consequência imediata e μ-independente:** `μ > 0` constante ⟹
`r_K' = √μ r'`. **O sinal de `r′` é invariante sob a tradução.** Logo
`r' ≥ 0` (eq. 18) e `ρ_{,r} ≤ 0` (eq. 16) valem **sem nenhuma
tradução**: são enunciados sobre sinais, imunes a `μ`, a `m²M_ef²` e à
normalização dos β. *(Isto responde o item mais frágil da fila do
R-b: aquele enunciado específico já era comensurável.)*

### 2.2 A inequação de Higuchi nas NOSSAS variáveis

Aplicando o mapa à eq. (15). Com `A ≡ m²M_ef²/M_g² > 0`,
`r_K^2 = μr²`, `r_K^3 = μ^{3/2}r³`, `r_K^4 = μ²r⁴`:

- `β₁^K = Aμ^{−1/2}β₁`
- `3r_K²(β₁^K−β₃^K) = 3μr²·A(μ^{−1/2}β₁ − μ^{−3/2}β₃) = 3A(μ^{1/2}β₁r² − μ^{−1/2}β₃r²)`
- `2r_K³(3β₂^K−β₄^K) = 2μ^{3/2}r³·A(3μ^{−1}β₂ − μ^{−2}β₄) = 2A(3μ^{1/2}β₂r³ − μ^{−1/2}β₄r³)`
- `3r_K⁴β₃^K = 3μ²r⁴·Aμ^{−3/2}β₃ = 3Aμ^{1/2}β₃r⁴`

Dividindo tudo por `Aμ^{−1/2} > 0`:

$$\boxed{\;\beta_1+3r^{2}\big(\mu\beta_1-\beta_3\big)+2r^{3}\big(3\mu\beta_2-\beta_4\big)+3\mu\beta_3 r^{4}\;\geq\;0\;}
\qquad \text{[(15) nas nossas variáveis]}$$

que em `μ = 1` reduz à (15) impressa. ✔

Aplicando o mapa à eq. (14). O parêntese esquerdo é
`β₁^K + 2β₂^K r_K + β₃^K r_K² = Aμ^{−1/2}(β₁+2β₂r+β₃r²)`, e o lado
direito é `Aμ^{−1/2}(β₁+3β₂r+3β₃r²+β₄r³) = Aμ^{−1/2}r³V_f(r)`.
Cancelando `Aμ^{−1/2}`:

$$\boxed{\;\tfrac{3}{2}\,\mathcal B(r)\,\big(1+\mu r^{2}\big)\;\geq\;r^{3}V_f(r)\;=\;\frac{3M_f^{2}}{m^{2}M_{\rm ef}^{2}}\,r\,H^{2}\;}
\qquad \text{[(14) nas nossas variáveis]}$$

onde **`ℬ(r) ≡ β₁ + 2β₂r + β₃r²` é, letra por letra, o `ℬ(r)` do
cap. 03 §0** — o `B₂` de Könnig **é** o nosso `ℬ`. E a última
igualdade é a nossa própria Friedmann-f resolvida para `r³V_f`.

Isolando `H²`:

$$\boxed{\;\frac{m^{2}M_{\rm ef}^{2}}{M_f^{2}}\;\mathcal B(r)\;\frac{1+\mu r^{2}}{r}\;\geq\;2H^{2}\;}
\qquad \textbf{[A forma "massa ≥ 2H²" do critério de Higuchi]}$$

**Hipóteses declaradas desta reescrita** (todas herdadas da fonte,
nenhuma acrescentada):

1. `r ≥ 0` e `μ > 0` constante (`μ` constante é o que permite
   `r_K' = √μ r'`; se `μ` variasse no tempo, o mapa não seria uma
   mudança de variável de fundo).
2. `m²M_ef²` constante — **atenção**: na v2 a modulação está absorvida
   em `β_n(φ₋)`, e o mapa acima trata os `β_n` como funções de `r`
   só. Com `β_n(φ₋(N))`, a inequação continua valendo **ponto a
   ponto**, mas a cadeia (14)→(16)→(18) usa `ρ_{,r}` a `β` fixo e
   **não** sobrevive intacta. **Fora do escopo verificado.**
3. Para a forma `r′ ≥ 0`: adicionalmente `ρ > 0` e `1 + w_tot > 0`
   (§1.3). O `ρ` relevante é a **matéria**, não a energia escura
   efetiva.
4. Matéria acoplada só a `g`, dois setores FLRW — a fonte declara
   ambas (§VI) como limitação do trabalho dela. **Coincide com a
   nossa ação** (cap. 03 §1).

### 2.3 `ξ` é o mesmo objeto — e a condição vira `ξ ≥ r`

A métrica `f` da fonte (eq. 5) é `b²(−X²ℋ⁻²dt² + dx²)`, contra
`a²(−ℋ⁻²dt² + dx²)` para `g` (eq. 4). Logo os lapsos são
`N_f = bX/ℋ` e `N_g = a/ℋ`, e

$$\frac{N_f}{N_g}=\frac{bX}{a}=r\,X \overset{(9)}{=} r\left(1+\frac{r'}{r}\right)=r+r'$$

**que é, letra por letra, o `ξ = r + dr/dN` do repositório** (grep:
`xi = r + drdN` em 13 scripts de `auditoria/code`). Sob a tradução,
`ξ_K = r_K + r_K' = √μ(r+r') = √μ·ξ` — fator positivo, **mesmo sinal,
mesmo zero**.

Portanto:

$$\textbf{Higuchi (fonte)}\;\Longleftrightarrow\;r'\geq 0\;\Longleftrightarrow\;\boxed{\;\xi\;\geq\;r\;}$$

e o critério tensorial da fonte (§III C, lapso de `f` positivo) é

$$\boxed{\;\xi\;>\;0\;}$$

— **que é literalmente o critério "lapso físico ξ > 0" da tabela do
cap. 05 §2.** O repositório e a fonte usam o mesmo objeto para o setor
tensorial; o que o repositório **não** tinha era a hierarquia entre os
dois (`ξ ≥ r` é estritamente mais forte que `ξ > 0` para `r > 0`).

---

## 3. Comparação com o `m_T² ≥ 2H²` que o repositório usa hoje

Forma em uso (cap. 06 §2 e §4; `derivations/02_setor_tensorial_mT2.md`
§3.3):

$$m_T^{2}=m^{2}M_{\rm ef}^{2}\left(\frac{1}{M_g^{2}}+\frac{\xi}{M_f^{2}r^{3}}\right)r\big[\beta_1+\beta_2(\xi+r)+\beta_3\,\xi r\big]\;\geq\;2H^{2}$$

### 3.1 São a mesma inequação? — **Sim em `ξ = r`; não fora dali**

Avaliando a caixa do cap. 06 em `ξ = r`. O prefator vira
`(1/M_g² + 1/(M_f²r²))`; usando `1/M_g² = μ/M_f²`:

$$\frac{1}{M_g^{2}}+\frac{1}{M_f^{2}r^{2}}=\frac{1}{M_f^{2}}\left(\mu+\frac{1}{r^{2}}\right)=\frac{1+\mu r^{2}}{M_f^{2}r^{2}}$$

e o colchete vira `β₁+2β₂r+β₃r² = ℬ(r)`. Logo

$$m_T^{2}\Big|_{\xi\to r}=\frac{m^{2}M_{\rm ef}^{2}}{M_f^{2}}\,\mathcal B(r)\,\frac{1+\mu r^{2}}{r}$$

que é **idêntico, termo a termo, ao lado esquerdo da caixa do §2.2.**

> $$\boxed{\;\text{Könnig (14)}\;\;\Longleftrightarrow\;\;m_T^{2}\big|_{\xi\to r}\;\geq\;2H^{2}\;}$$
>
> **Exato, para `μ` arbitrário e todos os `β_n`.** Não há fator
> residual, não há aproximação.

Isso é forte em dois sentidos. Primeiro, é uma **validação cruzada**: a
caixa de `m_T²` da `derivations/02` — derivada por maquinaria
independente (ação TT, Sylvester, autovalor de `K⁻¹M`) — reproduz
exatamente o bound FLRW de Fasiello–Tolley no limite `ξ = r`. Duas
rotas totalmente distintas, mesmo objeto. Segundo, **localiza a
discrepância num único ponto**: `ξ`.

### 3.2 Diferem por quê, exatamente

Por dois fatores, ambos iguais a 1 sse `ξ = r`:

$$\frac{m_T^{2}}{\,m_T^{2}\big|_{\xi\to r}}
=\underbrace{\frac{\mu r^{3}+\xi}{\mu r^{3}+r}}_{\text{cinético}}\;\cdot\;
\underbrace{\frac{\beta_1+\beta_2(\xi+r)+\beta_3\,\xi r}{\beta_1+2\beta_2 r+\beta_3 r^{2}}}_{\text{massa}}$$

**Regime de validade — é aqui que a diferença mora.** `ξ = r ⟺ r′ = 0`:
**fundo proporcional** (`f ∝ g`), de Sitter, ponto fixo. Ou seja: o
bound de Higuchi da fonte, escrito como massa, é o bound de de Sitter
`m² ≥ 2H²` **com a massa avaliada no fundo proporcional instantâneo**,
e não com a massa dinâmica. Fora do ponto fixo os dois objetos
divergem, e divergem justamente onde `r′ ≠ 0` — que é o observável que
a própria fonte usa como critério.

*(Que a forma "massa" do bound de FLRW coincida com a forma de de
Sitter com `ξ → r` é **inferência minha** sobre o significado da
identidade algébrica, não afirmação da fonte. A identidade em si é
álgebra, e está exibida acima.)*

**Ordem de grandeza da diferença, no caso que o repositório já publicou**
— *consequência algébrica direta da caixa do cap. 06 §2, NÃO
re-verificada numericamente:* no ramo finito primordial (`r → 0`,
`ξ = 4r`, F1 com `β₃ = 0`), os dois colchetes tendem ambos a `β₁`, e o
fator cinético tende a `4r/r = 4`. Como o cap. 06 §2 estabelece
`m_T² ≃ 4m²M_ef²β₁/(M_f²r)` e `H² → m²M_ef²β₁/(3M_f²r)`, dando
`m_T²/H² → 12`, o objeto de Könnig dá **`m_T²|_{ξ→r}/H² → 3`**. Ainda
`≥ 2`, mas a margem cai de fator 6 para fator 1.5.

**Consistência independente:** a fonte afirma (§III A) que todo ramo
finito com fundo viável satisfaz Higuchi, porque a viabilidade força
`r′ ≥ 0`; e o nosso ramo finito primordial tem `r′ = 3r > 0`
(cap. 05 §2). **As duas rotas — a forma "massa" dando 3 ≥ 2, e o
critério `r′ ≥ 0` — concordam.** Isso é evidência a favor de que a
tradução do §2 está certa.

### 3.3 A diferença mais importante não é numérica: é de canal

| | Repositório hoje | Könnig 1503.07436 |
|---|---|---|
| Objeto | `m_T²`, autovalor de massa do setor **TT (helicidade-2)** | funcional de Higuchi, saúde do modo **helicidade-0** |
| Forma | `m_T² ≥ 2H²` (bound de de Sitter aplicado) | eq. (14), sem massa nenhuma |
| Critério **tensorial** | o próprio `m_T² ≥ 2H²` | **sinal do lapso de f**, `ξ > 0` (§III C, via Cusin et al.) |
| `ξ` | dinâmico, `ξ = r + r′` | idem, mas **não entra** no bound de Higuchi |

Ou seja: o repositório usa **uma** inequação de massa para responder o
que a fonte trata como **dois** critérios de naturezas diferentes (um
funcional em `β,r` para helicidade-0; um sinal de lapso para
helicidade-2). Sob a tradução:

- o critério helicidade-0 da fonte = `m_T²|_{ξ→r} ≥ 2H²` = `r′ ≥ 0` =
  `ξ ≥ r`;
- o critério helicidade-2 da fonte = `ξ > 0` — **já presente no
  cap. 05 §2 como "lapso físico"**, mas nunca ligado a Higuchi;
- o `m_T² ≥ 2H²` com `ξ` dinâmico, como o repositório o usa hoje,
  **não é nenhum dos dois** e não tem correspondente na fonte.

**Recomendação (não executada — nenhum arquivo existente foi tocado).**
Onde o cap. 06 §2 diz "Higuchi (`m_T² ≥ 2H²`)", a atribuição correta é:
*"o bound de de Sitter aplicado à massa tensorial dinâmica; o bound de
Higuchi em FLRW (Fasiello–Tolley 1308.1647; Könnig 1503.07436 eq. 14)
é a mesma expressão com `ξ → r`, e é equivalente a `r′ ≥ 0`."* E o
número `12` merece a nota de que o objeto de Könnig dá `3` no mesmo
limite.

---

## 4. Sub-produtos verificados

### 4.1 A eq. (40) confirma o erratum que o R-12i registrou em 1407.4331

O R-12i §1.5 registrou que a eq. (69) da PRD de 1407.4331 tem
`(1+3r²)` **sem quadrado** dentro da raiz, incompatível com a
identidade (76) do próprio paper, e concluiu tratar-se de typo da
fonte. **Confirmado aqui, por terceira rota independente:** a eq. (40)
deste paper (mesmo autor, ano seguinte, mesmo modelo β₁-puro) imprime
o denominador **`(3r²+1)²`**, ao quadrado, nas duas rotas de extração.
Em `w = 0`, (40) dá `ω² = −(9r⁴+12r²−1)/(3r²+1)²·(k/ℋ)²`, que é
exatamente `−c_{s,K}²(k/ℋ)²` do R-12i — inclusive o sinal, pela
troca de ansatz do §1.7. **O erratum está fechado.**

Bônus: (40) mostra a dependência em `w` que 1407.4331 não exibia. O
numerador é `1+2w−6r²(w+2)−9r⁴`, e a fonte lê dele que há modos
instáveis para `r` pequeno **enquanto `w > −1/2`** — a condição
`c_s²(r→0) = −1` do R-11 é o caso `w = 0`, e o limiar geral é `w = −1/2`.

### 4.2 `B₂ = ℬ(r)`: o ramo algébrico da v1 fica na fronteira do bound

Da §2.2: `B₂` de Könnig é o nosso `ℬ(r) = β₁+2β₂r+β₃r²`. O cap. 03 §0
registra que **o ramo algébrico da v1 fixa `r` na raiz de `ℬ(r) = 0`**.
Mas a eq. (14) com `ℬ = 0` dá `0 ≥ (3M_f²/m²M_ef²)rH²`, logo
`rH² ≤ 0` — o ramo algébrico só sobrevive ao bound de Higuchi com
`H = 0` (ou `r = 0`).

**Não é veredito novo:** o ramo algébrico já foi superado pelo
Erratum-01 e substituído pelo ramo cinemático (cap. 04–05). Registro
porque é uma **âncora de validação a mais** — a tradução reencontra, por
um canal totalmente diferente (Higuchi), uma patologia que o
repositório achou por outro (Bianchi). Marcado como consequência da
álgebra do §2, não re-derivado.

### 4.3 Energia escura phantom — um observável que o corpus não usava

§III B, eq. (20): `w_mg = −1 − (B₂/ρ_mg)r′`. Com `ρ_mg > 0` e o bound
(`B₂ ≥ 0`, `r′ ≥ 0`), segue `w_mg ≤ −1`: **toda solução sem fantasma
de Higuchi tem energia escura phantom.** Nas nossas variáveis,
`B₂ → ℬ(r)` e `ρ_mg → V_g(r)` (a menos do fator `m²M_ef²/M_g²` comum,
que cancela na razão), e o `r′` é o nosso — então a fórmula é
diretamente utilizável:

$$w_{mg}=-1-\frac{\mathcal B(r)}{V_g(r)}\,\frac{dr}{dN}\qquad\text{[tradução; hipótese: }\beta_n\text{ constantes]}$$

A fonte trata isso como **assinatura observacional**, não como
patologia (§III B: a EOS depende fortemente do tempo e tende a −1 no
futuro assintótico; um phantom em bigravidade *"is not as frightening
as in ΛCDM"*). O cap. 09 não tem esse observável.

---

## 5. Fronteiras deste documento

- **Verificado na fonte:** todo o §1 (as sete perguntas), por duas
  rotas independentes, com as quatro conferências de integridade do §0.
- **Álgebra deste documento, à mão, NÃO verificada por CAS:** o mapa do
  §2.1, as duas caixas do §2.2, a identidade do §3.1, a razão do §3.2,
  os §4.2 e §4.3. **Item 1 da fila: passar tudo isso por sympy.**
- **Inferência (marcada como tal):** a leitura de que a forma "massa"
  do bound de FLRW é a forma de de Sitter avaliada no fundo
  proporcional instantâneo (§3.2). A identidade algébrica não depende
  dessa leitura.
- **NÃO verificado:** o comportamento do mapa com `β_n(φ₋)` dependentes
  do tempo (§2.2, hipótese 2). A cadeia (14)→(16)→(18) usa `ρ_{,r}` a
  β fixo; com modulação ligada, só a forma (14) sobrevive ponto a
  ponto, e a equivalência com `r′ ≥ 0` **não está estabelecida**.
- **NÃO verificado:** o paper de Fasiello–Tolley (1308.1647), de onde a
  (14) vem. Todo o §1.1 é a versão *de Könnig* dela, com o caveat
  declarado do fator `1/2` no potencial. Se o cap. 06 for citar a fonte
  primária do bound, **1308.1647 tem de ser aberto** — e o fator 2 nos
  β conferido.
- **NÃO verificado:** Lagos–Ferreira (1410.0207), Cusin et al.
  (1412.5979), Yamashita–Tanaka (1401.4336). São **nível de citação**:
  sei o que 1503.07436 diz que eles dizem, e as referências
  bibliográficas completas — não abri nenhum.
- **FORA DE ESCOPO, por instrução:** qualquer conclusão sobre o ramo
  infinito / IBB da F1. Este documento entrega o critério traduzido e
  para aí. O veredito `IBB REABERTO` do
  `posicionamento_literatura.md` §2b **permanece exatamente como está**;
  nada aqui o move, em nenhuma direção.

---

## 6. Fila que este resultado abre

1. **Verificação simbólica do §2** (sympy: mapa, as duas caixas, a
   identidade `m_T²|_{ξ→r}`). Barato e fecha a única fronteira
   epistêmica real deste documento.
2. **O teste de tradução do R-b, agora executável.** A especificação do
   `posicionamento_literatura.md` §2b pedia *"o funcional/inequação de
   Higuchi usado em 1503.07436"* na convenção do projeto — está no
   §2.2. Célula IBB genuína (`β₂ = β₃ = 0`, `β₁ > 0`, `0 < β₄ < 2β₁`),
   ramo infinito, medir `r′(N)`, `ξ(N)`, `ℬ(r)(1+μr²)/r` contra `2H²`.
   **Quem mede é outro processo.**
3. **Cap. 06 §2 e §4:** a atribuição de `m_T² ≥ 2H²` (§3.3), e a nota
   de que o bound de Higuchi propriamente dito dá `3` onde o texto diz
   `12`. Recomendação, não executada.
4. **Abrir Fasiello–Tolley 1308.1647** e conferir o fator `1/2` do
   potencial — é a fonte primária real do bound, e o repositório a cita
   (`posicionamento_literatura.md` linha 520) sem tê-la aberto.
5. **`w_mg ≤ −1` como predição** (§4.3): observável novo, já na nossa
   convenção, ausente do cap. 09.
6. **Registrar a armadilha de sinal do §1.7** no
   `docs/posicionamento_literatura.md`: 1407.4331 usa `e^{iωN}`,
   1503.07436 usa `e^{ωt}`; `ω² < 0` significa coisas opostas nos dois.
