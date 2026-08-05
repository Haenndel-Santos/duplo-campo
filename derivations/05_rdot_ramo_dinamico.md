# Derivação 5 — ṙ no Ramo Dinâmico

**Skill invocado:** `tdcp-f1-parameter-guardian`.

**Nota de numeração:** o PROMPT 2 cita "Cap.13 §13.11" usando a numeração
*anterior* à renumeração da Tarefa 2d (Prompt 1). No estado atual do
corpo (`manuscript/`), esse conteúdo está em **Cap.14, §14.11–14.14**
(`manuscript/capitulos/Cap.14.md`). Todas as citações abaixo usam a
numeração atual.

## 1. O que está sendo derivado e por que é necessário

O Cap.14, ao tratar do "ramo dinâmico" da constraint de Bianchi
bimétrica, apresenta **duas derivações diferentes** de ṙ(t) a partir da
mesma condição de ramo, chegando a resultados incompatíveis:

- §14.11 deriva $\dot r = 0$ diretamente da condição de ramo $H_g=\xi H_f$.
- §14.12 declara, sem justificar a mudança, uma condição de ramo
  *diferente* ($H_b=\xi H_g$, com $H_b\equiv \dot b/b$) e obtém
  $\dot r = r(\xi-1)H_g \neq 0$.

Isso é uma inconsistência interna real: ou $\dot r=0$ ou $\dot r\neq 0$
não podem ser ambos "o" resultado do mesmo ramo. Esta derivação refaz o
cálculo do zero, sem atalhos, para determinar qual (se algum) está
correto, e o que é preciso assumir para que a teoria tenha, de fato, um
"ramo dinâmico" no sentido de $r(t)$ evoluindo no tempo.

## 2. Ponto de partida

Do Cap.5 (§5.5) e do Cap.14 (§14.12), a constraint de Bianchi bimétrica
no fundo FLRW é:

$$ (\beta_1+2\beta_2 r+\beta_3 r^2)\,(H_g-\xi H_f)=0, $$

com as definições padrão (Cap.5 §5.3, Cap.14 §14.11):

$$ H_g \equiv \frac{1}{N_g}\frac{\dot a}{a}, \qquad H_f \equiv \frac{1}{N_f}\frac{\dot b}{b}, \qquad \xi \equiv \frac{N_f}{N_g}, \qquad r\equiv\frac{b}{a}. $$

Essa constraint define dois ramos possíveis:

- **Ramo algébrico:** $\beta_1+2\beta_2 r+\beta_3 r^2=0$, isto é,
  $r=r_\star$ é uma raiz fixa do polinômio (para F1, $\beta_3=0$, então
  $r_\star=-\beta_1/(2\beta_2)$, exigindo $\beta_1\beta_2<0$ — Cap.13
  §13.5, consistente com `tdcp-f1-parameter-guardian`).
- **Ramo dinâmico:** o outro fator, $H_g=\xi H_f$, é anulado em vez do
  polinômio.

O objetivo é obter $\dot r(t)$ **apenas** a partir de $H_g=\xi H_f$, sem
introduzir nenhuma condição adicional não declarada.

## 3. Derivação completa

### 3.1 Substituindo as definições

$$ H_g=\xi H_f \;\;\Longleftrightarrow\;\; \frac{1}{N_g}\frac{\dot a}{a} = \frac{N_f}{N_g}\cdot\frac{1}{N_f}\frac{\dot b}{b}. $$

O fator $N_f$ no lado direito **cancela exatamente** contra o $N_f$ que
aparece dentro de $H_f$ (isso já está implícito na própria definição
$\xi\equiv N_f/N_g$ multiplicando $H_f\equiv \dot b/(N_f b)$):

$$ \frac{1}{N_g}\frac{\dot a}{a} = \frac{1}{N_g}\frac{\dot b}{b}. $$

Em seguida, o fator $N_g$ (que é comum aos dois lados, qualquer que seja
o gauge/lapse escolhido) também cancela:

$$ \frac{\dot a}{a} = \frac{\dot b}{b}. $$

Esse cancelamento duplo (de $N_f$ e de $N_g$) foi verificado
simbolicamente com `sympy` (ver `derivations/code/05_rdot_check.py`),
tratando $a(t),b(t),N_g(t),N_f(t)$ como funções independentes genéricas:
o resultado $H_g-\xi H_f \propto (\dot a/a-\dot b/b)$, com constante de
proporcionalidade exatamente $1/N_g$, **sem nenhum resíduo dependente de
$N_f$**.

### 3.2 De volta a r(t)

Com $r\equiv b/a$:

$$ \frac{\dot r}{r} = \frac{d}{dt}\ln r = \frac{d}{dt}\ln b - \frac{d}{dt}\ln a = \frac{\dot b}{b}-\frac{\dot a}{a}. $$

Da seção 3.1, $\dot a/a=\dot b/b$ no ramo dinâmico, logo:

$$ \frac{\dot r}{r} = 0 \quad\Longrightarrow\quad \boxed{\dot r = 0.} $$

Este é **exatamente** o resultado de §14.11 — e a álgebra acima mostra
que ele é **inevitável**: não depende de gauge ($N_g$ arbitrário, não
precisa ser fixado a 1), não depende de $\xi(t)$ ter alguma forma
particular, e não depende de haver matéria em nenhum dos dois setores.
$H_g=\xi H_f$ **é**, literalmente, a afirmação $\dot a/a=\dot b/b$
reescrita — e essa é exatamente a afirmação $\dot r=0$.

