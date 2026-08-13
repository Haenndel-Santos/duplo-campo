# Parecer — Cosmologia

**Emissor:** revisor externo, cosmologia teórica (bimétrica, perturbações,
CMB, energia escura). **Data:** 2026-08-13. **Base de leitura:**
`manuscript-v2/04,05,07,09`, `docs/resultado_ramo_finito.md`,
`docs/resultado_r7_cascata.md`, `docs/resultado_r7e_saude_interna.md`,
`docs/resultado_r8a_quase_estatico.md`, `docs/resultado_r8b_limite_mH0.md`,
`docs/r8_dicionario_epocas_opcoes.md`, `docs/posicionamento_literatura.md`.

**Convenção epistêmica.** Uso os níveis do próprio projeto (1 / 2a / 2b / 3)
para o que o repositório **derivou**; tudo que for **opinião minha ou
inferência de literatura** vem marcado como *[opinião]* ou *[verificar]*.
Não modifiquei nada fora deste arquivo.

---

## Resumo executivo (10 linhas)

1. O fundo está no **ramo finito** (r: 0 → r_∞), corretamente identificado, com
   limite GR primordial exato e aceleração tardia — isto é bimétrica padrão,
   bem executada, e a literatura confirma o quadro (nível 2a/3).
2. O ponto cego mais grave do parecer é histórico e não foi confrontado: o
   ramo finito é exatamente o ramo que Könnig–Akrami–Amendola–Motta–Solomon
   (1407.4331) declaram **instável por gradiente** em altos redshifts, e o
   "ramo infinito" que o repo descarta é o que eles promovem (IBB).
3. A cascata R-7 mede autovalores **cinéticos** e taxas de envelope; ela **não
   mede c_s²** no limite k → ∞. Instabilidade de gradiente não é fantasma:
   ela passa incólume por todos os gates atuais.
4. O sinal está no próprio repo: R-7e reporta ω²(Ẽ) < 0 na janela inteira,
   variando de −10² a −10⁷ — lido como "artefato de envelope". Isso pode ser
   artefato **ou** ser exatamente λ₁ = −k²(2w₁+1) de Comelli–Crisostomi–Pilo.
   > **[NOTA DO REPOSITÓRIO — 2026-08-13]** Resolvido, e a alternativa era
   > falsa: aquele sinal específico não era nem artefato de envelope nem
   > c_s² < 0 — `W/K` simplesmente não é a frequência efetiva do sistema
   > (R-9, Bloco 0). Mas a instabilidade de gradiente que este parecer temia
   > **existe**, em outra época (r → 0), e é a de 1407.4331. Nota completa
   > no P3.
5. m_T ≈ 2.3 H₀ é resultado sólido e **não é surpresa**: é a assinatura
   genérica de auto-aceleração bimétrica. Cai confortavelmente acima do
   limite inferior publicado m_FP ≳ 1.2 H₀ (Högås–Mörtsell 2101.08795).
6. Corolário estrutural forte, que o repo ainda não enunciou: m_T/H ∈ [2.3, 3.5]
   em **todas** as épocas ⇒ o comprimento de Compton do gráviton massivo é
   sempre ~ raio de Hubble ⇒ toda a física distintiva está no
   super/quase-horizonte, em qualquer época.
7. Isso implica um risco estratégico: o "teste decisivo" do cap. 09 (baixo-ℓ,
   ISW, Gpc) é a janela **limitada por variância cósmica**. É plausível que o
   R-8 completo entregue "indistinguível" — resultado caro e pouco falsificável.
8. A alavanca observacional barata e sub-explorada é o **fundo**: w_eff(z) do
   ramo finito vs DESI DR2 BAO + SNe. Já há literatura de 2025 dizendo que
   bimétrica melhora o ajuste e alivia H₀ (2507.03743) — o repo não computou w_eff.
9. No β-constante o sistema é literalmente **HR ⊕ escalar livre** (o próprio
   cap. 07 diz: acoplamento Ẽ–δχ exatamente 0). Um R-8 sobre o benchmark testa
   bimétrica, não a TDCP. O que distingue a TDCP exige F′ ≠ 0 — e ali há uma
   trajetória, uma célula (2b).
10. Veredito curto: setor escalar são e fundo correto são conquistas reais;
    mas o programa observacional está desenhado para a janela errada primeiro,
    e falta um teste (gradiente) que a literatura considera decisivo.

---

## Pontos fortes

**F1. A identificação do ramo e a constraint de Bianchi correta.**
`manuscript-v2/04_bianchi_e_vinculos.md` §1–2 corrige ℬ(r)(H_g − ξH_f) = 0 para
ℬ(r)(N_f ȧ − N_g ḃ) = 0, com duas rotas independentes (canônica e lagrangiana),
nível 1. O argumento de que uma constraint canônica não pode conter o lapso é
o tipo de teste de sanidade que separa trabalho sério de trabalho apressado.
Daí sai ṙ = H_g(ξ − r) e o ramo finito com r ∝ a³ primordial. *[opinião]* Este
é o resultado metodologicamente mais forte do corpus.

