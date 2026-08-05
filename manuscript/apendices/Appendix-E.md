Perfeito. Vamos para o Anexo E, que é essencial como "manual operacional" da TDCP: ele transforma o formalismo em um sistema dinâmico fechado pronto para integração numérica (mesmo que você não vá rodar agora).

Vou construir este anexo com:

- conjunto de equações ODE completo,

- escolha de variáveis adimensionais,

- normalizações cosmológicas padrão,

- fechamento do sistema (quantas equações, quantas incógnitas),

- estratégia de integração e checagens internas,

- como extrair H(z), w_{\text{eff}}(z), G_{\text{eff}}(k,z) etc.

**ANEXO E**

**Sistema Dinâmico Completo para Simulação Numérica da TDCP**

**E.1 Por que um "sistema dinâmico" é necessário?**

O corpo principal e os anexos A--D fornecem:

- ação,

- equações de fundo,

- estrutura de perturbações,

- condições de estabilidade.

Mas, para confrontar com dados ou explorar regiões do espaço de parâmetros, precisamos:

de um conjunto mínimo de equações diferenciais fechadas.

Em cosmologia, isso sempre implica escolher:

- variáveis adimensionais,

- um parâmetro de tempo conveniente (geralmente N=\ln a),

- e um conjunto de equações de primeira ordem.

Este anexo constrói exatamente isso.

**E.2 Variáveis fundamentais do fundo**

A TDCP, no nível do fundo, envolve as funções:

- a(t) --- fator de escala observável,

- b(t) --- fator de escala do setor estrutural,

- N_f(t) --- lapse do setor f,

- \chi(t) --- campo estrutural,

- \rho_m(t) --- densidade de matéria (e radiação opcional),

- e a variável acumulada \eta(t).

Definimos:

$r(t)=\frac{b(t)}{a(t)}, \qquad \xi(t)=\frac{N_f(t)}{N_g(t)}.$

Escolhemos gauge cosmológico:

$N_g=1.$

Logo:

$$ H \equiv \frac{\dot a}{a}, \qquad H_f = \frac{1}{N_f}\frac{\dot b}{b} = \frac{1}{\xi}\frac{\dot b}{b}. $$

**E.3 Equações fundamentais (fundo)**

**(1) Friedmann do setor visível g**

$3M_g^2 H^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)}.$

com

$\rho_\chi = \frac12\dot\chi^2 + U(\chi),$

$$ \rho_{int}^{(g)} = m^2M_{eff}^2 F(\chi) \left(\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3\right). $$

**(2) Friedmann do setor estrutural f**

$3M_f^2 H_f^2 = \rho_{int}^{(f)},$

com

$$ \rho_{int}^{(f)} = m^2M_{eff}^2 F(\chi) \left(\beta_4 + 3\beta_3 r^{-1} + 3\beta_2 r^{-2} + \beta_1 r^{-3}\right). $$

**(3) Equação de χ (com fonte do acoplamento)**

Forma geral:

$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,W(r,\xi), $$

onde W(r,\xi) representa a combinação efetiva que surge ao variar o termo F(\chi)V(\xi,r) em relação a χ.

Uma escolha natural, coerente com o fundo FLRW, é:

$W(r,\xi) = V(\xi,r)$

isto é,

$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,V(\xi,r). $$

(Em aplicações, usa-se a forma completa de V.)

**(4) Evolução de η**

$\dot\eta = \Gamma \dot\chi^2.$

**(5) Conservação de matéria**

Para matéria fria:

$$ \dot\rho_m + 3H\rho_m = 0 \quad\Rightarrow\quad \rho_m = \rho_{m0} a^{-3}. $$

(Para radiação: \rho_r\propto a^{-4}, se incluída.)

**(6) Constraint de Bianchi (ramos)**

$(\beta_1 + 2\beta_2 r + \beta_3 r^2)(H - \xi H_f)=0.$

Escolha TDCP principal: ramo dinâmico, isto é:

$H = \xi H_f.$

Esta equação é essencial para fechar o sistema, pois liga H, H_f e \xi.

**E.4 Fechamento do sistema: incógnitas e equações**

Queremos resolver para:

- H(t),

- $\chi(t),$

- $\dot\chi(t),$

- $\eta(t),$

- r(t) e/ou \xi(t) (dependendo do ramo),

- com \rho_m(a) conhecido.

No ramo dinâmico:

$H = \xi H_f \quad\Rightarrow\quad H_f = \frac{H}{\xi}.$

Mas a equação de Friedmann f envolve H_f explicitamente, logo fornece uma relação algébrica para \xi dado H,r,\chi.

**E.5 Forma adimensional: escolha de variável temporal N=\ln a**

Definimos:

$N\equiv \ln a, \qquad \frac{d}{dt} = H\frac{d}{dN}.$

