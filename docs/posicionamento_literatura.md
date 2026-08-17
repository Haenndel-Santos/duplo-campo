# Posicionamento na Literatura — Consolidação

**Data desta versão:** 2026-08-13 (reescrita integral).
**Atualização:** 2026-08-13, arco **R-12i → R-13a → R-13b** — o ramo
infinito deixou de estar reaberto. Ver §0 evento (4), §1.1b, §2b R-b
(**RESOLVIDO**), §3 (ranking reordenado) e §5 (fila).
**Versão anterior:** 2026-08-11 (commit `e6d3ee1`, preservada no git).

**Método (herdado da v1):** quatro verificações independentes em
paralelo (instabilidades escalares bimétricas; massa variável e
constraint secundária; Stückelberg/Weinberg–Witten/spin-2 composto;
originalidade do conceito e da classe), com disciplina declarada por
item: **VERIFICADO-NA-FONTE** (abstract ou texto lido) vs
**NÍVEL-DE-BUSCA** (só buscas; ausência nunca é prova). Este documento
é o insumo da introdução e bibliografia do paper e da v2 enxuta.

**Aviso metodológico (mantido, e ele vale mais hoje do que valia):**
tudo aqui é literatura = **nível 3** do projeto, agora com fontes
nomeadas. Nada abaixo substitui as derivações próprias; posiciona-as.
As exceções parciais são **duas**, e são da mesma natureza: nos dois
casos o *conteúdo* da fonte continua sendo nível 3, e o que sobe de
nível são as **identidades algébricas** que ligam as fórmulas
publicadas às nossas.

1. **O bloco do R-12i (§1.1):** as identidades foram fechadas
   simbolicamente (resíduo 0) e estão transcritas em
   `docs/resultado_r12i_confronto_konnig.md` — que declara, ele
   próprio, não ter deixado script novo versionado.
2. **O bloco do R-13a/b (§1.1b):** a tradução do critério de Higuchi
   para as convenções do projeto é álgebra do
   `docs/resultado_r13a_criterio_higuchi_fonte.md`, e foi
   **re-verificada por CAS em rota independente** pelo
   `docs/resultado_r13b_ibb_ramo_infinito.md` §8.2 (três resíduos
   simbólicos zero, `β_n` e `μ` gerais). Onde a tradução fechou, o
   enunciado deixa de ser importação e passa a ser **medida interna**
   (`M-13b`). O que **não** fechou está em §6, P-6.

**Aviso de disciplina (novo).** A v1 declarava a disciplina "por item"
mas só a **registrou** em alguns itens (`(nível-de-busca)`,
`Confirmado na fonte`, `verbatim`, `verificados — nada`). Onde a v1 não
registrou, esta versão marca **`n/r`** (não registrado) e manda
**tratar como NÍVEL-DE-BUSCA** — o default conservador. Isso não é
rebaixamento de nenhuma fonte: é a recusa de herdar um nível de
verificação que ninguém escreveu. Ver §6, pendência P-1.

**A função deste documento.** Ele é o filtro que impede o repositório
de reivindicar o que não é dele. Depois do R-12i, essa função deixou
de ser hipotética: a linha central do setor escalar passou de
"resultado nosso" a "confirmação de um resultado de 2014". **E depois
do arco R-13 ela mostrou o outro lado:** o filtro não só rebaixa. A
exclusão do ramo infinito **caiu** com o argumento próprio e **voltou**
por um argumento alheio, traduzido e verificado — e o que este arquivo
protege, nesse caso, não é o veredito, é a **proveniência** dele.

---

## 0. Por que esta reescrita — dois eventos, uma inversão, e um arco que fechou

A v1 ficou inteiramente para trás de três coisas; o arco que se seguiu
acrescentou uma quarta.

**(1) Erratum-02 (2026-08-12).** Um bug numérico (`reduz_ponto`,
duplicação do Ċ nas entradas off-diagonais de `W_XX`) fabricava um
terceiro DOF escalar espúrio, promovendo a direção de vínculo Ψ_f a
grau propagante. **Caíram com ele:** o taquião persistente no ponto
fixo dS tardio, o fantasma de norma quase-nula na fresta μ→0, a banda
de amplificação métrica (lnA ≈ +4) e a previsão de excesso ISW.
Fontes: `auditoria/erratum_02_reducao_numerica.md`,
`docs/resultado_r7_cascata.md` §4 (tabela de supersessão),
`manuscript-v2/07_setor_escalar.md` Atos 2–3. **Quatro linhas da
tabela-mestra da v1 descreviam esses objetos**; elas saíram do §1 e
estão no §1.3.

**(2) O arco R-10 → R-12 (2026-08-13).** Um no-go *novo*, medido com o
instrumento já corrigido: instabilidade de gradiente do escalar
métrico, `c_s² = −1` exato em r → 0 na classe F1, 108/108 células, com
forma fechada exata na célula mínima e `c_s² = +1` exato no atrator
tardio. Fontes: `resultado_r10a_gradiente.md`,
`resultado_r11_nogo_gradiente.md`,
`resultado_r12_instrumento_e_cs2.md` (Erratum-03, instrumento),
`resultado_r12b_teorema_cs2.md`. **Nada disso estava na v1.**

**(3) R-12i (2026-08-13) — o confronto com a fonte primária, que
inverte o quadro de novidade.** O texto integral da versão publicada
de Könnig, Akrami, Amendola, Motta & Solomon (PRD 90, 124014 =
[arXiv:1407.4331]) foi lido e confrontado ponto a ponto. Resultado:

> **O no-go de classe do ramo finito é de 2014 e subsome o nosso.** O
> `c_s² = −1` é corolário de uma linha da equação deles. A forma
> fechada existe, é da **mesma família** que a nossa célula mínima, e
> a fórmula possivelmente incompleta é a **nossa**. O "0.28" que o
> corpus usava como limiar é de **outro modelo**. E a nossa exclusão
> do ramo infinito está em **conflito declarado** com a fonte, no
> único modelo que ela considera estável em todos os tempos.

Fonte: `docs/resultado_r12i_confronto_konnig.md` — o item que era, até o
R-13a, o mais bem verificado deste arquivo, e o primeiro cujo nível de
acesso foi "texto integral da versão publicada, conferido por duas
rotas independentes".

**(4) O arco R-13a → R-13b (2026-08-13) — o ramo infinito fecha, e
fecha por outro motivo.** O R-12i deixou o ramo infinito **REABERTO**:
o argumento próprio (`ξ = 0 ⟹ singularidade física`) tinha caído, e o
argumento candidato da literatura (`r′ < 0` vs. Higuchi) ainda não
estava traduzido. As duas metades foram fechadas em sequência:

- **R-13a** (`docs/resultado_r13a_criterio_higuchi_fonte.md`) abriu
  **arXiv:1503.07436 na fonte, por duas rotas independentes** (ar5iv +
  PDF) e **traduziu** o critério para as convenções do projeto:
  `Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0`, com a forma "massa" fechada.
- **R-13b** (`docs/resultado_r13b_ibb_ramo_infinito.md`) **mediu** 108
  células IBB genuínas na convenção do projeto e **re-verificou a
  tradução por CAS em rota independente** (três resíduos simbólicos
  zero, `β_n` e `μ` gerais, poeira).

> **Veredito adotado pelo autor: ramo infinito IBB da F1 — EXCLUÍDO
> PELO GHOST DE HIGUCHI.** A exclusão original por `ξ = 0` permanece
> **REVOGADA**; a vigente é **independente** dela: viola Higuchi
> **durante toda a história** nas células IBB testadas.

E o achado que estrutura o capítulo: **as duas patologias são
complementares.** Ramo finito: Higuchi OK, gradiente ruim. IBB:
gradiente OK (segundo a fonte), Higuchi ruim. Ver §1.1b e §2b R-b.

---

## 1. Tabela-mestra de posicionamento

Coluna **Nível**: `V-12i` = verificado no texto integral da fonte
(R-12i, 1407.4331); `V` = verificado na fonte pela v1, com marca
registrada lá; `B` = nível-de-busca declarado na v1; `n/r` = não
registrado na v1, **tratar como B**; **`V-1503`** =
**VERIFICADO-NA-FONTE pelo autor** (leitura direta de arXiv:1503.07436,
2026-08-13) — o nível com que o "Desfecho parcial" do R-b entrou;
**`V-13a`** = **VERIFICADO-NA-FONTE, texto integral de 1503.07436 por
duas rotas independentes** (ar5iv com 378 nós `<math>` + PDF), R-13a —
**supersede o `V-1503`** onde os dois se sobrepõem, e é hoje o nível
mais forte de *literatura* deste arquivo; **`M-13b`** = **medida
interna do projeto** (R-13b), **nível 2b** na varredura de 108 células
e **2a** nas formas fechadas — **não é literatura**.

**Duas regras de nível, e nenhuma delas se afrouxou com o R-13:**

1. **Literatura continua sendo nível 3.** `V-1503` e `V-13a` verificam
   *o que a fonte diz*, **não** que o enunciado dela valha nas nossas
   convenções.
2. **O que fecha a distância entre nível 3 e o corpus é a tradução —
   e ela agora existe, para este item específico.** O R-12i pedia o
   teste de tradução; o R-13a §2 o entregou (mapa `r_K = √μ r`,
   `β_n^K = A μ^{−n/2}β_n`) e o R-13b §8.2 o **verificou por CAS em
   rota independente** (resíduo 0 em três identidades, `β_n` e `μ`
   gerais). Onde a tradução fechou, o enunciado passa a ser
   **medida interna (`M-13b`)** e não importação. Onde ela **não**
   fechou — em particular o **mapa de convenções** do R-13a §2.1, que é
   *entrada* e não saída do R-13b —, continua valendo o nível 3. Ver
   §6, P-6.

### 1.1 Bloco A — o setor escalar depois do confronto (R-12i)

Este bloco é novo. Ele não existia na v1 e é o mais bem verificado do
arquivo.

