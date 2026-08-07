# Erratum 01 — O segundo fator da constraint de Bianchi

**Data:** 2026-08-07. **Gravidade:** alta — afeta o corpus, as âncoras
D1/D2/D5 e o `parecer_tecnico.md`.

**Descoberto em:** Passo 2 do plano v2, ao derivar a constraint
secundária pelo formalismo canônico.

---

## 1. O erro

O corpus escreve a constraint de Bianchi como

$$\big(\beta_1+2\beta_2r+\beta_3r^2\big)\big(H_g-\xi H_f\big)=0
\qquad\textbf{(FORMA DO CORPUS — ERRADA)}$$

em Cap.5 §5.5, Cap.14, Anexo B §B.8 (`[AB.54]`, `[AB.56]`, `[AB.71]`),
Anexo E §E.3(6) (`[AE.14]`) e Anexo H (`[AH.11]`).

A forma correta é

$$\boxed{\big(\beta_1+2\beta_2r+\beta_3r^2\big)\big(N_f\,\dot a-N_g\,\dot b\big)=0}$$

equivalentemente $\mathcal B(r)\,(\dot a/N_g-\dot b/N_f)=0$.

### Por que as duas diferem

Com $N_g=1$: a forma do corpus dá $\dot a/a-\dot b/b$; a correta dá
$\dot a-\dot b/N_f$. Coincidem apenas se $\xi=r$.

Um sintoma que deveria ter chamado atenção antes: **a forma do corpus
contém o lapso** (via $\xi=N_f/N_g$). Uma constraint canônica genuína é
uma relação entre variáveis de espaço de fase e é livre de lapso por
construção. A forma correta passa nesse teste; a do corpus não.

## 2. Como foi verificado

Duas rotas independentes, ambas a partir da lagrangiana de
minisuperespaço do Anexo B §B.4.5 (que está correta — verificada termo
a termo no lote 7):

**Rota canônica** (`auditoria/code/gate2_bracket.py`): o bracket
$\{\mathcal H_g,\mathcal H_f\}$ das duas constraints primárias produz
o fator $(M_g^2a\,p_b-M_f^2b\,p_a)\propto(\dot a/N_g-\dot b/N_f)$.

**Rota lagrangiana** (`auditoria/code/bianchi_rota_lagrangiana.py`): a
consistência temporal do vínculo de $N_g$, eliminando segundas
derivadas pelas equações de $a$, $b$, $\phi$ e usando o vínculo de
$N_f$, deixa o resíduo

$$3M_{\rm eff}^2m^2\,(N_f\dot a-N_g\dot b)\,(\beta_1a^2+2\beta_2ab+\beta_3b^2)\big/N_g$$

Teste por substituição (não por divisão): anular o candidato do corpus
deixa resíduo não-nulo; anular o canônico zera o resíduo exatamente.

**Ressalva de modo comum:** as duas rotas compartilham a lagrangiana
como entrada. Ela está bem verificada (lote 7, `[AB.17]`–`[AB.25]`
todas CONFERE, com conferência explícita), e o próprio corpus a usa
para derivar corretamente as duas Friedmann. Mas é a única premissa
comum às duas rotas.

## 3. Consequência imediata: ṙ no ramo dinâmico

O ramo dinâmico correto é $N_f\dot a=N_g\dot b$, isto é
$\xi=\dot b/\dot a$. Substituindo em $\dot r=r(\dot b/b-\dot a/a)$:

$$\boxed{\dot r = \frac{\dot a}{a}\,(\xi-r) \;=\; H_g\,(\xi-r)\ \ (N_g=1)}$$

**ṙ só se anula se ξ=r.** Genericamente, **r evolui**.

Isto **inverte** o resultado da âncora D5.

## 4. O que a D5 mostrou e o que não mostrou

A álgebra da D5 está correta: dado $H_g=\xi H_f$, segue $\dot r=0$.
O que a D5 não verificou foi se $H_g=\xi H_f$ é a condição de ramo —
ela tomou a constraint do corpus como dada.

**D5 passa a ser: consequência correta de premissa errada.**

Reclassificação: o resultado "$\dot r\equiv0$" sai do Nível 1 e é
**retirado**. Em seu lugar, Nível 1: $\dot r=H_g(\xi-r)$.

## 5. Efeito sobre D1, D2 e D8

As âncoras montaram os benchmarks de "ramo dinâmico" impondo
$\xi=H_g/H_f$ (tabela da D1: $r=1.20$, $\xi=3.497$).

Mas no ramo dinâmico **correto**, com $\dot b=\xi\dot a$:

$$\frac{H_g}{H_f}=\frac{\dot a/(aN_g)}{\dot b/(bN_f)}=r$$

ou seja, $H_g/H_f=r$, **não** $\xi$. Impor $\xi=H_g/H_f$ equivale a
impor $\xi=r$ — que é justamente o caso $\dot r=0$, e no benchmark da
D1 ($r=1.20$, $\xi=3.497$) essa igualdade não vale.

