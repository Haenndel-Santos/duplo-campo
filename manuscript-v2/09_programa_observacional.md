# 09 — O programa observacional: o que foi medido, e por que o teste decisivo não é executável

**A premissa deste capítulo caiu — e o capítulo registra isso como
resultado.** A versão de 2026-08-12 abria afirmando que, com o setor
escalar são, a viabilidade da F1 era uma pergunta *exclusivamente
observacional*. Não é. No dia seguinte o arco R-10 → R-12 estabeleceu,
no próprio setor escalar, um **no-go de classe por gradiente**
(cap. 07 §4), e a era instável que ele define **cobre a recombinação**.
A pergunta mudou de "o que os dados dizem sobre a F1?" para "**sobre
que janela a F1 ainda tem o direito de falar?**". Este capítulo
responde essa pergunta, mantém as duas sondas já medidas com as
ressalvas que elas exigem, e substitui o "teste decisivo" por uma fila
que os resultados e os pareceres tornaram obrigatória.

## 1. O enunciado de escopo: validade restrita

**O no-go, na forma do cap. 07 §4.** Na classe F1 (Hassan–Rosen com
β₃ = 0, matéria acoplada só a g, ramo finito), o escalar métrico do
sistema 2-DOF tem **c_s² = −1 exatamente em r → 0**, para *qualquer*
escolha de (β₀, β₂, β₄, μ): 108/108 células com |c_s²+1| ≤ 1.1×10⁻⁷,
zero células com sinal positivo. Não é propriedade da célula de
benchmark — é da classe. *Nível 2b para a classe; fronteiras: β₁ = 1
e β₃ = 0 fixos, dois pontos de época (a = 0.01 com kh = 10⁴; a = 10⁻⁴
com kh = 10⁶), matéria só como ρ de fundo, sem era de radiação.*
*Fontes: `docs/resultado_r11_nogo_gradiente.md`,
`docs/resultado_r12_instrumento_e_cs2.md` §3;
`auditoria/code/out/r11_varredura_forma_beta.txt`,
`auditoria/code/out/r12g_isola_ruido_e_classe.txt`.*

Na célula mínima da classe (β₂ = β₄ = 0, β₀ = 1, μ = 1) o valor não é
medido: é identidade algébrica,

> c_s²(r) = −(3r+1)(9r⁵ − 6r³ + 3r² − 10r + 2) / (2(3r²+1)²),

com **−1 exato em r → 0** e **+1 exato no atrator tardio**
r_∞ = (√13−1)/6; o resíduo sub-horizonte é massa, m_ef²/H² → 5/2, sem
termo k⁴ e sem estrutura em k. *Nível 1 (forma fechada, seis gates
simbólicos aprovados) para essa célula; a extensão a (β₀, β₂, β₄, μ)
permanece nível 2b.* *Fontes: `docs/resultado_r12b_teorema_cs2.md`;
`auditoria/code/out/r12b_prova_simbolica_cs2.txt`.*

**A severidade é o que fecha o programa observacional linear.** A
troca de sinal ocorre em a_cross = 0.57808 ⟹ **z_cross = 0.6105** no
fundo β-constante (β₁ = 1, âncora a₀ = 0.931 do R-8b); no fundo
dinâmico REF a era instável cobre 3.07 e-folds e termina em z = 3.31 —
a amostragem começa em z = 92.1, já dentro dela, de modo que o início
não foi medido. Modos com kh ≳ 7–8 na transição **saem do regime
linear** (lnA até
32.4, com δ_i = 10⁻⁵ adotado como referência); os intermediários
(kh ~ 1–7) permanecem formalmente lineares e ainda assim crescem por
fatores de 2 a 10⁴. E a recombinação (z = 1100 ⟹ a = 8.46×10⁻⁴) está
**dentro** da era instável nos dois fundos. *Nível 2b; fronteiras: um
fundo β-constante e uma trajetória dinâmica (célula REF), sem
radiação — o mapa a ↔ z usa a âncora a₀ = 0.931 e muda com radiação.*
*Fontes: `docs/resultado_r10a_gradiente.md` §3b (R-10b),
`docs/resultado_r10c_saidas.md` Parte B,
`docs/resultado_r10_consolidado.md` §3,
`docs/resultado_r12_instrumento_e_cs2.md` §3;
`auditoria/code/out/r10b_severidade_instabilidade.txt`,
`auditoria/code/out/r10c_saidas_ramo_e_dinamico.txt`,
`auditoria/code/out/r10d_screening.txt` (D2, D3),
`auditoria/code/out/r12f_veredito_instrumento.txt`.*

