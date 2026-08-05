Perfeito --- vamos ao Cap.19 e já vou fazer a ponte "teoria → observáveis" com unidades cosmológicas padrão, além de deixar explícito onde o sinal aparece e como escolher benchmarks realistas.

**CAPÍTULO 19**

**Confronto Observacional: Escalas, k_\star(a), RSD, Weak Lensing e "assinatura Yukawa" (F1)**

**19.1 Conversão crítica: H_0 em unidades de k (h\,{\rm Mpc}^{-1})**

Em cosmologia observacional, trabalhamos com k em h\,{\rm Mpc}^{-1}.

A escala de Hubble hoje, como número de onda comóvel, é:

$$ \frac{H_0}{c}=\frac{100\,h\ {\rm km/s/Mpc}}{299792\ {\rm km/s}} \simeq 3.335\times 10^{-4}\,h\ {\rm Mpc}^{-1}. $$

Logo:

$$ \boxed{ k_{H0}\equiv \frac{H_0}{c}\approx 3.3\times 10^{-4}\,h\,{\rm Mpc}^{-1}. } $$

Essa conta é importante porque ela fixa "onde" um m_{S0}\sim H_0 colocaria o joelho Yukawa.

**19.2 Implicação imediata: se m_{S0}=H_0, o joelho fica fora da faixa de LSS**

No Cap.18 definimos:

$k_\star(a)=a\,m_S(a)=m_{S0}a^{1-p}.$

Se você escolhe m_{S0}=H_0, então:

$$ k_\star(a_0)=k_{H0}\approx 3.3\times 10^{-4}\,h\,{\rm Mpc}^{-1}. $$

Porém medições típicas de crescimento/lensing usam:

- RSD e clustering: k \sim 0.01 \text{ a } 0.2\,h\,{\rm Mpc}^{-1}

- Weak lensing (efetivo): k\sim 0.1\,h\,{\rm Mpc}^{-1} (dependendo do binning)

Ou seja, para quase todo o que é medido:

$$ k \gg k_\star \quad \Rightarrow \quad \mu(k,a)\simeq 1+\alpha(a) $$

Resultado observacional: o efeito fica quase sem dependência de escala no regime que os surveys medem (a escala-dependência estaria apenas em escalas ultra-grandes, próximas ao horizonte).

- Isso ainda é "detectável" (como offset em \mu), mas não como "joelho Yukawa dentro do LSS".

**19.3 Para ter Yukawa dentro de k\sim 0.01\text{--}0.1, precisamos m_{S0}\gg H_0**

Queremos:

$k_\star(a_0)\sim 0.01\text{--}0.1\,h\,{\rm Mpc}^{-1}.$

Como k_{H0}\approx 3.3\times10^{-4}\,h\,{\rm Mpc}^{-1}, isso implica:

- Para k_\star=0.01: \;0.01/(3.3\times10^{-4})\approx 30

- Para k_\star=0.1: \;0.1/(3.3\times10^{-4})\approx 300

Logo um benchmark realista para "joelho dentro de LSS" é:

$\boxed{ m_{S0}\sim (30\text{--}300)\,H_0. }$

Essa é a correção mais importante para transformar a ideia em teste observacional prático.

**19.4 Benchmark TDCP (Yukawa dentro de LSS)**

Vou propor dois benchmarks (ambos com \alpha_0 moderado, como você escolheu "B"):

**Benchmark B1 (joelho em k_\star\simeq 0.01\,h\,{\rm Mpc}^{-1})**

$$ \boxed{ m_{S0}=30H_0,\quad p=1,\quad \alpha_0=0.07,\quad q=0,\quad \nu=1. } $$

Então:

$k_\star(a_0)\approx 0.01\,h\,{\rm Mpc}^{-1}.$

**Benchmark B2 (joelho em k_\star\simeq 0.1\,h\,{\rm Mpc}^{-1})**

$$ \boxed{ m_{S0}=300H_0,\quad p=1,\quad \alpha_0=0.05,\quad q=0,\quad \nu=1. } $$

Então:

$k_\star(a_0)\approx 0.1\,h\,{\rm Mpc}^{-1}.$

Nota: manter p=1 torna k_\star aproximadamente constante com o tempo; se quisermos que o joelho "ande" com z, escolhemos p\neq 1 (ver 19.6).

**19.5 Previsão direta para RSD: f\sigma_8(z)**

No regime QS, a equação de crescimento é:

$$ \delta'' + \left(2+\frac{H'}{H}\right)\delta' -\frac{3}{2}\Omega_m(a)\mu(k,a)\delta=0. $$

Com:

$\mu(k,a)=1+\frac{\alpha(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)}.$

**Duas regiões observacionais (para um dado z)**

- $Se k \ll k_\star(a): \mu\approx 1$

> \Rightarrow crescimento praticamente GR.

- $Se k \gg k_\star(a): \mu\approx 1+\alpha(a)$

> \Rightarrow crescimento reforçado.

Assinatura RSD prevista (qualitativa, porém objetiva):

- Em bins de k acima de k_\star, f\sigma_8(z) tende a ser maior do que GR.

- Em bins abaixo de k_\star, f\sigma_8(z) tende a coincidir com GR.

Na prática, surveys medem um "f\sigma_8 efetivo" integrado sobre uma janela em k. A TDCP prevê que esse efetivo pode mudar se a janela mudar.

**19.6 Dependência com redshift: como fazer o sinal "ligar tarde"**

Lembrando:

$k_\star(a)=m_{S0}a^{1-p}.$

- Se p=1: k_\star ~ constante (assinatura estável em z).

- Se p>1: k_\star(a)=m_{S0}a^{-(p-1)} cresce no passado (a menor)

> \Rightarrow mais modos ficam em k\ll k_\star no passado \Rightarrow GR no passado (bom para CMB/BAO).

Então uma escolha "ligar tarde" é:

$\boxed{p>1 \quad \text{e}\quad q\ge 0.}$

Porque:

- no passado m_S maior e/ou k_\star maior → suprime modificação,

- hoje m_S menor → joelho entra no LSS.

**19.7 Weak lensing: \Sigma(k,a) e discrepância RSD vs WL**

O lensing mede \Phi+\Psi. Definimos:

$-k^2(\Phi+\Psi)=8\pi G a^2\Sigma(k,a)\rho_m\delta.$

Com slip:

\eta_{\rm slip}=\frac{\Phi}{\Psi}, \qquad -k^2\Psi=4\pi G a^2\mu\rho_m\delta.

Então:

\boxed{ \Sigma(k,a)=\frac{\mu(k,a)}{2}\left(1+\eta_{\rm slip}^{-1}(k,a)\right). }

No benchmark minimalista:

\eta_{\rm slip}(k,a)=1+\frac{\beta(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)}, \qquad \beta(a)=\nu\alpha(a).

Assinatura combinada:

- $RSD vê \mu,$

- $WL vê \Sigma,$

- se \nu\neq 0, então \Sigma\neq \mu → padrão típico de bimetric.

**19.8 Matriz "o que medir / onde medir / qual sinal" (objetiva)**

**(1) RSD (f\sigma_8)**

- Sensível a: \mu(k,a)

- Sinal TDCP: aumento relativo em bins com k\gg k_\star

**(2) Weak Lensing (shear, CMB lensing)**

- Sensível a: \Sigma(k,a)

- Sinal TDCP: discrepância entre \Sigma e \mu se \eta_{\rm slip}\neq 1

**(3) E_G (estatística combinada)**

- Combina lensing + clustering + RSD

- Sinal TDCP: detecta \mu vs \Sigma e o slip com menos degenerescência.

**19.9 Condições de consistência (link direto com Cap.15--17)**

O que escolhemos aqui deve respeitar:

- Supressão de isocurvatura: m_S^2 \gg H^2 na era primordial

> (com p>1, isso fica mais fácil)

- Higuchi: m_T^2\ge 2H^2 no regime de Sitter efetivo

- $EFT: H\ll \Lambda_3\sim(m^2M_{\rm eff})^{1/3}$

O ponto chave: escolher m_{S0}\sim 30\text{--}300\,H_0 não viola EFT automaticamente; é apenas uma escolha de escala cosmológica "intermediária" para o modo relativo.

**Fechamento do Cap.19: o que está decidido e o que falta**

- Definimos como traduzir m_{S0} para escalas k observáveis.

- Estabelecemos benchmarks realistas para ter joelho Yukawa dentro de LSS.

- Especificamos quais observáveis distinguem TDCP de \LambdaCDM (RSD vs WL + slip).

Falta (próximo capítulo): transformar isso em um "modelo de previsão" fechado para comparação, isto é:

- escolher p,q,\alpha_0,\nu final,

- escolher m_{S0} final (B1 ou B2),

- e derivar o comportamento esperado de \Delta f\sigma_8(z) em termos de ordem de grandeza, por faixa de k.

**Próximo passo proposto (Cap.20)**

Cap.20 --- Previsões quantitativas de primeira ordem (sem simulação):

- aproximar solução do crescimento com \mu=1+\alpha em regime k\gg k_\star,

- estimar \Delta f\sigma_8(z) e dependência com k,

- estimar \Delta \Sigma e \Delta E_G.

