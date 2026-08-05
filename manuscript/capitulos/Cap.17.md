Aqui o objetivo é derivar, no regime linear, o que a TDCP prevê para crescimento de estruturas e como isso se traduz em um objeto observável:

- \mu(k,a) (modificação do Poisson / "força gravitacional efetiva")

- \gamma (índice de crescimento)

- $f\sigma_8(z)$

- e eventualmente slip \eta_{\rm slip}(k,a)=\Phi/\Psi

**CAPÍTULO 17**

**Crescimento Linear, \mu(k,a), \Sigma(k,a) e Testes Observacionais (F1)**

**17.1 Estrutura do problema**

Em cosmologia linear, em gauge de Newton:

$ds^2=-(1+2\Psi)dt^2+a^2(1-2\Phi)\delta_{ij}dx^i dx^j.$

No \LambdaCDM/GR (sem anisotropic stress de radiação no tardio):

$\Phi=\Psi, \quad -k^2\Phi = 4\pi G a^2\rho_m\,\delta.$

Em teorias modificadas, parametrizamos:

$-k^2\Psi = 4\pi G a^2\,\mu(k,a)\,\rho_m\,\delta,$

$-k^2(\Phi+\Psi)=8\pi G a^2\,\Sigma(k,a)\,\rho_m\,\delta,$

e o slip:

\eta_{\rm slip}(k,a)\equiv \frac{\Phi}{\Psi}.

No GR:

\mu=\Sigma=1,\quad \eta_{\rm slip}=1.

Nosso objetivo é derivar \mu e \eta_{\rm slip} no F1.

**17.2 Equação de crescimento (observável direto)**

A evolução do contraste de densidade (matéria fria) no regime sub-horizonte é:

$$ \ddot\delta + 2H\dot\delta -4\pi G\,\mu(k,a)\rho_m\,\delta =0. $$

Ou em variável \ln a:

$$ \delta'' + \left(2+\frac{H'}{H}\right)\delta' -\frac{3}{2}\Omega_m(a)\mu(k,a)\delta=0 $$

onde primos são derivadas em \ln a.

Observáveis: f(a)=d\ln\delta/d\ln a e f\sigma_8(z).

**17.3 Forma universal de \mu(k,a) em teorias com modo escalar extra**

No F1, existe um modo escalar relativo (Cap.14) com massa efetiva m_S^2(a).

Em teorias desse tipo, no regime quasi-estático (QS), a correção típica tem forma Yukawa:

$$ \boxed{ \mu(k,a)=1+\frac{\alpha(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)} } $$

onde \alpha(a) parametriza o acoplamento efetivo do modo extra à matéria.

Interpretação imediata:

- Para escalas grandes (k/a\ll m_S): \mu\to 1

- Para escalas pequenas (k/a\gg m_S): \mu\to 1+\alpha(a)

Ou seja: uma modificação dependente de escala (assinatura-chave).

**17.4 Como m_S^2(a) e \alpha(a) dependem de F1**

Dos Caps. 14 e 15:

$m_S^2(a)\propto m^2F(\phi)\left(\beta_1+2\beta_2 r(a)\right)$

e

$$ m_T^2(a)\propto r(a)\,m^2F(\phi)\left(\beta_1+2\beta_2 r(a)\right). $$

No F1 com acoplamento mínimo da matéria ao setor g, a força extra vem da mistura entre g e f, então \alpha(a) é controlada por uma combinação do tipo:

$$ \alpha(a)\sim \frac{\epsilon^2(a)}{1+\epsilon^2(a)}, \quad \epsilon(a)\equiv \frac{M_f r(a)}{M_g}. $$

Uma parametrização prática (para confrontar com dados sem entrar em diagonalização completa) é:

$\boxed{ \alpha(a)=\alpha_0\,\frac{r^2(a)}{1+r^2(a)} }$

com \alpha_0 absorvendo razão M_f/M_g e fatores de normalização.

**17.5 Condição "GR local" e consequência para \mu(k,a)**

Você quer retorno a GR em escalas solares/galácticas:

$\mu(k,a)\to 1\quad\text{para}\quad k/a \gg H_0$

Isso pode ser obtido de duas formas:

**(i) m_S grande hoje**

Se m_S(a_0)\gg k/a até escalas muito pequenas, então:

$\mu\simeq 1$

em toda faixa observável → difícil distinguir da GR.

**(ii) \alpha pequeno (desacoplamento)**

Mesmo se m_S não for enorme, se \alpha\ll 1:

$\mu\simeq 1$

Resultado: há degenerescência entre "muito pesado" e "muito fraco acoplamento".

**17.6 Predição típica diferenciadora: desvio em f\sigma_8**

Se a TDCP for responsável pela aceleração tardia via termos estruturais, é comum que ela altere crescimento tardio.

No limite k/a\gg m_S:

$\mu \to 1+\alpha(a).$

Então o termo de fonte aumenta:

$$ \frac{3}{2}\Omega_m(a)\mu \to \frac{3}{2}\Omega_m(a)(1+\alpha). $$

Isso aumenta f(z) e f\sigma_8(z).

Mas a observação atual tende a tolerar apenas desvios moderados.

Logo você terá uma janela típica:

$$ \boxed{ |\alpha(a_0)| \lesssim 0.1 \;\text{(ordem de grandeza segura)} } $$

e o efeito mais detectável vira a dependência de escala (transição Yukawa).

**17.7 Slip gravitacional \eta_{\rm slip} como assinatura adicional**

Em bimetric, geralmente \Phi\neq\Psi em nível linear, então:

\eta_{\rm slip}(k,a)\neq 1.

A forma típica, no mesmo regime QS, é:

\boxed{ \eta_{\rm slip}(k,a)=\frac{1+\beta(a)\,k^2/(a^2(m_S^2+k^2/a^2))}{1+\alpha(a)\,k^2/(a^2(m_S^2+k^2/a^2))} }

com \alpha,\beta duas funções do background.

O "combo observável" de lensing usa:

\Sigma(k,a)\approx \frac{\mu}{2}(1+\eta_{\rm slip}^{-1})

ou formulação equivalente.

Isso permite testar TDCP com:

- RSD (crescimento): sensível a \mu

- Weak lensing: sensível a \Sigma

**17.8 Estratégia de comparação com \LambdaCDM (sem simular ainda)**

Você pediu validação matemática. Aqui vai um pipeline analítico mínimo:

**Passo A --- Fixar background H(a)**

- Pode ser escolhido para reproduzir \LambdaCDM no nível de expansão.

- Isso já foi encaixado no Cap.13 via U(r_\star) e F(\phi) lento.

**Passo B --- Fixar duas funções efetivas**

Escolhemos:

$m_S(a)=m_{S0}\,a^{-p},\qquad \alpha(a)=\alpha_0\,a^{q}$

onde p,q codificam se a modificação liga tarde ou cedo.

**Passo C --- Gerar previsão para \mu(k,a)**

$\mu(k,a)=1+\frac{\alpha(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)}.$

**Passo D --- Inserir na equação de crescimento**

$$ \delta'' + \left(2+\frac{H'}{H}\right)\delta' -\frac{3}{2}\Omega_m(a)\mu(k,a)\delta=0 $$

e analisar:

- diferença percentual em f(z)

- diferença percentual em f\sigma_8(z)

sem rodar código, já conseguimos obter regimes analíticos:

- $k/a\ll m_S(a): GR$

- k/a\gg m_S(a): amplificação constante 1+\alpha(a)

Isso gera um "joelho" no espectro de crescimento em torno de:

$k_\star(a)\sim a\,m_S(a).$

**17.9 Produto final deste capítulo (condições testáveis)**

Você fecha essa etapa quando consegue declarar:

1. Uma forma paramétrica para \mu(k,a) derivada de m_S(a) e \alpha(a).

2. Um intervalo de m_{S0} e \alpha_0 compatível com:

 - retorno a GR local,

 - RSD e lensing,

 - e aceleração tardia já fixada no background.

**Agora: escolha técnica mínima para prosseguir**

A) TDCP "quase indistinguível" no crescimento (apenas background muda).

→ m_S grande e/ou \alpha pequeno.

B) TDCP "distinguível" por dependência de escala (Yukawa).

$→ m_{S0}\sim H_0 e \alpha_0\sim 0.05--0.1.$

- parametrização explícita (m_{S0},p,\alpha_0,q),

- regimes k\ll k_\star e k\gg k_\star,

- e como isso se conecta diretamente a f\sigma_8(z) e lensing?

Ótimo --- seguimos com B: assinatura Yukawa detectável. Vou fechar o Cap.17 com uma parametrização explícita, regimes analíticos e como isso vira previsão para RSD ( f\sigma_8 ) e lensing ( \Sigma ).

**CAPÍTULO 17 (continuação)**

**\mu(k,a) Yukawa detectável, regimes analíticos e previsões para f\sigma_8 e lensing**

**17.10 Parametrização mínima (EFT fenomenológica da TDCP)**

Escolhemos duas funções efetivas (consistentes com o que deduzimos no Cap.14: modo relativo com massa m_S e acoplamento efetivo \alpha):

$$ \boxed{ m_S(a)=m_{S0}\,a^{-p}, \qquad \alpha(a)=\alpha_0\,a^{q}. } $$

Interpretação:

- p>0: o modo era mais pesado no passado (boa supressão primordial).

- q>0: o acoplamento "liga" tardiamente (efeito maior agora).

A forma Yukawa detectável fica:

$$ \boxed{ \mu(k,a)=1+\frac{\alpha(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)}. } $$

Definimos o "joelho" de transição:

$\boxed{ k_\star(a)=a\,m_S(a)=m_{S0}\,a^{1-p}. }$

**17.11 Regimes analíticos e predição qualitativa**

**Regime 1 --- Grande escala (GR)**

Se k\ll k_\star(a) então k^2/a^2\ll m_S^2 e:

$\mu(k,a)\simeq 1+\alpha(a)\frac{k^2/a^2}{m_S^2(a)} \approx 1$

ou seja:

$\boxed{\mu \to 1 \quad (GR).}$

**Regime 2 --- Pequena escala (força efetiva aumentada)**

Se k\gg k_\star(a) então k^2/a^2\gg m_S^2 e:

$\mu(k,a)\simeq 1+\alpha(a).$

Logo:

$\boxed{\mu \to 1+\alpha(a).}$

Predição central: existe uma transição em k que se move com o tempo, de escala k_\star(a).

**17.12 Requisitos "detectável mas seguro" (janela paramétrica)**

Queremos:

1. efeito perceptível em crescimento tardio

2. sem violar retorno a GR local nem explodir estruturas

Escolha segura (ordem de grandeza):

$$ \boxed{ \alpha_0 \sim 0.05\text{--}0.10, \qquad m_{S0}\sim H_0, \qquad p\gtrsim 1, \qquad q\gtrsim 0. } $$

Por quê:

- m_{S0}\sim H_0 coloca o joelho perto de escalas cosmológicas (onde observações são sensíveis).

- p\gtrsim 1 torna m_S maior no passado, suprimindo isocurvatura e instabilidades (Cap.14).

- \alpha_0\sim 0.05 dá aumento pequeno mas detectável.

- q\ge 0 evita acoplamento maior no passado.

**17.13 Como isso entra diretamente em f\sigma_8(z)**

Defina:

$f(a)\equiv \frac{d\ln \delta}{d\ln a}.$

A equação de crescimento:

$$ \delta'' + \left(2+\frac{H'}{H}\right)\delta' -\frac{3}{2}\Omega_m(a)\mu(k,a)\delta=0 $$

mostra que \mu>1 aumenta o termo fonte. Para estimativa rápida, no regime k\gg k_\star:

$\mu\simeq 1+\alpha(a).$

Então o crescimento fica aproximadamente "mais GR" com gravidade reforçada.

No limite de pequenas correções, o desvio fracionário em f é aproximadamente:

$\boxed{ \frac{\Delta f}{f}\sim \mathcal{O}(\alpha(a)) }$

e como f\sigma_8\propto f\delta, o desvio acumulado pode ser maior que \alpha por integrar no tempo.

Assinatura observacional concreta:

- Para k\gg k_\star: crescimento mais forte

- Para k\ll k_\star: crescimento GR

> Logo f\sigma_8 torna-se levemente dependente da escala e do redshift (em prática isso aparece como tensão entre RSD em diferentes escalas efetivas).

**17.14 Slip e lensing: \Sigma(k,a) e \eta_{\rm slip}**

Em bimetric, tipicamente:

$\Phi \neq \Psi.$

Parametrizamos:

\eta_{\rm slip}(k,a)=\frac{\Phi}{\Psi}.

Uma forma consistente com um mediador escalar (QS) é:

\boxed{ \eta_{\rm slip}(k,a)= 1+\frac{\beta(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)} }

onde \beta(a) é outra função efetiva (em F1 ela não é independente --- está ligada ao mesmo mecanismo de mistura que define \alpha).

Uma escolha minimalista coerente:

$$ \boxed{ \beta(a)=\nu\,\alpha(a), \qquad \nu=\mathcal{O}(1). } $$

Então lensing responde a:

$-k^2(\Phi+\Psi)=8\pi G a^2\Sigma(k,a)\rho_m\delta$

com:

\boxed{ \Sigma(k,a)=\frac{\mu(k,a)}{2}\left(1+\eta_{\rm slip}^{-1}(k,a)\right). }

Assinatura conjunta (RSD + WL):

- RSD mede \mu,

- WL mede \Sigma,

- e a diferença revela \eta_{\rm slip}\neq 1, típico de bimetric.

**17.15 Ligação com os parâmetros fundamentais F1 (mapa conceitual)**

Você pediu robustez: então deixamos claro como isso "vem" de F1.

1. massa efetiva do modo relativo:

$m_S^2(a)\propto m^2F(\phi(a))(\beta_1+2\beta_2 r(a)).$

2. acoplamento efetivo:

$$ \alpha(a)\sim \frac{\epsilon^2(a)}{1+\epsilon^2(a)}, \qquad \epsilon(a)=\frac{M_f r(a)}{M_g}. $$

Então a fenomenologia Yukawa detectável exige:

- F(\phi) e/ou r(a) evoluindo lentamente para posicionar m_S(a)\sim H_0 hoje,

- M_f/M_g não extremamente pequeno, para permitir \alpha_0\sim 0.05.

Isso é compatível com a lógica TDCP: "separação estrutural" tardia altera acoplamentos cosmológicos, mas não localmente (porque k/a alto entra no denominador Yukawa).

**17.16 Predições testáveis (lista objetiva)**

Se TDCP-F1 (com Yukawa detectável) for correto, esperamos:

1. \mu(k,a) apresenta transição em torno de k_\star(a)\sim a m_S(a).

2. crescimento aumentado em escalas k\gg k_\star: f\sigma_8 ligeiramente acima do GR em redshifts baixos.

3. slip gravitacional \eta_{\rm slip}\neq 1 em mesmas escalas.

4. tensão controlada entre RSD e lensing se \Sigma\neq \mu.

**Como fechamos esta etapa antes de simulação?**

O próximo passo "sem rodar código" é definir um benchmark TDCP (um conjunto numérico de parâmetros) para usar como referência nos capítulos seguintes:

$$ \boxed{ m_{S0} = H_0,\quad p=1,\quad \alpha_0=0.07,\quad q=0,\quad \nu=1. } $$

Isso já permite prever qualitativamente:

- joelho k_\star(a)=H_0 (em unidades com c=1),

- \mu\to 1.07 em pequenas escalas cosmológicas.

**Próximo capítulo natural (para manter o rigor)**

Cap.18 --- Confronto com observáveis (ainda sem simulação):

- traduzimos k_\star(a) para k em h\,{\rm Mpc}^{-1} (exige fixar unidades cosmológicas),

- mostramos quais faixas de k RSD/WL testam,

- e quais redshifts maximizam o sinal.