| Nosso resultado | Estado na literatura | Veredito de novidade | Nível |
|---|---|---|---|
| **No-go de classe por gradiente** na F1 (ramo finito, β₃ = 0, matéria só em g): `c_s² < 0` em todo o regime r → 0, em 108/108 células da forma-β | **Publicado em 2014.** 1407.4331 §V: *todas* as soluções de ramo finito, para *qualquer* combinação de parâmetros, são inviáveis no fundo ou linearmente instáveis no passado. **Isto subsome o nosso enunciado** | **Já conhecido — confirmamos, não descobrimos.** Rebaixar de "resultado" a *reprodução independente de um no-go publicado, com o valor `−1` explicitado e a forma fechada exibida*. Ver também o risco R-a (§2b) sobre a palavra "no-go" | **V-12i** |
| **`c_s²(r → 0) = −1` exato** | Corolário de uma linha das eqs. (69)/(73): numerador → −1, denominador → 1. Eles **não escrevem o valor** — falam em "velocidade do som imaginária" — mas ele está lá para quem avaliar o limite | **Não é descoberta; é leitura explícita da fonte.** O que é nosso é a rota independente até o mesmo número | **V-12i** |
| **`c_s² = +1` exato no atrator tardio** `r_∞ = (√13−1)/6` | A eq. (73) avaliada em λ = β₀/β₁ = 1 dá **+1 exato** no mesmo ponto (R-12i §2.3, concordância simbólica) — logo também é corolário da forma fechada publicada | **Já contido na fonte.** Nosso = a segunda rota. Valor de método (ver linha "reprodução independente") | **V-12i** |
| **Forma fechada de `c_s²(r)`** na célula mínima (β₂ = β₄ = 0), grau 6 em r | **A família é a mesma.** A nossa célula **é** o modelo β₀β₁ deles com β₀/β₁ = 1 (assinatura inequívoca: `r_∞ = (√13−1)/6` resolve `λ = 1` exatamente). Eles têm a eq. (73), `c_s² = (9r⁴+12r²+2(β₀/β₁)r−1)/(3r²+1)²` | **Já conhecido como objeto.** As duas fórmulas concordam **exatamente** em `c_s²(0) = −1`, no coeficiente de r e em `c_s²(r_∞) = +1`, e diferem por `Δ = ½·r·r′ = (3/2)r²Ω_tot/(1+3r²)` — **proporcional à densidade de matéria**. Diagnóstico (inferência declarada, **não** re-derivada): a nossa L2 fixa `rho_s = 0`, eles carregam δρ/θ nas eqs. (39)–(40) — **a fórmula possivelmente incompleta é a nossa**. Rebaixar a "forma fechada da célula *sem perturbação de matéria*" | **V-12i** (identidades, resíduo 0); a atribuição de Δ é **inferência estrutural** |
| A identidade `c_s² = −r''/(3r')` | **É deles** — eq. (76), declarada válida para todos os submodelos de β₀β₁β₄. Não vale para β₂ e β₃ (declarado por eles) | **Deles. Citar.** O R-12b a redescobriu por acidente e em forma deslocada (`c_s² = −r''/(3r') + ½rr′`) | **V-12i** |
| **`m_ef²/H² → 5/2`** (termo de massa sub-dominante da relação de dispersão, ordem k⁰) | Eles descartam explicitamente as soluções independentes de k como subdominantes e **nunca dão o termo de massa** | **A candidata própria mais forte do setor escalar — e declaradamente em risco.** É ordem k⁰, exatamente onde a perturbação de matéria ausente da nossa L2 entraria (via Poisson). **Não reivindicar antes do teste δρ_m** (§5, item 1) | **V-12i** (quanto à ausência na fonte) |
| **108/108 células** — insensibilidade de `c_s²(r→0)` a (β₀, β₂, β₄, μ) | **Regra publicada:** no passado, todo modelo multiparamétrico viável de ramo finito **reduz ao modelo de interação de ordem mais baixa** (β₁β₂, β₁β₃, β₁β₂β₃ → β₁). Como o R-12b elimina β₁ pela Friedmann (logo β₁ ≠ 0 sempre), as 108 células estão **dentro do escopo da regra** | **Confirmação numérica de uma regra publicada** — mesma função que o ramo algébrico já cumpre nesta tabela: **âncora de validação do método**, não resultado novo | **V-12i** |
| **Reprodução independente dos dois extremos exatos** por maquinaria distinta (Schur/Faddeev–Jackiw ⟶ 2 DOF vs. a redução 10→2 deles) | Não é afirmação sobre a literatura: é a concordância **exata** de duas rotas independentes em `−1`, no coeficiente linear e em `+1` | **Sólida — como validação de MÉTODO, não como física.** Vale um parágrafo do paper; não vale uma reivindicação de novidade | **V-12i** |
| A patologia primordial da F1 é de **gradiente** (∝ k²), com cinética positiva | Mesma doença, mesmo modo, mesmo observável: 1403.5679 (λ₁ = −k²(2w₁+1)); 1407.4331 §V (o sistema 2-DOF reduzido, com ω imaginário = "velocidade do som imaginária"). **O limiar de r exige qualificação de modelo:** a raiz exata √((√5−2)/3) = **0.28052** é do modelo **β₁-puro (β₀ = 0)**, eq. (69); no **nosso** modelo (β₀β₁, λ = 1) a eq. (73) dá **0.21448**, contra o nosso **0.20793** — **3.1%**, não os 34.9% da comparação errada | **Já conhecido.** A v1 dizia "patologia de natureza distinta" — isso valia para o *taquião de massa*, que caiu com o Erratum-02 (ver §1.3). Hoje a nossa doença **é** a doença deles. A comparação explícita continua obrigatória no paper, mas com o sinal invertido: não "a nossa é diferente", e sim "a nossa é a mesma, e reproduz o número" | **V-12i** |
| **Exclusão do ramo infinito pelo nosso critério `ξ = 0`** (ξ cruza zero ⟹ lapso do setor f se anula ⟹ ponto singular) | **EM CONFLITO DECLARADO COM A FONTE.** `ξ = r + dr/dN` e `ξ = X/a` com `X ≡ ḃ/ℋ`: **mesmo sinal, mesmo zero**. O §II/§VI de 1407.4331 trata esse quique de `b` **explicitamente** e o defende como físico, com três argumentos declarados (f não acopla à matéria; nenhuma variável singular; `√(−det f)·R̄(f)` finita e não-nula) | **ARGUMENTO PRÓPRIO REVOGADO — e continua revogado.** O zero do lapso / quique **não é, por si só, singularidade**. Nada do arco R-13 o ressuscita, e essa ordem é deliberada (§2b, R-b). A exclusão **vigente** do ramo infinito é de **outra natureza** e está no §1.1b. Registro adicional: o R-13b mediu o quique nas nossas convenções e **confirmou a estrutura descrita pela fonte** — cruzamento de ξ **único**, em a = 0.674…0.713 (z = 0.40…0.48), em 108/108 células, com locus em forma fechada `β₄r³ − 6μβ₁r² + 4β₁ = 0` (concordância 1.78e−15 contra bissecção) | **V-12i** (o conflito com a fonte); **M-13b** (o quique medido, 2a + 2b) |

### 1.1b Bloco A′ — o desfecho do ramo infinito e o critério de Higuchi (R-13a → R-13b)

Este bloco também é novo. Ele registra o que o arco
**R-13a (fonte) → R-13b (medida)** acrescentou, e é o bloco onde vive o
**veredito vigente** sobre o ramo infinito. Disciplina, repetida porque
é justamente aqui que ela poderia escorregar: **`V-13a` é literatura
(nível 3)**; **`M-13b` é medida do projeto (2a/2b)**; a **tradução**
entre os dois é álgebra do R-13a **verificada por CAS em rota
independente** pelo R-13b §8.2.

| Nosso resultado | Estado na literatura | Veredito de novidade | Nível |
|---|---|---|---|
| **O critério de Higuchi nas nossas convenções:** `Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0`, com a forma "massa" `(m²M_ef²/M_f²)·ℬ(r)·(1+μr²)/r ≥ 2H²`, isto é **a caixa de `m_T²` do cap. 06 com `ξ → r`** | **A inequação é da literatura.** 1503.07436 eq. (14), escrita **só em `r` e nos `β_n`** — a fonte **não escreve massa nenhuma** (resultado negativo firme, R-13a §1.7). Ela credita a condição a **Fasiello–Tolley 1308.1647**, e as equivalências (15)/(16)/(18) a **Yamashita–Tanaka 1401.4336** e **De Felice et al. 1404.0008**. O `B₂` deles **é**, letra por letra, o nosso `ℬ(r) = β₁+2β₂r+β₃r²` | **A tradução é nossa; o critério não é.** O mapa (`r_K = √μ r`, `β_n^K = Aμ^{−n/2}β_n`) é sobredeterminado pelas duas Friedmann e fecha — e a caixa da `derivations/02`, derivada por maquinaria independente (ação TT, Sylvester, autovalor de `K⁻¹M`), **reproduz exatamente** o bound FLRW no limite `ξ = r`. Isso vale como **validação cruzada de método**, não como física nova | **V-13a** (a fonte); **M-13b** (a cadeia interna `(14) ⟺ (15) ⟺ 𝒲′(r) ≤ 0 ⟺ r′ ≥ 0`, **três resíduos simbólicos zero**, `β_n` e `μ` gerais, poeira) |
| **Exclusão do ramo infinito / IBB da F1** — veredito **vigente** | **JÁ PUBLICADO, e mais forte do que as ressalvas que a própria fonte cita.** 1503.07436 §III A e §VI: *todos* os ramos infinitos sofrem do fantasma de Higuchi **em todos os tempos** — a fonte **promove a "early times"** de Lagos–Ferreira 1410.0207 para **"all times"**, e registra ainda o ghost de helicidade-2 em tempos iniciais de Cusin et al. 1412.5979 | **RAMO INFINITO EXCLUÍDO PELO GHOST DE HIGUCHI.** Confirmação numérica, nas nossas convenções, de um veredito publicado — **não** é descoberta. O que é nosso é ter medido: `r′ < 0` em **100% da história em 108/108 células** (max r′ = −6.05e−5 na varredura inteira); Higuchi satisfeito em **0 de 64 800 pontos**; **0/108 células** em qualquer época; concordância entre as duas formas equivalentes em **64 800/64 800**; e controle positivo do ramo finito passando **400/400**. A exclusão é **independente** do argumento `ξ = 0` revogado | **V-13a** (o veredito da fonte); **M-13b** (a medida, 2b, fronteiras no R-13b §0) |
| **`m_T²/H²\|_{r_c} = 1 + 1/(μr_c²)`** no ponto fixo tardio do IBB, com a fronteira de existência dando `μr_c² > 1` ⟹ **`1 < sup_história m_T²/H² < 2` estrito, para todo μ** | **Nada a confrontar: a fonte não escreve massa de gráviton em lugar nenhum** (R-13a §1.7). Não há forma fechada publicada para comparar | **Forma fechada própria, e é o objeto que fecha a exclusão pelo canal do repositório.** Mas é uma quantidade de **exclusão**, não de reivindicação: o seu conteúdo é "o IBB nunca chega a 2". Verificado: max desvio 5.59e−4; min(μr_c²) = 1.284908; max da razão = 1.778266 | **M-13b** (2a fechado + 2b em 108 células) |
| **Janela de existência `0 < β₄/β₁ < 2μ^{3/2}`** | A fonte dá **`0 < β₄ < 2β₁`** — que é o **caso particular μ = 1**, porque ela **fixa `M_f = M_g`** (nota de rodapé 6 de 1503.07436, que declara a escolha como *permitida por redundância de parâmetros mas não a mais natural*) | **Generalização própria em μ**, verificada contra bissecção a ≤ 5.0e−14 (`y_max(1) = 2.0000000000`). Modesta: é a forma μ-covariante de um enunciado publicado, não um eixo físico novo — ver a linha seguinte | **M-13b** (2a) |
| **`μ` é PURA REESCALA no IBB genuíno** — com `r = μ^{−1/2}u`, `β₄/β₁ = 2μ^{3/2}f`, `ρ̂ = μ^{1/2}ρ̃`, tanto `Ω_m` quanto `m_T²/H²` viram funções **só** de `(f, ρ̂)` | A **redundância** de parâmetros é declarada pela fonte (nota 6); que ela seja **pura reescala neste bloco** não está lá | **Fecha o enunciado em vez de abri-lo.** A varredura em μ — a lacuna que o parecer de astrofísica apontou como decisiva — mostra que μ **não** é eixo físico novo aqui. Histórias a `f` fixo coincidem em **≤ 4.0e−15** com μ variando duas ordens de grandeza | **M-13b** (2a + 2b) |
| **A complementaridade das duas patologias** (o achado estrutural do arco) | **É a arquitetura declarada das duas fontes juntas**, não uma leitura nossa. 1503.07436 §IV A **mantém** o resultado de gradiente do IBB de 1407.4331 — ela **não o retrata**: os modos escalares do IBB são estáveis e a condição (36) é *"equivalente a `ρ > 0` nesse ramo e, portanto, trivialmente satisfeita em todos os tempos"* — e mata o IBB por **outro canal** | **Reprodução independente, com maquinaria própria e `μ` generalizado, de um padrão que está nas duas fontes.** Frase de nível paper, e é assim que deve ser escrita: *"Within the F1 parameterization, the two standard cosmological branches fail for complementary reasons: the finite branch violates scalar-gradient stability in the early universe, while the genuine infinite branch avoids that instability but violates the Higuchi condition throughout its evolution."* Contraste medido na **mesma rodada e com a mesma maquinaria**: finito `m_T²/H² → 12` e Higuchi **400/400**; IBB máximo **1.78** e Higuchi **0/64 800** | **V-13a** (o gradiente do IBB é da fonte, **não** medido por nós); **M-13b** (o lado Higuchi) |
| **A armadilha de sinal entre as duas fontes:** 1407.4331 usa `X ∝ e^{iωN}`; 1503.07436 usa `Ξ_i ∝ e^{ωt}` (exponencial **real**) | Ambas as convenções são declaradas nas respectivas fontes; **nenhuma das duas avisa sobre a outra** | **`sign(ω²)` NÃO é comparável entre as duas sem traduzir o ansatz.** Em 1503.07436, `ω² < 0` ⟹ oscilante ⟹ **estável** — o oposto de 1407.4331. Demonstração fechada: a eq. (24) dá `ω² = +(k/ℋ)²r''/(3r')` enquanto o R-12i extraiu `c_s² = −r''/(3r')` de 1407.4331 — **mesma física, sinal de ω² trocado**. É a **mesma família do erro do "0.28"** (§6): número/sinal importado sem a sua convenção | **V-13a** |
| **O funcional FLRW de Higuchi da fonte dá `3`, não `12`** | Consequência algébrica da tradução (R-13a §3.2), lá declarada como **não re-verificada numericamente** | **Verificada depois, e bate:** medido `m_T²/H² = 12.0000` (ξ dinâmico, caixa do cap. 06) contra `m_T²\|_{ξ→r}/H² = 3.000002` (objeto de Könnig), no mesmo ramo finito primordial. **É o número que requalificou o `m_T²/H² → 12` e o fez trocar de lugar no ranking** (era nº 1, hoje nº 2) — ver §1.2 e §3 | **M-13b** (2a) |

**Um ponto lógico, declarado e resolvido** (correção do autor, registrada
porque o R-13b a levanta corretamente na sua §1). O gate do R-13b
**declara-se cego ao gradiente**: ele mede Higuchi/helicidade-0 e o
setor tensorial, e nada diz sobre `c_s²` no ramo infinito. Essa
declaração **fica**. Mas ela **não bloqueia o veredito**: um ghost
físico basta para excluir, e é a própria fonte que estabelece a
assimetria de peso — fantasma é **fatal**, gradiente **não** (R-13a
§1.6, §III D de 1503.07436: Hamiltoniano ilimitado por baixo ⟹
decaimento do vácuo). Medir `c_s²` no IBB seria **validação adicional,
não requisito** — e continua na fila (§5) por esse estatuto.

