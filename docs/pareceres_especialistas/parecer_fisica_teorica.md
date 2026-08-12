# Parecer — Física Teórica

**Emissor:** revisor externo independente (teoria de campos, gravidade
massiva/bimétrica, formalismo hamiltoniano de vínculos, EFT).
**Data:** 2026-08-12. **Base de leitura:** `manuscript-v2/03,04,07,08`;
`auditoria/erratum_02_reducao_numerica.md`; `docs/gate2_ghost.md`;
`docs/gate1c_nota_trilema.md`; `docs/resultado_r7e_saude_interna.md`;
`docs/resultado_r8b_limite_mH0.md`; `docs/posicionamento_literatura.md`;
`docs/resultado_r7_cascata.md` §4 (filtro de supersessão aplicado —
nenhum número pré-2026-08-12 é citado como atual).

**Convenção deste parecer.** Cada afirmação vem marcada:
`[REPO-n1|2a|2b|3]` = derivado no repositório, no nível epistêmico que o
próprio repositório declara; `[OPINIÃO]` = juízo meu sobre material
derivado; `[CONJECTURA]` = previsão minha, não testada por ninguém;
`[verificar]` = referência externa que não confirmei na fonte.

---

## Resumo executivo

1. O Erratum-02 é sólido e o método que o produziu é o melhor ativo do
   projeto: a prova de identidade exata das duas ações (r6c) é o que
   transforma "duas reduções discordam" em "uma redução erra". `[REPO-n1]`
2. Com ele, a implementação F1 deixa de estar morta: 2 DOFs escalares,
   sem direção cinética negativa nos regimes testados. Isso é
   *consistência com Hassan–Rosen*, não descoberta — e o repo diz isso.
3. O Gate 2 Parte B continua sendo o único buraco capaz de matar a
   arquitetura, e ele é **mais grave do que o repo pesa** — não por
   falta de amostragem, mas por falta de *poder de detecção*: o BD é
   invisível ao setor linear por construção.
4. O suporte 2b (W00 nunca cruza zero) nunca foi submetido ao
   auto-teste de poder de detecção que o próprio método do projeto
   exige (`gate1c` §5.4). Isso é uma inconsistência interna.
5. Identifiquei dois riscos concretos e baratos de testar que não
   constam do corpus: **(i)** `p_φ` cruzando zero durante a oscilação
   de pouso degenera a matriz de Dirac periodicamente; **(ii)** a
   escolha "β₁ único" — que é simultaneamente o fator atenuante do
   Gate 2B e a novidade defensável — **não é radiativamente estável**.
6. A "terceira estrutura" é, na minha leitura, benigna para a contagem
   e maligna para a *invariância*: o teste que falta não é de contagem,
   é se a combinação de primeira classe (diff diagonal) sobrevive.
7. EFT: com m ~ H₀, Λ₃ ~ (10³ km)⁻¹; o trabalho linear cosmológico do
   repo está ~18 ordens de grandeza abaixo dessa escala — seguro. O
   transiente e^{0.4} é fisicamente irrelevante, e essa é a má notícia.
8. R-8b é o melhor resultado *físico* vivo do corpus (previsão em vez
   de postulado), mas "cravado" é sobre-afirmação: a família testada é
   um dial de 1 parâmetro num espaço de 5. E U0 < 0 é o problema da
   constante cosmológica reintroduzido, não resolvido.
9. Cap. 08 está correto ao chamar a identificação de decreto. Ofereço
   quatro rotas de derivação, uma das quais (posto de f composta) pode
   ser fatal em uma tarde de álgebra — e por isso deve vir primeiro.
10. Veredito curto: implementação sã, teoria não derivada, e uma
    previsão falseável. Publicável como estudo de classe assim que o
    Gate 2B fechar analiticamente; hoje, não antes disso.

---

## Pontos fortes

**F1. A prova de identidade de ação (r6c) é o passo decisivo, e é
raro.** `[REPO-n1]` A situação "reauditoria externa dá det K = 0
simbólico; nossa cadeia dá autovalor negativo estável a 60 dígitos"
(`erratum_02` §3.2) é um empate epistêmico: duas construções exatas
discordando. O que quebra o empate não é mais precisão — é a prova de
que as duas L2 são **a mesma ação** a menos de derivada total,
peça por peça, em aritmética racional e off-shell
(`auditoria/erratum_02_reducao_numerica.md` §3.3). Só depois disso
"logo o erro está numa das reduções" é dedução e não retórica. Muitos
grupos teriam parado no passo anterior e escolhido o resultado
preferido. `[OPINIÃO]` Este é o padrão que o resto do corpus deveria
imitar.

