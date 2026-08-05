# Derivação 3 — ∂V(ξ,r)/∂N_g com Regra da Cadeia Completa

**Skill invocado:** `bimetric-hr-formalism-guardian`.

## 1. O que está sendo derivado e por que é necessário

O Anexo B, ao variar a ação minisuperespaço em relação ao lapso $N_g$
para obter a equação de Friedmann do setor $g$ (§B.5), escreve a
derivada do termo de potencial como:

$$ \frac{\partial}{\partial N_g}\Big(-m^2M_{eff}^2\,N_g\,a^3\,F(\chi)\,V(\xi,r)\Big) = -m^2M_{eff}^2\,a^3\,F(\chi)\,V(\xi,r), $$

isto é, trata $V(\xi,r)$ como se não dependesse de $N_g$. Mas
$\xi\equiv N_f/N_g$ **depende explicitamente de $N_g$** — essa
dependência é omitida. O próprio Anexo B, ao variar em relação a $N_f$
na seção seguinte (§B.6), aplica a regra da cadeia corretamente
(via $\partial\xi/\partial N_f=1/N_g$) e obtém um resultado que **retém
$\beta_4$**. O resultado do setor $g$ (§B.5), citado de forma simbólica
como $\rho_{int}^{(g)}=m^2M_{eff}^2F(\chi)V(\xi,r)$, ao ser expandido
com a forma completa de $V(\xi,r)$, também retém $\xi$ e $\beta_4$.

Isso conflita diretamente com o Anexo A §A.8, usado em todo o corpo
principal (Cap.5, Cap.13/Cap.14, etc.), que dá:

$$ \rho_{int}^{(g)} = m^2M_{eff}^2\,(\beta_0+3\beta_1 r+3\beta_2 r^2+\beta_3 r^3), $$

**sem** $\xi$ e **sem** $\beta_4$. Esta derivação refaz §B.5 com a regra
da cadeia completa para determinar qual forma (se alguma) é a correta, e
reconcilia as duas.

## 2. Ponto de partida

Do Anexo B §B.4.5, o termo de potencial na Lagrangiana minisuperespaço é:

$$ \mathcal{L}_V \equiv -m^2M_{eff}^2\,N_g\,a^3\,F(\chi)\,V(\xi,r), $$

com (Anexo A §A.2, Anexo B §B.3, família F1 com $\beta_3=0$ no corpo
principal, mas mantido aqui por generalidade algébrica):

$$ V(\xi,r) = \beta_0+\beta_1(\xi+3r)+\beta_2(3\xi r+3r^2)+\beta_3(3\xi r^2+r^3)+\beta_4\,\xi r^3, $$

$$ \xi \equiv \frac{N_f}{N_g}, \qquad r\equiv\frac{b}{a}. $$

Na variação ADM padrão (usada consistentemente em §B.5 e §B.6), $N_g$ e
$N_f$ são lapses **independentes**: ao variar em relação a $N_g$,
mantêm-se $N_f, a, b, \chi$ (e suas derivadas temporais) fixos — logo
$r$ é tratado como constante nesta variação, mas $\xi=N_f/N_g$
**não é**, pois contém $N_g$ explicitamente no denominador.

## 3. Derivação completa

### 3.1 A regra da cadeia que falta

$$ \frac{\partial \mathcal{L}_V}{\partial N_g} = -m^2M_{eff}^2 a^3 F(\chi)\left[\underbrace{V(\xi,r)}_{\text{do fator explícito } N_g} \;+\; N_g\cdot\frac{\partial V}{\partial \xi}\cdot\frac{\partial \xi}{\partial N_g}\right]. $$

Calculando $\partial\xi/\partial N_g$ explicitamente:

$$ \frac{\partial \xi}{\partial N_g} = \frac{\partial}{\partial N_g}\left(\frac{N_f}{N_g}\right) = -\frac{N_f}{N_g^2} = -\frac{\xi}{N_g}. $$

Substituindo:

$$ N_g\cdot\frac{\partial V}{\partial \xi}\cdot\left(-\frac{\xi}{N_g}\right) = -\xi\,\frac{\partial V}{\partial \xi}, $$

logo:

$$ \frac{\partial \mathcal{L}_V}{\partial N_g} = -m^2M_{eff}^2 a^3 F(\chi)\left[V(\xi,r) - \xi\,\frac{\partial V}{\partial \xi}\right]. $$

Esse é exatamente o termo "$-\xi\partial V/\partial\xi$" ausente em
§B.5: a versão citada no Anexo B mantém apenas $V(\xi,r)$, equivalente a
assumir $\partial\xi/\partial N_g=0$, o que é falso.

### 3.2 Calculando $\partial V/\partial \xi$ e a combinação completa

$$ \frac{\partial V}{\partial \xi} = \beta_1+3\beta_2 r+3\beta_3 r^2+\beta_4 r^3. $$

$$ V(\xi,r)-\xi\frac{\partial V}{\partial\xi} = \Big[\beta_0+\beta_1(\xi+3r)+\beta_2(3\xi r+3r^2)+\beta_3(3\xi r^2+r^3)+\beta_4\xi r^3\Big] - \xi\Big[\beta_1+3\beta_2 r+3\beta_3 r^2+\beta_4 r^3\Big]. $$

Todos os termos proporcionais a $\xi$ cancelam **exatamente**:
$\beta_1\xi-\xi\beta_1=0$; $3\beta_2 r\xi-3\beta_2 r\xi=0$; $3\beta_3
r^2\xi-3\beta_3r^2\xi=0$; $\beta_4 r^3\xi-\xi\beta_4r^3=0$. Sobra:

$$ V(\xi,r)-\xi\frac{\partial V}{\partial\xi} = \beta_0+3\beta_1 r+3\beta_2 r^2+\beta_3 r^3. $$

Esse cancelamento foi verificado simbolicamente com `sympy`
(`derivations/code/03_dV_dNg_check.py`), tratando
$\beta_0,\dots,\beta_4,\xi,r$ como símbolos livres — a identidade vale
para qualquer família de parâmetros $\beta_n$, não é peculiar da F1.

### 3.3 Reconstituindo $\rho_{int}^{(g)}$ com o sinal e normalização já usados na fonte

O próprio §B.5 usa a convenção
$\rho_{int}^{(g)} = -\big[\partial\mathcal{L}_V/\partial N_g\big]/a^3$
(visível ao comparar sua derivada incompleta,
$\partial\mathcal L_V/\partial N_g=-m^2M_{eff}^2a^3F(\chi)V(\xi,r)$, com
seu próprio resultado final citado,
$\rho_{int}^{(g)}=+m^2M_{eff}^2F(\chi)V(\xi,r)$). Aplicando essa mesma
convenção à derivada **completa** da seção 3.1:

$$ \rho_{int}^{(g)} = -\frac{1}{a^3}\frac{\partial\mathcal L_V}{\partial N_g} = m^2M_{eff}^2 F(\chi)\Big[V(\xi,r)-\xi\frac{\partial V}{\partial\xi}\Big] = m^2M_{eff}^2 F(\chi)\big(\beta_0+3\beta_1 r+3\beta_2 r^2+\beta_3 r^3\big). $$

### 3.4 Verificação cruzada independente com o setor f (§B.6)

Como checagem adicional (não estritamente necessária, mas útil como
teste de consistência da própria mecânica de regra da cadeia usada
acima), a mesma $\partial V/\partial\xi$ calculada em 3.2 aparece também
no setor $f$. O Anexo B §B.6 (variação em $N_f$, já correta na fonte)
obtém:

$$ 3M_f^2H_f^2 = m^2M_{eff}^2F(\chi)\Big(\beta_4+3\beta_3 r^{-1}+3\beta_2r^{-2}+\beta_1r^{-3}\Big). $$

Dividir $\partial V/\partial\xi$ por $r^3$ (fator de normalização de
volume entre os dois setores, já que o volume próprio do setor $f$ é
$b^3=r^3a^3$) reproduz exatamente esse mesmo parêntese:

