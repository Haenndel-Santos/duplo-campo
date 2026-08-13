# Posicionamento na Literatura — Consolidação

**Data desta versão:** 2026-08-13 (reescrita integral).
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
A única exceção parcial é o bloco do R-12i (§1.1): lá o *conteúdo* da
fonte continua sendo nível 3, mas as **identidades algébricas** que
ligam as fórmulas publicadas às nossas foram fechadas simbolicamente
(resíduo 0) e estão transcritas em
`docs/resultado_r12i_confronto_konnig.md` — que declara, ele próprio,
não ter deixado script novo versionado.

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
"resultado nosso" a "confirmação de um resultado de 2014".

---

## 0. Por que esta reescrita — dois eventos e uma inversão

A v1 ficou inteiramente para trás de três coisas.

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

Fonte: `docs/resultado_r12i_confronto_konnig.md` — hoje o item mais
bem verificado deste arquivo, e o único cujo nível de acesso é "texto
integral da versão publicada, conferido por duas rotas independentes".

---

## 1. Tabela-mestra de posicionamento

Coluna **Nível**: `V-12i` = verificado no texto integral da fonte
(R-12i); `V` = verificado na fonte pela v1, com marca registrada lá;
`B` = nível-de-busca declarado na v1; `n/r` = não registrado na v1,
**tratar como B**.

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
| **Exclusão do ramo infinito** (nosso critério: ξ cruza zero ⟹ lapso do setor f se anula ⟹ ponto singular) | **EM CONFLITO DECLARADO COM A FONTE.** `ξ = r + dr/dN` e `ξ = X/a` com `X ≡ ḃ/ℋ`: **mesmo sinal, mesmo zero**. O §II/§VI trata esse quique de `b` **explicitamente** e o defende como físico, com três argumentos declarados. E o *infinite-branch bigravity* (IBB) é o **único** modelo estável em todos os tempos do paper. A v1 registrava outra rota (`r′<0 ⇒ fantasma de Higuchi eterno`, Könnig 1503.07436) que **aponta no sentido oposto ao §VI** e nunca foi verificada na fonte | **Não é "consistente, forma diferente" (v1). É conflito.** É a porta mais cara que o repositório fechou. Ver §2b, risco **R-b** | **V-12i** para 1407.4331; **não verificado** para 1503.07436 |

### 1.2 Bloco B — o restante da tabela-mestra (herdado da v1)

| Nosso resultado | Estado na literatura | Veredito de novidade | Nível |
|---|---|---|---|
| Fundo do ramo finito (limite GR primordial exato, r: 0 → r_∞) | Ramo finito padrão (Könnig et al. 1407.4331 — mesma convenção; Akrami et al. 1503.07521). **Confirmado ao nível de identidade pelo R-12i**: `r ≡ b/a` (eq. 17), normalização β letra por letra (eq. 16), `M_f = 1` ⟺ `μ = 1, M_ef² = 1/2`, e o nosso `dr/dN = −3ρ̃/ρ̃′` **é** a eq. (21)+(22) deles — *os fundos são o mesmo fundo* | **Já conhecido** — e agora sabemos *exatamente* o quanto | **V-12i** |
| Higuchi automático no ramo finito | **Provado em geral**: viabilidade ⇒ r′ ≥ 0 ⇒ sem fantasma de Higuchi (Könnig 1503.07436); tb. De Felice et al. 1404.0008 | **Já conhecido** — citar, não reivindicar. *Atenção:* 1503.07436 aparece em duas linhas deste documento com leituras que precisam ser conferidas **juntas** (esta e a do ramo infinito) — ver R-b | `n/r` |
| **m_T²/H² → 12** universal no primordial (setor tensorial) | Nenhuma razão universal publicada (Fasiello–Tolley 1206.3852/1308.1647, Könnig, Cusin et al., Akrami et al. verificados — nada encontrado). **1407.4331 é setor escalar: não toca esta linha** | **Novo** (sharpening quantitativo) — **e é o único item do arquivo que o arco R-10→R-12i não moveu.** Mas a qualificação por época deixou de ser opcional: a fórmula geral é `m_T²/H² → 3(4+3w)`, **12 em matéria e 15 em radiação** — e a era genuinamente primordial é de **radiação**, de modo que os rótulos "primordial" do corpus significam, de fato, "era de matéria". Ver D3 (§2) | `V` para a busca nas 4 fontes; **`B`** para a conclusão de ausência |
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
r ≠ 0 no passado remoto.

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

## 2b. Os dois riscos abertos criados pelo confronto (R-12i §6)

Esta seção é nova. Ela existe porque o confronto com a fonte primária
criou dois problemas que **não são de posicionamento, e sim de
substância**, e que o paper tem de absorver antes de qualquer
submissão. Nenhum dos dois é resolvido aqui.

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

