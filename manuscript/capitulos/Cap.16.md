Perfeito. Vamos fechar o bloco de validação com o Capítulo 16 --- Consistência UV e Estrutura de Teoria Efetiva (EFT), mantendo foco técnico e critérios verificáveis.

**CAPÍTULO 16**

**Consistência UV, Escala de Forte Acoplamento e Estrutura EFT (F1)**

Continuamos com:

$(\beta_0,\beta_1,\beta_2,0,\beta_4), \quad V \to F(\phi)V,$

e fundo FLRW já estabelecido.

Objetivos:

1.  Determinar a escala de forte acoplamento.

2.  Verificar ausência de novos fantasmas abaixo do cutoff.

3.  Definir domínio de validade da teoria.

4.  Avaliar estabilidade radiativa (naturalidade).

**16.1 Estrutura EFT do setor massivo**

Em teorias de gravidade massiva/bimetric, a escala de forte acoplamento típica (no setor helicity-0 do modo massivo) é:

$\boxed{ \Lambda_3 \sim (m^2 M_{\rm Pl})^{1/3}. }$

Aqui, com dois setores, substituímos M_{\rm Pl}\to M_{\rm eff}.

Logo:

\boxed{ \Lambda_{\rm TDCP} \sim (m^2 M_{\rm eff})^{1/3}. }

Essa é a escala onde interações não-lineares do modo helicity-0 tornam-se relevantes.

**16.2 Condição básica de validade EFT**

Para que a teoria seja consistente como EFT:

\boxed{ H \ll \Lambda_{\rm TDCP}. }

ou seja, a expansão cosmológica deve ocorrer bem abaixo da escala de forte acoplamento.

Substituindo:

$H \ll (m^2 M_{\rm eff})^{1/3}.$

Elevando ao cubo:

$H^3 \ll m^2 M_{\rm eff}.$

**16.3 Conexão com Higuchi**

Lembrando que:

$m_T^2 \sim m^2 F(\phi) r(\beta_1+2\beta_2 r).$

E Higuchi exige:

$m_T^2 \ge 2H^2.$

Portanto:

$m^2 \gtrsim \frac{2H^2}{F(\phi) r(\beta_1+2\beta_2 r)}.$

Substituindo na escala EFT:

\Lambda_{\rm TDCP} \sim \left( \frac{2H^2}{F r(\beta_1+2\beta_2 r)} M_{\rm eff} \right)^{1/3}.

Para consistência UV precisamos:

$$ H \ll \left( \frac{2H^2 M_{\rm eff}} {F r(\beta_1+2\beta_2 r)} \right)^{1/3}. $$

Elevando ao cubo e simplificando:

$H^3 \ll \frac{2H^2 M_{\rm eff}} {F r(\beta_1+2\beta_2 r)}.$

Cancelando H^2:

$$ \boxed{ H \ll \frac{2 M_{\rm eff}} {F r(\beta_1+2\beta_2 r)}. } $$

Como M_{\rm eff}\sim M_{\rm Pl} é enorme comparado a H, essa condição é facilmente satisfeita para valores naturais de \beta_n.

Conclusão:

✔ Higuchi não força a teoria fora do regime EFT

✔ Existe janela paramétrica consistente

**16.4 Estrutura helicity-0 e ausência de Boulware-Deser ghost**

O formalismo HR garante ausência do ghost Boulware-Deser no nível não-linear, desde que:

- O potencial tenha estrutura HR exata.

- Não haja acoplamento duplo da matéria às duas métricas.

No TDCP estamos assumindo:

$S_m = S_m[g,\psi]$

(acoplamento mínimo apenas a g_{\mu\nu}).

Logo:

\boxed{\text{Sem BD ghost abaixo de } \Lambda_{\rm TDCP}.}

Se incluirmos \beta_n(\phi), devemos garantir que a modulação preserve a estrutura simétrica do potencial.

**16.5 Correções radiativas**

A preocupação:

Loops quânticos podem gerar:

$$ \delta \beta_n \sim \frac{\Lambda_{\rm cut}^4}{16\pi^2 M_{\rm eff}^2 m^2}. $$

Para estabilidade radiativa precisamos:

$\delta \beta_n \ll \beta_n.$

Se a teoria for válida até \Lambda_{\rm TDCP}, então:

\Lambda_{\rm cut}\sim \Lambda_{\rm TDCP}.

Substituindo:

$$ \delta \beta_n \sim \frac{(m^2 M_{\rm eff})^{4/3}} {16\pi^2 M_{\rm eff}^2 m^2} = \frac{m^{2/3}} {16\pi^2 M_{\rm eff}^{2/3}}. $$

Como M_{\rm eff}\sim M_{\rm Pl} é enorme:

$\boxed{ \delta \beta_n \ll 1 }$

para m\ll M_{\rm Pl}, que é exatamente o regime cosmológico.

Conclusão:

✔ F1 é tecnicamente natural como EFT cosmológica.

**16.6 Domínio de validade cosmológica**

A TDCP deve ser tratada como válida:

H \lesssim \Lambda_{\rm TDCP}

ou seja:

- Pós-bifurcação.

- Não necessariamente válida na escala de Planck.

- Não descreve a singularidade original.

- É EFT gravitacional infravermelha modificada.

Isso é cientificamente aceitável e padrão em cosmologia moderna.

**16.7 Resultado final do bloco de validação**

Reunindo Cap.13--16, temos:

**Fundo:**

$$ \beta_1\beta_2<0, \quad \beta_0-\frac{3\beta_1^2}{4\beta_2}>0. $$

**Escalar:**

$\beta_1+2\beta_2 r > 0, \quad m_S^2 \gg H^2.$

**Tensor:**

$m_T^2 \ge 2H^2, \quad m_T^2 \lesssim H_0^2 \text{ hoje}.$

**UV:**

$H \ll (m^2 M_{\rm eff})^{1/3}.$

Não há inconsistência estrutural evidente dentro de F1 sob essas condições.

**Estado Atual da Teoria**

Com F1:

✔ Fundo cosmológico consistente

✔ Setor escalar estável e controlável

✔ Higuchi satisfeita

✔ Estrutura EFT consistente

✔ Ausência de ghost

**Próxima etapa lógica**

Agora existem duas direções naturais:

1.  Construir modelo explícito para F(\phi)

> (dinâmica concreta que realiza as condições acima)

ou

2.  Comparação quantitativa com ΛCDM via equação de crescimento \mu(k,a)

> (testabilidade observacional)

Qual você prefere abordar agora?