$$ \frac{1}{r^3}\frac{\partial V}{\partial\xi} = \beta_4+3\beta_3r^{-1}+3\beta_2r^{-2}+\beta_1r^{-3}. $$

Confirmado por `sympy` no mesmo script. Isso mostra que a mecânica de
regra da cadeia usada na seção 3.1 é exatamente a mesma que já produz,
sem modificação, o resultado do setor $f$ que a própria fonte já dá como
correto — reforçando que a assimetria entre os dois setores (setor $g$
sem $\beta_4$, setor $f$ com $\beta_4$) é uma consequência genuína da
regra da cadeia, não um erro de contas independente em cada seção.

## 4. Resultado final em forma fechada

$$ \boxed{\rho_{int}^{(g)} = m^2M_{eff}^2\,F(\chi)\,\big(\beta_0+3\beta_1 r+3\beta_2 r^2+\beta_3 r^3\big)} $$

## 5. Reconciliação explícita das "duas formas conflitantes"

- **Anexo A §A.8** ($\rho_{int}^{(g)}=m^2M_{eff}^2(\beta_0+3\beta_1
  r+3\beta_2 r^2+\beta_3 r^3)$, sem $F(\chi)$, sem $\xi$, sem $\beta_4$):
  **está algebricamente correta** na sua estrutura em $\beta_n$ e $r$ —
  é exatamente o que a regra da cadeia completa produz (seção 3.3). A
  única lacuna do Anexo A é não mostrar explicitamente o fator $F(\chi)$
  (que pertence à modulação escalar introduzida depois, no Cap.3
  §3.8/Cap.13 §13.1, e incorporada na Lagrangiana minisuperespaço do
  Anexo B §B.4.5) — não é um erro, é uma omissão de um fator que, nas
  seções originais do Anexo A, ainda não fazia parte do formalismo.

- **Anexo B §B.5** (citado como $\rho_{int}^{(g)}=m^2M_{eff}^2F(\chi)
  V(\xi,r)$, retendo $\xi$ e $\beta_4$ se expandido): **é o resultado de
  uma derivada incompleta**, que omite o termo $-\xi\,\partial
  V/\partial\xi$ vindo da dependência $\xi=\xi(N_g)$. Corrigindo a
  derivada (seção 3.1–3.3), o termo em $\beta_4$ e toda a dependência em
  $\xi$ cancelam **exatamente**, e o resultado colapsa para a forma do
  Anexo A (mais o fator $F(\chi)$, que estava correto em §B.5 e é
  preservado).

**Não há, portanto, duas físicas diferentes competindo** — há uma
derivação completa (Anexo A, na sua estrutura em $\beta_n$) e uma
derivação com um passo de cálculo faltando (Anexo B §B.5, no seu
resultado citado). Uma vez corrigida, a "segunda forma" deixa de existir
como resultado independente: ela **é** a primeira forma, com $F(\chi)$
multiplicando. $\beta_4$ não desaparece da teoria — ele permanece
inteiramente no setor $f$ (§B.6, já correto), que é onde a assimetria
estrutural do potencial bimétrico HR o coloca.

## 6. Classificação final

**DERIVADO.** A regra da cadeia completa
($\partial\xi/\partial N_g=-\xi/N_g$) foi aplicada por álgebra direta,
sem hipóteses adicionais, e o cancelamento de $\beta_4$ e de $\xi$ foi
verificado simbolicamente (`derivations/code/03_dV_dNg_check.py`),
incluindo uma checagem cruzada independente contra o resultado (já
correto) do setor $f$ em §B.6. O resultado citado em Anexo B §B.5
($\rho_{int}^{(g)}=m^2M_{eff}^2F(\chi)V(\xi,r)$, com $\xi$ e $\beta_4$
retidos) **não deve ser mantido como está** — deve ser substituído pela
forma em caixa da seção 4, que coincide com o Anexo A §A.8 mais o fator
$F(\chi)$.
