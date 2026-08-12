# Parecer — Astrofísica

**Emitido em:** 2026-08-13.
**Escopo:** objetos compactos, ondas gravitacionais, formação de
estrutura não-linear, testes astrofísicos de gravidade modificada.
**Base documental (leitura fechada, declarada):** `manuscript-v2/01_tese.md`,
`06_setor_tensorial.md`, `07_setor_escalar.md`, `09_programa_observacional.md`;
`docs/resultado_r7_cascata.md` (incl. §4, tabela de supersessão);
`docs/resultado_r8a_quase_estatico.md`; `docs/resultado_r8b_limite_mH0.md`;
`derivations/02_setor_tensorial_mT2.md`; `docs/resultado_ramo_finito.md`;
`docs/posicionamento_literatura.md`. Nenhum número anterior a 2026-08-12
foi reutilizado sem o filtro de supersessão de `resultado_r7_cascata.md` §4.

**Convenção de atribuição usada em todo o parecer:**

- **[REPO nível N]** — derivado no repositório, com o nível epistêmico
  que o próprio repositório declara (2a = simbólico com auto-testes;
  2b = numérico com fronteiras declaradas; 3 = literatura).
- **[CONTA-MINHA]** — aritmética ou álgebra que eu fiz aqui, a partir de
  fórmulas do repositório. **Não verificada pelos scripts do projeto.**
  Toda peça deste tipo vem com o insumo explícito para reexecução.
- **[OPINIÃO]** — juízo de especialista, não derivação.
- **[verificar]** — identificador bibliográfico ou valor numérico externo
  de que não tenho certeza suficiente para citar sem ressalva.

---

## Resumo executivo

1. Do lado astrofísico, a F1 pós-Erratum-02 **não tem nenhum problema de
   viabilidade conhecido** — e esse é simultaneamente seu maior mérito e
   seu maior problema.
2. GW170817 é passado **estruturalmente, não por ajuste**: o potencial
   Hassan–Rosen é algébrico (sem derivadas) e a matéria acopla só a g, logo
   c_g² = 1 identicamente; a onda observada é a de g. [REPO 2a + OPINIÃO]
3. c_f² = ξ²/r² ≠ 1 **ajuda** na propagação: a quebra de degenerescência
   de gradiente suprime a mistura g↔f na banda LIGO a ~10⁻⁴¹. Oscilação
   de gráviton é um não-problema aqui. [CONTA-MINHA]
4. m_T ≈ 2.3 H₀ ≈ 3.3×10⁻³³ eV está **10 ordens de grandeza** abaixo do
   limite de dispersão GWTC-3 e ~4 ordens abaixo dos melhores limites de
   estrutura em grande escala. Nenhum limite astrofísico de massa morde.
5. O raio de Vainshtein com essa massa é ~70 pc para o Sol, ~0.7 Mpc para
   a Via Láctea e ~7 Mpc para um aglomerado: **tudo que é ligado está
   profundamente blindado**. PPN e pulsares binários devem passar com
   folga de ordens — mas isso ainda **não foi derivado** nesta v2.
6. O corolário é duro: **não há separação de GR em nenhuma escala
   astrofísica** — nem halos, nem lente forte, nem dinâmica de aglomerado,
   nem sirenes padrão. [CONTA-MINHA + OPINIÃO]
7. Toda a alavanca observacional está onde o cap. 09 já a colocou: kh ≲ 22,
   ℓ ≲ 10, escalas ≳ Gpc — a região de variância cósmica irredutível.
8. Identifico um parâmetro organizador que o programa não isolou:
   ε ≡ K_ℓℓ/K_hh = μ r³/ξ (μ = M_f²/M_g²). Ele **é** a visibilidade do
   segundo setor; nem o R-8a nem o R-8b varreram μ. [CONTA-MINHA]
9. Duas lacunas de gate, não de refino: **buracos negros** (instabilidade
   tipo Gregory–Laflamme de spin-2 massivo) e **Vainshtein/PPN**, ambos
   ausentes da fila R-8 do cap. 09.
10. Veredito curto: teoria **saudável, blindada e quase-invisível**. O R-8
    decide entre "excluída no baixo-ℓ" e "indistinguível para sempre" — e
    o segundo desfecho é, na minha estimativa, o mais provável.

---

## Pontos fortes

