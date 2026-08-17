# AUDITORIA ADVERSARIAL DO ARCO R-13 (R-13a + R-13b)

**Data:** 2026-08-17. **Alvo:** `docs/resultado_r13a_criterio_higuchi_fonte.md`,
`docs/resultado_r13b_ibb_ramo_infinito.md` e a linha de veredito que eles
sustentam em `docs/posicionamento_literatura.md` §1.1b e §2b.

**Scripts desta auditoria** (todos com critérios pré-declarados no
cabeçalho, `np.gradient` travado por exceção, saídas versionadas em
`auditoria/code/out/`):

| Alvo | Script | Saída |
|---|---|---|
| A + D | `auditoria/code/r13aud_a_mapa_e_traducao.py` | `out/r13aud_a_mapa_e_traducao.txt` |
| B | `auditoria/code/r13aud_b_armadilha_de_sinal.py` | `out/r13aud_b_armadilha_de_sinal.txt` |
| C | `auditoria/code/r13aud_c_cs2_ibb.py` | `out/r13aud_c_cs2_ibb.txt` |
| E | `auditoria/code/r13aud_e_borda.py` | `out/r13aud_e_borda.txt` |
| F | `auditoria/code/r13aud_f_cegueiras.py` | `out/r13aud_f_cegueiras.txt` |

---

## 0. Veredito por alvo, em uma tabela

| Alvo | Objeto | Veredito | O que mudou |
|---|---|---|---|
| **A** | a tradução `Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0` | **CONFIRMADO — e estendido** | o mapa sai de uma **segunda rota independente** (a redundância da ação, não as Friedmann); a cadeia vale para **todo `w > −1`**, não só poeira |
| **B** | a armadilha de sinal entre 1407.4331 e 1503.07436 | **CONFIRMADO na fonte, verbatim** | nada; a leitura do R-13a está literalmente escrita nos dois papers, e a inversão seria total se ignorada |
| **C** | o elo do gradiente, não medido internamente | **FECHADO — `c_s² > 0` em 50/50** | o corpus passa a ter **os dois lados medidos por nós**; e apareceu um **defeito de instrumento** no caminho |
| **D** | `m_T²/H² = 3, não 12` | **CORRIGIDO no rótulo, CONFIRMADO no objeto** | o `12` está intacto; o que mudou foi só o rótulo. E a pendência **P-5 (6 vs 3) fica RESOLVIDA** |
| **E** | a borda `max r′ = −6.05e−5` | **CONFIRMADO — e a margem não existe** | a "margem estreita" é **número de grade**; o enunciado correto é um **teorema sem margem** |
| **F** | cegueira dos gates | **9 cegueiras listadas; 1 morde** | e o que ela morde é o **argumento**, não o veredito — o corpus tem de trocar o diagnóstico operacional |

**Nada do veredito central caiu.** O ramo infinito / IBB da F1 continua
excluído pelo ghost de Higuchi. Mas três coisas mudam de estatuto, e
duas delas para melhor:

1. o veredito deixa de depender de `r′ < 0` e passa a ter **prova em
   forma fechada** (§5);
2. a metade de literatura da frase de complementaridade vira **medida
   própria** (§4);
3. e o corpus ganha um **defeito de instrumento novo**, com raio de
   alcance mapeado (§4.2).

---

## 1. ALVO A — a tradução, re-derivada por rota independente

**Veredito: CONFIRMADO, com extensão.** *Script: `r13aud_a_mapa_e_traducao.py`.*

O R-13a obteve o mapa `r_K = √μ r`, `β_n^K = A μ^{−n/2} β_n` **casando
as duas equações de Friedmann**. Esta auditoria o obteve por outra
rota: a **redundância da ação** sob `f_{μν} → λ² f_{μν}`.

