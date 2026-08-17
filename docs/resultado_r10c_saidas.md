# R-10c — As Duas Saídas Baratas: Ramo Infinito e Fundo Dinâmico

> **[SUPERSESSÃO DE VALOR — 2026-08-13, R-12]** Os enunciados deste
> documento estão **confirmados**; os números de c_s² da **Parte B**
> estão superados. Eles foram medidos com Ċ₃/Ċ₂ por `np.gradient`
> (2ª ordem), cujo erro O(h²) é amplificado pelo condicionamento da
> redução; o Erratum-03 classifica **R-10a/b/c/d** como *contaminado
> no valor (enunciados intactos)*
> (`docs/resultado_r12_instrumento_e_cs2.md` §6).
>
> **O que NÃO muda.** As **quatro saídas continuam fechadas** *[esta
> frase caiu em 2026-08-13 pelo R-12i: passaram a ser **três fechadas e
> uma reaberta** — a do ramo infinito; ver o banner de REABERTURA da
> Parte A. **[2026-08-13, R-13a + R-13b:** voltam a ser **quatro
> fechadas**, mas com a exclusão do ramo infinito **inteiramente
> substituída** — o argumento `ξ = 0` permanece REVOGADO e no lugar dele
> entra o **ghost de Higuchi**; ver o bloco de VEREDITO da Parte A.**]**]*
> e a
> **modulação β₁(φ₋) continua chegando tarde demais** — é assim que o
> R-12 §4 ("as quatro saídas fechadas (R-10c/d, R-11)") e o cap. 07
> da v2 (Ato 4: "Modulação β₁(φ₋) | R-10c | fechada — age ~3 ordens
> tarde demais") registram o resultado. A **Parte A** (raízes da
> cúbica, r, ξ, H²) **não é afetada**: é fundo, e o fundo não passa
> pela cadeia numérica defeituosa (R-12 §4).
>
> **O que muda.** São do canal sujo os valores da tabela de c_s²(a)
> em kh = 30 (−1.010, −0.999, −0.901, −0.287, +0.698, +0.974,
> +1.01…+2.17), o **lnA = 85.7** derivado deles, as **3.07 e-folds**
> de era instável e o **"c_s² positivo já em r ≈ 0.026"**.
>
> **Valor limpo: não recomputado para este fundo.** A Parte B roda no
> **fundo dinâmico modulado**, e o R-12 §7 declara que só o que está
> no seu §3 — perfil em k, as 108 células, a_cross/z_cross — foi
> refeito com o instrumento limpo, tudo no benchmark **β-constante**.
> Nenhum ponto da tabela acima, nem o lnA, nem o r ≈ 0.026 tem valor
> limpo correspondente publicado: quem precisar deles tem de remedir.
> A única âncora limpa comparável é o mesmo par (a = 0.01, kh = 30)
> no β-constante, onde o estêncil de 8ª ordem dá **−0.99716** em vez
> de −1.010 (R-12 §2). O **sinal** negativo em r → 0 e a existência
> da troca de sinal sobrevivem ao instrumento limpo: **c_s² = −1
> exato** em r → 0 e **+1 exato** na era tardia, com a_cross = 0.578
> e z_cross = 0.61 no β-constante (R-12 §3). Ver
> `docs/resultado_r12_instrumento_e_cs2.md`.

**Data:** 2026-08-13. Script: `auditoria/code/r10c_saidas_ramo_e_dinamico.py`
(saída em `out/`). Sequência do R-10a/R-10b (instabilidade de
gradiente confirmada). Testa as saídas 2 e 4 listadas em
`docs/resultado_r10a_gradiente.md` §4.

---

## Parte A — A exclusão do ramo infinito: **correta, mas mal
justificada no corpus**

