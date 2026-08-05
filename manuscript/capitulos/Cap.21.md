**CAPÍTULO 21 --- Estabilidade Não-Linear na TDCP-F1**

(ausência de ghost/gradiente no regime screened + consistência EFT no Vainshtein)

**21.1 Objetivo e o que significa "estável" aqui**

Após o Cap.19--20, a TDCP-F1 sobreviveu ao teste solar via screening tipo Vainshtein do helicity-0 do modo massivo. Agora o critério de sobrevivência sobe de nível:

1.  Ausência de BD ghost no setor bimetric (não-linear completo).

2.  Ausência de ghost e de instabilidade de gradiente para flutuações no background screened (regime solar).

3.  Controle EFT: o regime Vainshtein não pode exigir excitação além do cutoff efetivo (ou deve permanecer classicamente controlado).

4.  (Opcional, mas importante) características causais: velocidades de propagação e possíveis superluminalidades.

O foco técnico deste capítulo é o ponto 2--3 no setor helicity-0 (o mais crítico para screening), mantendo coerência com HR ghost-free e com a modulação m^2\to m^2F(\phi).

**21.2 Estabilidade estrutural do setor HR: ausência do BD ghost (não-linear)**

A estrutura Hassan--Rosen (HR) ghost-free garante, por construção, que o potencial bimetric

\mathcal V_{HR}(g,f) mantém o conjunto de restrições (constraint structure) que elimina o Boulware--Deser ghost no nível não-linear.

Na TDCP-F1 a interação entra como:

$m^2F(\phi)\,\mathcal V_{HR}(g,f).$

Se F(\phi) é um escalar sem derivadas multiplicando o potencial (isto é, F não depende de curvaturas e não contém termos com derivadas misturadas com g,f), então:

- a estrutura algebraica do potencial HR é preservada;

- a contagem de graus de liberdade do setor bimetric permanece a mesma;

- o BD ghost não é reintroduzido por esse tipo de modulação multiplicativa.

Conclusão estrutural: a potencial ameaça BD ghost continua ausente no bloco HR, e o problema real desloca-se para a estabilidade dinâmica dos modos efetivos (helicity-0) no background screened.

**21.3 Limite de desacoplamento: ação efetiva para \pi com modulação F(\phi)**

No limite de desacoplamento (Cap.19), relembramos o bloco mínimo que captura Vainshtein:

$$ \boxed{ \mathcal{L}_{\pi} = -\frac{1}{2}Z(\phi)(\partial\pi)^2 + \frac{c_3(\phi)}{\Lambda_3^3}(\partial\pi)^2\square\pi + \frac{\alpha_V}{M_{\rm Pl}}\pi\,T } $$

com o ponto TDCP-específico:

$$ \boxed{ \Lambda_3^3 \sim m^2 F(\phi)\,M_{\rm eff} \;\;\approx\;\; m^2F_0\,M_{\rm Pl} \quad\text{(Solar: }F(\phi)\approx F_0\text{ quase constante).} } $$

O background screened é tomado como:

$\pi(x)=\bar\pi(r)+\varphi(x), \qquad r\ll r_V.$

Nos interessa a ação quadrática para a flutuação \varphi, pois é aí que surgem:

- ghost (sinal errado do termo temporal)

- instabilidades de gradiente (sinais errados nas derivadas espaciais)

- velocidades c_s^2 patológicas

**21.4 Quadrático efetivo: "métrica cinética" para as flutuações \varphi**

Expande-se a ação em torno de \bar\pi. Para o Galileon cúbico (o termo essencial do Vainshtein), o resultado padrão pode ser escrito como:

$$ \boxed{ S^{(2)}_\varphi = \frac12\int d^4x\; K^{\mu\nu}(\bar\pi)\;\partial_\mu\varphi\,\partial_\nu\varphi } $$

onde a matriz cinética efetiva é:

$$ \boxed{ K^{\mu\nu} = Z\,\eta^{\mu\nu} + \frac{2c_3}{\Lambda_3^3} \left[ 2\,\partial^\mu\partial^\nu\bar\pi - \eta^{\mu\nu}\,\Box\bar\pi \right] } $$

(aqui Z,c_3,\Lambda_3 são avaliados no valor solar local, F\simeq F_0).

Isso define um "cone causal efetivo" para \varphi. A estabilidade exige que:

- o coeficiente do termo temporal seja positivo (sem ghost)

- os coeficientes espaciais relevantes sejam positivos (sem gradiente instável)

**21.5 Especialização para background estático esfericamente simétrico**

Para \bar\pi=\bar\pi(r), temos:

$\Box\bar\pi = \bar\pi''+\frac{2}{r}\bar\pi'.$

E a Hessiana espacial pode ser decomposta em radial e angular:

$$ \partial_i\partial_j \bar\pi = \left(\bar\pi''-\frac{\bar\pi'}{r}\right)n_i n_j + \frac{\bar\pi'}{r}\delta_{ij}, \qquad n_i=\frac{x_i}{r}. $$

Assim, os coeficientes cinéticos efetivos podem ser organizados como:

- temporal: K^{00}\equiv -Z_t (com Z_t>0 exigido para ausência de ghost)

- radial: K^{rr}\equiv Z_r

- angular: K^{\Omega\Omega}\equiv Z_\Omega/r^2

Resulta (até fatores convencionais de sinal; a forma abaixo é a versão operacional padrão usada em análises de Galileon esférico):

$$ \boxed{ Z_t = Z + \frac{4c_3}{\Lambda_3^3} \left( \bar\pi''+\frac{2}{r}\bar\pi' \right) } $$

$$ \boxed{ Z_r = Z + \frac{8c_3}{\Lambda_3^3} \left( \frac{\bar\pi'}{r} \right) } $$

$$ \boxed{ Z_\Omega = Z + \frac{4c_3}{\Lambda_3^3} \left( \bar\pi''+\frac{\bar\pi'}{r} \right) } $$

Os critérios locais de estabilidade são então:

$\boxed{ Z_t>0,\qquad Z_r>0,\qquad Z_\Omega>0. }$

E as velocidades de propagação (características) seguem de:

$$ \boxed{ c_r^2 = \frac{Z_r}{Z_t}, \qquad c_\Omega^2=\frac{Z_\Omega}{Z_t}. } $$

**21.6 Regime Vainshtein (r ≪ r_V): sinais e hierarquia**

Do Cap.19, no regime r\ll r_V (cúbico dominante), a solução implica:

$$ y(r)\equiv \frac{\bar\pi'}{r} \propto r^{-3/2}, \quad\Rightarrow\quad \frac{\bar\pi'}{r}\gg \frac{\bar\pi''}{\;}\sim \mathcal{O}\!\left(\frac{\bar\pi'}{r}\right) \quad\text{(mesma ordem paramétrica)}. $$

O ponto decisivo é que, dentro de r_V, os termos proporcionais a c_3\bar\pi''/\Lambda_3^3 e c_3(\bar\pi'/r)/\Lambda_3^3 dominam sobre Z, tornando:

$$ Z_t \sim \frac{4c_3}{\Lambda_3^3}\left(\bar\pi''+\frac{2\bar\pi'}{r}\right), \qquad Z_r \sim \frac{8c_3}{\Lambda_3^3}\left(\frac{\bar\pi'}{r}\right), \qquad Z_\Omega \sim \frac{4c_3}{\Lambda_3^3}\left(\bar\pi''+\frac{\bar\pi'}{r}\right). $$

Portanto, os sinais de estabilidade são controlados pelo sinal efetivo de c_3 multiplicado pelo sinal do perfil \bar\pi (que é fixado pela condição de atratividade e pela fonte T\simeq-\rho). Em termos práticos, a condição robusta é:

$$ \boxed{ \frac{c_3}{Z} > 0 \quad\text{(escolha de ramo/parametrização que garante }Z_t,Z_r,Z_\Omega>0\text{ no Vainshtein).} } $$

Essa condição é exatamente o análogo do requisito "ramo saudável" em análises de Galileon/dRGT: um dos ramos resolve a EOM mas produz Z_t<0 (ghost), o outro produz cinética positiva e screening físico.

**21.7 Velocidades de propagação e superluminalidade (diagnóstico)**

No regime Vainshtein, é típico obter:

- c_r^2 = Z_r/Z_t de ordem unidade, frequentemente maior que 1

- c_\Omega^2 = Z_\Omega/Z_t subluminal ou ordem unidade

Em muitos modelos Galileon cúbicos, encontra-se genericamente:

$c_r^2 \gtrsim 1,$

isto é, superluminalidade radial efetiva nas flutuações \varphi sobre o background screened.

Interpretação no contexto TDCP-F1:

- Não é automaticamente uma inconsistência interna de EFT; é uma propriedade comum de cones efetivos em backgrounds não-triviais.

- Contudo, é um ponto sensível em relação à possibilidade de UV completion Lorentz-invariante estrita.

- O que a TDCP-F1 precisa é: ausência de instabilidade (ghost/gradiente) e controle EFT. A discussão "superluminal ⇒ inconsistente" não é conclusiva sem hipóteses extras sobre UV completion.

Neste capítulo, registramos o diagnóstico:

$$ \boxed{ \text{TDCP-F1 (como HR/dRGT-like) pode herdar cones efetivos modificados no Vainshtein; isso exige monitoramento, não invalidação imediata.} } $$

**21.8 Controle EFT no regime Vainshtein: condição operacional**

No Vainshtein, a solução satisfaz o equilíbrio:

$$ Z\,y \sim \frac{4c_3}{\Lambda_3^3}y^2 \quad\Rightarrow\quad y \sim \frac{Z\Lambda_3^3}{4c_3} \quad\text{em }r\sim r_V, $$

e para r\ll r_V, y cresce.

A consistência EFT exige que:

1.  As correções de operadores mais altos (quartic/quintic Galileon e termos além do truncamento) não dominem indevidamente.

2.  As correções quânticas sejam controláveis (regime "classicalization" típico do Vainshtein).

Um critério operacional clássico (suficiente) é exigir que o regime screened seja dominado pelo mesmo operador que usamos para definir r_V, isto é:

$$ \boxed{ \left|\frac{\partial^2\bar\pi}{\Lambda_3^3}\right| \lesssim \mathcal{O}(1) \quad\text{no raio de interesse (ex.: em AU).} } $$

Como o screening solar é extremamente profundo (r_{AU}\ll r_V), isso pode ser satisfeito com folga dependendo da normalização dos coeficientes. Em termos práticos, a condição se expressa como:

$$ \boxed{ \text{Escolher a hierarquia de coeficientes }(c_3,c_4,c_5,\dots) \text{ para que o operador dominante permaneça controlado e a série EFT não colapse.} } $$

Na TDCP-F1, isso é tecnicamente implementável porque:

- a estrutura HR fixa a classe de operadores no limite de desacoplamento (Galileon)

- a modulação F(\phi) apenas desloca \Lambda_3 localmente via m^2F_0, não muda a classe de operadores

Ou seja, o controle EFT depende do ponto paramétrico e do ramo, não de um defeito estrutural.

**21.9 Papel de \phi na estabilidade não-linear**

Há duas verificações essenciais:

**(i) F(\phi) não pode variar localmente de modo a inverter sinais**

Como:

$\Lambda_3^3 \propto m^2F(\phi),$

variações locais grandes poderiam deslocar o balanço dos termos e mudar sinais efetivos. A condição de segurança já antecipada é:

$$ \boxed{ \left|\frac{\delta F}{F_0}\right| \ll 1 \quad\text{em escalas solares.} } $$

**(ii) \phi não deve introduzir uma quinta força não-screened**

Isso é garantido se:

- \phi não acopla diretamente a \mathcal L_m[g] (sem termo \phi T/M), e

- o perfil \delta\phi(r) é pequeno localmente (por massa efetiva, rigidez cinética ou outro mecanismo).

Operacionalmente:

$$ \boxed{ |\nabla \phi| \;\text{pequeno no Sistema Solar} \;\Rightarrow\; \text{nenhuma força adicional relevante além do helicity-0 já screened.} } $$

**Conclusão do Capítulo 21**

A TDCP-F1 passa no teste não-linear local se satisfizer simultaneamente:

**(A) Segurança estrutural HR**

$$ \boxed{ \text{BD ghost ausente (potencial HR ghost-free preservado por }F(\phi)\text{ multiplicativo).} } $$

**(B) Estabilidade dinâmica do helicity-0 no Vainshtein**

$$ \boxed{ Z_t>0,\; Z_r>0,\; Z_\Omega>0 \;\;\Rightarrow\;\; \text{sem ghost e sem instabilidade de gradiente.} } $$

O que, no regime screened, equivale na prática a escolher o ramo saudável:

$$ \boxed{ c_3/Z > 0 \quad (\text{com o sinal do perfil escolhido fisicamente}).} $$

**(C) Controle EFT**

$$ \boxed{ \left|\partial^2\bar\pi/\Lambda_3^3\right|\lesssim \mathcal O(1) \;\;\text{(ou hierarquia de coeficientes que mantém truncamento válido).} } $$

**(D) \phi inócuo localmente**

$$ \boxed{ |\delta F/F_0|\ll 1 \text{ em escalas solares e sem acoplamento direto }\phi T.} $$

Com esses critérios, a TDCP-F1 permanece não-linearmente plausível no setor solar screened e está pronta para entrar no bloco observacional quantitativo.

**Próximo passo (Cap.22)**

Se você confirmar, eu avanço para:

**CAPÍTULO 22 --- Pipeline quantitativo BAO + RSD + WL**

onde vamos:

- mapear \mu(k,a), \Sigma(k,a), \eta_{\rm slip} da TDCP em observáveis

- definir funções de crescimento f\sigma_8(z), distâncias BAO, e lensing

- propor um pipeline mínimo para ajuste (MCMC / likelihood modular)

- identificar degenerescências com \LambdaCDM, w_0-w_a, \Omega_k, \sum m_\nu

Se quiser seguir: diga "Cap.22".