| Gate | O que testa | Resíduo |
|---|---|---|
| **A1** | `e_n(√(g⁻¹f))` do fundo, calculados pela raiz matricial de Sylvester + traços de `tdcp_pert_lib.py` (**não** por fórmula decorada), escalam como `e_n → λⁿ e_n` | **0, 0, 0, 0, 0** |
| **A2** | `−3M_f² b ḃ²/N_f → λ²·(idem)`, logo `M_f² → M_f²/λ²`, e `λ² = μ` leva `M_f² → M_g²` | **0** |
| **A3** | invariância de `Σβ_n e_n` força `β_n^K = λ^{−n}β_n`, **unicamente**, coeficiente a coeficiente | **0** ×5, solução única |
| **A4** | a Friedmann-g sozinha fixa `A_0..A_3 = A c^{−n}` e deixa `c` **livre** | **0** ×4 |
| **A5** | a Friedmann-f fixa `c² = μ` **e** `A_4 = Aμ^{−2}`, por duas condições independentes que dão o **mesmo** `c` | solução única `{A_4: A/μ², c: √μ}` |
| **A6a** | a eq. **(12)** de Könnig (que **não** entrou na construção) bate com a **nossa** `𝒲(r)` sob o mapa | **0** |
| **A6b** | a eq. **(13)** dá `r_K′ = √μ r′`, com **`w` geral** | **0** |
| **A7** | `ξ = N_f/N_g` literalmente (nossa convenção: `N_g = 1`, `N_f = ξ`), e `r X = r + r′` pela eq. (9) deles | **0**, **0** |
| **A8a** | `−μr²𝒲′(r) ≡` LHS da (15) traduzida | **0** |
| **A8b0** | caixa do cap. 06 com `ξ → r` ≡ caixa do R-13a §2.2 | **0** |
| **A8b** | `(m_T²\|_{ξ→r} − 2H²)·3M_f²r/(m²M_ef²) ≡` LHS(15) | **0** |
| **A8c** | `B₂` de Könnig sob o mapa ≡ `A μ^{−1/2} ℬ(r)` | **0** |
| **A9** | `w_mg = −1 − ℬ(r)r′/V_g(r)` derivada da **conservação** (rota própria), contra a tradução da eq. (20) deles | **0** |
| **A-PODER** | mapas **errados** (`c = μ`; `β_n ~ μ^{−n}`) têm de **reprovar** | resíduos **não nulos** ✔ |

### 1.1 O que a rota independente acrescenta

- **O mapa não é ajuste.** Ele sai da ação **sem olhar para as
  Friedmann**, e depois as Friedmann o **sobredeterminam**: a
  Friedmann-g deixa `c` livre, e a Friedmann-f o fixa por **duas vias
  independentes** (o bloco `β₁/β₂/β₃` e o termo `β₄`) que dão o mesmo
  `c`. O padrão `μ^{−n/2}` no `n = 4` **não foi imposto: saiu**.
- **A pendência P-6 do `posicionamento_literatura.md` FECHA.** Ela dizia
  que o mapa era "derivado à mão, entrada e não saída do R-13b". Agora
  é saída de duas rotas, com resíduo simbólico zero.

### 1.2 A extensão: a cadeia vale para todo `w > −1`

O R-13b verificou a cadeia por CAS **só para poeira**. Aqui:

$$\frac{dr}{dN}=-\frac{3(1+w)\,\tilde\rho}{\mathcal W'(r)}$$

O fator `(1+w)` é **positivo e comum**, e não toca a equivalência.
Logo `Könnig (14) ⟺ (15) ⟺ 𝒲′ ≤ 0 ⟺ r′ ≥ 0 ⟺ ξ ≥ r` vale para
**qualquer `w > −1`**, constante ou não — inclusive radiação, o que o
R-13b listava como não varrido.

### 1.3 O que a modulação quebra — localizado, não só declarado

Com `β_n(N)`:

$$\frac{dr}{dN}=-\frac{3(1+w)\tilde\rho+\left.\frac{d\mathcal W}{dN}\right|_r}{\mathcal W'(r)},
\qquad \left.\frac{d\mathcal W}{dN}\right|_r=\sum_n\dot\beta_n\,\partial_{\beta_n}\mathcal W$$

**A inequação (14)/(15) não usa `r′` e continua valendo ponto a ponto**
(ela é algébrica em `(r, β_n, μ)`). O que cai é **só a equivalência com
o sinal de `r′`**. Consequência operacional, desenvolvida no §6: sob
modulação, **medir `r′` não é medir Higuchi**.

---

## 2. ALVO B — a armadilha de sinal

**Veredito: CONFIRMADO na fonte, verbatim.**
*Script: `r13aud_b_armadilha_de_sinal.py`. Nível: VERIFICADO-NA-FONTE
(uma rota — HTML do ar5iv baixado e decodificado neste computador; o
R-13a usou duas, ar5iv + PDF).*

**1503.07436**, §IV, imediatamente após a eq. (31), verbatim:
> "in order to get stable scalar perturbations, i.e. `ω² < 0`"

e, após a eq. (23):
> "A negative value would imply oscillating and, therefore, stable"

com o ansatz `Ξ_i ∝ e^{ωt}` e `t` = tempo de e-folding (§II).

**1407.4331**, §V, verbatim:
> "substituting `X = X₀ e^{iωN}`"

com "real solutions (needed to obtain oscillating, rather than growing
and decaying, solutions for `X`)".

**As duas leituras estão nas fontes, literalmente, e são opostas.**

| Gate | Resultado |
|---|---|
| **B1** | `\|e^{i√s t}\| = 1` (oscila) contra `\|e^{iωN}\|_{ω=i√s} = e^{√s t}` (cresce) — a aritmética, explicitada |
| **B2** | `ω_K² + ω_{1407}² = 0` **identicamente** |
| **B2b** | `ω_{1407}² = c_s²(k/ℋ)²` com `c_s² = −r″/(3r′)` (a eq. 76 deles) ✔ |
| **B3** | o **conjunto** `{estável}` é o **mesmo** nas duas convenções: `r″/(3r′) < 0`. **As fontes não se contradizem** |
| **B5** | `r″ = −3r′ − r′²𝒲″/𝒲′` em forma fechada, confirmada por estêncil de 8ª ordem com refino em 8/8 pontos (≤ 1.1e−12) |
| **B6** | a condição **(36)** de Könnig **é** `ρ̃ > 0` nas nossas variáveis (resíduo 0), com generalização `β₄r³ + β₁ − 3μβ₁r² > 0` |

### 2.1 O contrafactual, medido

`ω_K²/(k/ℋ)² = r″/(3r′)` nas células IBB genuínas: **negativo em
5400/5400 pontos**, indo de **−1/2** no passado profundo a **−1** no
ponto fixo. Isto é *estável* na convenção de Könnig. Quem importasse o
mesmo número para a convenção de 1407.4331 leria **instável em 100% dos
pontos**. **A inversão seria total, e ela inverteria a frase de
complementaridade inteira.**

### 2.2 E a fonte de fato diz que o IBB é estável no gradiente

Extração própria de 1503.07436 §IV A, verbatim no essencial: com `r′`
sempre negativo no IBB a condição (34) deixa de valer, "however, we can
still use condition (31)"; o produto dos dois primeiros fatores é
positivo pela eq. (35), e então
> "stable modes are guaranteed if `3β₁r² < β₁+β₄r³`"

que "is equivalent to the condition `ρ>0` on that branch and,
therefore, trivially satisfied at all times".

**A leitura do R-13a §1.5 está correta: a fonte MANTÉM o resultado de
gradiente do IBB, e mata o IBB por outro canal.** *(Registro de método:
um resumo automático desta mesma seção afirmou o contrário. Só a
extração do texto integral resolveu. Fica o aviso.)*

---

## 3. ALVO D — o `3` e o `12`

**Veredito: CONFIRMADO no objeto, CORRIGIDO no rótulo. E a pendência
P-5 fica RESOLVIDA.** *Script: `r13aud_a_mapa_e_traducao.py`, bloco D.*

### 3.1 O que exatamente mudou: nem o número, nem o objeto — o rótulo

Formas fechadas obtidas nesta auditoria (limites simbólicos exatos,
`β_n` e `μ` gerais, `β₁ ≠ 0`):

$$\lim_{r\to0}\frac{m_T^2}{H^2}\bigg|_{\xi\ \rm dinâmico}=3(4+3w),
\qquad
\lim_{r\to0}\frac{m_T^2\big|_{\xi\to r}}{H^2}=3\quad\text{(para todo }w)$$

e a diferença entre os dois objetos zera **identicamente sse `ξ = r`**,
isto é, `r′ = 0`.

| | o `12` | o `3` |
|---|---|---|
| objeto | autovalor de massa tensorial (**helicidade-2**) sobre `H²`, com `ξ` dinâmico | funcional de Higuchi de Fasiello–Tolley/Könnig (**helicidade-0**) sobre `H²` |
| valor | **inalterado**, `3(4+3w)`: 12 em matéria, 15 em radiação | **3**, e não depende de `w` (`∂_w = 0`) |
| o que caiu | a **leitura** "margem enorme de Higuchi" | — |

**Portanto: o número não mudou, o objeto não mudou, e não há erratum de
valor. Mudou o rótulo — e só ele.** O `12` continua reivindicável como
razão de massa tensorial; nunca como margem de Higuchi.

### 3.2 A margem `1.5×` é a margem MÍNIMA — verificado

"Margem 1.5×" só é a margem se `3` for o **mínimo** do funcional sobre
a história. Medido no benchmark do corpus (`β = (1,1,−0.4,0,0.5)`,
`μ = 1`, `Ω_m(a=1) = 0.3`, poeira, `a ∈ [10⁻⁶, 10³]`, 4000 pontos, raiz
por Newton com `𝒲′` em forma fechada — resíduo 8.3e−16):

| | valor |
|---|---|
| mínimo de `m_T²\|_{ξ→r}/H²` | **3.000000** (em `r → 0`) |
| no ponto fixo tardio | 3.947347 |
| pontos com o funcional `≥ 2` | **4000/4000** |

**O `3` é o mínimo. A margem `1.5×` está correta como margem mínima no
ramo finito do benchmark.**

### 3.3 P-5 (a discrepância `6 vs 3` em `w = −1`) — RESOLVIDA

A fórmula `3(4+3w)` **não é avaliável em `w = −1`**, e a razão é
estrutural: a derivação usa `r ≈ β₁/(μρ̃)` com `ρ̃ → ∞`, o que **exige
que `ρ` dilua**, isto é `w > −1`. Em `w = −1` a densidade é constante,
`r` não vai a zero, e **o regime `r → 0` não existe**. Logo
`3(4+3w)|_{w=−1} = 3` é **extrapolação fora do domínio**, não predição.

O que existe em `w = −1` é o **ponto fixo de de Sitter** (`ρ̃ = 0`), onde
`r³V_f = μ r V_g` e portanto

$$\frac{m_T^2}{H^2}\bigg|_{\rm dS}=\frac{3\,\mathcal B(r_\infty)\,(1+\mu r_\infty^2)}{\mu\,r_\infty\,V_g(r_\infty)}$$

*(resíduo 0; e em `β₀=β₂=β₃=0` colapsa em `1 + 1/(μr_c²)`, resíduo 0 —
reencontrando o corolário F-1 do R-13b por outra via).*

**Essa expressão não é um número universal: depende de `r_∞` e dos
`β_n`.** Logo nem `6` nem `3` podem ser "o valor de de Sitter". A
pendência P-5 não é uma discrepância numérica a arbitrar — é uma
fórmula usada fora do domínio de um lado, e um número importado e não
verificado do outro, sobre uma quantidade que **não é universal**.

> A nota de higiene do `posicionamento_literatura.md` §6 P-5 — de que o
> `3` de `3(4+3w)|_{w=−1}` **não tem relação** com o `3` do funcional de
> Higuchi — está **CORRETA e é mantida**. São dois objetos diferentes
> que coincidem num número, e agora sabemos por quê: um é uma
> extrapolação ilegítima, o outro é um limite exato.

---

## 4. ALVO C — o elo não medido internamente: FECHADO

**Veredito: FECHADO. `c_s² > 0` em 50/50 pontos medidos.**
*Script: `r13aud_c_cs2_ibb.py`. Maquinaria: a mesma do R-12f/g (redução
2-DOF Schur + E2 sobre a `L2` de `derivations/code/01`), mpmath, fundo
em forma fechada, `np.gradient` travado.*

### 4.1 A medida

Células IBB genuínas (`β₀=β₂=β₃=0`, `β₁=1`, `f = y/2μ^{3/2}` ∈
{0.05, 0.20, 0.50, 0.80, 0.98}), 10 épocas de `a = 3×10⁻⁵` a `a = 30`,
`Ω_m(a=1) = 0.3`, poeira.

| | medido |
|---|---|
| `c_s² > 0` | **50/50 pontos** |
| mínimo | **0.442805690** (f = 0.98, a = 1) |
| máximo | 0.999943188 (a = 30) |
| no passado profundo (a = 3e−5) | **0.49999995** |
| canal 2 (literatura, `−r″/(3r′)`, forma fechada) | 0.5 → 1.0 |
| `Δ = ` canal 1 − canal 2 | máx **0.09241**, mín 5.25e−8; **negativo em 50/50** e → 0 nos **dois** extremos |
| **C-M5** — degenerescência em `μ` (gate novo) | **1.693e−16** |
| **C-M2/C-R4** — controle positivo, ramo finito | **−0.99999750** (a=1e−4), −0.99999150 (a=0.01) |
| calibrador do espectador | `\|cal − 1\| ≤ 5.3e−9` *(CEGO ao canal `Ċ` — não é prova)* |

> **(A-1) O ELO FECHA.** O `c_s²` do modo métrico do sistema 2-DOF é
> **positivo em toda a história de todas as células IBB genuínas
> medidas**, indo de **+1/2** no passado profundo a **+1** no atrator
> tardio, e acompanhando o canal fechado da literatura com desvio
> `\|Δ\| ≤ 0.093` que **zera nos dois extremos**. *Nível 2b, com
> controle positivo que reprova o ramo finito (−1).*
>
> **Consequência para o corpus:** a frase de complementaridade deixa de
> ser "metade medida, metade literatura". **Os dois lados passam a ser
> medidos por nós**, com maquinaria própria e `μ` generalizado.

### 4.2 O defeito de instrumento que o caminho revelou — e ele é novo

**Este é o achado de método desta auditoria, e ele é da mesma família do
Erratum-03.**

A regra 6 exige "estêncil de ordem ≥ 8 **com teste de refino**". A
prática do R-12g e do R-13b usa **um `h` fixo (1e−3)**, comparado com
3e−4. **Isso não basta quando o fundo tem `r` grande** — e o ramo
infinito tem `r ~ 10⁸` no passado profundo.

Célula IBB `f = 0.05`, `μ = 1`, `a = 3×10⁻⁵`, `kh = 10⁴`:

| `h` | `c_s²` |
|---|---|
| 1e−3 | **−18760.836** |
| 3e−4 | −25.400 |
| 1e−4 | +0.4960472 |
| 3e−5 | +0.4999997 |
| 1e−5 | **+0.4999999** |

**De −1.9×10⁴ a +0.5.** E o teste que **separa** truncamento de
arredondamento: subir `dps` de 60 para **250 não move o número** (13
dígitos idênticos); baixar `h` move-o em cinco ordens de grandeza.
**É truncamento de estêncil, não precisão de máquina.**

**Raio de alcance, medido com controle positivo:**

| | atinge? |
|---|---|
| **R-13b** | **NÃO.** Nenhum número decisivo dele passa por estêncil: `dr/dN`, `ξ`, `m_T²`, `H²` são forma fechada; a raiz é polinômio + Newton; o `a(ξ=0)` é bissecção sobre forma fechada. O estêncil de 8ª ordem lá é **só cross-check** do gate M4 |
| **R-12g** | **SIM, em princípio** — mas no domínio dele (`r → 0`, `r ≤ 1e−6`) o `h = 1e−3` está convergido: reproduzido aqui, `c_s² = −0.99999975` em `a = 1e−4`, `kh = 1e3..1e4` |
| **qualquer reuso futuro** da maquinaria de perturbação em fundo com `r` grande | **SIM, e com força** |

**Protocolo corrigido, usado na medida do §4.1:** refino em `h`
(1e−3 … 1e−6) até dois `h` sucessivos concordarem a ≤ 1e−7; depois
extrapolação de **Richardson em `1/kh²`** (o resíduo em `kh` é **massa**,
Erratum-03 §3 — não é erro e não deve ser exigido zero), com as duas
extrapolações concordando a ≤ 1e−6. **50/50 pontos passaram.**

*(Rodada ruim preservada no git: a 1ª versão do script mediu com `h`
fixo e reportou `c_s² = −1609` a `−18761`; a 2ª ainda usou um critério
de `kh` mal posto — exigir que três `kh` coincidam, o que rejeita o
termo de massa como se fosse erro — e reprovou 50/50. Ambas estão no
histórico.)*

### 4.3 A relação `Δ = ½rr′` do R-12i NÃO vale aqui — e isso é achado

Critério pré-declarado: se a relação `c²_{s,TDCP} = −r″/(3r′) + ½rr′`
valesse também no ramo infinito, os canais 1 e 3 bateriam a ≤ 1e−3.
**Não batem, e por 12 ordens de grandeza:** `½rr′` chega a ~1e12
enquanto o `Δ` medido é ≤ 0.093.

**Leitura:** a relação foi provada no R-12i **na célula `β₀–β₁`
(`β₄ = 0`) do ramo FINITO**. Aqui `β₄ ≠ 0` **e** o ramo é outro.
**Resultado pré-declarado: a relação é própria daquela célula e daquele
ramo. Achado, não falha.**

### 4.4 O gate novo: degenerescência em `μ`

O corolário **F-3** do R-13b prova que, no IBB genuíno, `μ` é **pura
reescala** do fundo a `f` fixo. Logo qualquer quantidade **adimensional**
do fundo — e `c_s²` é uma — tem de ser **idêntica** entre células de
mesmo `f` e `μ` diferente. **Onde não for, o número é ruído.**

Medido: **1.693e−16** sobre `μ ∈ {0.1, 1, 10}`. **Este gate não existia
no corpus** e é barato; recomendo adotá-lo como padrão em qualquer
medida futura no bloco IBB.

---

## 5. ALVO E — a borda: a margem não existe, existe um teorema

**Veredito: CONFIRMADO, e fortalecido de 2b para 2a.**
*Script: `r13aud_e_borda.py`, mpmath dps = 50.*

### 5.1 O teorema (E1)

Com `β₀ = β₂ = β₃ = 0`, `β₁ = 1`, `y = β₄/β₁`, defina
`Q(r) ≡ μ r 𝒲(r) = y r³ − 3μ r² + 1` (que é `μ r ρ̃`) e
`P(r) ≡ μ r² 𝒲′(r) = 2y r³ − 3μ r² − 1`. Então, **identicamente**
(resíduo simbólico **0**):

$$\boxed{\;P(r)\;=\;2\,Q(r)\;+\;3\,(\mu r^{2}-1)\;}$$

No ramo infinito, `Q > 0` (é `ρ̃`) e `μr² > μr_c² > 1` (porque
`r_c > 2μ/y > μ^{−1/2}` quando `y < 2μ^{3/2}` — sub-lemas E1b, E1c,
resíduos 0). Portanto

$$P(r)>0\ \Rightarrow\ \mathcal W'(r)>0\ \Rightarrow\
\frac{dr}{dN}=-\frac{3(1+w)\tilde\rho}{\mathcal W'(r)}<0
\quad\textbf{ESTRITAMENTE}$$