**F2. Limite GR primordial exato e Higuchi automático.**
`docs/resultado_ramo_finito.md` §1,3: H²/(ρ/3M_g²) = 1.0000 e
m_T²/H² → 12 no primordial, independente de β_n, M_f, M_eff, m — logo Higuchi
(m_T² ≥ 2H²) satisfeito com fator 6 de folga. Nível 2a com verificação numérica
(12.002 em a = 0.02). O próprio repo já classifica o corolário qualitativo como
conhecido (Könnig 1503.07436; De Felice et al. 1404.0008), e a razão numérica
universal como sharpening novo — classificação correta e honesta
(`docs/posicionamento_literatura.md` §1).

*Extensão gratuita que o repo deveria publicar junto* (D3 da própria fila):
na álgebra do §3 daquele doc, ξ = r[1 + 3(1+w)] e m_T²/H² → 3ξ/r, logo

  **m_T²/H² → 3[1 + 3(1+w)]**  ⇒ 12 (matéria), **15 (radiação)**, 6 (Λ, w = −1).

Isto responde o D3 de `posicionamento_literatura.md` §2 sem nova integração e
converte "constante da era de matéria" em "função universal de w". *[opinião:
verificar a álgebra no script do fundo antes de imprimir; o passo é elementar
mas usa o mesmo limite r → 0.]*

**F3. O Erratum-02 e a reexecução completa.**
`manuscript-v2/07_setor_escalar.md` §Ato 2: bug de dupla contagem de Ċ em
`reduz_ponto`, promovendo Ψ_f (direção de **vínculo** secundário HR) a DOF.
A queda em cinco passos — reauditoria externa independente, r6b (60 dígitos),
r6c (identidade exata off-shell das duas ações, nível 1), r6d (bug linha a
linha, det K₂ → 1e-33…1e-40), consistência com HR e com o setor escalar FRW de
Comelli–Crisostomi–Pilo — é, *[opinião]*, o melhor pedaço de higiene científica
do repositório. Retirar publicamente uma previsão própria (o excesso ISW 2–8×)
por bug próprio é raro e deve ir para o paper como parágrafo, não como nota.

**F4. A contagem 2 é a contagem certa.**
No vácuo bimétrico o setor escalar propaga 1 DOF (helicity-0 do gráviton
massivo); com φ₋ dinâmico, 2. Bate com Hassan–Rosen (1106.3344, 1109.3515) e
com Comelli–Crisostomi–Pilo 1403.5679. A verificação de que **W00 nunca cruza
zero** ao longo da trajetória de rolagem/pouso (`resultado_r7e_saude_interna.md`
§1, 4 modos × 14 000 pontos) é o teste certo para a sobrevivência da eliminação
de Ψ_f no regime não-fatorado. Nível 2b, fronteira declarada (uma trajetória).

**F5. A âncora analítica do espectador.**
`resultado_r7_cascata.md` §1: ω² = k²/a² + U″ e taxa tardia
−3/2 + √(9/4 − U″/H²) medidas com fechamento em 0.01–0.02. Isso é a assinatura
de um escalar canônico em FRW — e serve de **validação da maquinaria**, não só
de resultado. Um pipeline de perturbações que reproduz o resultado analítico
trivial num canal é um pipeline que se pode começar a acreditar no outro canal.

**F6. μ, Σ como razões de resposta bimétrico/GR.**
`docs/resultado_r8a_quase_estatico.md` §1: mesma fonte, mesmo H(a), toda
convenção e normalização cancela. Construção limpa. E o fraseado corrigido
pós-review ("nenhum desvio acima do piso QS de ~2% foi detectado"; os 0.66% são
valor central, não previsão de precisão) é exatamente o rigor que um referee
exige. O uso de kh = k/(aH) — adimensional — para tornar o enunciado
independente de dicionário é um bom truque e está corretamente argumentado.

**F7. O fold do R-8b e a morte do postulado 30–300 H₀.**
`docs/resultado_r8b_limite_mH0.md` §2: r²𝒱_f(r) = β₄r² + 3β₂ + β₁/r tem mínimo
positivo (0.3 em r = 1) na forma-β do benchmark; com H tardio fixo,
s ≤ 3μH*²/(0.3 m_eff²) ≈ 6.2, fold numérico em s ≈ 5.7. Resultado analítico +
numérico (2b) que **converte um postulado herdado em obstrução estrutural**.
Independente de eu concordar com a leitura (ver P7), o método — transformar um
número postulado em quantidade derivada e deixar o modelo falar — é o correto.

**F8. Consistência do valor m_T ≈ 2.3 H₀ com o vínculo publicado.**
Högås & Mörtsell, *Constraints on bimetric gravity II* (arXiv:2101.08795,
JCAP 05 (2021) 002) obtêm limite **inferior** m_FP ≳ 1.2 H₀ (equivalente a
m_FP > 2.5h × 10⁻³³ eV/c², Compton ~ horizonte observável). A predição
m_T/H₀ ∈ [2.26, 2.41] está acima e próxima do limite — ou seja, a família do
benchmark cai **dentro** da região viável publicada, num canto estreito.
*[verificar: o m_FP deles é a massa de Fierz–Pauli no fundo hoje; confirmar que
a fórmula do projeto (`derivations/02_setor_tensorial_mT2.md`) é a mesma
quantidade e não difere por fator de normalização de M_eff.]*

