# 07 — O setor escalar: do falso no-go à saúde tardia, e daí ao no-go de classe por gradiente

**Resultado central da v2.** Este capítulo conta quatro atos com
números e fontes: o no-go aparente, a sua queda, o setor corrigido —
são **na era tardia** — e o no-go real, de classe, por gradiente, na
era inicial. A honestidade do capítulo depende de manter os quatro
separados, e de não confundir os dois eixos que atravessam a
história. **Instrumento:** o segundo ato é inteiro sobre ele
(Erratum-02, que derrubou o primeiro no-go), e dentro do quarto está
o Erratum-03, que corrige *valores* sem tocar *enunciados*.
**Teoria:** é do quarto ato que se trata — o no-go de classe foi
medido com o instrumento já corrigido e validado, e por isso não cai
com ele, como caiu o primeiro.

## Ato 1 — O no-go aparente (2026-08-08 → 08-11)

Sobre o benchmark β-constante e suas vizinhanças, o programa mediu e
consolidou, em sequência: um taquião persistente σ ≈ (3–4)H no ponto
fixo tardio para μ ≥ 0.3; um fantasma quase-nulo (lapso do setor f)
na fresta μ = 0.1; ~1500 pontos de varredura 4D sem corredor
saudável; a modulação β₁(φ₋) piorando os dois canais; e o ramo
algébrico degenerado E taquiônico na raiz. Consolidação da época:
`docs/veredito_setor_escalar_final.md` (hoje superseded — ver o Ato 4,
que é a quarta seção deste capítulo, citada como "cap. 07 §4" nos
demais capítulos).

Dois avisos já haviam sido emitidos pelo próprio programa antes da
queda: (i) o **D-2** mostrou que vereditos de espectro *congelado*
não valem como vereditos dinâmicos nesta classe (as matrizes
comóveis nunca assentam; `docs/resultado_d2_evolucao.md`); (ii) o
**R-2** rebaixou o fantasma a "assinatura robusta com letalidade
indecidível" e descartou as magnitudes de energia como poluídas por
normalização (`docs/resultado_r2_fantasma.md`). O que ninguém sabia:
o objeto que essas análises estudavam não existia.

## Ato 2 — A queda (Erratum-02, 2026-08-12)

**O bug.** A rotina numérica de absorção de multiplicadores
(`reduz_ponto`, herdada de script em script desde o D-2) somava o
termo de conexão Ċ **duas vezes** nas entradas fora da diagonal de
W_XX — consequência de usar o Ċ pré-computado da matriz original
(stale) sem pular a entrada já antissimetrizada pelo multiplicador
anterior do par. Tamanho: 1.4–6.1% de W_XX, *suave* ao longo da
trilha — por isso parecia física e convergia em resolução. A
biblioteca simbólica (`derivations/code/tdcp_pert_lib.py`:
`matrix_ipp_row`, `schur_eliminate`) sempre esteve correta; o erro
era exclusivo da tradução numérica.
*Fonte: `auditoria/erratum_02_reducao_numerica.md` §1–2.*

**A consequência.** O bug promovia Ψ_f — que é direção de VÍNCULO (o
vínculo secundário de Hassan–Rosen que remove o modo Boulware–Deser)
— a terceiro grau de liberdade propagante. Desse único erro
descendiam: a contagem 3, o fantasma canônico do Gate F
(ω₀/H ≈ 7–12, lido como ω₀ ~ 3–4Λ₃), a banda de amplificação métrica
(lnA ≈ +4 por passagem), a previsão de excesso ISW 2–8× em baixo-ℓ
com sua "tensão", e a maior parte do no-go do Ato 1.

**A queda, em cinco passos verificáveis** (todos com saída
versionada):

1. Reauditoria externa independente (construção ADM/Faddeev–Jackiw;
   pacote preservado em `auditoria/external/r6_reaudit_chatgpt/`)
   obteve det K_métrico = 0 **simbólico**, com dois DOFs.
