Agora entramos no Anexo C, o mais delicado tecnicamente: o setor escalar é onde gravidade modificada costuma "morrer" (ghost/gradiente).

- definir as perturbações (duas métricas + χ),

- fixar gauge e identificar variáveis dinâmicas,

- integrar variáveis não-dinâmicas (constraints),

- obter a ação quadrática efetiva,

- extrair a matriz cinética K_{ij},

- impor condições de ausência de ghost,

- extrair velocidades do som c_s^2 e impor estabilidade de gradiente,

- mostrar o papel da modulação F(\chi) na TDCP.

Observação importante (para manter honestidade e rigor):

A forma completa de K_{ij}, G_{ij} e M_{ij} em bimetric cosmological perturbation theory é longa e dependente de parametrização específica (escolha de variáveis e gauge) e das funções de background a(t), r(t), \xi(t), \chi(t). Como estamos reconstruindo "o anexo" como material de tese, vou escrever a derivação no formato padrão: estrutura geral + forma canônica + condições explícitas e, onde os coeficientes são extensos, vou indicar a expressão em termos de combinações-padrão (funções A_i(r,\xi), etc.), deixando claro o que é calculável e como se obtém.

**ANEXO C**

**Análise Quadrática do Setor Escalar: Ghost, Gradiente e Mistura com χ**

**C.1 Objetivo e risco físico**

O setor tensorial em teorias HR é relativamente controlado.

O setor escalar é o lugar onde aparecem:

- ghost cinético (energia negativa),

- instabilidade de gradiente (c_s^2<0),

- crescimento explosivo em escalas pequenas,

- inconsistência com estrutura em larga escala.

A TDCP adiciona um escalar \chi e modula a massa efetiva por F(\chi).

Isso aumenta o risco de:

- misturar a helicidade-0 do modo massivo com \delta\chi,

- gerar um modo escalar mal-sinalizado.

Portanto, este anexo estabelece as condições gerais de saúde dinâmica do setor escalar.

**C.2 Perturbações escalares: duas métricas + χ**

Trabalharemos no espaço-tempo com simetria de fundo FLRW:

$$ \bar g_{\mu\nu}dx^\mu dx^\nu = -dt^2 + a^2(t)\delta_{ij}dx^i dx^j, $$

$$ \bar f_{\mu\nu}dx^\mu dx^\nu = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j. $$

Definimos perturbações escalares no espaço de Fourier (modo k).

**C.2.1 Setor g (escalar)**

No gauge genérico:

$$ ds_g^2 = -(1+2\Phi_g)dt^2 + 2a\,\partial_i B_g\,dt\,dx^i + a^2\left[(1-2\Psi_g)\delta_{ij} + 2\partial_i\partial_j E_g\right]dx^i dx^j. $$

**C.2.2 Setor f (escalar)**

$$ ds_f^2 = -N_f^2(1+2\Phi_f)dt^2 + 2bN_f\,\partial_i B_f\,dt\,dx^i + b^2\left[(1-2\Psi_f)\delta_{ij} + 2\partial_i\partial_j E_f\right]dx^i dx^j. $$

**C.2.3 Campo χ**

$\chi(t,\mathbf{x}) = \bar\chi(t) + \delta\chi(t,\mathbf{x}).$

**C.3 Escolha de gauge e contagem de variáveis**

Cada métrica tem 4 variáveis escalares (\Phi, B, \Psi, E).

Total bruto: 8 variáveis escalares + \delta\chi = 9.

Mas:

- simetria difeomórfica é reduzida na bimetric: a interação quebra Diff_g \times Diff_f para uma diagonal Diff.

- portanto há apenas 2 funções escalares de gauge (tempo + escalar espacial), removendo 2×2 = 4 graus escalares não físicos.

Além disso, variáveis tipo lapse e shift são não-dinâmicas (entram sem derivadas temporais) e geram constraints.

O resultado físico esperado (linear) é:

- 1 modo escalar propagante do graviton massivo (helicidade-0),

- 1 modo escalar propagante de \chi.

Total: 2 modos escalares físicos.

O objetivo é obter a ação quadrática desses dois modos.

