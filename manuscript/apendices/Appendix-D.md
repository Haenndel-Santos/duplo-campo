Perfeito --- vamos para o Anexo D, que trata do setor tensorial e da condição de Higuchi com o máximo de clareza e rigor.

Este anexo é importante por dois motivos:

1.  O setor tensorial é o lugar onde a massa efetiva do modo spin-2 aparece de forma mais "limpa";

2.  A condição de Higuchi é uma restrição universal (quase inevitável) para qualquer graviton massivo em fundo acelerado.

A TDCP, por modular o potencial por F(\chi), torna a massa efetiva dinâmica, então precisamos deixar isso cristalino.

**ANEXO D**

**Setor Tensorial, Massa Efetiva Dinâmica e Condição de Higuchi**

**D.1 Objetivo do anexo**

Queremos:

1.  Derivar a equação de movimento para perturbações tensorias na bimetric HR.

2.  Mostrar como surge o modo massless e o modo massivo.

3.  Definir a massa efetiva m_{\text{eff}}^2 no fundo cosmológico.

4.  Derivar a condição de Higuchi e explicar seu sentido físico.

5.  Explicar como a TDCP altera m_{\text{eff}}^2 via F(\chi).

**D.2 Perturbações tensoriais nas duas métricas**

No fundo FLRW (com curvatura espacial nula), definimos perturbações tensoriais transversas e sem traço (TT):

$\partial_i h^{ij} = 0, \qquad h^i_{\ i}=0.$

Para a métrica g:

$$ ds_g^2 = -dt^2 + a^2(t)\left(\delta_{ij}+h_{ij}\right)dx^i dx^j. $$

Para a métrica f:

$$ ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\left(\delta_{ij}+\ell_{ij}\right)dx^i dx^j. $$

onde h_{ij} e \ell_{ij} são tensores TT.

Cada um possui 2 polarizações.

**D.3 Ação quadrática tensorial: estrutura geral**

Expandimos a ação até segunda ordem em h_{ij},\ell_{ij}.

A ação tensorial quadrática assume a forma padrão:

$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 b^3 N_f^{-1}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 N_g F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$

Aqui:

- h e \ell representam cada polarização (tratamos uma polarização por vez).

- O termo de massa sempre aparece como diferença (h-\ell): isso é reflexo direto do potencial HR.

- \mathcal{M}(r,\xi) é uma função do background derivada das combinações \beta_n (abaixo).

No gauge N_g=1, fica:

$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 \frac{b^3}{N_f}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$

**D.4 Identificação da "massa efetiva" do modo massivo**

O termo que acopla (h-\ell)^2 define o modo massivo.

Para tornar isso explícito, fazemos combinação linear:

$$ h_+ \equiv \frac{M_g h + M_f r^{3/2}\ell}{\sqrt{M_g^2 + M_f^2 r^3}}, $$

$$ h_- \equiv \frac{M_f r^{3/2} h - M_g \ell}{\sqrt{M_g^2 + M_f^2 r^3}}. $$

- h_+: modo efetivamente massless (a "gravidade usual").

- h_-: modo massivo (sensível ao potencial HR).

Nesta base, a ação se diagonaliza em:

$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ \mathcal{A}_+(t)\left(\dot h_+^2 - c_+^2\frac{k^2}{a^2}h_+^2\right) + \mathcal{A}_-(t)\left(\dot h_-^2 - c_-^2\frac{k^2}{a^2}h_-^2 - m_T^2(t) h_-^2\right) \right]. $$

O modo h_+ propaga essencialmente como GR (com pequenas correções se r\neq 1 e N_f\neq 1).

O modo h_- tem uma massa efetiva:

$m_T^2(t) = m^2 F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f).$

O fator \mu_T^2 depende de combinações específicas do background.

**D.5 Forma explícita de \mu_T^2 em FLRW**

Na literatura de bimetric cosmology, surge uma combinação recorrente:

$\mathcal{B}(r)\equiv \beta_1 + 2\beta_2 r + \beta_3 r^2.$

Essa é a mesma combinação que aparece na constraint de Bianchi.

No setor tensorial, a massa efetiva do modo relativo h-\ell é proporcional a \mathcal{B}(r) multiplicada por fatores de r e pelas escalas de Planck.

Uma forma representativa (em gauge padrão, e reabsorvendo fatores) é:

$$ m_T^2(t)\propto m^2 F(\chi)\,\mathcal{B}(r)\,\left(\frac{1+r}{r}\right) \times \left(\text{fator de normalização em }M_g,M_f\right). $$

O ponto-chave para a TDCP não é o detalhe exato do coeficiente --- é que:

- o termo é proporcional a m^2F(\chi),

- e é controlado por uma combinação polinomial simples em r e \beta_n.

Assim:

A modulação por F(\chi) torna a massa tensorial do modo massivo uma função temporal dinâmica.

**D.6 Equação de movimento tensorial do modo massivo**

Da ação diagonalizada obtemos:

$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$

Este é o resultado central.

No limite m_T^2\to 0, recuperamos onda gravitacional padrão.

No limite m_T^2 \sim H_0^2, há efeitos apenas em escalas cosmológicas.

**D.7 Fundo de Sitter e a condição de Higuchi**

Agora consideramos o regime acelerado tardio ou de Sitter efetivo:

$a(t)\propto e^{Ht}, \qquad H=\text{constante}.$

Para um campo spin-2 massivo em de Sitter, a análise de representações do grupo de isometrias SO(1,4) mostra que:

- a helicidade-0 do spin-2 se torna ghost se a massa for pequena demais.

O resultado é a condição de Higuchi:

$m_{\text{spin-2}}^2 \ge 2H^2.$

No contexto da TDCP:

$$ m_{\text{spin-2}}^2 \equiv m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots). $$

Portanto, o bound se torna:

$m^2F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f) \ge 2H^2.$

Esse é um constrangimento duro: ele seleciona uma região do espaço de parâmetros e do background.

**D.8 Interpretação física do bound**

Por que exatamente 2H^2?

Porque em de Sitter:

- o operador cinético efetivo da helicidade-0 sofre correção proporcional ao fundo.

- quando m^2<2H^2, o termo cinético efetivo troca de sinal.

Ou seja:

A expansão acelerada "alimenta" o modo helicidade-0, e abaixo de um limiar ele vira energia negativa.

Isso é independente da TDCP --- é uma propriedade do spin-2 massivo em dS.

**D.9 Implicações diretas para a TDCP**

A TDCP quer:

- m \sim H_0 para ativação tardia,

- mas também quer estabilidade.

Se m\sim H_0, então o bound Higuchi força:

- F(\chi) não pode diminuir demais no regime tardio,

- e a combinação \mu_T^2 não pode ser pequena.

Em termos qualitativos:

- a TDCP não pode "gerar aceleração" reduzindo a massa do spin-2 até quase zero,

- porque isso tornaria a helicidade-0 fantasma.

Portanto, o mecanismo TDCP é coerente com a narrativa:

aceleração surge via separação estrutural acumulada (η), não por tornar o setor massivo ultraleve de forma perigosa.

**D.10 Consequências observacionais do termo de massa**

A presença de m_T^2(t) implica:

1.  Supressão de ondas gravitacionais em escalas muito longas (k/a \lesssim m_T).

2.  Dispersão: fase/frequência pode ser modificada para modos cosmológicos.

3.  Pequenas alterações no fundo estocástico de baixíssima frequência.

Mas, se m_T \sim H_0, então:

- efeitos estão fora da faixa do LIGO/Virgo/KAGRA,

- e ficam mais relevantes para:

  - PTA (pulsar timing arrays) em regime ultra-lento,

  - e observações cosmológicas indiretas.

**D.11 Conclusão do Anexo D**

Derivamos a estrutura essencial:

- Dois modos tensoriais aparecem: massless h_+ e massivo h_-.

- O modo massivo obedece:

$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$

- A massa efetiva é dinâmica:

$m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots).$

- A estabilidade em fundo acelerado impõe Higuchi:

$m_T^2(t)\ge 2H^2.$

Isso conecta diretamente:

- estabilidade interna (Cap. 5),

- espaço de parâmetros (Cap. 7),

- falsificabilidade tensorial (Cap. 8).

Se você aprovar o Anexo D, o próximo é:

**ANEXO E --- Sistema Dinâmico Completo para Simulação Numérica (conjunto fechado de ODEs, variáveis adimensionais e estratégia de integração)**

Mesmo você não rodando Python agora, este anexo serve como "manual de simulação" do modelo.

Posso continuar?