**As quatro saídas conhecidas foram testadas: três estão fechadas e
uma foi REABERTA pelo R-12i** — é o teste dessas saídas que transforma
um achado em enunciado de escopo, e a reabertura restringe o alcance
desse enunciado:

| Saída | Teste | Estado |
|---|---|---|
| Ramo infinito | R-10c → **REABERTA** (R-12i) | a exclusão por ξ cruzar zero **não se sustenta**: é o quique de `b` que 1407.4331 §II/§VI trata e defende como físico, com três argumentos. Reexame pendente, e o alvo é o ramo infinito **com β₄ ≠ 0** (o IBB viável exige 0 < β₄ < 2β₁; a célula mínima tem β₄ = 0) |
| Modulação β₁(φ₋) | R-10c | fechada — age ~3 ordens de grandeza tarde demais (φ₋/v = 0.002 em a = 0.465) |
| Screening de Vainshtein | R-10d | fechada — δ_screen = (4π/3)(m_T/H)² ≈ 20–60 em todas as eras; *o λ cancela*, não há escala linear protegida |
| Forma-β (β₀, β₂, β₄, μ) | R-11 + R-12g | fechada — constante estrutural da classe |

*A reabertura, em uma frase (R-12i §1.6 e §R-b).* Como `b = ra`, o
nosso `ξ = r + dr/dN` é `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al. —
**mesmo sinal, mesmo zero** —, de modo que o "ξ cruza zero" do R-10c é
ponto por ponto o quique de `b` que 1407.4331 §II/§VI trata
explicitamente e defende como físico: f não acopla à matéria e não tem
interpretação geométrica; nenhuma variável de fundo ou perturbada
apresenta singularidade; `√(−det f)·R̄(f)` permanece finita e não-nula,
logo as equações de movimento existem em todo instante. A
*infinite-branch bigravity* é o **único** modelo estável em todos os
tempos daquele paper. O estado não é "viável": é **reaberto e
exigindo reavaliação**, com o caveat de escopo obrigatório de que o
alvo é o ramo infinito da F1 **com β₄ ≠ 0**, e não a célula mínima
(β₄ = 0). **Não há hoje argumento sustentado contra o IBB no corpus** —
o candidato ("fantasma de Higuchi eterno", 1503.07436) aparece em duas
linhas contraditórias de `docs/posicionamento_literatura.md`, nenhuma
verificada na fonte; verificar 1503.07436 é o caminho mais barato para
decidir.

*Nível 2b, fronteiras nos docs de origem.* *Fontes:
`docs/resultado_r10c_saidas.md`, `docs/resultado_r10_consolidado.md`
§2–3, `docs/resultado_r11_nogo_gradiente.md` §3,
`docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b);
`auditoria/code/out/r10c_saidas_ramo_e_dinamico.txt`,
`auditoria/code/out/r10d_screening.txt`,
`auditoria/code/out/r11_varredura_forma_beta.txt`.*

Resta viva apenas a **auto-invalidação linear** — o argumento de que o
crescimento leva ao não-linear e portanto o linear não decide. O
R-10d o registra pelo que ele é: *não é proteção, é ignorância*.
"Impede de *refutar* a teoria pela instabilidade linear, e impede
igualmente de *calcular* qualquer observável linear na era instável"
(`docs/resultado_r10_consolidado.md` §3). Consequência direta e sem
rodeio: **o CMB da F1 não é calculável linearmente enquanto este
quadro valer.**

**A decisão.** O R-10 consolidado enumerou três opções e o R-11/R-12
fechou as outras duas (a varredura de forma-β foi feita e deu no-go; o
tratamento não-linear está fora do alcance do projeto). O que o
manuscrito adota é a opção 3, na formulação já fixada no documento:

> **Declarar validade restrita**: a F1 como implementação com domínio
> z ≲ 3, sem previsão de CMB. Honesto, publicável como estudo de
> classe, mas abandona o objetivo cosmológico.
> — `docs/resultado_r10_consolidado.md` §4, opção 3.

Nota de fronteira sobre o "z ≲ 3": os dois fundos medidos dão o fim da
era instável em z = 0.61 (β-constante) e z = 3.31 (dinâmico REF); o
domínio declarado é o mais permissivo dos dois, e **depende do fundo**.
Nenhuma medida existe com era de radiação, que move a_cross.

