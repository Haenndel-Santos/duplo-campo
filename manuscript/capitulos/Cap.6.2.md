Então vamos fazer do jeito certo --- e isso vai elevar a TDCP de "estrutura cosmológica" para "teoria dinâmica controlada".

A partir de agora, o Capítulo 6 vira um capítulo técnico de verdade, com:

- decomposição escalar completa (duas métricas + campo primordial),

- eliminação de variáveis não-dinâmicas,

- obtenção explícita do sistema reduzido,

- condições de no-ghost, no-gradient, no-tachyon,

- e só então a ponte para Poisson/crescimento.

**CAPÍTULO 6 (Versão Expandida)**

**O Setor Escalar: Redução Dinâmica, Estabilidade e Condições de Consistência**

**6.1 Por que o Setor Escalar é o "teste de vida" da teoria**

Em cosmologia, o setor escalar é onde vivem:

- a gravidade que forma estruturas,

- os potenciais gravitacionais que aparecem no lensing,

- as flutuações que viram anisotropias da CMB,

- e as instabilidades mais perigosas (fantasmas e gradientes).

Em teorias com dois campos geométricos, o setor escalar é o lugar onde o "segundo universo" pode se denunciar... ou destruir a teoria.

A pergunta do capítulo é clara:

Quando introduzimos (g_{\mu\nu}, f_{\mu\nu}) e um campo primordial \phi, conseguimos um setor escalar dinâmico, estável e observacionalmente admissível?

**6.2 Ansätze FLRW + perturbações escalares**

Tomamos como fundo:

$ds_g^2 = -dt^2 + a^2(t)\delta_{ij}dx^i dx^j$

$ds_f^2 = -X^2(t)\,dt^2 + b^2(t)\delta_{ij}dx^i dx^j$

onde X(t) é o lapse relativo do setor f.

Agora perturbamos apenas o setor escalar.

**Perturbações em g_{\mu\nu}**

$$ ds_g^2 = -(1+2\Phi)\,dt^2 + 2a(t)\partial_i B\,dt\,dx^i + a^2(t)\left[(1-2\Psi)\delta_{ij} + 2\partial_i\partial_j E\right]dx^i dx^j $$

**Perturbações em f_{\mu\nu}**

$$ ds_f^2 = -X^2(t)(1+2\Phi_f)\,dt^2 + 2X(t)b(t)\partial_i B_f\,dt\,dx^i + b^2(t)\left[(1-2\Psi_f)\delta_{ij} + 2\partial_i\partial_j E_f\right]dx^i dx^j $$

**Campo primordial**

$\phi(t,\vec{x}) = \phi_0(t) + \delta\phi(t,\vec{x})$

**6.3 Escolha de gauge e eliminação de redundâncias**

Como temos simetria de difeomorfismo, podemos fixar condições.

Uma escolha comum e eficiente:

- Gauge Newtoniano no setor visível:

$B = 0,\qquad E = 0$

Então o setor g fica descrito por \Phi e \Psi.

O setor f ainda tem \Phi_f, \Psi_f, B_f, E_f --- mas parte disso também será não-dinâmico.

**6.4 Ação quadrática: a estrutura geral**

Expandimos a ação total até segunda ordem em perturbações:

$S = S^{(0)} + S^{(1)} + S^{(2)} + \cdots$

O termo relevante para estabilidade é:

$$ S^{(2)} = \int dt\,d^3k \left[ \dot{\mathbf{Q}}^T \mathbf{K}\, \dot{\mathbf{Q}} - \mathbf{Q}^T \mathbf{\Omega}\, \mathbf{Q} \right] $$

onde o vetor de variáveis dinâmicas reduzidas pode ser escrito, após eliminação de campos auxiliares, como:

$\mathbf{Q} = (\zeta,\ \sigma,\ \delta\phi)$

Interpretando:

- \zeta: curvatura efetiva do setor visível,

- \sigma: modo escalar relativo entre as métricas (o "grau extra" do gravitón massivo),

- \delta\phi: flutuação do campo primordial.

**6.5 Variáveis não-dinâmicas: quem sai do jogo?**

Em teorias cosmológicas, \Phi e \Phi_f tipicamente entram sem derivada temporal (função de Lagrange).

Isso significa:

- elas não propagam

- impõem vínculos

Da mesma forma, B_f muitas vezes também é auxiliar.

Portanto o processo é:

1. escrever S^{(2)} com todas as variáveis

2. identificar as auxiliares

3. resolver suas equações algébricas