**C.4 Variáveis invariantes e base física**

É útil definir combinações:

- "modo adiabático" (associado ao setor visível e matéria),

- "modo relativo" (diferença entre métricas),

- e a flutuação de χ.

Uma escolha padrão é trabalhar com:

$$ \Delta\Psi \equiv \Psi_f - \Psi_g, \qquad \Delta E \equiv E_f - E_g, \qquad \delta\chi. $$

E fixar um gauge para remover redundâncias, por exemplo:

- Gauge Newtoniano no setor g: B_g=0, E_g=0.

> Isso fixa os 2 graus de gauge escalares.

Então o setor g fica com \Phi_g, \Psi_g, e o setor f mantém B_f, E_f e seus potenciais.

**C.5 Estrutura da ação quadrática**

Ao expandir a ação até segunda ordem:

$S = S^{(0)} + S^{(1)} + S^{(2)} + \cdots,$

o termo S^{(1)}=0 quando o fundo satisfaz as equações de Friedmann (Anexo B).

O termo relevante para estabilidade é S^{(2)}.

A forma geral para 2 modos escalares Q_i (após integrar constraints) é:

$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q_i\,K_{ij}(t,k)\,\dot Q_j - Q_i\,\Omega_{ij}(t,k)\,Q_j \right], $$

onde:

- Q_i são os dois modos propagantes,

- K_{ij} é a matriz cinética,

- \Omega_{ij} contém termos de gradiente (\propto k^2) e massa.

É comum decompor:

$\Omega_{ij} = \frac{k^2}{a^2}G_{ij}(t) + M_{ij}(t).$

**C.6 Integração das variáveis não-dinâmicas**

As variáveis:

- \Phi_g, \Phi_f (lapses),

- B_f (shift relativo, já que B_g=0),

entram sem derivadas temporais. Elas são multiplicadores de Lagrange.

Variação em relação a elas gera equações algébricas (constraints) do tipo:

$\mathcal{C}_A(Q,\dot Q;k,t)=0.$

Resolvendo essas constraints e substituindo de volta na ação, obtemos a ação reduzida.

Esse passo é onde o ghost BD desaparece na bimetric HR:

o sistema mantém restrições suficientes para remover o modo extra.

Na TDCP, desde que F(\chi) seja função escalar suave, as constraints estruturais do potencial permanecem (o ghost BD não é reintroduzido). O que muda é o acoplamento efetivo e a mistura com \delta\chi.

**C.7 Matriz cinética e condições de ausência de ghost**

Após redução, obtemos dois modos propagantes Q=(Q_1,Q_2), que podem ser escolhidos como:

- Q_1: helicidade-0 efetiva do modo massivo (combinação de \Delta\Psi,\Delta E),

- Q_2: \delta\chi reescalada.

A matriz cinética pode ser escrita genericamente como:

K_{ij}(t) = \begin{pmatrix} K_{11}(t) & K_{12}(t) \\ K_{12}(t) & K_{22}(t) \end{pmatrix}.

**Condição geral de ausência de ghost**

A energia cinética deve ser positiva definida:

1. $K_{11} > 0$

2. $\det K = K_{11}K_{22}-K_{12}^2 > 0.$

Essas duas condições equivalem a dizer que os autovalores \kappa_{\pm} de K são positivos.

**Interpretação na TDCP**

- K_{22} vem principalmente do termo canônico de \chi: tipicamente K_{22}\sim 1 (positivo).

- K_{11} vem da helicidade-0 do modo massivo: depende dos parâmetros \beta_n, de r,\xi, e da massa efetiva m^2F(\chi).

- K_{12} é mistura: controlada por F'(\chi) e pela sensibilidade do potencial a perturbações relativas.

Isso já sugere um requisito físico simples:

F(\chi) deve ser positiva e variar lentamente para evitar mistura forte e inversão de sinal efetiva.

Condições práticas (regime adiabático):