**PF-1. c_g² = 1 é estrutural, não ajustado — GW170817 não pode
falsificar esta classe.**
A derivação obtém K_hh = M_g²a³/4 e c_g² = 1 exatamente, com o setor χ
incluído via √−g (obrigatório: sem ele "o gráviton ganharia massa espúria
até em GR"). [REPO nível 2a — `derivations/02_setor_tensorial_mT2.md` §3.1;
`manuscript-v2/06_setor_tensorial.md` §1]
Acrescento o argumento estrutural que o repositório não enuncia: o
potencial HR é **algébrico** em g e f, sem derivadas; logo só pode gerar
termos de massa, nunca corrigir o termo de gradiente de h. Com matéria
acoplada exclusivamente a g, fótons e ondas gravitacionais compartilham o
mesmo cone nulo em **qualquer** fundo, não só em FLRW. [OPINIÃO, com base
na estrutura da ação]
Externo: |c_gw/c − 1| ≲ 10⁻¹⁵ de GW170817/GRB 170817A
(Abbott et al. 2017, ApJL **848**, L13, arXiv:1710.05834). Esta é
exatamente a razão pela qual a bigravity sobreviveu ao corte que
devastou Horndeski (Ezquiaga & Zumalacárregui, PRL **119**, 251304,
arXiv:1710.05901; Creminelli & Vernizzi, arXiv:1710.05877; Baker et al.,
arXiv:1710.06394).
**Ressalva a declarar:** a imunidade é contingente à escolha arquitetural
"matéria só em g". Um acoplamento duplo (métrica efetiva g–f) reintroduz
c_gw ≠ 1 e a classe volta a ser cortável. Isso deve aparecer como
**escolha estrutural declarada** no cap. 01, não como resultado.

**PF-2. A mistura g↔f é irrelevante em toda a banda de detectores — e
c_f ≠ c_g é o que a torna irrelevante.**
O repositório derivou c_f² = ξ²/r² e registrou corretamente que, com
c_g² ≠ c_f², gradiente e massa **não são simultaneamente
diagonalizáveis** [REPO 2a — `derivations/02...` §4]. A consequência
observacional não foi extraída; extraio-a aqui.
[CONTA-MINHA] Na banda LIGO (f ≈ 100 Hz), o ângulo de mistura entre h e ℓ
é governado por sin²θ ~ m_T²/(k²|c_g²−c_f²|). Com m_T ≈ 2.3 H₀ ≈
5×10⁻¹⁸ s⁻¹, ω = 2πf ≈ 6.3×10² s⁻¹ e |c_g²−c_f²| = O(10) hoje (ver CM-1
abaixo): sin²θ ≲ 10⁻⁴¹. A fase de oscilação acumulada em D = 40 Mpc é
Δφ = m_T²D/(2ω) ≈ 10⁻²² rad.
**Conclusão:** o modo detectado é h puro a 1 parte em 10⁴⁰; oscilação de
onda gravitacional **não é risco**. Isso é um resultado positivo e
publicável em si: o mecanismo de Max, Platscher & Smirnov
(PRL **119**, 111101, 2017; arXiv:1703.07785 — **verificado na busca**)
é construído na degenerescência c_f = c_g; a quebra ξ ≠ r **desliga o
canal**. Ver também arXiv:1912.06104 e arXiv:2601.15201 [verificar
autores de ambos].

**PF-3. m_T/H₀ cravado ∈ [2.26, 2.41] é rigidez genuína — o tipo de
propriedade que um testador quer.**
O *fold* em s ≈ 5.7 (analítico s_max ≈ 6.2) fecha a família e converte a
massa do gráviton de parâmetro em predição, com desvios de crescimento
≤ 0.012% em toda ela. [REPO nível 2b — `docs/resultado_r8b_limite_mH0.md`
§2; `manuscript-v2/09_programa_observacional.md` §2]
[OPINIÃO] Modelos de gravidade modificada quase sempre têm um dial que
absorve o vínculo; aqui o fundo o proíbe. Isso é raro e deve ser vendido
como tal — desde que acompanhado da ressalva do PFr-4 (a *ordem de
grandeza* m ~ H₀ é genérica em bigravity viável; o coeficiente é que é
novo).

**PF-4. Higuchi automático com margem de fator 6, e a razão universal
m_T²/H² → 12.**
[REPO 2a estrutural + 2b (12.002 em a = 0.02) —
`docs/resultado_ramo_finito.md` §3; `manuscript-v2/06...` §2]
Externo, corretamente já mapeado pelo próprio repositório: o corolário
qualitativo (viabilidade ⇒ r′ ≥ 0 ⇒ sem fantasma de Higuchi) é provado
em geral por Könnig (arXiv:1503.07436); ver também De Felice et al.
(arXiv:1404.0008) e Fasiello & Tolley (arXiv:1206.3852, 1308.1647).
[`docs/posicionamento_literatura.md` §1]

