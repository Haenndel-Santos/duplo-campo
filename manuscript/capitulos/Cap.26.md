> **RASCUNHO RECONSTRUÍDO --- REVISAR (seções 26.1--26.4 apenas)**
>
> `Cap.26.docx` era idêntico a `Cap.25.docx`: trazia apenas a repetição
> do fim do Capítulo 24 seguida diretamente das seções 26.5--26.8. As
> seções 26.5--26.8 abaixo **são o texto original, preservado sem
> nenhuma alteração de conteúdo** (apenas o preâmbulo duplicado do
> Capítulo 24 foi removido, já que pertence a este arquivo por engano).
> As seções 26.1--26.4, que faltavam, foram reconstruídas a partir do
> que o Capítulo 25 (também reconstruído nesta tarefa) já anuncia como
> próximo passo --- montar a *likelihood* conjunta e a estratégia de
> ajuste --- usando apenas elementos já estabelecidos: a decomposição
> modular L=L_BAO×L_RSD×L_WL do Capítulo 23, os canais de CMB do
> Capítulo 25, e o conjunto de parâmetros e intervalos já delimitados
> nos Capítulos 14--23.
>
> **O que precisa de validação do autor:**
> 1. §26.4 propõe uma ordem específica de ajuste (primeiro fixar a
>    linha de base ΛCDM, depois variar os parâmetros TDCP-específicos
>    com prior informado pela janela de estabilidade/screening); isso é
>    uma escolha metodológica razoável mas não a única possível --- o
>    autor pode preferir um ajuste conjunto sem hierarquia desde o
>    início.
> 2. Confirmar que a matriz de degenerescências original (§26.5, texto
>    preservado) é consistente com a análise de degenerescências do
>    Capítulo 25 (§25.6) --- ambas foram cruzadas nesta reconstrução e
>    não apresentam contradição aparente, mas vale checagem do autor.

**CAPÍTULO 26**

**Estratégia de Ajuste Global e Matriz de Degenerescências**

**26.1 Objetivo: da Análise de Canais à Likelihood Conjunta**

Os Capítulos 23 e 25 identificaram, separadamente, como a TDCP-F1 afeta
BAO, RSD, WL (Capítulo 23) e CMB via ISW tardio e lentes (Capítulo 25).
Isoladamente, nenhum desses canais fixa os quatro parâmetros
TDCP-específicos (m_{S0},\alpha_0,p,q); juntos, e explorando exatamente
as degenerescências que cada canal quebra de forma diferente
(Capítulo 25, §25.6), eles permitem um ajuste global bem posto. Este
capítulo monta essa *likelihood* conjunta e consolida a matriz de
degenerescências e a região paramétrica plausível.

**26.2 Estrutura da Likelihood Conjunta**

Estendendo a decomposição modular do Capítulo 23 (§23.7, Etapa 4) para
incluir o CMB do Capítulo 25:

$$ \boxed{ \mathcal{L}_{\rm total} = \mathcal{L}_{\rm CMB}\times\mathcal{L}_{BAO}\times\mathcal{L}_{RSD}\times\mathcal{L}_{WL}, } $$

com \mathcal{L}_{\rm CMB} a *likelihood* padrão do Planck (TT, TE, EE e
lentes, tipicamente aproximada por um conjunto de espectros gaussianos
com covariância própria) avaliada nos espectros que o pipeline do
Capítulo 24 produz. Cada fator usa o mesmo conjunto de parâmetros
cosmológicos de fundo (\Omega_b,\Omega_c,H_0,A_s,n_s,\tau) e os quatro
parâmetros TDCP-específicos (m_{S0},\alpha_0,p,q) do Capítulo 24,
§24.11.

**26.3 Priors e Hierarquia de Parâmetros**

Dois grupos de parâmetros entram na *likelihood* com papéis distintos:

- os parâmetros de fundo (\Omega_b,\Omega_c,H_0,A_s,n_s,\tau) recebem
  priors largos, padrão de análises ΛCDM (consistentes com Planck);