> **[O ELO FECHOU — 2026-08-17, `docs/auditoria_r13.md` §4.]** A
> validação adicional **foi feita**. `c_s²` do modo métrico do sistema
> 2-DOF, medido no ramo infinito de células IBB genuínas com a
> maquinaria limpa do R-12f/g: **positivo em 50/50 pontos** (5 valores
> de `f = y/2μ^{3/2}` × 10 épocas de `a = 3e−5` a `a = 30`), indo de
> **+1/2** no passado profundo a **+1** no atrator tardio, com mínimo
> **0.4428**. Acompanha o canal fechado da literatura `−r″/(3r′)` com
> desvio `|Δ| ≤ 0.093` que **zera nos dois extremos**. Controle
> positivo na mesma rodada: ramo finito dá **−0.99999750**.
> Degenerescência em `μ` (gate novo, do corolário F-3): **1.7e−16**.
>
> **Consequência para a linha da complementaridade na tabela acima:** o
> nível dela deixa de ser *"`V-13a` (o gradiente do IBB é da fonte,
> **não** medido por nós); `M-13b` (o lado Higuchi)"* e passa a ser
> **`M-13b` + `M-13aud` nos DOIS lados**, com `V-13a` como
> concordância independente. A frase de nível-paper pode agora ser
> escrita como medida própria em vez de importação — mantendo, claro, o
> crédito de que o padrão está publicado.
>
> **Fronteira herdada, que NÃO muda:** a `L2` deste projeto não tem
> `δρ_m`. Toda medida de `c_s²` aqui herda a mesma limitação do
> R-11/R-12g, e ela continua declarada.

### 1.2 Bloco B — o restante da tabela-mestra (herdado da v1)