**F9. Higiene de supersessão.**
`resultado_r7_cascata.md` §4 e `07_setor_escalar.md` §4 mantêm tabelas
explícitas do que caiu e do que fica. Isso é raro e é exatamente o que permite
a um revisor externo trabalhar rápido sem citar números mortos.

---

## Pontos fracos e riscos

**P1 [CRÍTICO]. O confronto com a instabilidade de gradiente do ramo finito
não foi feito — e é o resultado da literatura que mais ameaça a F1.**
Könnig, Akrami, Amendola, Motta & Solomon, *Stable and unstable cosmological
models in bimetric massive gravity* (arXiv:1407.4331, PRD 90, 124014) concluem
que **todos** os modelos do ramo finito sofrem instabilidade de gradiente no
setor escalar em altos redshifts, e identificam o *infinite-branch bigravity*
(IBB, β₁β₄) como o único caso com fundo viável **e** perturbações lineares
estáveis. Reforços: Comelli–Crisostomi–Pilo 1403.5679 (autovalor
λ₁ = −k²(2w₁ + 1)); Könnig–Amendola 1402.1988 (modelo mínimo); Könnig
1503.07436 (Higuchi vs gradiente); Lagos–Ferreira 1410.0207.
`docs/posicionamento_literatura.md` §1 **registra** esses papers e até diz "o
paper TEM que compará-las explicitamente" — mas a cascata R-7 (2026-08-12) não
executou essa comparação, e o cap. 07 não a menciona. O repo escolheu o ramo
que a literatura reprova e descartou o ramo que a literatura promove, sem
endereçar o conflito. *[opinião: este é o item #1 do parecer. Um referee de
PRD/JCAP levanta isso no primeiro parágrafo.]*

**P2 [CRÍTICO]. Os gates do R-7 são cegos a gradiente por construção.**
Todos os critérios reportados são: (i) autovalores de K₂ (fantasma), (ii) W00
sem cruzar zero (vínculo), (iii) taxas de envelope / ganho de campo G_win,
(iv) lnA de passagem. **Nenhum deles é sign(c_s²)**. Instabilidade de gradiente
é ω² < 0 com |ω²| ∝ k² — matriz cinética positiva, vínculos intactos, e o modo
explode com taxa ~ k/a. Os testes do R-7 rodam em kh ∈ {0.2 … 20} e a passagem
é justamente **de kh alto para kh baixo** (20 → 0.2), ou seja, na direção que
*desliga* o efeito. O regime perigoso (kh ≫ 1, alto z, até o corte de EFT) é
exatamente o que não foi amostrado.

**P3 [CRÍTICO]. Há um sinal explícito de gradiente nos próprios dados e ele foi
arquivado como artefato.**
`resultado_r7e_saude_interna.md` §2 (A1): *"ω²(Ẽ) = W/K é **negativo** na janela
inteira e varia 5 ordens de magnitude (−1e2 → −1e7 em kh=10)"*. A conclusão do
doc — que o **envelope** normalizado por ω²(t) fabricava crescimento — está
correta como diagnóstico do envelope, mas **não explica o sinal de ω²**. Duas
leituras possíveis, e o repo não decidiu entre elas:
  (a) ω² = W/K não é a relação de dispersão física (mistura com C, sistema 2×2,
      K quase singular) e o sinal é irrelevante — plausível, dado que o campo
      medido decai (G_win = −10);
  (b) ω² < 0 com |ω²| crescendo é literalmente c_s² < 0, e a medida de decaimento
      não a viu porque a janela de kh testada é curta e o intervalo temporal é
      curto comparado com 1/|ω|.
  Nota quantitativa que agrava (b): |ω²| ~ 10⁷ (em unidades de H²) ⇒ |ω|/H ~ 3×10³.
  Um modo com |ω| ≫ H e ω² < 0 cresceria como e^{|ω|t} — inconciliável com
  G_win = −10 ao longo de vários e-folds. Ou seja: **os dois números do próprio
  doc são mutuamente incompatíveis sob a leitura ingênua**, o que significa que
  a quantidade "ω² = W/K" não está sendo interpretada corretamente em algum
  lugar. Isso precisa ser resolvido antes de qualquer enunciado de saúde. *[opinião]*