E o que este enunciado **não** é (registrado no próprio R-10
consolidado §6 e no R-11 §4): não é refutação da TDCP como hipótese
conceitual. É refutação da *suficiência* da implementação F1, no ramo
finito, para fins cosmológicos, no estado atual. As portas que ficam
entreabertas são duas: β₃ ≠ 0 — que sai da definição de F1, isto é,
leva a uma F2 — e, desde o R-12i, o **reexame do ramo infinito com
β₄ ≠ 0** (§1).

## 2. Sonda 1 — sub-horizonte quase-estático (R-8a), com o escopo de época

**O que a sonda mediu, e por que sobrevive.** μ(a,k) e a razão de
lensing definidos como **razões de resposta** bimétrico/GR com a mesma
fonte e o mesmo fundo H(a) — construção em que toda convenção e
normalização cancela. Gates: o desvio de slip do ramo GR escala como
C/kh² (C ≈ 9.2 — física subdominante quase-estática, medida e usada
para **definir** a região confiável kh ≥ 22); μ(kh=300) → 1 a
6.7×10⁻⁵; queda ∝ kh⁻¹·⁸⁶ ≈ kh⁻² (termo líder (m·a/k)² presente).

**Resultado** (região confiável, duas eras, dois fundos): valores
centrais |μ−1|, |Σ_lente−1| ≤ 0.66% (kh = 30, era de matéria), ≤ 0.06%
em kh ≥ 100. **Fraseado de precisão vinculante:** o piso de erro da
própria sonda é ~2% na fronteira da região confiável; o enunciado
forte é *"nenhum desvio acima do piso QS foi detectado"* — 0.66% é
valor central computado, não previsão de precisão. A janela
quase-horizonte (kh ≲ 22) fica **indecidida** por esta sonda (os
números crus de até 17% lá são contaminação da própria aproximação —
não são enunciado). *Nível 2b; fronteiras: benchmark β-constante
(F′ = F″ = 0), matéria só como fonte, χ̄ parado, grade a = 0.1…75000
em unidades de código, a_eq interna = 0.686 (β₁=1) / 0.429 (β₁=4.47).*
*Fontes: `docs/resultado_r8a_quase_estatico.md`;
`auditoria/code/out/r8a_quase_estatico_mu_sigma.txt`.*

O R-8a **não passa pela cadeia numérica defeituosa do Erratum-03**:
ele resolve −W q + J = 0, sem Ċ e sem `np.gradient`. O item "refazer o
R-8a com instrumento limpo" saiu da fila por medida, não por
suposição. *Nível 2b, como o R-12 inteiro declara; fronteira do mapa
de alcance que sustenta o enunciado: amostragem em 16 pontos
(a ∈ {100, 10³, 10⁴, 8×10⁴} × kh ∈ {0.2, 1, 5, 20}) mais um corte em
kh na era tardia — não é escaneio contínuo, e a faixa a ∈ (0.05, 100)
ficou sem sondar.*
*Fonte: `docs/resultado_r12_instrumento_e_cs2.md` §6–7;
`auditoria/code/out/r12h_raio_de_alcance.txt`.*

**A ressalva de escopo de época — vinculante.** Como kh = k/(aH) é
adimensional, a janela de crescimento/lensing observável (RSD,
cisalhamento; k ≳ 0.01 h/Mpc ⟺ kh ≳ 30 hoje) está inteira na região
onde nenhum desvio foi detectado. Mas **kh é função da época**, e é
aqui que o enunciado precisa de fronteira explícita:

- o "sub-horizonte consistente com GR" vale para **z ≲ 10 e
  k ≳ 0.01 h/Mpc** — a grade da sonda, traduzida para unidades
  físicas, não vai além de z ≈ 8;
- o critério "kh ≲ 22 indecidido", **avaliado na recombinação**,
  corresponde a k ≲ 0.14 h/Mpc, isto é, **ℓ ≲ 1300** — todo o CMB
  primário;
- o regime z ≳ 100 **nunca foi sondado**, e o modelo do R-8a sequer
  tem era de radiação;
- o próprio R-8a registra que os **desvios crescem quando r decresce**
  ("r pequeno → setor-f responde mais",
  `docs/resultado_r8a_quase_estatico.md` §2) — a tendência medida
  aponta na direção errada para uma extrapolação tranquilizadora.

Os três primeiros itens são aritmética e leitura de escopo do
**parecer de astronomia observacional** (W1) — *opinião de especialista
externo, não resultado do repositório*; o quarto é medida do
repositório. *Fonte do parecer:
`docs/pareceres_especialistas/parecer_astronomia.md` W1;
`docs/pareceres_especialistas/00_sintese_cruzada.md` §4.2 item 5.*