| Nosso resultado | Estado na literatura | Veredito de novidade | Nível |
|---|---|---|---|
| Fundo do ramo finito (limite GR primordial exato, r: 0 → r_∞) | Ramo finito padrão (Könnig et al. 1407.4331 — mesma convenção; Akrami et al. 1503.07521). **Confirmado ao nível de identidade pelo R-12i**: `r ≡ b/a` (eq. 17), normalização β letra por letra (eq. 16), `M_f = 1` ⟺ `μ = 1, M_ef² = 1/2`, e o nosso `dr/dN = −3ρ̃/ρ̃′` **é** a eq. (21)+(22) deles — *os fundos são o mesmo fundo* | **Já conhecido** — e agora sabemos *exatamente* o quanto | **V-12i** |
| Higuchi automático no ramo finito | **Provado em geral**: viabilidade ⇒ r′ ≥ 0 ⇒ sem fantasma de Higuchi (Könnig 1503.07436 eqs. 14–18, que credita Fasiello–Tolley 1308.1647, Yamashita–Tanaka 1401.4336 e De Felice et al. 1404.0008). **Texto integral verificado por duas rotas (R-13a):** em cosmologia **expansiva**, `r` tem de **crescer** para satisfazer a condição associada ao Higuchi e manter sãos helicidade-0 e helicidade-2 — sob três hipóteses declaradas: `ρ > 0`, `1 + w_tot > 0`, `r ≥ 0` | **Já conhecido** — citar, não reivindicar. **Correção de 2026-08-13 (mantida):** as duas linhas sobre 1503.07436 (esta e a do ramo infinito) **não são contraditórias**; são o **mesmo critério aplicado a ramos diferentes** — finito r′ ≥ 0 passa, infinito r′ < 0 não passa. **Acréscimo do arco R-13:** o critério está **traduzido** (§1.1b) e **medido dos dois lados** — controle positivo do ramo finito passa `r′ ≥ 0` **400/400** e Higuchi-da-fonte **400/400**. O que era importação virou medida | **V-13a** (o enunciado da fonte, supersede o `V-1503`); **M-13b** (a tradução verificada por CAS e o controle positivo) |
| **m_T²/H² → 12** universal no primordial (setor tensorial) | Nenhuma razão universal publicada (Fasiello–Tolley 1206.3852/1308.1647, Könnig, Cusin et al., Akrami et al. verificados — nada encontrado). **1407.4331 é setor escalar: não toca esta linha.** **1503.07436 também não escreve massa de gráviton em lugar nenhum** (R-13a §1.7, resultado negativo firme por duas rotas) — o que **reforça** a afirmação de ausência neste ponto específico | **Continua novo como objeto matemático — mas a LEITURA caiu.** A fórmula por época segue: `m_T²/H² → 3(4+3w)`, **12 em matéria, 15 em radiação**, e os rótulos "primordial" do corpus significam "era de matéria" (D3, §2). **O que o R-13 derrubou é a venda:** o `12` **não** é margem de Higuchi. O funcional FLRW de Higuchi da fonte dá **`3`** no mesmo limite (medido: 3.000002) — **satisfaz o bound 2 com margem de 1.5×, não 6×**. Pior: o `m_T² ≥ 2H²` com `ξ` **dinâmico**, como o repositório o usa, **não corresponde a nenhum dos dois critérios da fonte** (helicidade-0 é `ξ ≥ r`; helicidade-2 é o **sinal do lapso**, `ξ > 0`). **Reivindicar o `12` como razão de massa tensorial: sim. Como margem de Higuchi: não.** Ver §3 | `V` para a busca nas 4 fontes; **`B`** para a conclusão de ausência; **`V-13a`** para o resultado negativo em 1503.07436; **`M-13b`** para o `3` |
| Degenerescência cinética no ramo algébrico | É a fenomenologia publicada do "branch 1": cinética evanescente, strong coupling, sem grau extra no linear (1111.1983, 1202.1986, 1403.5679); primos em massive gravity: fantasma não-linear escondido (1111.4107, 1206.2080) | **Já conhecido — usar como âncora de validação do método.** *Estado interno:* o ramo algébrico está **deferido** (cap. 07 Ato 4, "pendências declaradas") e não foi reexaminado com o instrumento limpo; o veredito de literatura não depende do nosso número | `n/r` |
| Classe β_n(φ) em bigravity | Existe como classe: chameleon bigravity = TODOS os β com fator global f(φ) (De Felice–Mukohyama–Uzan 1702.04490; +Oliosi 1711.04655); MVMG = V(ψ)·potencial, métrica fixa (Huang–Piao–Zhou 1206.5678); possibilidade de coeficientes individuais declarada desde 2012, nunca estudada | **Subclasse mínima (β₁ único) é primeiro estudo dedicado.** Caveat da síntese dos pareceres (§4.2, item 6): a escolha "β₁ único" **não é radiativamente estável** — os e_n se misturam sob renormalização — e ela sustenta *simultaneamente* o fator atenuante do Gate 2A e a novidade reivindicada | `n/r` (a existência da classe); `B` (o "nunca estudada") |
| Constraint secundária não-fatorada (resíduo p_φβ₁′) | Análogo publicado em MVMG (métrica fixa, fator global: termo ∝ π·V′ entra e o vínculo sobrevive); em chameleon bigravity o termo φ̇U_,ξφ está implícito nas eqs. de fundo **mas a análise de vínculos NUNCA foi feita — lacuna explícita** | **Novo na forma bigravity/β₁-único**; a lacuna hamiltoniana da classe-irmã é nossa oportunidade. **Dois caveats obrigatórios:** o resultado é de **minisuperespaço**, e a síntese dos pareceres (§4.3, item 11) aponta que `manuscript-v2/04_bianchi_e_vinculos.md` §4 **embaça** que o resíduo é sombra da Bianchi e **não** o par de constraints que remove o BD | `n/r` |
| Fundo transientemente FORA dos dois ramos, com pouso | Sem nome nem caracterização na literatura; mecanismo implícito nas eqs. do chameleon bigravity, nunca estudado como estrutura | **Novo como fenômeno caracterizado** (2b, uma célula — declarar). *É fundo:* não passa pela redução numérica, logo **intocado** pelos Erratums 02 e 03 | `n/r` |
| Back-reaction contra a condensação (limiar Δ) | O mecanismo é o coração do camaleão: "interaction terms play the role of a potential for φ" (1702.04490, **verbatim**) | **Aplicação nova de mecanismo conhecido** — citar 1702.04490; o limiar quantitativo e a competição com a bifurcação são nossos | **`V`** |
| Helicity-0 = Stückelberg das difeos relativas | Estrutura padrão (AGS hep-th/0210184; Hinterbichler 1105.3735; de Rham 1401.4173); identificação **qualitativa** do modo patológico cosmológico como helicity-0 já publicada (**Aoki–Maeda–Namba 1506.04543 — citação obrigatória**; Könnig 1503.07436) | **PENDENTE — não decidido nesta reescrita.** A v1 punha a nossa contribuição na **medida** (projeções 0.995; identidade k-dependente π_L/π⁰; cancelamento quebra×EH). Mas os objetos medidos eram *o taquião congelado de k = 1* (π_L 0.995) e *o fantasma da fresta μ = 0.1* (π⁰ 0.998) — **os dois estão na lista dos que caíram** (cap. 07 Ato 4). A medida nunca foi refeita sobre o sistema 2-DOF corrigido e **não aparece em nenhuma tabela de supersessão**. Ver §6, pendência P-2 | `n/r` |
| Weinberg–Witten só bloqueia massless; f₂(1270) spin-2 composto | **Confirmado na fonte** (enunciado, escopo, PDG); nenhuma extensão a massivo composto encontrada | gate1c §2 **sólido como está** | **`V`** |
| Programa (b1): spin-2 massivo emergente, g fundamental | Precedentes reais em 4 tradições: **Isham–Salam–Strathdee 1971 (f-dominance — o precursor literal)**; holografia (Kiritsis 2006; Aharony–Clark–Karch); QCD (f₂/glueball 2⁺⁺); **FQH "chiral graviton" (Nature 628, 2024 — spin-2 massivo de métrica INTERNA, medido)**; análogo 2-BEC bimétrico (Visser–Weinfurtner gr-qc/0506029; Liberati–Visser–Weinfurtner gr-qc/0510125) | **Correto como programa; original como síntese** — o nicho exato (relativístico 4D, quebra interna, g fundamental) segue vago. Obstáculos a declarar: BD, Λ₃, positividade (Alberte–de Rham–Jaitly–Tolley 1910.11799), torre infinita | `n/r` |
| Conceito TDCP (bifurcação do modo diferencial → dois setores) | Mosaico de vizinhos: análogo 2-BEC (modos in/out-of-phase → bimetria com setor massivo — **o paralelo estrutural mais próximo**); Higgs gravitacional ('t Hooft 0708.3184; Chamseddine–Mukhanov 1002.3877); Hossenfelder 0807.2838 (dois setores por postulado); tempo relacional em QG (Page–Wootters, GFT) | **Síntese não encontrada como proposta unificada** — mas novidade-por-síntese é a mais frágil; citar e diferenciar os vizinhos explicitamente | `n/r` |
| Metodologia (gates, estratificação, pré-registro) | No-gos de classe existem (de Rham–Matas–Tolley 1311.6485 é o modelo); programa metodológico como o nosso, não | **Não vender como novidade de física** — é qualidade, não resultado. Registro de hoje: o arco Erratum-02 → Erratum-03 → R-12i é, na avaliação dos cinco pareceres (§8 da síntese cruzada), o ativo mais forte do projeto — inclusive porque **derrubou reivindicações próprias três vezes** | `n/r` |

### 1.3 Registro histórico — linhas da v1 cujo OBJETO deixou de existir

Estas linhas **não foram apagadas**: foram movidas para cá. Elas
descrevem posicionamentos corretos *em relação a objetos que o
Erratum-02 mostrou serem artefato numérico*. Nenhuma delas pode
aparecer no paper.

| Linha da v1 (§1) | O que aconteceu | Onde está registrado |
|---|---|---|
| **Taquião de MASSA primordial** (taxa √\|m²\|, indep. de k) — veredito v1: "conhecido em forma diferente; patologia de natureza distinta" | **Objeto caiu.** Com o instrumento limpo, o termo de massa primordial é **positivo** (`m_ef²/H² → +5/2`) e a patologia vigente é de **gradiente** (`ω²/H² = −kh² + 5/2 + O(r)`). A premissa da linha — "a nossa é de natureza distinta da da literatura" — **inverteu-se**: é a mesma | Erratum-02; `resultado_r12_instrumento_e_cs2.md` §3; `resultado_r12b_teorema_cs2.md` §1 |
| **Taquião persistente no ponto fixo dS tardio** (μ ≥ 0.3) — veredito v1: "genuinamente novo SE o modo for físico; em tensão com a literatura" | **Caiu** (R-7a/R-7f). A era tardia tem `c_s² = +1` **exato**, e o quadro "instável cedo, saudável tarde" da literatura é o quadro real. A "tensão com a literatura" era com um objeto inexistente | `resultado_r7_cascata.md` §4; cap. 07 Ato 4 |
| **Fantasma de norma quase nula em μ→0** (kN ~ μ³) — veredito v1: "não documentado (nível-de-busca)" | **Caiu.** A fresta μ = 0.1 foi varrida sem violações (R-7f); zero autovalores cinéticos negativos em todos os regimes testados | idem |
| **No-go de CLASSE para o setor escalar modulado** — veredito v1: "novo como enunciado de classe (nível-de-busca)" | **Retirado** no R-7e: "no-go de classe retirado (scan μ×β₁ + fresta, zero violações); o no-go escalar da F1 está revogado em todos os regimes que o sustentavam". **Cuidado com a homonímia:** existe hoje *outro* no-go de classe — o de **gradiente** — e esse não é novo: é o de 2014 (§1.1) | `resultado_r7_cascata.md` §5b |

Caíram junto, sem terem tido linha própria na v1 mas sustentando o
ranking e os desafios D1/D2: a **banda de amplificação métrica**
(lnA ≈ +4 → −8.4 estático, −11…−14.7 no pousado), a **previsão de
excesso ISW 2–8×** com a sua "tensão observacional", a **dispersão
p = 0.44** e a **localização da tensão-Akrami** (R-7b/c/d), o
**σ/H ≈ 13** da Fase B (R-7e) e a **contagem de 3 DOFs escalares**
(Erratum-02).

---

## 2. Os desafios de referee (itens de trabalho PRÉ-paper)

**D1 — Sobrevivência do par doente à redução de vínculos.**
**[OBJETO CAÍDO — 2026-08-12.]** A v1 marcava este item como
"RESOLVIDO A FAVOR" (`resultado_d1_reducao.md`, 2026-08-11): a redução
Faddeev–Jackiw exata dava espectro idêntico ao QEP, "o taquião
persiste e o fantasma vira autovalor negativo da matriz cinética
reduzida". **O par doente não existe.** A resolução foi emitida **um
dia antes** do Erratum-02, e tudo o que ela certificava — o taquião, o
fantasma, a contagem congelada 3 — é artefato do `reduz_ponto`. O que
**sobrevive de D1 é a maquinaria**, não o resultado: a redução exata
com aritmética racional é a mesma linhagem que produziu, dois dias
depois, o teorema fechado de `c_s²(r)` do R-12b. Registrar assim, e só
assim.

**D2 — Mesma doença ou doença nova?**
**[OBJETO CAÍDO; a CONCLUSÃO sobrevive por outra rota.]** A v1
registrava "RESOLVIDO 2026-08-11 COM REVERSÃO": a evolução temporal
mostrava que o taquião tardio congelado não era dinâmico e que "o
quadro real converge com a literatura (saudável tarde)". O objeto
(taquião tardio) caiu no dia seguinte. **A conclusão, porém, está hoje
mais forte e por rota independente:** a era tardia tem `c_s² = +1`
exato e o modo métrico é overdamped e decai. E a pergunta-título do
desafio tem hoje resposta limpa, oposta à da v1: **é a mesma doença** —
instabilidade de gradiente do escalar métrico, o mesmo modo e o mesmo
observável de 1407.4331 §V (§1.1). Os avisos metodológicos que o D2
gerou ("congelado não é árbitro dinâmico") **ficam, reforçados**.

**D3 — O "12" é por era.**
**[FECHADO POR DERIVAÇÃO EXTERNA — NÃO VERIFICADO INTERNAMENTE.]**
Dois especialistas independentes (cosmologia e astrofísica), sem
contato, generalizaram para w arbitrário e chegaram à **mesma
fórmula**:

> `ξ = r[1+3(1+w)]` ⟹ **`m_T²/H² → 3(4+3w)`** — **12 em matéria, 15
> em radiação**.

A astrofísica acrescenta `c_f² = (4+3w)²` (radiação: c_f = 5c), com
c_f² → 1 no ponto fixo tardio. Três consequências, nesta ordem de
importância:

1. **Os rótulos "primordial" do corpus significam "era de matéria".**
   A era genuinamente primordial é de **radiação**, onde a constante é
   **15**. O headline "m_T²/H² → 12 universal no primordial" está,
   como escrito, errado de escopo.
2. **Discrepância aberta, não resolvida.** O resumo da cosmologia
   atribui **6** ao caso Λ, enquanto a fórmula comum dá **3** em
   w = −1. Causa provável apontada lá: o limite assintótico foi
   derivado em r → 0 e o ponto fixo tardio tem r → r_∞ ≠ 0 — regime
   diferente. Instrução explícita da síntese, aqui repetida:
   **verificar antes de usar qualquer dos dois números.**
3. **Estatuto.** Ambas as derivações são de **especialistas externos e
   não foram verificadas internamente**. Entram como **candidatas a
   resultado, não como resultado** — é a regra do §9 da síntese
   cruzada, e ela vale integralmente aqui.

*Fonte:* `docs/pareceres_especialistas/00_sintese_cruzada.md` §5.

**D4 — Cura não-linear.** **[ABERTO, e mais agudo do que era.]**
Aoki–Maeda–Namba 1506.04543: mantendo as não-linearidades do
helicity-0, a instabilidade primordial não tem fantasma nem gradiente
(rota Vainshtein). O nosso no-go é quadrático — declarar a fronteira.
**O que mudou:** a própria fonte primária faz esse mesmo movimento no
§VIII (a instabilidade pode ser curada não-linearmente), o que
transforma D4 de "desafio antecipado" em **posição declarada da
literatura contra o nosso enunciado** — ver R-a (§2b). Do nosso lado há
uma medida que a literatura não tem: o R-10d fechou o screening de
Vainshtein como saída nesta implementação (δ_screen ≈ 20–60, *o λ
cancela*). Essa medida é o único argumento próprio disponível para
sustentar a leitura forte, e o paper tem de exibi-la nesse papel. A
rota de escape de Akrami et al. 1503.07521 (M_f pequeno empurra a
instabilidade para antes do BBN) continua na mesa; a fonte primária
nomeia ainda outra, o **acoplamento duplo da matéria**, que permite
r ≠ 0 no passado remoto. **Uma rota saiu da mesa em 2026-08-13:** o
**ramo infinito / IBB**, que era a saída mais óbvia (curar o gradiente
mudando de ramo), está **fechado pelo ghost de Higuchi** — §2b, R-b,
"Desfecho final". Isso *aperta* o D4 em vez de aliviá-lo: as duas rotas
que restam (`M_f` pequeno e acoplamento duplo) são ambas **fora da F1
como está**.

**D5 — Precedentes de certificação prematura.** **[FICA — reforçado.]**
O extended quasidilaton teve "is ghost free" (v1, 2013) revertido pelo
próprio autor para "Boulware–Deser ghost in..." (versão publicada,
2017). Nossa recusa de certificar ausência de BD por contagem numérica
(gate2_ghost §4) tem precedente direto — vira parágrafo do paper, não
fraqueza. **Reforço interno:** o repositório agora tem três retratações
próprias documentadas (Erratum-02, Erratum-03, e o "0.28" do §6), o
que torna o parágrafo mais forte, não mais fraco — desde que ele seja
escrito com os três, e não só com o precedente alheio.

---

## 2b. Os dois riscos criados pelo confronto (R-12i §6) — **um resolvido, um aberto**

Esta seção é nova. Ela existe porque o confronto com a fonte primária
criou dois problemas que **não são de posicionamento, e sim de
substância**, e que o paper tem de absorver antes de qualquer
submissão.

**Estado em 2026-08-13, depois do arco R-13a → R-13b:**

| Risco | Estado |
|---|---|
| **R-a** — a palavra "no-go" | **ABERTO.** É decisão editorial e bloqueia a submissão. E o R-13a o **reforçou**: a assimetria de peso (fantasma fatal, gradiente **não** fatal) é declarada pela fonte, não inferida por nós |
| **R-b** — a exclusão do ramo infinito | **RESOLVIDO.** Ver o "Desfecho final" abaixo. Item (a) executado; itens (b) e (c) **absorvidos pelo desfecho**, não abandonados — ver a leitura de cada um lá |

### R-a — a palavra "no-go"

**O fato.** A fonte lê o mesmo cálculo de forma **mais fraca**. No
§VIII de 1407.4331: a instabilidade **não** exclui automaticamente os
modelos; ela impede o uso da teoria de perturbações linear em escalas
sub-horizonte profundas, e pode ser curada por efeitos não-lineares
(Vainshtein). **O nosso enunciado é mais forte que o da literatura
sobre o mesmo cálculo.**

**Agravante interno — o repositório já se contradiz.** O
`resultado_r10a_gradiente.md` §3b faz, por conta própria, a leitura
fraca: *"a saída de Akrami et al. se aplica — nas escalas mais
violentas a perturbação linear se auto-invalida, e a instabilidade
linear não é, por si, uma refutação"*. O cap. 07 §4, no entanto,
chama o mesmo objeto de **NO-GO DE CLASSE**. Os dois textos não podem
ficar como estão.

**O que decidiria.** Uma de duas coisas, e é escolha editorial, não
cálculo: **(i)** justificar a força extra — e o único argumento
próprio disponível é o R-10d (screening fechado: δ_screen ≈ 20–60, o λ
cancela, não há escala linear protegida), que precisaria ser elevado a
peça central em vez de nota de rodapé; ou **(ii)** adotar a leitura
deles e reescrever o enunciado como *"a implementação F1 tem uma era
em que a teoria de perturbações linear é inválida em escalas
sub-horizonte, cobrindo a recombinação"* — que é mais defensável, mais
próximo do que foi de fato medido, e ainda assim fatal para o programa
observacional do cap. 09. **Recomendação registrada:** (ii), com o
R-10d citado como a razão pela qual a saída padrão não funciona nesta
implementação.

### R-b — a exclusão do ramo infinito (era o mais caro) — **RESOLVIDO em 2026-08-13**

> **Veredito vigente, em uma linha:** **ramo infinito IBB da F1 —
> EXCLUÍDO PELO GHOST DE HIGUCHI.** A exclusão original por `ξ = 0`
> permanece **REVOGADA**; a vigente é **independente** dela: viola
> Higuchi **durante toda a história** nas células IBB testadas.
>
> A proveniência está na tabela do "Desfecho final", e ela é a peça
> que este risco existia para exigir: **o argumento próprio caiu e
> continua caído; o argumento que exclui hoje é outro, é independente,
> e está verificado.**

O que segue é o registro completo, em ordem cronológica. **Nada foi
apagado** — a leitura da proveniência depende de as três camadas
estarem visíveis: o risco como nasceu (R-12i), o desfecho parcial
(1503.07436 aberto), e o desfecho final (R-13a → R-13b).

**O fato (como o risco nasceu).** O nosso critério de exclusão é `ξ = r + dr/dN`; como
`b = ra`, vale `db/dN = aξ`, logo **`ξ = X/a`** com `X ≡ ḃ/ℋ` — o
mesmo objeto deles, **mesmo sinal e mesmo zero**. O critério do R-10c
Parte A ("ξ cruza zero ⟹ o lapso do setor f se anula ⟹ ponto singular
⟹ história contínua excluída") é, ponto por ponto, o **quique de `b`**
que a fonte primária trata explicitamente (§II e §VI, com nota de
rodapé) e defende como **físico**, por três razões declaradas:

1. f não acopla à matéria e não tem interpretação geométrica;
2. nenhuma variável de fundo ou perturbada apresenta singularidade;
3. `√(−det f)·R̄(f)` permanece finita e não-nula — as equações de
   movimento existem em todo instante (a escolha de sinal da raiz é
   feita para deixar a ação diferenciável na travessia).

**Por que é o risco mais caro.** O IBB é o **único modelo estável em
todos os tempos** daquele paper — e, desde 2026-08-13, esta frase só
pode ser escrita **com o canal declarado**: 1407.4331 é **setor
escalar** (ver §1.2, linha do `m_T²/H²`), logo "estável" ali significa
**estável no canal de gradiente**. Ver o "Desfecho parcial" abaixo,
fato 5. Com essa qualificação: fundo viável, sem constante
cosmológica explícita para g, com r decrescendo de ∞ a um valor
finito, e estabilidade garantida por `r_c > 1` em toda a faixa
`0 < β₄ < 2β₁`. Ou seja: o repositório fechou, com um argumento que a
fonte primária rejeita nominalmente, exatamente a porta que a fonte
primária declara ser a saída.

*Como isso terminou (2026-08-13):* a porta **está** fechada, mas por
uma tranca que não é a nossa e que a **outra** fonte já havia instalado
— e o "único modelo estável em todos os tempos" de 1407.4331 continua
verdadeiro **no canal em que foi dito** (gradiente), sem que isso o
salve. É a separação de canais levada até o fim. E a janela
`0 < β₄ < 2β₁` desta frase é, ela própria, o caso μ = 1 de
`0 < β₄/β₁ < 2μ^{3/2}` (§1.1b).

**Os três itens que o risco abriu — e o estado de cada um hoje.**

- **(a) — EXECUTADO em 2026-08-13.** *Abrir 1503.07436 na fonte.* Ver
  o bloco "**Desfecho parcial**" abaixo. Ele resolveu a pendência, mas
  **não** do modo como ela estava escrita — e a caracterização antiga
  ("duas linhas contraditórias") era **errada** e está corrigida ali.
  Depois disso, o **R-13a** reabriu a mesma fonte por **duas rotas
  independentes** e a leitura passou de `V-1503` a `V-13a`.
- **(b) O reexame do fundo, com o escopo certo — EXECUTADO (R-13b).**
  O IBB viável exige **β₄ ≠ 0**, enquanto a nossa célula mínima tem
  β₄ = 0. O alvo era o **ramo infinito da F1 com β₄ ligado**, e é
  exatamente ele que o R-13b mediu: β₂ = β₃ = β₀ = 0, β₁ = 1,
  `0 < β₄/β₁ < 2μ^{3/2}`, 12 valores de β₄ × 9 de μ = **108 células**,
  com a armadilha da seleção de raiz nomeada e desarmada (seleção por
  **continuação**, semeada pela assíntota analítica do passado
  profundo — `resolve_r()` sem referência devolve a **menor** raiz, que
  é a do ramo **finito**). A "segunda solução tardia viável" que o
  R-10c Parte A registrava como inexplorada **está explorada**.
- **(c) O ônus argumentativo — DISSOLVIDO, não pago.** A pergunta era:
  se a exclusão for mantida **pelo nosso critério ξ**, ela precisa de
  um argumento novo que responda aos três deles, um a um. **A exclusão
  não é mais pelo nosso critério ξ.** O ônus some porque a tese que o
  gerava foi abandonada — e os três argumentos da fonte sobre o quique
  **continuam de pé, sem contestação nossa**. Registro adicional: o
  R-13b **confirma** a descrição deles do quique (cruzamento único,
  108/108, locus fechado) e mede `m_T² > 0` em 100% da história em
  108/108 células — **nem sequer na travessia de `ξ = 0`** aparece
  patologia tensorial. O nosso argumento antigo não só caiu: o objeto
  que ele apontava como singular foi medido e está são.

#### Desfecho parcial — 2026-08-13: 1503.07436 aberto na fonte

> **[REGISTRO HISTÓRICO — preservado, e superado no veredito.]** Este
> bloco é o estado do risco entre a leitura do autor e o arco R-13. Os
> seus **fatos** continuam válidos e foram todos reconfirmados pelo
> R-13a por duas rotas. O que ele **não** tem é o desfecho: onde ele
> diz "REABERTO", "teste de tradução pendente" e "lacunas declaradas",
> leia o "**Desfecho final**" logo abaixo. Nada aqui foi apagado
> porque a proveniência é o produto.

**Disciplina de atribuição, antes de tudo.** O que segue é
**VERIFICADO-NA-FONTE — leitura do autor** de arXiv:1503.07436
(nível `V-1503` do §1). **Não** é derivação deste repositório, **não**
é medida interna, e **não** é nível 1, 2a nem 2b do projeto: continua
sendo **literatura = nível 3**, agora com acesso direto ao texto. E há
uma segunda fronteira, tão importante quanto: **a tradução dos
enunciados da fonte para as convenções deste repositório NÃO foi
feita.** Enquanto ela não for, nada abaixo pode ser usado como
resultado do projeto.

**O que a fonte diz (cinco fatos, e só estes cinco):**

1. Para cosmologias **em expansão**, a razão `r = b/a` deve
   **crescer** ao longo da evolução para satisfazer a condição
   associada ao **Higuchi** e manter sãos os setores **helicidade-0** e
   **helicidade-2**.
2. O **infinite branch** é definido ali precisamente como aquele em
   que `r` parte de valores infinitamente grandes no passado e
   **decresce** com o tempo.
3. Logo há **colisão direta**: saúde/Higuchi em universo expansivo
   ⟹ **r′ > 0**; infinite branch ⟹ **r′ < 0**.
4. O mesmo paper registra que o IBB havia sido identificado antes como
   **livre das instabilidades escalares lineares**, mas ressalva que
   trabalhos anteriores encontraram **violação do Higuchi no limite
   inicial** e que foi reportado um **ghost no setor helicidade-2 em
   tempos iniciais**.
5. **Consequência conceitual — três perguntas distintas e não
   intercambiáveis:** estabilidade de **gradiente** ≠ saúde de
   **Higuchi/helicidade-0** ≠ saúde do **setor tensorial**. É
   perfeitamente possível o IBB curar o gradiente que matou o ramo
   finito e **ainda assim** falhar por outro canal.

**A CORREÇÃO — o corpus registrava isto errado.** Até hoje este
documento (e o cap. 07, o cap. 09, o R-10c e o R-10 consolidado)
afirmava que as **duas linhas sobre 1503.07436 são contraditórias
entre si**. **Não são.** Elas são o **mesmo enunciado aplicado a ramos
diferentes**:

| Ramo | Sinal de `r′` | Higuchi |
|---|---|---|
| finito | r′ ≥ 0 | passa |
| infinito | r′ < 0 | não passa |

Um único critério, dois ramos, dois desfechos. **São consistentes.**

**Onde está a tensão de verdade: entre as duas fontes.** 1407.4331
declara o IBB **estável** — mas isso é o **canal de gradiente**
(escalar linear). 1503.07436 diz que `r′ < 0` colide com a condição de
Higuchi. As duas coisas podem valer ao mesmo tempo, e a dissolução é
exatamente a **separação de canais** do fato 5: *"estável" sem
qualificação de canal não é um dado — é a mesma armadilha do "0.28"
(§6), agora no eixo do canal em vez do eixo do modelo.*

**O estado do ramo infinito: CONTINUA REABERTO.** *(Estado em
2026-08-13, ANTES do R-13a/b. Superado pelo "Desfecho final".)* Isto
não é cautela retórica, é o registro exato:

- O R-12i **derrubou o argumento específico do repositório**
  (`ξ = 0 ⟹ singularidade física`), e ele **continua derrubado**. Nada
  aqui o ressuscita.
- 1503.07436 oferece um argumento **independente e diferente**
  (`r′ < 0 ⟹ problema de Higuchi/ghost`) — um **candidato**, não uma
  exclusão do corpus, porque **ainda não foi traduzido para as
  convenções do repositório**.
- O veredito só pode ser elevado de **`IBB REABERTO`** para algo como
  **`IBB EXCLUÍDO NA F1 PELO HIGUCHI, NÃO PELO ZERO DO LAPSO`**
  **depois** do teste de tradução abaixo. Até lá, escrever "o IBB está
  excluído" é importar um resultado de outro sistema de convenções —
  precisamente o erro que este arquivo existe para impedir.

**O teste de tradução (próximo item da fila — especificação exata):**
*(**EXECUTADO**: R-13a entregou o critério traduzido, R-13b mediu. Ver
"Desfecho final".)*

> Pegar uma célula IBB genuína — **β₂ = β₃ = 0, β₁ > 0,
> 0 < β₄ < 2β₁** —, seguir o ramo infinito e medir, **na convenção do
> projeto**: `r′(N)`, `m_T²/H²`, e o funcional/inequação de Higuchi
> usado em 1503.07436. Se a tradução fechar e der `r′ < 0` junto com
> violação do Higuchi na era inicial, o veredito pode ser elevado.

**Por que esta ordem importa — e não é burocracia.** Ela **preserva o
R-12i**. O corpus admitiu que a **primeira** razão para excluir o ramo
infinito estava errada, e **só depois** foi verificar se existia uma
**segunda** razão válida. Inverter a ordem — deixar o argumento novo
apagar a retratação — seria transformar uma correção em conveniência:
a exclusão sobreviveria por ter encontrado uma justificativa nova,
não por a antiga ter resistido. O erro fica no registro; o argumento
novo entra por mérito próprio, e só depois de traduzido.

**Lacunas declaradas (o que NÃO se sabe da fonte).** *(As três foram
**FECHADAS** pelo R-13a — ver "Desfecho final".)* A leitura cobre os
cinco fatos acima e nada além deles. Em particular, **não** estão
registrados aqui: a forma explícita do funcional/inequação de Higuchi
usada em 1503.07436 nas variáveis dela; se o paper emite veredito
final próprio sobre o IBB; e como os enunciados dele se mapeiam nas
nossas variáveis (`ξ`, `r`, `N`, normalização β, `μ`, `M_ef²`). Esta
terceira lacuna **é** o teste de tradução.

**O enunciado honesto de então** *(2026-08-13, antes do R-13a/b —
**superado**; o enunciado vigente está no fim do "Desfecho final"):*
*"o repositório excluiu o ramo infinito por um critério (`ξ → 0`) que
a fonte primária examina e rejeita — e isso continua valendo. Existe
um argumento independente na literatura (`r′ < 0` vs. Higuchi,
1503.07436, verificado na fonte pelo autor) que pode vir a excluí-lo
por outro canal, mas ele ainda não foi traduzido para as nossas
convenções. O ramo infinito está REABERTO."*

#### Desfecho final — 2026-08-13: o arco R-13a → R-13b fecha o R-b

**TABELA DE PROVENIÊNCIA** — é ela que fecha o risco, e é por ela que
este item deve ser lido em qualquer revisão futura:

| Saída | Veredito vigente | Razão |
|---|---|---|
| Infinite branch / IBB | **EXCLUÍDO** | ghost de Higuchi, `r′ < 0` em toda a história |
| argumento antigo `ξ = 0` | **REVOGADO** | zero do lapso / quique não é por si só singularidade |
| gradiente no IBB | **SAUDÁVEL** segundo a fonte | canal independente; não salva o Higuchi |

**As três lacunas do "Desfecho parcial" — FECHADAS, e por qual peça.**

| Lacuna de então | Fechada por | Conteúdo |
|---|---|---|
| a forma explícita do funcional de Higuchi nas variáveis da fonte | **R-13a §1.1** (`V-13a`) | eq. (14), escrita **só em `r` e nos `β_n`**, **sem massa nenhuma**; equivalentes (15), (16) `ρ_{,r} ≤ 0`, (18) `r′ ≥ 0`, (19) `B₂ ≥ 0` |
| se o paper emite veredito próprio sobre o IBB | **R-13a §1.5** (`V-13a`) | **SIM, e duas vezes** — §III A e §VI: todos os ramos infinitos sofrem do fantasma de Higuchi **em todos os tempos**. A fonte **promove** o "early times" de Lagos–Ferreira a "all times" |
| como os enunciados se mapeiam nas nossas variáveis | **R-13a §2** (álgebra) + **R-13b §8.2** (CAS, rota independente) | mapa `r_K = √μ r`, `β_n^K = Aμ^{−n/2}β_n`, sobredeterminado pelas duas Friedmann; `ξ_K = √μ ξ` ⟹ **mesmo sinal, mesmo zero**; `Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0` |

**A evidência, peça por peça, com o nível de cada uma.**

| Peça | Conteúdo | Nível |
|---|---|---|
| Critério na fonte | eq. (14) e a cadeia (14)⟺(15)⟺(16)⟺(18), com as três hipóteses declaradas (`ρ > 0`, `1 + w_tot > 0`, `r ≥ 0`) | **V-13a** — literatura, texto integral por **duas rotas** |
| Tradução | mapa de convenções + as duas caixas + `Higuchi ⟺ ξ ≥ r` | álgebra do **R-13a**, **re-verificada por CAS em rota independente** (R-13b §8.2: **três resíduos simbólicos zero**, `β_n` e `μ` **gerais**, poeira) |
| `r′ < 0` no IBB | **100% da história em 108/108 células**; max r′ = **−6.05e−5** na varredura inteira; forma fechada `dr/dN = −3ρ̃/𝒲′(r)` (`np.gradient` **proibido** por trava no script; cross-check por estêncil de 8ª ordem, 8/8 pontos, margem de cinco ordens) | **M-13b** (2a + 2b) |
| Higuchi violado | **0 de 64 800 pontos**; **0/108 células** em qualquer época | **M-13b** (2b) |
| As duas formas equivalentes concordam | **64 800/64 800** | **M-13b** (2b) |
| O teste tem **poder** | controle positivo do ramo finito: `r′ ≥ 0` **400/400**, Higuchi-da-fonte **400/400**, concordância **400/400**. **Aprova o finito e reprova o infinito** — não é concordância trivial | **M-13b** (2b) |
| Forma fechada do supremo | `m_T²/H²\|_{r_c} = 1 + 1/(μr_c²)` e `μr_c² > 1` em toda a janela ⟹ **`1 < sup < 2` estrito, para todo μ** | **M-13b** (2a) |
| `μ` | **pura reescala** no IBB genuíno — o eixo nunca antes varrido **fecha** o enunciado em vez de abri-lo | **M-13b** (2a + 2b) |

**O ponto lógico, declarado e não escondido.** O gate do R-13b
**declara-se cego ao gradiente** (§1 dele, regra 7): ele mede
Higuchi/helicidade-0 e o tensorial, e nada diz sobre `c_s²` no ramo
infinito. **Essa declaração fica — e não bloqueia o veredito.** Um
ghost físico basta para excluir, e a assimetria de peso é **da
fonte**, não nossa: fantasma ⟹ Hamiltoniano ilimitado por baixo ⟹
decaimento do vácuo, e nem o argumento de teoria efetiva salva
(1503.07436 §III D, citando Woodard 2007 e Sbisà 1406.4550); modos
escalares instáveis *"will not necessarily rule out the theory"*
(§VI). Medir `c_s²` no IBB seria **validação adicional, não
requisito**; continua na fila (§5) com esse estatuto e não com o de
pendência bloqueante.

**O que este desfecho NÃO faz — as fronteiras que continuam de pé.**

- **Não** reabilita o argumento `ξ = 0`. Ele continua revogado, e essa
  ordem é deliberada (ver "Por que esta ordem importa" acima).
- **Não** contesta os três argumentos da fonte sobre o quique. Eles
  continuam de pé, sem contestação nossa — e o R-13b, ao medir
  `m_T² > 0` em 100% da história em 108/108 células, **inclusive na
  travessia**, é evidência *a favor* deles.
- **Não** verifica o **mapa de convenções** do R-13a §2.1 por CAS: ele
  é **entrada** do R-13b, não saída. O que ficou verificado é a cadeia
  **interna**, **dado** o mapa. Ver §6, **P-6**.
- **Não** vale com `β_n(φ₋)` modulados: o R-13a §2.2 (hipótese 2) avisa
  que a cadeia (14)→(16)→(18) usa `ρ_{,r}` a β fixo e **não sobrevive
  intacta**. Todo este desfecho vale para **β_n constantes**.
- **Não** cobre β₂ ≠ 0 / β₃ ≠ 0 sobre o ramo infinito, nem radiação,
  nem acoplamento duplo da matéria. Fronteiras no R-13b §0.
- **Não** abriu **Fasiello–Tolley 1308.1647**, que é a fonte primária
  *real* do bound e que este arquivo cita (§4) sem tê-la lido.

**O enunciado honesto de hoje:** *"o repositório excluiu o ramo
infinito por um critério (`ξ → 0`) que a fonte primária examina e
rejeita; esse argumento caiu e **continua caído**. A exclusão vigente é
**outra**: o critério de Higuchi de 1503.07436 — verificado na fonte
por duas rotas, traduzido para as nossas convenções e re-verificado por
CAS em rota independente — é violado em **toda** a história do ramo
infinito, em 108/108 células IBB genuínas, com o supremo de `m_T²/H²`
preso em `1 < sup < 2` por forma fechada, para todo μ. O ramo infinito
está **EXCLUÍDO PELO GHOST DE HIGUCHI**, com o gate declaradamente cego
ao gradiente — e a própria fonte declara o gradiente do IBB **saudável**
e **não fatal**, o que não o salva."*

---

## 3. Ranking de novidade defensável (reescrito)

O ranking da v1 foi construído sobre resultados que caíram: os seus
lugares nº 1 e nº 3 dependiam de D1/D2 e do taquião tardio, e o nº 3
citava um no-go de classe que ou foi retirado (o modulado) ou é de
2014 (o de gradiente). Este é o ranking do que sobra **de fato**.

**Nota sobre a reordenação de 2026-08-13 (arco R-13).** A v1 desta
seção punha o `m_T²/H² → 12` em nº 1, seguindo a tabela de
sobreviventes do R-12i, com o argumento de que o confronto não o
tocara. **O arco R-13 tocou** — não no objeto, na **leitura**. O `12`
continua exato e continua sendo o objeto tensorial do projeto; o que
caiu é a frase "razão universal que demonstra enorme margem de
Higuchi", porque o **funcional FLRW de Higuchi da fonte dá `3`** no
mesmo limite (medido: 3.000002), satisfazendo o bound `2` com margem de
**1.5×, não 6×** — e porque o `m_T² ≥ 2H²` com `ξ` dinâmico **não é
nenhum dos dois critérios da fonte**. Um item cujo *interesse* depende
de uma leitura que caiu não pode ficar acima de um item que não se
moveu. Daí a troca dos dois primeiros lugares. **Ela não é promoção do
`5/2`:** o `5/2` não ficou melhor, o item acima dele ficou pior — e o
`5/2` sobe carregando intacto o seu risco de morte súbita.

1. **`m_ef²/H² → 5/2`** (massa efetiva do escalar métrico, ordem k⁰).
   *Por quê aqui:* é o único número do setor escalar que sobreviveu ao
   confronto com a fonte que cobre **exatamente** esse setor — eles
   descartam explicitamente as soluções independentes de k como
   subdominantes e **nunca dão o termo de massa**. E é o único dos dois
   primeiros que o arco R-13 **não moveu em nada**, nem no objeto nem
   na leitura. *Risco, declarado e inalterado:* é exatamente a ordem k⁰
   onde a perturbação de matéria ausente da nossa L2 entraria;
   `Δ = ½rr′` zera nos dois extremos justamente porque é ordem k², e
   nada garante que o termo k⁰ tenha a mesma sorte. **Não reivindicar
   antes do teste δρ_m** (§5, item 1). Continua sendo o item de maior
   valor esperado **e maior variância** do arquivo — subir de posição
   não reduz a variância.
2. **`m_T²/H² → 3(4+3w)`** (setor tensorial; 12 em matéria, **15 em
   radiação**) — **REQUALIFICADO, e o que muda é a venda.** *O que
   fica:* o objeto é exato, é do setor tensorial (que não passa pela
   redução corrigida pelos Erratums 02/03), nenhuma das duas fontes
   primárias o toca, e o resultado negativo do R-13a §1.7 — **a fonte
   do Higuchi não escreve massa de gráviton em lugar nenhum**, firme
   por duas rotas — **reforça** a afirmação de ausência nesse ponto.
   *O que sai:* a leitura "margem enorme de Higuchi". O funcional de
   Higuchi da fonte dá **3** (margem 1.5×), e o `m_T² ≥ 2H²` com `ξ`
   dinâmico não corresponde ao critério de helicidade-0 (`ξ ≥ r`) nem
   ao de helicidade-2 (sinal do lapso, `ξ > 0`). *Riscos herdados, os
   três de pé:* (i) afirmação de **ausência** em nível-de-busca; (ii) a
   generalização por época vem de **dois especialistas externos, não
   verificada internamente**; (iii) a discrepância em w = −1 (6 vs 3)
   está **aberta**. **Reivindicar como razão de massa tensorial; nunca
   como margem de Higuchi.**
3. **As duas reproduções independentes** — item único, porque as duas
   fazem o **mesmo trabalho** num paper: dar ao referee razão para
   confiar na maquinaria. Nenhuma das duas é reivindicação de física.
   - **(a) Os dois extremos exatos do `c_s²`** (`−1` e `+1`, mais o
     coeficiente linear) por maquinaria totalmente distinta —
     Schur/Faddeev–Jackiw contra a redução 10→2 de 1407.4331.
     Concordância **exata**, simbólica.
   - **(b) A complementaridade dos dois ramos** (R-13a → R-13b),
     reproduzida com maquinaria própria e **`μ` generalizado**, com
     **três formas fechadas nossas**: a janela de existência
     `0 < β₄/β₁ < 2μ^{3/2}`, o locus de `ξ = 0`
     (`β₄r³ − 6μβ₁r² + 4β₁ = 0`), e `m_T²/H²|_{r_c} = 1 + 1/(μr_c²)`
     com o `1 < sup < 2` estrito. Some-se a validação cruzada de que a
     caixa de `m_T²` da `derivations/02`, derivada por rota
     independente, **reproduz exatamente** o bound FLRW no limite
     `ξ = r`.

   *Avaliação honesta de (b) — nem inflar, nem enterrar.* **Não é
   descoberta:** a complementaridade está nas duas fontes (1407.4331
   para o gradiente, 1503.07436 §III A/§VI para o Higuchi), e o
   veredito "todos os ramos infinitos, em todos os tempos" é
   **publicado**. **Não é trivial:** foi medido em 108 células na
   convenção do projeto, com controle positivo que dá poder ao teste
   (aprova o finito 400/400, reprova o infinito 0/64 800), com a
   armadilha de seleção de raiz nomeada e desarmada, e com a tradução
   re-verificada por CAS em rota independente. **E o `μ` generalizado
   rende menos do que parece:** a varredura no eixo nunca antes varrido
   mostra que `μ` é **pura reescala** neste bloco — ela **fecha** o
   enunciado em vez de abri-lo, o que é bom para a solidez e ruim para
   a novidade. *Por quê aqui e não mais acima:* o valor é **de método,
   não de física**. *Por quê não mais abaixo:* junto com (a), este é o
   material mais bem verificado do arquivo. **Vale um parágrafo e três
   fórmulas no apêndice, não uma reivindicação.**
4. **O pacote da subclasse mínima**: β₁(φ) único + não-fatoração
   derivada + fundo transiente fora dos ramos com pouso. *Por quê
   aqui:* é fundo e estrutura de vínculos — não passa pela redução
   numérica, logo intocado pelos eventos (1) e (2) do §0 —, e a lacuna
   hamiltoniana do chameleon bigravity é um gancho real. *Risco:*
   nível-de-busca; minisuperespaço; e a instabilidade radiativa da
   escolha "β₁ único" (§4.2 da síntese) ataca a própria premissa. O
   arco R-13 também não o tocou.
5. **Limiar de back-reaction** — como aplicação do mecanismo camaleão
   (citar 1702.04490 **verbatim**), com o limiar e a competição com a
   bifurcação como parte nossa. Intocado pelos quatro eventos do §0.
6. **Síntese conceitual TDCP** — defensável só com diferenciação
   explícita do análogo 2-BEC e do Higgs gravitacional. Novidade-por-
   síntese é a mais frágil das categorias; sem mudança de estatuto.

**Fora do ranking (rebaixados ou suspensos):**

- **O no-go de classe por gradiente** — sai do ranking de novidade.
  Vai para a introdução como *reprodução independente de um resultado
  de 2014*, com o `−1` explicitado e a forma fechada exibida. Ainda
  assim sujeito a R-a quanto ao **nome**.
- **A exclusão do ramo infinito pelo Higuchi** — **fora do ranking de
  novidade, e por simetria com a linha acima.** 1503.07436 §III A e
  §VI já enunciam que *todos* os ramos infinitos sofrem do fantasma de
  Higuchi **em todos os tempos**; o nosso 108/108 é **confirmação
  numérica de um veredito publicado**, na nossa convenção. O que o
  arco rende ao ranking é o item 3(b) — a maquinaria e as três formas
  fechadas —, **não** o veredito. *Mas ele rende algo maior que uma
  linha de ranking:* é o que autoriza o corpus a **usar** a exclusão
  como resultado próprio em vez de importá-la, e é o que fecha o R-b.
- **O `12` como "margem de Higuchi"** — **retirado como leitura.** O
  número fica (item 2); a interpretação não. Onde o corpus escrever
  "enorme margem de Higuchi", o objeto correto é o funcional da fonte,
  que dá **3** contra o bound **2**. Este é o tipo de frase que um
  referee que conheça 1503.07436 mata em uma linha.
- **A forma fechada de `c_s²(r)`** — sai. A família é a mesma, a eq.
  (73) é deles, e a nossa difere por um termo de matéria que
  provavelmente é **omissão nossa**. Se o teste δρ_m confirmar a
  inferência, o objeto correto passa a ser a deles.
- **A medida Stückelberg** (0.995 / 0.998) — **suspensa**, não
  rebaixada: os modos sobre os quais ela foi tomada caíram, e ninguém
  a refez. Ver §6, P-2.
- **O taquião tardio persistente** — não existe (§1.3).

---

## 4. Bibliografia consolidada (núcleo que o paper cita)

**Fundação HR/bigravity:** Hassan–Rosen 1106.3344 (PRL 108, 041101),
1109.3515 (JHEP 02 (2012) 126), 1111.2070 (secundária); dRGT 1011.1232.
**Ramos e cosmologia:** Volkov 1110.6153; Comelli–Crisostomi–Nesti–Pilo
1111.1983; von Strauss et al. 1111.1655; Comelli–Crisostomi–Pilo
1202.1986 e 1403.5679; Könnig–Amendola 1402.1988; **Könnig, Akrami,
Amendola, Motta & Solomon, PRD 90, 124014 (2014) = 1407.4331** (ver
§4b); **Könnig, *Higuchi ghosts and gradient instabilities in bimetric
gravity*, PRD 91, 104019 (2015) = 1503.07436** (ver §4c);
Lagos–Ferreira 1410.0207; Akrami et al. 1503.07521; De Felice et al.
1404.0008; Cusin et al. 1412.5979; Aoki–Maeda–Namba 1506.04543;
Mörtsell–Enander 1506.04977; Sakakihara et al. 1211.5976; Brizuela et
al. 2507.11526 (estado 2025).
**Higuchi:** Fasiello–Tolley 1206.3852 e **1308.1647** (a fonte
primária *real* do bound de FLRW — **NÃO ABERTA**, ver §4c).

**Entradas acrescentadas pelo R-13a — todas em NÍVEL DE CITAÇÃO.**
Sabemos o que 1503.07436 diz que elas dizem, e temos as referências
bibliográficas completas; **nenhuma foi aberta** (R-13a §5). Tratar
como `B` até que alguém as leia: Yamashita–Tanaka, JCAP 1406, 004
(2014) [1401.4336] (a equivalência `ρ_{,r} ≤ 0`); Könnig–Patil–Amendola,
JCAP 1403, 029 (2014) [1312.3208] (`r′ < 0` em todos os ramos
infinitos); Enander, Akrami, Mörtsell, Renneby & Solomon [1501.02140]
(ajuste observacional do IBB); Sbisà, Eur. J. Phys. 36, 015009 (2015)
[1406.4550] (por que o argumento de teoria efetiva não salva um
fantasma); Woodard, Lect. Notes Phys. 720, 403 (2007)
[astro-ph/0601672] (decaimento do vácuo; e a ressalva de que o
fantasma de Higuchi pode só aparecer em ordens superiores).
**Massa variável / classe-irmã:** Huang–Piao–Zhou 1206.5678;
Huang–Zhang–Zhou 1306.4740; Hinterbichler–Stokes–Trodden 1301.4993;
quasidilaton 1206.4253, 1304.0723, 1304.0449, 1306.5502, 1309.0956,
**1309.2146 (versão publicada!)**; **chameleon bigravity 1702.04490 e
1711.04655 (obrigatórias)**; GMG 1410.0960, 1912.08560; Matas
1506.00666; 2507.21542 (minimal MVMG, estado 2025).
**Stückelberg/EFT:** AGS hep-th/0210184; Hinterbichler 1105.3735;
de Rham 1401.4173; Schmidt-May–von Strauss 1512.00021;
Noumi–Yamaguchi–Yoshida 1602.03132.
**W–W e compostos:** Weinberg–Witten PLB 96 (1980) 59; Porrati
0804.4672; PDG Quark Model; Isham–Salam–Strathdee PRD 3 (1971) 867;
Kiritsis JHEP 11 (2006) 049; Aharony–Clark–Karch (2006); FQH chiral
graviton Nature 628 (2024); Golkar–Nguyen–Son 1602.08499;
Alberte–de Rham–Jaitly–Tolley 1910.11799; Boulware–Deser PRD 6 (1972);
"infinity of states" PLB (1989); 1812.01012.
**Análogos/conceito:** Visser–Weinfurtner gr-qc/0506029;
Liberati–Visser–Weinfurtner gr-qc/0510125; de Rham–Matas–Tolley
1308.4136 (deconstrução) e 1311.6485 (no-go cinético); 't Hooft
0708.3184; Chamseddine–Mukhanov 1002.3877; Hossenfelder 0807.2838.
**BECs:** Abad–Recati 1301.6864; Zibold et al. PRL 105, 204101;
Takeuchi et al. PRL 105, 205301; Ishino et al. 1106.0884; Leggett RMP
73, 307.

### 4b. Adendo do R-12i — como citar 1407.4331 sem herdar erro

A referência deixou de ser um item de lista e passou a ser a fonte
primária do capítulo do setor escalar. Quatro exigências de citação,
todas verificadas:

1. **Referência completa:** Könnig, Akrami, Amendola, Motta & Solomon,
   *Stable and unstable cosmological models in bimetric massive
   gravity*, **PRD 90, 124014 (2014)**, [arXiv:1407.4331].
2. **Numeração de equações:** a numeração usada no corpus é a da
   **versão publicada na PRD**. O arXiv/ar5iv tem as mesmas equações
   deslocadas de **+3** (a nossa (69) é a (72) de lá). Qualquer
   citação por número tem de dizer qual das duas está usando.
3. **Seções a citar nominalmente:** §V (instabilidades; o no-go de
   classe do ramo finito; eqs. 68–76), §II e §VI (IBB e o quique de
   `b`), §VIII (a leitura fraca da instabilidade — base do R-a).
4. **Erratum na fonte, verificado e sem consequência:** a eq. (69)
   impressa tem `(1+3r²)` **sem quadrado** dentro da raiz, incompatível
   com a identidade (76) que os próprios autores declaram cobri-la. As
   duas rotas de leitura (PDF publicado e ar5iv) concordam no que está
   impresso — é typo da fonte, não da nossa extração. O fator é
   positivo-definido: **não move a raiz**, e o 0.28 permanece válido.
   **Quem citar a (69) literalmente herda o typo.**

*Fora de escopo declarado da fonte, para não ser citada além do que
cobre:* a identidade (76) **não** vale para os modelos β₂ e β₃, então a
comparação a células com β₂ ≠ 0 não pode usar essa rota.

### 4c. Adendo do R-13a — como citar 1503.07436 sem herdar erro

A referência passou de item de lista a fonte primária do critério de
Higuchi. Cinco exigências, todas verificadas por duas rotas:

1. **Referência completa:** Frank Könnig, *Higuchi ghosts and gradient
   instabilities in bimetric gravity*, **PRD 91, 104019 (2015)**,
   [arXiv:1503.07436] (NORDITA-2015-44).
2. **Numeração:** ao contrário de 1407.4331, aqui **não há
   deslocamento** — a versão do arXiv é a publicada e as duas rotas dão
   a mesma numeração. Seções do PDF publicado: `III. HIGUCHI GHOSTS` /
   `A. Higuchi bound` / `B. Phantom dark energy` / `C. Tensor ghosts` /
   `D. Consequences…`; o ar5iv renderiza como III.1–III.4.
3. **Seções a citar nominalmente:** §III A (a condição, eqs. 14–19),
   §III C (o critério tensorial = **sinal do lapso de f**, via Cusin et
   al. 1412.5979), §III D (por que fantasma é fatal e gradiente não),
   §IV A (o gradiente do IBB, **mantido**, não retratado), §V (o
   teorema de classificação) e §VI (conclusões).
4. **A condição de Higuchi NÃO é da fonte — ela credita.** A eq. (14) é
   a versão *"nas notações dele"* de **Fasiello–Tolley 1308.1647**; as
   equivalências vêm de **Yamashita–Tanaka 1401.4336** e **De Felice et
   al. 1404.0008**. **Nota de rodapé 3, e é um custo real:**
   Fasiello–Tolley usam um fator global `1/2` na frente do termo de
   potencial, *"which can be compensated for by a redefinition of the
   β-couplings"* — **quem citar 1308.1647 diretamente herda esse fator
   2 nos β.** Este arquivo cita 1308.1647 desde a v1 **sem tê-la
   aberto** (§5, fila).
5. **Duas imprecisões da fonte, registradas para não serem herdadas:**
   (i) §III A diz que `B₂` *"is simply the derivative of ρ_mg"* — é a
   derivada **a menos de um fator 3**
   (`d/dr(β₀+3β₁r+3β₂r²+β₃r³) = 3B₂`); sem consequência ali, porque só
   o sinal é usado, mas quem citar a frase herda o erro. (ii) O ansatz
   é `Ξ_i ∝ e^{ωt}`, **exponencial real** — ver a armadilha de sinal do
   §6.

*Sub-produto verificado, e vale citar:* a eq. (40) desta fonte
**confirma o erratum** que o R-12i registrou na eq. (69) de 1407.4331
(o `(1+3r²)` sem quadrado). É o mesmo autor, ano seguinte, mesmo modelo
β₁-puro, e imprime o denominador `(3r²+1)²` **ao quadrado** nas duas
rotas. **Terceira rota independente; o erratum está fechado.** Bônus da
(40): a dependência em `w` que 1407.4331 não exibia — o limiar geral da
instabilidade primordial é **`w = −1/2`**, e o `c_s²(r→0) = −1` do R-11
é o caso `w = 0`.

---

## 5. Efeito na fila

1. **δρ_m na L2 e re-derivação do R-12b.** É o item caro e o mais
   valioso: decide se o `m_ef²/H² → 5/2` — hoje o nº 2 do ranking — é
   resultado ou artefato de truncagem. Predição falsificável e nítida
   registrada no R-12i §4: **Δ deve zerar identicamente**, isto é, o
   novo `c_s²` deve valer exatamente `−r''/(3r')`. Não é flip de
   parâmetro: `rho_s` na `tdcp_pert_lib.py` é densidade de **fundo** e
   não há campo δρ_m em `NOMES`; exige acrescentar o grau de liberdade
   à maquinaria.
2. ~~**Abrir 1503.07436 na fonte**~~ → ~~**TESTE DE TRADUÇÃO**~~ —
   **OS DOIS FEITOS em 2026-08-13.** A leitura do autor fechou o
   primeiro (R-b, "Desfecho parcial"); o **R-13a** reabriu a fonte por
   duas rotas independentes e **entregou o critério traduzido**
   (`Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0`, com a forma "massa" fechada), e o
   **R-13b** o **mediu** em 108 células e **re-verificou a tradução por
   CAS em rota independente**. O veredito foi elevado, e a redação
   final é a do §2b: **`IBB EXCLUÍDO PELO GHOST DE HIGUCHI, NÃO PELO
   ZERO DO LAPSO`**. O que entra no lugar são os itens 4–8 abaixo.
3. ~~**Reabrir o ramo infinito com β₄ ≠ 0**~~ (R-b, itens (b) e (c)) —
   **FEITO (R-13b).** O alvo era o ramo infinito da F1 com β₄ ligado, e
   foi ele que rodou: 108 células, `0 < β₄/β₁ < 2μ^{3/2}`, com o eixo
   `μ` varrido pela primeira vez. O item (c) — o ônus de responder aos
   três argumentos de §II/§VI de 1407.4331 — **não foi pago, foi
   dissolvido**: a exclusão deixou de depender do nosso critério `ξ`.
   Ver §2b, "Desfecho final".
4. **`c_s²` no ramo infinito — o canal cego.** O gate do R-13b declara
   (regra 7) não medir gradiente; o no-go do R-11 (`c_s² = −1`) foi
   medido no ramo **finito** e nada o transporta para o infinito.
   **Estatuto explícito: validação adicional, NÃO requisito.** O
   veredito de exclusão já está fechado por um ghost, e a própria fonte
   declara o gradiente **não fatal** e o gradiente do IBB **saudável**
   (§IV A de 1503.07436). Medir `c_s²` lá com a maquinaria limpa do
   R-12 fecharia o arco de forma redonda — e daria a **terceira** rota
   independente sobre a complementaridade — mas nada bloqueia enquanto
   não rodar.
5. **`w_mg ≤ −1` como observável** — o achado de passagem do R-13a
   §4.3, e o item de melhor razão custo/benefício desta fila. Na nossa
   convenção:
   > `w_mg = −1 − (ℬ(r)/V_g(r))·(dr/dN)`, com
   > `ℬ(r) = β₁+2β₂r+β₃r²` — **toda solução sem fantasma de Higuchi
   > tem energia escura phantom** (`ℬ ≥ 0` e `r′ ≥ 0` ⟹ `w_mg ≤ −1`).
   > *Hipótese declarada: `β_n` constantes.*

   É **energia escura fantasma já na nossa convenção**, sem tradução
   pendente, e a fonte a trata como **assinatura observacional**, não
   como patologia (§III B: a EOS depende fortemente do tempo e tende a
   −1 no futuro assintótico; um phantom em bigravidade *"is not as
   frightening as in ΛCDM"*). **Conecta diretamente com a alavanca A2
   do parecer de cosmologia** — `w_eff(z)` do ramo finito vs. DESI DR2
   BAO + SNe (`docs/pareceres_especialistas/parecer_cosmologia.md`,
   item **A2**, marcado lá como "prioridade alta, ~meia sessão"; é
   também o **nº 1** da lista de prioridades de
   `docs/pareceres_especialistas/00_sintese_cruzada.md`, com a nota de
   que o fundo já está pronto). O R-13b **não** mediu `w_mg`; o cap. 09
   não tem esse observável.
6. **Verificar por CAS o mapa de convenções do R-13a §2.1**
   (`r_K = √μ r`, `β_n^K = A μ^{−n/2}β_n`). É a **única fronteira
   epistêmica real** que sobrou no arco: o mapa é **entrada** do R-13b,
   não saída, e o que ficou verificado é a cadeia **interna** dado o
   mapa. Barato. Ver §6, **P-6**.
7. **Abrir Fasiello–Tolley 1308.1647** — a fonte primária *real* do
   bound de Higuchi em FLRW, que este arquivo cita desde a v1 **sem
   tê-la lido**, e conferir o **fator `1/2` no potencial** que a nota
   de rodapé 3 de 1503.07436 declara (⟹ **fator 2 nos β** para quem
   citar 1308.1647 diretamente). Se o cap. 06 for citar a fonte
   primária do bound, isto é **pré-requisito**, não opcional.
8. **A cota de Higuchi em fundo dinâmico bimétrico, DERIVADA** — nem
   herdada de de Sitter, nem obtida pela substituição `ξ → r`. Hoje o
   repositório usa `m_T² ≥ 2H²` com `ξ` dinâmico, que o R-13a §3.3
   mostra **não corresponder a nenhum dos dois critérios da fonte**.
   É o item conceitualmente mais caro que o arco deixou aberto.
9. **D3 — verificar internamente** `m_T²/H² → 3(4+3w)` e **resolver a
   discrepância em w = −1 (6 vs 3)** antes de usar qualquer dos dois
   números. Enquanto isso não for feito, o corpus deve escrever "12 na
   era de matéria" e nunca "12 no primordial".
10. **Decidir R-a** (§2b): alinhar o cap. 07 §4 com o `r10a` §3b, ou
    justificar a força extra com o R-10d elevado a argumento central.
    É decisão editorial e bloqueia a submissão. **O arco R-13 aumentou
    a pressão sobre este item:** a assimetria de peso que o R-a explora
    (fantasma fatal, gradiente **não** fatal) deixou de ser inferência
    nossa e é **estrutura declarada** de 1503.07436 (§III D, §VI).
11. **Correções de texto herdadas do R-12i §5 e do arco R-13** — estado
    hoje. *Feitas:* cap. 07 §4 (limiar r ≳ 0.21, com nota de
    proveniência); `resultado_r10a_gradiente.md` §3 (linha do enunciado
    corrigido); este documento (esta reescrita, e a atualização do arco
    R-13). *Pendentes, todas apenas registradas aqui — nenhum outro
    arquivo foi tocado:*
    - **cap. 06 §2 e §4** — a atribuição de `m_T² ≥ 2H²` (R-13a §3.3):
      é o **bound de de Sitter aplicado à massa tensorial dinâmica**;
      o bound de Higuchi em FLRW (Fasiello–Tolley 1308.1647; Könnig
      1503.07436 eq. 14) é a **mesma expressão com `ξ → r`** e equivale
      a `r′ ≥ 0`. E o `12` merece a nota de que o objeto de Könnig dá
      **`3`** no mesmo limite.
    - **cap. 05 §2** — o critério "lapso físico `ξ > 0`" **é** o
      critério tensorial/helicidade-2 da fonte (§III C, via Cusin et
      al. 1412.5979). Ligar os dois, e registrar a hierarquia:
      `ξ ≥ r` é estritamente mais forte que `ξ > 0` para `r > 0`.
    - **Housekeeping de normalização** (R-13b §3.5): `derivations/02`
      §3.4 e `manuscript-v2/06` §4 citam `m_T² = −3.19` com
      `M_ef² = 1`, enquanto o script de fundo usa
      `M_ef² = 1/(1/M_g²+1/M_f²) = 0.5` — razão medida **2.000000**.
      **Não é erro de física** (o fator estrutural e o sinal batem, e
      `m_T²/H²` é invariante), é inconsistência de normalização entre
      dois documentos do corpus.
    - **Onde o corpus escrever "o IBB está em aberto/reaberto"** —
      cap. 07, cap. 09, R-10c, R-10 consolidado — atualizar para o
      veredito vigente **com a proveniência**, nunca só com o veredito.
12. **Decidir a pendência da medida Stückelberg** (§6, P-2) — ou refazer
    a projeção sobre o modo métrico Ẽ do sistema 2-DOF corrigido, ou
    retirar a linha.
13. **β₂ ≠ 0 / β₃ ≠ 0 sobre o ramo infinito** (fora da célula IBB
    genuína) e **radiação** (`1 + w_tot > 0` continua valendo, mas a
    cúbica muda). Fronteiras declaradas do R-13b §0; baixa alavanca
    enquanto o veredito de classe estiver fechado na célula genuína.
14. O programa (b1) ganhou genealogia (ISS 1971 → holografia → FQH
    2024) e checklist de obstáculos — insumo direto do cap. 09, sem
    alteração de estatuto por nenhum dos três eventos.

*Itens da v1 que saem da fila:* "D1 (redução completa de vínculos no
ponto fixo)" — objeto caído; "a escrita do cap. 07 pode começar já com
esta bibliografia, condicionada ao D1" — o cap. 07 existe e foi
reescrito em 2026-08-13 com o arco completo.

*Itens que saem da fila em 2026-08-13 (arco R-13):* o **teste de
tradução** (item 2) e a **reabertura do ramo infinito com β₄ ≠ 0**
(item 3) — **os dois executados**. Saem também, por consequência, as
duas frases de espera que eles sustentavam: *"enquanto isso não rodar,
o ramo infinito permanece REABERTO"* e *"escrever 'o IBB está excluído'
é importar um resultado de outro sistema de convenções"* — a tradução
foi feita, verificada e medida, e o enunciado deixou de ser importação.

---

## 6. Pendências declaradas e as duas lições de importação

### A lição do "0.28" — um número sem qualificação de modelo

O número **existe**, é **exato**, e **não é do nosso modelo**.
√((√5−2)/3) = 0.28052 é a raiz do numerador da eq. (69) de 1407.4331,
que é enunciada sob a hipótese explícita de que **apenas β₁ é
não-nulo**. A nossa célula mínima é o modelo **β₀β₁ com β₀/β₁ = 1**
(assinatura inequívoca: `r_∞ = (√13−1)/6` resolve λ = 1 exatamente), e
para *esse* modelo a fonte tem equação própria — a (73) — cuja raiz é
**0.21448**, contra o nosso **0.20793**: **3.1% de acordo**, e não os
34.9% que a comparação errada exibia.

**O percurso, verificável no git.** O "0.28" entrou no corpus em
**2026-08-11**, por este documento (commit `e6d3ee1`), sem
qualificação de modelo. Em **2026-08-13** foi copiado para
`resultado_r10a_gradiente.md` §3 ("o setor escalar é são na era tardia,
r ≳ 0.28") e daí para o cap. 07 §4 do manuscrito, onde passou a
**contradizer o `a_cross = 0.578` citado quatro linhas abaixo** — em
r = 0.28 o nosso `c_s²` já vale **+0.41**, de modo que usar 0.28 como
fronteira entregava **0.2 e-fold de era instável para o lado
saudável**. Caiu no mesmo dia, quando a fonte foi finalmente aberta.

**A regra que entra.** Todo número importado da literatura carrega,
na mesma linha, **o modelo e o ponto do espaço de parâmetros em que
foi derivado** — ou não é importado. Um limiar sem o seu modelo não é
um dado: é um rumor com casas decimais. E note o padrão, que é o mesmo
do Erratum-02 e do Erratum-03: o número não foi refutado por um
cálculo melhor; foi refutado por **alguém abrir a fonte**. Três
retratações, três causas diferentes, uma constante — validação
exaustiva dentro de um ponto cego estrutural.

### A segunda lição — a armadilha de SINAL entre as duas fontes

*Da mesma família do "0.28", e registrada **antes** de custar alguma
coisa. Nível: **`V-13a`** (R-13a §1.7, verificado nas duas rotas).*

**O fato.** As duas fontes primárias do corpus usam **ansätze
diferentes** para a análise de perturbações:

| Fonte | Ansatz | O que `ω² < 0` significa |
|---|---|---|
| **1407.4331** (§V) | `X ∝ e^{iωN}` | ω imaginário ⟹ crescente ⟹ **INSTÁVEL** |
| **1503.07436** (§IV) | `Ξ_i ∝ e^{ωt}`, exponencial **real** | oscilante ⟹ **ESTÁVEL** |

**`sign(ω²)` não é comparável entre as duas sem traduzir o ansatz.** E
a demonstração é fechada, não retórica: a eq. (24) de 1503.07436 dá
`ω² = +(k/ℋ)²·r''/(3r')`, enquanto o R-12i extraiu de 1407.4331 a
identidade `c_s² = −r''/(3r')`. **Mesma física, sinal de `ω²` trocado.**
Quem importar a (24) sem notar isso troca **estável por instável** — e
é o mesmo autor, com um ano de diferença.

**A regra que entra, irmã da anterior.** Todo **sinal** importado da
literatura carrega, na mesma linha, **a convenção de ansatz em que foi
derivado** — ou não é importado. Um `ω² < 0` sem o seu `e^{iωN}` ou
`e^{ωt}` não é um dado: é meio dado, e a metade que falta inverte a
conclusão. Note que esta lição **não** custou uma retratação: ela foi
apanhada na leitura da fonte, não numa contradição interna. É o único
item desta lista que chegou por prevenção em vez de por dano.

### Pendências que esta reescrita NÃO conseguiu decidir

**P-1 — Níveis de verificação da v1.** A v1 declarou disciplina por
item mas só a registrou em cinco linhas. Todas as demais estão
marcadas `n/r` no §1.2 e devem ser **tratadas como nível-de-busca**
até que alguém as reabra. Isto não é uma acusação contra a v1: é a
recusa de herdar um nível que ninguém escreveu.

**P-2 — A medida Stückelberg (0.995 / 0.998).** Os objetos medidos
eram *o taquião congelado de k = 1* e *o fantasma da fresta μ = 0.1*
(`gate1c_nota_trilema.md`, `resultado_stuckelberg_goldstone.md`,
`resultado_d1_reducao.md`), e ambos constam como **caídos** na tabela
do cap. 07 Ato 4. A medida não foi refeita sobre o sistema 2-DOF
corrigido e **não aparece em nenhuma tabela de supersessão** — nem na
do R-7 §4, nem na do cap. 07. **Nenhum documento do corpus decide o
caso.** As duas saídas possíveis: ou a identificação helicity-0 se
transfere para o modo métrico Ẽ do sistema corrigido — e a linha volta,
com **números novos** —, ou a medida caiu junto com os modos. Até lá,
**suspensa**, e fora do ranking.

**P-3 — A atribuição de `Δ = ½rr′`.** O R-12i declara-a **inferência
estrutural, não re-derivada**: hipótese forte, com assinatura
quantitativa fechada e predição falsificável, mas hipótese. Enquanto o
teste do item 1 da fila não rodar, o corpus não pode escrever "a nossa
fórmula está incompleta" como fato — só como diagnóstico declarado.

**P-4 — `Δ` para λ ≠ 1.** Não testado; a forma fechada do R-12b só
existe em λ = 1. Em r → 0, porém, `r′ → 3r` para qualquer λ, então
`Δ → (3/2)r² → 0` sempre — o `−1` está seguro em λ qualquer, *se* a
forma de Δ for genérica. O "se" é literal.

**P-5 — A discrepância em w = −1** (6 vs 3), herdada do D3. Aberta,
com instrução explícita de não usar nenhum dos dois números antes de
verificar. *Nota de higiene, para não gerar uma terceira confusão:* o
`3` desta pendência (fórmula `3(4+3w)` avaliada em w = −1) **não tem
relação nenhuma** com o `3` do funcional de Higuchi do §1.1b
(`m_T²|_{ξ→r}/H² → 3` no ramo finito primordial, era de **matéria**).
São dois objetos diferentes que coincidem num número.

> **[RESOLVIDA — 2026-08-17, `docs/auditoria_r13.md` §3.3.]** *A nota de
> higiene acima está CORRETA e fica.* O que se resolve é a discrepância
> em si, e ela não era numérica: **`3(4+3w)` não é avaliável em
> `w = −1`**. A derivação usa `r ≈ β₁/(μρ̃)` com `ρ̃ → ∞`, o que exige
> que `ρ` **dilua**, isto é `w > −1`. Em `w = −1` a densidade é
> constante, `r` não vai a zero, e o regime `r → 0` **não existe** —
> logo `3(4+3w)|_{w=−1} = 3` é **extrapolação fora do domínio**, não
> predição da fórmula. O que existe em `w = −1` é o ponto fixo de de
> Sitter (`ρ̃ = 0`), onde `r³V_f = μ r V_g` e
> `m_T²/H²|_dS = 3ℬ(r_∞)(1+μr_∞²)/(μ r_∞ V_g(r_∞))` — **verificado por
> CAS (resíduo 0), e em `β₀=β₂=β₃=0` colapsa em `1+1/(μr_c²)`,
> reencontrando o corolário F-1 do R-13b por outra via**. Essa
> expressão **não é um número universal**: depende de `r_∞` e dos `β_n`.
> Portanto **nem `6` nem `3` podem ser "o valor de de Sitter"**, e não
> há discrepância a arbitrar. A instrução de não usar nenhum dos dois
> números **fica** — agora com a razão.

**P-6 — O mapa de convenções do R-13a §2.1 não passou por CAS.**
`r_K = √μ r`, `β_n^K = A μ^{−n/2}β_n`, `ρ_K = ρ/M_g²`: derivado à mão,
sobredeterminado pelas duas Friedmann (e a sobredeterminação **fecha**,
o que é evidência forte), mas é **entrada** do R-13b e não saída. O que
o R-13b verificou por CAS é a cadeia **interna** — `(14) ⟺ (15) ⟺
𝒲′(r) ≤ 0 ⟺ r′ ≥ 0` —, **dado** o mapa. É a **única fronteira
epistêmica real** que o arco R-13 deixou sobre o veredito do ramo
infinito, e é barata de fechar (§5, item 6). Enquanto não fechar, o
veredito do §2b permanece — ele não depende deste item para o **sinal**
de `r′`, que é invariante sob a tradução (`μ > 0` constante ⟹
`r_K′ = √μ r′`), mas depende dele para a **forma "massa"**.

> **[FECHADA — 2026-08-17, `docs/auditoria_r13.md` §1.]** O mapa foi
> re-derivado por **rota independente** — a redundância da ação sob
> `f_{μν} → λ² f_{μν}`, com os `e_n(√(g⁻¹f))` calculados pela raiz
> matricial de Sylvester de `tdcp_pert_lib.py`, **sem tocar nas
> Friedmann**. Resíduos simbólicos **zero** nos cinco `β_n`, com
> solução **única**; e mapas errados (`c = μ`; `β_n ~ μ^{−n}`)
> **reprovam** (teste de poder). A sobredeterminação foi **exibida**:
> a Friedmann-g deixa `c` livre, a Friedmann-f o fixa por **duas** vias
> independentes que dão o mesmo `c = √μ`, e o padrão `μ^{−n/2}` no
> `n = 4` **saiu** em vez de ser imposto. As eqs. **(12)** e **(13)** de
> Könnig — que não entraram na construção — batem com a nossa `𝒲(r)` e
> com `√μ·dr/dN` (resíduos 0), esta última com **`w` geral**.
>
> **O item mais caro da fila passa a ser outro:** se a **própria
> eq. (14)** continua sendo a condição de Higuchi ponto a ponto sob
> modulação `β_n(φ₋)`. Isso é declarado pelo R-13a (§2.2, hipótese 2) e
> **não foi verificado por ninguém — nem pela auditoria**. Ver
> `auditoria_r13.md` §6.3.

**P-7 — Fasiello–Tolley 1308.1647 continua não aberta.** É a fonte
primária *real* do bound de Higuchi em FLRW; este arquivo a cita desde
a v1 (§4) sem tê-la lido, e agora o corpus usa o bound como critério de
exclusão. A nota de rodapé 3 de 1503.07436 declara um **fator `1/2` no
potencial** que se compensa por redefinição dos β — **quem citar
1308.1647 diretamente herda fator 2 nos β**. Enquanto não for aberta, a
citação correta do bound é **via Könnig 1503.07436 eq. (14)**, com a
atribuição a Fasiello–Tolley registrada como sendo *da fonte*, não
nossa. É exatamente o padrão que o "0.28" ensinou.