### 3.3 Onde a derivação de §14.12 diverge (e por quê está errada)

§14.12 define $H_b\equiv \dot b/b$ (Hubble de $b$ em *tempo coordenado*,
sem dividir por $N_f$ — uma quantidade auxiliar legítima) e então afirma
que a condição de ramo dinâmico é:

$$ H_b = \xi H_g \qquad \text{(forma usada em §14.12)}. $$

Usando a relação de definição $H_f=H_b/\xi$ (que decorre trivialmente de
$H_b\equiv \dot b/b$ e $H_f\equiv \dot b/(N_f b)=\dot b/(\xi N_g b)$ — e
com $N_g=1$ no gauge escolhido, $H_f=H_b/\xi$), a condição *original* e
correta $H_g=\xi H_f$ (§14.11) se traduz em:

$$ H_g = \xi\cdot\frac{H_b}{\xi} = H_b, $$

ou seja, **$H_g=H_b$** — não $H_b=\xi H_g$. As duas condições
($H_g=H_b$ vs. $H_b=\xi H_g$) só coincidem se $\xi=1$; para $\xi\neq1$
são condições **diferentes e mutuamente incompatíveis** (exceto no ponto
trivial $H_g=H_b=0$). §14.12 não deriva $H_b=\xi H_g$ de nenhum
princípio — ela aparece como uma reafirmação da constraint original
"trocando" qual variável ($H_f$ ou $H_b$) é multiplicada por $\xi$, sem
justificar a troca. Essa é a origem exata da inconsistência: **duas
formas não-equivalentes da "mesma" condição de ramo, usadas em
sequência**, produzindo dois resultados incompatíveis.

## 4. Resultado final em forma fechada

$$ \boxed{\text{No ramo dinâmico } (H_g=\xi H_f) \text{ da constraint de Bianchi bimétrica FLRW}, \quad \dot r \equiv 0 \text{ identicamente.}} $$

Isto é: **com o ansatz FLRW diagonal homogêneo padrão (Cap.5), usado sem
modificação em todo o corpo principal, nenhum dos dois ramos da
constraint de Bianchi permite $r(t)$ genuinamente variável.** No ramo
algébrico, $r=r_\star$ é fixado pelas raízes do polinômio em $\beta_n$;
no ramo dito "dinâmico", $r=r_{\text{livre}}$ é uma constante de
integração **não fixada pelo potencial**, mas ainda assim uma constante
no tempo. A diferença entre os dois ramos é *o que fixa o valor de r*
(o potencial vs. as condições iniciais), não *se r evolui*.

### 4.1 Consequência necessária: como o texto pode obter $r(t)$ genuinamente evolutivo

Se a intenção do autor é que $r(t)$ evolua de fato (o que o Cap.13 §13.6
e o Cap.14 chamam de "memória estrutural"), a única via consistente
dentro do formalismo já estabelecido é tornar os $\beta_n$ dependentes de
$\phi$ (já introduzido em outros pontos como $\beta_n\to\beta_n(\phi)$ ou
$V\to F(\phi)V$ — Cap.3 §3.8, Cap.13 §13.1). Nesse caso, o ramo
"algébrico" deixa de ser estático:

$$ \beta_1(\phi)+2\beta_2(\phi)\,r+\beta_3(\phi)\,r^2=0 \quad\Longrightarrow\quad r_\star(t) = r_\star\big(\phi(t)\big), $$

uma raiz que **muda lentamente no tempo conforme $\phi(t)$ evolui**
(desde que a condição de adiabaticidade $|\dot\beta_n/\beta_n|\ll H$ já
exigida no Cap.6.2 §6.10 seja respeitada, para que $r(t)$ acompanhe
$r_\star(\phi(t))$ quase estaticamente, sem introduzir uma nova
instabilidade dinâmica). Essa é uma extensão consistente, mas é
**diferente do "ramo dinâmico" da constraint de Bianchi** propriamente
dita — é, na verdade, um "ramo algébrico com raiz móvel", e deveria ser
nomeado e tratado como tal, não confundido com o segundo fator da
constraint de Bianchi.

## 5. Classificação final

**DERIVADO.** O resultado $\dot r=0$ no ramo dinâmico (como literalmente
definido pela constraint de Bianchi $H_g=\xi H_f$) é obtido por álgebra
direta, sem hipóteses adicionais, e foi verificado simbolicamente
(`derivations/code/05_rdot_check.py`). A afirmação alternativa do Cap.14
§14.12 ($\dot r=r(\xi-1)H_g$) não é derivável da mesma constraint sem
substituir, sem justificativa, a condição de ramo por uma segunda
condição não-equivalente — portanto **não deve ser mantida como está**.

A evolução genuína de $r(t)$ que o corpo principal narrativamente
pressupõe (Cap.5, Cap.13, Cap.14) requer a hipótese adicional de
$\beta_n(\phi)$ com raiz móvel $r_\star(\phi(t))$ no ramo algébrico —
esse resultado é **DERIVADO SOB HIPÓTESE ADICIONAL** ($\beta_n(\phi)$ +
adiabaticidade), não uma propriedade do "ramo dinâmico" per se.