**F2. O diagnóstico da forma da constraint de Bianchi (Erratum-01) é
estruturalmente correto e elementar da maneira certa.**
`[REPO-n1]` "Uma constraint canônica genuína é relação entre variáveis
de espaço de fase e é livre de lapso por construção"
(`manuscript-v2/04_bianchi_e_vinculos.md` §1) é o argumento certo, e a
forma resultante ℬ(r)(N_f ȧ − N_g ḃ) = 0 é a constraint de Bianchi
padrão de bigravity FRW da literatura (Comelli–Crisostomi–Nesti–Pilo
1111.1983; Volkov 1110.6153 `[verificar]` — o repo já cita ambos em
`posicionamento_literatura.md` §4). As duas rotas independentes
(bracket canônico e resíduo lagrangiano) com a mesma lagrangiana como
única premissa comum é a estrutura de prova correta.

**F3. A degenerescência do modulador global (cap. 03 §0) é uma
observação de desenho genuína, e é o que separa a F1 do vizinho mais
próximo.** `[REPO-n1]` Sob β_n → F(φ)β_n, r★ = −β₁/(2β₂) é invariante:
o fator global cancela na razão. Isso é álgebra de duas linhas, mas
tem consequência forte — implica que **chameleon bigravity**
(De Felice–Mukohyama–Uzan 1702.04490; +Oliosi 1711.04655), que usa
exatamente fator global, é *estruturalmente incapaz* de mover a raiz
algébrica pelo mecanismo da TDCP. A modulação diferencial não é um
detalhe de implementação: é a única forma da classe que faz o que a
teoria pede. `[OPINIÃO]` Este é o argumento mais forte de originalidade
do corpus e está subvendido em `posicionamento_literatura.md`.