**Leitura correta, portanto:** no benchmark e **na janela tardia**, a
F1 passa pelos vínculos de crescimento sem ajuste. O regime z ≳ 100
com kh ≲ 22 naquela época é **não testado e de alto risco** — e o §1
deste capítulo explica por que ele não pode ser testado linearmente no
estado atual.

## 3. Sonda 2 — a massa tensorial (R-8b), com o qualificador

Para testar o postulado do corpus m ~ 30–300 H₀, construiu-se a
família β_n → s·β_n com vácuo de φ₋ (U₀) mantendo o H tardio — o dial
canônico que varre a escala da interação preservando a forma-β e a
história de expansão. Dois resultados:

**(a) O fundo dobra.** r²𝒱_f(r) tem mínimo positivo (0.3 em r = 1) na
forma-β do benchmark; com H tardio fixo isso trava
s ≤ 3μH*²/(0.3 m_eff²) ≈ 6.2 — verificado analítica e numericamente
(fold em s ≈ 5.7). **O postulado 30–300 H₀ é inalcançável por dial
contínuo nesta família.** Alcançá-lo exige outra forma-β (𝒱_f com zero
em r finito) — uma escolha estrutural nova, que ademais implica ajuste
fino (U₀ < 0 grande, vácuo de φ₋ cancelando a energia da interação). A
v2 registra o postulado como **não incorporado**: se um dia for
adotado, entra como hipótese estrutural declarada, não como parâmetro
livre. *Nível 2b (obstrução verificada por rota analítica e numérica,
mas dentro de uma família); fronteira: forma-β do benchmark sob
rescala uniforme, ramo conectado por continuação.*
*Fontes: `docs/resultado_r8b_limite_mH0.md` §2a;
`auditoria/code/out/r8b_limite_mH0.txt`.*

**(b) Dentro da família, a massa é fixada — com três qualificadores.**
m_T/H₀ ∈ [2.26, 2.41] em toda a família alcançável (s = 0.25 → 5.5,
todos os membros com saúde cinética verificada), pela fórmula do
projeto (`derivations/02_setor_tensorial_mT2.md`, avaliada em a₀; a
razão é função da época: ~2.3 em a₀, ~3.5 no Λ profundo). Os desvios
de crescimento na janela observacional (z ≤ 1, k = 0.05–0.15 h/Mpc):
≤ 0.012%. *Nível 2b; fronteiras: forma-β do benchmark sob rescala
uniforme; ramo conectado por continuação; saúde por membro = gate de
assinatura (3 épocas × 2 kh); limites observacionais adotados como
referência de ordem de grandeza (declarado).* *Fontes:
`docs/resultado_r8b_limite_mH0.md` §2b, §4;
`auditoria/code/out/r8b_limite_mH0.txt`.*

