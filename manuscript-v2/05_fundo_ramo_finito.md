# 05 — O fundo do ramo finito

**Porte de `docs/resultado_ramo_finito.md` (2026-08-07, consequência
do Erratum-01; script `auditoria/code/ramo_dinamico_correto.py`), com
as notas de continuação numérica aprendidas em R-8b.**

## 1. A cúbica e as duas famílias de raiz

No ramo cinemático (cap. 04), r é fixado instante a instante pela
densidade: a combinação das duas Friedmann dá uma cúbica
m²M_eff²𝒲(r) = ρ com duas famílias:

- **ramo infinito**, r ~ √ρ̃ → ∞: produz ξ < 0 (lapso negativo no
  setor f) **no regime primordial**; descartado pelo corpus — mas por
  uma razão que **caiu**. O descarte foi reaberto pelo R-12i e está
  **de novo fechado desde o R-13a/R-13b, por um argumento
  inteiramente outro**: o **ghost de Higuchi**, não o zero do lapso.
  Ver a qualificação de época, a nota de revogação *e* o bloco de
  veredito abaixo — nesta ordem, que é a do processo;
- **ramo finito**, r ~ β₁/ρ̃ → 0 no primordial: físico.

*Qualificação de época (R-10c)* — *mantida como registro; o veredito
"correta" que ela carrega caiu no R-12i e não foi restaurado — o que
exclui o ramo hoje é o Higuchi, ver as duas notas abaixo:* a exclusão
está **correta**, mas a
justificativa herdada do corpus ("dá ξ < 0", sem qualificar época)
não. A varredura de todas as raízes reais positivas da cúbica mostra
que essa raiz tem ξ < 0 só no primordial (ξ ≈ −9.4e3 em a = 0.001;
−8.38 em a = 0.1) e ξ > 0 a partir de a ≈ 1 (r = 2.358, ξ = +1.985),
logo **ξ cruza zero** em algum a ∈ (0.1, 1): uma história cosmológica
contínua nesse ramo teria de atravessar lapso nulo no setor f — ponto
singular. É *isso* que exclui o ramo, e não a patologia em toda época.
Fica registrado o achado colateral: existe uma **segunda solução
tardia viável** (r ≈ 2.23, ξ ≈ 2.23, H² > 0), que não se conecta ao
nosso primordial e que o repositório **nunca explorou** — o espaço de
soluções do fundo é maior do que a cascata assumiu. *Nível 2b; fonte:
`docs/resultado_r10c_saidas.md` Parte A.*

> **[REVOGAÇÃO DO CRITÉRIO `ξ = 0` — 2026-08-13, R-12i; permanece
> revogado]** O critério que sustenta o
> parágrafo acima — ξ cruza zero ⟹ o lapso do setor f se anula ⟹ ponto
> singular ⟹ história contínua excluída — **está em conflito declarado
> com a fonte primária**. Como `b = ra`, o nosso `ξ = r + dr/dN`
> satisfaz `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al. (1407.4331):
> **mesmo sinal, mesmo zero**. Aquele paper trata esse quique de `b`
> **explicitamente** (§II e §VI, com nota de rodapé 9) e argumenta que
> ele **não** torna a solução não-física, por três razões declaradas:
> (i) f não acopla à matéria e não tem interpretação geométrica; (ii)
> nenhuma variável de fundo ou perturbada apresenta singularidade;
> (iii) `√(−det f)·R̄(f)` permanece finita e não-nula, de modo que as
> equações de movimento existem em todo instante — a escolha de sinal
> da raiz é feita justamente para deixar a ação diferenciável na
> travessia. E a *infinite-branch bigravity* (IBB) é o **único**
> modelo estável em todos os tempos daquele paper.
>
> **Estado desta nota, quando escrita:** a exclusão do ramo infinito
> passou a **REABERTA e exigindo reavaliação** — não "fechada", e
> tampouco "aberta e viável". Ou a
> exclusão ganha um argumento novo que responda aos três deles, ou
> cai. **Caveat de escopo, obrigatório em toda menção:** o IBB viável
> exige β₄ ≠ 0, especificamente `0 < β₄ < 2β₁`, enquanto a nossa
> célula mínima tem β₄ = 0 — o alvo do reexame é o ramo infinito da F1
> **com β₄ ligado**, e não a célula atual.
>
> **[ATUALIZADO 2026-08-13 — 1503.07436 verificado na fonte pelo
> autor.]** Existe agora um **argumento independente candidato**, de
> natureza diferente do nosso: naquele paper, saúde de Higuchi em
> universo em expansão exige **r′ > 0**, enquanto o ramo infinito é
> definido por **r′ < 0** — colisão direta, e nada a ver com o zero do
> lapso. Cai também a caracterização anterior de que as duas linhas do
> `posicionamento_literatura.md` sobre esse paper eram contraditórias:
> são o **mesmo enunciado aplicado a ramos diferentes** (finito, r′ ≥ 0,
> passa; infinito, r′ < 0, não passa). A tensão real é **entre as duas
> fontes** — 1407.4331 declara o IBB estável **no canal de gradiente**,
> 1503.07436 o ataca **pelo Higuchi** — e ela se dissolve pela
> separação de canais: estabilidade de gradiente, saúde de
> Higuchi/helicidade-0 e saúde do setor tensorial são **três perguntas
> distintas**, e o IBB pode curar a primeira e falhar nas outras. O
> argumento era, então, literatura (nível 3) e **não traduzido** para
> as convenções do projeto; o teste ficou na fila — **e foi
> executado**, ver o bloco de veredito logo abaixo. *Fontes:
> `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b);
> `docs/posicionamento_literatura.md` §2b.*