**PF-5. A revogação do no-go foi feita do jeito certo, e isso importa
para o parecer astrofísico.**
Cinco passos verificáveis, identidade exata off-shell entre duas ações
(r6c, aritmética racional), reprodução independente do resultado externo
(r6d), e concordância com a contagem de Hassan–Rosen e
Comelli–Crisostomi–Pilo. [REPO nível 1 (r6c) + 2b —
`manuscript-v2/07_setor_escalar.md` Ato 2]
[OPINIÃO] Do meu lado da mesa, o que isso compra é confiança
metodológica: quando o R-8 produzir um C_ℓ, eu vou acreditar no pipeline.
Isso é mais raro do que parece — o precedente D5 (extended quasidilaton
"is ghost free" revertido pelo próprio autor) está no
`posicionamento_literatura.md` §2 e é exatamente o erro que este programa
não cometeu.

**PF-6. A invalidação da âncora D8 é um estudo de caso reaproveitável.**
Impor ξ = H_g/H_f (em vez da constraint correta H_g/H_f = r) forçava
β₁+β₂(ξ+r) = −0.88 < 0 e portanto m_T² < 0 **por construção**; no fundo
correto o mesmo fator vale +0.72. [REPO 2b —
`docs/resultado_ramo_finito.md` §4; `manuscript-v2/06...` §4]
[OPINIÃO] Vale como parágrafo de método no paper: "violação de Higuchi"
reportada sem o fundo on-shell é rotineiramente um artefato de
parametrização, e a comunidade de gravidade massiva já tropeçou nisso.

---

## Pontos fracos e riscos

**PFr-1. (CRÍTICO) c_f > 1 relativo ao cone da matéria — derivado e
nunca interpretado.**
[REPO 2a] A fórmula c_f² = ξ²/r² está derivada; o ramo finito dá ξ = 4r
no limite primordial de matéria (`docs/resultado_ramo_finito.md` §2), logo
**c_f² = 16, isto é, c_f = 4c**, durante toda a era de matéria primordial.
[CONTA-MINHA — generalização, ver CM-2] na era de radiação ρ ∝ a⁻⁴ dá
ξ = 5r e **c_f = 5c**.
O repositório não tem uma única linha sobre a estrutura causal disso.
Riscos concretos, em ordem de severidade:
1. Cones não-encaixados (f estritamente mais largo que g) é precisamente
   a configuração que a literatura de gravidade massiva associa a
   acausalidade e a problemas de boa-posição do problema de Cauchy —
   Deser & Waldron, PRL **110**, 111101 (arXiv:1212.5835); Deser, Izumi,
   Ong & Waldron, PLB **726**, 544 (arXiv:1306.5457).
2. Superluminalidade no IR é o gatilho canônico das cotas de
   positividade/analiticidade: Adams, Arkani-Hamed, Dubovsky, Nicolis &
   Rattazzi, JHEP **0610**, 014 (hep-th/0602178). O repositório **já
   cita** Alberte, de Rham, Jaitly & Tolley (arXiv:1910.11799) em
   `posicionamento_literatura.md` §1 como obstáculo do programa (b1) —
   as ferramentas estão na bibliografia e não foram aplicadas ao próprio
   c_f.
3. Boa-posição/hiperbolicidade do sistema bimétrico com cones distintos
   tem literatura numérica própria (Kocic, Torsello, Högås & Mörtsell;
   p.ex. arXiv:1904.06305 [verificar]).
**Defesa possível** (e é uma defesa razoável): nada observável propaga em
f, então não há curva tipo-tempo fechada no setor de matéria em nível
linear. **Mas isso precisa ser um enunciado derivado e declarado, não uma
omissão.** [OPINIÃO] Se eu fosse referee de PRD, este seria meu primeiro
pedido.

