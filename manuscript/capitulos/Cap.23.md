> **RASCUNHO RECONSTRUÍDO --- REVISAR**
>
> As seções 23.1--23.10 abaixo não existiam no arquivo original:
> `Cap.23.docx` preservava apenas a seção 23.11 ("Preparação para MCMC") e
> a conclusão do capítulo. A abertura foi reconstruída aqui a partir do
> que o próprio Capítulo 22 já anunciava para o Capítulo 23 ("Modificar
> módulo perturbations.c; Inserir μ(k,a), Σ(k,a); Ajustar equação de
> Poisson; Garantir gauge consistency; Produzir espectro CMB
> preliminar"), sem introduzir física nova: as equações usadas (μ, Σ,
> Poisson modificado, condições de estabilidade) são exatamente as já
> derivadas nos Capítulos 6--21. A estratégia de implementação descrita
> (injetar μ,Σ no setor de perturbações de um código tipo CLASS/CAMB,
> mantendo o background padrão) segue a prática já estabelecida na
> literatura de gravidade modificada para códigos de Boltzmann
> (parametrização tipo PPF / EFT da energia escura, como em hi_class e
> EFTCAMB) --- citada aqui como metodologia de referência, não como
> resultado específico da TDCP.
>
> **O que precisa de validação do autor:**
> 1. Confirmar se o autor pretende de fato basear a implementação em
>    CLASS (código citado no Cap.22) ou se prefere CAMB/outro código ---
>    isso muda detalhes de nomenclatura de módulos (§23.1--23.3).
> 2. §23.4 assume gauge síncrono como *default* do CLASS e apresenta a
>    transformação para o gauge newtoniano usado nos Cap.7--18; isso é
>    convenção padrão do CLASS, mas o autor deve confirmar que não há
>    preferência diferente já implícita em capítulos anteriores.
> 3. §23.8 marca explicitamente que o screening tipo Vainshtein
>    (Cap.19--21) opera em escalas não-lineares/locais fora do regime
>    linear que o CLASS resolve --- isso precisa ser confirmado como a
>    leitura correta antes de qualquer implementação real.
> 4. Nenhuma linha de código foi escrita; o capítulo descreve apenas a
>    arquitetura e os pontos de injeção, como notas de implementação
>    (consistente com o nível dos Capítulos 17--18).

**CAPÍTULO 23**

**Implementação Formal em CLASS**

**23.1 Arquitetura de Injeção: Onde a TDCP Entra em um Código de Boltzmann**

Um código de Boltzmann do tipo CLASS resolve, em sequência, três
blocos: (i) o módulo de fundo (`background.c`), que integra H(a) e as
densidades; (ii) o módulo de perturbações (`perturbations.c`), que
resolve a hierarquia de Einstein-Boltzmann para cada modo k; (iii) o
módulo de espectros (`spectra.c`), que projeta P(k,z) e os C_ℓ a partir
das soluções perturbativas. A TDCP-F1 entra nos três, mas de formas
distintas: no fundo, apenas através de ρ_int(r) (já um termo efetivo
de fluido, Capítulos 5 e 13); nas perturbações, através das funções
μ(k,a) e Σ(k,a) (Capítulos 17--18) na equação de Poisson e na constraint
de anisotropia; nos espectros, apenas como consequência do que já foi
resolvido --- nenhuma modificação adicional é necessária nesse módulo.

**23.2 Módulo de Fundo**

O fundo já está inteiramente especificado pelas equações de Friedmann
duplas do Capítulo 5 e pela redução F1 do Capítulo 13:

$$ 3M_g^2 H_g^2 = \rho_m + \rho_\phi + \rho_{\rm int}^{(g)}(r,\phi). $$

Como o ramo dinâmico (Capítulo 13, §13.4) fixa r(t) e ξ(t) por meio de
H_g=\xi H_f, o módulo de fundo pode ser implementado como um fluido
escuro efetivo com equação de estado w_{\rm eff}(a) tabulada
numericamente a partir de ρ_int(r(a)) --- exatamente como o Capítulo 13
(§13.5) já antecipava para o caso proporcional, generalizado aqui para
o ramo dinâmico completo.

**23.3 Módulo de Perturbações: Pontos de Injeção**

No setor de perturbações, dois pontos precisam de modificação:

1. A equação de Poisson, que em CLASS aparece como uma relação entre o
   potencial métrico e o contraste de densidade total. A substituição
   TDCP é direta:

$$ k^2\Psi = -4\pi G a^2\,\mu(k,a)\,\rho\,\delta \qquad \text{(Capítulo 7, §7.5).} $$

2. A constraint de anisotropia (que relaciona Φ e Ψ), onde entra o
   slip:

$$ \eta_{\rm slip}(k,a) = \Phi/\Psi \qquad \text{(Capítulo 7, §7.8; forma explícita no Capítulo 17, §17.7).} $$

Nenhuma outra equação do setor de perturbações precisa ser alterada: a
hierarquia de Boltzmann para fótons, neutrinos e bárions permanece
padrão, pois esses setores continuam minimamente acoplados à métrica
g_{\mu\nu} (Capítulo 3, §3.4).

**23.4 Convenção de Gauge**