### R-b — a exclusão do ramo infinito (o mais caro)

**O fato.** O nosso critério de exclusão é `ξ = r + dr/dN`; como
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
todos os tempos** daquele paper — fundo viável, sem constante
cosmológica explícita para g, com r decrescendo de ∞ a um valor
finito, e estabilidade garantida por `r_c > 1` em toda a faixa
`0 < β₄ < 2β₁`. Ou seja: o repositório fechou, com um argumento que a
fonte primária rejeita nominalmente, exatamente a porta que a fonte
primária declara ser a saída.

**Não resolvido aqui — não há elementos.** O que fica registrado é o
que decidiria:

- **(a) A tensão interna do próprio corpus.** Este documento tem
  **duas** linhas sobre 1503.07436: uma diz "viabilidade ⇒ r′ ≥ 0 ⇒
  sem fantasma de Higuchi", a outra diz "r′ < 0 ⇒ fantasma de Higuchi
  eterno" **no ramo infinito**. Mas o IBB do §VI tem `r` **decrescendo**
  (r′ < 0) e é declarado estável em todos os tempos. **As duas
  leituras não podem estar ambas certas como escritas.** Nenhuma das
  duas foi verificada na fonte. *Este é o teste mais barato do
  repositório inteiro: abrir 1503.07436 e ler o que ele diz sobre o
  ramo infinito.* Se ele sustentar o fantasma de Higuchi eterno, o
  repositório tem um argumento — publicado, e **não** o nosso ξ — para
  excluir o IBB; se não sustentar, a exclusão fica sem apoio algum.
- **(b) O reexame do fundo, com o escopo certo.** O IBB viável exige
  **β₄ ≠ 0** (`0 < β₄ < 2β₁`), enquanto a nossa célula mínima tem
  β₄ = 0. O alvo do reexame é, portanto, o **ramo infinito da F1 com
  β₄ ligado** — não a célula atual. O R-10c Parte A já registrava "uma
  **segunda solução tardia viável** (r ≈ 2.23, ξ ≈ 2.23, H² > 0),
  completamente inexplorada pelo repositório": é essa.
- **(c) O ônus argumentativo.** Se a exclusão for mantida, ela precisa
  de um argumento **novo** que responda aos três deles, um a um.
  Repetir "ξ < 0" não responde a nenhum.

**Enquanto (a), (b) e (c) não forem feitos, o enunciado honesto é:**
*"o repositório excluiu o ramo infinito por um critério que a fonte
primária examina e rejeita; a exclusão está, hoje, sem apoio na
literatura."*

---

## 3. Ranking de novidade defensável (reescrito)

O ranking da v1 foi construído sobre resultados que caíram: os seus
lugares nº 1 e nº 3 dependiam de D1/D2 e do taquião tardio, e o nº 3
citava um no-go de classe que ou foi retirado (o modulado) ou é de
2014 (o de gradiente). Este é o ranking do que sobra **de fato**.

**Nota sobre os dois primeiros lugares.** O R-12i chama o `5/2` de
"a candidata mais forte" na sua tabela de sobreviventes **do setor
escalar** e, na mesma tabela, mantém o `m_T²/H² → 12` como "nº 1 do
ranking de novidade". Leitura adotada aqui: o primeiro é o melhor do
*setor confrontado*; o segundo é o melhor do *arquivo inteiro*,
porque o confronto não o tocou. Se essa leitura estiver errada, os
dois primeiros lugares trocam — e o ponto prático não muda:
**nenhum dos dois pode ser reivindicado sem a qualificação declarada
ao lado.**

1. **`m_T²/H² → 3(4+3w)`** (setor tensorial; 12 em matéria, **15 em
   radiação**). *Por quê aqui:* é o único item cujo objeto nenhum dos
   dois eventos moveu — 1407.4331 é setor escalar, e o tensorial não
   passa pela redução que o Erratum-02/03 corrigiu. É específica,
   verificável e não foi encontrada na literatura. *Risco:* (i) é uma
   afirmação de **ausência** em nível-de-busca; (ii) a generalização
   por época vem de **dois especialistas externos, não verificada
   internamente**; (iii) a discrepância em w = −1 (6 vs 3) está
   **aberta**. Citar Könnig 1503.07436 pelo corolário qualitativo.
2. **`m_ef²/H² → 5/2`** (massa efetiva do escalar métrico, ordem k⁰).
   *Por quê aqui:* é o único número do setor escalar que sobreviveu ao
   confronto — eles descartam explicitamente as soluções independentes
   de k como subdominantes e **nunca dão o termo de massa**. *Risco,
   declarado:* é exatamente a ordem k⁰ onde a perturbação de matéria
   ausente da nossa L2 entraria; `Δ = ½rr′` zera nos dois extremos
   justamente porque é ordem k², e nada garante que o termo k⁰ tenha a
   mesma sorte. **Não reivindicar antes do teste δρ_m** (§5, item 1).
   Este é o item de maior valor esperado e maior variância do arquivo.
