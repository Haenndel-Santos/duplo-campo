# TDCP v2 — Passo 2: Ghost-Freedom sob β_n(φ₋)

**Gate mais crítico do plano.** Toda a arquitetura da v2 depende dele.
Verificação parcial: `auditoria/code/gate2_lapso.py`.

---

## 1. O que precisa ser provado, exatamente

A ausência do fantasma de Boulware–Deser em Hassan–Rosen não é
acidente: decorre de uma estrutura específica. Enunciando com precisão
o que a v2 precisa preservar:

**Contagem alvo.** Espaço de fase das duas métricas espaciais:
2×(6+6)=24. O difeomorfismo diagonal remove 4 constraints de primeira
classe (×2 com fixação de gauge) = 8, deixando 16 → 8 graus. A
estrutura HR fornece **um par adicional de constraints de segunda
classe** (primária + secundária), removendo 1 grau: **7 = 2 (gráviton
sem massa) + 5 (gráviton massivo)**. Sem esse par, o oitavo grau é o
fantasma BD.

Somando os dois escalares primordiais, a v2 deve dar

$$\boxed{\;7 + 2 = 9 \text{ graus físicos}\;}$$

Se a contagem der **10**, o fantasma BD voltou e a arquitetura falha.

**O mecanismo que produz o par.** Após a redefinição de shift de
Hassan–Rosen, o termo de potencial torna-se **linear nos lapsos**. Os
lapsos deixam de ser determinados pelas próprias equações e passam a
ser multiplicadores de Lagrange — o que gera a constraint primária
$\mathcal C=0$. A exigência de que ela se preserve no tempo,
$\dot{\mathcal C}=\{\mathcal C,H\}=0$, gera a secundária. As duas
juntas formam o par de segunda classe.

**Portanto o Gate 2 tem duas partes, com dificuldades muito diferentes:**

| Parte | Enunciado | Dificuldade |
|---|---|---|
| **2.A** | A linearidade nos lapsos sobrevive a $\beta_n(\phi_-)$ | tratável — feita abaixo |
| **2.B** | A constraint secundária sobrevive | **cálculo aberto** |

---

## 2. Parte A — Linearidade nos lapsos (RESOLVIDA)

### 2.A.1 Argumento geral

O termo de potencial é $\sqrt{-g}\sum_n\beta_n(\phi_-)e_n(\mathcal K)$.
Em ADM, $\sqrt{-g}=N\sqrt\gamma$, e $e_n(\mathcal K)$ carrega a
estrutura de lapso conhecida do formalismo HR.

O ponto decisivo é elementar: **$\phi_-$ é um campo escalar, e o valor
de um campo escalar em um ponto não depende do lapso.** Logo
$\beta_n(\phi_-)$ é apenas um coeficiente que varia no espaço-tempo,
sem introduzir nenhuma dependência nova em $N$ ou $L$.

Formalmente: se $\sqrt{-g}\sum_n\beta_n e_n$ é linear em $(N,L)$ para
$\beta_n$ constantes, então é linear para $\beta_n$ quaisquer funções
de campos que não contenham lapso — porque a linearidade é termo a
termo em $n$, e $\beta_n$ multiplica cada termo por um escalar.

### 2.A.2 Verificação explícita em minisuperespaço

No fundo FLRW (Anexo B §B.4.2), com $\xi=N_f/N_g$:

$$\sqrt{-g}\,V = N_g a^3\sum_{n=0}^{4}\beta_n(\phi_-)\,e_n(\xi,r)$$

Expandindo termo a termo, com $e_n$ do Anexo A §A.7:

| $n$ | $e_n(\xi,r)$ | $N_g a^3\,\beta_n e_n$ |
|---|---|---|
| 0 | $1$ | $a^3\beta_0\,N_g$ |
| 1 | $\xi+3r$ | $a^3\beta_1\,(N_f + 3r\,N_g)$ |
| 2 | $3\xi r+3r^2$ | $a^3\beta_2\,(3r\,N_f + 3r^2 N_g)$ |
| 3 | $3\xi r^2+r^3$ | $a^3\beta_3\,(3r^2 N_f + r^3 N_g)$ |
| 4 | $\xi r^3$ | $a^3\beta_4\,r^3 N_f$ |

**Todo termo é de grau 1 em $N_g$ e grau 1 em $N_f$** — o $1/N_g$
implícito em $\xi$ cancela exatamente contra o $N_g$ do volume. E os
$\beta_n(\phi_-)$ passam como coeficientes inertes.

Isto é a sombra minisuperespaço do resultado ADM completo, e é
verificável simbolicamente: `gate2_lapso.py` confirma
$\partial^2/\partial N_g^2 = \partial^2/\partial N_f^2 = 0$ com os
$\beta_n$ como funções arbitrárias de $\phi_-$.

### 2.A.3 O setor escalar não estraga

O setor de $\phi_\pm$ contribui

$$\mathcal L_\phi = a^3\left(\frac{\dot\phi^2}{2N_g} - N_g V(\phi_+,\phi_-)\right)$$

que **não** é linear em $N_g$ (tem $1/N_g$). Isso é esperado e inócuo:
é exatamente a estrutura de qualquer matéria minimamente acoplada, e
matéria minimamente acoplada comprovadamente não reintroduz o fantasma
BD (é premissa do próprio teorema HR, e o Cap.17 §17.4 já a declarava).

O que importa é que o **potencial de interação** permanece linear — e
permanece.

**Conclusão da Parte A: a constraint primária sobrevive.** Nível 2a.

---

## 3. Parte B — A constraint secundária (ABERTA)

Aqui está o risco real, e é preciso ser explícito sobre ele.