> **[NOTA DO REPOSITÓRIO — 2026-08-13, pós-R-9/R-10a/R-11/R-12. O texto do
> parecer acima fica intacto; esta é anotação, não reescrita.]** O P3 foi
> resolvido, e o parecer acertou **duas vezes, em objetos diferentes**.
>
> **Era a leitura (a).** O R-9 (Bloco 0), item (c), mediu: `ω² = W/K` **não é
> a relação de dispersão na convenção do repositório**. O integrador resolve
> `K q̈ + (K̇ + C − Cᵀ) q̇ + (Ċ + W) q = 0`, logo a frequência efetiva é
> `(Ċ + W)/K` — exatamente a "mistura com C" que o parecer apontou — e essa
> razão é **positiva**. **16/32 entradas têm `W/K < 0` e `(Ċ+W)/K > 0`**:
> todas as do modo métrico, nos dois fundos, em todas as épocas. Em a = 200,
> `W/K = −1.5e5 H²` contra `(Ċ+W)/K = +514 H²`. O discriminador de frequência
> fecha o caso: se `|W/K|` fosse a frequência haveria ~110 cruzamentos de zero
> na janela, e medem-se **6** (a WKB pela frequência correta prevê 6.5). E a
> "nota quantitativa que agrava (b)" — |ω|/H ~ 3×10³ inconciliável com
> G_win = −10 — estava **certa, e era o sintoma**: os dois números do doc eram
> mesmo mutuamente incompatíveis, precisamente porque a quantidade medida não
> era a frequência. Fonte: `docs/resultado_r9_bloco0.md` §1;
> `docs/resultado_r7e_saude_interna.md` §2 foi corrigido.
>
> **E o P1/P2 se confirmou — por outra via.** A leitura (b) deste P3 errou o
> *lugar* do fenômeno, mas a preocupação central do parecer estava certa
> quanto ao *fenômeno*: os gates do R-7 são **cegos a gradiente por
> construção** (P2), e o "no-go revogado" era **forte demais** (veredito,
> item 2). O **A1**, que este parecer pôs como recomendação nº 1, rodou e
> encontrou **instabilidade de gradiente real**: `c_s² < 0` em todo o regime
> r → 0 (`docs/resultado_r10a_gradiente.md`), elevada a **no-go de classe por
> gradiente** em 108/108 células da forma-β
> (`docs/resultado_r11_nogo_gradiente.md`) e fixada, com instrumento limpo, em
> **c_s² = −1 exato** em r → 0 e **+1 exato** na era tardia, com troca de sinal
> em **a_cross = 0.578 ⟹ z_cross = 0.61** — a era instável **cobre a
> recombinação** (`docs/resultado_r12_instrumento_e_cs2.md`,
> `docs/resultado_r10_consolidado.md`). O P1 acertou também a fonte: a previsão
> de Könnig–Akrami–Amendola–Motta–Solomon ([arXiv:1407.4331]) para o *finite
> branch* **se reproduz na nossa implementação**. **O parecerista previu o
> desfecho, e o repositório o registra como tal.**
>
> Uma precisão sobre o mascaramento: ele não foi o da *direção da passagem em
> kh* que a leitura (b) conjecturou — foi o da **época**. Toda a cascata R-7
> rodou em a ∈ [100, 8e4], que nesta família é a era tardia (r = r_∞), onde
> c_s² é de fato positivo; o regime da alegação da literatura ficou fora **por
> construção**. O próprio P2 já havia nomeado esse regime: *"o regime perigoso
> (kh ≫ 1, alto z, até o corte de EFT) é exatamente o que não foi amostrado"*.
> Era.

**P4 [GRAVE]. O fundo é dust+Λ. Sem radiação, o cap. 09 é indefinível.**
`r8_dicionario_epocas_opcoes.md` já lista o problema, mas o custo está
subestimado. Sem ρ_r: (i) não existe z_eq, logo não existem picos acústicos,
logo C_ℓ^{TT,TE,EE} não é computável nem em princípio; (ii) o limite universal
m_T²/H² → 12 é da era de matéria e vale 15 na radiação (ver F2) — os enunciados
"primordiais" do cap. 05 e do `resultado_ramo_finito.md` §3 estão, hoje,
**rotulados errado** (dizem "universo primordial", significam "era de matéria");
(iii) BBN não foi confrontado — Högås & Mörtsell, arXiv:2106.09030
(JCAP 11 (2021) 001) derivam vínculos de BBN sobre o ângulo de mistura
(θ ≲ 18° para m_FP ≳ 10⁻¹⁶ eV) que a F1 tem de satisfazer. No ramo finito o
limite GR é exato em a → 0, então *[opinião]* a F1 deve passar trivialmente —
mas "deve passar" não é "passou", e o vínculo real é sobre a **normalização de
G_N cosmológico vs local**, que o repo nunca tratou.

**P5 [GRAVE]. A época do pouso de φ₋ é a variável mais perigosa e está solta.**
A trajetória REF tem janela de deslocamento ordem-1 em a ∈ [225, 7086]
(`resultado_r7e_saude_interna.md` §1) e cruzamentos testados até a_cross = 30000
(`resultado_r7_cascata.md` §3), tudo em unidades de código, sem âncora de a₀.
Se o pouso cair depois da recombinação (z ≲ 1100), um deslocamento |H − rH_f|/H
até 0.48 é uma modificação de ordem 50% da relação entre os dois setores
**dentro** da janela em que o CMB é formado e propagado — a probabilidade de
sobreviver aos dados é *[opinião]* baixa. Se cair muito antes, a física
distintiva da TDCP fica invisível e o modelo degenera em bimétrica + Λ. Não há,
no material lido, nenhum mecanismo que **amarre** essa época: v★, g e m² são
escolhas. Isto é um ajuste, e o paper precisa dizê-lo com essa palavra.

**P6 [GRAVE]. No benchmark β-constante a TDCP não é distinguível de
"bimétrica ⊕ quintessência".**
`resultado_r7_cascata.md` §1: *"Acoplamento K₂/C₂/W₂ entre Ẽ e δχ:
**exatamente 0**"*; e o cap. 07 chama o benchmark de "HR + espectadores". Então
todo o programa R-8a/R-8b/R-8-completo, se rodado sobre o benchmark, mede
Hassan–Rosen com um escalar livre acoplado só via fundo. Isso tem duas
consequências desagradáveis: (i) os resultados observacionais serão
**reprodutíveis pela literatura bimétrica existente** e o repo estará
redescobrindo números publicados; (ii) a única física TDCP genuína (F′ ≠ 0,
não-fatoração da constraint, pouso) está apoiada em **uma trajetória, uma
célula** (2b) e nunca foi levada ao regime observacional. O centro de gravidade
declarado no cap. 09 está, portanto, deslocado do centro de gravidade da teoria.