para **todo** ponto do ramo infinito com `ρ̃ > 0`, em **toda** célula da
janela, em **todo** `μ`, com **qualquer** fluido de `w > −1`.

> **NÃO HÁ MARGEM NUMÉRICA. É um teorema.**

### 5.2 De onde vem o `−6.05e−5`: número de grade

Em `a → ∞`, `ρ̃ → 0` e `𝒲′(r_c) > 0` finito, logo `r′ → 0⁻`. O supremo
de `r′` sobre a história **é zero, atingido só assintoticamente**.
Qualquer "max `r′`" reportado é o valor no **último ponto da grade** e
escala como `a_max^{−3}`. Medido (célula `μ=1`, `f=0.726` — a que dá o
`−1.91e−4` do R-13b):

| `a_max` | `max r′` | razão com a linha acima |
|---|---|---|
| 30 | −1.913264e−4 | — |
| 300 | −1.913447e−7 | 0.0010000955 |
| 3000 | −1.913447e−10 | 0.0010000001 |
| 3e4 | −1.913447e−13 | 0.001 |

**Exatamente `a^{−3}` por década.** O `−6.05e−5` do R-13b é o
`r′(a = 30)` dessa célula reescalado por `μ^{−1/2}` (μ=10). **Ele não é
uma margem estreita: é o valor de uma quantidade que tende a zero por
construção.**