> **[REABERTURA — 2026-08-13, R-12i]** *Nota acrescentada; o texto
> original da Parte A permanece intacto abaixo.* **Esta nota é registro
> do caminho: a revogação do `ξ = 0` que ela estabelece permanece de
> pé, mas o estado "REABERTA" que ela declara está superado pelo bloco
> de VEREDITO logo abaixo (R-13a + R-13b), que fecha a saída pelo ghost
> de Higuchi.* **O veredito desta
> Parte A caiu.** O critério que ela estabelece — ξ cruza zero ⟹ o
> lapso do setor f se anula ⟹ ponto singular ⟹ história contínua
> excluída — **não se sustenta**. Como `b = ra`, o nosso
> `ξ = r + dr/dN` satisfaz `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al.
> (1407.4331): **mesmo sinal, mesmo zero**. O que esta Parte A
> descarta é, ponto por ponto, o **quique de `b`** que aquele paper
> trata **explicitamente** (§II e §VI, com nota de rodapé 9) e
> argumenta **não** tornar a solução não-física, por três razões
> declaradas: (i) f não acopla à matéria e não tem interpretação
> geométrica; (ii) nenhuma variável de fundo ou perturbada apresenta
> singularidade; (iii) `√(−det f)·R̄(f)` permanece finita e não-nula,
> de modo que as equações de movimento existem em todo instante — a
> escolha de sinal da raiz é feita justamente para deixar a ação
> diferenciável na travessia. E a *infinite-branch bigravity* (IBB) é
> o **único** modelo estável em todos os tempos daquele paper: esta é
> a porta mais cara que o repositório fechou.
>
> **Estado correto** *[à data desta nota; superado pelo bloco de
> VEREDITO abaixo — a exclusão ganhou, de fato, o argumento novo que
> este parágrafo exigia]***:** a saída do ramo infinito não é "fechada"
> nem "aberta e viável" — está **REABERTA e exige reavaliação**. Ou a
> exclusão ganha um argumento novo que responda aos três deles, ou
> cai. **Caveat de escopo, obrigatório em toda menção:** o IBB viável
> exige β₄ ≠ 0, especificamente `0 < β₄ < 2β₁`, enquanto a nossa
> célula mínima tem β₄ = 0 — o alvo do reexame é o ramo infinito da F1
> **com β₄ ligado**, e não a célula atual. A "segunda solução tardia
> inexplorada" que esta Parte A já registrava é justamente o objeto
> desse reexame.
>
> **[ATUALIZADO 2026-08-13 — 1503.07436 verificado na fonte pelo
> autor.]** Existe um **argumento independente candidato**, e ele não
> é o nosso: saúde de Higuchi em universo em expansão exige **r′ > 0**,
> enquanto o ramo infinito é definido por **r′ < 0**. Cai a
> caracterização anterior desta nota, de que as duas linhas do
> `posicionamento_literatura.md` sobre esse paper eram contraditórias
> — são o mesmo enunciado em ramos diferentes, e são consistentes. A
> tensão real é entre as **duas fontes** (1407.4331 declara o IBB
> estável *no canal de gradiente*; 1503.07436 o ataca *pelo Higuchi*),
> e dissolve-se pela separação de canais: gradiente,
> Higuchi/helicidade-0 e setor tensorial são perguntas distintas.
> **A exclusão ficou REABERTA** *[estado desta nota quando escrita;
> superado pelo bloco de VEREDITO logo abaixo]***:** o argumento é
> nível 3 e ainda não
> foi traduzido para as convenções do projeto — esse teste é o próximo
> item da fila. Ver `docs/posicionamento_literatura.md` §2b.
>
> **O que esta nota NÃO move:** o no-go de gradiente do **ramo finito**
> continua de pé, e as outras três saídas (modulação β₁(φ₋) — Parte B;
> screening de Vainshtein — R-10d; forma-β — R-11) continuam
> **fechadas**. *Fonte:
> `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b).*