**P7 [MÉDIO]. A leitura do fold ("30–300 H₀ é inalcançável") é mais estreita do
que o texto sugere.**
O fold é derivado com a **forma-β do benchmark sob rescala uniforme** e com
**H tardio fixo** (`resultado_r8b_limite_mH0.md` §1 e §4 — o próprio doc declara
a fronteira). Na literatura, m_FP ≫ H₀ é rotina: obtém-se com **ângulo de
mistura pequeno** (M_f/M_g e β₁ pequenos, com β₀ fornecendo Λ), que é o canto
ΛCDM-like do espaço de parâmetros de Högås–Mörtsell (2101.08794/08795). Ou seja,
"exige outra forma-β + ajuste fino U₀ < 0" é verdade *dentro do dial escolhido*,
mas pode ser falso no espaço de parâmetros completo. **Risco de enunciado
sobre-generalizado no paper.** Correção barata: mapear (β_n, μ = M_f/M_g) do
benchmark para o par (θ, m_FP) da parametrização de Högås–Mörtsell e mostrar
onde o benchmark cai no plano publicado.

**P8 [MÉDIO]. Contagem de parâmetros vs poder de predição.**
Entre β₀…β₄, m, M_f/M_g, U₀, U″(v), v★, g, o modelo tem *[estimativa minha]*
~10 parâmetros contra 6 do ΛCDM — e o enunciado atual é
"observacionalmente indistinguível e não-excluída" (cap. 09 §3). Um modelo com
mais parâmetros e nenhuma assinatura é penalizado por qualquer critério de
informação. O paper precisa de um **inventário de parâmetros** com (i) quais
são fixados pelas âncoras, (ii) quais são degenerados, (iii) quais são
realmente livres — e do Δχ² honesto, não só de "passa nos limites".

**P9 [MÉDIO]. O integrador do fundo não é de qualidade CMB — e não precisa existir.**
`resultado_r7e_saude_interna.md` §5 declara ±2e-3 entre Heun e Euler na janela e
±O(1) de sistemática nos lnA do pousado; `05_fundo_ramo_finito.md` §4 registra
M0 = 3e-4 e cadeia rp de 1ª ordem. Para C_ℓ é preciso ~10⁻⁵–10⁻⁶ relativo em
H(a) ao longo de ~10 décadas em a. **Mas**: o cap. 05 §1 diz que no ramo
cinemático *r é fixado instante a instante pela densidade* pela cúbica. Logo,
com β constantes o fundo **não precisa de integração nenhuma** — é raiz
algébrica por continuação a cada a, com precisão de máquina. A integração só é
necessária com modulação. *[opinião: substituir o fundo β-constante integrado
por solução algébrica elimina a sistemática ±O(1) de graça e deve ser feito
antes do R-8.]*

**P10 [MÉDIO]. O R-8a não foi validado contra fórmulas QS publicadas.**
Solomon, Akrami & Koivisto, *Linear growth of structure in massive bigravity*
(arXiv:1404.4061, JCAP 1410:066) e Könnig–Amendola 1402.1988 dão expressões
quase-estáticas fechadas para μ(a,k) e Σ(a,k) no setor bimétrico. Reproduzi-las
com a maquinaria do repo é um teste de aceitação de meio dia e vale mais, para
um referee, do que qualquer gate interno. Sem isso, "|μ−1| ≤ 0.66%" é um número
sem controle externo. *[verificar as convenções: aqueles trabalhos usam y = b/a
e β_n normalizados de forma ligeiramente diferente.]*

**P11 [MÉDIO]. Nenhum enunciado super-horizonte, nenhuma IC adiabática.**
Todos os testes de perturbação vivem em kh ∈ [0.2, 20]; as "ICs" são vetores
de teste (métricas ou dchi), e o próprio R-7b admite que lnA de passagem
*"é sensível ao estado de entrada"* e *"não é invariante de k"*. Isso é aceitável
como diagnóstico de saúde, mas não é física observável. Falta: (i) limite
k → 0, (ii) conservação de ζ no modo adiabático, (iii) decisão explícita sobre
isocurvatura em δφ₋. Sem (i)–(iii), C_ℓ de baixo-ℓ é incomputável.

**P12 [MENOR, mas de honestidade]. Rótulos de época e âncoras heterogêneas.**
`05_fundo_ramo_finito.md` §2 usa Ω_m ≈ 0.25 no "hoje natural"; o R-8b ancora
Ω_m(a₀) = 0.3; Planck dá 0.315. O cap. já pede que se cite a âncora — bom — mas
o número 0.25 não deve aparecer em tabela de resultado sem a marca de que é
consequência de uma escolha de "hoje", não predição.

