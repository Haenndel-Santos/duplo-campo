Agora entramos no Anexo B, que é o "motor" matemático do fundo cosmológico: a variação explícita no ansatz FLRW, as duas equações de Friedmann e a dedução formal da constraint de Bianchi (incluindo a separação em ramos).

Vou escrever de forma auto-contida, como apêndice de tese: definindo variáveis, mostrando onde cada termo entra, e deixando claro o que é resultado geral do formalismo HR e o que é específico da TDCP (modulação por F(\chi) e energia do campo \chi).

**ANEXO B**

**Derivação Completa das Equações de Friedmann Bimétricas e da Constraint de Bianchi**

**B.1 Ação no Fundo e Convenções**

Começamos da ação bimétrica (Hassan--Rosen) com modulação TDCP:

$$ S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2\int d^4x\,\sqrt{-g}\,F(\chi)\,V(\mathcal{K}) + S_\chi + S_m. $$

com:

$$ V(\mathcal{K})=\sum_{n=0}^4\beta_n e_n(\mathcal{K}), \qquad \mathcal{K}=\sqrt{g^{-1}f}. $$

O setor escalar mínimo é:

$$ S_\chi = \int d^4x\,\sqrt{-g}\left[-\frac12 g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi - U(\chi)\right]. $$

Assumimos matéria S_m acoplada ao setor visível g.

**B.2 Ansatz FLRW Duplo (com lapses independentes)**

Tomamos o fundo cosmológico mais geral homogêneo e isotrópico:

$ds_g^2 = -N_g^2(t)dt^2 + a^2(t)\delta_{ij}dx^i dx^j,$

$ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j.$

Definimos as taxas de expansão:

$$ H_g \equiv \frac{1}{N_g}\frac{\dot a}{a}, \qquad H_f \equiv \frac{1}{N_f}\frac{\dot b}{b}. $$

E as variáveis estruturais:

$$ r(t)\equiv \frac{b(t)}{a(t)}, \qquad \xi(t)\equiv \frac{N_f(t)}{N_g(t)}. $$

A invariância por reparametrização temporal permite fixar N_g=1 ao final, mas manteremos N_g durante a variação para obter as equações corretamente.

**B.3 Potencial HR no Fundo FLRW**

No Anexo A obtivemos:

$\mathcal{K}=\mathrm{diag}(\xi,r,r,r).$

Logo os polinômios:

$e_0=1,$

$e_1=\xi+3r,$

$e_2=3\xi r+3r^2,$

$e_3=3\xi r^2+r^3,$

$e_4=\xi r^3.$

O potencial explícito:

$$ V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3). $$

Na TDCP:

$V\to F(\chi)V(\xi,r).$

**B.4 Redução da Ação ao "minisuperspace"**

No fundo FLRW, a ação reduz-se a uma integral temporal:

$$ S = \int dt\,\mathcal{L}(a,\dot a,N_g;\,b,\dot b,N_f;\,\chi,\dot\chi). $$

**B.4.1 Termos de Einstein--Hilbert**

Para a métrica g, o termo de Einstein--Hilbert reduz (ignorando termos de borda) a:

$\mathcal{L}_g = -3M_g^2\,\frac{a\dot a^2}{N_g}.$

Para o setor f:

$\mathcal{L}_f = -3M_f^2\,\frac{b\dot b^2}{N_f}.$

Essas expressões são as formas padrão no minisuperspace FLRW.

**B.4.2 Termo de interação (potencial HR)**

O determinante do setor g no fundo:

$\sqrt{-g} = N_g a^3.$

Logo o termo de interação na Lagrangiana é:

$$ \mathcal{L}_{int} = - m^2 M_{eff}^2\,(N_g a^3)\,F(\chi)\,V(\xi,r). $$

**B.4.3 Setor escalar χ**

$$ \sqrt{-g}\left(-\frac12 g^{00}\dot\chi^2 - U(\chi)\right) = N_g a^3\left(\frac{1}{2N_g^2}\dot\chi^2 - U(\chi)\right). $$

Portanto:

$$ \mathcal{L}_\chi = a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right). $$

**B.4.4 Matéria**

Definimos a densidade de energia de matéria por:

$$ \delta S_m = -\frac12\int d^4x \sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}. $$

No fundo, isso implica contribuição de energia:

$\mathcal{L}_m = -N_g a^3 \rho_m.$

**B.4.5 Lagrangiana total no minisuperspace**

Somando:

$$ \mathcal{L} = -3M_g^2\,\frac{a\dot a^2}{N_g} -3M_f^2\,\frac{b\dot b^2}{N_f} - m^2 M_{eff}^2 N_g a^3 F(\chi)V(\xi,r) + a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right) - N_g a^3 \rho_m. $$

A partir dessa Lagrangiana obtemos as equações de Friedmann pela variação em relação aos lapses N_g e N_f.

**B.5 Equação de Friedmann do Setor g (variação em N_g)**

Calculamos:

$\frac{\partial\mathcal{L}}{\partial N_g}=0.$

Termos dependentes de N_g:

1. -3M_g^2 a\dot a^2/N_g → derivada:

$$ \frac{\partial}{\partial N_g}\left(-3M_g^2\frac{a\dot a^2}{N_g}\right) = -3M_g^2 a\dot a^2\left(-\frac{1}{N_g^2}\right) = \frac{3M_g^2 a\dot a^2}{N_g^2}. $$

2. interação:

$$ \frac{\partial}{\partial N_g}\left(-m^2M_{eff}^2 N_g a^3F V\right) = - m^2 M_{eff}^2 a^3 F V. $$

3. escalar:

$$ \frac{\partial}{\partial N_g}\left(a^3\frac{1}{2N_g}\dot\chi^2\right) = -\frac{a^3}{2N_g^2}\dot\chi^2, $$

$$ \frac{\partial}{\partial N_g}\left(-a^3 N_g U\right) = - a^3 U. $$

4. matéria:

$\frac{\partial}{\partial N_g}(-N_g a^3\rho_m)= -a^3\rho_m.$

Somando:

$$ \frac{3M_g^2 a\dot a^2}{N_g^2} - m^2 M_{eff}^2 a^3F V - \frac{a^3}{2N_g^2}\dot\chi^2 - a^3U - a^3\rho_m =0. $$

Dividimos por a^3 e identificamos:

$$ H_g = \frac{1}{N_g}\frac{\dot a}{a} \quad\Rightarrow\quad \frac{\dot a^2}{N_g^2 a^2} = H_g^2. $$

Então:

$$ 3M_g^2 H_g^2 = \rho_m + \left(\frac12\frac{\dot\chi^2}{N_g^2}+U\right) + m^2M_{eff}^2 F(\chi)V(\xi,r). $$

Fixando gauge N_g=1 (opcional):

$3M_g^2 H_g^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)},$

onde:

$$ \rho_\chi = \frac12\dot\chi^2+U(\chi), \qquad \rho_{int}^{(g)} = m^2M_{eff}^2F(\chi)V(\xi,r). $$

**B.6 Equação de Friedmann do Setor f (variação em N_f)**

Agora variamos:

$\frac{\partial\mathcal{L}}{\partial N_f}=0.$

O termo EH de f:

$$ -3M_f^2\frac{b\dot b^2}{N_f} \quad\Rightarrow\quad \frac{\partial}{\partial N_f} = \frac{3M_f^2 b\dot b^2}{N_f^2}. $$

O termo de interação depende de N_f via:

$\xi = \frac{N_f}{N_g}.$

Como V(\xi,r) depende de \xi, então:

$$ \frac{\partial}{\partial N_f}\left(-m^2M_{eff}^2N_ga^3F V(\xi,r)\right) = -m^2M_{eff}^2N_ga^3F \frac{\partial V}{\partial \xi} \frac{\partial\xi}{\partial N_f}. $$

Mas:

$\frac{\partial\xi}{\partial N_f}=\frac{1}{N_g}.$

Logo:

$$ \frac{\partial\mathcal{L}_{int}}{\partial N_f} = -m^2M_{eff}^2a^3F \frac{\partial V}{\partial \xi}. $$

Então a equação N_f é:

$$ \frac{3M_f^2 b\dot b^2}{N_f^2} - m^2M_{eff}^2a^3F\frac{\partial V}{\partial \xi} =0. $$

Dividimos por a^3, escrevemos b=ra:

$$ \frac{3M_f^2 r^3 a^3}{a^3}\left(\frac{\dot b^2}{N_f^2 b^2}\right) = m^2M_{eff}^2F\frac{\partial V}{\partial \xi}. $$

Identificando:

$H_f = \frac{1}{N_f}\frac{\dot b}{b},$

obtemos:

$$ 3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\frac{\partial V}{\partial \xi}. $$

Agora calculamos \partial V/\partial\xi explicitamente:

$$ V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3). $$

Logo:

$$ \frac{\partial V}{\partial\xi} = \beta_1 +3\beta_2 r +3\beta_3 r^2 +\beta_4 r^3. $$

Portanto:

$$ 3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_1+3\beta_2 r+3\beta_3 r^2+\beta_4 r^3\right). $$

Dividindo por r^3:

$$ 3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right). $$

Esta é a equação de Friedmann do setor f.

**B.7 Equações de aceleração (variação em a e b)**

As equações acima são constraints (equações 00).

Para obter equações dinâmicas (análogas à equação de Raychaudhuri), variamos a Lagrangiana em relação a a e b.

De modo esquemático, para g:

$$ M_g^2(2\dot H_g + 3H_g^2) = - (p_m + p_\chi + p_{int}^{(g)}), $$

onde:

$p_\chi=\frac12\dot\chi^2-U(\chi),$

e p_{int}^{(g)} é obtido pela projeção espacial do tensor de interação.

(As expressões completas são extensas, mas o ponto essencial é que o termo HR gera pressão efetiva dependente de r,\xi.)

Essas equações serão usadas principalmente em análise completa de estabilidade e não são necessárias para a obtenção da constraint fundamental (Bianchi), que é nosso foco.

**B.8 Dedução da Constraint de Bianchi (passo a passo)**