**PFr-2. (CRÍTICO) Buracos negros: zero análise, e existe uma
instabilidade conhecida no regime exato desta teoria.**
Não há uma linha sobre objetos compactos em nenhum dos arquivos lidos.
Soluções bi-Schwarzschild proporcionais são soluções exatas da bigravity,
e suas perturbações contêm um spin-2 massivo — que é **linearmente
instável** por um mecanismo tipo Gregory–Laflamme para m·r_s ≲ 0.4:
Babichev & Fabbri (CQG **30**, 152001, arXiv:1304.5992); Brito, Cardoso &
Pani (PRD **88**, 023514, arXiv:1304.6725); revisão Babichev & Brito
(CQG **32**, 154001, arXiv:1503.07529). [LITERATURA nível 3]
[CONTA-MINHA] Com m_T ≈ 3.3×10⁻³³ eV, **todo** buraco negro astrofísico
está em m·r_s ~ 10⁻²³ — o interior profundo da janela instável. A escala
de tempo no limite m·r_s → 0 é justamente o ponto que precisa ser
recalculado [verificar: não tenho certeza suficiente do comportamento
assintótico da taxa para afirmá-lo aqui].
**Por que isso é gate e não refino:** se a instabilidade for rápida em
escala astrofísica, a teoria morre por observação de buracos negros
(EHT, ringdown de GWTC) independentemente de qualquer C_ℓ. Se for lenta,
custa um parágrafo. De qualquer forma é barato de decidir e caro de
ignorar.

**PFr-3. (CRÍTICO) O bloco Vainshtein/PPN continua não re-derivado — e é
o único gate que pode matar a teoria antes da cosmologia.**
O cap. 09 registra honestamente: "o bloco aritmético Vainshtein/PPN e o
formalismo HR do Anexo A permanecem como material de partida, a
re-derivar" [`manuscript-v2/09...` §4, parágrafo final]. Concordo com o
diagnóstico e discordo da prioridade: isso não é "quando o R-8 alcançar",
é **antes** do R-8.
Razão: sem Vainshtein, o gráviton massivo entrega a descontinuidade vDVZ
e γ_PPN = 1/2, contra Cassini γ − 1 = (2.1 ± 2.3)×10⁻⁵ (Bertotti, Iess &
Tortora, Nature **425**, 374, 2003). Nenhum C_ℓ salva isso.
[CONTA-MINHA — estimativas que sugerem que a notícia é boa, mas que
**não substituem a derivação**]:
- r_V = (r_s/m_T²)^{1/3}: Sol ≈ **70 pc**; Via Láctea (10¹² M☉) ≈
  **0.7 Mpc**; aglomerado (10¹⁵ M☉) ≈ **7 Mpc**.
- Resíduo típico de Vainshtein (r/r_V)^{3/2} na órbita de Saturno:
  ~6×10⁻¹⁰ — quatro ordens abaixo de Cassini.
Ou seja: **se** o mecanismo funcionar como na bigravity padrão
(Babichev & Crisostomi, PRD **88**, 084002, arXiv:1307.3640; ver também
arXiv:1812.08686, "compatível com testes locais" [verificar autores]),
o sistema solar passa com folga enorme. O que falta é exatamente a parte
não-trivial: **existência** do regime Vainshtein *nesta* família, e o
*matching* da solução estática à condição de contorno cosmológica
r(∞) = r(a₀) — que a v1 nunca fez e a v2 ainda não fez.

**PFr-4. O risco escondido não é o gráviton — é φ₋.**
No benchmark β-constante, F′ = 0 e φ₋ é espectador puro: nenhuma quinta
força. [REPO 2b — `manuscript-v2/07...` Ato 3] Mas a arquitetura da F1 é
β_n(φ₋), e o cap. 08 quer **derivar** o elo Φ₋ → φ₋ → r.
[CONTA-MINHA] A dispersão medida do espectador é ω² = k²/a² + U″ com
U″ ≈ 0.3 H² [`docs/resultado_r7_cascata.md` §1, âncora
−3/2+√(9/4−0.3/H²)] ⇒ m_φ ≈ 0.55 H₀ ⇒ comprimento de Compton ~8 Gpc.
Um escalar ultraleve **sem mecanismo de Vainshtein próprio** (não é
Galileon) e sem massa que o blinde. Se ele adquirir acoplamento
conforme/disforme à matéria via a modulação, precisa de camaleão ou
symmetron para sobreviver a Cassini e ao Lunar Laser Ranging.
Âncora existente e já na bibliografia do projeto: chameleon bigravity, De
Felice, Mukohyama & Uzan (arXiv:1702.04490) e com Oliosi
(arXiv:1711.04655) — o repositório registra que "interaction terms play
the role of a potential for φ" [`posicionamento_literatura.md` §1].
[OPINIÃO] Este é o item que eu apostaria como o mais provável de gerar um
problema real, e ele está ausente de todas as filas.