- os parâmetros TDCP-específicos (m_{S0},\alpha_0,p,q) recebem priors
  restritos à janela já delimitada nos capítulos anteriores: screening
  solar seguro e estabilidade linear/não-linear (Capítulos 6, 20--22)
  e o intervalo observacionalmente interessante do Capítulo 23, §23.8
  (m_{S0}\sim30\text{--}300\,H_0,\ \alpha_0\sim0.1\text{--}1,\
  p,q\sim\mathcal{O}(1)). Priors fora dessa janela correspondem a
  pontos já excluídos por consistência interna, não por dados.

**26.4 Protocolo de Ajuste Proposto**

Um protocolo em duas etapas evita que a alta dimensionalidade do
espaço conjunto esconda as degenerescências identificadas no
Capítulo 25:

1. **Linha de base:** ajustar (\Omega_b,\Omega_c,H_0,A_s,n_s,\tau) ao
   Planck com a TDCP desligada (\alpha_0\to0), fixando a referência
   ΛCDM;

2. **Ajuste conjunto:** variar todos os parâmetros simultaneamente em
   \mathcal{L}_{\rm total}, usando a linha de base como ponto de
   partida, e monitorando explicitamente as três degenerescências do
   Capítulo 25 (§25.6) através dos canais que as quebram (forma do
   sinal em P(k), padrão não monotônico em k, EE de baixo l).

O restante deste capítulo (§26.5--26.8) consolida essa análise em uma
matriz de degenerescências e em um diagnóstico final de
falsificabilidade.

**26.5 Matriz de Degenerescências Principais**

**1. \alpha_0 ↔ A_s**

Aumento em \alpha_0 aumenta crescimento.

Pode ser compensado reduzindo A_s.

Quebra:

- Lensing CMB

- WL

**2. m_{S0} ↔ \sum m_\nu**

Neutrinos suprimem crescimento em altas-k.

TDCP pode:

- aumentar crescimento em certas escalas

- criar padrão não monotônico

Assinatura distintiva:

$\text{joelho escala-dependente em } f\sigma_8(k)$

**3. p,q ↔ w_0-w_a**

Evolução temporal pode imitar DE dinâmica.

Quebra:

- RSD escala-dependente

- combinação BAO + WL

**4. \beta_0 ↔ Slip degeneracy**

Afeta WL mais que RSD.

**26.6 Região Paramétrica Plausível (Diagnóstico Atual)**

Com base nos capítulos anteriores:

- $m_{S0} \sim 30--300 H_0$

- $\alpha_0 \sim 0.1--0.5$

- $p \sim 0--1$

- $q \sim 0--1$

Região onde:

- Solar screening seguro

- LSS modificável

- CMB primário quase intacto

- Lensing alterável

**26.7 Falsificabilidade Clara**

A TDCP-F1 pode ser falsificada se:

1. Não for possível reproduzir simultaneamente:

$> C_\ell^{\phi\phi} \text{ e } f\sigma_8(z)$

2. O joelho escala-dependente não aparecer.

3. O ajuste exigir:

$> \alpha_0 \to 0$
>
> consistentemente com todos os dados.

**26.8 Diagnóstico Estratégico Final**

A TDCP-F1 agora:

- Passou no teste solar

- É não-linearmente estável

- É implementável numericamente

- Tem assinatura observacional distintiva

- Pode ser ajustada globalmente

Isso significa:

$$ \boxed{ \text{A teoria está em nível de confronto observacional real.} } $$

**Próximo Movimento Científico Real**

Agora existem três caminhos possíveis:

**Caminho A --- Rodar MCMC real**

Produzir constraints quantitativos.

**Caminho B --- Procurar assinatura analítica fechada**

Encontrar relação fechada entre:

$S_8 \text{ e } \alpha_0,m_{S0}$

**Caminho C --- Publicação técnica estruturada**

Organizar como:

- Paper 1: Fundamentos + screening

- Paper 2: Cosmologia linear + dados

- Paper 3: Extensões (não-linear LSS)

**Estado Final Atual da TDCP-F1**

A teoria saiu de:

Ideia conceitual

para

Modelo gravitacional consistente, implementável e falsificável.
