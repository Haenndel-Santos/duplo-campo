# Síntese Cruzada dos Cinco Pareceres Especializados

**Data:** 2026-08-13. Cinco especialistas independentes (astrofísica,
física teórica, astronomia observacional, fundamentos quânticos,
cosmologia) leram o estado atual da TDCP-F1 — manuscrito v2 +
erratums + cascata R-7 + sondas R-8a/b — e emitiram parecer com
critério comum: pontos fortes, pontos fracos, referências por ponto e
propostas de modelagem. Cada um trabalhou isolado dos demais e sob o
filtro de supersessão (proibido citar números da era do sistema
espúrio como vigentes).

Pareceres: `parecer_astrofisica.md`, `parecer_fisica_teorica.md`,
`parecer_astronomia.md`, `parecer_mecanica_quantica.md`,
`parecer_cosmologia.md`.

Este documento **não substitui** os pareceres — sintetiza
convergências, divergências e consequências para a fila. Onde os
pareceres opinam, a opinião é atribuída ao especialista; onde
derivam, o cálculo é marcado como tal e **carece de verificação
interna** antes de virar resultado do repositório.

---

## 1. A convergência principal: sã, blindada e quase-invisível

Os cinco chegam, por caminhos diferentes, ao mesmo diagnóstico:

| Especialista | Formulação |
|---|---|
| Astrofísica | "saudável e segura — e é segura demais; nenhuma escala astrofísica acessível separa a teoria de GR" |
| Física teórica | "empiricamente indistinguível de ΛCDM + espectador no linear tardio" |
| Astronomia | "viável e não-excluída, mas ainda não é uma teoria testável… o risco dominante não é a refutação, é a indistinguibilidade por construção" |
| Cosmologia | "no benchmark β-constante a teoria é HR ⊕ escalar livre; a TDCP propriamente dita vive em F′ ≠ 0" |
| Quântica | "a dimensão quântica está genuinamente não construída" |

E três deles observam, independentemente, que a única previsão
falseável viva (m_T/H₀ ≈ 2.3) **testa gravidade bimétrica, não a
TDCP** — é a assinatura genérica de auto-aceleração da classe.

**Consequência editorial imediata:** o cap. 01 e o cap. 09 devem
declarar que a F1 não alivia nenhuma tensão observacional e que sua
motivação é conceitual (recomendação explícita da astrofísica) — sob
pena de ser corrigido por um referee na primeira página.

## 2. A convergência metodológica: o padrão do Erratum-02 se repete em dois eixos novos

Dois pareceres, sem contato, identificam a **mesma classe de falha**
que produziu o Erratum-02 — validação exaustiva dentro de um ponto
cego estrutural:

- **Cosmologia:** os gates do R-7 (autovalores de K₂, W00, envelope,
  lnA) são **cegos a instabilidade de gradiente por construção**;
  c_s² < 0 passa incólume, e as passagens correm de kh 20 → 0.2, a
  direção que desliga o efeito.
- **Física teórica:** o suporte 2b do Gate 2B (W00 nunca cruza zero)
  tem **poder de detecção estruturalmente baixo, não amostralmente
  baixo** — o fantasma BD é invisível na ação quadrática por
  construção; mais pontos jamais ajudariam. Agravante interno: o
  repositório tem regra de auto-teste de poder de detecção (gate1c
  §5.4) que **nunca foi aplicada ao W00**.

Isto é mais grave que qualquer achado individual: significa que a
lição do Erratum-02 foi codificada (V-XREP-a/b, normalização
congelada) mas **não generalizada** — os gates continuam sendo
desenhados a partir do que se sabe olhar.

**Regra proposta para o método (cap. 02):** todo gate novo declara
explicitamente *qual patologia ele seria incapaz de ver*, e essa
declaração entra no cabeçalho junto com os critérios.

## 3. O sinal ambíguo que ninguém pode ignorar