**PFr-5. (ESTRUTURAL) A visibilidade do segundo setor não foi isolada — e
nem o R-8a nem o R-8b varreram o dial que a controla.**
[CONTA-MINHA — CM-3, a peça central deste parecer]
Da própria derivação tensorial, K_hh = M_g²a³/4 e K_ℓℓ = M_f²b³/(4ξ),
logo

    ε(a) ≡ K_ℓℓ/K_hh = μ r³/ξ ,      μ ≡ M_f²/M_g²

com ε → μ r²/4 no limite primordial (ξ = 4r, r → 0) e ε ≈ μ r∞² ≈ 0.11 μ
no ponto fixo tardio (ξ = r, r∞ ≈ 0.33).
Este único número organiza **tudo** o que este parecer encontrou:
1. Explica por que o célebre m_T²/H² → 12 é observacionalmente inócuo:
   o modo que carrega essa massa vive quase inteiramente em ℓ, cujo peso
   cinético se anula como r² no primordial. A massa efetiva sentida pelo
   próprio h vale ~3 μ r² H² → 0. **Higuchi com margem 6 é verdade sobre
   um modo que quase não nos toca.**
2. Explica por que o sub-horizonte dá 10⁻⁴ (R-8a/R-8b) e por que a única
   janela sobrevivente é tardia e de escala Gpc: ε só sobe quando r sobe.
3. **É o parâmetro que decide se a teoria é falseável.** O R-8a rodou dois
   fundos (β₁ = 1 e 4.47) e o R-8b varreu s (escala global dos β_n
   preservando a forma-β). **Nenhum dos dois varreu μ.** Se μ ≪ 1 a F1 é
   exatamente ΛCDM em toda parte e o R-8 completo produzirá um nulo caro
   e não-informativo.
O próprio `posicionamento_literatura.md` §1 já registra que "μ→0 como
limite GR desacoplante é conhecido" (Akrami et al., arXiv:1503.07521) —
a âncora existe, a consequência para o desenho do R-8 não foi tirada.
*(Identificação de μ com M_f²/M_g² inferida de H*² = s·m_eff²·r²𝒱_f/(3μ)
em `resultado_r8b...` §2 confrontada com a Friedmann-f de
`resultado_ramo_finito.md` §3 — confirmar no código antes de citar.)*

**PFr-6. Nenhuma escala astrofísica separa a teoria de GR. Isso precisa
ser dito no manuscrito, não descoberto por um referee.**
[CONTA-MINHA + OPINIÃO] Somando PFr-3 e PFr-5: λ_C = 1/m_T ≈ **1.9 Gpc**,
e r_V de qualquer estrutura ligada excede o tamanho da própria estrutura
por ordens de grandeza. Consequências:
- Perfis de halo, dinâmica de aglomerados, lente forte, lente fraca em
  escalas de halo: **blindados** — GR restaurada.
- Entre r_V e λ_C a força extra é essencialmente **constante** (e^{−r/λ_C}
  ≈ 1 até Gpc), logo é reabsorvida na definição de G_N medido. Não é
  assinatura, é renormalização.
- Sirenes padrão / d_L^GW vs d_L^EM: o cinético de g é M_g²a³/4 sem
  correr, logo α_M = 0 e não há assinatura. Somado a PF-2 (mistura
  10⁻⁴¹), o canal GW está **fechado**.
Conclusão que o cap. 09 deve absorver: a lista "o que é testável
astrofisicamente" tem, hoje, **um item** — o quase-horizonte. Todo o
resto é nulo por construção.

**PFr-7. Risco de leitura: "banda morta" ≠ "sem assinatura ISW".**
O R-7b/c mede lnA de passagem de modos **homogêneos** do sistema 2-DOF
(kh 20 → 0.2), obtendo −8.4 (estático) e −11.0…−14.7 (pousado)
[REPO 2b — `docs/resultado_r7_cascata.md` §2–3]. Isso é enunciado de
**estabilidade**, não de Φ_g **fisicamente fontado** por matéria. O ISW
depende do decaimento do Φ sourced, não do autovalor homogêneo.
O repositório está formalmente correto (retirou uma previsão positiva; não
afirmou uma nova — `resultado_r7_cascata.md` §5 item 4), mas o risco de
que a frase "a banda está morta" seja lida como "não há ISW anômalo" é
alto, inclusive internamente. [OPINIÃO] Blindar com uma frase explícita no
cap. 07 e no cap. 09.

