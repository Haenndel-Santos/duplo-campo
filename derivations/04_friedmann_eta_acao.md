# Derivação 4 — H² = (8πG/3)ρ_tot/(1−η) a partir de uma Ação

**Skill invocado:** `mathematical-consistency-auditor`.

## 1. O que está sendo derivado e por que é necessário

A forma "$H^2=\frac{8\pi G}{3}\frac{\rho_{tot}}{1-\eta}$" aparece **quatro
vezes** no corpus, sempre **afirmada diretamente**, nunca deduzida de uma
ação:

- Cap.1 §1.6: *"Essa diferença acumulada **pode** modificar a dinâmica
  cosmológica efetiva: $H^2=\frac{8\pi G}{3}\frac{\rho}{1-\eta}$."*
- Cap.2 (com $\eta=\int^t\Gamma(H_g-H_f)^2dt$, uma definição de $\eta$
  diferente da usada depois): mesma frase, mesma equação.
- Anexo E §E.7 (*"aqui está o pulo do gato"*): a equação é reintroduzida
  do zero, sem citar de onde vem, imediatamente antes de ser diferenciada
  em $N$ para fechar o sistema de ODEs.
- Anexo H §H.6, como *"forma compacta final"*: *"Podemos escrever **a
  essência** da TDCP como: $\boxed{H^2=\frac{8\pi G}{3}\frac{\rho_m+\rho_\chi+\rho_{int}}{1-\eta}}$."*

O problema estrutural é que **os mesmos dois anexos** (E e H) que
afirmam essa equação também **derivam** — a partir da ação bimétrica
HR + $\chi$ minimamente acoplado (Anexo B §B.4.5, Anexo A, Anexo E §E.3,
Anexo H §H.3) — a equação de Friedmann visível **sem nenhum termo em
$\eta$**:

$$ \text{Anexo E §E.3(1) / Anexo H §H.3(1):}\qquad 3M_g^2H^2 = \rho_m+\tfrac12\dot\chi^2+U(\chi)+m^2M_{eff}^2F(\chi)\mathcal V(r). $$

As duas formas **não podem ambas ser "a" equação de Friedmann do setor
$g$**: uma tem $1/(1-\eta)$ multiplicando $\rho_{tot}$, a outra não. Esta
derivação verifica se a forma com $\eta$ é obtível a partir de alguma
ação, e, não sendo, constrói explicitamente a extensão mínima que a
geraria — e mostra exatamente o que essa extensão produz de fato.

## 2. Ponto de partida

**O que já está estabelecido como vindo de uma ação:** o Anexo B §B.4.5
escreve a Lagrangiana minisuperespaço completa da TDCP:

$$ \mathcal{L} = -3M_g^2\frac{a\dot a^2}{N_g} - 3M_f^2\frac{b\dot b^2}{N_f} - m^2M_{eff}^2N_g a^3F(\chi)V(\xi,r) + a^3\Big(\frac{\dot\chi^2}{2N_g}-N_gU(\chi)\Big) - N_ga^3\rho_m. $$

**$\eta$ não aparece em nenhum termo desta Lagrangiana.** Não há campo
$\eta$, não há termo cinético para $\eta$, não há acoplamento de $\eta$
a $R_g$, $R_f$, ou a qualquer outro campo. Consequentemente, variar essa
ação (como já feito em §B.5/§B.6, e verificado na Derivação 3) **não
pode, por construção, produzir nenhum termo em $\eta$** na equação de
Friedmann resultante — o que é exatamente o que se observa em Anexo E
§E.3(1) / Anexo H §H.3(1).

