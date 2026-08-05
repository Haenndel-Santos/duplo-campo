Agora que o Capítulo 6 está robusto e o setor escalar foi reduzido a graus físicos com condições de estabilidade, o próximo passo lógico é pegar esse setor escalar reduzido e perguntar:

Como a gravidade "aparece" para a matéria no regime sub-horizonte?

Isso é o coração da ponte entre a TDCP e observações de estrutura em larga escala.

**CAPÍTULO 7**

**Limite Quase-Estático, Gravidade Efetiva e Equação de Poisson Modificada**

**7.1 Por que a Equação de Poisson é o "mapa da gravidade" no universo real**

A Relatividade Geral é uma teoria geométrica completa.

Mas quando estudamos formação de estrutura --- galáxias, aglomerados, filamentos --- o que observações realmente medem é como a matéria responde a potenciais gravitacionais fracos.

Nesse regime (sub-horizonte, velocidades pequenas, potenciais fracos), a dinâmica gravítica se resume a algo familiar:

$\nabla^2 \Phi = 4\pi G a^2 \rho\,\delta$

onde:

- \Phi é o potencial gravitacional,

- a(t) é o fator de escala,

- \rho é densidade média,

- \delta = \delta\rho/\rho é o contraste de densidade.

Na cosmologia ΛCDM, essa equação é essencialmente válida (com correções relativísticas pequenas).

Mas em teorias modificadas, ela muda.

E essa mudança é exatamente onde a TDCP pode se manifestar observacionalmente sem "quebrar GR localmente".

**7.2 O Limite Quase-Estático: o que assumimos**

No regime de crescimento de estruturas em escalas menores que o horizonte:

$k \gg aH$

e para muitos modelos cosmológicos, as perturbações relevantes satisfazem:

- termos espaciais dominam termos temporais

- \dot{\Phi} e \dot{\Psi} são subdominantes

Essa aproximação é chamada limite quase-estático.

Formalmente, adotamos:

$\left|\dot{X}\right| \ll \left|\frac{k}{a}X\right|$

para variáveis escalares perturbadas X.

Isso não significa que o universo é estático.

Significa que, para as flutuações relevantes, o "tempo" é lento comparado ao gradiente espacial.

**7.3 Potenciais gravitacionais no setor visível**

No gauge Newtoniano (usado no Capítulo 6), escrevemos:

$$ ds_g^2 = -(1+2\Phi)\,dt^2 + a^2(t)(1-2\Psi)\,\delta_{ij}dx^i dx^j. $$

As duas funções \Phi e \Psi são fundamentais:

- \Phi governa movimento de matéria não relativística,

- \Phi + \Psi governa lensing gravitacional.

Na GR padrão, para matéria sem anisotropia:

$\Phi = \Psi.$

Na TDCP, isso pode deixar de ser verdade.

E isso é observável.

**7.4 A origem da modificação: o modo escalar relativo**

Do Capítulo 6, sabemos que o setor escalar reduzido pode ser representado por graus físicos:

$\mathbf{Q} = (\zeta,\ \sigma,\ \delta\phi)$

onde:

- \sigma é o modo relativo entre as métricas (memória do duplo campo),

- \delta\phi é a flutuação do campo primordial.

Em regimes cosmológicos tardios, geralmente ocorre uma hierarquia:

- um dos modos pode se tornar pesado e "integrável",

- outro pode permanecer leve e atuar como mediador.

A consequência é típica de teorias com campo extra:

a gravidade passa a ser mediada não só por \Phi, mas também por um grau escalar efetivo.

Isso leva a uma equação de Poisson modificada.

**7.5 Forma geral da Equação de Poisson Modificada**

A forma mais útil (e observacionalmente padrão) é definir uma constante gravitacional efetiva dependente de escala:

$k^2\Psi = -4\pi G a^2 \mu(k,a)\,\rho\,\delta$

e um parâmetro de deslizamento (gravitational slip):

$\eta_{\text{slip}}(k,a) \equiv \frac{\Phi}{\Psi}.$

Na GR:

$\mu = 1,\qquad \eta_{\text{slip}} = 1.$

Na TDCP:

- \mu pode ser maior ou menor que 1,

- \eta_{\text{slip}} pode desviar de 1,

- e ambos podem depender de k e a.

Isso é o que torna a teoria testável.

**7.6 Derivação conceitual (sem perder a robustez)**

No limite quase-estático, as equações de Einstein linearizadas no setor visível fornecem uma relação tipo:

$$ k^2\Psi \sim 4\pi G a^2\rho\delta + \mathcal{S}(\sigma,\delta\phi) $$

onde \mathcal{S} é uma fonte extra devido ao acoplamento com o segundo setor.

O ponto decisivo é:

- \sigma e \delta\phi obedecem equações do tipo:

$$ \left(\frac{k^2}{a^2} + m_\sigma^2\right)\sigma \approx A_\sigma \rho\delta $$

$$ \left(\frac{k^2}{a^2} + m_\phi^2\right)\delta\phi \approx A_\phi \rho\delta $$

onde A_\sigma e A_\phi dependem dos parâmetros da interação (βₙ, r(t), etc.).

Isso permite resolver algebraicamente:

$$ \sigma \sim \frac{A_\sigma}{k^2/a^2 + m_\sigma^2}\,\rho\delta $$

$$ \delta\phi \sim \frac{A_\phi}{k^2/a^2 + m_\phi^2}\,\rho\delta. $$

Substituindo na equação para \Psi, obtemos:

$$ k^2\Psi = -4\pi G a^2 \left[1 + \frac{\Delta_\sigma}{1 + m_\sigma^2 a^2/k^2} + \frac{\Delta_\phi}{1 + m_\phi^2 a^2/k^2}\right]\rho\delta. $$

Portanto:

$$ \mu(k,a)=1+\frac{\Delta_\sigma}{1+m_\sigma^2 a^2/k^2}+\frac{\Delta_\phi}{1+m_\phi^2 a^2/k^2}. $$

Essa expressão tem uma interpretação física clara:

- Em escalas pequenas k \to \infty, os termos extras suprimem → GR recuperada.

- Em escalas grandes, os termos extras emergem → gravidade efetiva muda.

alteração cosmológica sem quebrar física local.

**7.7 O papel do "vácuo dinâmico" na gravidade efetiva**

A TDCP não interpreta esses termos apenas como "campo extra".

Ela os interpreta como:

a assinatura do desacoplamento estrutural entre dois regimes geométricos.

O modo \sigma é o mensageiro matemático daquilo que, filosoficamente, você chamou de:

- tensão,

- diferença,

- vácuo dinâmico,

- busca estrutural entre campos.

Nesse ponto, filosofia e matemática se encontram:

- a matemática diz: "há um modo relativo mediando força extra".

- a filosofia diz: "há uma diferença estrutural produzindo aceleração e gravidade emergente".

**7.8 O parâmetro de slip gravitacional**

Na presença de um modo escalar extra, geralmente surge:

$\Phi \neq \Psi.$

A relação pode ser parametrizada por:

$\eta_{\text{slip}}(k,a) = \frac{1+\Pi_1(k,a)}{1+\Pi_2(k,a)}$

com \Pi_i funções de acoplamento e massas efetivas.

Se \eta_{\text{slip}}\neq 1, então:

- lensing mede \Phi+\Psi

- dinâmica mede \Psi

E a teoria produz uma diferença observável entre:

- crescimento de estrutura

- deflexão de luz

**7.9 Condições de consistência com o Capítulo 6**

Agora fechamos o ciclo:

O Capítulo 7 só é válido se as condições do Capítulo 6 forem satisfeitas:

- \mathbf{K}>0  (sem fantasma)

- c_s^2>0 (sem gradiente)

- m^2>0 no regime tardio (sem taquion)

- Higuchi m_T^2\ge 2H^2

Ou seja:

a equação de Poisson modificada só faz sentido se o sistema é estável.

Assim, um capítulo reforça o anterior e abre o próximo --- exatamente como você pediu.

**7.10 Fechamento do Capítulo 7**

Concluímos:

1. A TDCP prevê uma gravidade efetiva:

$> G \to G_{\text{eff}}(k,a)=G\mu(k,a)$

2. A teoria prevê possível slip:

$> \Phi\neq\Psi$

3. O retorno a GR ocorre naturalmente em escalas pequenas.

4. A assinatura cosmológica aparece em escalas grandes.

5. O "vácuo dinâmico" é o mecanismo estrutural interpretativo desse setor extra.

O próximo capítulo natural é:

**CAPÍTULO 8 --- Crescimento de Estruturas, Equação para \delta e o Papel do Setor Escuro**

onde vamos derivar:

$$ \ddot\delta + 2H\dot\delta = 4\pi G_{\text{eff}}(k,a)\rho\delta $$

e conectar com observações.