**P13 [MENOR]. Setor tensorial observacional intocado.**
Com m_T ≈ 2.3 H₀ há oscilações gráviton-gráviton em escala de Hubble
(ver *Gravitational wave oscillations in bimetric cosmology*, arXiv:2309.08536)
— irrelevante para LIGO/Virgo (m_g < 1.2×10⁻²² eV ≈ 10¹¹ H₀ não vincula nada
aqui) e para c_T (matéria acopla só a g ⇒ c_T = 1, GW170817 satisfeito por
construção), mas potencialmente relevante para modos B primordiais. Vale um
parágrafo, nem que seja para dizer "nulo".

---

## Propostas de modelagem

### A. Antes de qualquer C_ℓ: três testes baratos que podem matar ou salvar a F1

**A1 — Teste de gradiente (prioridade máxima; ~1 sessão).**
No sistema 2-DOF corrigido, com β constantes e no fundo do ramo finito, extrair
a relação de dispersão do modo métrico no limite k → ∞:
  - diagonalizar (K, C, W) mantendo apenas o termo líder em k²; definir
    c_s² ≡ lim_{k→∞} W_kk/(K · a²) na base canônica (não em "W/K" bruto —
    ver P3);
  - varrer **z de 0 até o corte de EFT**, com kh ∈ {10, 10², 10³, 10⁴};
  - comparar com λ₁ = −k²(2w₁ + 1) de Comelli–Crisostomi–Pilo 1403.5679,
    calculando w₁ analiticamente para a forma-β do benchmark.
  **Critérios pré-declarados:** (a) c_s² ≥ 0 em toda a trilha ⇒ o repo contradiz
  1407.4331 e isso é *resultado de primeira ordem*, que exige explicação
  (diferença de convenção? β₂,β₄ ≠ 0 abrindo janela estável? μ = M_f/M_g?);
  (b) c_s² < 0 ⇒ medir z_inst(k), comparar a taxa |k c_s|/a com H e com o corte
  Λ₃, e adotar/refutar a rota de escape de Akrami–Hassan–Könnig–Schmidt-May–
  Solomon (arXiv:1503.07521, PLB 748, 37: M_f pequeno empurra a instabilidade
  para antes do BBN / acima do corte, onde o tratamento linear não vale);
  (c) resultado ambíguo por má condicionamento ⇒ é **falha de maquinaria**, não
  resultado, e bloqueia o R-8.
  *Observação:* o scan μ ∈ {0.3, 1, 3, 10} do R-7f já é o dial de Akrami et al.
  — basta reler o resultado nessa linguagem.

**A2 — w_eff(z) do ramo finito vs DESI DR2 (prioridade alta; ~meia sessão).**
O fundo é nível 2a e já existe. Computar
w_eff(z) ≡ p_int/ρ_int a partir da cúbica e comparar com os contornos
(w₀, w_a) de DESI DR2 + Pantheon+/Union3/DES-Y5. A literatura de 2025 diz que
bimétrica dá energia escura **fantasma** e melhora o ajuste: *Bimetric gravity
improves the fit to DESI BAO and eases the Hubble tension*, arXiv:2507.03743
(PRD 112, 103515, 2025), com H₀ = 69.0 ± 0.4 km/s/Mpc e a tensão caindo de 5σ
para 3.7σ. *[verificar autoria e números na fonte antes de citar.]*
  **Critérios:** Δχ²(F1 vs ΛCDM) em BAO+SNe; se a F1 reproduzir a fenomenologia
  fantasma, **isto — e não o baixo-ℓ — é o enunciado observacional publicável do
  repo hoje**, e não é limitado por variância cósmica. Se a F1 divergir do ramo
  finito padrão da literatura, é sinal de erro de convenção e deve ser
  investigado antes de tudo.

**A3 — Reprodução das fórmulas QS publicadas (validação; ~meio dia).**
Ver P10. Aceitação: μ, Σ do repo vs 1404.4061 dentro de 1% no regime de validade
comum. Falha ⇒ o R-8a não é citável.

### B. O pipeline R-8 completo — passo a passo com critérios de falha

**Passo 0 — Dicionário (decisão do autor, mas com recomendação).**
Recomendo a **Opção B** de `r8_dicionario_epocas_opcoes.md`, não a C→A. Razão:
comparabilidade. Adotar a parametrização (θ, m_FP, Ω_m, H₀) de Högås–Mörtsell
para o setor métrico e montar φ₋ por cima. Isso (i) permite citar e reusar
vínculos publicados em vez de reinventá-los, (ii) transforma P7 em resultado,
(iii) dá ao referee um mapa. Âncoras: T_CMB, N_eff = 3.044, ω_b de BBN,
Ω_m(a₀) = 0.315, e **a época do pouso de φ₋ declarada como parâmetro**, com prior
z_pouso > 1100 como escolha default (justificar ou varrer).
  *Falha:* se não existir membro da família com Ω_m ∈ [0.28, 0.34] e
  H₀ ∈ [65, 75] simultaneamente ao fold do R-8b, a família do benchmark está
  observacionalmente excluída no fundo — e isso encerra a questão barato.

**Passo 1 — Fundo com radiação.**
ρ = ρ_γ + ρ_ν + ρ_b + ρ_cdm + U(φ₋); r por **raiz algébrica com continuação**
(P9), não por ODE, quando F′ = 0; ODE só na trajetória modulada, com integrador
de ordem ≥ 4 e controle de erro relativo.
  *Aceitação:* |H_F1/H_ΛCDM − 1| < 10⁻³ para z ∈ [10³, 10¹⁰]; ΔN_eff efetivo
  < 0.2 em BBN (confrontar 2106.09030); m_T²/H² → 15 na era de radiação
  (predição de F2 — se o número der outro, há erro em algum lugar).