### 5.3 A varredura de borda em precisão estendida (E3)

24 valores de `f` — as duas bordas log-espaçadas, `f` de **1e−9** até
**1 − 1e−12** — × 3 valores de `μ` × 200 épocas de `a = 10⁻⁶` a `10⁶`:

| | medido |
|---|---|
| pontos varridos | **14 400** |
| pontos com `r′ ≥ 0` | **0** |
| `max r′` sobre a varredura inteira | **−1.6686885e−18** |
| `min P(r)` | positivo em toda a varredura |
| `min (μr² − 1)` | positivo em toda a varredura |

*(A grade do R-13b ia de `a = 10⁻⁴` a `30` e `f` de `0.05` a `0.98`;
esta vai 12 ordens em `a` e até `1e−9`/`1e−12` das bordas.)*

### 5.4 "Célula IBB genuína" e a raiz espúria — resposta fechada (E4)

A cúbica de fundo é `(y/μ)r³ − 3r² − ρ̃ r + 1/μ = 0`. Produto das
raízes `= −1/y < 0`; soma `= 3μ/y > 0`. Produto negativo ⟹ número
**ímpar** de raízes negativas (1 ou 3); soma positiva ⟹ 3 é
impossível. **Logo há exatamente UMA raiz negativa**, e as demais são
ou duas positivas ou um par complexo conjugado.