Definimos as variáveis adimensionais:

$$ x \equiv \frac{\dot\chi}{\sqrt{6}M_g H}, \qquad y \equiv \frac{\sqrt{U(\chi)}}{\sqrt{3}M_g H}, \qquad \Omega_m \equiv \frac{\rho_m}{3M_g^2 H^2}. $$

E também:

$\Omega_{int} \equiv \frac{\rho_{int}^{(g)}}{3M_g^2 H^2}.$

Então a Friedmann g vira um constraint:

$1 = \Omega_m + x^2 + y^2 + \Omega_{int}.$

**E.6 Equações diferenciais em N**

**E.6.1 Evolução de χ**

$\frac{d\chi}{dN} = \frac{\dot\chi}{H} = \sqrt{6}M_g x.$

**E.6.2 Evolução de x**

Começamos de:

$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V(\xi,r). $$

Escrevemos \ddot\chi = H\frac{d\dot\chi}{dN}.

Como:

$\dot\chi = \sqrt{6}M_g H x,$

então:

$$ \ddot\chi = \sqrt{6}M_g\left(\dot H x + H\dot x\right) = \sqrt{6}M_g H^2\left(\frac{d x}{dN} + x\frac{d\ln H}{dN}\right). $$

Substituindo:

$$ \sqrt{6}M_g H^2\left(\frac{dx}{dN}+x\frac{d\ln H}{dN}\right) + 3H(\sqrt{6}M_g H x) + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V. $$

Dividindo por \sqrt{6}M_g H^2:

$$ \frac{dx}{dN}+x\frac{d\ln H}{dN}+3x + \frac{U'(\chi)}{\sqrt{6}M_g H^2} = \frac{m^2 M_{eff}^2}{\sqrt{6}M_g H^2}F'(\chi)V. $$

Definimos os parâmetros de "inclinação":

$$ \lambda(\chi) \equiv M_g\frac{U'(\chi)}{U(\chi)}, \qquad \Rightarrow \frac{U'}{H^2} = 3M_g^2 \lambda y^2. $$

Logo:

$\frac{U'}{\sqrt{6}M_g H^2} = \sqrt{\frac{3}{2}}\lambda y^2.$

Portanto:

$$ \boxed{ \frac{dx}{dN} = -3x - x\frac{d\ln H}{dN} - \sqrt{\frac{3}{2}}\lambda y^2 + \mathcal{S}(r,\xi,\chi)\frac{m^2}{H^2} } $$

onde

$$ \mathcal{S}(r,\xi,\chi)= \frac{ M_{eff}^2}{\sqrt{6}M_g}F'(\chi)V(\xi,r). $$

**E.6.3 Evolução de η**

$$ \dot\eta = \Gamma \dot\chi^2 \Rightarrow \frac{d\eta}{dN} = \frac{\dot\eta}{H} = \Gamma \frac{\dot\chi^2}{H}. $$

Como:

$\dot\chi^2 = 6M_g^2 H^2 x^2,$

então:

$\boxed{ \frac{d\eta}{dN} = 6\Gamma M_g^2 H x^2 }$

Em forma totalmente adimensional, absorve-se o fator dimensional definindo \tilde\Gamma = \Gamma M_g^2 H_0, mas deixamos aqui a forma geral.

**E.6.4 Evolução de \Omega_m**

$De \rho_m\propto a^{-3}:$

$\frac{d\ln\rho_m}{dN}=-3.$

Como:

$\Omega_m = \frac{\rho_m}{3M_g^2H^2},$

temos:

$\frac{d\ln\Omega_m}{dN} = -3 - 2\frac{d\ln H}{dN}.$

Logo:

$$ \boxed{ \frac{d\Omega_m}{dN} = \Omega_m\left(-3 -2\frac{d\ln H}{dN}\right). } $$

**E.7 Como obter d\ln H/dN**

Aqui está o "pulo do gato" do sistema.

No formalismo TDCP efetivo:

$H^2 = \frac{8\pi G}{3}\frac{\rho_{tot}}{1-\eta}.$

Tomando log:

\ln H^2 = \ln\rho_{tot} - \ln(1-\eta) + const.

Derivando em N:

$$ \frac{d\ln H^2}{dN} = \frac{d\ln\rho_{tot}}{dN} + \frac{1}{1-\eta}\frac{d\eta}{dN}. $$

Logo:

$$ \boxed{ \frac{d\ln H}{dN} = \frac12\frac{d\ln\rho_{tot}}{dN} + \frac{1}{2(1-\eta)}\frac{d\eta}{dN}. } $$

No regime onde \rho_{tot}\approx \rho_m + \rho_\chi + \rho_{int}, podemos calcular \frac{d\ln\rho_{tot}}{dN} a partir das equações de conservação e da dinâmica de \chi.

Em implementação numérica, é comum:

- usar a equação de aceleração (Raychaudhuri) derivada da variação em a,

- ou usar diretamente:

$$ w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN}, $$

e então:

$$ \frac{d\ln H}{dN} = -\frac32\left(1+w_{\text{eff}}\right)\left(1-\Omega_r\right)+\cdots $$

dependendo de quais componentes foram incluídos.

Aqui, como anexo, deixamos a estratégia geral:

Para rodar simulação, você escolhe ou (i) equação de aceleração explícita, ou (ii) fecha via expressão efetiva de w_{\text{eff}} + composição de densidades.

**E.8 Fechamento com o setor f: obtenção de \xi**

No ramo dinâmico:

$H=\xi H_f \Rightarrow H_f = \frac{H}{\xi}.$

A Friedmann f:

$$ 3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi) \left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right). $$

