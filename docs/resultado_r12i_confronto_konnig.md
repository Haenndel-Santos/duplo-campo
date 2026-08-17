# R-12i — CONFRONTO com Könnig et al. (1407.4331): o "0.28" existe, é real, e é de **outro modelo**

**Data:** 2026-08-13. Fonte primária: Könnig, Akrami, Amendola, Motta &
Solomon, *Stable and unstable cosmological models in bimetric massive
gravity*, **PRD 90, 124014 (2014)** = [arXiv:1407.4331]. Fecha o item
nº 2 da fila aberta em `docs/resultado_r12b_teorema_cs2.md` §6, marcado
desde então como *[verificar contra a fonte]*. **Sem script novo no
repositório** (esta sessão só criou este documento): toda a álgebra do
confronto é fechada e está transcrita aqui — sympy sobre `c_s²(r)` do
R-12b, sobre `dr/dN = −3ρ̃/ρ̃′` do mesmo script, e sobre as equações
publicadas de §V; cada identidade citada como "resíduo 0" é
`sp.simplify(lhs − rhs) == 0`.

**Veredito em uma linha: caso (b).** Os números não eram comparáveis —
0.28 é o limiar do modelo **β₁-puro (β₀ = 0)**, e a nossa célula é o
modelo **β₀β₁ com β₀/β₁ = 1**. Sob a tradução correta, o número deles
para o *nosso* modelo é **0.2145** contra o nosso **0.2079** (3.1%), e
a diferença residual tem forma fechada exata.

---

## 0. Nível de acesso à fonte

Disciplina de `docs/posicionamento_literatura.md`: **VERIFICADO-NA-FONTE**
vs **NÍVEL-DE-BUSCA**.

| Item | Nível |
|---|---|
| Abstract, autores, referência de periódico | **VERIFICADO** (arxiv.org/abs/1407.4331) |
| Texto integral da versão publicada na PRD | **VERIFICADO** — PDF de `arxiv.org/pdf/1407.4331` (17 pp.), texto extraído por decodificador `zlib`+operadores `TJ/Tj` próprio |
| Eqs. (16), (17), (21)–(24), (28) — fundo | **VERIFICADO** |
| Eqs. (68)–(76) — §V Instabilidades | **VERIFICADO**, com conferência cruzada independente contra o HTML do ar5iv |
| §VI (IBB), §VIII (conclusões) | **VERIFICADO** |
| Diagnóstico da origem do resíduo de 3.1% | **INFERÊNCIA ESTRUTURAL** — não re-derivado (§6) |

**Caveat de extração (declarado):** o decodificador perde ligaduras
(fi/fl) e mapeia glifos de fonte matemática (o ponto decimal sai como
`:`, sub/sobrescritos colam). Todas as equações citadas abaixo foram
**conferidas duas vezes**, por duas rotas independentes (PDF publicado
e HTML ar5iv), e — o teste mais forte — **fecham entre si por
identidade algébrica** (§2.3). Nenhuma afirmação abaixo depende de
paráfrase de terceiros. **A numeração de equações usada aqui é a da
versão publicada na PRD**; o ar5iv (versão arXiv) tem as mesmas
equações deslocadas de **+3** (a nossa (69) é a (72) de lá).

---

## 1. O que a fonte de fato afirma

### 1.1 O critério (pergunta 1)

Não é "ω real" como categoria solta: é a **relação de dispersão do
sistema 2-DOF reduzido**, e é comensurável com a nossa ponto a ponto.

Eles reduzem as dez equações linearizadas a duas equações de segunda
ordem (§V, eq. 68)

$$X_i'' + F_{ij}X_j' + S_{ij}X_j = 0,\qquad X_i \equiv \{\hat H,\ \Psi\},$$

com `N = log a` como variável temporal (`'` = d/dN) e substituem
`X = X₀ e^{iωN}`, desprezando a dependência temporal de ω (WKB;
critério declarado na nota de rodapé 7: |ω′/ω²| ≪ 1). ω imaginário ⟹
soluções crescentes/decrescentes em vez de oscilantes; eles próprios
nomeiam o caso como **velocidade do som imaginária**. É **exatamente
instabilidade de gradiente do escalar métrico** — a mesma doença, o
mesmo modo, o mesmo observável.

**Convenções de tempo/escala (críticas para traduzir):** métrica g em
tempo conforme (eq. 13), `ℋ ≡ ȧ/a` é o Hubble **conforme**, `k` é
comóvel. Logo `X ∝ e^{iωN}` com `dN = ℋ dη` dá frequência conforme
`ω_η = ωℋ = k·c`, isto é `ω_t² = c²(k/a)²`. **A função `c²` deles é o
nosso `c_s²` sem nenhum fator de conversão.**

