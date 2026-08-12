# 04 — Vínculos e a constraint de Bianchi correta

**Aqui o Erratum-01 vira conteúdo, não errata.** Porte de
`auditoria/erratum_01_bianchi.md` (nível 1: duas rotas independentes)
e do Gate 2 (`docs/gate2_ghost.md`, `auditoria/code/gate2_bracket.py`,
`gate2_fatoracao.py`), com o estado pós-R-7 anotado.

## 1. A forma do corpus era impossível — e o sintoma estava à vista

A v1 escrevia a constraint de Bianchi como
ℬ(r)·(H_g − ξH_f) = 0, com ℬ(r) = β₁+2β₂r+β₃r². O sintoma que deveria
ter denunciado o erro: **essa forma contém o lapso** (via ξ). Uma
constraint canônica genuína é relação entre variáveis de espaço de
fase e é livre de lapso por construção. A forma correta:

$$\boxed{\;\mathcal B(r)\,\big(N_f\,\dot a - N_g\,\dot b\big) = 0\;}$$

equivalentemente ℬ(r)·(ȧ/N_g − ḃ/N_f)·(fatores positivos) = 0.

**Duas rotas independentes** (mesma lagrangiana de minisuperespaço
como única premissa comum — verificada termo a termo no lote 7):

- **Canônica** (`gate2_bracket.py`): o bracket {ℋ_g, ℋ_f} das duas
  constraints primárias produz o fator (M_g²a·p_b − M_f²b·p_a) ∝
  (ȧ/N_g − ḃ/N_f).
- **Lagrangiana** (`bianchi_rota_lagrangiana.py`): a consistência
  temporal do vínculo de N_g deixa o resíduo
  3M_eff²m²(N_f ȧ − N_g ḃ)(β₁a²+2β₂ab+β₃b²)/N_g. Teste por
  substituição: anular o candidato do corpus deixa resíduo; anular o
  canônico zera exatamente.

*Nível 1.*

## 2. Os dois ramos da fatoração — e o que cada um custou à v1

Com β_n constantes, a constraint fatora em duas famílias:

**Ramo algébrico:** ℬ(r) = 0 ⟹ r = r★ fixo. Estático por construção
(e, com modulação global, incapaz de se mover — cap. 03 §0).

**Ramo cinemático (o "finito"):** N_f ȧ = N_g ḃ, isto é ξ = ḃ/ȧ.
Substituindo em ṙ = r(ḃ/b − ȧ/a):

$$\boxed{\;\dot r = H_g\,(\xi - r)\quad (N_g=1)\;}$$

**ṙ só se anula se ξ = r; genericamente r evolui.** E neste ramo
H_g/H_f = r, **não** ξ.

Isso inverteu a âncora D5 da auditoria ("ṙ≡0", consequência correta
de premissa errada — retirada) e desmontou os benchmarks "ramo
dinâmico" de D1/D2/D8, que impunham ξ = H_g/H_f — o que equivale a
impor ξ = r, justamente o caso estático, avaliado porém em pontos
onde a igualdade não valia (r=1.2, ξ=3.497). A lição de método: *o
"duplamente morto" do parecer perdeu as duas pernas de uma vez — não
porque a física melhorou, mas porque a premissa era uma só.*
*Fonte: erratum-01 §4–6.*

## 3. Com modulação, a constraint NÃO fatora — a terceira estrutura

Com β₁ = β₁(φ₋), o teste correto de fatoração (anular na raiz;
`gate2_fatoracao.py` — o teste original por divisão era vácuo e foi
substituído) dá, avaliado em r = r★(φ₋):

$$\{\mathcal H_g,\mathcal H_f\}\big|_{r_\star} =
-M_{\rm eff}^2 m^2\, p_\phi\, \beta_1'(\phi_-) \;\neq\; 0$$

A obstrução só se anula se p_φ = 0 (φ₋ congelado) ou β₁′ = 0 (sem
modulação) — exatamente quando a v2 degenera na v1. **A dicotomia
"ramo algébrico OU ramo dinâmico" é artefato de β constantes.** Com
modulação, a solução vive **deslocada da raiz** por δ ∝ p_φβ₁′ — a
própria constraint proíbe ficar sobre a raiz enquanto φ₋ evolui.
*Nível 2a (bracket simbólico).*

Este deslocamento deixou de ser curiosidade formal: é ele que a Fase
A mediu como deslocamento ordem-1 dos dois ramos durante a
condensação (|H − rH_f|/H até 0.48), e é nessa janela que o R-7e
verificou a saúde da estrutura de vínculos em nível perturbativo
(§4). *Fontes: `docs/resultado_investigacao2_faseA.md`,
`docs/resultado_r7e_saude_interna.md`.*

## 4. Gate 2 — o fantasma de Boulware–Deser sob β_n(φ₋)

Contagem alvo: 7 (gráviton sem massa + massivo) + 2 (escalares
primordiais) = **9 graus físicos**; 10 = fantasma BD de volta.

**Parte A (linearidade nos lapsos): RESOLVIDA, nível 2a.** O ponto é
elementar: φ₋ é escalar e o valor de um escalar num ponto não depende
do lapso; β_n(φ₋) é coeficiente que varia no espaço-tempo e a
estrutura de lapso do potencial HR (após a redefinição de shift) é
intocada — a constraint primária sobrevive à modulação.
*Fonte: gate2_ghost.md §2.*

**Parte B (a constraint secundária): analítica ainda ABERTA; suporte
dinâmico 2b forte.** O risco real era a secundária — que agora
depende de φ₋ — falhar em regime dinâmico. O que há de novo,
pós-Erratum-02: no sistema de perturbações corrigido, a direção Ψ_f é
vínculo exato no benchmark (det K = 0 simbólico; cap. 07), e ao longo
da trajetória de rolagem/pouso — incluindo a janela de deslocamento
do §3 — o coeficiente auxiliar W00 que legitima a eliminação de Ψ_f
**nunca cruza zero** (R-7e, 4 modos × 14 000 pontos): a estrutura de
vínculos aguenta o regime não-fatorado em nível linear. Isso é
verificação numérica com fronteiras declaradas (2b, uma trajetória) —
**não substitui** a prova analítica do bracket {𝒞, H_φ} que o Gate 2
exige em 2a; substitui apenas o medo por um prior informado.
*Fontes: erratum-02, resultado_r7e_saude_interna §1.*
