# Veredito Consolidado: o Setor Escalar do Ramo Finito

**Data:** 2026-08-07. Consolida `no_go_beta_constante.md`,
`estrutura_par_relativo.md` e a rodada final de `modulacao_qep.py`.
Este documento é o fechamento do arco iniciado no Erratum 01.

---

## 1. A cadeia de evidência completa

| # | Resultado | Nível | Fonte |
|---|---|---|---|
| 1 | A constraint de Bianchi do corpus estava errada; a correta é $\mathcal B(r)(N_f\dot a - N_g\dot b)=0$ | **1** (duas rotas independentes) | Erratum 01 |
| 2 | No ramo finito corrigido: $\dot r\neq0$, limite GR exato, Higuchi 400/400, $m_T^2/H^2\to12$ universal | 1–2b | `resultado_ramo_finito.md` |
| 3 | O par escalar relativo é taquiônico ($\sigma\approx(3\text{–}4)H$) **no ponto fixo**, onde o congelamento é exato | **2b forte** (sem caveat de congelamento) | `resultado_setor_escalar.md` §7 |
| 4 | Nenhum β constante cura: taquião em μ≥0.3, fantasma em μ=0.1, ~1500 pontos, 4D | 2b (fronteira declarada) | `no_go_beta_constante.md` |
| 5 | A doença mora no **setor de vínculos**: dubleto de shifts (B_g±B_f) em μ~1; lapso Φ_f em μ→0, com $|k_N|\sim\mu^3$ | 2b + composição de autovetores | `estrutura_par_relativo.md` |
| 6 | A modulação β₁(φ₋) **não cura e piora**: em μ=1, σ/H sobe 3.65→3.85–4.43 monotonicamente em g; em μ=0.1 o fantasma quase-nulo nunca vira (kN −2e−5→−5e−3 com g) e em g=4 o taquião retorna | 2b (knobs declarados) | `modulacao_qep.py`, rodada final |

## 2. O diagnóstico do mecanismo (por que a modulação não podia curar)

A tabela da varredura separou os dois canais da modulação:

- **Canal Fb** (deslocamento de β₁eff): move a teoria **dentro** do
  espaço-β — que é integralmente doente (resultado 4). Não há região
  saudável para onde ir. Subir β₁eff até 17 confirmou.
- **Canal Fp/Fpp** (misturas derivativas com δφ₋): **repulsão de
  níveis** — misturar um modo saudável com o taquião empurra o taquião
  para baixo, e com o fantasma quase-nulo empurra a norma para mais
  negativa. Confirmado empiricamente **nos dois regimes**
  independentes.

A conexão do Gate 2 (o termo $p_\phi\beta_1'$ entra na constraint
secundária, exatamente o setor da doença) garantia que a modulação
atuava *no lugar certo* — mas atuar no lugar certo com o **sinal
errado** não cura. A geometria do mecanismo é contrária à geometria da
doença.

## 3. Enunciado do no-go (com sua fronteira)

> **Na TDCP-F1 sobre o ramo finito da constraint corrigida, o setor
> escalar do par relativo é patológico (taquiônico ou fantasma) para
> todos os β_n constantes varridos (~1500 pontos, μ de 0.1 a 100) E
> para a modulação β₁(φ₋) quadrática em todos os knobs varridos
> (g≤4, v*∈[0.3,10], m_χ²∈[0.3,30], nos regimes μ=1 e μ=0.1).**

Não coberto (as saídas restantes, por custo crescente):

1. **Modulação de β₂/β₄** — as fatias estão prontas; mas os dois
   canais do mecanismo são os mesmos, e ambos falharam por razões
   estruturais, não numéricas. Prior baixo.
2. **β₃≠0** (família F2) — dimensão genuinamente inexplorada; mas a
   doença é de estrutura de vínculos e nada indica sensibilidade a β₃.
   Prior baixo-médio.
3. **Acoplamento de matéria não-mínimo** — muda a classe da teoria e
   arrisca o fantasma BD que o acoplamento mínimo garante ausente.
   Custo alto.
4. **Ramo algébrico com a constraint corrigida** — não reavaliado
   pós-erratum (a raiz exata tinha degenerescência cinética na D1;
   com a constraint corrigida e a não-fatoração do Gate 2, o quadro
   pode ser diferente). Genuinamente aberto.
   **[FECHADO 2026-08-11 — também NO-GO, ver seção 6.]**
5. **Análise além do quadrático-congelado** — condensação NÃO
   estacionária (p_φ≠0, onde a constraint não fatora e a estrutura é
   genuinamente nova — o único regime que nenhuma sondagem tocou).
   **[FECHADO 2026-08-11 — também NO-GO, ver seção 7.]**

## 4. O que o programa estabeleceu de positivo

O no-go não apaga o que foi construído — define seu alcance:

- **O Erratum 01** corrige um erro real do corpus (e da literatura
  interna do projeto), com $\dot r = H_g(\xi-r)$ no lugar de
  $\dot r\equiv0$.
