> **RASCUNHO RECONSTRUÍDO --- REVISAR**
>
> `Cap.25.docx` era idêntico a `Cap.26.docx`: nenhum dos dois continha o
> conteúdo real do Capítulo 25. O arquivo original trazia apenas a
> repetição do fim do Capítulo 24 seguida diretamente das seções
> 26.5--26.8 (que pertencem ao Capítulo 26). O conteúdo abaixo foi
> reconstruído a partir do que o próprio Capítulo 24 já anunciava para o
> Capítulo 25 ("Analisar impacto detalhado no TT, TE, EE; Avaliar ISW;
> Identificar degenerescências com A_s, τ, m_ν; Definir estratégia de
> ajuste global"), combinando exclusivamente resultados já estabelecidos:
> a fórmula padrão do efeito ISW (física de RG-padrão, não específica da
> TDCP) aplicada à substituição Φ+Ψ=2Σ(k,a)Φ_GR já derivada nos
> Capítulos 7, 18 e 19; e a restrição, já imposta desde os Capítulos 9 e
> 10, de que a TDCP não pode alterar apreciavelmente o espectro primordial
> quase invariante de escala.
>
> **O que precisa de validação do autor:**
> 1. §25.4 identifica uma contribuição de ISW "extra" (além da
>    supressão/amplificação usual) vindo da variação temporal da própria
>    função Σ(k,a), não apenas do potencial Φ_GR. Essa é uma consequência
>    matemática direta de Φ+Ψ=2ΣΦ_GR já estabelecido, mas o autor deve
>    confirmar se concorda com essa leitura antes de tratá-la como
>    previsão da teoria.
> 2. A estratégia de ajuste global (§25.6) é esboçada apenas em nível de
>    princípio aqui; o detalhamento operacional completo (ordem de
>    parâmetros, priors) fica para o Capítulo 26, seções 26.1--26.4
>    (também reconstruídas nesta tarefa).
> 3. Confirmar a numeração 25.1--25.7 proposta.

**CAPÍTULO 25**

**CMB + Planck Likelihood**

**25.1 Objetivo do Capítulo**

O Capítulo 24 deixou a TDCP-F1 formalmente implementável em um código
de Boltzmann. Falta agora perguntar, especificamente: o que a TDCP-F1
faz com os observáveis do CMB medidos pelo Planck --- os espectros
TT, TE, EE e o espectro de lentes C_ℓ^{φφ} --- e como isso se degenera
com os parâmetros padrão do ΛCDM (A_s, τ, \sum m_\nu)? Esse diagnóstico
é o que permite, no Capítulo 26, montar a estratégia de ajuste global.

**25.2 Por Que o Espectro Primário Permanece Quase Intacto**

Os Capítulos 9 e 10 já impuseram, como condição de viabilidade, que o
campo primordial não pode destruir o espectro quase invariante de
escala: |P_{\rm TDCP}(k)-P_{\rm obs}(k)|\ll P_{\rm obs}(k) no regime
primordial. Como a modificação de gravidade da TDCP-F1 (as funções
μ, Σ, η_slip) só se torna relevante em k\gtrsim k_\star(a) e em
a\sim\mathcal{O}(1) (tempos tardios --- Capítulos 18--19), a física de
recombinação e o padrão de picos acústicos, que se originam em
z\sim1100, não são afetados diretamente. Isso significa que TT, TE e EE
em multipolos intermediários e altos (l\gtrsim 30, dominados pela
física acústica pré-recombinação) permanecem essencialmente os do
ΛCDM.

**25.3 Onde a TDCP-F1 Realmente Aparece: Baixo l e Lentes**

A modificação tardia da gravidade afeta o CMB por exatamente dois
canais:

1. o efeito Sachs--Wolfe integrado tardio (ISW tardio), que domina o
   espectro TT em baixo l (l\lesssim 30);

2. o espectro de lentes do CMB C_ℓ^{φφ}, que suaviza os picos acústicos
   em TT/TE/EE e é sensível a Σ(k,a) exatamente como o espectro de
   lentes de galáxias (Capítulo 23, §23.5).

**25.4 O Efeito ISW Tardio na TDCP-F1**

A fórmula padrão do ISW tardio é:

$$ \left(\frac{\Delta T}{T}\right)_{\rm ISW} = \int d\eta\; \partial_\eta(\Phi+\Psi)\big(\eta,\,\vec{x}(\eta)\big), $$

integrada ao longo da linha de visada, do último espalhamento até
hoje. Usando Φ+Ψ=2Σ(k,a)Φ_{\rm GR}(k,a) (Capítulos 7, 18, 19):

$$ \partial_\eta(\Phi+\Psi) = 2\Big[\Sigma(k,a)\,\partial_\eta\Phi_{\rm GR}(k,a) \;+\; \Phi_{\rm GR}(k,a)\,\partial_\eta\Sigma(k,a)\Big]. $$

O primeiro termo é o ISW usual (o decaimento de Φ_GR quando a energia
escura passa a dominar), apenas reescalado por Σ. O segundo termo é
**específico da TDCP-F1**: mesmo que Φ_GR fosse exatamente constante, a
própria evolução temporal de Σ(k,a) --- através de m_S(a)=m_{S0}a^{-p}
e do joelho k_\star(a) (Capítulo 18, §18.10) --- gera uma contribuição
adicional ao ISW tardio, concentrada nas escalas onde k\sim k_\star(a)
no intervalo de redshift relevante (tipicamente z\lesssim 2).

**25.5 Impacto no Espectro de Lentes C_ℓ^{φφ}**

O espectro de lentes do CMB segue a mesma integral de Limber do
Capítulo 23 (§23.5), com as fatias de redshift W_i,W_j substituídas
pelo *kernel* de lentes do CMB (fonte em z\simeq1100):

$$ C_\ell^{\phi\phi} = \int_0^{\chi_*} d\chi\; \frac{W_{\rm CMB}^2(\chi)}{\chi^2}\; \Sigma^2\!\left(\frac{\ell}{\chi},z(\chi)\right) P\!\left(\frac{\ell}{\chi},z(\chi)\right). $$

Como Σ(k,a)>1 tipicamente em escalas pequenas e tempos tardios
(Capítulos 18--19), a TDCP-F1 prevê um espectro de lentes do CMB
ligeiramente amplificado em relação ao ΛCDM na mesma região de
parâmetros onde o crescimento de estruturas é amplificado --- a mesma
assinatura de fσ₈(k) do Capítulo 23, vista agora através de um canal
independente.

**25.6 Degenerescências com A_s, τ e \sum m_\nu**

Três degenerescências imediatas precisam ser controladas em qualquer
ajuste:

- **α_0 ↔ A_s**: como o ISW extra (§25.4) e o lensing (§25.5) escalam
  com a amplitude das flutuações, um α_0 maior pode ser parcialmente
  compensado por um A_s menor --- quebrado pela forma *não*
  escala-independente do sinal TDCP (o ΛCDM-A_s reescala P(k)
  uniformemente; a TDCP não).

- **m_{S0} ↔ \sum m_\nu**: neutrinos massivos suprimem o crescimento
  em altas-k de forma monotônica; a TDCP-F1 pode aumentar o
  crescimento em torno de k_\star(a), produzindo um padrão não
  monotônico que os neutrinos sozinhos não reproduzem (mesma
  assinatura antecipada no Capítulo 23, §23.6, detalhada na matriz do
  Capítulo 26, §26.5).

- **τ**: como τ controla a amplitude da reionização e do bump de
  polarização em baixo l, e o ISW tardio também vive em baixo l, os
  dois se misturam estatisticamente em TT --- mas não em EE, onde o
  bump de reionização tem uma assinatura própria em l\sim10 que o ISW
  não produz. EE de baixo l é, portanto, o canal que quebra essa
  degenerescência específica.

**25.7 Conclusão do Capítulo 25**

A TDCP-F1:

- deixa intacto o espectro primário de picos acústicos (TT/TE/EE em
  l intermediário/alto);

- modifica o CMB apenas via ISW tardio (baixo l) e lentes (C_ℓ^{φφ});

- introduz uma contribuição de ISW genuinamente nova, ligada à
  evolução temporal de Σ(k,a), além do ISW usual reescalado;

- tem degenerescências identificáveis e quebráveis com A_s, \sum m_\nu
  e τ, usando canais independentes (forma não escala-independente do
  sinal, padrão não monotônico em k, e EE de baixo l).

**Próximo Passo**

**CAPÍTULO 26 --- Estratégia de Ajuste Global e Matriz de Degenerescências**

onde vamos montar a *likelihood* conjunta (CMB + BAO + RSD + WL) e
consolidar a matriz completa de degenerescências e a região paramétrica
plausível da TDCP-F1.