**PFr-8. m_T ≈ 2.3 H₀ é menos novo do que soa, e o repositório sabe
disso pela metade.**
A ordem de grandeza m ~ H₀ é **genérica** em bigravity auto-acelerada: é a
própria condição de a interação fazer o papel de Λ. O
`posicionamento_literatura.md` §1 já classifica o ramo finito como "já
conhecido" (Könnig et al. arXiv:1407.4331; Akrami et al. arXiv:1503.07521).
O que é novo é o **coeficiente cravado** e o *fold*. [OPINIÃO] Vender
"m_T ≈ 2.3 H₀ é predição" sem esse qualificador é o tipo de coisa que um
referee corta em duas linhas. E testar 2.3 contra, digamos, 1.5 exige medir
um efeito de quase-horizonte com precisão melhor que ~30% — ver PFr-9.

**PFr-9. A janela decisiva é a janela limitada por variância cósmica.**
[CONTA-MINHA] Em kh ≈ 1 a estrutura (m/aH)²/kh² do R-8a extrapola para
O(1) — coerente com o repositório apontar o quase-horizonte como decisivo,
e é uma boa notícia (há efeito). Mas o ISW é uma fração subdominante do
C_ℓ^TT em ℓ ≲ 10, e a variância cósmica ali é ~1/√(2ℓ+1) ≳ 20%. Mesmo uma
modificação de fator ~2 no ISW rende, na melhor das hipóteses, ~2–3σ
combinando TT de baixo-ℓ com a correlação cruzada ISW–LSS (que tem, ela
própria, significância global de poucos σ — Planck 2015 XXI,
arXiv:1502.01595 [verificar a significância exata]).
[OPINIÃO] O desfecho realista do R-8 é bimodal e **assimétrico**: ou o
efeito é grande e a família já está excluída pelo Planck existente, ou é
pequeno e a teoria fica permanentemente indistinguível. Não existe zona
confortável no meio. Isso deve entrar nos critérios pré-declarados
(cap. 09 §4 item 4) — ver PM-4.

**PFr-10. Regime forte não coberto: geração ≠ propagação.**
[CONTA-MINHA] A escala de forte acoplamento Λ₃ = (m_T² M_Pl)^{1/3} ≈
3×10⁻¹³ eV ⟺ **~10³ km**. Toda a física de geração de ondas (raio de
estrela de nêutrons ~10 km; horizonte de BH estelar ~30 km; a própria
fusão de GW170817) acontece **abaixo** da escala de corte ingênua da EFT.
A resposta padrão é o *redressing* de Vainshtein (o corte efetivo sobe
dentro de r_V), mas o repositório não estabelece nada disso.
Enunciado seguro que a v2 pode fazer hoje: "a F1 não modifica a
**propagação** de ondas gravitacionais". Enunciado que a v2 **não** pode
fazer hoje: qualquer coisa sobre **geração**, ringdown ou fusão.

**PFr-11. A teoria não alivia nenhuma tensão atual — e portanto não tem
motivação fenomenológica.**
[CONTA-MINHA + OPINIÃO] Com H(a) tardio fixado por construção na família
R-8b e desvios de crescimento ≤ 0.012% na janela observável, a F1 não toca
H₀ nem S₈. Não é um defeito lógico; é um fato estratégico. A motivação da
F1 tem de ser **conceitual** (cap. 08: o elo Φ₋ → φ₋ → r), e o manuscrito
deve dizer isso de frente, porque um referee de cosmologia observacional
vai perguntar "para que serve?" na primeira página.

**PFr-12. Vazios de fronteira herdados, menores mas citáveis.**
[REPO, fronteiras declaradas] R-8a: matéria só como fonte, χ̄ parado, sem
radiação/neutrinos/bárions, unidades de código
[`docs/resultado_r8a_quase_estatico.md` §4]. Ramo finito: só Higuchi
testado; nem screening solar nem fσ₈ verificados
[`docs/resultado_ramo_finito.md` §5(c)]. Nenhuma dessas fronteiras é
escondida — o repositório é exemplar nisso — mas juntas significam que
**nenhum confronto com dado real foi feito até hoje**, e o cap. 01 já
afirma isso ("Não afirma validação observacional"). Manter essa frase
literalmente no abstract do paper.

---

## Propostas de modelagem (priorizadas)

Ordenadas por **razão decisão/custo**, não por elegância. As três
primeiras são baratas e podem mudar o desenho do R-8; por isso vêm
**antes** dele.