**Passo 2 — Gauge e variáveis.**
Bimétrica tem **um único** grupo de difeomorfismos: fixar o gauge no setor g
consome toda a liberdade, e as quatro funções escalares de f (Φ_f, B_f, E_f, Ψ_f)
são físicas ou vinculadas — não há liberdade residual para "fixar E_f = 0".
Recomendo: **gauge newtoniano (longitudinal) em g** (que o R-8a já usa),
Ẽ = k²E_f como variável métrica dinâmica (como no R-7a), Ψ_f eliminado via W00.
Para a hierarquia de matéria, usar as equações newtonianas de CLASS (que existem
em ambos os gauges) e **não** síncrono, para evitar o modo de gauge residual
misturar-se com o modo bimétrico quase-horizonte. Anotar explicitamente o mapa
para a convenção Ψ-temporal da v2 (cap. 09 §4.1 já pede isso).
  *Falha:* qualquer resultado que dependa do gauge escolhido em kh ≲ 1.

**Passo 3 — Condições iniciais.**
(i) Derivar o limite k → 0 do sistema 2-DOF na era de radiação; (ii) impor o
modo adiabático crescente padrão (δ_γ = 4/3 δ_b = 4/3 δ_c, etc.) e resolver o
**modo bimétrico atrator** (o sistema é overdamped: existe um ramo que decai,
que deve ser projetado fora, e um ramo forçado pela matéria, que é a IC certa);
(iii) declarar δφ₋ inicial = 0 (adiabático puro) como default e tratar
isocurvatura de φ₋ como extensão separada.
  *Aceitação (gate obrigatório):* ζ conservado a < 0.5% para kh < 10⁻² entre
  z = 10⁸ e z = 10⁴. Se ζ não se conservar, ou a redução está errada, ou existe
  um DOF a mais, ou as ICs estão contaminadas pelo modo decaindo — em qualquer
  caso, **stop**.

**Passo 4 — Duas rotas para o observável (fazer 4a antes de 4b).**

*4a — Rota "(μ, Σ) exatos", barata e suficiente para baixo-ℓ.* Como o escalar
métrico é overdamped e o espectador tem c_s = 1, a resposta do sistema a uma
fonte de matéria pode ser tabulada **sem aproximação quase-estática**: resolver
o sistema linear 2-DOF forçado por δ_m(a,k) e extrair μ(a,k), Σ(a,k) e o slip
η(a,k) **exatos** em kh ∈ [10⁻³, 10³]. Alimentar CLASS pela interface de
gravidade modificada (ou um cálculo de Green para o ISW,
ΔT/T|_ISW = 2∫ ∂_τ(Φ+Ψ)/2 dτ). Entrega: C_ℓ^{TT} em ℓ < 100, ISW-galáxia
cruzado, P(k) até k ~ 10⁻³ h/Mpc.
  *Critérios de falha:* |ΔC_ℓ^{TT}/C_ℓ| acima de 2× a variância cósmica
  (√(2/(2ℓ+1))) em qualquer ℓ ≤ 30 ⇒ excluído/detectável; abaixo de 1× ⇒
  **declarar indistinguível e parar** (não construir 4b).

*4b — Boltzmann completo, só se 4a indicar sinal.* Fork de **CLASS**, não
hi_class nem EFTCAMB. Razão técnica: hi_class (Zumalacárregui, Bellini, Sawicki,
Lesgourgues, Ferreira, arXiv:1605.06102) e EFTCAMB (Hu, Raveri, Frusciante,
Silvestri, arXiv:1312.5742) parametrizam **Horndeski / EFT of DE**: uma métrica
+ um escalar, via α_K, α_B, α_M, α_T. Bimétrica não é Horndeski — tem uma
segunda métrica com seus próprios modos tensoriais e um helicity-0 que não é um
escalar de Horndeski. Mapear a F1 nesses códigos exigiria uma redução
quase-estática que **destrói exatamente a janela que se quer medir**. A
arquitetura de referência correta é o módulo `perturbations_scalar_field` de
CLASS estendido para um multipleto (Ẽ, δχ) com matriz de acoplamento (K, C, W)
tabulada a partir da biblioteca simbólica do repo — mantendo os gates V-XREP
como testes de regressão do módulo.
  *Aceitação:* reproduzir ΛCDM a < 0.1% no limite β₁ → 0 (ou m → ∞); reproduzir
  4a a < 5% na banda de sobreposição.

**Passo 5 — Confronto e pré-registro.**
Critérios de falseamento escritos e commitados **antes** da primeira rodada
(cap. 02 do manuscrito já exige): lista fechada com valores numéricos para
Δχ²(BAO+SNe), ΔC_ℓ baixo-ℓ, fσ₈, S₈, BBN, e o teste A1 de gradiente.

### C. O que confrontar da literatura bimétrica (lista fechada)