2. `r6b`: o autovalor negativo do nosso K_red é estável a 60 dígitos
   e sob varredura de passo — não era arredondamento. Duas
   construções exatas discordavam.
3. `r6c`: as duas ações são **A MESMA** — identidade exata
   (aritmética racional, off-shell, peça por peça, a menos de
   derivada total). Logo o erro estava numa das reduções. *Nível 1
   (duas rotas, prova exata).*
4. `r6d`: o bug localizado linha a linha; a absorção corrigida
   (one-shot, S simétrica) colapsa det K₂/esc² de ~1e-8 para
   1e-33…1e-40 (dps=40), com direção nula = Ψ_f puro. O pipeline
   corrigido **reproduz independentemente** o resultado externo.
5. Consistência externa: a contagem 2 é exatamente a do teorema de
   Hassan–Rosen e do setor escalar FRW de Comelli–Crisostomi–Pilo —
   que a contagem 3 contradizia. *Nível 3 (literatura), em
   concordância com níveis 1–2a internos.*

## Ato 3 — O setor corrigido (cascata R-7, 2026-08-12)

No sistema físico de dois DOFs (modo métrico Ẽ = k²E_f + espectador
δφ₋; token `dchi` nos scripts), com a maquinaria corrigida
(equilibração de variáveis; gates V-XREP-a/b; critérios
pré-declarados):

**Estrutura.** Zero autovalores cinéticos negativos em todos os
regimes testados: benchmarks estáticos (2×24 000 pontos, R-7a),
classe μ×β₁ ampla incluindo a fresta μ=0.1 (17 células × 9 amostras,
R-7f), trajetória completa de rolagem/pouso incluindo a janela de
deslocamento ordem-1 (4×14 000 pontos, R-7e). O coeficiente auxiliar
W00 de Ψ_f **nunca cruza zero** — a eliminação do vínculo sobrevive
ao regime não-fatorado; sem quebra de Faddeev–Jackiw. *Nível 2b;
fronteiras: grades citadas, uma trajetória REF para o dinâmico.*
*Fontes: `docs/resultado_r7_cascata.md`,
`docs/resultado_r7e_saude_interna.md`, saídas r7a/r7e/r7f.*

**Dinâmica.** O modo métrico é overdamped e **decai** (−2.5…−2.7/
e-fold tardio); o espectador δφ₋ tem fricção 3H e dispersão
ω² = k²/a² + U″ medidas exatas (âncoras analíticas fecham em
0.01–0.02: taxas físicas tardias −0.381 vs −0.368 e −0.088 vs
−0.082). O σ_can ≈ 1.13/1.41 que o Gate F-b lia como "assentamento do
fantasma" era a normalização a^{3/2} do espectador saudável — provado
dinamicamente. *Nível 2a (âncora analítica + medida).*
*Fonte: `auditoria/code/out/r7a_dinamica_2dof.txt` M2/M3.*

**A banda está morta.** lnA de passagem (kh 20 → 0.2), componente
métrica: −8.37/−8.39 nos fundos estáticos (antigo: +3.97/+3.62);
−11.0…−14.7 nas oito épocas de cruzamento do fundo pousado (antigo:
−0.2…+4.8); o potencial temporal do setor g decai junto (31/32
combinações; a única exceção é log de componente com entrada
próxima de zero, com a norma métrica da mesma IC decaindo — enunciado
robusto: 32/32). A previsão de excesso ISW está **retirada**; a
"tensão observacional" dissolvida — a previsão era artefato. *Nível
2b; nota: os lnA do pousado carregam ±O(1) de sistemática do
integrador de fundo (V-XREP-a a detectou; margens de 10+ unidades
log tornam o veredito insensível).*
*Fontes: `docs/resultado_r7_cascata.md` §2–3, saídas r7b/r7c.*

**O que sobra de dinâmica não-trivial.** Um único transiente: durante
a rolagem, U″(φ₋) transita de negativo a positivo (condensação — a
física da Fase A) e o espectador ganha no máximo e^{+0.4} no IR
profundo, autocurável, sem contaminação métrica. Medido com
normalização congelada e halving pleno (kh=10 fino: dG=0.19<0.3).
*Nível 2b.* *Fonte: `docs/resultado_r7e_saude_interna.md` §2–3,
`auditoria/code/out/r7e_halving_fino.txt`.*

