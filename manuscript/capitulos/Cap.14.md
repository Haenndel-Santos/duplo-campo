**CAPÍTULO 14**

**Setor Escalar, Modos Adiabáticos/Isocurvatura e Condições de Estabilidade (F1)**

Trabalharemos com:

$(\beta_0,\beta_1,\beta_2,0,\beta_4)$

no fundo FLRW já definido no Cap.13.

Nosso objetivo aqui é:

1. Extrair a ação quadrática no setor escalar.

2. Identificar os graus físicos (adiabático + isocurvatura).

3. Determinar a massa efetiva do modo isocurvatura m_S^2.

4. Impor condições:

 - ausência de fantasma,

 - ausência de instabilidade de gradiente,

 - supressão observacional de isocurvatura.

**14.1 Perturbações escalares das métricas**

Escrevemos as perturbações escalares padrão:

Para g_{\mu\nu}:

$$ ds_g^2 = -(1+2\Phi_g)dt^2 +2a\partial_i B_g dx^i dt +a^2\left[(1-2\Psi_g)\delta_{ij} +2\partial_i\partial_j E_g\right]dx^i dx^j $$

Para f_{\mu\nu}:

$$ ds_f^2 = -\xi^2(1+2\Phi_f)dt^2 +2\xi b\partial_i B_f dx^i dt +b^2\left[(1-2\Psi_f)\delta_{ij} +2\partial_i\partial_j E_f\right]dx^i dx^j $$

Incluímos também o campo estrutural:

$\phi(t) \rightarrow \phi(t) + \delta\phi.$

**14.2 Contagem de graus de liberdade**

Em bimetric HR:

- Existem 2 modos escalares físicos após remover constraints.

- Um deles corresponde ao modo adiabático (curvatura total).

- O outro é o modo relativo (isocurvatura).

Definimos combinações úteis:

Modo adiabático:

$$ \zeta = \frac{\rho_g \Psi_g + \rho_f \Psi_f}{\rho_g + \rho_f} $$

Modo relativo (isocurvatura estrutural TDCP):

$S \propto \Psi_f - \Psi_g.$

Mais precisamente, o modo físico é combinação canonicamente normalizada dessas variáveis.

**14.3 Ação quadrática (estrutura geral)**

A ação escalar quadrática assume forma matricial padrão:

$$ S^{(2)} = \frac12 \int dt\, d^3k\, a^3 \left[ \dot{\vec Q}^T K \dot{\vec Q} - \vec Q^T \Omega^2 \vec Q \right] $$

onde:

\vec Q = \begin{pmatrix} Q_\zeta \\ Q_S \end{pmatrix}

K é matriz cinética, \Omega^2 matriz de massa.

**14.4 Condição de ausência de fantasma**

Para ausência de fantasma:

$\boxed{ K \ \text{deve ser positiva definida} }$

Ou seja:

$\det(K) > 0, \quad {\rm Tr}(K) > 0.$

Em bimetric F1, a condição reduz-se a:

$M_{\rm eff}^2 \left(\beta_1 + 2\beta_2 r\right) > 0$

avaliado no fundo.

Observe que:

- No ramo algébrico temos \beta_1+2\beta_2 r_\star=0.

- Isso implica que exatamente no ramo algébrico puro o modo relativo pode se tornar fortemente acoplado.

Portanto:

Conclusão técnica importante

Para estudar isocurvatura física propagante, precisamos trabalhar ligeiramente fora do ramo algébrico puro ou incluir modulação TDCP.

**14.5 Massa efetiva do modo isocurvatura m_S^2**

A massa escalar efetiva do modo relativo é proporcional à derivada do potencial em relação a r.

Para F1:

$U(r)=\beta_0+3\beta_1 r+3\beta_2 r^2$

Logo:

$\frac{dU}{dr}=3\beta_1+6\beta_2 r.$

A massa efetiva do modo relativo assume forma típica:

$$ \boxed{ m_S^2 \sim m^2 F(\phi)\, \left(\beta_1+2\beta_2 r\right) } $$

(omito fatores de normalização dependentes de M_g,M_f,r, que são positivos.)

**14.6 Interpretação crítica**

Observe:

- O mesmo fator que define o ramo algébrico

- é o fator que controla a massa do modo isocurvatura.

$\boxed{ m_S^2 \propto \beta_1+2\beta_2 r. }$

Portanto:

- No ramo algébrico puro → m_S^2 = 0.

- No ramo dinâmico → m_S^2 \neq 0.

Isso é estrutural no HR.

**14.7 Condição de supressão observacional**

Dados CMB exigem:

$\frac{P_S}{P_\zeta} \ll 1.$

Para campo pesado:

$\boxed{ m_S^2 \gg H^2 }$

então

$S \propto a^{-3/2} e^{-m_S t}$

decai exponencialmente.

Logo condição matemática fundamental:

$$ \boxed{ m^2 F(\phi) \left(\beta_1+2\beta_2 r\right) \gg H^2. } $$

**14.8 Relação com F1 e restrições já obtidas**

Recordando:

$r_\star=-\frac{\beta_1}{2\beta_2}.$

Então:

$\beta_1+2\beta_2 r = 2\beta_2 (r-r_\star).$

Logo:

$\boxed{ m_S^2 \propto 2\beta_2 (r-r_\star). }$

Interpretação:

- Se r evolui ligeiramente ao redor de r_\star,

- o modo isocurvatura adquire massa proporcional ao desvio estrutural.

Isso é coerente com TDCP:

- no momento de bifurcação → r pode deslocar-se,

- posteriormente → relaxa para r_\star,

- tornando m_S^2 grande e suprimindo isocurvatura.

**14.9 Condição final fechada para F1**

Para controle completo precisamos impor:

**(1) Ausência de fantasma:**

$\beta_1+2\beta_2 r > 0.$

**(2) Supressão de isocurvatura:**

$m^2 F(\phi)(\beta_1+2\beta_2 r) \gg H^2.$

**(3) Consistência com Cap.13:**

$$ \beta_1\beta_2<0, \quad \beta_0-\frac{3\beta_1^2}{4\beta_2}>0. $$

Essas três já delimitam fortemente o espaço F1.

**14.10 Resultado estrutural importante**

No modelo F1:

- O controle de isocurvatura,

- a estabilidade escalar,

- e a existência do ramo,

estão todos ligados ao mesmo fator:

$\beta_1+2\beta_2 r.$

Isso significa que o ajuste de F1 é altamente não trivial:

não é possível escolher \beta_n arbitrariamente sem afetar simultaneamente:

- fundo cosmológico,

- setor escalar,

- estabilidade.

**Próximo passo lógico**

Agora temos duas direções técnicas:

(inflação TDCP e geração primordial)

ou

(necessário para fechar consistência tensorial)

Dado que o controle escalar depende fortemente da massa efetiva m_T^2 também, o caminho matematicamente mais consistente é:

Ir para Cap.15 --- Setor Tensorial e Limites na Massa do Gravitón.