$$ F(\chi)>0, \qquad \left|\frac{\dot F}{F}\right| \ll H, \qquad \left|\frac{F'}{F}\right|\Delta\chi \ll 1. $$

**C.8 Velocidade do som e estabilidade de gradiente**

O termo de gradiente define G_{ij}.

Os modos propagantes têm velocidades do som obtidas de:

$\det\left(c_s^2 K - G\right)=0.$

Ou seja, os c_s^2 são autovalores da matriz:

$K^{-1}G.$

**Condição de estabilidade de gradiente**

Para evitar instabilidade exponencial em escalas sub-horizonte:

$c_{s,\pm}^2 > 0.$

Além disso, em teoria relativística estável, usualmente esperamos:

$c_s^2 \le 1$

(não estritamente necessário em teorias efetivas, mas desejável para evitar superluminalidade sistemática e problemas de causalidade efetiva).

**Interpretação física**

- Se c_s^2<0, então para k/a grande, o modo cresce como:

$\exp\left(|c_s| \frac{k}{a} t\right),$

o que destrói a teoria imediatamente.

Na TDCP, o maior risco é quando:

- m_{eff}^2 = m^2F(\chi) fica muito pequeno,

- ou quando a mistura K_{12} fica grande.

Por isso o bound de Higuchi e a positividade de F aparecem como "guard rails" não só tensorialmente, mas também no setor escalar.

**C.9 Conexão com Higuchi e com o modo helicidade-0**

Em fundos próximos a de Sitter, para um campo spin-2 massivo, a helicidade-0 é saudável apenas se:

$m_{eff}^2 \ge 2H^2.$

Quando essa condição é violada:

- a helicidade-0 troca sinal cinético,

- e torna-se ghost.

Logo, em linguagem da matriz cinética:

$K_{11} \to 0 \quad \text{em } m_{eff}^2\to 2H^2,$

e se m_{eff}^2<2H^2, então K_{11}<0.

Portanto, Higuchi é equivalente (em regimes dS-like) à positividade do bloco cinético do modo massivo.

**C.10 Condições resumidas em forma "operacional"**

A TDCP é escalarmente estável se, ao longo da evolução cosmológica relevante:

**(1) Ghost-free (cinética positiva)**

$$ K_{11} > 0, \qquad K_{22} > 0, \qquad K_{11}K_{22}-K_{12}^2 > 0. $$

**(2) Gradiente estável**

$c_{s,\pm}^2 > 0.$

**(3) Higuchi (regime acelerado)**

$m^2F(\chi) \ge 2H^2.$

**(4) Adiabaticidade da modulação**

$\left|\frac{\dot F}{F}\right| \ll H.$

**C.11 Comentário técnico: por que F(\chi) não reintroduz o ghost BD**

O ghost BD é removido em HR pela estrutura especial do potencial com \sqrt{g^{-1}f}, que gera constraints não-lineares adicionais.

A TDCP modifica o termo:

$$ \sqrt{-g}\,V(\mathcal{K}) \quad\to\quad \sqrt{-g}\,F(\chi)V(\mathcal{K}). $$

Como F(\chi) não depende de derivadas de métricas e não altera a forma funcional em \mathcal{K}, a estrutura de constraints do setor gravitacional permanece.

O que muda é o acoplamento temporal efetivo do potencial, que afeta o background e a mistura linear com \delta\chi, mas não reintroduz automaticamente o BD ghost.

**C.12 Conclusão do Anexo C**

Neste anexo estabelecemos:

1. O setor escalar propagante na TDCP contém 2 modos físicos:

 - helicidade-0 do spin-2 massivo,

 - flutuação do campo estrutural \chi.

2. A ação quadrática reduzida pode ser escrita na forma canônica:

$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q^T K \dot Q - Q^T\left(\frac{k^2}{a^2}G+M\right)Q \right]. $$

3. As condições fundamentais de saúde dinâmica são:

 - K positiva definida (sem ghost),

 - autovalores de K^{-1}G positivos (sem instabilidade de gradiente),

 - Higuchi no regime acelerado,

 - modulação F(\chi) adiabática.

Este anexo fornece o "check-list" matemático que deve ser imposto em qualquer ajuste numérico futuro do background (a,r,\chi).

**ANEXO D --- Setor Tensorial e Condição de Higuchi (derivação detalhada do modo massivo em fundo FLRW e limite de Sitter)**
