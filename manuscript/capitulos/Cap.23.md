> **RASCUNHO RECONSTRUÍDO --- REVISAR**
>
> As seções 23.1--23.6 abaixo não existiam no arquivo original: `Cap.23.docx`
> preservava apenas o final do capítulo, a partir do "Diagnóstico importante"
> sobre degenerescência com w₀-wₐ e massa de neutrinos, seguido das seções
> 23.7--23.9 e da conclusão. As aberturas 23.1--23.6 (mapeamento de μ, Σ,
> η_slip em observáveis; fσ₈(z); distâncias BAO; lensing fraco;
> degenerescências) foram reconstruídas aqui **sem introduzir nenhuma
> física nova**: cada função e cada definição usada já havia sido derivada
> nos Capítulos 18, 19 e 22, que também já anunciavam exatamente este
> roteiro ("mapear μ(k,a), Σ(k,a), η_slip da TDCP em observáveis; definir
> funções de crescimento fσ8(z), distâncias BAO, e lensing..."). As
> definições de distância BAO (§23.4) e do espectro de lentes P_κ(l)
> (§23.5) são as definições padrão da cosmologia observacional (não
> específicas da TDCP), aplicadas ao histórico de expansão e ao espectro
> de potência já estabelecidos nos capítulos anteriores.
>
> **O que precisa de validação do autor:**
> 1. Confirmar que a numeração 23.1--23.6 proposta aqui é a pretendida
>    (o próprio Cap.22 só anuncia o conteúdo, não os números de seção).
> 2. §23.4 usa a definição textual padrão de D_V(z) sem repetir a
>    dedução completa de d_A(z) e d_H(z) a partir de H(a) --- decidir se
>    isso deve ser expandido em uma futura revisão.
> 3. §23.5 apresenta a integral de Limber para P_κ(l) na forma padrão
>    (mesma usada em qualquer pipeline ΛCDM/MG); nenhum termo
>    TDCP-específico além de Σ(k,a) foi adicionado --- confirmar que é
>    isso mesmo que o autor pretendia neste nível do capítulo (o
>    detalhamento numérico completo fica para o Cap.24, que trata da
>    implementação em CLASS).
> 4. O cabeçalho "23.6" foi inserido imediatamente antes do parágrafo
>    "Diagnóstico importante..." que já existia no arquivo original,
>    apenas para completar a numeração 23.1--23.9 anunciada; o texto do
>    parágrafo em si não foi alterado.

**CAPÍTULO 23**

**Pipeline Quantitativo BAO + RSD + WL (TDCP-F1)**

**23.1 Objetivo do Capítulo**

Os Capítulos 18--22 estabeleceram o formalismo completo do setor F1 no
regime observacional: a forma Yukawa detectável de μ(k,a), o slip
η_slip(k,a), a função de lentes Σ(k,a), e as condições de estabilidade
e screening que delimitam o espaço de parâmetros viável. Falta agora
reunir essas peças em um pipeline quantitativo --- isto é, converter o
formalismo em previsões numéricas comparáveis a BAO, RSD e *weak
lensing* (WL), e propor a estrutura de um ajuste global (*likelihood*).
Esse é o objetivo deste capítulo, antes de passarmos à implementação
formal em CLASS (Capítulo 24).

**23.2 As Três Funções Efetivas: μ, Σ e η_slip**

Do Capítulo 18, com a parametrização mínima m_S(a)=m_{S0}a^{-p} e
α(a)=α_0 a^q:

$$ \boxed{ \mu(k,a) = 1 + \frac{\alpha(a)\,k^2/a^2}{k^2/a^2 + m_S^2(a)} } $$

$$ \boxed{ \eta_{\rm slip}(k,a) = 1 + \frac{\beta(a)\,k^2/a^2}{k^2/a^2 + m_S^2(a)} } $$

$$ \boxed{ \Sigma(k,a) = \frac{\mu(k,a)}{2}\Big(1+\eta_{\rm slip}^{-1}(k,a)\Big) } $$

com o "joelho" de transição k_\star(a)=a\,m_S(a). Essas três funções são
os únicos ingredientes TDCP-específicos que entram nos observáveis a
seguir: tudo o que vem depois é aparato padrão de cosmologia
observacional aplicado a μ, Σ e η_slip.

**23.3 Crescimento e fσ₈(z)**

Do Capítulo 8, a equação de crescimento modificada é:

$$ \ddot\delta + 2H\dot\delta = 4\pi G\,\mu(k,a)\,\rho\,\delta. $$

Resolvendo numericamente para δ(k,a) e definindo a taxa de crescimento
f(a)=d\ln\delta/d\ln a (Capítulo 8, §8.5), o observável de RSD é:

$$ f\sigma_8(z) \equiv f(z)\,\sigma_8(z), \qquad \sigma_8(z)=\sigma_8\,\frac{D(z)}{D(0)}, $$

com D(a) o fator de crescimento já definido no Capítulo 8. Como μ
depende de k, fσ₈ deixa de ser um único número por redshift e passa a
ser uma família de curvas fσ₈(z;k) --- a "dependência de escala" já
antecipada nos Capítulos 9 e 18--19.

**23.4 Distâncias BAO**

O fundo TDCP-F1 (Capítulos 5 e 14) fornece H(a) a partir da equação de
Friedmann com densidade de interação ρ_int(r). A partir de H(a),
definem-se as distâncias cosmológicas padrão:

$$ D_C(z) = \int_0^z \frac{c\,dz'}{H(z')}, \qquad D_A(z) = \frac{D_C(z)}{1+z}, \qquad D_H(z) = \frac{c}{H(z)}, $$