> **[VEREDITO — 2026-08-13, R-13a + R-13b] RAMO INFINITO IBB DA F1:
> EXCLUÍDO PELO GHOST DE HIGUCHI.**
>
> **Qualificação obrigatória, que acompanha toda menção a esta saída.**
> A exclusão original, pelo cruzamento `ξ = 0`, permanece
> **REVOGADA** — a nota acima não é revertida por esta, e o quique do
> lapso continua não sendo, por si só, uma singularidade. A exclusão
> vigente é **independente**: nas células IBB testadas o ramo infinito
> **viola a condição de Higuchi durante toda a história**.
>
> **O critério, traduzido e verificado.** O funcional de Higuchi da
> fonte (Könnig 2015, arXiv:1503.07436, eq. 14) foi extraído na fonte e
> traduzido para as convenções do projeto (R-13a §2), e a tradução foi
> **re-verificada por CAS em rota independente** — três resíduos
> simbólicos **zero**, com `β_n` e `μ` gerais e matéria de poeira
> (R-13b §8.2). Nas nossas variáveis a cadeia fecha exata:
> **Higuchi ⟺ `ξ ≥ r` ⟺ `r′ ≥ 0`**.
>
> **A medida** (R-13b §§5–6, células IBB genuínas β₂ = β₃ = 0, β₁ > 0,
> `0 < β₄/β₁ < 2μ^{3/2}`): `r′ < 0` em **100% da história em 108/108
> células**; Higuchi satisfeito em **0 de 64 800 pontos**; concordância
> entre as duas formas equivalentes em **64 800/64 800**; **controle
> positivo** no ramo finito **400/400** — o gate aprova o que deve
> aprovar. O enunciado é **fechado**, não amostral:
> `m_T²/H²|_{r_c} = 1 + 1/(μr_c²)` com `μr_c² > 1` em toda a janela de
> existência, logo **1 < sup(m_T²/H²) < 2 estrito** em toda ela. E
> **`μ` é pura reescala** no IBB genuíno: o eixo `μ` não abre exceção.
>
> **O que o veredito NÃO é.** *"The IBB branch is not tachyonic in the
> tensor-mass sense; it is excluded by the Higuchi ghost condition."*
> `m_T² > 0` em **108/108** — não há taquiônico tensorial, e isso
> **não** o salva.
>
> **Complementaridade — é este o achado.** *"Within the F1
> parameterization, the two standard cosmological branches fail for
> complementary reasons: the finite branch violates scalar-gradient
> stability in the early universe, while the genuine infinite branch
> avoids that instability but violates the Higuchi condition throughout
> its evolution."* O gradiente do IBB é **saudável segundo a fonte**
> (§IV A de 1503.07436, que **confirma** e **não** retrata 1407.4331) —
> canal independente, que não salva o Higuchi.
>
> **Ponto lógico, declarado.** O gate do R-13b **não mede gradiente**, e
> essa cegueira continua declarada como boa prática (regra 7). Ela
> **não bloqueia o veredito**: um ghost físico basta para excluir,
> independentemente de o gradiente estar saudável. Um teste de `c_s²` no
> IBB é **validação adicional desejável, não requisito** — o veredito
> não o aguarda.
>
> **Proveniência:** *infinite branch / IBB* → **EXCLUÍDO**, pelo ghost
> de Higuchi (`r′ < 0` em toda a história); *argumento antigo `ξ = 0`* →
> **REVOGADO**, porque o zero do lapso / quique não é por si só
> singularidade; *gradiente no IBB* → **SAUDÁVEL segundo a fonte**,
> canal independente que não salva o Higuchi.
> *Fontes: `docs/resultado_r13a_criterio_higuchi_fonte.md`;
> `docs/resultado_r13b_ibb_ramo_infinito.md` §§4–6 e §8;
> `auditoria/code/out/r13b_ibb_ramo_infinito.txt`.*