O CLASS resolve as perturbações por padrão no gauge síncrono, enquanto
os Capítulos 7--18 desenvolveram μ, Σ e η_slip no gauge newtoniano
(longitudinal), onde a interpretação física de Φ e Ψ é mais direta. A
tradução entre os dois usa a transformação padrão de gauge da teoria
de perturbações cosmológicas (independente da TDCP): definindo o
potencial síncrono h e o *shift* η_s da métrica síncrona, tem-se

$$ \Psi = \frac{1}{2k^2}\left(\ddot h + 6\ddot\eta_s\right) + \mathcal{H}\,\alpha_T, \qquad \Phi = \eta_s - \mathcal{H}\,\alpha_T, $$

com α_T a variável auxiliar padrão que conecta os dois gauges. Como μ e
Σ foram definidos como razões gauge-invariantes de potenciais
newtonianos (Capítulo 7, §7.5 e §7.8), a substituição acima preserva o
significado físico das duas funções --- este é precisamente o
requisito de "gauge consistency" que o Capítulo 22 exigia deste
capítulo.

**23.5 Verificação de Consistência de Gauge**

Como checagem interna, exige-se que qualquer observável físico (fσ₈,
C_ℓ^{φφ}, P_κ(ℓ)) calculado no gauge síncrono coincida, dentro da
precisão numérica, com o mesmo observável calculado no gauge
newtoniano. Essa invariância é uma propriedade geral de teorias
perturbativas bem-postas e serve aqui como teste de implementação, não
como uma previsão nova da TDCP.

**23.6 Condições Iniciais**

As condições iniciais herdam diretamente o resultado do Capítulo 10: o
modo adiabático domina, com isocurvatura suprimida por m_S^2\gg H^2
no período anterior à entrada no horizonte (Capítulo 14). Isso permite
usar as condições iniciais adiabáticas padrão do CLASS, sem um novo
modo isocurvatura independente a ser propagado.

**23.7 Implementação Numérica da Escala de Transição k_\star(a)**

A função μ(k,a) (Capítulo 17, §17.10) depende de k apenas através da
razão k^2/a^2 comparada a m_S^2(a); numericamente, isso significa
avaliar m_S(a)=m_{S0}a^{-p} e k_\star(a)=a\,m_S(a) em cada passo de
tempo do integrador de perturbações, para cada modo k da grade. Não há
necessidade de resolver uma equação diferencial adicional para μ: ela é
puramente algébrica uma vez conhecidos a(t) e r(t) do módulo de fundo.

**23.8 Regime de Validade: Onde o Screening Não Se Aplica**

O screening tipo Vainshtein (Capítulos 19--21) opera no regime
não-linear, em escalas muito menores que as resolvidas por um código
de Boltzmann linear como o CLASS. O pipeline aqui descrito resolve
apenas o regime linear (k na faixa de LSS/CMB, tipicamente
k\lesssim 0.2\,h\,{\rm Mpc}^{-1}); a supressão de quinta força em
escalas de Sistema Solar (Capítulo 19--20) é uma afirmação separada,
sobre um regime que o CLASS não resolve e que não entra neste pipeline.

**23.9 Saídas: Espectros CMB Preliminares**

Com os pontos de injeção acima, o código produz diretamente:

- os espectros de temperatura e polarização C_ℓ^{TT}, C_ℓ^{TE}, C_ℓ^{EE}
  (afetados apenas indiretamente, via ISW tardio --- ver Capítulo 24);

- o espectro de lente do CMB C_ℓ^{\phi\phi} (afetado por Σ(k,a), como
  qualquer observável de lentes);

- o espectro de matéria P(k,z) e a taxa de crescimento fσ₈(z) (Capítulo
  22, §22.3).

**23.10 Testes de Consistência Antes do Ajuste**

Antes de qualquer ajuste (MCMC), três testes de sanidade são exigidos:

1. no limite α_0→0 (ou m_{S0}\to\infty), todos os espectros devem
   coincidir com o ΛCDM padrão dentro da precisão numérica;

2. a checagem de gauge (§23.5) deve ser satisfeita;

3. os parâmetros usados devem estar dentro da janela de estabilidade e
   screening já delimitada nos Capítulos 6, 19 e 21 (sem fantasma, sem
   gradiente, Higuchi satisfeita, screening solar intacto).

**23.11 Preparação para MCMC**

Agora a teoria é compatível com:

- MontePython

- Cobaya

Conjunto mínimo de parâmetros cosmológicos:

$\{\Omega_b,\Omega_c,H_0,A_s,n_s,\tau,\alpha_0,m_{S0},p,q\}$

**Conclusão do Capítulo 23**

A TDCP-F1 agora:

- Está formalmente implementável em CLASS

- Preserva gauge consistency

- Pode gerar espectros CMB

- Permite comparação com BAO/RSD/WL

- Está pronta para likelihood real

**Próximo Passo**

**CAPÍTULO 24 --- CMB + Planck Likelihood**

onde iremos:

- Analisar impacto detalhado no TT, TE, EE

- Avaliar ISW

- Identificar degenerescências com A_s, \tau, m_\nu

- Definir estratégia de ajuste global