### PM-1 (barato, ~1 dia; fecha um item aberto do próprio repositório)
**Estender o limite primordial a w geral.** Fecha o desafio **D3** de
`docs/posicionamento_literatura.md` §2 ("o 12 é por era; fazer antes que o
referee faça") e entrega um companheiro que ninguém pediu.
[CONTA-MINHA — CM-2, álgebra a validar com
`derivations/code/02_setor_tensorial_mT2.py`]: no ramo finito r ∝ ρ⁻¹ ∝
a^{3(1+w)}, logo κ ≡ ξ/r = 1 + 3(1+w) = 4 + 3w, e no limite r → 0

| | m_T²/H² → 3(4+3w) | c_f² = (4+3w)² |
|---|---|---|
| Radiação (w = 1/3) | **15** | **25** (c_f = 5c) |
| Matéria (w = 0) | **12** ✓ (reproduz o repo) | **16** (c_f = 4c) |
| dS tardio (κ → 1, ṙ → 0) | — (fórmula não vale: r ↛ 0) | **→ 1** |

Três ganhos: (i) fecha D3 com fórmula fechada em vez de um número por era;
(ii) mostra que **Higuchi é automático para todo w ≥ −1** (3κ ≥ 3 > 2),
o que é mais forte que o enunciado atual; (iii) revela que a mesma álgebra
governa c_f — e portanto que o item PFr-1 tem uma expressão universal.
Bônus estrutural: **c_f² → 1 no ponto fixo tardio**, porque ṙ = H_g(ξ−r)
= 0 ⇒ ξ = r. A superluminalidade é um fenômeno primordial que **se cura
sozinho** no dS tardio — este é um bom parágrafo de defesa contra PFr-1,
e é derivável da equação de fundo que o cap. 01 já cita.
*Verificar antes de publicar: reexecutar o script com ρ ∝ a⁻⁴.*

### PM-2 (barato, ~2–3 dias; decide se o R-8 vale o custo)
**Varrer μ = M_f²/M_g² no R-8a e medir a escala do sinal.**
Reusar `auditoria/code/r8a_quase_estatico_mu_sigma.py` sem mudar física:
varrer μ ∈ [0.01, 10] a kh e época fixos, e verificar se
|μ_MG − 1| ∝ ε = μ r³/ξ como CM-3 prevê. Duas saídas, ambas valiosas:
- se a escala confirmar, o programa ganha **um parâmetro de visibilidade**
  e pode pré-declarar a faixa de μ em que a F1 é falseável;
- se não confirmar, minha conta CM-3 está errada e é melhor descobrir
  agora do que no referee.
[OPINIÃO] Este é o item de maior alavancagem do parecer inteiro. Sem ele,
o R-8 completo corre o risco de custar meses para produzir um nulo que
era previsível em três dias.

### PM-3 (gate de sobrevivência; ~2–4 semanas; **antes** do R-8)
**Vainshtein/PPN, na ordem certa.** O cap. 09 coloca isto como "material
a re-derivar quando o R-8 alcançar"; recomendo inverter.
Ordem obrigatória:
1. **Solução estática esfericamente simétrica bi-métrica** na família do
   benchmark, com a condição de contorno **cosmológica**
   r(∞) = r(a₀) — o *matching* é a parte que a v1 nunca fez e é onde a
   física de ramo pode morder.
2. **Existência do regime Vainshtein e o expoente do resíduo** nesta
   família (âncora: Babichev & Crisostomi, arXiv:1307.3640).
3. **γ_PPN, β_PPN** vs Cassini (2.1 ± 2.3)×10⁻⁵ e vs LLR. Minha estimativa
   [CONTA-MINHA] diz ~10⁻⁹, com 4 ordens de folga — mas é estimativa de
   ordem, não derivação.
4. **A quinta força de φ₋ na versão modulada (F′ ≠ 0)** — PFr-4. Sem
   Vainshtein próprio; precisa de camaleão. Âncora obrigatória:
   arXiv:1702.04490.
Critério de gate: se (4) falhar, nenhuma cosmologia importa.

### PM-4 (o R-8 do cap. 09, com critérios que proponho pré-declarar)
Executar a fila 1–3 do `manuscript-v2/09...` §4 como está — com uma
adição: **pré-declarar os dois desfechos**, porque o cap. 02 exige e
porque PFr-9 mostra que a zona intermediária é estreita.
Proponho, para discussão do autor (números meus, [OPINIÃO], a calibrar
com a sensibilidade real do Planck):
- **Critério A — exclusão.** Se |ΔC_ℓ^TT/C_ℓ^TT| > 20% para qualquer
  2 ≤ ℓ ≤ 30, **ou** se a amplitude do ISW mudar > 50%, a família do
  benchmark está excluída pelos dados existentes. Fim de linha
  observacional, e um resultado publicável.
- **Critério B — indistinguibilidade.** Se o desvio máximo ficar < 2% em
  todo ℓ e todo k, declarar a F1 **observacionalmente indistinguível de
  ΛCDM** e **encerrar** o programa observacional, transferindo o ônus
  inteiro para o cap. 08 (o elo Φ₋ → φ₋ → r). Isso é um desfecho legítimo
  e deve ser dito antes, não depois.
- **Zona C** (2%–20%): a única em que vale escalar para likelihood
  completa. Estimo-a estreita.

### PM-5 (gate independente; ~2–4 semanas; pode matar a teoria sozinho)
**Buracos negros.** Não está em nenhuma fila e deveria ser gate.
1. Verificar que as soluções proporcionais (bi-Schwarzschild) existem no
   ramo finito da F1 e qual r local elas selecionam.
2. Recalcular a instabilidade tipo Gregory–Laflamme do spin-2 massivo no
   regime m_T r_s ~ 10⁻²³, e **extrair a escala de tempo** — o número que
   decide tudo (Babichev & Fabbri, arXiv:1304.5992; Brito, Cardoso & Pani,
   arXiv:1304.6725; revisão arXiv:1503.07529).
3. Se instável em escala astrofísica: confrontar com ringdown (GWTC) e
   com a estabilidade de sombras (EHT). Se estável: um parágrafo e segue.
[OPINIÃO] O custo de não fazer isto é um referee de objetos compactos
derrubar o paper com uma citação de 2013.

### PM-6 (menor, mas fecha o flanco de pulsares)
**Geração em binárias.** Radiação de polarizações extras com supressão de
Vainshtein, confrontada com o decaimento orbital de PSR J0737−3039 e
PSR B1913+16. Âncoras: de Rham, Tolley & Wesley (PRD **87**, 044025,
arXiv:1208.0580); de Rham, Matas & Tolley (PRD **87**, 064024,
arXiv:1212.5212). Espero supressão total [OPINIÃO], mas é o tipo de
enunciado que precisa de conta, não de expectativa — e responde
diretamente ao item "pulsares binários" do escopo deste parecer.

### PM-7 (resultado pequeno mas publicável, quase de graça)
**Teorema de imunidade a oscilação de gráviton.** Formalizar PF-2: em
bigravity com c_f ≠ c_g o canal de oscilação g↔f é suprimido por
m_T²/(k²|c_g²−c_f²|), e portanto **desligado** em toda a banda de
detectores. É uma delimitação útil do resultado de Max, Platscher &
Smirnov (arXiv:1703.07785), que opera na degenerescência. Custo: uma
seção; risco: verificar se alguém já publicou a versão com gradientes
não-degenerados [verificar].

### PM-8 (registro, custo trivial)
**BBN e o setor f.** O limite GR primordial é exato
(H²/(ρ/3M_g²) = 1.0000, `docs/resultado_ramo_finito.md` §1) e o gráviton
massivo não é termicamente produzido, logo N_eff é intocado. Uma frase no
cap. 09, para fechar a pergunta antes que seja feita.

---

## Veredito do especialista

1. **A F1 pós-Erratum-02 é, do ponto de vista astrofísico, saudável e
   segura — e é segura demais.** GW170817, limites de massa do gráviton
   (10 ordens de folga), crescimento e lente estão todos passados por
   estrutura, não por ajuste; o preço é que nenhuma escala astrofísica
   acessível separa a teoria de GR.
2. **Duas lacunas são de gate, não de refino, e ambas estão fora da fila
   do cap. 09:** Vainshtein/PPN (com o quinto-força de φ₋ na versão
   modulada como o risco real) e buracos negros (instabilidade de spin-2
   massivo). Recomendo movê-las para **antes** do R-8.
3. **Antes de gastar meses no R-8, gastar dias no PM-2:** se a
   visibilidade ε = μ r³/ξ for pequena na faixa de μ adotada, o R-8
   produzirá um nulo previsível — e é melhor saber disso antes.
4. **O manuscrito deve dizer explicitamente que a F1 não alivia nenhuma
   tensão observacional e que sua motivação é conceitual.** Essa é a
   posição honesta e é defensável; a alternativa é ser corrigido por um
   referee na primeira página.
5. **Prognóstico:** o R-8 termina em "indistinguível" com probabilidade
   substancialmente maior que em "excluída", e a zona intermediária é
   estreita. Isso não é fracasso — mas precisa ser pré-declarado como
   desfecho aceitável (PM-4, critério B), sob pena de o programa
   observacional ficar aberto indefinidamente à espera de um sinal que a
   variância cósmica não deixa aparecer.