> **Não existe "terceira raiz positiva espúria".** Quando o ramo
> existe, há **exatamente duas** raízes positivas — a menor é o ramo
> finito, a maior é o infinito. O teste é "tome a maior das duas", e
> não há o que confundir. *Verificado numericamente em dps=50 nas duas
> bordas: 3 raízes reais, 2 positivas, 1 negativa, em todos os casos.*

### 5.5 Poder do teste (E5) — a janela faz trabalho

**Fora** da janela (`y > 2μ^{3/2}`) não há ponto fixo tardio, e
`P = 2Q + 3(μr² − 1)` pode ser **negativo** onde `μr² < 1`. Medido:
`r′ > 0` em pontos com `y/y_max = 1.01, 2, 10`. **O teste tem poder, e
a janela `0 < β₄/β₁ < 2μ^{3/2}` está fazendo trabalho real.**

### 5.6 A degenerescência em `f → 1` (E6)

`μr_c² → 1⁺` e `m_T²/H²\|_{r_c} = 1 + 1/(μr_c²) → 2⁻` **sem alcançar**,
verificado até `1 − f = 10⁻¹²` (o R-13b foi até `1 − f = 0.02`):

| `1 − f` | `r_c` | `μ r_c²` | `1 + 1/(μr_c²)` |
|---|---|---|---|
| 1e−4 | 1.00824351481074 | 1.016554985157914 | 1.983714619081483 |
| 1e−8 | 1.000081657436634 | 1.000163321541205 | 1.999836705128365 |
| 1e−12 | 1.000000816497359 | 1.000001632995384 | 1.999998367007283 |