O R-7e reportou ω²(Ẽ) = W/K **negativo**, variando de −10² a −10⁷, e
o repositório arquivou o fenômeno como "artefato de envelope"
(`docs/resultado_r7e_saude_interna.md` §2). A cosmologia aponta uma
incompatibilidade interna: |ω|/H ~ 3×10³ com decaimento medido
G_win = −10 não fecha sob leitura ingênua — com |ω| ≫ H a fricção 3H
não pode amortecer.

Leituras possíveis: (i) W/K não é ω² na convenção do repositório
(há contribuições de C e Ċ que não entram nessa razão) — o mais
provável; (ii) o modo é constrangido e a razão não tem significado
espectral; (iii) há instabilidade de gradiente real mascarada pela
direção da passagem. **Nenhuma das três está estabelecida.** Até
resolver, o enunciado "no-go revogado" é forte demais para o setor
métrico — a saúde do espectador δφ₋ (âncoras analíticas fechadas) não
está em questão.

> **[NOTA DO REPOSITÓRIO — 2026-08-13, pós-R-9/R-10a/R-11/R-12. O
> texto do parecer acima fica intacto; esta é anotação, não
> reescrita.]** O ponto foi resolvido, e o parecer acertou **duas
> vezes, em objetos diferentes**.
>
> **Era a leitura (i).** O R-9 (Bloco 0), item (c), mediu:
> `W/K` **não é a relação de dispersão na convenção do repositório**.
> O integrador resolve `K q̈ + (K̇ + C − Cᵀ) q̇ + (Ċ + W) q = 0`, logo
> a frequência efetiva é `(Ċ + W)/K` — exatamente as "contribuições de
> C e Ċ que não entram nessa razão" que o parecer apontou.
> **16/32 entradas têm `W/K < 0` e `(Ċ+W)/K > 0`** — todas as do modo
> métrico, nos dois fundos, em todas as épocas; em a = 200,
> −1.5e5 H² contra +514 H². O discriminador de frequência fecha o
> caso: se `|W/K|` fosse a frequência haveria ~110 cruzamentos de zero
> na janela, e medem-se **6** (WKB pela frequência correta prevê 6.5).
> A incompatibilidade interna que a cosmologia detectou — |ω|/H ~ 3×10³
> com G_win = −10 — era **real, e era o sintoma**: a razão apontada não
> era a frequência. `docs/resultado_r7e_saude_interna.md` §2 foi
> corrigido; fonte: `docs/resultado_r9_bloco0.md` §1.
>
> **E a preocupação de fundo se confirmou — por outra via.** A frase
> *"o enunciado 'no-go revogado' é forte demais para o setor métrico"*
> estava certa, só que o problema não morava naquele sinal. O **A1**,
> que este mesmo documento pôs como prioridade máxima do Bloco 1 (§7,
> item d), rodou e encontrou **instabilidade de gradiente real**:
> `c_s² < 0` em todo o regime r → 0
> (`docs/resultado_r10a_gradiente.md`), elevada a **no-go de classe
> por gradiente** em 108/108 células da forma-β
> (`docs/resultado_r11_nogo_gradiente.md`) e fixada, com instrumento
> limpo, em **c_s² = −1 exato** em r → 0, **+1 exato** na era tardia,
> com troca de sinal em **a_cross = 0.578 ⟹ z_cross = 0.61** — a era
> instável **cobre a recombinação**
> (`docs/resultado_r12_instrumento_e_cs2.md`,
> `docs/resultado_r10_consolidado.md`).
>
> A **leitura (iii)** deste mesmo §3 **antecipava a possibilidade**.
> O mascaramento medido, porém, não foi o da direção da passagem em
> kh: foi o da **época**. Toda a cascata R-7 rodou em a ∈ [100, 8e4],
> que nesta família é a era tardia (r = r_∞), e seus gates são cegos a
> instabilidade de gradiente por construção — o §2 deste documento,
> que a própria cosmologia escreveu. Ou seja: (i) explica o `W/K`
> negativo do R-7e; (iii) é o fenômeno físico, que estava em outra
> época.

## 4. Achados novos, por gravidade