4. substituir de volta

5. obter o sistema reduzido real

Esse é o ponto em que a teoria se revela.

**6.6 Condição No-Ghost: positividade da matriz cinética**

A matriz cinética \mathbf{K} deve ser definida positiva:

$\mathbf{K} > 0$

equivalente a:

1. $K_{11} > 0$

2. $\det K_{2\times2} > 0$

3. $\det K_{3\times3} > 0$

Se algum autovalor for negativo:

→ existe fantasma

→ energia não limitada inferiormente

→ instabilidade fatal.

**Interpretação TDCP**

No contexto da TDCP isso significa:

a interação entre campos não pode "extrair energia" de modo ilimitado do vácuo dinâmico.

Ou o "vácuo dinâmico" se torna um motor infinito, o que seria inconsistente.

**6.7 Condição No-Gradient: positividade de c_s^2**

Depois da redução, as equações tomam forma:

$$ \ddot{Q}_i + 3H\dot{Q}_i + \left(c_{s,i}^2\frac{k^2}{a^2} + m_i^2\right) Q_i = 0 $$

A condição essencial:

$c_{s,i}^2 > 0$

Se c_s^2 < 0, então para grandes k (pequenas escalas):

$Q \sim e^{|c_s|k t/a}$

Explode rapidamente.

Isso destruiria a formação de estrutura e violaria observações.

**6.8 Condição No-Tachyon (regime tardio)**

Para estabilidade tardia:

$m_i^2 > 0$

Mas aqui há uma nuance importante para a TDCP:

- No regime primordial, m^2 < 0 pode ser a instabilidade necessária para bifurcação.

- No regime tardio, precisa relaxar para m^2 > 0.

Isso encaixa perfeitamente com o espírito da TDCP:

A teoria nasce de uma instabilidade primordial, mas precisa de um regime estável após a estrutura emergir.

**6.9 A estrutura do modo relativo \sigma**

O modo \sigma é, efetivamente, o "modo entre as métricas".

Ele é o lugar natural onde o seu conceito de vácuo dinâmico vive matematicamente.

Em termos físicos:

- \sigma mede como o universo visível "descola" do universo maior.

- \sigma é o grau que pode carregar a memória do entanglement estrutural.

E no nível efetivo, ele entra com massa e acoplamento controlados por \beta_n e por r(t).

**6.10 Integração com o campo primordial: modulação dinâmica e segurança**

Se a TDCP permite:

$\beta_n \rightarrow \beta_n(\phi),$

isso é poderoso, mas perigoso.

Porque derivadas temporais de \beta_n(\phi) introduzem termos adicionais na matriz cinética.

Logo precisamos impor uma condição de "adiabaticidade":

$\left|\frac{\dot{\beta}_n}{\beta_n}\right| \ll H$

no regime tardio.

Isto significa:

- o campo primordial pode modular,

- mas não pode oscilar violentamente no universo atual.

**6.11 Resultado técnico consolidado**

A TDCP possui setor escalar viável se:

**(i) No ghost**

$\mathbf{K} > 0$

**(ii) No gradient**

$c_{s,i}^2 > 0$

**(iii) Regime tardio estável**

$m_i^2 > 0$

**(iv) Higuchi no setor tensorial (conecta Cap.6 ao Cap.5)**

$m_T^2 \ge 2H^2$

**(v) Modulação adiabática**

$|\dot{\beta}_n/\beta_n| \ll H$

**6.12 Fechamento narrativo: o que isso significa na linguagem da TDCP?**

Em linguagem menos formal, mas fiel:

O Duplo Campo Primordial não é apenas uma história de dois universos.

Ele exige que:

- a separação entre os campos seja dinâmica,

- mas não destrua o universo por instabilidade,

- e que a memória primordial (a bifurcação) seja preservada sem gerar graus patológicos.

O "vácuo dinâmico" não é permitido ser um motor infinito --- ele deve ser um reservatório estrutural estável.

A flecha do tempo, na TDCP, continua sendo a leitura dessa separação, mas agora sabemos:

Essa leitura só é válida se o modo relativo for estável e não fantasmático.

- **Próximo passo natural (sem pular processos)**

Agora sim, com o setor escalar estruturado:

Capítulo 7 deve ser:

**"Redução Quase-Estática: Equação de Poisson Modificada e Gravidade Efetiva"**

Isso conecta diretamente:

- estabilidade → gravidade efetiva

- gravidade efetiva → formação de estruturas

- formação de estruturas → matéria escura observacional

