Perfeito.

Vamos agora ao Capítulo 15 --- Setor Tensorial, Massa do Gravitón e Condições de Higuchi, mantendo rigor técnico completo.

**CAPÍTULO 15**

**Setor Tensorial, Massa do Gravitón e Limites de Consistência (F1)**

Continuamos com:

$$ (\beta_0,\beta_1,\beta_2,0,\beta_4) $$

no fundo FLRW.

Nosso objetivo:

1.  Extrair a ação quadrática tensorial.

2.  Identificar modos massless e massive.

3.  Derivar a massa efetiva do gravitón.

4.  Impor:

    - Higuchi bound,

    - estabilidade,

    - consistência com observações cosmológicas.

**15.1 Perturbações tensorais**

Perturbamos apenas o setor TT (transverso-traceless):

Para g_{\mu\nu}:

$$ ds_g^2 = -dt^2 + a^2(t)(\delta_{ij} + h_{ij})dx^i dx^j, $$

Para f_{\mu\nu}:

$$ ds_f^2 = -\xi^2 dt^2 + b^2(t)(\delta_{ij} + \ell_{ij})dx^i dx^j, $$

com:

$$ \partial_i h_{ij}=0,\quad h_{ii}=0, $$

$$ \partial_i \ell_{ij}=0,\quad \ell_{ii}=0. $$

**15.2 Ação quadrática tensorial**

A ação tensorial toma forma:

$$ S_T^{(2)} = \frac12 \int dt\, d^3k\, a^3 \Big[ M_g^2(\dot h^2 - \frac{k^2}{a^2}h^2) + M_f^2 r^2(\dot \ell^2 - \frac{k^2}{a^2}\ell^2) - m_{\rm mix}^2(h-\ell)^2 \Big]. $$

O termo de mistura vem do potencial HR.

Para F1, a massa de mistura é:

$$ \boxed{ m_{\rm mix}^2 = m^2 M_{\rm eff}^2 F(\phi) \left(\beta_1 r + 2\beta_2 r^2\right). } $$

Observe novamente o mesmo fator estrutural:

$$ \beta_1 + 2\beta_2 r. $$

**15.3 Diagonalização: modos físicos**

Definimos combinações:

Modo massless (GR-like):

$$ h_0 \propto M_g h + M_f r \ell, $$

Modo massivo:

$$ h_m \propto h - \ell. $$

Após diagonalização:

$$ S_T^{(2)} = \frac12 \int dt\, d^3k\, a^3 \Big[ \dot h_0^2 - \frac{k^2}{a^2}h_0^2 + \dot h_m^2 - \frac{k^2}{a^2}h_m^2 - m_T^2 h_m^2 \Big]. $$

**15.4 Massa efetiva do gravitón**

A massa do modo massivo é:

$$ \boxed{ m_T^2 = m^2 F(\phi) \frac{M_{\rm eff}^2}{M_g^2} \left(\beta_1 r + 2\beta_2 r^2\right). } $$

Fatorando:

$$ m_T^2 \propto r(\beta_1 + 2\beta_2 r). $$

Novamente o mesmo fator estrutural.

**15.5 Condição de Higuchi**

Em fundo quase-de Sitter:

$$ \boxed{ m_T^2 \ge 2 H^2. } $$

Se:

$$ m_T^2 \< 2H^2, $$

o helicity-0 do gravitón massivo torna-se fantasma (instabilidade grave).

Portanto:

$$ \boxed{ m^2 F(\phi) r(\beta_1 + 2\beta_2 r) \ge 2H^2. } $$

**15.6 Conexão com Cap.14 (isocurvatura)**

Lembrando:

$$ m_S^2 \propto m^2 F(\phi)(\beta_1 + 2\beta_2 r). $$

e agora:

$$ m_T^2 \propto r\, m^2 F(\phi)(\beta_1 + 2\beta_2 r). $$

Portanto:

$$ \boxed{ m_T^2 \sim r\, m_S^2. } $$

Isso é estruturalmente forte:

- Não é possível ajustar escalar e tensor independentemente em F1.

- Se você torna m_S^2 grande para suprimir isocurvatura,

- você também aumenta m_T^2.

Isso é bom do ponto de vista Higuchi.

**15.7 Limites cosmológicos tardios**

Observações de ondas gravitacionais exigem que:

1.  O modo massless se propague com c_T=1.

2.  O modo massivo não altere propagação observável.

Isso exige:

$$ m_T \ll k/a $$

para modos observados.

Em escala cosmológica atual:

$$ m_T \lesssim H_0 $$

é condição segura.

Mas Higuchi no passado exigia:

$$ m_T^2 \ge 2H_{\rm inf}^2. $$

A solução natural TDCP:

$$ \boxed{ m_T^2(a) = m^2 F(\phi(a)) r(a)(\beta_1 + 2\beta_2 r(a)). } $$

Se F(\phi) evolui:

- Pode ser grande na era primordial,

- Pequeno hoje.

Isso permite:

✔ Higuchi no passado

✔ Massa efetiva pequena hoje

sem tuning extremo de \beta_n.

**15.8 Condições finais de consistência para F1**

Reunindo tudo:

**(1) Estabilidade escalar:**

$$ \beta_1 + 2\beta_2 r \> 0. $$

**(2) Supressão isocurvatura:**

$$ m^2 F(\phi)(\beta_1 + 2\beta_2 r) \gg H^2. $$

**(3) Higuchi:**

$$ m^2 F(\phi) r(\beta_1 + 2\beta_2 r) \ge 2H^2. $$

**(4) Recuperação GR hoje:**

$$ m_T^2 \lesssim H_0^2. $$

**15.9 Conclusão técnica do setor tensorial**

No modelo F1:

- Escalar e tensor são rigidamente correlacionados.

- O fator estrutural único:

$$ > \beta_1 + 2\beta_2 r $$
>
> controla:

- estabilidade,

- massa escalar,

- massa do gravitón.

Isso torna F1 altamente restrito --- mas matematicamente elegante.

**Próximo passo lógico**

Agora só resta fechar o ciclo de validação com:

**CAPÍTULO 16 --- Consistência UV e Teoria Efetiva**

Precisamos analisar:

1.  Escala de forte acoplamento.

2.  Estrutura de EFT.

3.  Estabilidade radiativa.

4.  Domínio de validade.

Isso fecha o bloco matemático.

Confirmo que avançamos para Cap.16?
