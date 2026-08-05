Diagnóstico importante:

\boxed{ \text{TDCP pode imitar } w_0-w_a \text{ ou massa de neutrinos.} }

Isso significa que o ajuste global precisa incluir:

$$ \{\Omega_m, H_0, \sigma_8, w_0, w_a, \sum m_\nu\} $$

para evitar falso positivo.

**22.7 Pipeline Computacional Proposto**

**Etapa 1 --- Background**

Resolver:

H(a)

com integração numérica.

**Etapa 2 --- Perturbações**

Implementar:

$$ \mu(k,a),\quad \Sigma(k,a) $$

no solver de crescimento.

**Etapa 3 --- Observáveis**

Calcular:

$$ - f\sigma_8(z) $$

- P(k,z)

$$ - D_V(z) $$

$$ - P_\kappa(l) $$

**Etapa 4 --- Likelihood modular**

$$ \mathcal L = \mathcal L_{BAO}\times \mathcal L_{RSD}\times \mathcal L_{WL} $$

**22.8 Intervalos Paramétricos Iniciais**

Com base nos capítulos anteriores:

$$ m_{S0} \sim 30--300\,H_0 $$

$$ \alpha_0 \sim 0.1--1 $$

$$ p,q \sim \mathcal{O}(1) $$

Isso garante:

- Yukawa entra em k\sim 0.01--0.1\,h\,{\rm Mpc}^{-1}

- Screening solar intacto

- Modificações visíveis em LSS

**22.9 Teste Observacional Crítico**

O sinal característico da TDCP-F1 é:

\boxed{ \text{Joelho escala-dependente em } f\sigma_8(k) }

Isso é distintivo comparado a:

- w_0-w_a (escala-independente)

- Neutrinos (suprimem poder em alta-k)

Portanto:

\boxed{ \text{RSD escala-dependente é o teste mais limpo.} }

**Conclusão do Capítulo 22**

A TDCP-F1 agora:

✔ Tem previsão quantitativa para crescimento

✔ Pode ser confrontada com BAO

✔ Pode ser testada com WL

✔ Tem assinatura distintiva em RSD

✔ Está pronta para implementação em CLASS/CAMB

**Próximo Passo**

**CAPÍTULO 23 --- Implementação formal em CLASS**

onde vamos:

- Modificar módulo perturbations.c

- Inserir \mu(k,a), \Sigma(k,a)

- Ajustar equação de Poisson

- Garantir gauge consistency

- Produzir espectro CMB preliminar

Se quiser seguir: diga "Cap.23".