**F4. Gate 2 Parte A está certa, e a razão dada é a razão certa.**
`[REPO-n2a]` "φ₋ é escalar e o valor de um escalar num ponto não
depende do lapso; a linearidade é termo a termo em n"
(`docs/gate2_ghost.md` §2.A.1). É o mesmo mecanismo pelo qual
mass-varying massive gravity preserva a constraint hamiltoniana
(Huang–Piao–Zhou, [arXiv:1206.5678](https://arxiv.org/abs/1206.5678)).
A tabela minisuperespaço de grau 1 em N_g e N_f (§2.A.2) é verificação
honesta do que ela é: sombra, e o doc diz isso.

**F5. A recusa explícita de certificar ausência de BD por contagem
numérica.** `[REPO-n3 + método]` `gate2_ghost.md` §4 registra a
assimetria correta (10 modos falsifica; 9 modos não certifica) e
`posicionamento_literatura.md` §2/D5 ancora isso em precedente real: o
extended quasidilaton foi declarado "ghost free" em 2013 e revertido
pela versão publicada — **Boulware–Deser ghost in extended quasidilaton
massive gravity**,
[arXiv:1309.2146](https://arxiv.org/abs/1309.2146). `[OPINIÃO]` Este é
o parágrafo que eu, como referee, usaria para acreditar no resto do
corpus. Mantenham-no no paper.

**F6. R-8b converte um postulado do corpus em previsão falseável, e o
mecanismo é auditável.** `[REPO-n2b]` O fold em s ≈ 5.7–6.2 vem de
`r²V_f(r) = β₄r² + 3β₂ + β₁/r` ter mínimo positivo (0.3 em r=1) na
forma-β do benchmark, com H*² = s·m_eff²·r²V_f/(3μ) fixo — verificado
numérica e analiticamente (`docs/resultado_r8b_limite_mH0.md` §2a).
Consequência: **m_T/H₀ ∈ [2.26, 2.41]** ao longo de toda a família
alcançável, com desvios de crescimento ≤ 0.012% na janela QS. Derrubar
o próprio postulado (30–300 H₀) com o próprio cálculo é o
comportamento correto e raro.

**F7. Gate1c nomeia a obstrução que importa.** `[REPO-n3 + 2b]` Duas
coisas: (i) a demolição parcial de Weinberg–Witten está correta — o
teorema restringe partículas *sem massa* de |h| > 1 com T^μν conservado
e Lorentz-covariante, e f₂(1270) é o contraexemplo massivo composto
experimental (Weinberg–Witten PLB 96 (1980) 59; PDG); (ii) a
**circularidade HR–Goldstone** é a observação mais afiada de todo o
corpus: "o modo mais provável de o programa R2 falhar não é dar errado:
é dar certo de volta para dentro da F1"
(`docs/gate1c_nota_trilema.md` §3). E o §9 mostra que a premissa subiu
de nível 3 para 2a/2b por medida (taquião de k=1 = π_L com projeção
0.995+). `[OPINIÃO]` Vale mais que vários resultados numéricos do
corpus e deve estar na introdução do paper, não numa nota de gate.

**F8. Infraestrutura anti-regressão real.** `[REPO-método]` A tabela de
supersessão (`resultado_r7_cascata.md` §4) e o par V-XREP-a/b
(`erratum_02` §6.2, com a nota de nomenclatura corrigindo o próprio
deslize de naming) são o tipo de instrumento que impede a repetição do
Erratum-02. Poucos programas acadêmicos têm equivalente.

---

## Pontos fracos e riscos

**W1. Gate 2B: o suporte 2b tem poder de detecção estruturalmente baixo,
e isso não está dito.** Este é o ponto mais importante do parecer.

O argumento do cap. 04 §4 é: no sistema corrigido, Ψ_f é vínculo exato
(det K = 0 simbólico) e W00 nunca cruza zero em 4 modos × 14 000 pontos
(`resultado_r7e_saude_interna.md` §1), logo "a estrutura de vínculos
aguenta o regime não-fatorado em nível linear". `[REPO-n2b]` Isso é
verdade e é útil. Mas:

- `[OPINIÃO]` O fantasma de Boulware–Deser em dRGT/HR é **notoriamente
  invisível na ação quadrática** em torno de backgrounds simétricos.
  A história da classe é exatamente essa: contagens lineares limpas
  seguidas de reversão por análise hamiltoniana completa
  ([1309.2146](https://arxiv.org/abs/1309.2146) é o caso citado pelo
  próprio repo em D5). Portanto "14 000 pontos sem cruzamento de W00"
  não é evidência fraca por amostragem — é evidência **do tipo errado**.
  Mais pontos não melhoram nada.
- `[OPINIÃO]` O corpus tem uma regra de método explícita para
  exatamente esta situação — `gate1c_nota_trilema.md` §5.4:
  *"o teste deve provar que detectaria a patologia conhecida antes de
  ser acreditado quando não a encontrar"*. **Esse auto-teste nunca foi
  aplicado ao W00.** É uma inconsistência interna do método, e o
  Erratum-02 é a prova viva de que ela morde: o pipeline anterior
  também passava em todos os seus gates.
- `[OPINIÃO]` Há um segundo problema de escopo que o cap. 04 §4 embaça.
  O resíduo `−M_eff²m²p_φβ₁′` do §3 é uma afirmação de **minisuperespaço**
  sobre o bracket das duas constraints de FRW `{ℋ_g, ℋ_f}` — que é a
  sombra da constraint de Bianchi, **não** o par de segunda classe que
  remove o BD. O BD vive no helicity-0 com dependência espacial; ele
  não existe no minisuperespaço. O repo sabe disso em um lugar
  (`posicionamento_literatura.md` §1, linha "nosso resultado é
  minisuperespaço") e desliza no outro (cap. 04 §4 apresenta W00 como
  suporte à Parte B sem marcar que são objetos diferentes). W00 é
  melhor que minisuperespaço — é k≠0 — mas continua linear.

**Gravidade: alta.** A arquitetura inteira da v2 (cap. 03 §5) depende
deste gate, e ele é o único item aberto que pode revertê-la por
completo. `[OPINIÃO]` Enquanto ele não fechar em 2a, o enunciado
correto do cap. 07 §4 deveria carregar a ressalva "no setor **linear**,
onde o BD é sabidamente invisível" — hoje ele carrega "no setor escalar
linear (ação quadrática)", o que é literalmente correto mas não avisa o
leitor de que a limitação é fatal para a pergunta feita.

**W2. `p_φ → 0` no pouso degenera a matriz de Dirac — e provavelmente
cruza zero periodicamente.** `[CONJECTURA, barata de testar]`

O corpus estabelece duas coisas que, juntas, produzem um risco que
ninguém nomeou:

- A obstrução `{ℋ_g, ℋ_f}|_{r★} = −M_eff²m²p_φβ₁′` só se anula se
  `p_φ = 0` ou `β₁′ = 0` (cap. 04 §3). `[REPO-n2a]`
- Pós-pouso, δχ tem fricção 3H e dispersão `ω² = k²/a² + U″` com
  U″(v) > 0 (cap. 07, Ato 3; `resultado_r7e_saude_interna.md` §3).
  `[REPO-n2a/2b]`

`ω² > 0` com fricção 3H é **oscilação amortecida** em torno de v, não
relaxação monótona. Numa oscilação, `p_φ` cruza zero uma vez por
meio-período. Se `p_φ` cruza zero, o determinante da matriz de Dirac
`det{Φ_a, Φ_b}` — que a modulação torna genericamente não-nulo — passa
por zero **periodicamente**. Nesses instantes o par de segunda classe
degenera: localmente as constraints viram de primeira classe, a
contagem de graus muda, e o sistema fica sobre uma superfície de
strong coupling (a expansão perturbativa perde invertibilidade, não a
teoria perde saúde — mas é exatamente onde artefatos numéricos e
patologias reais são indistinguíveis).

`[OPINIÃO]` Isto não é fatal a priori — pode ser um cruzamento suave de
medida zero, inócuo, como acontece em muitos sistemas com vínculos
dependentes do tempo. Mas é *exatamente* o tipo de estrutura em que o
Erratum-02 nasceu: um efeito pequeno, suave, com todos os sintomas de
física. E o teste é trivial: plotar `p_φ(t)` (equivalentemente `φ̇₋`)
ao longo da trajetória REF já integrada e contar cruzamentos de zero.
**Se cruza, o enunciado "a estrutura de vínculos aguenta o regime
não-fatorado" precisa de qualificação em cada cruzamento.**

**W3. A escolha "β₁ único" não é radiativamente estável — e é o pilar
duplo do projeto.** `[CONJECTURA fundamentada]`

A modulação mínima (`β₁(φ₋)`, demais constantes) faz dois trabalhos
simultâneos no corpus: é o **fator atenuante do Gate 2B**
(`gate2_ghost.md` §3.2: "reduz o termo novo a uma única contribuição —
o caso mais favorável possível") e é a **novidade defensável nº 2**
(`posicionamento_literatura.md` §1: "subclasse mínima (β₁ único) é
primeiro estudo dedicado"). Um único pressuposto sustentando os dois.

O problema: `[OPINIÃO]` não existe simetria que proteja "só β₁ depende
de φ₋". Os polinômios simétricos elementares `e_n(𝒦)` misturam-se sob
renormalização — loops de φ₋ com vértices vindos de
`β₁⁽⁰⁾(φ₋²/v★²) e₁(𝒦)` geram, ao inserir a expansão de 𝒦 em torno de
g = f, contribuições a `e₀, e₂, e₃, e₄` com dependência em φ₋. A massa
do gráviton em dRGT/HR é tecnicamente natural porque a simetria de
difeomorfismo é restaurada em m → 0 (padrão da EFT — ver discussão em
[arXiv:1408.1678](https://arxiv.org/abs/1408.1678) `[verificar]` para o
enunciado preciso), mas essa proteção é sobre a *escala global* m², não
sobre a **razão** entre β_n — e é precisamente a razão que a TDCP usa
para mover r★.

Consequências, em ordem de dureza:
1. Se `β₀,₂,₄` adquirem dependência em φ₋ por loop, o "caso mais
   favorável possível" do Gate 2B evapora e o cálculo tem de ser feito
   com β_n(φ₋) genéricos de qualquer forma.
2. A afirmação de novidade "subclasse mínima" vira uma afirmação sobre
   uma escolha de renormalização num ponto, não sobre uma teoria.
3. `[OPINIÃO]` **Recomendação estrutural:** fazer o Gate 2B com
   `β_n(φ₋)` genéricos desde o início. Se passar no caso genérico,
   passa no mínimo e o problema radiativo fica inócuo. Se só passar no
   mínimo, o resultado é frágil e deve ser apresentado como tal.

**W4. A saúde comprou a sobrevivência ao preço da falseabilidade.**
`[OPINIÃO sobre REPO-n2b]`

O balanço pós-R-7 é: banda morta (lnA de −8.4 a −14.7), ISW retirado,
dispersão retirada, canto-Akrami retirado, "nenhuma assinatura
observacional exótica no regime linear tardio deste brinquedo"
(`resultado_r7_cascata.md` §5.3). O que sobra de dinâmica não-trivial é
um transiente de `e^{+0.4}` — ganho de 50% num único modo no IR
profundo, autocurável, sem contaminação métrica. Isso é *nada*
observacionalmente.

O repo é honesto sobre isso, mas não tira a conclusão: `[OPINIÃO]` no
regime linear tardio, a F1 é hoje **empiricamente indistinguível de
ΛCDM + um escalar espectador**. A única previsão viva é `m_T/H₀ ≈ 2.3`
(R-8b), e ela é do setor tensorial — o setor que nunca dependeu da
modulação, do φ₋, nem da identificação normativa. Ou seja: **o único
resultado falseável do corpus não testa a TDCP; testa bigravity.** Isso
precisa estar dito no cap. 01 e no abstract do paper, ou um referee dirá
por vocês, com menos delicadeza.

**W5. "Cravado" é sobre-afirmação em R-8b.** `[OPINIÃO sobre REPO-n2b]`
A família varrida é `β_n → s·β_n` com U0 resolvido por s — um **dial de
1 parâmetro** num espaço de 5 (β₀..β₄), com a forma-β fixa. O doc
declara isso corretamente em §4 ("forma-β do benchmark sob rescala
uniforme"), mas o título e o §3.2 dizem "cravado" e "predição" sem
qualificador. O enunciado defensável é: *m_T/H₀ ∈ [2.26,2.41] ao longo
do dial de rescala uniforme, na forma-β do benchmark, no ramo conectado
ao benchmark*. Um referee derruba a versão sem qualificadores em uma
linha.

`[OPINIÃO — e esta é construtiva]` A razão pela qual isso funciona é
mais interessante que o número: o doc observa que "m_T²/H² é função só
de r ao longo da família de H fixo" (§2b), e r é raiz do cúbico do
fundo. Isso é a **mesma** estrutura que produz o `m_T²/H² → 12`
primordial (`posicionamento_literatura.md` §1). Enunciar isso como um
único teorema — *em bigravity com história de expansão fixada,
m_T²/H² é função apenas de r, e r é determinado algebricamente por
(Ω_m, forma-β); logo m_T/H nunca é livre* — é mais publicável que
qualquer dos dois números isolados, porque explica **por quê**, e
generaliza para além do dial testado. Recomendo fortemente.

**W6. U0 < 0 é o problema da constante cosmológica reintroduzido.**
`[OPINIÃO sobre REPO-n2b]` `resultado_r8b_limite_mH0.md` §3.1 registra
que alcançar o postulado m ~ 30–300 H₀ exige outra forma-β (V_f com
zero em r finito) **e** o ajuste fino U0 < 0, "vácuo-χ cancelando a
energia da interação". Chamemos pelo nome: isso é um Λ negativo
sintonizado contra a energia da interação bimétrica para produzir o H
tardio observado. A bigravity é frequentemente motivada como
auto-aceleração *sem* Λ ajustado; a sub-família que atinge o postulado
do corpus **piora** o balanço, com dois ajustes em vez de um. Não é
fatal — ΛCDM tem o mesmo problema — mas invalida qualquer alegação de
naturalidade nessa direção, e o paper deve declarar isso antes que
alguém pergunte.

**W7. Risco sistemático residual: uma trajetória, um integrador de 1ª
ordem efetiva.** `[REPO-n2b, declarado]` `resultado_r7e_saude_interna.md`
§5 registra: fundos Heun vs Euler diferem ~2e-3 na janela, o lnA do
pousado herda ±O(1), e a cadeia rp do Heun é ainda de 1ª ordem
(M0 ≈ 3.1e-4). As margens atuais (10+ unidades log) tornam BANDA-MORTA
insensível, e isso está corretamente dito. `[OPINIÃO]` O risco não é
para os vereditos atuais — é para o **próximo** resultado marginal, que
virá do R-8 (C_ℓ/P(k)), onde as margens não serão de 10 unidades log.
Fechar o housekeeping do integrador **antes** do R-8, não depois.

**W8. Volume de amostragem não é rota independente — e o corpus ainda
confunde os dois.** `[OPINIÃO]` O no-go anterior tinha ~1500 pontos de
varredura 4D e estava inteiramente errado (cap. 07, Ato 1 → Ato 2). O
enunciado atual apoia-se em ≈ 2×24k + 8×14k + 4×14k pontos + 17 células
(`resultado_r7e_saude_interna.md` §6.2). A lição do Erratum-02 é
literalmente que **erro sistemático de pipeline é invariante sob
amostragem**. O que protege é rota independente, e a única rota
verdadeiramente independente do corpus até hoje veio de fora (a
reauditoria ADM). O V-XREP-b (Γ–Γ vs ADM) é a resposta certa; o
erratum §6.2 o declara obrigatório "a cada mudança da maquinaria de
redução". `[OPINIÃO]` Endureça: **obrigatório para cada resultado que
entra no paper**, independentemente de a maquinaria ter mudado.

**W9. EFT — o que está seguro e o que não está.** `[OPINIÃO + n3]`
Com m ~ H₀, a escala de strong coupling em torno de Minkowski é
Λ₃ = (m²M_Pl)^{1/3} ≈ 1.3×10⁻¹³ eV ≈ (1.5×10³ km)⁻¹
(consistente com a literatura padrão da classe `[verificar]`).
Balanço honesto:
- **Seguro:** todo o trabalho linear cosmológico do repo (kh ~ 0.3–450;
  k = 0.05–0.15 h/Mpc no R-8b) vive ~18 ordens de grandeza abaixo de
  Λ₃ em energia. A validade EFT do tratamento linear **não é um
  problema** e o corpus não precisa se defender aí.
- **Não coberto:** o raio de Vainshtein do Sol é
  r_V ~ (r_s/m²)^{1/3} ~ 10¹⁵–10¹⁶ km ~ 0.1 Mpc — todo teste local está
  *dentro* dele, e nada no corpus trata do regime Vainshtein. Qualquer
  frase sobre compatibilidade com testes de sistema solar é hoje sem
  base no repo.
- **Não estimado e potencialmente pior:** a modulação introduz uma
  escala nova, v★. Os vértices mistos π–φ₋ vindos de
  `(m²M_eff²/v★²) φ₋² e₁(𝒦)` têm sua própria escala de strong coupling,
  e `[CONJECTURA]` ela é *menor* que Λ₃ quando v★ ≪ M_eff. Como o
  corpus roda com v★ = 1 em unidades internas, **ninguém sabe onde essa
  escala está em unidades físicas**. Isso deve ser estimado antes de
  qualquer alegação de consistência EFT da modulação (proposta P4).

**W10. O ramo algébrico está deferido com "prior de artefato".**
`[REPO, declarado]` Tanto o cap. 07 §4 quanto
`resultado_r7e_saude_interna.md` §6.4 listam o ramo algébrico como
pendência com "prior de artefato, sem afirmação". `[OPINIÃO]` O prior é
provavelmente certo — a fenomenologia publicada do "branch 1"
(cinética evanescente, strong coupling, sem grau extra no linear:
1111.1983, 1202.1986, 1403.5679 via `posicionamento_literatura.md` §1)
sustenta-o. Mas nomear um prior não é o mesmo que testá-lo, e este é o
ramo onde a TDCP originalmente vivia. Deixar assim é aceitável; vendê-lo
como fechado, não.

---

## Propostas de modelagem

Em ordem de execução recomendada. Cada uma com critério de falha
pré-declarado, no espírito do método do projeto.

### P1 — `p_φ(t)` cruza zero? (custo: horas; risco de desmontar W2: alto)

Plotar `φ̇₋(t)` / `p_φ(t)` ao longo da trajetória REF já integrada
(g=2, m30, v★=1) e contar cruzamentos de zero após o pouso. Se a
condensação termina em oscilação amortecida (o que `ω² = k²/a² + U″>0`
com fricção 3H sugere), há cruzamentos periódicos, e em cada um a
obstrução `p_φβ₁′` se anula: a matriz de Dirac degenera.

- **Falha (risco confirmado):** ≥ 1 cruzamento de zero de `p_φ` após o
  pouso ⇒ o enunciado do cap. 04 §3/§4 precisa de qualificação, e o
  Gate 2B tem de ser feito **também** na vizinhança do cruzamento, não
  só na janela de deslocamento.
- **Passa:** `p_φ` decai monotonicamente sem cruzar (relaxação
  overdamped) ⇒ risco W2 fechado, e o corpus ganha uma frase forte:
  "a estrutura de vínculos é uniformemente não-degenerada ao longo da
  trajetória".

### P2 — O diff diagonal continua de primeira classe? (custo: 1 sessão simbólica; poder: alto)

Este é o teste que falta e que a "terceira estrutura" torna urgente.
Com `{ℋ_g, ℋ_f} ≠ 0` genericamente (cap. 04 §3), a contagem sobrevive
sem drama — segunda classe remove graus em pares. O que **não** é
automático é que a combinação geradora do difeomorfismo temporal
diagonal permaneça de primeira classe. Calcular, na estrutura de
minisuperespaço já validada (`gate2_bracket.py` / `gate2_fatoracao.py`):

```
ℋ_diag = ℋ_g + ξ ℋ_f ,    ℋ_rel = ℋ_g − ξ ℋ_f
{ℋ_diag , ℋ_rel} =? combinação linear de constraints
```

com β₁ = β₁(φ₋) e p_φ ≠ 0.

- **Falha:** `{ℋ_diag, ℋ_rel}` contém termo que não é proporcional a
  nenhuma constraint ⇒ **o difeomorfismo diagonal está quebrado pela
  modulação**. Isso mataria a arquitetura de forma mais direta e mais
  rápida que o BD, porque é a simetria que define a teoria. Nível de
  gravidade: terminal.
- **Passa:** fecha na álgebra ⇒ a "terceira estrutura" é benigna, e o
  corpus ganha o enunciado preciso que hoje falta: *a modulação
  converte o par (algébrico ∪ cinemático) em um único par de segunda
  classe deformado, preservando a simetria diagonal*.

`[OPINIÃO]` Esta é a proposta com melhor razão custo/informação de
todas. Faça-a antes do ADM completo.

### P3 — O Gate 2B, feito direito (custo: a "sessão dedicada" já prevista; é o item que destrava tudo)

`gate2_ghost.md` §6 já lista os ingredientes. Acrescento a estrutura do
cálculo e onde estão as armadilhas.

**Setup.** ADM completo, ambas as métricas dinâmicas, dependência
espacial retida. Redefinição de shift de Hassan–Rosen
([1109.3515](https://arxiv.org/abs/1109.3515); a demonstração explícita
da secundária está em Hassan–Rosen–Schmidt-May,
[arXiv:1111.2070](https://arxiv.org/abs/1111.2070) — *Confirmation of
the Secondary Constraint and Absence of Ghost in Massive Gravity and
Bimetric Gravity*). **Verificação prévia barata:** confirmar que a
redefinição `D^i_j` é puramente geométrica (função de γ, f) e
**independente dos β_n** — se for, a Parte A sobe de minisuperespaço
para ADM completo de graça.

**O objeto certo não é `{𝒞, H}`, é `{𝒞(x), 𝒞(y)}`.** Este é o ponto que
`gate2_ghost.md` §3 formula de maneira que pode desviar o cálculo. Em
HR, após eliminar os shifts auxiliares, `H = ∫ [N 𝒞_g + M 𝒞_f + …]` com
𝒞 independente dos lapsos. A secundária vem de
`𝒞̇ = ∫ N(y){𝒞(x),𝒞(y)}`; ela é constraint (e não equação para o
lapso) precisamente porque o bracket **não** é proporcional às
constraints e a condição vale para todo N. Com matéria minimamente
acoplada a g e modulação:

```
𝒞_tot = 𝒞_grav[γ,π,f ; β_n(φ₋)] + ℋ_φ[φ,π_φ,γ]
{𝒞_tot(x),𝒞_tot(y)} = {𝒞_grav,𝒞_grav}_HR
                     + [{𝒞_grav(x),ℋ_φ(y)} + (x↔y)]   ← termo NOVO
                     + {ℋ_φ,ℋ_φ}_álgebra de hipersuperfície
```

**Previsão do revisor** `[CONJECTURA, e é a boa notícia]`: a parte
**ultralocal** do termo novo cancela por antissimetria. Escrevendo
`A ≡ ∂𝒞_grav/∂φ₋ = Σ_n β_n′(φ₋) ∂𝒞/∂β_n` e
`B ≡ {φ₋, ℋ_φ} = π_{φ₋}/√γ`, a contribuição ultralocal é
`A(x)B(y)δ(x−y) − A(y)B(x)δ(x−y) ≡ 0`. É o mesmo mecanismo pelo qual
MVMG ([1206.5678](https://arxiv.org/abs/1206.5678)) preserva o par.
Se isso se confirmar, ~90% do medo do Gate 2B evapora numa página.

**Onde o gate realmente se decide** `[CONJECTURA]`: nos termos com
`∂_i δ(x−y)`, que **não** cancelam por antissimetria. Eles vêm de duas
fontes: (i) o gradiente espacial `√γ γ^ij ∂_iφ₋ ∂_jφ₋ /2` dentro de
ℋ_φ, cujo bracket com a dependência de 𝒞_grav em γ_ij produz termos
∝ `∂_iφ₋`; (ii) a dependência de 𝒞_grav em φ₋ contra a dependência de
ℋ_φ em γ. **Critério de falha:** se o resíduo de derivada de δ **não**
for proporcional a `𝒞_tot`, `𝒞_f` ou ao vínculo de momento `H_i`, então
`𝒞̇ = 0` deixa de ser constraint independente do lapso e o BD volta —
Gate 2B FALHA, e vale a rota (a) de `gate2_ghost.md` §5 (procurar a
condição sobre `∂β_n/∂φ₋` que anula o resíduo).

**Duas exigências de escopo, não negociáveis:**
1. Fazer com `β_n(φ₋)` **genéricos**, não só β₁ (razão: W3). O caso
   mínimo é corolário.
2. Comparar explicitamente com os três vizinhos, porque a literatura
   tem resultados nos dois sentidos e a diferença está na estrutura:
   MVMG passa ([1206.5678](https://arxiv.org/abs/1206.5678)); extended
   quasidilaton falha ([1309.2146](https://arxiv.org/abs/1309.2146));
   **Generalized Massive Gravity** (Gumrukcuoglu–Heisenberg–Mukohyama,
   [arXiv:1410.0960](https://arxiv.org/abs/1410.0960) `[verificar]`) é
   o análogo estruturalmente mais próximo — β_n promovidos a *funções*,
   com condições sobre as funções — e está **subutilizado** no
   `posicionamento_literatura.md`. E chameleon bigravity
   ([1702.04490](https://arxiv.org/abs/1702.04490)) é a classe-irmã
   cuja análise hamiltoniana **nunca foi feita**: essa lacuna é a
   oportunidade de publicação mais limpa do projeto, e P3 a fecha de
   passagem.

### P4 — Falsificação barata via limite de decoupling (custo: médio; alternativa a P3 se P3 empacar)

Escrever o limite de decoupling da F1 com β₁(φ₋): `M_Pl → ∞`, `m → 0`,
`Λ₃ = (m²M_Pl)^{1/3}` fixo, retendo o helicity-0 π e o φ₋. O BD, quando
presente, aparece como termo com derivadas superiores em π que **não**
é derivada total.

- **Falha:** aparece `(□π)²`-type sem estrutura total-derivative ⇒ BD
  confirmado, Gate 2B falha, sem precisar de ADM.
- **Passa:** estrutura total-derivative preservada ⇒ evidência forte
  (não prova) para 2B, e — o bônus — **saem as escalas de strong
  coupling do setor misto π–φ₋ em função de v★**, resolvendo W9.

### P5 — Estabilidade radiativa da modulação mínima (custo: baixo-médio)

Computar a mistura de operadores a um loop: com o vértice
`(m²M_eff²/v★²) φ₋² e₁(𝒦)`, um loop de φ₋ gera contribuições a
`e₀, e₂, e₃, e₄` com dependência em φ₋?

- **Falha:** sim, gera ⇒ "β₁ único" é uma escolha num ponto de
  renormalização, não uma teoria; o Gate 2B **precisa** ser genérico
  (já é a exigência de P3) e a alegação de novidade
  ("subclasse mínima") deve ser reescrita.
- **Passa:** não gera (existe simetria protetora) ⇒ **descoberta**: a
  simetria que protege a modulação diferencial é um resultado por si
  só, e resolve o problema de naturalidade da classe inteira. `[OPINIÃO]`
  Considero improvável, mas o payoff assimétrico justifica o custo.

### P6 — Posto de `f` composta: o teste que pode matar a rota de emergência numa tarde (custo: horas)

Rota de derivação mais direta para o cap. 08: `f_μν` construída dos
campos primordiais,
`f_μν = c₀ g_μν + c₁ ∂_μφ₁∂_νφ₁ + c₂ ∂_μφ₂∂_νφ₂ + c₃ ∂_{(μ}φ₁∂_{ν)}φ₂`.

- **Falha (previsão minha)** `[CONJECTURA]`: com **apenas dois**
  escalares, o tensor `∂_μφ_a ∂_νφ_b` tem posto ≤ 2. Logo
  `𝒦 = √(g⁻¹f)` tem **espectro degenerado** — no máximo dois autovalores
  distintos de 1 — e os `e_n(𝒦)` colapsam numa subfamília com relações
  algébricas fixas entre si. O potencial HR degenera; provavelmente
  recai no ramo algébrico. Se confirmado, isto é **fatal para a rota
  "f_μν composta de (φ₁,φ₂)"** e é conhecível em uma tarde de álgebra
  simbólica com a maquinaria existente.
- **Consequência construtiva se falhar:** a TDCP precisa de **quatro**
  campos primordiais (os φ^a de Stückelberg), não dois — φ₋ passa a ser
  o modo diferencial de uma estrutura interna maior (p.ex. dois dubletos
  complexos com U(1)×U(1) → U(1)_diag). Isso não destrói a narrativa da
  bifurcação; reformula-a, e **melhora** o alinhamento com o análogo
  2-BEC que o corpus já cita.
- **Passa:** posto suficiente ⇒ rota viva, e segue-se ao critério
  anti-circularidade (nomear os geradores quebrados: se forem difeos
  relativas, é F1 renomeada — `gate1c` §3).

### P7 — Derivar a modulação (não a métrica): integrar out um setor pesado (custo: médio)

Meta mais modesta que P6 e mais alcançável: aceitar f fundamental e
**derivar** `β_n(φ₋)` integrando um campo pesado Χ com massa `M(φ₋)`
acoplado às duas métricas. A contribuição de um loop pesado gera termos
no potencial de interação com coeficientes calculáveis.

- **Falha (previsão minha)** `[CONJECTURA]`: a contribuição de loop de
  um campo acoplado covariantemente tende a aparecer como um **fator
  global** `F(φ₋)·√(-g)·(função de 𝒦)`, sem preferência por n — e o
  cap. 03 §0 provou que fator global **não move a raiz**. Se isso se
  confirmar, o resultado é forte e negativo: **a modulação diferencial
  é estruturalmente não-Wilsoniana** — não se obtém integrando graus
  pesados, tem de ser postulada. Isso seria um achado publicável e uma
  restrição séria à arquitetura.
- **Passa:** aparece dependência diferencial (razões β_i/β_j movidas)
  ⇒ **a modulação deixa de ser decreto e vira derivação**, e o cap. 08
  ganha seu primeiro elo derivado. Este é o maior prêmio disponível no
  projeto hoje.

### P8 — O teorema `m_T²/H² = função(r)` (custo: baixo; alto retorno editorial)

Generalizar as duas observações isoladas (`m_T²/H² → 12` primordial;
`m_T/H₀ ≈ 2.3` hoje) num enunciado único: *fixada a história de
expansão, `m_T²/H²` depende apenas de r; r é raiz algébrica determinada
por (Ω_m, forma-β); portanto `m_T/H` não é parâmetro livre em nenhuma
época.* Inclui o item D3 do `posicionamento_literatura.md` (o "12" é da
era de matéria; refazer com radiação) como corolário.

- **Falha:** existe dependência residual em algo além de r ⇒ os dois
  números são coincidências da família testada, e ambos perdem força.
- **Passa:** o corpus troca dois números frágeis por um teorema
  robusto, com a fronteira honesta embutida na própria estrutura.

---

## Veredito do especialista

A F1 é hoje uma implementação **internamente sã e corretamente
auditada** de uma identificação que continua sendo decreto — e o
corpus diz exatamente isso, o que é o comportamento certo. O Erratum-02
e o método que o produziu (prova de identidade de ação, V-XREP-b,
tabela de supersessão) valem mais que qualquer resultado numérico do
projeto e são o que me faz acreditar no resto. Mas o Gate 2B continua
aberto e é mais grave do que o corpus pesa: o suporte 2b é do tipo
errado, não do tamanho errado, e nunca passou pelo auto-teste de poder
de detecção que o próprio método exige. Somem-se dois riscos que não
constam do repo — `p_φ` cruzando zero no pouso, e a instabilidade
radiativa da escolha "β₁ único", que é simultaneamente o fator
atenuante do gate e a novidade reivindicada. Recomendação: **P1 e P2
imediatamente** (horas a uma sessão, poder de falsificação alto), **P3
com β_n genéricos** antes de qualquer submissão, e o reconhecimento
explícito de que, pós-R-7, a única previsão falseável viva (`m_T/H₀ ≈
2.3`) testa bigravity, não a TDCP. Publicável como estudo de classe —
com a lacuna hamiltoniana do chameleon bigravity como gancho — assim
que 2B fechar em 2a; não antes.