Em HR puro, a secundária vem de

$$\dot{\mathcal C} = \{\mathcal C, H\} = 0$$

Na v2, duas coisas mudam simultaneamente:

1. $\mathcal C$ **agora depende de $\phi_-$**, através dos $\beta_n$.
2. $H$ ganha o setor escalar, $H = H_{\rm grav} + H_\phi$.

Logo

$$\{\mathcal C, H\} = \underbrace{\{\mathcal C, H_{\rm grav}\}}_{\text{como em HR}}
\;+\; \underbrace{\{\mathcal C, H_\phi\}}_{\textbf{novo}}$$

e o termo novo é não-nulo precisamente porque $\partial\mathcal C/\partial\phi_-\neq0$:

$$\{\mathcal C, H_\phi\} \;\supset\; \frac{\partial\mathcal C}{\partial\phi_-}\,\frac{\partial H_\phi}{\partial\pi_{\phi_-}}
\;=\; \frac{\partial\mathcal C}{\partial\phi_-}\cdot\frac{\pi_{\phi_-}}{a^3}$$

**A pergunta do gate:** a condição $\dot{\mathcal C}=0$ continua sendo
uma **constraint** (relação entre variáveis canônicas, independente do
lapso), ou passa a ser uma **equação que determina o lapso**?

- Se continua constraint → o par de segunda classe sobrevive → 9 graus
  → **Gate 2 PASSA**.
- Se passa a determinar o lapso → o par não se forma → o oitavo grau
  reaparece → 10 graus → **fantasma BD de volta, Gate 2 FALHA**.

### 3.1 Por que isto não é formalidade

A literatura de gravidade massiva com massa dependente de campo
("mass-varying massive gravity", quase-dílaton e variantes) tem
resultados **nos dois sentidos**, dependendo da estrutura do
acoplamento. Não existe teorema geral que autorize assumir a passagem.
É preciso calcular para a nossa estrutura específica.

### 3.2 Fator atenuante do nosso desenho

A v2 escolheu a modulação **mínima possível**: apenas $\beta_1$ depende
de $\phi_-$; $\beta_0,\beta_2,\beta_3,\beta_4$ são constantes
(`acao_v2.md` §1.2). Isso reduz o termo novo a uma única contribuição,
proporcional a $\partial\beta_1/\partial\phi_-$ — o caso mais favorável
possível dentro da classe de modulações diferenciais.

Não é garantia. Mas se existe uma subclasse que passa, esta é a
candidata natural.

---

## 4. Corroboração numérica — e por que ela NÃO certifica

O plano previa contagem de modos no espectro perturbativo como
corroboração. Aqui é preciso registrar uma limitação que vem
diretamente da estratificação epistêmica:

**A D1 declara, em seus próprios caveats, que a análise em fundo
congelado ($\dot H=\dot H_f=\dot\xi=0$) não enxerga a remoção de modo
por constraint secundária dependente do tempo.**

E a remoção do fantasma BD é feita exatamente por uma constraint
secundária. Portanto:

| Resultado da contagem | O que conclui |
|---|---|
| **10 modos** | Fantasma presente → **Gate 2 FALHA** (conclusivo) |
| **9 modos** | Compatível, mas **não prova nada** — o fundo congelado é cego ao mecanismo |

Ou seja: a contagem numérica serve como **falsificação**, nunca como
certificação. É Nível 2b, e o Gate 2 exige 2a.

**Isso reforça que a Parte B tem de ser analítica.** Não há atalho
numérico.

---

## 5. Critério do Gate 2

| | |
|---|---|
| **Critério** | A constraint secundária existe e é independente do lapso, com $\beta_1(\phi_-)$ variável; contagem final = 9 graus |
| **Nível exigido** | **2a obrigatoriamente** para a Parte B |
| **Parte A** | ✅ **RESOLVIDA** — linearidade nos lapsos preservada (Nível 2a) |
| **Parte B** | ⬜ **ABERTA** — cálculo do bracket $\{\mathcal C,H_\phi\}$ |
| **Falsificação rápida** | contagem de modos: se der 10, falha na hora |

### Se falhar

Em ordem de preferência:

**(a) Restringir a classe de $\beta_n(\phi_-)$.** Pode existir uma
condição sobre $\partial\beta_n/\partial\phi_-$ que anule o termo
problemático do bracket. Vale procurar antes de abandonar — seria uma
condição derivada, não um ajuste.

**(b) Mudar o que é modulado.** Em vez de $\beta_n(\phi_-)$, testar
modulação via um acoplamento que não entre no potencial HR — mas note
que isso provavelmente recai na degenerescência da §0 de `acao_v2.md`
(modulação que não move a raiz).

**(c) Aceitar o resultado.** Se nenhuma subclasse funciona, a conclusão
honesta é que a evolução estrutural via raiz móvel é incompatível com
ghost-freedom em HR — o que é, em si, um resultado publicável e
encerra a questão de forma limpa.

---

## 6. Próximo artefato necessário

O cálculo da Parte B precisa de:

1. ADM completo do potencial HR com a redefinição de shift de
   Hassan–Rosen (não minisuperespaço — a constraint secundária é uma
   afirmação sobre o sistema com dependência espacial).
2. $\mathcal C$ explícito com $\beta_1(\phi_-)$.
3. O bracket $\{\mathcal C, H_{\rm grav}+H_\phi\}$.
4. Verificar se o resultado contém $N$ ou $L$.

É trabalho de porte — provavelmente uma sessão dedicada, com sympy
sobre a estrutura ADM. **Não deve ser feito por atalho, e o Passo 3 não
começa antes.**