| # | Referência | Por que é obrigatória |
|---|---|---|
| 1 | Könnig, Akrami, Amendola, Motta, Solomon, arXiv:1407.4331 (PRD 90, 124014) | Instabilidade de gradiente do **ramo finito**; IBB como o modelo estável. Confronto direto com a escolha de ramo do repo. |
| 2 | Comelli, Crisostomi, Pilo, arXiv:1403.5679 | λ₁ = −k²(2w₁+1); é o teste A1 em forma analítica. |
| 3 | Könnig, arXiv:1503.07436 | Higuchi ⇔ r′ ≥ 0 e a relação com gradiente; já citado, falta usar. |
| 4 | Akrami, Hassan, Könnig, Schmidt-May, Solomon, arXiv:1503.07521 (PLB 748, 37) | A rota de escape via M_f pequeno — o dial μ do R-7f já a implementa sem saber. |
| 5 | Könnig, Amendola, arXiv:1402.1988 | Instabilidade do modelo mínimo β₁. |
| 6 | Solomon, Akrami, Koivisto, arXiv:1404.4061 | μ, Σ quase-estáticos publicados = alvo de validação do R-8a. |
| 7 | Lagos, Ferreira, arXiv:1410.0207 | Análise linear completa e contagem de DOFs — segunda âncora para o Erratum-02. |
| 8 | Högås, Mörtsell, arXiv:2101.08794 e 2101.08795 (JCAP 05 (2021) 001, 002) | Vínculos analíticos + observacionais; m_FP ≳ 1.2 H₀; parametrização (θ, m_FP) para o Passo 0 e para P7. |
| 9 | Högås, Mörtsell, arXiv:2106.09030 (JCAP 11 (2021) 001) | BBN; vínculo sobre o ângulo de mistura. |
| 10 | arXiv:2507.03743 (PRD 112, 103515, 2025) | DESI DR2 BAO + H₀: o benchmark observacional atual da bimétrica. *[verificar autoria]* |
| 11 | Lüben, Mörtsell, Schmidt-May, arXiv:1812.08686; *Vainshtein screening in bimetric cosmology*, PRD 102, 123529 | Testes locais/Vainshtein — permite **citar em vez de re-derivar** o bloco PPN da v1 (cap. 09 §4). |
| 12 | Aoki, Maeda, Namba, arXiv:1506.04543 | Cura não-linear da instabilidade primordial; define a fronteira do enunciado linear do repo. |
| 13 | De Felice, Mukohyama, Uzan, arXiv:1702.04490; +Oliosi 1711.04655 | Chameleon bigravity = classe-irmã com fator global; a lacuna hamiltoniana declarada é a oportunidade do repo (já mapeado em `posicionamento_literatura.md`). |
| 14 | *Gravitational wave oscillations in bimetric cosmology*, arXiv:2309.08536 | Setor tensorial observacional (P13). |
| 15 | Brizuela et al., arXiv:2507.11526 | Estado 2025 do debate sobre quebra da PT linear — contexto do Ato 2. |

---

## Veredito do especialista (5 linhas)

1. O corpus corrigido é **tecnicamente competente e epistemicamente honesto**:
   Bianchi correta (nível 1), ramo finito com limite GR exato (2a), setor
   escalar de 2 DOFs verificado em muitos regimes (2b) e uma retratação pública
   de previsão própria. Isso é mais qualidade de método do que a maioria dos
   papers de gravidade modificada apresenta.
2. Mas a **saúde perturbativa está declarada sem o teste que a literatura
   considera decisivo para este ramo**: instabilidade de gradiente. Os gates do
   R-7 são cegos a ela, e há um sinal ambíguo (ω² < 0 em 5 ordens de magnitude)
   arquivado como artefato. Enquanto A1 não rodar, "no-go revogado" é forte demais.
   > **[NOTA DO REPOSITÓRIO — 2026-08-13]** O A1 rodou: **c_s² = −1 exato** em
   > r → 0, elevado a no-go de classe por gradiente em 108/108 células
   > (`docs/resultado_r10a_gradiente.md`,
   > `docs/resultado_r11_nogo_gradiente.md`,
   > `docs/resultado_r12_instrumento_e_cs2.md`). O "no-go revogado" **era**
   > forte demais: este item do veredito estava certo. O sinal ambíguo do
   > R-7e, porém, era questão separada — `W/K` não é a frequência efetiva
   > (R-9, Bloco 0). Nota completa no P3.
3. A escolha de janela do cap. 09 está, na minha opinião, invertida: o teste
   decisivo proposto (baixo-ℓ/ISW) é o mais caro **e** o mais limitado por
   variância cósmica; o teste barato e discriminante (w_eff(z) do fundo vs DESI
   DR2) não foi feito e já existe pronto no nível 2a.
4. m_T ≈ 2.3 H₀ é resultado real, mas é a **assinatura genérica de
   auto-aceleração bimétrica**, não uma predição exclusiva da TDCP; e no
   benchmark β-constante a teoria é HR ⊕ escalar livre. A TDCP propriamente
   dita vive em F′ ≠ 0, com uma trajetória e uma célula de suporte.
5. Recomendação: **não iniciar o R-8 completo**. Rodar A1 (gradiente), A2
   (w_eff vs DESI) e A3 (validação QS contra 1404.4061) primeiro — três sessões
   que decidem se há teoria para levar a um Boltzmann, e que, no melhor caso,
   já entregam o primeiro enunciado observacional citável do projeto.