### 1.2 A convenção de r (pergunta 2) — **idêntica à nossa**

Eq. (17): `r ≡ b/a`. Mesma razão, mesmo sentido, mesmo domínio.
E a normalização dos β também bate: a densidade efetiva do termo de
massa (eq. 16) é

$$\rho_{mg} = B_0 \equiv \beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3,$$

que é **letra por letra** o `rho_int = M_ef²(β₀ + 3β₁r + 3β₂r²)` do
`r12b_prova_simbolica_cs2.py`. Eles fixam `M_f = 1` por reescala
(§II); nós fixamos `μ = M_f² = 1`, com `M_ef² = μ/(1+μ) = 1/2` — que é
justamente `M_g²M_f²/(M_g²+M_f²)`. **Mesma normalização.**

Verificação independente da tradução: o nosso `dr/dN = −3ρ̃/ρ̃′` é,
substituído, `r′ = 3rΩ_tot/(1+3r²)` com `Ω_tot = 1 − (β₀/β₁)r − 3r²` —
que é exatamente a eq. (21) com a eq. (22) deles para w_tot = 0. **Os
fundos são o mesmo fundo.** (Eles restringem-se a poeira, w_tot = 0,
§II — igual à nossa fronteira "sem radiação".)

### 1.3 O modelo que produz o 0.28 (pergunta 3) — **não é o nosso**

O 0.28 aparece logo depois da eq. (69), que é enunciada sob a hipótese
explícita de que **apenas β₁ é não-nulo**:

$$\omega_{\beta_1} = \pm\frac{k}{\mathcal H}\sqrt{\frac{-1+12r^2+9r^4}{1+3r^2}}
\qquad (69)$$

A nossa célula mínima **não é essa**. O `r12b_prova_simbolica_cs2.py`
fixa `B0V, B2V, B4V, MUV = 1, 0, 0, 1` — isto é **β₀ = 1**, e o próprio
comentário do script a chama de "o modelo mínimo **β₀–β₁**". Na
taxonomia deles isso é o **modelo β₀β₁**, que tem equação própria:

$$\omega_{\beta_0\beta_1} = \pm\frac{k\sqrt{9r^4+2(\beta_0/\beta_1)r+12r^2-1}}{\mathcal H\,(3r^2+1)}
\qquad (73)$$

### 1.4 O número 0.28 (pergunta 4) — **existe, §V, e é exato**

Existe. Está em §V, no parágrafo imediatamente após a eq. (69): as
soluções reais só aparecem para r > 0.28, o que ocorre em N = −0.4,
i.e. z ≈ 0.5; antes disso o sistema é instável para k grande, e isso
invalida a teoria de perturbações linear em escalas sub-horizonte.

E o 0.28 **não é numérico**: é a raiz do numerador de (69),

$$9r^4+12r^2-1=0 \;\Longrightarrow\;
r_K^{(\beta_1)} = \sqrt{\tfrac{\sqrt5-2}{3}} = 0.28051617748939762732\ldots$$

verificado simbolicamente (resíduo 0 exato).

### 1.5 Forma fechada para c_s² (pergunta 5) — **sim, e mais do que esperávamos**

Duas, e a segunda é uma identidade que o repositório não conhecia.

De (73), com `λ ≡ β₀/β₁`:

$$\boxed{\;c_{s,K}^2(r) = \frac{9r^4+12r^2+2\lambda r-1}{(3r^2+1)^2}\;}$$

E, eq. (76) — o achado estrutural do paper, que eles declaram válida
para **todos** os submodelos de β₀β₁β₄ (inclusive as eqs. 69–72):