| Âncora | O que sobrevive | O que precisa refazer |
|---|---|---|
| **D1** | benchmark C (ramo **algébrico**, $r=r_\star$): a degenerescência cinética na raiz é real e independe deste erro | benchmarks A e B (par fantasma/taquiônico "no ramo dinâmico") — o fundo não é o ramo dinâmico |
| **D2** | a **forma fechada** de $m_T^2$ com ξ — é Nível 2a, simbólica, não depende de benchmark | a avaliação numérica ($m_T^2=-3.19$, Higuchi violado) — mesmo fundo incorreto |
| **D3** | tudo — regra da cadeia, independe da constraint | — |
| **D8** | o achado documental (faixa m_S0 é design, não dinâmica) | o scan 0/60, se usou o ramo dinâmico incorreto |
| **D6, D7** | não usam a constraint de ramo | — |

## 6. Efeito sobre o parecer

O veredito **"o ramo dinâmico está duplamente morto"** (Problema
Transversal 1) perde as duas pernas:

- $\dot r\equiv0$: **retirado** — era premissa errada;
- par fantasma: **suspenso** — calculado em fundo que não é o ramo.

Não é que o ramo dinâmico esteja provado saudável. Está **não
avaliado**. É diferente, e a diferença importa.

Ironia registrada: o Cap.14 §14.12, que a auditoria criticou por
"contornar" $\dot r=0$ trocando a constraint, tinha a **intuição
física correta** — o autor percebeu que $\dot r=0$ não podia ser o fim
da história. O método (trocar constraint sem derivar) continua
indefensável, e a condição que ele usou ($H_b=\xi H_g$) também está
errada, por outro fator. Mas a crítica de que "o §14.11 estava certo e
o §14.12 o contornou" se inverte: **§14.11 estava errado** (por herdar
a premissa) e o §14.12 estava tateando na direção certa pelo caminho
errado.

## 7. Vereditos da auditoria a revisar

| Local | Veredito atual | Ação |
|---|---|---|
| Cap.5 §5.5 (constraint) | CONFERE | corrigir o segundo fator |
| Cap.5 §5.5B (legenda "r(t) evolui") | ERRO (D5) | **a legenda estava certa** |
| Cap.14 §14.4B (mesma legenda) | ERRO (D5) | idem |
| Cap.14 §14.11 (deriva ṙ=0) | CONFERE | premissa errada — rever |
| Cap.14 §§14.12–14.17 | 11 × ERRO | crítica de método mantida; física a reavaliar |
| Anexo B `[AB.54/56/71]` | CONFERE SOB HIPÓTESE | corrigir o segundo fator |
| Anexo B `[AB.65]` (ṙ=0) | CONFERE | premissa errada — rever |
| Anexo E `[AE.14]`, `[AE.51]` | CONFERE | idem |
| Anexo H `[AH.11]` | CONFERE | corrigir |

## 8. Falha de método que permitiu isto

No lote 7, achado H5, a auditoria **registrou** que a constraint do
Anexo B é citada e não derivada — o texto anuncia "vamos mostrar por
que essa estrutura aparece" e não mostra. E mesmo assim atribuiu
`CONFERE SOB HIPÓTESE`, com a justificativa de que "o resultado é o
padrão conhecido da literatura de gravidade bimétrica HR".

Isso é reconhecimento de padrão — **Nível 3** — aplicado com peso de
Nível 2a. É exatamente o que a estratificação epistêmica (Parte III-B
do parecer) existe para impedir, e passou porque não foi aplicada à
própria auditoria.

**Regra derivada deste erratum:** quando o corpus declara que vai
derivar algo e não deriva, o veredito não pode ser CONFERE sob nenhuma
qualificação. Ou se deriva na auditoria, ou o veredito é INCOMPLETA
com a lacuna nomeada. "Bate com a literatura" é Nível 3 e não fecha
lacuna de derivação.

Nota adicional: a auditoria leu 856 equações e pegou 115 erros de
escrita. Este erro não era de escrita — era de conteúdo, numa fórmula
plausível e não derivada. **Leitura sequencial não pega esse tipo.** Só
recalcular pega.

## 9. Efeito sobre o plano v2

O Passo 1 (ação) e o Gate 2 Parte A (linearidade nos lapsos) não são
afetados — não dependem da forma da constraint.

O achado do Gate 2 (a constraint **não fatora** com $\beta_1(\phi_-)$,
resíduo $-M_{\rm eff}^2m^2p_\phi\beta_1'$) **também não é afetado**:
ao anular $\mathcal B(r)$, o fator cinemático morre inteiro, seja qual
for sua forma.

O que muda é a **motivação** da arquitetura. A v2 adotou
$\beta_n(\phi_-)$ porque "os dois ramos estão mortos". Metade dessa
premissa caiu. O Passo 3 precisa começar por reavaliar o ramo dinâmico
correto — que agora tem $\dot r\neq0$ e pode não precisar de modulação
nenhuma para produzir evolução estrutural.

**O Passo 3 não deve começar antes dessa reavaliação.**