> **[VEREDITO — 2026-08-13, R-13a + R-13b] RAMO INFINITO IBB DA F1:
> EXCLUÍDO PELO GHOST DE HIGUCHI.** *Bloco acrescentado; o texto
> original da Parte A e a nota de REABERTURA acima permanecem intactos
> como registro do caminho.*
>
> **Qualificação obrigatória, que precisa aparecer toda vez que o
> histórico desta saída for contado.** A exclusão original, pelo
> cruzamento `ξ = 0` — a que esta Parte A estabelecia —, permanece
> **REVOGADA**: nada aqui a ressuscita, e o quique do lapso continua não
> sendo, por si só, uma singularidade. A exclusão vigente é
> **independente**: o ramo infinito **viola a condição de Higuchi
> durante toda a história** nas células IBB testadas. A contagem passa
> de "três fechadas + uma reaberta" a **quatro rotas novamente
> fechadas, com a exclusão do IBB inteiramente substituída** — e a
> substituição tem de ser visível, nunca a contagem sozinha.
>
> **O critério, traduzido e verificado.** O funcional de Higuchi da
> fonte (Könnig 2015, arXiv:1503.07436, eq. 14) foi extraído **na
> fonte** e traduzido para as convenções do projeto (R-13a §2), e a
> tradução foi **re-verificada por CAS em rota independente** — três
> resíduos simbólicos **zero**, com `β_n` e `μ` gerais e matéria de
> poeira (R-13b §8.2). A cadeia fecha exata:
> **Higuchi ⟺ `ξ ≥ r` ⟺ `r′ ≥ 0`**.
>
> **A medida** (R-13b §§5–6; células IBB genuínas β₂ = β₃ = 0, β₁ > 0,
> `0 < β₄/β₁ < 2μ^{3/2}`): `r′ < 0` em **100% da história em 108/108
> células**; Higuchi satisfeito em **0 de 64 800 pontos**; concordância
> Higuchi(fonte) ⟺ `r′ ≥ 0` em **64 800/64 800**; **controle positivo**
> no ramo finito **400/400** — o gate aprova o que deve aprovar. Forma
> fechada: `m_T²/H²|_{r_c} = 1 + 1/(μr_c²)` com `μr_c² > 1` sempre,
> logo **1 < sup(m_T²/H²) < 2 estrito** em toda a janela; e **`μ` é
> pura reescala** no IBB genuíno.
>
> **O que o veredito não é.** *"The IBB branch is not tachyonic in the
> tensor-mass sense; it is excluded by the Higuchi ghost condition."*
> `m_T² > 0` em **108/108** — e isso **não** o salva.
>
> **Complementaridade — é este o achado.** *"Within the F1
> parameterization, the two standard cosmological branches fail for
> complementary reasons: the finite branch violates scalar-gradient
> stability in the early universe, while the genuine infinite branch
> avoids that instability but violates the Higuchi condition throughout
> its evolution."* O gradiente do IBB é **saudável segundo a fonte**
> (§IV A de 1503.07436, que **confirma** e **não** retrata 1407.4331):
> canal independente, que não salva o Higuchi.
>
> **Ponto lógico, declarado.** O gate do R-13b **não mede gradiente**, e
> essa cegueira continua declarada como boa prática (regra 7). Ela
> **não bloqueia o veredito**: um ghost físico basta para excluir,
> independentemente de o gradiente estar saudável. Um teste de `c_s²` no
> IBB é **validação adicional desejável, não requisito** — o veredito
> não o aguarda.
>
> | Saída | Veredito vigente | Razão |
> |---|---|---|
> | Infinite branch / IBB | **EXCLUÍDO** | ghost de Higuchi, `r′ < 0` em toda a história |
> | argumento antigo `ξ = 0` | **REVOGADO** | zero do lapso / quique não é por si só singularidade |
> | gradiente no IBB | **SAUDÁVEL** segundo a fonte | canal independente; não salva o Higuchi |
>
> *Fontes: `docs/resultado_r13a_criterio_higuchi_fonte.md`;
> `docs/resultado_r13b_ibb_ramo_infinito.md` §§4–6 e §8;
> `auditoria/code/out/r13b_ibb_ramo_infinito.txt`.*

`docs/resultado_ramo_finito.md` §2 descartava o ramo infinito porque
"dá ξ < 0, isto é, lapso negativo no setor f". A varredura de todas as
raízes reais positivas da cúbica mostra que a frase é **verdadeira
apenas no regime primordial**:

| a | raiz | r | ξ | H² | viável? |
|---|---|---|---|---|---|
| 0.001 | 0 | 1.7e−09 | +6.7e−09 | +1.0e08 | sim |
| 0.001 | **1** | 1.9e+04 | **−9.4e+03** | +2.9e07 | **não** |
| 0.1 | 1 | 19.7 | **−8.38** | +32.2 | **não** |
| 1 | **1** | 2.358 | **+1.985** | +0.334 | **SIM** |
| 10 | 1 | 2.227 | +2.227 | +0.288 | **SIM** |
| 10³ | 1 | 2.227 | +2.227 | +0.288 | **SIM** |

Idêntico em β₁ = 4.47 (segunda raiz viável a partir de a ≈ 1, com
r = 8.0).

**Leitura correta:** a segunda raiz tem ξ < 0 no primordial e ξ > 0 no
tardio, logo **ξ cruza zero** em algum a ∈ (0.1, 1). Uma trajetória
cosmológica contínua nesse ramo teria de atravessar ξ = 0 — lapso do
setor f anulando-se, ponto singular. **A exclusão para uma história
contínua está portanto CORRETA**; o que estava errado era a
justificativa ("dá ξ<0", sem qualificar época).

**Mas há um achado real:** existe uma **segunda solução tardia
viável** (r ≈ 2.23, ξ ≈ 2.23, H² > 0), completamente inexplorada pelo
repositório. Ela não se conecta ao nosso primordial, mas é uma
configuração de fundo legítima da mesma ação. Como o problema atual é
justamente o primordial, vale registrar: *o espaço de soluções do
fundo é maior do que a cascata assumiu.*

**Correção a aplicar:** `resultado_ramo_finito.md` §2 e o cap. 05 da
v2 devem dizer "ξ < 0 **no regime primordial**; a segunda raiz torna-se
viável em a ≳ 1 mas não conecta continuamente (ξ cruza zero)".