### 4.1 Bloqueantes (podem matar ou reescrever a teoria)

1. **Paredes de domínio** (quântica). Uma Z₂ discreta global exata
   quebrada espontaneamente produz paredes; o corpus é *inteiramente
   silencioso* (zero ocorrências de "domain wall"/"Kibble"/"Zurek"/
   "Zel'dovich"). Pior que o caso genérico: a Z₂ é exata em sentido
   forte (V par, β_n ∝ φ₋², matéria não toca φ) — nenhum setor pode
   enviesá-la — e o cap. 03 §1 **veta explicitamente** a quebra
   explícita, fechando por decisão de projeto a saída padrão.
   Primeiro vínculo dimensional real da teoria:
   σ ≈ (2√2/3)μ₋³/λ₋ ≲ (1 MeV)³ ⟹ **μ₋ ≲ λ₋^{1/3} MeV**, salvo bias
   ou diluição. Como a escala de μ₋ nunca foi fixada (benchmark em
   v★=1 adimensional), *não sabemos se passa ou falha*. Detalhe
   específico: no núcleo da parede φ₋=0 ⟹ r★ = r★⁽⁰⁾ — a parede é uma
   folha onde a bifurcação é desfeita.
2. **Instabilidade de gradiente do ramo finito** (cosmologia). O
   repositório trabalha exatamente no ramo que Könnig–Akrami–
   Amendola–Motta–Solomon ([arXiv:1407.4331]) declaram instável por
   gradiente em alto z; o "ramo infinito" descartado por ξ<0 é o que
   eles promovem. Registrado em `posicionamento_literatura.md`, nunca
   confrontado pela cascata.
3. **`p_φ` cruza zero periodicamente** (física teórica). Pós-pouso,
   com ω²>0 e fricção 3H, o campo oscila amortecido ⟹ p_φ passa por
   zero a cada meio período ⟹ a matriz de Dirac degenera em cada
   cruzamento. Teste de horas.

### 4.2 Estruturais (mudam o que a teoria é, ou o que podemos afirmar)

4. **δφ₊ ausente da redução** (quântica). Não há inflaton; o modo que
   carrega ζ não está no sistema. A contagem "2 DOFs escalares" é **do
   setor modelado**, não da teoria — e nenhuma afirmação sobre
   n_s/A_s/isocurvatura é possível hoje. Ressalva de escopo
   obrigatória no cap. 07.
5. **Escopo de época do R-8a** (astronomia). kh = k/(aH) é função da
   época: "kh ≲ 22 indecidido" avaliado em z ≈ 1100 cobre k ≲ 0.14
   h/Mpc ⟹ **ℓ ≲ 1300**, todo o CMB primário. A sonda só foi até
   z ≈ 8, e o próprio R-8a registra que os desvios **crescem** quando
   r decresce. "Sub-horizonte consistente com GR" vale para z ≲ 10 e
   está sendo lido como se valesse para o CMB.
6. **A modulação "β₁ único" não é radiativamente estável** (física
   teórica): os e_n se misturam sob renormalização, e a proteção
   técnico-natural da bigravity é sobre m², não sobre razões β_i/β_j.
   Essa escolha sustenta *simultaneamente* o fator atenuante do Gate
   2A e a novidade reivindicada.
7. **μ = M_f²/M_g² nunca foi varrido** (astrofísica). A "visibilidade"
   do segundo setor é ε ≡ K_ℓℓ/K_hh = μr³/ξ (→ μr²/4 primordial,
   ≈ 0.11μ hoje) — é o dial que decide se a F1 é falseável, e nem
   R-8a nem R-8b o varreram.
8. **O potencial escolhido é inflação híbrida** com φ₋ como waterfall
   Z₂ (quântica) — a variante que a literatura evita por causa das
   paredes, e cujo waterfall tipicamente *termina* a inflação,
   comprometendo a saída "diluição inflacionária".

### 4.3 Correções factuais no corpus