## Ato 4 — O enunciado, e a tabela de supersessão (R-10 → R-12, 2026-08-13)

> **[REVISADO 2026-08-13; limiar corrigido pelo R-12i]** No setor
> escalar linear, **na era tardia** (r ≳ 0.21, i.e. z ≲ 0.6 no
> benchmark), a F1 não apresenta fantasma, taquião letal,
> instabilidade crescente nem quebra da estrutura de vínculos: o no-go
> *daquela* era está revogado, e o fantasma do Gate F era artefato
> numérico (§Ato 2 — isso não mudou).
>
> **Mas o setor NÃO é são em todas as épocas.** Em r ≲ 0.05 (alto
> redshift) o escalar métrico tem **instabilidade de gradiente**,
> **c_s² = −1** (exato no limite r → 0; R-12), com cinética positiva —
> confirmando a previsão de
> Könnig–Akrami–Amendola–Motta–Solomon ([arXiv:1407.4331]) para o
> *finite branch*, que este repositório registrava sem confrontar.

*Nota sobre o limiar (R-12i, 2026-08-13).* A versão anterior deste
enunciado usava **r ≳ 0.28**, sem fonte. O número não é nosso: é o
limiar do modelo **β₁-puro** (β₀ = 0) de 1407.4331 — raiz exata
√((√5−2)/3) = 0.28052 —, enquanto a nossa célula mínima é o modelo
**β₀β₁ com β₀/β₁ = 1**. No nosso fundo, r = 0.28 fica ΔN = +0.205
*adiante* do cruzamento e lá c_s² já vale +0.41, o que contradizia o
a_cross = 0.578 citado poucas linhas abaixo. O valor correto é a raiz
da nossa forma fechada, **r = 0.20793**; a eq. (73) de 1407.4331
avaliada no *nosso* modelo (λ = 1) dá **0.21448** — concordância de
3.1%, contra os 34.9% da comparação errada. *Fonte:
`docs/resultado_r12i_confronto_konnig.md`.*