Confirmando isso, o próprio Anexo H (§H.2, "Postulados Fundamentais")
introduz a evolução de $\eta$ como o **Postulado 5** ("Irreversibilidade
Estrutural"): $\dot\eta=\Gamma\dot\chi^2$ — listado ao lado de postulados
como a existência das duas métricas e a forma $V(\mathcal K)$, **não**
como algo derivado de uma equação de movimento obtida por variação. Isso
confirma, pela própria estrutura que o texto declara para si mesmo, que
$\eta$ é, no estado atual da TDCP, uma variável auxiliar **definida por
uma equação de evolução postulada**, e não um campo dinâmico com um
termo próprio na ação.

## 3. Derivação completa

### 3.1 Por que a ação existente não pode gerar o fator $(1-\eta)$

Isso já está estabelecido na seção 2: $\eta$ está ausente da
Lagrangiana do Anexo B §B.4.5, então nenhuma variação dessa ação
(em $N_g$, $N_f$, $a$, $b$, ou $\chi$) pode produzir um termo em $\eta$
em qualquer equação de campo. O fator $(1-\eta)$ em Cap.1/Cap.2/§E.7/§H.6
**tem que** vir de fora dessa ação — ele é inserido à mão nas quatro
ocorrências, nunca derivado.

### 3.2 Construção da extensão mínima que geraria o fator $(1-\eta)$

A única forma estruturalmente natural de fazer um fator $(1-\eta(t))$
multiplicar $\rho_{tot}$ do lado direito de uma equação com $H^2$ do
lado esquerdo, **sem** alterar a forma de $G_{\mu\nu}=3H^2$ (que é pura
geometria, fixa), é tornar a "constante" de Planck do setor $g$
dependente do tempo através de $\eta$ — isto é, acoplar $\eta$
**não minimamente** ao escalar de Ricci do setor $g$:

$$ S_g \supset \int d^4x\sqrt{-g_g}\;\frac{\Omega(t)}{2}R_g, \qquad \Omega(t)\equiv M_g^2\big(1-\eta(t)\big). $$

Esta é exatamente a estrutura de uma teoria escalar-tensorial tipo
Brans--Dicke (ou "massa de Planck rodante"), com $\Omega$ dependendo do
tempo apenas através de $\eta(t)$ (que por sua vez dependeria de $\chi$
via o Postulado 5). **Esta é uma extensão proposta — não existe
atualmente em nenhuma ação escrita no corpus.**

### 3.3 Equação de campo exata da extensão proposta (verificada via geometria FLRW completa)

A variação padrão de $\int\sqrt{-g}\,\Omega R/2$ em relação a $g^{\mu\nu}$
(resultado estabelecido de teorias escalares-tensoriais, ver p.ex.
Brans--Dicke) produz, além do tensor de Einstein usual multiplicado por
$\Omega$, um termo extra vindo de $\Omega$ não ser constante:

$$ \Omega\,G_{\mu\nu} = T_{\mu\nu} + \nabla_\mu\nabla_\nu\Omega - g_{\mu\nu}\Box\Omega. $$

Como este termo extra ($\nabla_\mu\nabla_\nu\Omega$, $\Box\Omega$) é
exatamente o tipo de cálculo que excede uma conta seguro à mão (requer
os símbolos de Christoffel, o tensor de Ricci e o d'Alembertiano
covariante de um escalar, todos no FLRW), ele foi computado **do zero**
— sem assumir nenhuma fórmula "de livro" para a equação de Friedmann
escalar-tensorial — em `derivations/code/04_friedmann_eta_check.py`:
o script constrói a métrica FLRW plana, calcula os símbolos de
Christoffel, o tensor de Riemann, o tensor de Ricci, o escalar de Ricci
e o tensor de Einstein inteiramente por álgebra tensorial explícita
(sem pacotes de relatividade prontos), confirma $G_{00}=3H^2$ como
checagem de sanidade, e então calcula $\nabla_0\nabla_0\Omega$ e
$\Box\Omega$ para $\Omega=M_g^2(1-\eta(t))$.

Resultado do script (componente "00" da equação de campo, já substituindo
$\dot a=Ha$):

$$ 3M_g^2(1-\eta)H^2 \;-\; 3M_g^2H\dot\eta \;=\; \rho_{tot}. $$

Isolando $H^2$:

$$ H^2 = \frac{\rho_{tot}}{3M_g^2(1-\eta)} + \frac{H\dot\eta}{1-\eta}. $$

### 3.4 Comparação com a meta postulada

A meta (Cap.1/Cap.2/§E.7/§H.6, com $8\pi G\equiv 1/M_g^2$ — identificação
já usada de forma consistente em todo o corpus, já que $M_g$ é definida
como "massa de Planck associada à métrica $g$") é:

$$ H^2_{\text{meta}} = \frac{\rho_{tot}}{3M_g^2(1-\eta)}. $$

O script calcula explicitamente o resíduo:

$$ H^2_{\text{exato}} - H^2_{\text{meta}} = \frac{H\dot\eta}{1-\eta}, $$

que **não** é identicamente nulo — só se anula se $\dot\eta\to0$. Ou
seja: **mesmo a extensão mínima natural (acoplamento não-mínimo
$\Omega(\eta)R_g$) não reproduz exatamente a equação postulada** — ela
produz essa equação **mais** um termo de atrito $H\dot\eta/(1-\eta)$
vindo da própria variação temporal de $\eta$, que as quatro ocorrências
no corpus omitem inteiramente.

O termo extra é desprezível apenas na aproximação adiabática
$|\dot\eta|\ll H(1-\eta)$ — que, para $\eta\ll1$ (regime explicitamente
assumido em Cap.1 §1.6, *"Para $\eta\ll1$"*), se reduz a $|\dot\eta|\ll
H$: **$\eta$ deve variar lentamente comparado à taxa de Hubble**. Essa
condição não está declarada em nenhuma das quatro ocorrências da
equação.

### 3.5 Uma segunda lacuna independente: a evolução de $\eta$ não vem desta ação

Mesmo aceitando a extensão de 3.2 e a aproximação adiabática de 3.4, resta
um problema separado: variar a ação estendida em relação ao próprio
$\eta$ produziria um termo $-\,\delta(\Omega)/\delta\eta\cdot R_g/2 =
M_g^2R_g/2$ na equação de movimento de $\eta$ — **não** o Postulado 5
($\dot\eta=\Gamma\dot\chi^2$). Para manter essa lei de evolução
postulada dentro de uma ação, seria necessário adicionar um termo de
multiplicador de Lagrange independente,

$$ S_\eta \supset \int d^4x\sqrt{-g_g}\;\lambda(t)\big[\dot\eta-\Gamma\dot\chi^2\big], $$

impondo a relação como uma constraint, em vez de deixá-la emergir da
extremização da ação gravitacional. Isso é uma **segunda hipótese
estrutural independente**, adicional ao acoplamento não-mínimo de 3.2.

## 4. Resultado final em forma fechada

$$ \boxed{ \begin{aligned} &\text{Com a ação atualmente escrita no corpus (Anexo B §B.4.5), } \eta \text{ não aparece,}\\ &\text{logo } H^2=\frac{8\pi G}{3}\frac{\rho_{tot}}{1-\eta} \text{ não é derivável dela.}\\[4pt] &\text{A extensão mínima que geraria um fator } (1-\eta) \text{ — acoplamento não-mínimo}\\ &\Omega(t)=M_g^2(1-\eta(t)) \text{ ao escalar de Ricci } R_g \text{ — produz, em vez disso:}\\[4pt] &3M_g^2(1-\eta)H^2 - 3M_g^2H\dot\eta = \rho_{tot},\\[4pt] &\text{que se reduz à forma postulada apenas na aproximação adiabática } |\dot\eta|\ll H(1-\eta). \end{aligned} } $$

## 5. Classificação final

**NÃO DERIVÁVEL SEM DADO EXTERNO / SEM ACOPLAMENTO ADICIONAL.**

O que falta, precisamente:

1. **Um termo de ação para $\eta$.** A Lagrangiana minisuperespaço
   efetivamente usada em todo o formalismo (Anexo B §B.4.5, e todas as
   equações de fundo que dela derivam nos Anexos A/E/H) não contém
   $\eta$. Sem um termo assim, $\eta$ não pode aparecer em nenhuma
   equação de campo — a Friedmann derivada da ação (Anexo E §E.3(1) =
   Anexo H §H.3(1)) confirma isso ao não conter $\eta$.

2. **Um acoplamento não-mínimo explícito**, proposto aqui como a
   extensão mínima ($\Omega(\eta)R_g$, seção 3.2) — esta é uma hipótese
   estrutural nova, não presente em nenhuma versão atual da ação, e deve
   ser declarada como tal se adotada, não introduzida silenciosamente
   como neste anexo.

3. **Mesmo com essa extensão, uma hipótese adicional de adiabaticidade**
   ($|\dot\eta|\ll H$, para $\eta\ll1$) é necessária para recuperar a
   forma exata postulada — sem ela, a equação correta tem um termo extra
   $H\dot\eta/(1-\eta)$ que muda a dinâmica (em particular, contribui
   para $w_{\text{eff}}$ de uma forma que as Seções E.6–E.7 não incluem).

4. **Uma constraint independente (multiplicador de Lagrange) para
   preservar $\dot\eta=\Gamma\dot\chi^2$** (Postulado 5, Anexo H §H.2)
   — sem ela, mesmo a extensão de acoplamento não-mínimo não reproduz a
   lei de evolução de $\eta$ já postulada em outro lugar do texto.

**Recomendação para o corpo principal:** tratar a equação
$H^2=(8\pi G/3)\rho_{tot}/(1-\eta)$ explicitamente como uma
**aproximação fenomenológica de uma extensão proposta** (acoplamento
não-mínimo + constraint), válida no regime adiabático $|\dot\eta|\ll H$,
e não como uma consequência direta da ação bimétrica + $\chi$ já
estabelecida — que, sozinha, produz apenas a forma sem $\eta$ (Anexo E
§E.3(1) / Anexo H §H.3(1)).