*Nota numérica (lição do R-8b):* a seleção de raiz "menor positiva"
só é segura com ρ̃ > 0; em extensões com vácuo escalar (ρ̃ efetivo
negativo) a seleção deve ser por **continuação** (raiz mais próxima
da anterior), sob pena de salto de ramo. *Fonte:
`docs/resultado_r8b_limite_mH0.md` §1.*

## 2. O que o ramo finito entrega

| | Resultado | Nível |
|---|---|---|
| Evolução estrutural | ṙ ≠ 0; r cresce de ~0 até r_∞ ≈ 0.33 (benchmark) | 2a |
| Primordial | r ∝ a³ ⟹ dr/dN = 3r ⟹ **ξ = 4r > 0** | 2a |
| Limite GR | H²/(ρ/3M_g²) = 1.0000 — exato | 2a |
| Lapso físico | ξ > 0 em toda a história | 2b (trilha) |
| Ponto fixo tardio | raiz da cúbica com ρ=0; universo acelera | 2a |
| Cosmologia | Ω_m ≈ 0.25 no "hoje" natural desse fundo | 2b |

Sobre o "hoje": cada fundo/família define o seu — o resultado acima
usa o ponto natural do benchmark original; a família do R-8b ancora
Ω_m(a₀) = 0.3 como escolha de dicionário. Comparações entre docs
devem citar a âncora. *Fontes: resultado_ramo_finito §1–2,
resultado_r8b §1.*

## 3. O mecanismo de separação estrutural — sem modulador

**É este o mecanismo que a v1 procurava.** No ramo finito, r evolui
porque ρ cai — sem β_n(φ₋), sem campo modulador, sem hipótese
adicional. A separação estrutural (r: ~0 → 0.33) é consequência da
constraint correta + Friedmann.

Isso reordenou a arquitetura (resultado_ramo_finito §6): a modulação
β₁(φ₋) deixou de ser necessidade e virou **extensão** — e a ordem de
teste passou a ser "primeiro β constantes, depois modulação". A
cascata pós-Erratum-02 executou exatamente essa ordem e fechou as duas
etapas, **com o alcance que o cap. 07 §4 declara e não mais que ele**:
com β constantes o setor escalar é são **na era tardia** (benchmark =
HR + espectadores) e tem **instabilidade de gradiente de classe em
r → 0** (c_s² = −1 exato, para qualquer forma-β;
`docs/resultado_r11_nogo_gradiente.md`). Com a modulação ligada, a
trajetória de rolagem/condensação existe, desloca ordem-1, pousa de
volta no ramo finito e mantém a saúde perturbativa na janela (Fase A +
R-7c/e) — janela que está inteira dentro da cobertura tardia da cascata
(a ≥ 100) e portanto não enuncia nada sobre r → 0; testada depois
*como saída* para a instabilidade, a modulação reprovou (R-10c).

## 4. O fundo dinâmico completo (rolagem e pouso)

A realização com φ₋ dinâmico (célula de referência g=2, m²=30,
v★=1): condensação dirige r de 0.031 a 0.498 (×16), deslocamento
ordem-1 dos dois ramos na janela a ∈ [225, 7086] (máx. 0.476), pouso
limpo de volta no ramo finito (r_fim = 0.4979; φ₋/v = 0.932 — âncoras
reproduzidas em três reintegrações independentes: original, Euler do
R-7c, Heun do R-7e). *Nível 2b; fronteira: uma trajetória, uma
célula.* *Notas de integrador declaradas:* as taxas armazenadas do
fundo Euler eram internamente inconsistentes ~1e-3 (detectado pelo
V-XREP-a; corrigido com taxas spline-consistentes) e o Heun atual tem
M0 = 3e-4 (cadeia rp de 1ª ordem) — suficiente para tudo que foi
medido; um integrador de 2ª ordem completo está na fila de
housekeeping. *Fontes: resultado_investigacao2_faseA.md,
resultado_r7_cascata §3, resultado_r7e_saude_interna §1.*