---

## 6. ALVO F — cegueira dos gates

*Script: `r13aud_f_cegueiras.py`.*

### 6.1 A lista fechada, com veredito de mordida

| # | O que o arco R-13 **não** vê | Morde o veredito? |
|---|---|---|
| 1 | `β₂ ≠ 0` ou `β₃ ≠ 0` no ramo infinito (a cúbica vira quártica) | **Não** — limita o alcance, não o enunciado de classe |
| 2 | acoplamento duplo da matéria | **Não** — hipótese declarada também pela fonte |
| 3 | fundo não-FLRW, Vainshtein, ordens superiores | **Não** — e a própria fonte (Woodard 2007) avisa que o ghost pode só aparecer em ordem superior, o que **reforça** a exclusão |
| 4 | a **derivação** do bound (Fasiello–Tolley 1308.1647 não aberto) | **Morde o rótulo, não a medida** — `r′ < 0` e `𝒲′ > 0` são fatos de fundo, independentes de como o bound foi derivado |
| 5 | fantasma escalar (autovalores de `K₂`) no ramo infinito | **Não muda o veredito** (um ghost já basta), mas é um canal a mais, **aberto** |
| 6 | `δρ_m` (perturbação de matéria ausente da `L2`) | **Morde o `c_s²` do alvo C**, não o Higuchi. Mesma fronteira do R-11/R-12g |
| 7 | validade EFT, screening, `f·σ₈` | **Não** — fora de escopo declarado |
| 8 | **`β_n(φ₋)` — a modulação da v2** | **MORDE O ARGUMENTO, NÃO O VEREDITO** — ver §6.2 |
| 9 | **a própria eq. (14) sob modulação** | **NÃO SABIDO POR NINGUÉM** — ver §6.3 |

### 6.2 A que morde (#8): sob modulação, `r′` é o diagnóstico errado

O limiar, em forma fechada, para a subclasse F1 (só `β₁` modulado):

$$\frac{d\beta_1}{dN}\;\ge\;\frac{3\mu\,r\,\tilde\rho\,(1+w)}{3\mu r^{2}-1}
\qquad\Longrightarrow\qquad r'\ge 0$$

Medido (`β₁ = 1`, logo isto é `d\ln β₁/dN`): **~7.4e4** em `a = 10⁻³` e
**~7e−5** em `a = 30`. **Perto do atrator tardio o limiar tende a zero
— qualquer modulação positiva inverte o sinal de `r′`.**

**Mas inverter `r′` NÃO restaura Higuchi.** A cadeia é
`(14) ⟺ (15) ⟺ 𝒲′ ≤ 0 ⟺ r′ ≥ 0`, e **só o último elo usa `dr/dN`**.
O elo `(15) ⟺ 𝒲′ ≤ 0` é algébrico em `(r, β_n, μ)` e **não vê a
modulação**. Medido, em `μ=1, y=1, a=30`:

| `dβ₁/dN` | `r′` | LHS(15) | Higuchi |
|---|---|---|---|
| 0 (0.0× limiar) | −2.2903e−4 | **−21.8751** | VIOLADO |
| 7.288e−5 (1.0×) | −0 | **−21.8751** | VIOLADO |
| 1.4576e−4 (2.0×) | +2.2903e−4 | **−21.8751** | VIOLADO |
| 7.288e−4 (10×) | +2.0613e−3 | **−21.8751** | VIOLADO |

> **`r′` troca de sinal; LHS(15) nem se move.** O veredito de exclusão
> **sobrevive** — mas o argumento com que o corpus o defende, **não**.
>
> **RECOMENDAÇÃO NORMATIVA:** onde o corpus escreve *"o IBB é excluído
> porque `r′ < 0`"*, a formulação robusta é *"o IBB é excluído porque
> `𝒲′(r) > 0`, isto é, `ρ̃ > 0` e `μr² > 1` — e isso é teorema (§5.1),
> não medida"*. As duas coincidem com `β_n` constantes; sob modulação só
> a segunda vale.

### 6.3 A que ninguém sabe (#9): a eq. (14) sob modulação

Tudo no §6.2 supõe que **a própria eq. (14) continue sendo a condição de
Higuchi ponto a ponto** com `β_n(N)`. Essa hipótese é **declarada** pelo
R-13a (§2.2, hipótese 2) e **não foi verificada por ninguém — nem aqui**.
Se (14) ganhar termos em `β̇_n` na derivação hamiltoniana, nada deste
arco cobre o caso.

> **É a fronteira epistêmica real que o arco R-13 deixa aberta sobre a
> v2.** Ela substitui a P-6 (que fecha, §1.1) como o item mais caro da
> fila.