9. Ω_m ≈ 0.25 descrito como "razoável" em
   `docs/resultado_ramo_finito.md` está ~8–9σ fora de Planck —
   marcar como superado pela reancoragem do R-8b (Ω_m = 0.3).
10. "m_T/H₀ cravado" (R-8b) é sobre-afirmação: é um dial de 1
    parâmetro num espaço de ≥5 (física teórica).
11. `manuscript-v2/04_bianchi_e_vinculos.md` §4 embaça que o resíduo
    p_φβ₁′ é objeto de minisuperespaço (sombra da Bianchi), **não** o
    par de constraints que remove o BD (física teórica).
12. A imunidade a GW170817 é contingente à escolha "matéria só em g" —
    deve ser declarada como *escolha*, não como resultado
    (astrofísica).

## 5. Duas derivações independentes convergentes — e uma discrepância a resolver

Cosmologia e astrofísica, sem contato, generalizaram o m_T²/H² → 12
para w arbitrário e chegaram à **mesma fórmula**:

- cosmologia: ξ = r[1+3(1+w)] ⟹ m_T²/H² → 3[1+3(1+w)]
- astrofísica: m_T²/H² → 3(4+3w)

São idênticas (3[1+3(1+w)] = 3(4+3w)): **12 em matéria, 15 em
radiação**. Fecha o desafio D3 de `posicionamento_literatura.md` sem
nova integração e mostra que os rótulos "primordial" do corpus
significam, de fato, "era de matéria". A astrofísica acrescenta
c_f² = (4+3w)² (radiação: c_f = 5c) e observa que c_f² → 1 no ponto
fixo tardio.

**Discrepância a resolver:** o resumo da cosmologia atribui 6 ao caso
Λ, enquanto a fórmula comum dá 3 em w = −1. Provável causa: o limite
assintótico foi derivado no regime r → 0, e o ponto fixo tardio tem
r → r_∞ ≠ 0 — regime diferente. **Verificar antes de usar qualquer
dos dois números.**

Ambas as derivações são de especialistas e **não foram verificadas
internamente**; entram como candidatas a resultado, não como
resultado.

## 6. As oportunidades — onde a teoria pode voltar a ser falseável

Cinco propostas novas, nenhuma no plano atual, ordenadas por
custo/informação:

1. **w_eff(z) vs DESI DR2** (cosmologia) — meia sessão, o fundo já
   existe em nível 2a. Bimétrica dá DE fantasma; há literatura
   recente reportando melhora de ajuste e alívio de H₀. **É a única
   alavanca observacional viva do lado do fundo**, e o cap. 09 mira
   justamente onde a variância cósmica é pior.
2. **Isocurvatura β_iso** (astronomia) — dois campos primordiais e
   *zero linhas* no corpus. Provavelmente o vínculo mais decisivo
   disponível hoje.
3. **Modos B / supressão de r** (astronomia) — m_T/H = O(2–3.5) em
   toda a história ⟹ a transição k = m_T·a cai sempre em kh ≈ 2–3.5;
   o ângulo de mistura g–f prevê supressão de r observável pelo
   LiteBIRD.
4. **Collider cosmológico** (quântica) — m_T²/H² → 12 põe o spin-2 na
   série principal: μ₂ = √9.75 = 3.12 com dependência angular P₂,
   **frequência sem parâmetro livre**. A previsão mais distintiva
   proposta em toda a rodada.
5. **Varredura de μ** (astrofísica) — dias, decide se o R-8 produzirá
   um nulo previsível.

Recuperável dos Anexos I–K (quântica): o **emaranhamento gaussiano
φ₁–φ₂**, com ξ_ent = (√ω₊−√ω₋)/(√ω₊+√ω₋), que **diverge no ponto
crítico** — derivável da própria ação, uma sessão. Já Λ_ent é
insalvável por razão mais funda que a registrada: entropia não
gravita, e bipartição interna não é grau métrico (viola o critério de
anti-circularidade do G1-c).

## 7. Recomendação unânime sobre a fila: NÃO iniciar o R-8 completo

