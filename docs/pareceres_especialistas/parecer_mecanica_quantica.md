# Parecer — Fundamentos Quânticos

**Autor:** revisor externo independente (fundamentos quânticos, QFT em
espaços curvos, cosmologia de defeitos e flutuações primordiais).
**Data:** 2026-08-13. **Base de leitura:** `manuscript-v2/01_tese.md`,
`03_acao_e_dicionario.md`, `07_setor_escalar.md` (§3–4),
`08_identificacao_normativa.md`; `docs/gate1c_nota_trilema.md`;
`docs/gate1_identidade_relacional.md` (§1–4); `integration_assessment.md`;
`docs/resultado_r7_cascata.md` §4.
**Regra de citação obedecida:** nenhum número anterior a 2026-08-12 é
tratado como vigente (filtro de supersessão de `resultado_r7_cascata.md` §4).

**Convenção deste parecer:** `[REPO]` = derivado/medido no repositório, com
fonte; `[LIT]` = literatura externa; `[MEU]` = conta ou julgamento meu,
feito aqui pela primeira vez, não auditado pelo repositório;
`[verificar]` = referência ou número que o autor deve conferir.

---

## Resumo executivo (10 linhas)

1. A bifurcação da TDCP é, como escrita em `03_acao_e_dicionario.md`, uma
   quebra espontânea de uma Z₂ **global, discreta e exata** — inclusive no
   setor de matéria, que não toca φ.