### 6.4 A que não morde, e o R-13b a listava como fronteira (#F2)

**Radiação.** O teorema E1 usa apenas `ρ̃ > 0`, `μr² > 1` e `1+w_tot > 0`
— **nenhum deles usa a forma de `ρ̃(N)`**. Verificado numericamente com
`ρ = ρ_m a⁻³ + ρ_r a⁻⁴` atravessando a equipartição (`a_eq = 1/3400`),
de `a = 10⁻⁶` a `30`: **`r′ < 0` em 8/8 pontos**, com `w_tot` de 0.332 a
0.000.

**O R-13b listava "sem radiação" como fronteira de varredura. Para o
SINAL de `r′` ela era desnecessária.** *(Continua necessária para os
VALORES: a história `r(a)` muda.)*

### 6.5 Duas armadilhas vivas, registradas

- **Seleção de raiz (F5).** A semente analítica `r ~ √(μρ̃/β₄)` só é
  válida no passado profundo; perto do ponto fixo o Newton converge
  para a raiz do ramo **finito**. Medido: em `a = 10`, a semente
  converge para `0.65136` quando `r_c = 2.8795`. **O R-13b está
  protegido** (continuação a partir do passado + gate M1(d)), mas a
  armadilha derrubou a 1ª versão do script do alvo C desta auditoria.
- **Estêncil com `h` fixo (§4.2).** Já tratada.

---

## 7. Banners de supersessão emitidos

Aplicados nesta sessão, todos como **anotação, não reescrita silenciosa**:

| Documento | O que o banner faz |
|---|---|
| `docs/resultado_r13b_ibb_ramo_infinito.md` | (i) o `max r′ = −6.05e−5` é número de grade e o enunciado correto é o teorema E1; (ii) o mapa do R-13a §2.1 deixa de ser "entrada não reverificada"; (iii) a cadeia vale para todo `w > −1`; (iv) o elo do gradiente foi fechado |
| `docs/resultado_r13a_criterio_higuchi_fonte.md` | o item 1 da fila (verificação simbólica do §2) e a alegação de sobredeterminação ficam **CONFIRMADOS por rota independente** |
| `docs/posicionamento_literatura.md` | P-6 **FECHADA**; P-5 **RESOLVIDA**; a linha da complementaridade em §1.1b passa a ter os dois lados medidos |
| `docs/resultado_r12_instrumento_e_cs2.md` | **regra 6b**: o teste de refino tem de ser adaptativo em `h`; um `h` fixo pré-escolhido não é auditável |
| `manuscript-v2/02_metodo.md` | idem, na regra 6 |

---

## 8. O que esta auditoria NÃO fez (regra 7, aplicada a ela mesma)

- **Não abriu Fasiello–Tolley 1308.1647**, a fonte primária real do
  bound. O caveat do fator `1/2` no potencial (nota 3 de 1503.07436)
  continua declarado e **não verificado**.
- **Não validou a caixa de `m_T²`** da `derivations/02`. Ela é entrada.
  O rastreamento de dependência do §6.1/F3 mostra que a **exclusão** não
  depende dela; os números tensoriais (E3, E4, o `3` e o `12`) dependem.
- **Não mediu fantasma escalar** (autovalores de `K₂`) no ramo infinito.
- **Não testou a eq. (14) sob modulação** (§6.3).
- **Não varreu `β₂ ≠ 0` nem `β₃ ≠ 0`** sobre o ramo infinito.
- **Não decidiu se a v2 produz `dβ₁/dN` acima do limiar do §6.2** — o
  script mede o limiar, não a dinâmica de `φ₋`.
- **A extração das fontes foi por UMA rota** (ar5iv); o R-13a usou duas.
- O `c_s²` do §4 herda a fronteira do R-11/R-12g: **a `L2` deste projeto
  não tem `δρ_m`**.

---

## 9. Fila que esta auditoria abre

1. **A eq. (14) sob `β_n(N)`** (§6.3) — passa a ser o item mais caro da
   fila, e substitui a P-6.
2. **Trocar o diagnóstico operacional** de `r′ < 0` para `𝒲′(r) > 0` nos
   docs de veredito (§6.2). Barato, e imuniza o enunciado contra a v2.
3. **Adotar o gate de degenerescência em `μ`** (§4.4) como padrão no
   bloco IBB. Barato, e é detector de ruído.
4. **Regra 6b** (§4.2): refino adaptativo em `h`, com o `h` necessário
   determinado pelo fundo, não pré-escolhido.
5. **Fantasma escalar no ramo infinito** — o único canal do arco que
   ninguém mediu.
6. Abrir **1308.1647** (herdado do R-13a §6, item 4).