3. **A reprodução independente dos dois extremos exatos** (`−1` e
   `+1`, mais o coeficiente linear) por maquinaria totalmente distinta
   — Schur/Faddeev–Jackiw contra a redução 10→2 de 1407.4331. *Por quê
   aqui e não mais acima:* o valor é **de método, não de física**;
   nenhum dos dois números é nosso. *Por quê não mais abaixo:* é o
   item mais bem verificado do arquivo, e uma concordância exata entre
   duas rotas independentes é exatamente o que um referee usa para
   confiar no resto da maquinaria. Vale um parágrafo, não uma
   reivindicação.
4. **O pacote da subclasse mínima**: β₁(φ) único + não-fatoração
   derivada + fundo transiente fora dos ramos com pouso. *Por quê
   aqui:* é fundo e estrutura de vínculos — não passa pela redução
   numérica, logo intocado pelos dois eventos —, e a lacuna
   hamiltoniana do chameleon bigravity é um gancho real. *Risco:*
   nível-de-busca; minisuperespaço; e a instabilidade radiativa da
   escolha "β₁ único" (§4.2 da síntese) ataca a própria premissa.
5. **Limiar de back-reaction** — como aplicação do mecanismo camaleão
   (citar 1702.04490 **verbatim**), com o limiar e a competição com a
   bifurcação como parte nossa. Intocado pelos dois eventos.
6. **Síntese conceitual TDCP** — defensável só com diferenciação
   explícita do análogo 2-BEC e do Higgs gravitacional. Novidade-por-
   síntese é a mais frágil das categorias; sem mudança de estatuto.

**Fora do ranking (rebaixados ou suspensos):**

- **O no-go de classe por gradiente** — sai do ranking de novidade.
  Vai para a introdução como *reprodução independente de um resultado
  de 2014*, com o `−1` explicitado e a forma fechada exibida. Ainda
  assim sujeito a R-a quanto ao **nome**.
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
§4b); Könnig 1503.07436; Lagos–Ferreira 1410.0207; Akrami et al.
1503.07521; De Felice et al. 1404.0008; Cusin et al. 1412.5979;
Aoki–Maeda–Namba 1506.04543; Mörtsell–Enander 1506.04977; Sakakihara
et al. 1211.5976; Brizuela et al. 2507.11526 (estado 2025).
**Higuchi:** Fasiello–Tolley 1206.3852 e 1308.1647.
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
2. **Abrir 1503.07436 na fonte** (R-b, item (a)). **É o item mais
   barato do arquivo e o de maior alavanca**: decide se o repositório
   tem ou não um argumento publicado contra o IBB, e resolve de
   passagem uma contradição interna entre duas linhas deste documento.
3. **Reabrir o ramo infinito com β₄ ≠ 0** (R-b, itens (b) e (c)),
   contra os três argumentos de §II/§VI de 1407.4331. Alvo: o ramo
   infinito da F1 com β₄ ligado — não a célula atual.
4. **D3 — verificar internamente** `m_T²/H² → 3(4+3w)` e **resolver a
   discrepância em w = −1 (6 vs 3)** antes de usar qualquer dos dois
   números. Enquanto isso não for feito, o corpus deve escrever "12 na
   era de matéria" e nunca "12 no primordial".
5. **Decidir R-a** (§2b): alinhar o cap. 07 §4 com o `r10a` §3b, ou
   justificar a força extra com o R-10d elevado a argumento central.
   É decisão editorial e bloqueia a submissão.
6. **Correções de texto herdadas do R-12i §5** — estado hoje:
   cap. 07 §4 **feito** (limiar r ≳ 0.21, com nota de proveniência);
   `resultado_r10a_gradiente.md` §3 **feito** (linha do enunciado
   corrigido); este documento **feito** (esta reescrita).
7. **Decidir a pendência da medida Stückelberg** (§6, P-2) — ou refazer
   a projeção sobre o modo métrico Ẽ do sistema 2-DOF corrigido, ou
   retirar a linha.
8. O programa (b1) ganhou genealogia (ISS 1971 → holografia → FQH
   2024) e checklist de obstáculos — insumo direto do cap. 09, sem
   alteração de estatuto por nenhum dos dois eventos.

*Itens da v1 que saem da fila:* "D1 (redução completa de vínculos no
ponto fixo)" — objeto caído; "a escrita do cap. 07 pode começar já com
esta bibliografia, condicionada ao D1" — o cap. 07 existe e foi
reescrito em 2026-08-13 com o arco completo.

---

## 6. Pendências declaradas e a lição do "0.28"

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
verificar.