2. Toda Z₂ discreta global quebrada espontaneamente forma **paredes de
   domínio**; o problema de Zel'dovich–Kobzarev–Okun é obrigatório, e o
   repositório **nunca o menciona** (zero ocorrências de "parede de
   domínio", "Kibble", "Zurek", "Zel'dovich" no corpus). `[REPO/MEU]`
3. O vínculo novo que isto impõe é dimensional e simples:
   σ ≈ (2√2/3)·μ₋³/λ₋ ≲ (1 MeV)³, salvo bias explícito ou diluição
   inflacionária. A TDCP nunca fixou a escala de μ₋ — logo não sabe se
   está dentro ou fora do vínculo. `[MEU]`
4. Existem três saídas viáveis, e uma delas é quase gratuita (bias
   suprimido por M_Pl); mas a saída padrão colide de frente com a exigência
   declarada em `03_acao_e_dicionario.md` §1 (Z₂ exata).
5. O potencial V(φ₊,φ₋) escolhido é, termo a termo, o de **inflação
   híbrida** com φ₋ como campo waterfall Z₂ — a família de modelos onde o
   problema de paredes é clássico e conhecido. `[MEU/LIT]`
6. Ninguém é o inflaton no corpus: φ₊ é candidato natural mas V₊ é
   declarado "entrada do modelo", e δφ₊ **não aparece** na redução do setor
   escalar (2 DOFs = modo métrico + δφ₋) — falta o modo que carrega ζ.
7. O sinal de ⟨φ₋⟩ é, nesta ação, **acoplado a nada**: β_n depende de φ₋².
   Consequência quântica não trivial: o ambiente não decohere o sinal, e as
   paredes são a única manifestação observável da escolha.
8. A "correlação primordial φ₁–φ₂" tem conteúdo quântico exato e barato de
   calcular: o vácuo é gaussiano de dois modos, com emaranhamento
   ξ = (√ω₊−√ω₋)/(√ω₊+√ω₋), que **diverge no ponto crítico** da bifurcação.
   Este é o primeiro cálculo quântico a fazer.
9. Dos Anexos I–K, o que é recuperável é exatamente isso (emaranhamento
   gaussiano derivado da ação); o que não é recuperável é Λ_ent — entropia
   não gravita, ⟨T_μν⟩ gravita, e o mapa S_ent → T_μν não existe.
10. A quantização é legítima só como EFT: o corte Λ₃=(m²M_Pl)^{1/3} dá
    Λ₃/H ≈ 2.3·(M_Pl/H)^{1/3} ~ 10² no primordial — há margem, mas Bunch–Davies
    em k/a→∞ está formalmente fora do domínio de validade. `[MEU]`

---

## Pontos fortes

**F1 — A Z₂ é a formulação certa do conceito, e é honesta.**
`manuscript-v2/03_acao_e_dicionario.md` §2 substitui a narrativa vaga de
"bifurcação" por um enunciado técnico verificável: Z₂ como troca φ₁↔φ₂,
parâmetro de ordem ⟨φ₋⟩, ponto crítico φ₊,crit² = μ₋²/(2λ_c), condensado
v²(φ₊) = (μ₋²−2λ_cφ₊²)/λ₋. Isso é SSB de livro-texto, corretamente posta, e
transforma uma metáfora em objeto de cálculo. Do ponto de vista de
fundamentos, é o passo mais valioso da v2: uma vez escrita como Z₂ global
discreta, a teoria fica sujeita a toda a maquinaria conhecida — inclusive
às suas obrigações (ver R1).

**F2 — A exigência de paridade em φ₋² é derivada, não estética.**
`03_acao_e_dicionario.md` §1 justifica β₁(φ₋) ∝ (1+φ₋²/v★²) porque uma
dependência linear quebraria a Z₂ explicitamente. Está correto, e o
argumento de §0 (o fator global F cancela na razão β₁/β₂, logo a modulação
tem de ser diferencial) é uma observação estrutural genuína — degenerescência
de forma, não erro de conta. `[REPO]`

**F3 — O critério anti-circularidade do G1-c é metodologicamente superior
ao que se vê na literatura de gravidade emergente.**
`docs/gate1c_nota_trilema.md` §3 obriga qualquer construção do braço (b) a
**nomear os geradores quebrados** antes de reivindicar emergência, e
antecipa o modo de falha real: "o modo mais provável de o programa R2
falhar não é dar errado: é dar certo de volta para dentro da F1". Isso é
raro e correto. A demolição parcial de Weinberg–Witten (Phys. Lett. B96
(1980) 59) também está certa: o teorema proíbe |h|>1 **sem massa**, e a
f₂(1270) é o contraexemplo experimental para spin-2 massivo composto.
`[REPO/LIT]`

**F4 — A derivação de Stückelberg de §9 do G1-c é um resultado quântico de
verdade, e o repositório subestima seu alcance.**
A identificação medida (taquião de k=1 = π_L com sobreposição 0.995+;
fantasma da fresta = π⁰ puro, 0.998) é exatamente o tipo de evidência que
torna o argumento de circularidade um resultado e não uma analogia. E o
refinamento — a doença vive no **balanço** quebra×EH, com cancelamento de
~0.5–1% — é a informação de projeto mais útil do documento inteiro: exclui
toda uma classe de curas. `[REPO]`

**F5 — `integration_assessment.md` fez, em 2026, o diagnóstico correto dos
Anexos I–K, com o argumento técnico certo.**
A Pergunta 2 identifica que L_int = λχ(g⁽¹⁾−g⁽²⁾)² sem a contração de
Fierz–Pauli reintroduz o fantasma de Boulware–Deser, e que e_n(𝒦) não é
recuperável de uma expressão quadrática em (g⁽¹⁾−g⁽²⁾). Isso é
tecnicamente correto e é o argumento decisivo (Fierz–Pauli 1939;
de Rham–Gabadadze–Tolley arXiv:1011.1232; Hassan–Rosen arXiv:1109.3515).
A decisão de manter I–K fora do corpo principal está bem fundamentada.
`[REPO/LIT]`

**F6 — O espectador δφ₋ está caracterizado com dispersão explícita, o que
torna o cálculo do espectro primordial imediato.**
`manuscript-v2/07_setor_escalar.md` §3 dá fricção 3H e ω² = k²/a² + U″,
com âncoras analíticas fechando em 0.01–0.02. É exatamente a forma de um
campo espectador em FLRW: nada exótico precisa ser construído para
quantizá-lo — a normalização de Bunch–Davies e a evolução de modo são
padrão. Esse é o ponto de entrada barato para a física quântica primordial
da teoria. `[REPO]`

**F7 — m_T²/H² → 12 no primordial é uma predição de valor quântico
subaproveitada.**
`manuscript-v2/06_setor_tensorial.md` §(caixa) dá m_T/H ≈ 3.5 no regime
primordial, universal no benchmark. Isso põe o spin-2 massivo na **série
principal** de de Sitter (bem acima do limite de Higuchi m²≥2H²;
Higuchi, Nucl. Phys. B282 (1987) 397) — o regime em que a partícula deixa
assinatura oscilatória no biespectro. Ver P3: é a predição observacional
mais específica que a teoria pode oferecer e ainda não pediu. `[REPO/LIT]`

---

## Pontos fracos e riscos

### R1 — **PAREDES DE DOMÍNIO: o problema não tratado, e o achado central deste parecer.**

**O fato.** Uma Z₂ discreta global quebrada espontaneamente produz, no
universo em expansão, uma rede de paredes de domínio separando as regiões
com ⟨φ₋⟩=+v e ⟨φ₋⟩=−v (Kibble, J. Phys. A9 (1976) 1387; Zurek, Nature 317
(1985) 505). Paredes diluem como ρ_wall ∝ a⁻¹ na solução de escala —
mais lentamente que matéria e radiação — e portanto **dominam** o universo,
salvo remoção. O vínculo clássico é
σ ≲ (1 MeV)³ (Zel'dovich, Kobzarev & Okun, Sov. Phys. JETP 40 (1975) 1
[ZhETF 67 (1974) 3]; revisão moderna: Saikawa, *Universe* 3 (2017) 40,
arXiv:1703.02576). `[LIT]`

**O estado do repositório.** Busca no corpus inteiro (`*.md`): zero
ocorrências de "parede de domínio"/"domain wall", "Kibble", "Zurek",
"Zel'dovich". A única ocorrência de "parede" é `docs/resultado_gatef_a.md`
em sentido não relacionado ("parede de normalização"). **O problema nunca
foi levantado.** `[REPO — verificação minha, 2026-08-13]`

**Por que aqui é pior que no caso genérico.** A Z₂ desta ação é exata em
sentido forte: V é par em φ₋; os β_n dependem de φ₋²; e a matéria acopla
**só a g**, sem tocar φ₁ ou φ₂. Logo não existe, dentro da teoria como
escrita, **nenhum** setor capaz de quebrar a Z₂ nem sequer explicitamente
por um pequeno termo — a estabilidade topológica das paredes é exata. Além
disso `03_acao_e_dicionario.md` §1 **veta explicitamente** a quebra
explícita ("uma dependência linear quebraria a Z₂ explicitamente — e a
bifurcação deixaria de ser bifurcação"), ou seja, a teoria já fechou, por
decisão de projeto, a saída padrão do problema. `[REPO/MEU]`

**A conta que falta, e o vínculo novo.** Para V(φ₋) = −½μ₋²φ₋² + ¼λ₋φ₋⁴,
com v = μ₋/√λ₋ e m_{φ₋} = √2 μ₋, a tensão do kink é

> σ = (2√2/3)·√λ₋·v³ = (2√2/3)·μ₋³/λ₋ = (2/3)·m_{φ₋}·v²

e o vínculo de Zel'dovich exige, na ausência de bias e de diluição,

> **(2√2/3)·μ₋³/λ₋ ≲ (1 MeV)³  ⟹  μ₋ ≲ λ₋^{1/3} MeV.** `[MEU]`

Há ainda uma contribuição gravitacional própria desta teoria: no núcleo da
parede φ₋=0, logo β₁=β₁⁽⁰⁾ e r★=r★⁽⁰⁾, enquanto no volume β₁ é modulado e
r★ é maior. **A parede é, literalmente, uma folha onde a bifurcação é
desfeita** — uma descontinuidade da separação estrutural r. Isso adiciona
δσ ≈ m²M_eff²·β₁⁽⁰⁾·(v²/v★²)·e₁(𝒦)·w, com w ~ 1/m_{φ₋}. Com m ~ H₀ essa
parcela é da ordem de ρ_Λ·w e é desprezível; a parcela dominante é a
escalar acima. `[MEU]`

**O ponto crucial: a TDCP não sabe em que corner do vínculo está.** μ₋, λ₋
e v★ são entradas livres; o benchmark de `manuscript-v2/05_fundo_ramo_finito.md`
trabalha em unidades de código com v★=1. Sem uma âncora dimensional, a
teoria não pode afirmar que passa nem que falha. **Este é, na minha
avaliação, o vínculo quantitativo mais forte que se pode impor à TDCP hoje
com uma conta de dez linhas.** `[MEU]`

**As três saídas, avaliadas.**

- **(S1) Bias suprimido por Planck — a saída recomendada, e quase
  gratuita.** A conjectura de ausência de simetrias globais exatas em
  gravidade quântica (Banks & Seiberg, PRD 83 (2011) 084019,
  arXiv:1011.5120) prevê operadores tipo δV ~ c·φ₋⁵/M_Pl que levantam a
  degenerescência. Pelo critério de Gelmini, Gleiser & Kolb (PRD 39 (1989)
  1558), as paredes colapsam em t_ann ~ σ/V_bias. Com μ₋ ~ 10¹³ GeV, λ₋~1 e
  V_bias ~ v⁵/M_Pl, obtém-se t_ann ~ λ₋^{3/2}·M_Pl/μ₋² ~ 10⁻³² s — as
  paredes desaparecem essencialmente na formação. **Para escalas altas, o
  problema se resolve sozinho.** O custo é declaratório, não físico: a
  linha "Z₂ … exata na ação" da tabela de simetrias de
  `03_acao_e_dicionario.md` §2 precisa virar "exata até operadores
  suprimidos por M_Pl", e o texto de §1 precisa distinguir **bias em V**
  (inofensivo para r★) de **modulação linear em β_n** (que é o que
  destruiria a bifurcação). Esses dois são hoje confundidos no manuscrito.
  `[MEU/LIT]`
- **(S2) Diluição inflacionária — provavelmente já operante, mas não
  demonstrada.** Se a travessia φ₊ → φ₊,crit ocorre durante inflação e ≳60
  e-folds antes do fim, os domínios são inflados para fora do volume
  observável. `docs/resultado_investigacao2_faseA.md` menciona rolagem de
  ~80 e-folds — **mas o repositório nunca declara se esses e-folds são
  inflacionários**, e a estrutura híbrida (R2) sugere o contrário: no
  potencial escrito, a travessia do crítico é o *waterfall*, que
  tipicamente **termina** a inflação, não a precede por 60 e-folds. Se o
  waterfall é o fim da inflação, S2 **não está disponível**. Isso precisa
  ser resolvido explicitamente. `[REPO/MEU]`
- **(S3) Domínios super-horizonte por transição lenta.** Se a transição é
  adiabática e |U″| ≪ H² por muitos e-folds, a inflação estocástica
  (Starobinsky & Yokoyama, arXiv:astro-ph/9407016) gera domínios de
  tamanho ~e^N H⁻¹, possivelmente maiores que o volume observável — sem
  paredes dentro do horizonte. É a saída mais elegante, mas tem preço
  observacional: deixa um **gradiente super-horizonte de ⟨φ₋⟩**, isto é,
  uma modulação dipolar/assimetria hemisférica da amplitude das
  perturbações, que é diretamente testável no CMB. Não é uma saída grátis:
  é uma predição. `[MEU/LIT]`

**Gravidade do achado.** Não é fatal — S1 e S3 funcionam — mas é **grave
como omissão**: uma teoria que se apresenta como "SSB de Z₂ discreta com
parâmetro de ordem ⟨φ₋⟩" e não discute paredes de domínio será rejeitada
em qualquer arbitragem de cosmologia na primeira leitura. Recomendo tratar
isto como bloqueio de publicação, não como refinamento.

### R2 — O potencial escolhido é inflação híbrida, e o repositório não sabe disso.

V(φ₊,φ₋) = V₊(φ₊) − ½μ₋²φ₋² + ¼λ₋φ₋⁴ + λ_cφ₊²φ₋² é, termo a termo, o
potencial de inflação híbrida (Linde, PRD 49 (1994) 748,
arXiv:astro-ph/9307002 [verificar]) com φ₋ como campo *waterfall* e
φ₊ como campo lento. Isso tem três consequências não registradas:
(i) o waterfall é **preaquecimento taquiônico** — a instabilidade espinodal
é violenta e não perturbativa (Felder et al., PRL 87 (2001) 011601,
arXiv:hep-ph/0012142), logo o enunciado de `07_setor_escalar.md` §3 de que
o espectador "ganha no máximo e^{+0.4} no IR profundo, autocurável" é um
resultado **linear, sobre uma trajetória REF tardia**, e não pode ser lido
como ausência de formação de domínios na transição primordial;
(ii) na literatura de híbrida, um waterfall Z₂ é justamente a variante que
se evita, por causa das paredes — usa-se campo complexo/carregado;
(iii) λ_c precisa ser O(1) para que φ₊,crit seja da ordem do campo em
rolagem, o que é um acoplamento direto grande entre o "inflaton" e o
waterfall — problema-η em potencial. `[MEU/LIT]`

### R3 — Não há inflaton identificado, e δφ₊ está ausente da redução escalar.

`03_acao_e_dicionario.md` §5 declara V₊(φ₊) "entrada do modelo (a
bifurcação só exige φ₊ decrescente)". Ao mesmo tempo,
`07_setor_escalar.md` §3 descreve o sistema físico como **dois** DOFs:
"modo métrico Ẽ = k²E_f + espectador δφ₋". Ou seja: **δφ₊ não é carregado
pela cascata de perturbações.** Se φ₊ é o inflaton, δφ₊ é precisamente o
modo que gera ζ; se não é, a teoria não diz quem gera ζ. Em ambos os casos,
o corpus não tem hoje nenhum caminho para o espectro de curvatura — e sem
isso não há como falar de "flutuações primordiais" da TDCP. Nenhuma
afirmação sobre n_s, A_s ou isocurvatura é possível no estado atual.
`[REPO — inferência de leitura; confirmar contra `docs/resultado_r7_cascata.md`]`

### R4 — O sinal de ⟨φ₋⟩ é acoplado a nada: o ambiente não pode decoherê-lo.

Como β_n depende de φ₋² e a matéria não toca φ, **nenhum observável local
distingue +v de −v**. Isso tem consequências de fundamentos que a TDCP
deveria enunciar e não enuncia:
(i) o programa usual de decoerência (Kiefer & Polarski, arXiv:0810.0087;
Burgess, Holman & Hoover, arXiv:astro-ph/0601646; Nelson,
arXiv:1601.03734) atua sobre a **amplitude do campo**, não sobre o rótulo
de sinal, e o setor gravitacional é cego a esse rótulo em primeira ordem;
(ii) o que decohere e classicaliza é a configuração espacial δφ₋(x) — e é
exatamente ela que define a rede de domínios. Isto é, a decoerência
primordial **produz** o problema R1 em vez de resolvê-lo;
(iii) não há mecanismo dinâmico algum, nesta ação, capaz de selecionar um
sinal **global**. Qualquer texto que sugira "o universo escolheu um ramo"
está descrevendo algo que a teoria não implementa. `[MEU]`

### R5 — O aparato de colapso dos Anexos I–K é justamente o que seria preciso para evitar R1, e é justamente o que não está disponível.

|Ψ⟩ = α|g₁⟩ + β|g₂⟩ com colapso global selecionaria um ramo em todo o
espaço de uma vez — e portanto nenhum domínio, nenhuma parede. É por isso
que a linha I–K é sedutora. Mas: (a) colapso objetivo é uma modificação da
dinâmica quântica, com parâmetros já experimentalmente limitados
(Bassi et al., Rev. Mod. Phys. 85 (2013) 471, arXiv:1204.4325), e nenhum
modelo de colapso conhecido é não-local dessa forma sem conflito com
causalidade; (b) `integration_assessment.md` (Pergunta 1, ajuste 3) já
identificou que não há equação ligando |Ψ⟩ à ação clássica; (c) o erro de
categoria é anterior: **g e f não são ramos alternativos** — coexistem nas
mesmas equações de movimento, acopladas por e_n(𝒦) no mesmo ponto x. Uma
superposição de "universo-g" e "universo-f" não é o que a ação descreve.
`[REPO/LIT/MEU]`

### R6 — Λ_ent é insalvável na forma proposta, por uma razão mais funda que a apontada no `integration_assessment.md`.

O documento de integração objeta, corretamente, que Λ_ent não tem equação
de movimento e que aditivo≠multiplicativo. A objeção decisiva, porém, é
outra: **entropia não gravita.** A fonte da equação de Einstein é
⟨T_μν⟩ renormalizado, não S_ent = −Tr(ρ ln ρ). Para um estado gaussiano —
que é o caso em todo o regime linear da teoria — ⟨T_μν⟩ é a energia de
vácuo usual, ou seja, exatamente o problema da constante cosmológica, não
sua solução. Um programa sério nessa direção precisaria de um postulado
adicional do tipo Jacobson (PRL 75 (1995) 1260, arXiv:gr-qc/9504004) ou
Van Raamsdonk (arXiv:1005.3035), que são afirmações sobre a **origem** da
equação de Einstein, não termos somáveis a Λ. E aí o critério
anti-circularidade do G1-c morde: uma entropia de emaranhamento entre φ₁ e
φ₂ é uma quantidade de um **bipartite interno**, não um grau métrico — é
literalmente o caso do segundo marcador do §3 de `gate1c_nota_trilema.md`
("um Goldstone interno não é um grau métrico"). `[MEU/LIT]`

### R7 — Quantização: a EFT tem corte, e a margem no primordial é de ~duas ordens de grandeza.

A gravidade bimétrica HR é uma EFT com corte Λ₃ = (m²M_Pl)^{1/3}
(de Rham–Gabadadze–Tolley arXiv:1011.1232; Hassan–Rosen arXiv:1109.3515;
correções quânticas: de Rham, Heisenberg & Ribeiro, arXiv:1307.7169
[verificar]). Consequências para a TDCP:
- **Hoje**, com m_T ≈ 2.3 H₀ (`manuscript-v2/06_setor_tensorial.md`),
  Λ₃⁻¹ ~ 10³ km `[MEU]` — a teoria não tem nada a dizer, quanticamente,
  abaixo dessa escala; qualquer discurso "quântico" sobre o setor massivo
  no universo tardio é vazio.
- **No primordial**, com m_T² = 12H², obtém-se
  Λ₃/H = 12^{1/3}(M_Pl/H)^{1/3} ≈ 2.3·(M_Pl/H)^{1/3}, que dá ≈ 1.4×10²
  para H ~ 10¹³ GeV `[MEU]`. Há margem, mas é finita: **impor Bunch–Davies
  em k/a→∞ está fora do domínio de validade**. As condições iniciais devem
  ser impostas em k/a ≲ Λ₃ e a dependência do resultado nessa escolha deve
  ser exibida. Nenhum documento do corpus faz isso.
- **Estabilidade radiativa da modulação:** o Gate 2 Parte B (ausência de
  fantasma BD com β_n(φ₋)) está aberto **classicamente**
  (`03_acao_e_dicionario.md` §5). Quanticamente é pior: loops de φ₋ geram
  operadores tipo (∂φ₋)²e_n(𝒦)/Λⁿ que não são da forma HR, destoando o
  ajuste de Fierz–Pauli ao longo da direção φ₋. Mesmo que a Parte B feche,
  a **preservação radiativa** do ajuste é uma pergunta separada e mais
  difícil. `[MEU/LIT]`
- **Unitariedade:** com o setor escalar são (2 DOFs, R-7) e Higuchi
  satisfeito por larga margem, não vejo violação de unitariedade dentro do
  corte — o risco não é fantasma, é **o corte ser baixo demais para as
  perguntas que a teoria quer fazer**.
- **Contagem:** 2 (sem massa) + 5 (massivo) + 2 (φ±) = 9 DOFs na v2.
  `01_tese.md` menciona a contagem antiga com um só escalar (8). Vale
  conferir a consistência da contagem declarada. `[verificar]`

### R8 — Isocurvatura: a estrutura é χ², e ninguém calculou.

Antes da transição, ⟨φ₋⟩=0 e δβ₁ ∝ (δφ₋)²/v★² — a impressão geométrica da
flutuação é **quadrática**, isto é, um campo χ² fortemente não-gaussiano.
Depois, com ⟨φ₋⟩=v, δβ₁ ≈ 2v·δφ₋/v★² e a resposta é linear. A transição
entre os dois regimes ocorre exatamente na janela em que U″ cruza zero.
Isso é um mecanismo de isocurvatura **modulada** perfeitamente definido, com
assinatura não-gaussiana característica, e sujeito aos vínculos de Planck
(β_iso ≲ 0.04 para isocurvatura CDM não-correlacionada, 95% — Planck 2018 X,
arXiv:1807.06211 [verificar valor exato]). Nada disso foi computado. O
resultado de `07_setor_escalar.md` sobre o espectador ser saudável é uma
afirmação de **estabilidade**, não de **amplitude**: saúde espectral não
limita o espectro. `[MEU]`

### R9 — "Correlação primordial φ₁–φ₂" ainda não tem definição no corpus.

`01_tese.md` postula "dois graus de liberdade fundamentais
**correlacionados**". Como estado quântico, isso está indefinido: correlação
clássica? gaussiano de dois modos? emaranhado? A situação é ironicamente
favorável — a resposta é derivável em uma tarde (ver P1) e é não-trivial —
mas enquanto não for escrita, "correlacionados" é adjetivo, não física, e
está no mesmo estatuto normativo que a identificação G1-a. `[MEU]`

### R10 — Risco de circularidade nas propostas quânticas de emergência.

Aplicando o critério de `gate1c_nota_trilema.md` §3 às rotas quânticas
plausíveis: (a) "f emerge do emaranhamento entre φ₁ e φ₂" — os geradores
quebrados são **internos** (a Z₂, ou uma U(1)_rel se promovida), portanto
cai no segundo marcador: não entrega multiplete spin-2 massivo, e a dívida
tem de ficar explícita; (b) "f emerge da decoerência/ramificação" — não há
gerador quebrado nenhum, logo a construção nem sequer é enquadrável pelo
critério, o que é sinal de que não é uma construção; (c) "f emerge de um
condensado de pares φ₁φ₂" — aqui o padrão é de difeos relativas assim que
o condensado carrega índices, e **cai por herança** na F1, exatamente como
o §3 antecipa. Nenhuma das três rotas quânticas óbvias passa. `[MEU]`

---

## Propostas de modelagem

Ordenadas por razão (o que decide) / (custo).

### P1 — **Primeiro cálculo: o emaranhamento gaussiano φ₁–φ₂ e sua divergência no ponto crítico.** (custo: uma sessão; decide R9 e o que sobra de I–K)

**Formalismo.** Matriz de covariância de estado gaussiano em FLRW, modo a
modo. Por modo k, o Hamiltoniano é diagonal em (φ₊,φ₋) com
ω±²(k) = k²/a² + V″±, e V″₋ = U″ = −μ₋² + 2λ_cφ₊² (a mesma dispersão já
medida em `07_setor_escalar.md` §3). O vácuo é produto em (φ₊,φ₋) e,
portanto, **emaranhado** na base (φ₁,φ₂). Escrevendo
ψ ∝ exp[−½(ω₊φ₊²+ω₋φ₋²)] = exp[−½(A(φ₁²+φ₂²)+2Bφ₁φ₂)] com
A=(ω₊+ω₋)/2, B=(ω₊−ω₋)/2, o parâmetro de mistura de Srednicki
(PRL 71 (1993) 666, arXiv:hep-th/9303048) é

> **ξ(k) = B/(A+√(A²−B²)) = (√ω₊ − √ω₋)/(√ω₊ + √ω₋)**

e S(k) = −ln(1−ξ) − ξ ln ξ/(1−ξ) [conferir convenção ξ vs ξ²].

**O que decide.**
- ξ = 0 ⟺ ω₊ = ω₋: se os dois campos tivessem o mesmo potencial, a
  "correlação primordial" seria **nula** — a assimetria de V é a origem do
  emaranhamento. Isso responde R9 com uma frase derivada.
- **ξ → 1 e S → ∞ quando ω₋ → 0**, ou seja, exatamente em φ₊ = φ₊,crit no
  limite IR. **O emaranhamento φ₁–φ₂ diverge no ponto de bifurcação.** Se
  isso se confirmar, a TDCP passa a ter um enunciado quântico próprio,
  derivado da sua própria ação: *a bifurcação é o máximo de emaranhamento
  entre os dois campos primordiais.* É a única parte dos Anexos I–K que eu
  consideraria recuperável — e ela sai de graça.
- Para k/a ≫ |U″|^{1/2}, ω₊≈ω₋≈k/a e ξ→0: o emaranhamento é **IR**, vive
  em modos super-horizonte. Isso já mata qualquer tentativa de ler S_ent
  como densidade de energia local.

**Extensão necessária:** para U″<0 não existe estado fundamental; o objeto
correto é a matriz de covariância evoluída (in-in / Bogoliubov) através da
instabilidade. Continua sendo um problema linear, tratável com a maquinaria
existente.

**O que P1 NÃO decide:** nada sobre gravitação. S_ent computado aqui não
entra em nenhuma equação de campo (R6). Isso deve ser declarado no próprio
documento de resultado, para não recriar o erro de I–K.

### P2 — **Segundo cálculo: o vínculo de paredes de domínio, e a decisão de escala.** (custo: meia sessão de conta + uma decisão de projeto; decide R1)

**Formalismo.** (i) Fixar a âncora dimensional: converter as unidades de
código de `05_fundo_ramo_finito.md` (v★=1) em GeV, exibindo μ₋, λ₋, v★, m,
M_g, M_f. (ii) Avaliar σ = (2√2/3)μ₋³/λ₋ e comparar com (1 MeV)³.
(iii) Determinar, no fundo da Fase A, **em que época** φ₊ cruza φ₊,crit —
número de e-folds antes do fim da inflação, se houver inflação, ou
redshift, se for pós-inflacionária. (iv) Se necessário, escrever o bias
δV = ε·μ₋³·φ₋ (ou v⁵/M_Pl) e verificar t_ann ~ σ/V_bias pelo critério de
Gelmini–Gleiser–Kolb, exigindo aniquilação antes de BBN.

**O que decide.** Três desfechos possíveis e todos informativos:
(a) a teoria vive em μ₋ ≲ MeV — sem problema, mas então a bifurcação é um
evento de baixa energia e "primordial" precisa ser reescrito;
(b) μ₋ alto com transição inflacionária precoce — S2/S3 valem, e a teoria
ganha uma **predição** (assimetria hemisférica, S3);
(c) μ₋ alto com transição tardia ou no fim da inflação — a teoria precisa
do bias de S1, e a tabela de simetrias de `03_acao_e_dicionario.md` §2 tem
de ser corrigida.
Em qualquer caso o resultado é uma restrição nova e publicável no espaço
de parâmetros, coisa que a TDCP hoje não tem.

**Variante estrutural a considerar seriamente:** promover a Z₂ discreta a
uma U(1)_rel contínua (φ_a complexos, parâmetro de ordem = fase relativa).
Defeitos viram **cordas**, não paredes — vínculos muito mais fracos e
assinaturas de GW interessantes. E isso conecta diretamente com a analogia
de condensados acoplados já registrada em `gate1_identidade_relacional.md`
§3 (modo de fase tipo Josephson). Preço: β_n passam a depender de |φ₋|², e
aparece um Goldstone sem massa — que, note-se, é inofensivo para testes de
quinto-força porque não acopla à matéria. Recomendo avaliar esta variante
**antes** de aceitar o bias ad hoc.

### P3 — **Terceiro cálculo: o collider cosmológico do spin-2 massivo — a predição que a teoria ainda não pediu.** (custo: uma sessão; decide se a TDCP tem assinatura própria)

**Formalismo.** In-in em de Sitter com um campo de spin 2 de massa
m² = 12H² (`06_setor_tensorial.md`), que está na série principal. Para
spin s, μ_s = √(m²/H² − (s−½)²) (Lee, Baumann & Pimentel, arXiv:1607.03735;
Arkani-Hamed & Maldacena, arXiv:1503.08043). Aqui **μ₂ = √(12 − 2.25) =
3.12** `[MEU]`. O biespectro no limite comprimido carrega

> B(k_L,k_S) ⊃ (k_L/k_S)^{3/2}·cos[μ₂·ln(k_L/k_S) + δ]·P₂(cos θ)

com frequência de oscilação **fixada pelo resultado universal
m_T²/H²→12** — ou seja, **sem parâmetro livre**. [verificar convenção de μ_s
e o expoente 3/2.]

**O que decide.** Se a amplitude for computável e não-desprezível, a TDCP
adquire uma assinatura falseável **exclusiva**: a dependência angular P₂ é
a impressão digital de spin 2, e a frequência 3.12 é a impressão digital
deste modelo. Se a amplitude for suprimida (o acoplamento à matéria é só
via mistura com g), o resultado é igualmente valioso: fecha por dentro a
esperança de assinatura primordial e concentra o programa observacional na
janela quase-horizonte tardia já identificada em `01_tese.md`.

### P4 — **Quarto cálculo: espectro e isocurvatura de δφ₋ com δφ₊ reintegrado.** (custo: moderado; decide R3 e R8)

Reintroduzir δφ₊ na redução do setor escalar; identificar quem é o modo
adiabático; computar o espectro de δφ₋ através da janela U″<0 → U″>0 e a
transferência para ζ via r★(φ₋) (formalismo δN de duas trajetórias). Saídas
diretas: fração de isocurvatura, f_NL de tipo χ² antes da transição, e o
n_s efetivo. É o que permite a primeira comparação da TDCP com Planck
2018 X (arXiv:1807.06211) no plano primordial.

### P5 — **Quinto: decoerência do modo δφ₋ e a formação de domínios, com o formalismo certo.** (custo: alto; só depois de P1–P4)

Master equation / influence functional para δφ₋ com o setor métrico como
ambiente, medindo a taxa de decoerência por modo e a escala de
classicalização; e a densidade inicial de paredes por Kibble–Zurek com o
tempo de quench τ_Q = |v²/(d v²/dt)| avaliado no crítico da trajetória da
Fase A. Isso quantifica R1/R4 em vez de estimá-los, e conecta com a
literatura padrão (Burgess–Holman–Hoover arXiv:astro-ph/0601646; Nelson
arXiv:1601.03734). Só vale a pena depois que P2 fixar a escala.

### P6 — **Critério anti-circularidade, versão quântica (uma página, custo zero).**

Estender `gate1c_nota_trilema.md` §3 com um terceiro marcador explícito
para propostas quânticas: *toda construção que invoque emaranhamento,
decoerência ou colapso para produzir a segunda métrica deve exibir
(i) o estado, (ii) a bipartição, (iii) o operador cujo valor esperado é
f_μν e (iv) a equação em que ele entra como fonte.* Falhando qualquer um
dos quatro, é narrativa. Isto vacinaria de antemão a ressurreição dos
Anexos I–K, e custa uma página.

---

## Veredito do especialista (5 linhas)

A TDCP fez, na v2, o movimento certo — trocou "bifurcação" por SSB de Z₂ —
e com isso herdou uma obrigação que não cumpriu: **uma Z₂ discreta global
exata quebrada espontaneamente produz paredes de domínio, e o corpus é
inteiramente silencioso a respeito.** O problema não é fatal (bias
suprimido por M_Pl, diluição inflacionária, ou promoção a U(1)_rel
resolvem), mas é bloqueante para publicação e impõe o primeiro vínculo
dimensional real da teoria: σ ≈ (2√2/3)μ₋³/λ₋ ≲ (1 MeV)³ sem escape. A
dimensão quântica, fora isso, está genuinamente não construída — não há
inflaton, δφ₊ não é carregado, nenhum espectro foi computado, e
"correlação primordial" segue sem definição de estado, embora seja
derivável de graça (o emaranhamento gaussiano φ₁–φ₂ diverge no ponto
crítico: é o único fragmento dos Anexos I–K que eu resgataria). Λ_ent e o
colapso global permanecem sem ponte, agora por uma razão mais forte que a
já registrada — entropia não gravita, e uma bipartição interna não é um
grau métrico, exatamente o que o critério do G1-c proíbe. Como teoria
quântica a TDCP é uma EFT com corte Λ₃, com ~duas ordens de margem sobre H
no primordial: suficiente para calcular, insuficiente para especular.

---

### Anexo — referências externas usadas

Domínios e defeitos: Zel'dovich, Kobzarev & Okun, Sov. Phys. JETP 40 (1975) 1
[ZhETF 67 (1974) 3] · Kibble, J. Phys. A9 (1976) 1387 · Zurek, Nature 317
(1985) 505 · Vilenkin, PRD 23 (1981) 852 [verificar] · Gelmini, Gleiser &
Kolb, PRD 39 (1989) 1558 · Saikawa, Universe 3 (2017) 40, arXiv:1703.02576 ·
Banks & Seiberg, PRD 83 (2011) 084019, arXiv:1011.5120.
Inflação híbrida e preaquecimento: Linde, PRD 49 (1994) 748,
arXiv:astro-ph/9307002 [verificar] · Felder et al., PRL 87 (2001) 011601,
arXiv:hep-ph/0012142 · Starobinsky & Yokoyama, arXiv:astro-ph/9407016 ·
Lyth & Wands, arXiv:hep-ph/0110002.
Bimétrica/massiva: de Rham, Gabadadze & Tolley, PRL 106 (2011) 231101,
arXiv:1011.1232 · Hassan & Rosen, arXiv:1109.3515 e arXiv:1106.3344 ·
de Rham, Heisenberg & Ribeiro, arXiv:1307.7169 [verificar] · Higuchi,
Nucl. Phys. B282 (1987) 397 · Comelli, Crisostomi & Pilo, arXiv:1202.1986 ·
Könnig et al., arXiv:1407.4331 · Akrami et al., arXiv:1503.07521 ·
Weinberg & Witten, Phys. Lett. B96 (1980) 59.
Quântico/emaranhamento/decoerência: Srednicki, PRL 71 (1993) 666,
arXiv:hep-th/9303048 · Kiefer & Polarski, arXiv:0810.0087 · Burgess,
Holman & Hoover, arXiv:astro-ph/0601646 · Nelson, arXiv:1601.03734 ·
Bassi et al., Rev. Mod. Phys. 85 (2013) 471, arXiv:1204.4325 · Jacobson,
arXiv:gr-qc/9504004 · Van Raamsdonk, arXiv:1005.3035 · Ryu & Takayanagi,
arXiv:hep-th/0603001.
Collider cosmológico e dados: Arkani-Hamed & Maldacena, arXiv:1503.08043 ·
Lee, Baumann & Pimentel, arXiv:1607.03735 · Planck 2018 X, arXiv:1807.06211.