Os cinco convergem, com ênfases diferentes, em que o R-8 completo
(Boltzmann + C_ℓ) é caro, mira a janela mais limitada por variância
cósmica, e seria construído sobre fundações não testadas nos eixos que
importam. **Fila reordenada proposta:**

**Bloco 0 — horas a dias (falsificação barata):**
- (a) `p_φ` cruza zero no pouso ⟹ degenerescência da matriz de Dirac
  [física teórica P1];
- (b) primeira-classe do difeomorfismo diagonal: {ℋ_diag, ℋ_rel}
  fecha? — falha aqui é mais rápida e mais terminal que o BD
  [física teórica P2];
- (c) resolver o ω² < 0 do R-7e (qual das três leituras) [cosmologia].

**Bloco 1 — uma sessão cada (decidem se há teoria):**
- (d) **A1: teste de gradiente c_s²** com critérios pré-declarados,
  confrontando λ₁ = −k²(2w₁+1) e o resultado de 1407.4331
  [cosmologia] — *prioridade máxima do bloco*;
- (e) **A2: w_eff(z) vs DESI** [cosmologia];
- (f) escopo de época: refazer R-8a em z ≳ 100 com era de radiação
  [astronomia];
- (g) varredura de μ [astrofísica];
- (h) paredes de domínio: fixar a escala de μ₋ e decidir a saída
  (bias/diluição/promoção a U(1)) [quântica].

**Bloco 2 — antes de qualquer submissão:**
- (i) Gate 2B feito direito: {𝒞(x),𝒞(y)} com β_n genéricos e
  comparação obrigatória com a literatura de mass-varying/quasidilaton
  [física teórica P3];
- (j) Vainshtein/PPN + buracos negros (instabilidade de spin-2
  massivo) [astrofísica];
- (k) V-EXT: reproduzir um resultado bimétrico publicado dentro de 2%
  antes de afirmar qualquer C_ℓ próprio [astronomia].

**Só então** o R-8, e com a arquitetura que dois pareceres
recomendam: **fork de CLASS, não hi_class/EFTCAMB** (bimétrica não é
Horndeski; o mapeamento EFT destrói justamente a janela
quase-horizonte), fundo por raiz algébrica em vez de ODE, gauge
newtoniano em g, ICs adiabáticas com gate de conservação de ζ, e
critérios de falseamento **pré-declarados** — incluindo o critério de
encerramento (astrofísica PM-4: se o efeito máximo em ℓ ≤ 30 for
< 2%, encerrar o programa observacional e declarar
indistinguibilidade como resultado).

## 8. O que os cinco elogiam (e que deve ser preservado)

- O Erratum-02 e o método que o produziu — prova de identidade de
  ação (r6c), V-XREP-b, tabela de supersessão — "valem mais que
  qualquer resultado numérico do projeto" (física teórica);
  "mais qualidade de método do que a maioria dos papers de gravidade
  modificada apresenta" (cosmologia).
- A retratação auto-imposta da previsão de ISW e o fraseado de
  precisão do R-8a (astronomia).
- A construção de μ/Σ como razão de resposta, em que convenções
  cancelam (astronomia, cosmologia).
- A degenerescência do modulador global (cap. 03 §0) — considerada
  *subvendida*: implica que o chameleon bigravity é estruturalmente
  incapaz de mover a raiz, e mereceria a introdução do paper (física
  teórica).
- A circularidade HR–Goldstone do gate1c como obstrução real e bem
  formulada (física teórica).
- A troca de "bifurcação" por SSB de Z₂ na v2 — "o movimento certo"
  (quântica).

## 9. Estatuto deste documento

Nível: **pareceres externos, não verificados internamente**. Nenhum
número, fórmula ou vínculo aqui entra no corpus como resultado do
repositório antes de (i) verificação por script com critérios
pré-declarados, ou (ii) checagem de fonte para os itens de
literatura. As referências externas citadas pelos especialistas
carregam as marcas [verificar] que eles próprios atribuíram.