e a escala de dilatação BAO:

$$ \boxed{ D_V(z) \equiv \left[ (1+z)^2 D_A(z)^2\, c\,z / H(z) \right]^{1/3}. } $$

Como a TDCP-F1 recupera o ΛCDM no limite r=\text{const.} (Capítulo 5,
§5.9), D_V(z) reduz-se à forma padrão nesse limite; o desvio observável
vem inteiramente da modificação de H(a) através de ρ_int(r(a)), não de
um termo novo na própria definição de D_V.

**23.5 Lentes Gravitacionais Fracas: P_κ(ℓ)**

O potencial de lentes é Φ+Ψ=2Σ(k,a)Φ_{\rm GR} (Capítulos 7--19). No
limite de Limber, o espectro de convergência entre duas fatias de
redshift i,j é:

$$ \boxed{ P_\kappa^{ij}(\ell) = \int_0^{\chi_{\rm max}} d\chi\; \frac{W_i(\chi)W_j(\chi)}{\chi^2}\; \Sigma^2\!\left(\frac{\ell}{\chi},z(\chi)\right) P\!\left(\frac{\ell}{\chi},z(\chi)\right), } $$

onde W_i(\chi) são os *kernels* de lentes padrão (distribuição de fontes
e distância) e P(k,z) é o espectro de potência da matéria, já modificado
pelo crescimento G_eff=Gμ (Capítulo 9). O único fator TDCP-específico
inserido na integral é Σ(k,a); o restante é o formalismo padrão de WL.

**23.6 Degenerescências com Parâmetros Cosmológicos Padrão**

Diagnóstico importante:

$$ \boxed{ \text{TDCP pode imitar } w_0-w_a \text{ ou massa de neutrinos.} } $$

Isso significa que o ajuste global precisa incluir:

$\{\Omega_m, H_0, \sigma_8, w_0, w_a, \sum m_\nu\}$

para evitar falso positivo.

**23.7 Pipeline Computacional Proposto**

**Etapa 1 --- Background**

Resolver:

H(a)

com integração numérica.

**Etapa 2 --- Perturbações**

Implementar:

$\mu(k,a),\quad \Sigma(k,a)$

no solver de crescimento.

**Etapa 3 --- Observáveis**

Calcular:

- $f\sigma_8(z)$

- P(k,z)

- $D_V(z)$

- $P_\kappa(l)$

**Etapa 4 --- Likelihood modular**

$$ \mathcal L = \mathcal L_{BAO}\times \mathcal L_{RSD}\times \mathcal L_{WL} $$

**23.8 Intervalos Paramétricos Iniciais**

Com base nos capítulos anteriores:

$m_{S0} \sim 30--300\,H_0$

$\alpha_0 \sim 0.1--1$

$p,q \sim \mathcal{O}(1)$

Isso garante:

- Yukawa entra em k\sim 0.01--0.1\,h\,{\rm Mpc}^{-1}

- Screening solar intacto

- Modificações visíveis em LSS

**23.9 Teste Observacional Crítico**

O sinal característico da TDCP-F1 é:

$\boxed{ \text{Joelho escala-dependente em } f\sigma_8(k) }$

Isso é distintivo comparado a:

- w_0-w_a (escala-independente)

- Neutrinos (suprimem poder em alta-k)

Portanto:

$\boxed{ \text{RSD escala-dependente é o teste mais limpo.} }$

**Conclusão do Capítulo 23**

A TDCP-F1 agora:

- Tem previsão quantitativa para crescimento

- Pode ser confrontada com BAO

- Pode ser testada com WL

- Tem assinatura distintiva em RSD

- Está pronta para implementação em CLASS/CAMB

**Próximo Passo**

**CAPÍTULO 24 --- Implementação formal em CLASS**

onde vamos:

- Modificar módulo perturbations.c

- Inserir \mu(k,a), \Sigma(k,a)

- Ajustar equação de Poisson

- Garantir gauge consistency

- Produzir espectro CMB preliminar