$$\omega_{\beta_0\beta_1\beta_4} = \pm\frac{ik}{\mathcal H}\sqrt{\frac{r''}{3r'}}
\qquad\Longleftrightarrow\qquad
\boxed{\;c_s^2 = -\frac{r''}{3r'} = -\frac13\frac{d r'}{d r}\;}$$

**a velocidade do som é menos um terço da derivada do fluxo de fundo.**
Daí a condição de estabilidade deles, `r''/r' = dr'/dr < 0`.

*Verificação nossa (simbólica, resíduo 0):* `−(1/3)d/dr[3r(1−λr−3r²)/(1+3r²)]`
reproduz **exatamente** a eq. (73), inclusive o denominador ao
quadrado; e em λ = 0 reproduz `(9r⁴+12r²−1)/(3r²+1)²`.

> **Erratum na fonte (VERIFICADO, e sem consequência).** A eq. (69)
> impressa tem `(1+3r²)` **sem quadrado** dentro da raiz, o que é
> incompatível com a identidade (76) que os próprios autores declaram
> cobri-la. As duas rotas de leitura (PDF publicado e ar5iv)
> concordam no que está impresso, então é typo da fonte, não da nossa
> extração. O fator é positivo-definido: **não move a raiz**, e 0.28
> permanece válido. Registrado porque, se o cap. 07 citar a (69)
> literalmente, herda o typo.

### 1.6 O ramo infinito / IBB (pergunta 6) — **e a nossa exclusão está em tensão com a fonte**

O resultado positivo do paper é a **infinite-branch bigravity (IBB)**:
apenas β₁ e β₄ ligados, ramo infinito, `0 < β₄ < 2β₁`; r decresce de ∞
a um valor finito; estável em **todos** os tempos, com fundo viável e
sem constante cosmológica explícita para g. Eles provam (§V, via eq.
77 e regra de sinais de Descartes) que r_c > 1 sempre nessa faixa, o
que garante a estabilidade.

**O ponto que nos atinge diretamente.** Nesse modelo `b` **quica**:
`X ≡ ḃ/ℋ` muda de sinal, e no ponto do quique `f₀₀ = −ḃ²/ℋ² = 0` — o
lapso do setor f se anula. Eles tratam isso **explicitamente** (§II e
§VI, com nota de rodapé 9) e argumentam que **não** torna a solução
não-física, por três razões declaradas: f não acopla à matéria e não
tem interpretação geométrica; nenhuma variável de fundo ou perturbada
apresenta singularidade; e `√(−det f)·R̄(f)` permanece finita e não-nula,
de modo que as equações de movimento existem em todo instante. A
escolha de sinal da raiz quadrada é feita justamente para deixar a
ação diferenciável na travessia.

**Isso é exatamente a configuração que o R-10c Parte A descarta.** O
nosso ξ é `ξ = r + dr/dN`, e como `b = ra` vale `db/dN = aξ`, logo
`ξ = X/a`: **mesmo sinal, mesmo zero**. O critério "ξ cruza zero ⟹
lapso do setor f se anula ⟹ ponto singular ⟹ história contínua
excluída" é, ponto por ponto, o quique que a fonte primária defende
como físico. *A exclusão do ramo infinito no repositório está, hoje,
sem apoio na literatura e em conflito declarado com ela.*

### 1.7 O que mais a fonte já provou (e que nos atinge no §6)

- **§V, no-go de classe para o ramo finito:** *todas* as soluções de
  ramo finito, para *qualquer* combinação de parâmetros, são ou
  inviáveis no fundo ou linearmente instáveis no passado. Publicado em
  2014.
- Regra de redução: no passado, todo modelo multiparamétrico viável de
  ramo finito **reduz ao modelo de interação de ordem mais baixa**
  (β₁β₂, β₁β₃, β₁β₂β₃ → β₁). Os únicos monoparamétricos sem
  instabilidade primordial são β₂ e β₄ (eqs. 70 e 72: `ω_β2 = ±k/(ℋr)`,
  `ω_β4 = ±k/(√2 ℋ)`, ambas reais) — e ambos são **inviáveis no fundo**
  (sem era de matéria no passado assintótico).
- **§VIII, leitura própria deles do mesmo fato:** a instabilidade
  **não** exclui automaticamente os modelos; ela impede o uso da teoria
  linear em escalas sub-horizonte profundas, e pode ser curada por
  efeitos não-lineares (Vainshtein).
- Rota de escape que eles nomeiam: acoplamento duplo da matéria, que
  permite r ≠ 0 no passado remoto.

---

## 2. O confronto lado a lado

### 2.1 A tradução

| | Könnig et al. | TDCP (R-12b) | Batem? |
|---|---|---|---|
| razão das escalas | `r ≡ b/a` (eq. 17) | `r = b/a` | **sim** |
| normalização β | `β₀+3β₁r+3β₂r²+β₃r³` (eq. 16) | idem (`rho_int`) | **sim** |
| massa de Planck de f | `M_f = 1` | `μ = M_f² = 1`, `M_ef² = 1/2` | **sim** |
| matéria de fundo | poeira, `w = 0` | poeira, sem radiação | **sim** |
| fluxo de fundo | eq. (21)+(22) | `−3ρ̃/ρ̃′` = `3rΩ_tot/(1+3r²)` | **sim** (identidade) |
| ramo | finito (para o 0.28) | finito | **sim** |
| β₃ | 0 no modelo em questão | 0 (classe F1) | **sim** |
| definição de c_s² | `ω_t² = c²(k/a)²` | `lim_{k→∞} ω²a²/k²` | **sim** |
| **β₀** | **0** (modelo β₁-puro) | **β₀ = 1, β₁ = 1** | **NÃO** |
| perturbação da matéria | **incluída** (δρ, θ nas eqs. 39–40) | **ausente** (`rho_s = 0`; matéria só no fundo) | **NÃO** |

**Como sabemos que a nossa célula é λ = β₀/β₁ = 1** (e não outro
valor): o atrator tardio do repositório, `r_∞ = (√13−1)/6`, é raiz de
`3r²+r−1 = 0`; a condição `ρ̃ = 0` no nosso fundo é `1 − λr − 3r² = 0`.
Resolvendo para λ em `r = r_∞` dá **λ = 1 exatamente** (sympy). Ou
seja: `r_∞ = (√13−1)/6` é a assinatura de β₀/β₁ = 1, e não existe
nenhuma outra leitura.

### 2.2 Os três números

| Quantidade | Modelo | Valor | Forma fechada |
|---|---|---|---|
| **0.28 da fonte** | β₁-puro, β₀ = 0 | **0.2805161775** | `√((√5−2)/3)` |
| **Könnig no NOSSO modelo** | β₀β₁, λ = 1, eq. (73) | **0.2144766108** | raiz de `9r⁴+12r²+2r−1` |
| **Nosso R-12b** | β₀β₁, λ = 1 | **0.2079261621** | raiz de `9r⁵−6r³+3r²−10r+2` |

- 0.2079 vs **0.28** (comparação errada, a que estava no corpus): **+34.9%**
- 0.2079 vs **0.2145** (comparação certa, mesmo modelo): **+3.1%**

### 2.3 As duas funções, e a diferença em forma fechada

$$c_{s,\rm TDCP}^2(r) = -\frac{(3r+1)(9r^5-6r^3+3r^2-10r+2)}{2(3r^2+1)^2},
\qquad
c_{s,K}^2(r) = \frac{9r^4+12r^2+2r-1}{(3r^2+1)^2}$$

Concordâncias **exatas** (simbólicas, não numéricas):

| Ponto | TDCP | Könnig (λ=1) |
|---|---|---|
| `r → 0` | **−1** | **−1** |
| termo linear da série | `−1 + 2r + …` | `−1 + 2r + …` |
| `r = r_∞ = (√13−1)/6` | **+1** | **+1** |

O termo em `r²` difere (19.5 vs 18), e a diferença tem forma fechada:

$$\boxed{\;\Delta(r) \equiv c_{s,\rm TDCP}^2 - c_{s,K}^2
= \tfrac12\,r\,r' = \frac{3}{2}\,\frac{r^2\,\Omega_{\rm tot}(r)}{1+3r^2}\;}$$

verificada como identidade racional (resíduo 0). Equivalentemente:

$$c_{s,\rm TDCP}^2 = -\frac{r''}{3r'} + \frac{1}{2}rr'.$$

**Δ é proporcional à densidade de matéria.** Ela zera exatamente nos
dois extremos — em `r → 0` porque `Δ ≈ (3/2)r²`, e em `r_∞` porque
`r′ = 0` (Ω_tot = 0, de Sitter). Por isso os dois teoremas de ponta do
R-12b (`−1` e `+1`) sobrevivem intactos, e só o miolo — inclusive o
cruzamento por zero — se desloca.

| r | c_s² TDCP | c_s² Könnig (λ=1) | c_s² Könnig (β₁-puro) |
|---|---|---|---|
| 1e−6 | −0.999998 | −0.999998 | −1.000000 |
| 0.01 | −0.978064 | −0.978213 | −0.998201 |
| 0.05 | −0.853532 | −0.857040 | −0.955557 |
| 0.1 | −0.627447 | −0.640117 | −0.828636 |
| **0.20793** | **0.000000** | −0.038001 | −0.363851 |
| **0.21448** | +0.039401 | **0.000000** | −0.331109 |
| **0.28052** | +0.413383 | +0.367220 | **0.000000** |
| 0.434258 | **+1.000000** | **+1.000000** | +0.645727 |

---

## 3. O VEREDITO: **(b)**

**Critérios e convenções são os mesmos; a família não é.** Não há
discrepância de 26% (nem de 35%): há um **erro de identificação de
modelo**. O 0.28 é o limiar do modelo β₁-puro (β₀ = 0), a que o
repositório nunca correspondeu; a nossa célula mínima é o modelo β₀β₁
com β₀/β₁ = 1, cujo limiar publicado é 0.2145.

A tradução correta, portanto, é:

> `r_cross(λ) = ` a raiz positiva de `9r⁴ + 12r² + 2λr − 1`, com
> `λ = β₀/β₁`. Em λ = 0 dá `√((√5−2)/3) = 0.28052` (o número da fonte);
> em λ = 1 dá `0.21448` (o número da fonte **para o nosso modelo**);
> o nosso R-12b dá `0.20793`.

Sob a tradução, os dois cálculos **concordam exatamente** em `c_s²(0) = −1`,
no coeficiente de `r`, e em `c_s²(r_∞) = +1`, e diferem por `½rr'`.

---

## 4. Origem do resíduo de 3.1% — **inferência estrutural, não verificada**

*Nível: hipótese estrutural forte, com assinatura quantitativa
fechada. NÃO re-derivada.*

Δ = ½rr′ ∝ Ω_matéria aponta para uma diferença **declarada** de escopo,
não para um erro: a fronteira "matéria só como ρ de fundo" do R-12b.
No `r12b_prova_simbolica_cs2.py` o dicionário de substituição fixa
`rho_s: 0` e `Up: 0` — a L2 não contém **nenhuma** perturbação de
matéria, enquanto o fundo carrega poeira (`ρ̃ ≠ 0`, e de fato
`ρ̃ = (β₁/r)Ω_tot` é *literalmente* a densidade de matéria). Könnig
carregam δρ e θ nas eqs. (39)–(40) e os eliminam algebricamente pelos
vínculos, de modo que o modo de poeira **está** dentro do sistema 2×2
deles e **não está** no nosso.

Contagem consistente com isso: os 2 DOF deles são {helicity-0, poeira};
os nossos 2 DOF são {`E_f` (helicity-0), `δχ` espectador desacoplado}.
**O modo métrico é o mesmo; o parceiro não é.**

**Teste que decide (proposto, não executado):** introduzir δρ_m na L2 e
refazer o R-12b. Predição falsificável e nítida: **Δ deve zerar
identicamente**, isto é, o novo `c_s²` deve valer exatamente
`−r''/(3r')`. Não é um flip de parâmetro — `rho_s` na
`tdcp_pert_lib.py` é densidade de **fundo**, e não há campo δρ_m em
`NOMES`; exige acrescentar o grau de liberdade à maquinaria.

---

## 5. Consequência para o cap. 07 §4 — **recomendação, não editado**

*(Instrução respeitada: nenhum arquivo do manuscrito foi tocado.)*

**O "r ≳ 0.28" do cap. 07 §4 não tem fonte legítima e precisa ser
trocado.** É o limiar de Könnig para β₀ = 0, aplicado ao nosso
benchmark, que tem β₀/β₁ = 1. O erro não é cosmético:

- no **nosso** fundo, `r = 0.28` está `ΔN = +0.205` adiante do
  cruzamento verdadeiro — `a_cross` iria de 0.578 para 0.709 (+23%);
- em `r = 0.28` o nosso `c_s²` já vale **+0.41**, não ≈ 0: usar 0.28
  como fronteira **entrega 0.2 e-fold de era instável para o lado
  saudável**;
- e é internamente inconsistente com o próprio `a_cross ≈ 0.578` do
  R-12f, que o mesmo capítulo cita quatro linhas abaixo.

**Troca recomendada** (`r ≳ 0.28` → o número do repositório, com a
fonte certa ao lado):

> "na era tardia (r ≳ 0.21, `a_cross ≈ 0.578` — R-12f)" — e, se quiser
> a comparação com a literatura no mesmo fôlego: "…em acordo de 3% com
> a eq. (73) de [1407.4331] avaliada em β₀/β₁ = 1, que dá 0.2145; o
> 0.28 citado com frequência é o valor **do modelo β₁-puro** (eq. 69),
> outro ponto do espaço de parâmetros."

**Manter, e fortalecer, o resto do parágrafo.** A frase "confirmando a
previsão de Könnig–Akrami–Amendola–Motta–Solomon para o *finite
branch*" está **certa** — e é mais forte do que o capítulo supõe: não é
uma "previsão registrada sem confrontar", é uma **forma fechada
publicada que a nossa reproduz exatamente nos dois extremos**. Vale
citar §V e as eqs. (69), (73) e (76) nominalmente.

**Correção adicional recomendada** (fora do cap. 07, para a fila): o
`docs/posicionamento_literatura.md` linha 24 diz "ω real só p/ r > 0.28"
sem qualificar o modelo. Deve passar a dizer "…no modelo β₁-puro
(β₀ = 0); no modelo β₀β₁ com β₀/β₁ = 1 o mesmo critério dá 0.2145".

---

## 6. Consequência para o enunciado de novidade — **confirma, e é mais amplo do que pensávamos**

O nosso no-go de classe **CONFIRMA** a literatura. Não a contradiz em
nenhum ponto. O problema não é conflito: é **precedência**.

**O que já estava publicado (e o corpus subestimava):**

1. **O no-go de classe do ramo finito é de 2014.** §V de 1407.4331
   enuncia que todas as soluções de ramo finito, para qualquer
   combinação de parâmetros, são inviáveis no fundo ou instáveis no
   passado. Isto **subsome** o nosso "NO-GO DE CLASSE POR GRADIENTE"
   do cap. 07 §4.
2. **`c_s² = −1` em r → 0 é corolário de uma linha da eq. (69)/(73):**
   numerador → −1, denominador → 1. Eles **não escrevem o valor** (só
   falam em "velocidade do som imaginária"), mas ele está lá para quem
   avaliar o limite. Não é descoberta; é **leitura explícita**.
3. **O nosso 108/108 do R-12g é a confirmação numérica de uma regra
   publicada:** a regra de redução ("todo modelo viável de ramo finito
   reduz, no passado, à interação de ordem mais baixa") prevê
   exatamente que qualquer célula com β₁ ≠ 0 caia no comportamento do
   β₁ — que é o que o escaneio mediu. Como o R-12b **elimina** β₁ pela
   Friedmann (logo β₁ ≠ 0 sempre), as 108 células estão todas dentro
   do escopo da regra. **Âncora de validação do método, não resultado
   novo** — a mesma função que o ramo algébrico já cumpre na tabela do
   `posicionamento_literatura.md`.
4. **A identidade `c_s² = −r''/(3r')` (eq. 76) é deles.** O R-12b a
   redescobriu por acidente e em forma deslocada. Citar.

**O que sobra como contribuição própria defensável:**

| Item | Estado após o confronto |
|---|---|
| **`m_ef²/H² → 5/2`** (o termo de massa sub-dominante) | **A candidata mais forte.** Eles descartam explicitamente as soluções independentes de k como subdominantes e **nunca dão o termo de massa**. Mas **está em risco**: é ordem `k⁰`, e é exatamente aí que a perturbação de matéria ausente entra (via Poisson). **Não reivindicar antes do teste do §4.** |
| **A forma fechada completa em `r`** (grau 6, não 4) | Nova como objeto, mas é a *nossa* truncagem — a versão com δρ_m é que seria a forma fechada do modelo físico. Rebaixar a "forma fechada da célula sem perturbação de matéria". |
| **Reprodução independente** dos dois extremos exatos por maquinaria totalmente distinta (Schur/Faddeev–Jackiw vs redução 10→2) | **Sólida como validação de método.** Vale um parágrafo: dois caminhos independentes, mesmos `−1` e `+1` exatos, mesma primeira ordem. |
| **`m_T²/H² → 12`** (tensorial) | Intocado por este confronto — 1407.4331 é setor escalar. Continua nº 1 do ranking de novidade. |
| **O no-go de classe como enunciado** | **Rebaixar.** Passa de "resultado" a "reprodução independente de um no-go publicado, com o valor `−1` explicitado e a forma fechada exibida". |

**Dois riscos de referee que este confronto cria, e que o paper tem de
absorver antes de ser submetido:**

- **R-a — a palavra "no-go".** A própria fonte lê o mesmo fato de
  forma mais fraca (§VIII): a instabilidade **não** exclui os modelos,
  apenas invalida a teoria linear sub-horizonte, e pode ser curada
  não-linearmente. O nosso enunciado é mais forte que o da literatura
  **sobre o mesmo cálculo**. Ou se justifica a força extra, ou se
  adota a leitura deles. (Conecta com D4 e com Aoki–Maeda–Namba
  1506.04543 — a rota Vainshtein.)
- **R-b — a exclusão do ramo infinito.** §1.6: o critério `ξ → 0` do
  R-10c é o quique de `b` que a fonte primária **trata e defende
  explicitamente** como físico (f não acopla à matéria; nenhuma
  variável singular; `√(−det f)R̄(f)` finita e não-nula). Como o IBB é
  o **único** modelo estável em todos os tempos do paper, esta é a
  porta mais cara que o repositório fechou. *Ela precisa ser reaberta
  e re-examinada, ou a exclusão precisa de um argumento novo que
  responda aos três deles.* Caveat de escopo: o IBB viável deles exige
  β₄ ≠ 0 (`0 < β₄ < 2β₁`), enquanto a nossa célula mínima tem β₄ = 0 —
  então o alvo do reexame é o ramo infinito da F1 **com β₄ ligado**, e
  não a célula atual.

> **[NOTA DATADA — 2026-08-13, desfecho PARCIAL do R-b]**
> O §1.6 acima **não muda**: continua correto e é o registro do
> confronto com 1407.4331. Esta nota só acrescenta o que aconteceu
> *depois* dele.
>
> **(1) A verificação foi feita.** O autor abriu **arXiv:1503.07436**
> na fonte. Atribuição: **VERIFICADO-NA-FONTE — leitura do autor**,
> literatura = **nível 3**; **não** é derivação nem medida deste
> repositório, e **não** é nível 1/2a/2b. O registro completo, com os
> cinco fatos, está em `docs/posicionamento_literatura.md` §2b, R-b,
> bloco "Desfecho parcial".
>
> **(2) Existe um argumento independente contra o IBB.** Em cosmologia
> **expansiva**, 1503.07436 exige `r` **crescente** para satisfazer a
> condição associada ao Higuchi e manter sãos helicidade-0 e
> helicidade-2; e define o *infinite branch* como aquele em que `r`
> parte de infinito e **decresce**. Colisão direta: `r′ > 0` exigido
> vs. `r′ < 0` do ramo. O paper registra ainda que o IBB fora
> identificado antes como livre das instabilidades escalares
> lineares, mas ressalva **violação do Higuchi no limite inicial** em
> trabalhos anteriores e um **ghost em helicidade-2 em tempos
> iniciais**.
>
> **(3) A correção que isto obriga.** O item (a) do R-b acima dizia
> que as duas linhas do `posicionamento_literatura.md` sobre
> 1503.07436 eram **contraditórias**. **Estava errado.** São o mesmo
> critério em ramos diferentes (finito: r′ ≥ 0, passa; infinito:
> r′ < 0, não passa) — **consistentes**. A tensão real é **entre as
> duas fontes**, e dissolve-se pela **separação de canais**:
> estabilidade de **gradiente** ≠ saúde de **Higuchi/helicidade-0** ≠
> saúde do **setor tensorial**. O "IBB estável" de 1407.4331 é o canal
> de gradiente. O IBB pode curar o gradiente que matou o ramo finito e
> ainda assim falhar por outro canal.
>
> **(4) O que falta — e por isso o desfecho é parcial.** O argumento
> de 1503.07436 **não foi traduzido para as convenções deste
> repositório**. O teste que fecharia:
>
> > Pegar uma célula IBB genuína — **β₂ = β₃ = 0, β₁ > 0,
> > 0 < β₄ < 2β₁** —, seguir o ramo infinito e medir, **na convenção
> > do projeto**: `r′(N)`, `m_T²/H²`, e o funcional/inequação de
> > Higuchi usado em 1503.07436. Se a tradução fechar e der `r′ < 0`
> > junto com violação do Higuchi na era inicial, o veredito pode ser
> > elevado de `IBB REABERTO` para `IBB EXCLUÍDO NA F1 PELO HIGUCHI,
> > NÃO PELO ZERO DO LAPSO`.
>
> **(5) Estado: o ramo infinito CONTINUA REABERTO** *[estado desta
> nota quando escrita; superado pelo bloco de VEREDITO logo abaixo —
> mas só na parte "reaberto": a derrubada do `ξ = 0` que esta nota
> registra permanece de pé, e é parte do veredito]***.** O R-12i
> derrubou
> o argumento específico do repositório (`ξ = 0 ⟹ singularidade
> física`) e ele **continua derrubado** — nada nesta nota o
> ressuscita. O argumento de 1503.07436 é **outro**, é da literatura,
> e está pendente de tradução. **Esta ordem é deliberada e preserva o
> R-12i:** o corpus admitiu que a *primeira* razão para excluir o ramo
> estava errada, e só *depois* foi verificar se havia uma *segunda*
> razão válida. Os itens (b) e (c) do R-b seguem abertos.

> **[VEREDITO — 2026-08-13, R-13a + R-13b; desfecho FINAL do R-b]**
> *Bloco acrescentado; o §1.6, o §6 e a nota datada acima permanecem
> intactos como registro do caminho.*
>
> **RAMO INFINITO IBB DA F1: EXCLUÍDO PELO GHOST DE HIGUCHI.** O
> teste que a nota acima especificava — item (4), célula IBB genuína,
> medir `r′(N)`, `m_T²/H²` e o funcional de Higuchi na nossa convenção —
> **foi executado**, e o veredito é o que a própria nota antecipava
> como possível: **`IBB EXCLUÍDO NA F1 PELO HIGUCHI, NÃO PELO ZERO DO
> LAPSO`**.
>
> **Qualificação obrigatória, que precisa aparecer toda vez que o
> histórico desta saída for contado.** A exclusão original, pelo
> cruzamento `ξ = 0`, permanece **REVOGADA** — este bloco **não**
> reverte o §1.6, que é o resultado deste documento e continua correto.
> A exclusão vigente é **independente**: o ramo infinito viola a
> condição de Higuchi **durante toda a história** nas células IBB
> testadas. A contagem de saídas passa de "três fechadas + uma
> reaberta" a **quatro rotas novamente fechadas, com a exclusão do IBB
> inteiramente substituída** — e a substituição tem de ser visível,
> nunca a contagem sozinha.
>
> **Evidência.** A condição de Higuchi de Könnig 2015 (arXiv:1503.07436,
> eq. 14) foi extraída **na fonte** e traduzida para as convenções do
> projeto (R-13a §2), e a tradução foi **re-verificada por CAS em rota
> independente** — três resíduos simbólicos **zero**, com `β_n` e `μ`
> gerais e matéria de poeira (R-13b §8.2), dando
> **Higuchi ⟺ `ξ ≥ r` ⟺ `r′ ≥ 0`**. Medido em células IBB genuínas
> (β₂ = β₃ = 0, β₁ > 0, `0 < β₄/β₁ < 2μ^{3/2}`): `r′ < 0` em **100% da
> história em 108/108 células**; Higuchi satisfeito em **0 de 64 800
> pontos**; concordância Higuchi(fonte) ⟺ `r′ ≥ 0` em **64 800/64 800**;
> **controle positivo** no ramo finito **400/400**. Forma fechada
> `m_T²/H²|_{r_c} = 1 + 1/(μr_c²)` com `μr_c² > 1` sempre ⟹
> **1 < sup(m_T²/H²) < 2 estrito** em toda a janela; e **`μ` é pura
> reescala** no IBB genuíno.
>
> **O que o veredito não é.** *"The IBB branch is not tachyonic in the
> tensor-mass sense; it is excluded by the Higuchi ghost condition."*
> `m_T² > 0` em **108/108** — e isso **não** o salva.
>
> **Complementaridade — é este o achado, e ele fecha o R-b.** *"Within
> the F1 parameterization, the two standard cosmological branches fail
> for complementary reasons: the finite branch violates scalar-gradient
> stability in the early universe, while the genuine infinite branch
> avoids that instability but violates the Higuchi condition throughout
> its evolution."* A separação de canais que este documento nomeou
> (item 3 da nota acima) é o que sustenta a leitura: o gradiente do IBB
> é **saudável segundo a fonte** — §IV A de 1503.07436, que
> **confirma** o resultado de 1407.4331 e **não** o retrata —, canal
> independente que não salva o Higuchi.
>
> **Ponto lógico, declarado.** O gate do R-13b **não mede gradiente**, e
> essa cegueira continua declarada como boa prática (regra 7). Ela
> **não bloqueia o veredito**: um ghost físico basta para excluir,
> independentemente de o gradiente estar saudável. Um teste de `c_s²` no
> IBB é **validação adicional desejável, não requisito** — o veredito
> não o aguarda.
>
> | Saída | Veredito vigente | Razão |
> |---|---|---|
> | Infinite branch / IBB | **EXCLUÍDO** | ghost de Higuchi, `r′ < 0` em toda a história |
> | argumento antigo `ξ = 0` | **REVOGADO** | zero do lapso / quique não é por si só singularidade |
> | gradiente no IBB | **SAUDÁVEL** segundo a fonte | canal independente; não salva o Higuchi |
>
> *Fontes: `docs/resultado_r13a_criterio_higuchi_fonte.md`;
> `docs/resultado_r13b_ibb_ramo_infinito.md` §§4–6 e §8;
> `auditoria/code/out/r13b_ibb_ramo_infinito.txt`.*

---

## 7. Fronteiras deste documento

- **Verificado:** o conteúdo da fonte (§1), a tradução de convenções
  (§2.1), os três números e as identidades algébricas (§2.2–2.3), a
  identificação λ = 1.
- **Não verificado:** a atribuição do resíduo Δ = ½rr′ à perturbação
  de matéria (§4) — é inferência estrutural com predição falsificável,
  não re-derivação.
- **Não testado:** se `Δ = ½rr'` vale para λ ≠ 1. A forma fechada do
  R-12b só existe em λ = 1. (Em `r → 0`, porém, `r′ → 3r` para
  qualquer λ, então `Δ → (3/2)r² → 0` sempre: o `−1` está seguro em λ
  qualquer, *se* a forma de Δ for genérica.)
- **Fora de escopo:** β₂ e β₃ — os autores declaram que a identidade
  (76) **não** vale para os modelos β₂ e β₃, então a extensão da nossa
  comparação a células com β₂ ≠ 0 não pode usar essa rota.

**Fila que este resultado abre:**

1. **δρ_m na L2** e re-derivação do R-12b — decide o §4 e resgata (ou
   mata) o `m_ef²/H² → 5/2`. É o item caro e o mais valioso.
2. **Reabrir o ramo infinito com β₄ ≠ 0** contra os três argumentos de
   §II/§VI de 1407.4331 (R-b). O R-10c Parte A já registrava "uma
   segunda solução tardia inexplorada" — é essa. *[FEITO — R-13a +
   R-13b, 2026-08-13: o ramo foi reaberto, medido e **excluído pelo
   ghost de Higuchi**, com o argumento `ξ = 0` permanentemente
   revogado. Ver o bloco de VEREDITO do §6.]*
3. **Correções de texto** (não executadas aqui): cap. 07 §4 (§5 acima)
   e `posicionamento_literatura.md` linha 24.
4. Reescrever o enunciado de novidade do setor escalar segundo a
   tabela de §6.