**Por que a v1 deste capítulo dizia o contrário.** O enunciado
anterior — "são em todos os regimes testados" — era literalmente
verdadeiro e materialmente enganoso: toda a cascata R-7 e as sondas
R-8 rodaram em a ∈ [100, 80000], que no brinquedo é a era tardia.
**Nunca testamos a < 100.** É a mesma família de ponto cego do
Erratum-02, agora no eixo do tempo cósmico — e foi exatamente o que o
parecer de cosmologia previu ("os gates do R-7 são cegos a gradiente
por construção"). *Fontes: `docs/resultado_r10a_gradiente.md`,
saídas r10a/r10b.*

**Severidade:** a transição ocorre em z ≈ 0.61 (β₁=1; a_cross = 0.578
com instrumento limpo — R-12f); modos com
k/aH ≳ 8 na transição saem do regime linear (lnA até 32); os
intermediários (k/aH ~ 1–7) permanecem lineares mas crescem por
fatores de 2 a 10⁴. **A era instável cobre a recombinação.**

**[2026-08-13; revisto pelo R-12i] As quatro saídas foram testadas —
três fechadas, uma REABERTA:**

| Saída | Teste | Estado |
|---|---|---|
| Ramo infinito | R-10c → **REABERTA** (R-12i) | a exclusão por ξ cruzar zero **não se sustenta**: é o quique de `b` que 1407.4331 §II/§VI trata e defende como físico, com três argumentos. Reexame pendente, e o alvo é o ramo infinito **com β₄ ≠ 0** (o IBB viável exige 0 < β₄ < 2β₁; a célula mínima tem β₄ = 0). **[2026-08-13]** Existe um argumento independente **candidato** — Higuchi via `r′ < 0` (1503.07436, verificado na fonte pelo autor) —, **pendente de tradução para as convenções do projeto**; a saída segue REABERTA |
| Modulação β₁(φ₋) | R-10c | fechada — age ~3 ordens tarde demais |
| Screening de Vainshtein | R-10d | fechada — δ_screen ≈ 20–60; *o λ cancela*, não há escala linear protegida |
| Forma-β (β₀, β₂, β₄, μ) | R-11 + R-12g | fechada — **c_s² = −1 em 108/108 células**, com `\|c_s²+1\| ≤ 1.1e−7` |

*A reabertura, em detalhe (R-12i §1.6 e §R-b).* O critério que fechava
o ramo infinito era: ξ cruza zero ⟹ o lapso do setor f se anula ⟹
ponto singular ⟹ história contínua excluída. Como `b = ra`, o nosso
`ξ = r + dr/dN` satisfaz `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al. —
**mesmo sinal, mesmo zero**. Ou seja, o que o R-10c descarta é
*exatamente* o quique de `b` que a fonte primária trata
explicitamente (§II e §VI, com nota de rodapé 9) e argumenta **não**
tornar a solução não-física, por três razões declaradas: (i) f não
acopla à matéria e não tem interpretação geométrica; (ii) nenhuma
variável de fundo ou perturbada apresenta singularidade; (iii)
`√(−det f)·R̄(f)` permanece finita e não-nula, de modo que as equações
de movimento existem em todo instante — a escolha de sinal da raiz é
feita justamente para deixar a ação diferenciável na travessia. E a
*infinite-branch bigravity* (IBB) é o **único** modelo estável em
todos os tempos daquele paper. **Caveat de escopo, sem o qual a linha
não pode ser citada:** o IBB viável exige β₄ ≠ 0, especificamente
`0 < β₄ < 2β₁`, enquanto a nossa célula mínima tem β₄ = 0 — o alvo do
reexame é o ramo infinito da F1 **com β₄ ligado**, não a célula atual.
O estado correto não é "fechada" nem "aberta e viável": é **reaberta,
exigindo reavaliação**.

**[2026-08-13 — 1503.07436 verificado na fonte pelo autor.]** A
caracterização anterior desta linha ("duas linhas contraditórias em
`docs/posicionamento_literatura.md`, nenhuma verificada na fonte")
**estava errada e fica retratada**: as duas linhas são o mesmo
critério em ramos diferentes (finito, `r′ ≥ 0`, passa; infinito,
`r′ < 0`, não passa) — consistentes entre si. O que a fonte dá é um
argumento **independente** contra o IBB: em cosmologia expansiva `r`
tem de **crescer** para satisfazer a condição associada ao Higuchi e
manter sãos helicidade-0 e helicidade-2, ao passo que o *infinite
branch* é definido como aquele em que `r` parte de infinito e
**decresce**. A tensão com o "IBB estável" de 1407.4331 dissolve-se
pela **separação de canais**: estabilidade de **gradiente** ≠ saúde de
**Higuchi/helicidade-0** ≠ saúde do **setor tensorial** — o IBB pode
curar o gradiente e ainda assim falhar por outro canal. **Isto não
fecha a saída.** É literatura (nível 3, leitura do autor na fonte),
**não traduzida** para as convenções deste projeto; o argumento
próprio (`ξ = 0`) continua derrubado, e a saída continua **REABERTA**
até rodar o teste de tradução (célula IBB genuína `β₂ = β₃ = 0`,
`β₁ > 0`, `0 < β₄ < 2β₁`; medir `r′(N)`, `m_T²/H²` e o funcional de
Higuchi na nossa convenção). *Fontes:
`docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b, nota
datada); `docs/posicionamento_literatura.md` §2b R-b.*

**NO-GO DE CLASSE POR GRADIENTE (R-11, valor fixado no R-12):** na
classe F1 (β₃ = 0, matéria só em g, ramo finito),

> **c_s² = −1 exatamente em r → 0**, para *qualquer* escolha de β₀, β₂,
> β₄, μ — 108/108 células, `|c_s² + 1| ≤ 1.1e−7`.