- **O fundo do ramo finito funciona**: evolução estrutural genuína
  (r fixado pela densidade, sem ODE), limite GR exato, cosmologia
  aceitável.
- **O setor tensorial funciona**: Higuchi automático no primordial
  ($m_T^2/H^2\to12$, independente de TODOS os parâmetros incluindo μ)
  — um resultado estrutural elegante e novo.
- **A obstrução escalar está localizada** (setor de vínculos),
  **quantificada** (σ~4H; |kN|~μ³) e **testada contra as duas
  famílias de cura propostas**. Isso é um resultado publicável por si:
  "a classe X não admite setor escalar saudável, e eis o porquê".
- **A metodologia** — estratificação epistêmica, gates com critério de
  falha pré-declarado, auto-testes com poder de detecção, rota dupla —
  pegou cinco testes vácuos e um erro estrutural do corpus. É o ativo
  transferível do projeto.

## 5. Recomendação

Aceitar o no-go como **resultado central** do programa de reconstrução
e documentá-lo como tal (o plano v2 previa exatamente isto no seu
"se falhar" do Gate 6: *"relatar como resultado, não como fracasso"*).

As duas investigações que ainda merecem sessão própria, por ordem:

1. **O ramo algébrico pós-erratum** (item 3.4) — barato, nunca refeito
   com a constraint correta. **[FEITO 2026-08-11, ver seção 6.]**
2. **A condensação dinâmica** (item 3.5) — caro, mas é o único regime
   genuinamente novo que resta, e é onde a estrutura não-fatorada do
   Gate 2 vive de verdade.

A TDCP como narrativa física (dois campos primordiais, bifurcação,
separação estrutural) permanece o que sempre foi: uma hipótese
conceitual legítima à espera de uma implementação matemática que
feche. A implementação F1-ramo-finito não fecha — e agora se sabe
exatamente onde e por quê.

## 6. Atualização (2026-08-11) — item 3.4 fechado

`docs/resultado_investigacao1_ramo_algebrico.md` fecha o item 3.4 da
seção 3 ("ramo algébrico com a constraint corrigida — genuinamente
aberto"): **também NO-GO**. Na raiz exata ($r=r_\star$), o par relativo
é simultaneamente degenerado (kN~1e-16, confirmando a D1 pré-erratum) E
taquiônico (taxa 3.0H, independente de k — assinatura de massa). Uma
varredura de corredor ($\delta=(r-r_\star)/r_\star\in[-0.30,+0.30]$, k=1,
10, 100) não encontrou nenhum ponto com os três k simultaneamente
saudáveis: sair da raiz cura a degenerescência numérica, não a doença.

O mesmo script embutiu o teste G1-b (`docs/gate1_identidade_relacional.md`),
com resultado **R1 PASSA**: em toda a F1 já varrida (ramo finito, β_n
constante, μ∈{0.1,0.3,1,3,10}), os modos patológicos têm projeção
\|⟨v,δφ₋⟩\|² = 0.0000 — o grau relacional primordial é espectador da
doença. Por isso R1 passa a ser o enquadramento oficial do no-go: a
patologia é da representação F1, não (até aqui) do grau relacional
δΦ₋ em si. Ver `docs/gate1_identidade_relacional.md` §7 para o
detalhe do gate.

## 7. Atualização (2026-08-11, tarde) — item 3.5 fechado; o arco completo

`docs/resultado_investigacao2_faseA.md` + `resultado_investigacao2_faseB.md`
fecham a saída 5 (condensação dinâmica, p_φ≠0): o fundo de rolagem
**existe** e realiza a narrativa da bifurcação (a condensação de φ₋
dirige r de 0.031 a 0.498, deslocando o fundo ordem 1 dos dois ramos e
pousando de volta no ramo finito) — mas o setor escalar é **pior** lá:
σ/H sobe monotonicamente com o deslocamento até **13.08** no coração
da janela não-fatorada, sem nenhum ponto limpo em toda a trajetória, e
relaxa para σ/H≈4.25 no fundo estacionário pousado (dentro da família
3.85–4.43 já varrida). Contagem de modos = 3 em toda parte (sem BD na
rota numérica; não certificador). Os modos patológicos continuam
δφ₋-espectadores mesmo com F′≠0 e χ̇≠0 — e a instabilidade de
condensação (essa sim δφ₋-dominada) **sara sozinha** ao assentar.

**Com os itens 3.4 e 3.5 fechados, as duas saídas estruturais do no-go
estão mortas.** Restam as saídas de prior baixo (β₂/β₄ modulados; F2
com β₃≠0) e a mudança de classe (matéria não-mínima). O arco
computacional da TDCP-F1 está completo: fundo ✓, tensor ✓, escalar ✗
em todos os regimes acessíveis — constante, modulado-estacionário,
algébrico e dinâmico não-fatorado. Achado estrutural da Fase A que
qualquer sucessor herda: a interação HR resiste à condensação de φ₋
(limiar m_χ² ≳ 2Δ_∞). R2 segue viva apenas FORA da representação F1,
sob o critério anti-circularidade do `gate1c_nota_trilema.md`.
