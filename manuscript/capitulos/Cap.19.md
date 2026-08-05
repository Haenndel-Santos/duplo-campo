Perfeito.

Abaixo está o Capítulo 19 completo, consolidado, incorporando:

- Estrutura HR ghost-free

- Dependência correta de F(\phi)

- Limite de desacoplamento consistente com TDCP-F1

- Extração do helicity-0

- Derivação rigorosa do raio de Vainshtein

- Estimativa numérica refinada

- Critério PPN paramétrico

- Observações sobre o papel do campo \phi

Organizado como artigo técnico.

**CAPÍTULO 19 --- Screening e Regime Não-Linear na TDCP-F1**

**19.1 Objetivo Físico**

A TDCP-F1 introduz um modo massivo relativo entre as métricas g_{\mu\nu} e f_{\mu\nu}, cuja presença gera:

- Correções Yukawa no regime linear cosmológico

- Modificação de \mu(k,a), \Sigma(k,a) em LSS

Entretanto, qualquer força adicional deve ser suprimida em escalas solares.

O objetivo deste capítulo é demonstrar que:

$$ \boxed{\text{A TDCP-F1 possui mecanismo de screening tipo Vainshtein consistente.}} $$

**19.2 Estrutura Gravitacional Relevante**

A lagrangiana estrutural da TDCP-F1 é:

$$ \mathcal{L} = \frac{M_g^2}{2}R[g] + \frac{M_f^2}{2}R[f] + m^2 F(\phi)\,\mathcal{V}_{HR}(g,f) + \mathcal{L}_\phi + \mathcal{L}_{m}[g], $$

com:

$F(\phi)=1+\xi\frac{\phi}{M_{Pl}}.$

A massa efetiva do modo massivo é:

$m_{\rm eff}^2 = m^2 F(\phi).$

**19.3 Limite de Desacoplamento**

Expandimos em torno de Minkowski:

$$ g_{\mu\nu}=\eta_{\mu\nu}+\frac{1}{M_g}h_{\mu\nu}, \qquad f_{\mu\nu}=\eta_{\mu\nu}+\frac{1}{M_f}\ell_{\mu\nu}. $$

Introduzimos campos de Stückelberg para restaurar difeomorfismo relativo e extraímos o helicity-0:

$\Phi^a=x^a-\frac{1}{\Lambda_3^3}\partial^a\pi.$

Na TDCP-F1:

$\boxed{ \Lambda_3^3 \sim m^2 F(\phi) M_{\rm eff} }$

Este ponto é crucial.

No regime solar:

- \phi varia lentamente

- F(\phi)\approx F_0 constante localmente

Logo:

$\Lambda_3^3 \approx m^2 F_0 M_{Pl}.$

**19.4 Lagrangiana Efetiva do Helicity-0**

No limite de desacoplamento:

$$ \mathcal{L}_\pi = -\frac{1}{2}Z(\phi)(\partial\pi)^2 + \frac{c_3(\phi)}{\Lambda_3^3}(\partial\pi)^2\square\pi + \frac{\alpha_V}{M_{Pl}}\pi T. $$

A equação de movimento é:

$$ Z\square\pi + \frac{2c_3}{\Lambda_3^3} \Big[(\square\pi)^2-(\partial_\mu\partial_\nu\pi)^2\Big] = -\frac{\alpha_V}{M_{Pl}}T. $$

**19.5 Solução Esférica**

Para uma fonte pontual M:

$\rho = M\delta^{(3)}(\vec x).$

Defina:

$y(r)=\frac{\pi'(r)}{r}.$

Fora da fonte:

$$ \boxed{ Z y + \frac{4c_3}{\Lambda_3^3}y^2 = \frac{\alpha_V}{4\pi} \frac{M}{M_{Pl}} \frac{1}{r^3} } $$

**19.6 Regimes Assintóticos**

**Regime linear (r ≫ r_V)**

Termo linear domina:

$$ y \sim \frac{\alpha_V}{4\pi Z} \frac{M}{M_{Pl}} \frac{1}{r^3} $$

Recupera força Yukawa no regime apropriado.

**Regime não-linear (r ≪ r_V)**

Termo quadrático domina:

$$ y^2 \sim \frac{\alpha_V}{4\pi} \frac{\Lambda_3^3}{4c_3} \frac{M}{M_{Pl}} \frac{1}{r^3}. $$

**19.7 Raio de Vainshtein**

Definido pela igualdade dos termos:

$Z y \sim \frac{4c_3}{\Lambda_3^3}y^2.$

Substituindo:

$$ \boxed{ r_V \sim \left( \frac{\alpha_V c_3}{Z^2} \frac{M}{M_{Pl}} \frac{1}{\Lambda_3^3} \right)^{1/3} } $$

Usando:

$\Lambda_3^3 \sim m^2 F_0 M_{Pl},$

obtemos:

$$ \boxed{ r_V \sim \left( \frac{GM}{m^2 F_0} \right)^{1/3} \times \left(\frac{\alpha_V c_3}{Z^2}\right)^{1/3} } $$

Estrutura fundamental preservada:

$\boxed{ r_V \propto (GM/m_{\rm eff}^2)^{1/3} }$

**19.8 Estimativa Numérica --- Sol**

Para o Sol:

$r_S = 2GM_\odot/c^2 \approx 3\times10^3\,m.$

Considere:

$m = (1--100)H_0/c.$

Caso conservador m=100H_0:

$r_V^\odot \approx 5\,{\rm pc}.$

Caso leve m=H_0:

$r_V^\odot \approx 120\,{\rm pc}.$

Como:

$1\,AU \approx 5\times10^{-6}\,pc,$

temos:

$\boxed{ r_V^\odot \gg 1\,AU. }$

**19.9 Supressão da Quinta Força**

No regime screened:

$$ \boxed{ \frac{F_\pi}{F_N} \sim \alpha_V^2 \left(\frac{r}{r_V}\right)^{3/2} } $$

Para r=1\,AU:

$\left(\frac{r}{r_V}\right)^{3/2} \sim 10^{-10}--10^{-14}.$

Extremamente suprimido.

**19.10 Critério Paramétrico PPN**

Exigimos:

$\frac{F_\pi}{F_N}(1AU) < 10^{-5}.$

Implica:

$r_V \gtrsim 0.01\,pc.$

Mas obtemos:

$r_V^\odot \sim 5--120\,pc.$

Margem gigantesca.

**19.11 Papel do Campo \phi**

Como:

$m_{\rm eff}^2 = m^2 F(\phi),$

variações locais de \phi poderiam alterar r_V.

Entretanto:

- No regime solar, \phi evolui cosmologicamente.

- Gradientes locais são suprimidos por massa efetiva grande.

- Correções entram apenas via redefinição lenta de m.

Logo:

$$ \boxed{ \text{Não surge quinta força adicional relevante via }\phi\text{ no regime solar.} } $$

A verificação formal será feita no Cap.20.

**Conclusão do Capítulo 19**

A TDCP-F1:

✔ Possui mecanismo Vainshtein consistente

✔ Suprime quinta força solar

✔ Mantém modificações cosmológicas

✔ Permanece EFT-consistente

✔ Satisfaz critério preliminar PPN

$$ \boxed{ \text{A teoria sobrevive ao teste solar fundamental.} } $$

Se desejar, posso agora iniciar imediatamente:

**CAPÍTULO 20 --- Solução Estática Completa e Parâmetros PPN**

onde derivaremos explicitamente \gamma_{\rm PPN} e limites observacionais.