Substituindo H_f=H/\xi:

$$ 3M_f^2 \frac{H^2}{\xi^2} = m^2M_{eff}^2F(\chi)\,\mathcal{U}(r), $$

onde:

$$ \mathcal{U}(r)\equiv \beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}. $$

Logo obtemos \xi algebraicamente:

$$ \boxed{ \xi(N) = H\sqrt{\frac{3M_f^2}{m^2M_{eff}^2F(\chi)\mathcal{U}(r)}} } $$

(up to escolha de sinal físico).

Isso fecha a dependência de \xi sem necessidade de ODE separada.

**E.9 Dinâmica de r: escolha de parametrização**

Como:

$$ r=\frac{b}{a} \Rightarrow \dot r = r(N_fH_f - H)= r(\xi H_f - H). $$

Mas no ramo dinâmico, H=\xi H_f, então formalmente:

$\dot r = 0.$

Isso significa que:

- em bimetric HR puro, o ramo dinâmico tende a restringir r por consistência,

- e a dinâmica efetiva pode estar mais em \xi e nos coeficientes temporais (como F(\chi)).

Na TDCP, portanto, há duas práticas possíveis:

**(E.9.A) r constante (solução mais simples e útil)**

Assume-se r=c (subcaso proporcional aproximado) e toda dinâmica extra vem de χ e η.

**(E.9.B) r variável via escolha de ramo mais geral**

Se quisermos \dot r\neq 0, trabalhamos fora do ramo estrito ou adotamos parametrização alternativa onde H=\xi H_f é relaxada por termos efetivos associados a F(\chi) e ao acoplamento dinâmico.

Como este anexo é "manual", registramos as duas opções.

Para a TDCP como foi desenvolvida conceitualmente, a opção (A) é compatível: a separação estrutural principal é carregada por η/χ, não necessariamente por r.

**E.10 Observáveis extraídos do sistema**

Uma simulação entrega, como funções de N ou z:

**(1) Hubble**

$H(z) \quad\text{com}\quad 1+z=a^{-1}.$

**(2) Função efetiva w_{\text{eff}}**

$$ \boxed{ w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN}. } $$

**(3) Frações de densidade**

$\Omega_m(N),\quad \Omega_\chi(N),\quad \Omega_{int}(N).$

**(4) Massa efetiva do modo tensorial**

$m_T^2(N)=m^2F(\chi)\mu_T^2(\cdots).$

**(5) Checagem de Higuchi**

$m_T^2(N) \ge 2H^2(N).$

**E.11 Procedimento de integração (roteiro prático)**

1.  Fixe parâmetros:

$> (m,\beta_n,M_g,M_f, U(\chi), F(\chi), \Gamma).$

2.  Escolha condições iniciais em N=N_i (alta redshift):

- \chi(N_i) pequeno,

- x(N_i)\approx 0 (campo congelado),

- $\eta(N_i)\approx 0,$

- $\Omega_m(N_i)\approx 1.$

3.  Integre as ODEs para \chi, x, \eta, \Omega_m.

4.  A cada passo, calcule:

- H(N) pela Friedmann,

- $w_{\text{eff}}(N),$

- Higuchi,

- positividade de F(\chi).

5.  Pare se:

- Higuchi viola,

- $F(\chi)\le 0,$

- 1-\eta\to 0 (singularidade efetiva).

**E.12 Conclusão do Anexo E**

Este anexo fornece o esqueleto numérico completo:

- Um sistema ODE em N=\ln a,

- Constraints (Friedmann),

- Equação de χ + variável irreversível η,

- Regras claras para estabilidade.

Mesmo sem execução, ele serve como:

"documentação operacional" da TDCP, mostrando como a teoria seria confrontada com dados via simulação.

Se você aprovar o Anexo E, seguimos para o último do bloco técnico:

**ANEXO F --- Espaço de Parâmetros, Regiões Permitidas/Excluídas e Mapa de Consistência**

Posso continuar?