Não é propriedade da célula de benchmark: é **da classe**. O desvio
residual é **massa** (ω²/H² = −kh² + 5/2 + O(r)) — não há termo k⁴ nem
estrutura em k. Na era tardia o mesmo modo tem **c_s² = +1 exato**.
E o valor não é medido: é **teorema**. Na célula mínima da classe
(β₂ = β₄ = 0) a redução 2-DOF fecha em forma exata e dá

> c_s²(r) = −(3r+1)(9r⁵ − 6r³ + 3r² − 10r + 2) / (2(3r²+1)²),

donde **c_s² → −1 em r → 0** e **c_s² = +1 exato no atrator tardio**
r_∞ = (√13−1)/6 — os dois limites são exatamente ±1. A massa efetiva
sai junto: m_ef²/H² → 5/2.
*Fontes: `docs/resultado_r11_nogo_gradiente.md`,
`docs/resultado_r12_instrumento_e_cs2.md`,
`docs/resultado_r12b_teorema_cs2.md`.*

**[ERRATUM-03, 2026-08-13]** Os valores numéricos originais do R-11
(−1.010 ± 6e−6 em kh = 30) e as tabelas de c_s² do R-9a/R-10a/R-10b
estavam contaminados: Ċ₃/Ċ₂ eram calculados por `np.gradient` (2ª
ordem), e o erro O(h²) é amplificado pelo condicionamento da redução
(cond ≈ 1e11 em a = 0.01). A causa foi **demonstrada** — o estêncil de
2ª ordem reproduz a tabela antiga dígito a dígito e move com h,
enquanto a 8ª ordem é estável em 14 dígitos. **O enunciado não muda; o
valor fica mais limpo.** Duas regras novas entram no cap. 02:
derivadas de fundo em forma fechada (ou ordem ≥ 8 com teste de
refino), e *declaração de cegueira* de todo gate — o calibrador do
espectador δχ deu 1.00000 em todos os pontos justamente porque é cego
ao canal Ċ.

**O contraste com o no-go antigo importa.** O anterior
(fantasma/taquião) era artefato de bug e caiu quando o instrumento foi
corrigido; este foi medido com o instrumento já corrigido e validado,
é insensível a toda a forma do potencial, e reproduz uma previsão
independente da literatura que o repositório registrava sem confrontar.
A porta que resta entreaberta é β₃ ≠ 0 — que sai da definição de
F1, isto é, leva a uma F2 — **e, desde o R-12i, também o ramo infinito
com β₄ ≠ 0**, que voltou à condição de saída sob reexame (tabela
acima).

Pendências declaradas: ramo algébrico (deferido); fronteira de uma
trajetória no dinâmico; scan de classe em nível de assinatura; **a
validade do tratamento linear na era instável** — que não é saída (o
R-10d fechou o screening de Vainshtein como escape: δ_screen ≈ 20–60 e
o λ cancela), mas fronteira: onde os modos saem do regime linear, a
teoria deixa de ser refutável *e* de ser calculável pelo mesmo motivo;
A1 no fundo dinâmico e com era de radiação.

| Afirmação da era do no-go | Estado |
|---|---|
| 3 DOFs escalares; fantasma; ω₀/Λ₃; H-SC | **caíram** (Erratum-02) |
| Taquião σ≈(3–4)H persistente; fresta μ=0.1 | **caíram** (R-7a/R-7f) |
| Banda lnA≈+4; "supressão-matéria" | **caíram** (R-7b/c) |
| Excesso ISW 2–8×; dispersão p=0.44; canto-Akrami | **retirados** (R-7d) |
| σ/H≈13 no regime não-fatorado (Fase B) | **caiu** (R-7e + autópsia) |
| D-2: "congelado não é árbitro dinâmico" | **fica** (reforçado) |
| R-2: "energias poluídas por normalização" | **fica** (era o aviso certo) |
| Fundo, tensor, Bianchi/Erratum-01, Gate 1 | **ficam** (não usavam a redução) |
