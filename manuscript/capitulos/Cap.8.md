> **RASCUNHO RECONSTRUÍDO --- REVISAR**
>
> O arquivo `Cap.8.docx` original era uma cópia idêntica de `Cap.7.docx`: o
> Capítulo 8 nunca chegou a ser escrito na sequência numerada em português,
> embora o Capítulo 7 já prometesse seu conteúdo ("CAPÍTULO 8 --- Crescimento
> de Estruturas, Equação para δ e o Papel do Setor Escuro... onde vamos
> derivar: δ̈+2Hδ̇=4πG_eff(k,a)ρδ") e o Capítulo 9 já assumisse esse
> conteúdo como dado ("Como vimos no Capítulo 8: G_eff = Gμ(k,a)").
>
> Esta versão **não foi inventada do zero**: ela traduz e adapta o
> Capítulo 8 real, já escrito e completo, encontrado em
> `Eng Version/CHAPTER 1.docx` (um documento cujo nome sugere conter
> apenas o Capítulo 1, mas que na verdade é uma versão em inglês,
> condensada, dos Capítulos 1 a 14 --- inclusive um Capítulo 8 completo,
> com seções 8.1 a 8.12, que nunca foi portado para a numeração em
> português). A tradução preserva a notação, as equações e a lógica
> exatamente como estão na fonte; nenhuma física nova foi adicionada.
>
> **O que precisa de validação do autor** (ver também `hygiene_log.md`
> e a lista ao final deste arquivo):
> 1. Confirmar que este é de fato o conteúdo pretendido para o Capítulo 8
>    da sequência em português (o título usado aqui é o que o próprio
>    Capítulo 7 já anunciava).
> 2. A equação de crescimento δ̈+2Hδ̇=4πGρδ (§8.2) é apresentada, na
>    fonte em inglês, como válida "em ΛCDM" sem derivação própria dentro
>    deste capítulo -- ela é a equação padrão de crescimento de matéria
>    em RG, apenas com G substituído por G_eff. Isso é consistente com o
>    nível de rigor do Cap.7 (que também introduz G_eff por substituição,
>    não por derivação completa das equações de Einstein perturbadas),
>    mas o autor deve decidir se quer, em uma revisão futura, incluir a
>    derivação completa a partir das equações do Capítulo 6.
> 3. §8.6 cita "Capítulo 6" para os graus de liberdade escalares
>    (ζ, σ, δφ) -- confirmado consistente com a "EXPANSÃO TÉCNICA" do
>    Cap.6.2 e com a definição usada no Cap.7.
> 4. Verificar se o autor quer manter a estrutura em subseções curtas
>    (8.1--8.12, estilo mais telegráfico da fonte em inglês) ou reescrever
>    em prosa mais próxima do estilo narrativo dos Capítulos 1--7.

**CAPÍTULO 8**

**Crescimento de Estruturas, Equação para δ e o Papel do Setor Escuro**

**8.1 Da Gravidade à Formação de Estruturas**

Até este ponto, a TDCP estabeleceu:

- uma cosmologia de fundo consistente,

- um setor perturbativo estável,

- uma equação de Poisson modificada.

Passamos agora à consequência observável central: como crescem as
perturbações de matéria? É isso que os levantamentos observacionais
efetivamente medem, através de:

- aglomeração de galáxias (*galaxy clustering*),

- distorções no espaço de redshift (RSD),

- lentes gravitacionais fracas (*weak lensing*).

**8.2 O Contraste de Densidade e Sua Evolução**

Definimos o contraste de densidade:

$$ \delta = \frac{\delta\rho}{\rho} $$

Para matéria não relativística em um universo em expansão, a equação de
evolução padrão é:

$$ \ddot{\delta} + 2H\dot{\delta} = 4\pi G\rho\delta $$

Essa é a forma válida em RG sob as hipóteses do ΛCDM. Na TDCP, a
gravidade é modificada.

**8.3 Incorporando a Gravidade Efetiva**

Do Capítulo 7:

$$ G \rightarrow G_{\text{eff}}(k,a) = G\,\mu(k,a) $$

Assim, a equação de crescimento torna-se:

$$ \ddot{\delta} + 2H\dot{\delta} = 4\pi G_{\text{eff}}(k,a)\,\rho\delta $$

ou, equivalentemente:

$$ \ddot{\delta} + 2H\dot{\delta} = 4\pi G\,\mu(k,a)\,\rho\delta $$

Esta é a equação-chave que conecta a TDCP às observações.

**8.4 Interpretação Física de μ(k,a)**

A função μ(k,a) codifica:

- dependência de escala (k),

- evolução temporal (a).

Do Capítulo 7:

$$ \mu(k,a) = 1 + \frac{\Delta_\sigma}{1 + m_\sigma^2 a^2/k^2} + \frac{\Delta_\phi}{1 + m_\phi^2 a^2/k^2} $$

Isso leva a:

- em escalas pequenas, μ→1 e a RG é recuperada;

- em escalas grandes, μ≠1 e o crescimento é modificado.

**8.5 Taxa de Crescimento e Quantidades Observáveis**

Define-se o fator de crescimento:

$$ D(a) = \frac{\delta(a)}{\delta(a_{\text{inicial}})} $$

e a taxa de crescimento:

$$ f(a) = \frac{d\ln\delta}{d\ln a} $$

Observacionalmente, os levantamentos medem a combinação fσ_8, que
combina o crescimento com a normalização das flutuações. A TDCP
modifica essa quantidade através de G_eff.

**8.6 Impacto do Setor Escalar**

Do Capítulo 6, os graus de liberdade escalares são:

$$ (\zeta,\ \sigma,\ \delta\phi) $$

Seu efeito sobre o crescimento de estruturas é:

- σ modifica o agrupamento gravitacional (*clustering*);

- δφ introduz dependência de escala adicional.

Assim, a formação de estruturas não é governada apenas pela matéria ---
ela é influenciada pelo setor estrutural.

**8.7 Equação de Crescimento Modificada na Prática**

No espaço de Fourier:

$$ \ddot{\delta}_k + 2H\dot{\delta}_k = 4\pi G\,\mu(k,a)\,\rho\,\delta_k $$

Isso implica que o crescimento passa a depender da escala: diferentes
modos k evoluem de maneira diferente. Essa é uma assinatura
observacional chave.

**8.8 Relação com Matéria Escura e Energia Escura**

No ΛCDM: a matéria escura impulsiona o *clustering*; a energia escura
impulsiona a aceleração.

Na TDCP: o setor estrutural modifica a gravidade; o campo primordial
contribui dinamicamente.

Assim, parte do que interpretamos como "matéria escura" ou "energia
escura" pode ser uma manifestação efetiva do acoplamento estrutural
entre os dois setores.

**8.9 Consistência com Observações**

Para que a TDCP seja viável:

1. em escalas pequenas, μ(k,a)→1;

2. a taxa de crescimento deve corresponder ao fσ_8 observado;

3. não deve haver dependência de escala excessiva em conflito com os
   dados;

4. deve haver compatibilidade com lentes gravitacionais (via Φ+Ψ).

**8.10 Condições de Estabilidade Revisitadas**

Todos os resultados acima dependem das condições do Capítulo 6:

- ausência de fantasma: **K**>0;

- ausência de instabilidade de gradiente: c_s²>0;

- ausência de taquion no regime tardio: m²>0;

- condição de Higuchi: m_T²≥2H².

Sem essas condições, as previsões de crescimento não têm significado
físico.

**8.11 Interpretação Conceitual**

A formação de estruturas na TDCP pode ser interpretada como matéria
evoluindo dentro de um sistema geométrico dinamicamente acoplado. A
"gravidade extra" não é uma força externa: é a manifestação da
interação estrutural entre os dois regimes.

**8.12 Resultado Final do Capítulo 8**

Concluímos que:

- a TDCP prevê crescimento modificado de estruturas;

- a equação-chave é:

$$ \ddot{\delta} + 2H\dot{\delta} = 4\pi G_{\text{eff}}(k,a)\,\rho\delta $$

- o crescimento é dependente de escala;

- a RG é recuperada localmente;

- os desvios aparecem em escalas cosmológicas.

O próximo capítulo natural é:

**CAPÍTULO 9 --- Espectro de Potência, Função de Transferência e Assinaturas Observacionais**

que já assume as duas relações centrais estabelecidas aqui: a equação
de crescimento modificada e a substituição G→G_eff=Gμ(k,a).