Os qualificadores, que o enunciado anterior deste capítulo ("a massa
do gráviton deixou de ser parâmetro e virou predição") não carregava:

1. **"Cravado" é sobre-afirmação.** A família varrida é um **dial de 1
   parâmetro num espaço de ≥5**, com a **forma-β congelada**. O
   enunciado defensável é: *m_T/H₀ ∈ [2.26, 2.41] ao longo do dial de
   rescala uniforme, na forma-β do benchmark, no ramo conectado ao
   benchmark*. Sob mudança de forma-β o número muda — e o próprio
   R-8b diz que outra forma-β seria necessária se o postulado
   30–300 H₀ fosse perseguido. *Juízo do parecer de física teórica,
   endossado pela síntese; opinião externa, não resultado.* *Fonte:
   `docs/pareceres_especialistas/00_sintese_cruzada.md` §4.3 item 10;
   `docs/pareceres_especialistas/parecer_fisica_teorica.md` W5.*
2. **O número testa gravidade bimétrica, não a TDCP.** Três dos cinco
   pareceres, sem contato entre si, observam que m_T ~ O(H₀) é a
   assinatura **genérica de auto-aceleração da classe** bimétrica — é
   a própria condição de o termo de interação fazer o papel de Λ.
   Concordar com a expectativa genérica da classe é consistência, não
   discriminação. *Convergência dos pareceres; opinião externa.*
   *Fonte: `docs/pareceres_especialistas/00_sintese_cruzada.md` §1;
   `docs/pareceres_especialistas/parecer_astrofisica.md` PFr-8;
   `docs/pareceres_especialistas/parecer_astronomia.md` W6(d), F8.*
3. **A família apaga a própria alavanca.** U₀ é resolvido por s para
   manter o H tardio do benchmark — um parâmetro ajustado para
   eliminar a diferença observável em H(z) não pode depois ser
   reivindicado como testável via H(z). O ajuste está declarado no
   R-8b §1; a leitura é do parecer de astronomia (W6a). *Opinião
   externa sobre resultado do repositório.*

Enunciado que o capítulo adota, então: **m_T ≈ 2.3 H₀ é uma predição
da família do benchmark, não da TDCP** — e converter isso em predição
*com barra de erro* exige varrer a forma-β mantendo H(z), Ω_m e saúde
cinética fixos (proposta P3 do parecer de astronomia; não feita).

## 4. O que continua indistinguível, e o que está em conflito

O enunciado global anterior — "observacionalmente indistinguível e
não-excluída" — **não vale mais como enunciado global**. Ele vale
sobre uma janela e falha sobre outra, e a separação é o conteúdo desta
seção.

**Continua retirado** (não voltou nada): a previsão de excesso ISW
2–8× em baixo-ℓ e a "tensão" associada, a dispersão p = 0.44 e a
localização da tensão-Akrami — todas da era do sistema espúrio.
*Fontes: cap. 07 §4; `docs/resultado_r7_cascata.md` §5.*

**Continua indistinguível — a janela tardia sub-horizonte.** Em
z ≲ 10 e kh ≥ 22, nenhum desvio acima do piso QS (~2%) foi detectado
(§2), e ao longo de toda a família do R-8b os desvios de crescimento
na janela z ≤ 1 ficam em ≤ 0.012% (§3). É a mesma janela em que o
setor escalar é são: na era tardia o modo métrico tem **c_s² = +1
exato** (§1). Aqui a F1 não é excluída — e também não é distinguível.
A isso os pareceres acrescentam, como juízo externo, que **nenhuma
escala astrofísica acessível separa a teoria de GR**: com
λ_C = 1/m_T ≈ 1.9 Gpc e r_V de qualquer estrutura ligada excedendo o
tamanho da própria estrutura, perfis de halo, dinâmica de aglomerados
e lente ficam blindados, e o canal de ondas gravitacionais está
fechado por construção (matéria só em g ⟹ c_T = 1). *Opinião de
especialista; contas de ordem do parecer, não do repositório.*
*Fonte: `docs/pareceres_especialistas/parecer_astrofisica.md` PFr-6.*

**Está em conflito — a era inicial.** Em r ≲ 0.05 o escalar métrico
tem instabilidade de gradiente com c_s² = −1, a era instável cobre a
recombinação, e das quatro saídas conhecidas três estão fechadas —
a do **ramo infinito foi reaberta pelo R-12i**, com o alvo em β₄ ≠ 0
e reexame pendente (§1). O
conflito não tem, hoje, a forma "a F1 prevê X e o dado mede Y": tem a
forma mais dura de que **o observável não é computável** no regime em
que o dado existe. Modos com kh ≳ 7–8 se auto-invalidam; modos com
kh ~ 1–7 permanecem lineares e crescem por fatores de 2 a 10⁴ — uma
deformação enorme da função de transferência, que precisaria ser
calculada e confrontada, e cujo cálculo o próprio regime impede de
fechar com a maquinaria linear atual.

**A janela que o capítulo anterior chamava de decisiva é, além disso,
a pior do céu.** A cadeia que a versão anterior usava — kh ≲ 22 ⟺
escalas ≳ Gpc ⟺ baixo-ℓ — tem os dois primeiros elos equivalentes e o
terceiro **não**: o ℓ que um dado k ocupa depende da distância comóvel
até onde a física age. Feita a projeção corretamente, dois pareceres
mostram, independentemente, que a região é exatamente onde a variância
cósmica é uma parede: a amplitude de banda em 2 ≤ ℓ ≤ 20 não é
mensurável melhor que ~8% por experimento nenhum, e em k = 10⁻³ h/Mpc
um volume DESI-like contém ~1 modo (σ(P)/P ≈ 141%), de modo que
"P(k) em escalas ≳ Gpc" não é um teste caro, é uma impossibilidade
salvo por multi-tracer. *Contas dos pareceres de astronomia (W2, W3,
W4) e astrofísica (PFr-9); opinião externa, não verificada
internamente.*
*Fontes: `docs/pareceres_especialistas/parecer_astronomia.md` W2–W4;
`docs/pareceres_especialistas/parecer_astrofisica.md` PFr-9.*

Somando: mesmo que o no-go de gradiente não existisse, o alvo do
"teste decisivo" da versão anterior estava atrás de uma parede
irredutível. O no-go torna o ponto acadêmico — mas ele explica por que
a fila do §6 não tenta contorná-lo.

## 5. Duas declarações que este capítulo faz de frente

**(a) A F1 não alivia nenhuma tensão observacional; sua motivação é
conceitual.** Com o H tardio fixado por construção na família do R-8b
e desvios de crescimento ≤ 0.012% na janela observável, a F1 **não
toca H₀ nem S₈**. Não há mecanismo para a tensão H₀ — a família fixa
H(z) —, e a tensão S₈ deixou de ser alvo confiável de qualquer forma.
Isto não é defeito lógico: é fato estratégico, e a posição honesta é
declará-lo. A motivação da F1 é a costura conceitual do cap. 08 (o elo
Φ₋ → φ₋ → r), que permanece **normativa, não derivada** (Gate 1,
G1-a). *Recomendação explícita e unânime dos pareceres — síntese §1,
astrofísica PFr-11 e veredito item 4; opinião externa endossada por
este manuscrito como decisão editorial.* *Fontes:
`docs/pareceres_especialistas/00_sintese_cruzada.md` §1;
`docs/pareceres_especialistas/parecer_astrofisica.md` PFr-11;
base quantitativa: `docs/resultado_r8b_limite_mH0.md` §1–2.*

**(b) Ressalva de escopo obrigatória: o setor primordial não está
modelado.** O modo δφ₊ está **ausente da redução**. Não há inflaton
identificado, e o modo que carregaria ζ não está no sistema. A
contagem "2 DOFs escalares" é **do setor modelado**, não da teoria.
Consequência vinculante para este capítulo: **nenhuma afirmação sobre
n_s, A_s ou isocurvatura é possível hoje** — nem positiva nem
negativa. Onde o §6 lista isocurvatura como canal com futuro, é como
*cálculo a fazer depois de o setor primordial existir*, não como
previsão pendente. *Ressalva levantada pelo parecer de fundamentos
quânticos; opinião externa, adotada como fronteira declarada.*
*Fonte: `docs/pareceres_especialistas/00_sintese_cruzada.md` §4.2
item 4.*

## 6. A fila real

**O "teste decisivo = R-8 completo" sai.** Duas razões, uma interna e
uma externa:

- **Interna (resultado do repositório):** o R-8 completo calcularia
  C_ℓ de baixo-ℓ sobre o sistema 2-DOF, e "o objeto que ele calcularia
  é linearmente indefinido na época em que o CMB se forma"
  (`docs/resultado_r10_consolidado.md` §4). Não é falta de máquina.
- **Externa (recomendação unânime dos cinco pareceres, §7 da
  síntese):** **não iniciar o R-8 completo**. A razão registrada é
  tríplice — ele é caro, mira a janela mais limitada por variância
  cósmica, e seria construído sobre fundações não testadas nos eixos
  que importam. *Opinião externa convergente, não resultado.* *Fonte:
  `docs/pareceres_especialistas/00_sintese_cruzada.md` §7.*

### 6.1 Itens baratos que decidem antes (uma sessão ou menos cada)

1. **w_eff(z) do ramo finito vs DESI DR2.** O fundo já existe (cap. 05
   §2 declara nível 2a para os seus enunciados) e **não passa pela
   redução de perturbações** — é a única alavanca
   observacional viva do lado do fundo, e **não é limitada por
   variância cósmica**. Critério: Δχ²(F1 vs ΛCDM) em BAO+SNe. Se a F1
   reproduzir a fenomenologia fantasma que a literatura recente
   reporta para bimétricas, *isto — e não o baixo-ℓ — é o enunciado
   observacional publicável do repositório hoje*; se divergir do ramo
   finito padrão da literatura, é sinal de erro de convenção e precisa
   ser investigado antes de tudo. *Proposta A2 do parecer de
   cosmologia; opinião externa. Referências externas dela carregam a
   marca [verificar] do próprio parecer.* *Fonte:
   `docs/pareceres_especialistas/parecer_cosmologia.md` A2;
   `docs/pareceres_especialistas/00_sintese_cruzada.md` §6 item 1.*
2. **Validação do R-8a contra fórmulas QS publicadas.** Reproduzir as
   expressões quase-estáticas fechadas de μ(a,k) e Σ(a,k) da
   literatura bimétrica com a maquinaria da casa. Aceitação proposta:
   1% no regime de validade comum. Sem isso, "|μ−1| ≤ 0.66%" é um
   número sem controle externo — e a lição do Erratum-02 é
   precisamente que o pipeline interno pode convergir para o objeto
   errado. *Propostas P10/A3 (cosmologia) e P1/V-EXT (astronomia);
   opinião externa.* *Fontes:
   `docs/pareceres_especialistas/parecer_cosmologia.md` P10, A3;
   `docs/pareceres_especialistas/parecer_astronomia.md` P1.*
3. **Varredura de μ = M_f²/M_g².** A visibilidade do segundo setor é
   ε ≡ K_ℓℓ/K_hh = μr³/ξ — o dial que decide se a F1 é falseável, e
   **nem o R-8a nem o R-8b o varreram** (o R-8a rodou dois fundos, o
   R-8b varreu a escala global s). Se ε for pequena na faixa de μ
   adotada, qualquer programa observacional produzirá um nulo
   previsível. *Proposta PFr-5/PM-2 do parecer de astrofísica; a
   identificação de μ com M_f²/M_g² é inferida pelo parecer e ele
   próprio pede confirmação no código antes de citar — opinião
   externa não verificada internamente.* *Fonte:
   `docs/pareceres_especialistas/parecer_astrofisica.md` PFr-5.*
4. **Escopo de época com era de radiação.** Refazer a sonda do R-8a em
   z = 30, 300, 1100, depois de adicionar ρ_r a⁻⁴ ao fundo, com
   kh = 5, 10, 22, 50, 100. Pergunta única pré-declarada: |μ−1| e
   |Σ−1| **crescem, saturam ou desligam** quando r → 0? Custo baixo (é
   o script existente com grade nova). Este item ganhou uma segunda
   função depois do R-10: a era de radiação também **move a_cross**, e
   nenhuma medida de c_s² existe com radiação. *Proposta P2 do parecer
   de astronomia (opinião externa); a fronteira "sem radiação" é
   declarada em todos os docs de R-10 a R-12 (resultado do
   repositório).* *Fontes:
   `docs/pareceres_especialistas/parecer_astronomia.md` P2;
   `docs/resultado_r12_instrumento_e_cs2.md` §7.*

### 6.2 Gates de sobrevivência — fora da fila atual, e antes de qualquer cosmologia

Dois gates podem matar a implementação sem que nenhum C_ℓ seja
calculado, e **nenhum dos dois está na fila do repositório**:

- **Vainshtein/PPN.** O bloco aritmético Vainshtein/PPN da v1 e o
  formalismo HR do Anexo A permanecem como material de partida, a
  re-derivar. A prioridade mudou: isto não é "quando o R-8 alcançar",
  é **antes**. Sem Vainshtein, o gráviton massivo entrega a
  descontinuidade vDVZ, e nenhum C_ℓ salva isso. O que falta é a parte
  não-trivial — a **existência** do regime Vainshtein *nesta* família
  e o *matching* da solução estática à condição de contorno
  cosmológica r(∞) = r(a₀), que a v1 nunca fez e a v2 ainda não fez.
  Incluindo, como o item que o parecer aponta como o mais provável de
  gerar problema real: **a quinta força de φ₋ na versão modulada
  (F′ ≠ 0)** — um escalar ultraleve sem mecanismo de Vainshtein
  próprio, que precisaria de camaleão ou symmetron para sobreviver aos
  testes locais. *Propostas PFr-3/PFr-4/PM-3 do parecer de
  astrofísica; as estimativas de r_V e de resíduo PPN ali são contas
  do especialista, declaradas por ele como estimativas de ordem e não
  derivações — opinião externa.* *Fonte:
  `docs/pareceres_especialistas/parecer_astrofisica.md` PFr-3, PFr-4,
  PM-3.*
  **Distinção que este capítulo faz questão de manter:** o R-10d
  fechou o *screening* como saída para a instabilidade **linear
  cosmológica** (δ_screen ≈ 20–60; o λ cancela). Isso é outra
  pergunta, e não substitui o gate solar/PPN — que continua aberto.
- **Buracos negros e instabilidade do spin-2 massivo.** Verificar a
  existência das soluções proporcionais no ramo finito da F1,
  recalcular a instabilidade tipo Gregory–Laflamme no regime
  m_T r_s ≪ 1 e **extrair a escala de tempo**. Se instável em escala
  astrofísica, a teoria morre por observação de objetos compactos,
  independentemente de qualquer cosmologia; se estável, custa um
  parágrafo. *Proposta PM-5 do parecer de astrofísica; opinião
  externa, com o próprio parecer registrando [verificar] sobre o
  comportamento assintótico da taxa.* *Fonte:
  `docs/pareceres_especialistas/parecer_astrofisica.md` PM-5.*

### 6.3 Canais com futuro real que o corpus nunca tocou

Se o programa observacional voltar a existir — o que hoje depende de
sair da F1 (β₃ ≠ 0 ⟹ F2) ou de um tratamento não-linear da era
instável —, ele não deve mirar o baixo-ℓ TT. Os dois canais com futuro
instrumental real, ambos com **zero linhas no corpus**:

- **Isocurvatura.** A TDCP postula dois graus de liberdade primordiais
  e o setor corrigido tem um espectador δφ₋ que sobrevive — a
  definição de um candidato a modo de isocurvatura. O parecer de
  astronomia avalia que este é o vínculo mais provável de matar ou
  validar a hipótese, e o único que ataca a hipótese *conceitual*
  (dois campos), não só a implementação bimétrica. **Sujeito à
  ressalva §5(b): sem δφ₊ na redução, o cálculo não pode nem começar
  hoje.** *Proposta W8/P7; opinião externa.* *Fonte:
  `docs/pareceres_especialistas/parecer_astronomia.md` W8, P7.*
- **Modos B / supressão de r_T.** (`r_T` = razão tensor-escalar; o
  dicionário da v2 exige esse símbolo para não colidir com r = b/a.)
  Com m_T/H da ordem de 2–3.5 em toda a história, o modo tensorial
  massivo nunca está no regime de massa desprezível: a transição
  k = m_T·a cai sempre em kh ≈ 2–3.5. O ângulo de mistura g–f é fixado
  pelos mesmos β_n e por r = b/a, e suprime o r_T observado frente ao
  inflacionário —
  canal com fundo nulo em ΛCDM sem tensores, e portanto favorável em
  variância cósmica, com instrumento voando (LiteBIRD). *Proposta
  W9/P4; opinião externa, e as sensibilidades citadas pelo parecer
  carregam a marca [verificar].* *Fonte:
  `docs/pareceres_especialistas/parecer_astronomia.md` W9, P4.*

### 6.4 Se um pipeline de C_ℓ um dia for construído

O **dicionário de épocas** (`docs/r8_dicionario_epocas_opcoes.md`)
segue de pé como **decisão declarada, não como resultado**: os insumos
que só o autor fixa — a forma-β (mantê-la ⇒ m_T ≈ 2.3 H₀ é a predição
da família; mudá-la ⇒ declarar a escolha estrutural), a massa física
de φ₋ hoje, a normalização primordial e a história de fundo com
radiação — permanecem escolhas, e nenhuma delas foi tomada. A elas o
§5(b) acrescenta um pré-requisito que não é escolha e sim lacuna: sem
δφ₊ na redução, não há de onde tirar a normalização primordial.

Duas condições que este capítulo pré-declara agora, para não serem
negociadas depois:

1. **Gate externo antes de qualquer C_ℓ próprio** (V-EXT): reproduzir
   um resultado bimétrico publicado dentro de ~2% antes de afirmar
   qualquer C_ℓ da casa. Racional: o Erratum-02 mostrou que um
   pipeline interno pode convergir lindamente para o objeto errado, e
   um pipeline de Boltzmann é muito mais complexo que a redução que
   falhou. *Proposta P1 do parecer de astronomia; opinião externa,
   adotada aqui como condição.*
2. **Critério de encerramento pré-declarado**: se o efeito máximo em
   ℓ ≤ 30 ficar abaixo de ~2%, declarar a F1 **observacionalmente
   indistinguível de ΛCDM**, encerrar o programa observacional e
   transferir o ônus inteiro para o cap. 08. O desfecho
   "indistinguível" é legítimo e precisa ser aceito **antes**, não
   depois. *Critério B da proposta PM-4 do parecer de astrofísica; os
   limiares numéricos são do especialista, declarados por ele como a
   calibrar — opinião externa.* *Fonte:
   `docs/pareceres_especialistas/parecer_astrofisica.md` PM-4;
   `docs/pareceres_especialistas/00_sintese_cruzada.md` §7.*

## 7. Ativos e passivos da v1

Os números CLASS/ISW da v1 seguem **inutilizáveis** (sistema espúrio;
cap. 07 Ato 2). O bloco aritmético Vainshtein/PPN e o formalismo HR do
Anexo A permanecem como material de partida — mas deixaram de ser
"material a re-derivar quando o R-8 completo os alcançar" e passaram a
ser **gate de sobrevivência** (§6.2). É a única mudança de estatuto que
o arco R-10 → R-12 produziu nesse acervo.