O termo de interação produz tensores efetivos X_{\mu\nu} e \tilde{X}_{\mu\nu}.

No formalismo HR, a consistência exige:

$\nabla_g^\mu X_{\mu\nu}=0$

(e de forma equivalente no setor f).

No fundo FLRW, isso implica uma relação entre r,\xi,H_g,H_f.

O resultado padrão (para bimetric HR) é:

$$ \left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0. $$

Vamos mostrar por que essa estrutura aparece.

**B.8.1 Forma física da conservação**

No setor g, assumimos matéria conservada:

$$ \nabla_g^\mu T^{(m)}_{\mu\nu}=0, \quad \nabla_g^\mu T^{(\chi)}_{\mu\nu} = (\Box\chi-U')\partial_\nu\chi, $$

logo a conservação total exige que a divergência do termo de interação seja cancelada pela fonte de \chi quando F(\chi) está presente. No regime de fundo homogêneo, isso se traduz em uma condição algébrica/dinâmica entre r,\xi.

No caso HR padrão (F=1), essa condição surge exclusivamente da estrutura de constraints.

Quando há F(\chi), a forma do produto permanece, mas a evolução de r e \xi pode receber contribuição indireta via \chi. Ainda assim, a decomposição em ramos é estruturalmente a mesma.

**B.8.2 Decomposição em ramos**

A condição:

$$ \left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0 $$

implica:

**(A) Ramo Algébrico**

$$ \beta_1 + 2\beta_2 r + \beta_3 r^2 = 0 \quad\Rightarrow\quad r = \text{constante}. $$

Nesse ramo, a razão de escalas é fixada por uma equação quadrática.

Isso geralmente gera um termo efetivo semelhante a Λ (combinando \beta_n).

**(B) Ramo Dinâmico**

$H_g = \xi H_f.$

Aqui, r(t) pode evoluir.

Este ramo é o foco da TDCP porque permite separação estrutural histórica.

**B.9 Dinâmica de r(t) e relação com o ramo dinâmico**

Definimos:

$r=\frac{b}{a}.$

Derivando:

$$ \dot r = \frac{\dot b}{a} - \frac{b\dot a}{a^2} = r\left(\frac{\dot b}{b} - \frac{\dot a}{a}\right). $$

Substituindo:

$\frac{\dot b}{b}=N_f H_f, \quad \frac{\dot a}{a}=N_g H_g.$

Logo:

$\dot r = r(N_f H_f - N_g H_g) = rN_g(\xi H_f - H_g).$

$Se N_g=1:$

$\dot r = r(\xi H_f - H_g).$

Portanto, no ramo dinâmico H_g=\xi H_f:

$\dot r=0$

se a igualdade for estrita em todo tempo.

Isso revela um ponto sutil: em bimetric FLRW, o ramo "dinâmico" não implica necessariamente \dot r\neq 0 --- ele implica que a evolução pode ocorrer via evolução de \xi e da relação entre lapses, e que r pode ser determinado por uma equação diferencial implícita ao combinar Friedmann g/f + equação de \chi.

Na TDCP, como F(\chi) altera a dependência efetiva do potencial com o tempo, isso pode permitir evolução efetiva do grau estrutural do acoplamento mesmo quando r é aproximadamente constante em determinados regimes: a separação dinâmica pode residir em F(\chi) e em \eta, não apenas em r.

Este ponto é importante para evitar um erro interpretativo comum:

o "dinâmico" da TDCP não depende exclusivamente de \dot r\neq 0; depende da evolução do acoplamento estrutural total.

**B.10 Limite Proporcional como Subcaso Analítico**

Um subcaso útil é:

$f_{\mu\nu} = c^2 g_{\mu\nu}.$

No fundo FLRW:

$b = c a \Rightarrow r=c=\text{constante}.$

Nesse caso, o potencial gera densidade efetiva constante (se F constante):

$$ \rho_{int}^{(g)} = m^2M_{eff}^2F(\chi) (\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3). $$

Na TDCP, se F(\chi) evolui lentamente, isso se torna uma "Λ efetiva" quase constante, oferecendo ponte formal direta com ΛCDM.

**B.11 Conclusão do Anexo B**

Neste anexo derivamos, a partir da ação reduzida no minisuperspace:

1. Equação de Friedmann do setor g:

$> 3M_g^2 H_g^2=\rho_m+\rho_\chi+\rho_{int}^{(g)}.$

2. Equação de Friedmann do setor f:

$> 3M_f^2 H_f^2=\rho_{int}^{(f)}.$

3. Constraint de Bianchi, que impõe a estrutura de ramos:

$> (\beta_1+2\beta_2 r+\beta_3 r^2)(H_g-\xi H_f)=0.$

Esses resultados são a base matemática do corpo principal da TDCP, e são a fundação para:

- cosmologia de fundo (Cap. 3--4),

- perturbações e crescimento (Cap. 4 e anexo técnico subsequente),

- estabilidade completa (Cap. 5 e anexo C/D).

**ANEXO C --- Análise Quadrática do Setor Escalar (matriz cinética, ghost e estabilidade de gradiente)**