## Parte B — A modulação β₁(φ₋) **não** salva: a instabilidade sobrevive

Medido c_s²(a) ao longo do fundo dinâmico completo (célula REF,
condensação de φ₋, fatias moduladas com β₁′ e β₁″, kh = 30):

| a | r | φ₋/v | c_s² |
|---|---|---|---|
| 0.010 | ~0 | 0.001 | **−1.010** |
| 0.047 | 2e−04 | 0.001 | **−0.999** |
| 0.100 | 1.6e−03 | 0.001 | **−0.901** |
| 0.216 | 0.011 | 0.001 | **−0.287** |
| 0.465 | 0.026 | 0.002 | +0.698 |
| 1.0 | 0.030 | 0.003 | +0.974 |
| ≥10 | 0.031→0.50 | 0.015→0.93 | +1.01 a +2.17 |

**Resultado:** c_s² < 0 em 5/22 amostras, de a = 0.010 a a = 0.216 —
**3.07 e-folds** de instabilidade. O crescimento acumulado para o modo
kh = 30 é **lnA = 85.7**, muito acima do limiar de não-linearidade
(11.5). **A instabilidade sobrevive à modulação.**

Duas observações finas:

1. **A modulação muda o limiar, e para melhor.** No fundo β-constante
   a estabilidade só chega em r ≈ 0.17; no dinâmico, c_s² já é
   positivo com r ≈ 0.026 (a = 0.465). Ou seja, β₁(φ₋) *desloca* a
   fronteira — é a primeira vez que a modulação produz um efeito
   físico favorável mensurável. Mas o deslocamento não é suficiente:
   a era instável ainda dura 3 e-folds.
2. **A condensação chega tarde demais.** Em a = 0.465, φ₋/v = 0.002 —
   a condensação ainda não começou. O que estabiliza ali é a evolução
   de r pela diluição de ρ, não a modulação. A modulação só age em
   a ≳ 10³ (φ₋/v > 0.01), muito depois da era instável.

**Consequência de desenho:** se a modulação for para salvar a
implementação, ela precisa **ocorrer mais cedo** — o que significa
mexer em μ₋/λ_c (a época crítica da bifurcação), não em v★. Isso
conecta com o vínculo de paredes de domínio do parecer de fundamentos
quânticos (μ₋ ≲ λ₋^{1/3} MeV): as duas restrições agora apontam para o
mesmo parâmetro, em direções que precisam ser checadas juntas.

## Fronteiras e ressalvas

Uma trajetória (célula REF), sem radiação, kh = 30, 22 amostras. O
calibrador (espectador) fica em 0.997–1.023 — nos pontos tardios
desvia 2.3% de 1, acima do 1% ideal; os pontos da era instável têm
calibração 1.00000, portanto o achado principal não é afetado. Um
ponto (a = 4.6e3) reportou K₂ < 0 isoladamente, fora da era instável e
sem afetar o veredito — anotado para verificação.

## O que resta das saídas do R-10a §4

| Saída | Estado |
|---|---|
| 1. Screening / auto-invalidação linear | **Única viva** — não testada; agora é o único caminho conhecido |
| 2. Ramo infinito | *[texto original:]* **Fechada** (não conecta continuamente) — mas há segunda solução tardia inexplorada. **[2026-08-13, R-12i: REABERTA]** a exclusão por ξ cruzar zero não se sustenta: é o quique de `b` que 1407.4331 §II/§VI trata e defende como físico, com três argumentos. Reexame pendente, e o alvo é o ramo infinito **com β₄ ≠ 0** (o IBB viável exige 0 < β₄ < 2β₁; a célula mínima tem β₄ = 0) — ver o banner da Parte A. **[2026-08-13, R-13a + R-13b: FECHADA POR OUTRA RAZÃO]** o reexame foi feito: o argumento `ξ = 0` **permanece REVOGADO** e a exclusão vigente é **independente** — **ghost de Higuchi durante toda a história** (`r′ < 0` em 100% da história em 108/108 células; Higuchi em 0/64 800 pontos; controle positivo no ramo finito 400/400). Ver o bloco de VEREDITO da Parte A |
| 3. Varredura de forma-β | Aberta; o R-8b mostrou rigidez da forma sob rescala, falta varrer forma |
| 4. Corte de época pela modulação | **Fechada** — a modulação chega ~3 ordens tarde demais |

**Fila:** o teste de Vainshtein/validade linear passa de "item nº 1"
a **único item**: é a última saída conhecida antes de concluir que a
implementação F1, no ramo finito e com esta forma-β, tem uma era de
instabilidade de gradiente que nenhum mecanismo interno cura.
