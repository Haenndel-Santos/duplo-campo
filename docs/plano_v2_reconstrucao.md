# TDCP v2 — Plano de Reconstrução Derivacional com Gates

Data: 2026-08-06. Base: `auditoria/parecer_tecnico.md` (auditoria das
856 equações), `derivations/00_indice.md` (âncoras D1–D8).

## Princípio que organiza tudo

A v1 foi construída na ordem: **assinatura desejada → equação que a
produz**. Foi isso que gerou o Cap.18 (32 erros em 48) e o Cap.19
(faixa m_S0 obtida por inversão do resultado desejado).

A v2 inverte: **ação → derivação → observável → interpretação**. A
interpretação filosófica é a *última* coisa escrita, e descreve o que
foi derivado — não o contrário.

## Regra dos gates

Cada passo tem um **gate** com quatro campos obrigatórios:

| Campo | O que especifica |
|---|---|
| **Critério** | A condição matemática precisa que decide passa/não-passa |
| **Nível exigido** | O grau de evidência aceitável (ver estratificação abaixo) |
| **Como testar** | Método concreto e artefato produzido |
| **Se falhar** | A ação definida — não "repensar", mas *o que* repensar |

**Nenhum passo começa antes do gate anterior fechar.** Um gate aberto
não é motivo para avançar "provisoriamente" — foi exatamente assim que
o Cap.14 §14.12 contornou ṙ=0 e produziu 11 equações erradas em
cascata.

### Níveis de evidência (de `parecer_tecnico.md`, Parte III-B)

- **Nível 1** — álgebra fechada, verificável à mão, sem código.
- **Nível 2a** — derivação simbólica válida para *todos* os parâmetros.
- **Nível 2b** — benchmark ou grade: válido *onde foi testado*, com
  cobertura declarada.
- **Nível 3** — juízo interpretativo. **Nunca suficiente para passar um
  gate.**

A regra dura: **gates de consistência estrutural exigem Nível 1 ou 2a.**
Um benchmark não pode provar ausência de fantasma no espaço de
parâmetros — só pode encontrar um. Gates de *existência* (há região
viável?) podem passar em 2b, com a cobertura declarada.

---

## Ativos que atravessam da v1

Isto não se reconstrói — importa-se, com a correção indicada:

| Ativo | Origem | Estado |
|---|---|---|
| Formalismo HR (ξ, r, K, e_n) | Anexo A | Limpo, 30/30 — usar como está |
| Redução minisuperespaço | Anexo B §B.4 | Limpo, verificado termo a termo |
| Friedmann do setor f | Anexo B §B.6 | Limpo |
| ṙ≡0 no ramo H=ξH_f | Anexo B §B.9 / D5 | Nível 1 — é o resultado que motiva a v2 |
| ρ_int com regra da cadeia completa | D3 | Nível 2a — substitui Anexo B §B.5 |
| m_T² com ξ (forma fechada) | D2 | Nível 2a — substitui Cap.16 e Anexo D §D.5 |
| Ação tensorial + base ponderada | Anexo D §D.3/§D.4 | Confirmada por D2 |
| Fundo F1, r★, U(r★) | Cap.14 (fora do cluster) | Verificado |
| Bloco Vainshtein/PPN | Cap.20–22 | Aritmética confirmada; **coeficientes a derivar** (Passo 8) |
| Implementação CLASS, ISW | Cap.24–25 | Limpo |
| Biblioteca de perturbações | `derivations/code/tdcp_pert_lib.py` | Auto-testes GR embutidos — reusar |
| Previsão n_σ−1≈−(2/3)\|m_σ²\|/H² | D7 | Ganho líquido da v1 |

---

# Passo 0 — Dicionário de símbolos

Antes de qualquer equação. A auditoria encontrou sobrecarga em **oito**
símbolos (r, ξ, η, Φ/Ψ, ζ, U, F, Γ), e três delas produziram erros
reais, não só confusão.

**Entregável:** uma tabela única — símbolo, significado, dimensão,
seção onde é definido — em que cada símbolo aparece **uma vez**.

### Gate 0
- **Critério:** nenhum símbolo com dois significados no corpus v2.
- **Nível exigido:** 1 (verificação mecânica).
- **Como testar:** script que extrai todo símbolo em `$...$` e reporta
  colisões contra a tabela.
- **Se falhar:** renomear antes de prosseguir. Custo de renomear agora:
  minutos. Custo de renomear depois de 20 capítulos: a v1.

---

# Passo 1 — A ação mínima

Escrever **uma** ação, completa, com todos os termos explícitos.
Proposta de arquitetura (a ser confirmada nos gates seguintes):

$$S = \frac{M_g^2}{2}\!\int\!\sqrt{-g}R[g] + \frac{M_f^2}{2}\!\int\!\sqrt{-f}R[f] - m^2M_{\rm eff}^2\!\int\!\sqrt{-g}\sum_{n=0}^{4}\beta_n(\phi_-)\,e_n(\mathcal K) + S_{\phi_\pm} + S_m[g,\psi]$$

com $\phi_\pm=(\phi_1\pm\phi_2)/\sqrt2$ e o potencial **explícito**:

$$V(\phi_+,\phi_-) = V_+(\phi_+) - \tfrac{1}{2}\mu_-^2\phi_-^2 + \tfrac{1}{4}\lambda_-\phi_-^4 + \lambda_c\phi_+^2\phi_-^2$$

cuja massa efetiva do modo diferencial é

$$\frac{\partial^2V}{\partial\phi_-^2}\bigg|_{\phi_-=0} = -\mu_-^2 + 2\lambda_c\phi_+^2$$

(o fator 2 vem da derivada segunda de $\phi_-^2$ no termo de portal;
o ponto crítico é $\phi_{+,\rm crit}^2=\mu_-^2/(2\lambda_c)$).

**Duas escolhas de arquitetura que este passo fixa:**

1. **A modulação é em β_n(φ₋), não em M²(φ).** Massas de Planck
   dependentes de campo são mais agressivas e arriscam a prova de
   ghost-freedom sem necessidade; e a rota usual de escapar para o
   frame de Einstein está bloqueada, porque reescalar $g$ muda
   $\sqrt{g^{-1}f}$ e portanto o potencial inteiro. Escalar para M²(φ)
   só se o Gate 3 falhar por insuficiência de β_n(φ).
2. **O campo que modula é φ₋, o modo diferencial da bifurcação.** Isto
   costura a cadeia que a v1 nunca fechou: a bifurcação de φ₋ *é* o que
   move os β_n, que move r★, que produz a separação estrutural. Na v1,
   Φ₁/Φ₂ (Cap.1) e φ/χ (ação HR) nunca foram relacionados.

### Gate 1
- **Critério:** (a) toda constante com dimensão declarada e todo termo
  dimensionalmente homogêneo; (b) simetrias declaradas — invariância de
  difeo e a Z₂ em φ₋ que a bifurcação quebra; (c) $V(\phi_+,\phi_-)$
  escrito explicitamente, fechando o achado A7 (a v1 nunca especificou
  V(Φ±), o que deixava $m_-^2<0$ como hipótese); (d) $\beta_n(\phi_-)$
  com forma funcional explícita, não abstrata; (e) reduz a HR padrão
  quando $\phi_-$ = const.
- **Nível exigido:** 1.
- **Como testar:** conferência dimensional termo a termo; verificação
  do limite $\phi_-\to$ const.
- **Se falhar:** o modo mais provável de falha é (d) fighting (c) — não
  existir uma $\beta_n(\phi_-)$ que simultaneamente admita bifurcação e
  mantenha os β_n em faixa fisicamente sensata. Nesse caso, φ₋ não é o
  modulador certo: testar φ₊, ou um terceiro campo, e reabrir a escolha
  de arquitetura 2.

---

# Passo 2 — Ghost-freedom sob β_n(φ)

**O gate mais crítico do plano.** Toda a arquitetura depende dele.

A prova de Hassan–Rosen de ausência do fantasma de Boulware–Deser
depende da estrutura do potencial na análise ADM — especificamente, de
o potencial ser **linear no lapso** do setor g, o que gera a constraint
primária que remove o sexto grau.

**Argumento a priori favorável:** $\beta_n(\phi_-)$ multiplica
$e_n(\mathcal K)$, que é quem carrega a estrutura de lapso; e $\phi_-$
não contém derivadas do lapso. A linearidade em $N_g$ é, portanto,
intocada. Isso torna a passagem *provável* — mas provável não é provado,
e é exatamente esse tipo de "obviamente sobrevive" que produziu metade
dos erros da v1.

### Gate 2
- **Critério:** a constraint primária que remove o modo BD persiste com
  $\beta_n$ dependente de campo, e a contagem de graus de liberdade é
  exatamente 2 (massless) + 5 (massivo) + 2 (φ₊, φ₋) = 9. Nenhum modo
  extra.
- **Nível exigido:** **2a — obrigatoriamente.** Um benchmark pode
  *encontrar* um fantasma, nunca provar sua ausência no espaço de
  parâmetros.
- **Como testar:** (i) análise ADM analítica da linearidade em $N_g$;
  (ii) corroboração numérica independente — contagem de modos físicos
  no espectro perturbativo em vários fundos, reusando a maquinaria da
  D1 (o auto-teste GR já embutido: 1 modo, $c_s^2=+1.000000$).
- **Se falhar:** duas saídas, nesta ordem. **(a)** Restringir a classe
  de $\beta_n(\phi_-)$ à subclasse que preserva a estrutura — pode
  existir uma condição do tipo "só combinações que mantêm $\sum$
  linear no lapso". **(b)** Se não houver subclasse viável, abandonar a
  modulação de β_n e buscar outro mecanismo de evolução estrutural —
  nesse ponto, reavaliar honestamente se a TDCP é separável da
  gravidade bimétrica padrão.

---

# Passo 3 — Fundo e a raiz móvel

Derivar o fundo com $\beta_n(\phi_-(t))$ no **ramo algébrico**:

$$\mathcal B(r,t) \equiv \beta_1(\phi_-) + 2\beta_2(\phi_-)r + \beta_3(\phi_-)r^2 = 0 \;\Rightarrow\; r_\star = r_\star(\phi_-(t))$$

Este é o coração da v2: é aqui que a separação estrutural passa a
evoluir de fato, resolvendo o que o ramo dinâmico não entregou.

**Cuidado específico, herdado do erro do Cap.14 §14.12:** satisfazer
$\mathcal B=0$ instantaneamente não basta. A derivada temporal da
constraint precisa ser consistente com as equações de movimento — o
sistema não pode ficar sobredeterminado. Foi exatamente ao trocar uma
constraint por outra não-equivalente que a v1 gerou 11 equações erradas.

### Gate 3
- **Critério:** (a) $\dot r_\star \neq 0$ com $|\dot r_\star/r_\star|$
  da ordem de $H$ na época relevante — se for ordens de grandeza abaixo,
  o mecanismo existe mas não faz nada; (b) $d\mathcal B/dt=0$
  compatível com as EOM, sem sobredeterminação; (c) adiabaticidade
  $|\dot\beta_n/\beta_n| \ll H$ no regime de interesse; (d) $H(z)$
  compatível com ΛCDM dentro das barras atuais no tardio.
- **Nível exigido:** 1 para (b) — é álgebra e é onde a v1 tropeçou;
  2b para (a), (c), (d) — integração numérica com cobertura declarada.
- **Como testar:** derivação à mão de (b); integração do sistema em
  $N=\ln a$ reusando a estrutura do Anexo E (que é limpa), com o sinal
  da equação de χ **corrigido**.
- **Se falhar:** em (a), a modulação é lenta demais → revisar a forma
  de $\beta_n(\phi_-)$ ou a dinâmica de φ₋ (potencial mais íngreme). Em
  (b), há sobredeterminação → o ramo algébrico com β_n(t) não é
  consistente, e a arquitetura precisa de outro mecanismo. Em (c),
  perde-se o controle adiabático → o setor de perturbações não pode ser
  tratado com coeficientes lentamente variáveis, encarecendo tudo
  adiante.

---

# Passo 3.5 — Pré-triagem de Higuchi (fail fast)

**Gate barato inserido de propósito antes do passo caro.** A D8
encontrou Higuchi violado em **60/60** pontos da grade com o $m_T^2$
real. Esse é o resultado mais preocupante de toda a auditoria, e não
faz sentido investir no setor escalar (Passo 4, caro) antes de saber se
o tensorial sobrevive no fundo novo.

Usar a forma fechada da D2 (Nível 2a, válida para todos os parâmetros):

$$m_T^2 = m^2F M_{\rm eff}^2\left(\frac{1}{M_g^2}+\frac{\xi}{M_f^2r^3}\right)r\big[\beta_1+\beta_2(\xi+r)+\beta_3\xi r\big]$$

avaliada no fundo do Passo 3.

### Gate 3.5
- **Critério:** $m_T^2 > 0$ **e** $m_T^2 \geq 2H^2$ durante a época
  acelerada.
- **Nível exigido:** 2b, com a faixa de β_n varrida declarada.
- **Como testar:** plug direto — o Passo 3 dá $r(t), \xi(t), F(t)$; a
  D2 dá a fórmula. Custo: horas, não semanas.
- **Se falhar:** três investigações, nesta ordem. **(a)** Existe região
  de β_n onde $\beta_1+\beta_2(\xi+r)>0$ com margem? A v1 falhou com
  $\beta_1+\beta_2(\xi+r)=1-0.4(4.7)=-0.88$ — o problema foi ξ grande
  no ramo dinâmico; no ramo algébrico ξ pode ser muito menor, o que
  muda o quadro qualitativamente. **(b)** O bound de Higuchi na forma
  $m^2\geq2H^2$ é derivado para massa **constante** em dS exato. Com
  $m_T^2(t)$ variando, há correções — verificar se o bound aplicável é
  o mesmo. Isto é questão técnica legítima, não evasão. **(c)** Se nem
  (a) nem (b) salvarem, este é o ponto de parada mais provável do
  programa, e deve ser relatado como tal.

---

# Passo 4 — Setor escalar: fantasma e gradiente

Refazer a análise da D1 **sem** a aproximação de fundo congelado, que
era seu principal caveat, e com a raiz móvel.

**Sub-questão crítica, nova:** a D1 mostrou que **na raiz exata** o par
relativo degenera ($k_N\sim10^{-16}$: fortemente acoplado,
não-propagante na ordem quadrática). Isso significa que o modelo
provavelmente precisa viver **perto** da raiz, não **sobre** ela — mas
o ramo algébrico é definido *por estar* sobre ela. Essa tensão precisa
ser resolvida explicitamente, não contornada.

### Gate 4
- **Critério:** (a) matriz cinética $K$ positiva definida ao longo de
  toda a trajetória; (b) $c_s^2>0$ para todos os modos; (c) nenhuma
  instabilidade taquiônica com taxa maior que $H$; (d) **corredor
  seguro definido** — o menor $|\mathcal B|$ que mantém $K$
  não-degenerada, e demonstração de que a trajetória fica nele.
- **Nível exigido:** 2a para (a) se possível; 2b com cobertura
  declarada e **justificativa da amostragem** se não for.
- **Como testar:** reusar `tdcp_pert_lib.py` com coeficientes
  dependentes do tempo; manter os auto-testes GR embutidos como
  calibração.
- **Se falhar:** em (d) — se não existir corredor, ou seja, se a
  degenerescência for inescapável no ramo algébrico — voltar ao Passo 1
  e reconsiderar: talvez a teoria precise estar **fora** de ambos os
  ramos, o que exige aceitar $\mathcal B\neq0$ e $H\neq\xi H_f$
  simultaneamente, com um termo de fonte que absorva a inconsistência
  de Bianchi. Isso seria uma mudança estrutural séria e deve ser
  declarada como tal.

---

# Passo 5 — Setor tensorial completo

Com Higuchi já pré-triado no 3.5, aqui é a análise completa: velocidades
de propagação, o cone causal $c_f^2=\xi^2/r^2$, e a condição sob a qual
o modo massless propaga em $c=1$.

### Gate 5
- **Critério:** (a) $c_T=1$ para o modo observável dentro de
  $|c_T-1|<10^{-15}$ (GW170817) — o que, pela D2, exige declarar o
  regime, porque $c_g^2=1$ mas $c_f^2=\xi^2/r^2$ e os dois setores não
  são simultaneamente diagonalizáveis em geral; (b) nenhum modo
  tensorial fantasma.
- **Nível exigido:** 2a (a D2 já é forma fechada).
- **Se falhar:** em (a), a única saída conhecida é $\xi\approx r$ na
  época observável — verificar se o fundo do Passo 3 a satisfaz
  naturalmente ou se exige tuning. Se exigir tuning fino, isso deve
  entrar como custo declarado da teoria.

---

# Passo 6 — Existe região viável?

O sucessor do scan 0/60 da D8, agora com tudo acima derivado.

### Gate 6
- **Critério:** interseção **não-vazia** de: fundo viável + cinética
  escalar positiva + Higuchi + EFT controlada ($H\ll\Lambda_3$) +
  screening solar.
- **Nível exigido:** 2b — um scan é amostragem por natureza. Mas a
  cobertura precisa ser honesta: faixas declaradas, resolução
  declarada, e as formas de $V_+$, $\beta_n(\phi_-)$ fixadas
  explicitamente. A D8 falhou com 60 pontos e formas específicas; um
  scan sério precisa de ordens de magnitude a mais.
- **Se falhar:** com scan genuinamente amplo e região vazia, isto é o
  no-go prático da arquitetura. **Relatar como resultado**, não como
  fracasso — "esta classe de modelos não admite região viável" é uma
  contribuição científica publicável, e é mais do que a v1 sabia.

---

# Passo 7 — Observáveis derivados

**Só agora.** Calcular $\mu(k,a)$, $\Sigma$, $\eta_{\rm slip}$ das
equações de perturbação reais. Nenhum ansatz.

### Gate 7
- **Critério:** (a) $\alpha_\infty=0$ recuperado — GR automática em
  pequenas escalas, que a D6 já indicou ser propriedade da estrutura;
  (b) a assinatura é **computada**, não escolhida; (c) distinguível de
  ΛCDM e de $w_0w_a$ na precisão de Euclid/DESI/LSST; (d) $\Sigma$
  calculado com a fórmula **correta**, $\Sigma=(\mu/2)(1+\eta_{\rm slip})$
  — a v1 usou $\eta_{\rm slip}^{-1}$ em quatro lugares.
- **Nível exigido:** 2b com benchmarks dentro da região do Gate 6.
- **Se falhar:** em (c), a teoria é viável mas indistinguível → isso é
  um resultado legítimo e deve ser publicado como tal, não escondido.
  Nesse caso o valor da TDCP passa a ser conceitual (mecanismo de
  bifurcação), não observacional.

---

# Passo 8 — Bloco solar com coeficientes derivados

O Cap.20–22 é o ativo mais forte da v1, mas **postula** $Z$, $c_3$ e
$\alpha_V$ por analogia com dRGT. Aqui eles passam a ser derivados dos
$\beta_n$ reais via Stückelberg.

### Gate 8
- **Critério:** com $Z, c_3, \alpha_V$ derivados: $r_V \gg 1$ AU,
  $|\gamma-1|<2.3\times10^{-5}$ (Cassini), e $c_3/Z>0$ (ramo saudável
  do Cap.22). Adicionalmente: resolver a pendência de
  $Z_t$/$Z_r$/$Z_\Omega$ do Cap.22 §22.5 — o script
  `auditoria/code/lote05_C22_galileon_stability.py` já existe.
- **Nível exigido:** 2a para os coeficientes derivados; 1 para a
  aritmética de $r_V$ (já verificada na v1, com margem de 2–3 ordens).
- **Se falhar:** se os coeficientes derivados derem $r_V$ pequeno
  demais, o screening deixa de funcionar e a teoria falha o teste
  solar — que a v1 passava apenas por importar coeficientes de outra
  teoria. Seria uma falha grave e honesta.

---

# Passo 9 — O destino de η

**Só depois de 1–8.** Duas saídas possíveis, e a decisão deve ser
tomada pelo que os passos anteriores mostrarem:

**(A) η derivado.** Definir $\eta$ como funcional da evolução acumulada
de $\phi_-$ e mostrar que reproduz a fenomenologia que motivou sua
introdução. Isso **dissolve** o achado A2 (duas leis incompatíveis) em
vez de decidi-lo por decreto: η deixa de ter lei própria.

**(B) η aposentado.** Se a aceleração já vem de $\rho_{\rm int}(r_\star(t))$
sem precisar de η, retirá-lo formalmente do núcleo e mantê-lo, no
máximo, como quantidade descritiva.

### Gate 9
- **Critério:** ou η é derivado com equação de movimento que **decorre**
  da ação, ou é removido do núcleo. **Não é aceitável** manter
  $H^2=8\pi G\rho/(3(1-\eta))$ como postulado sem ação que a produza —
  a D4 já mostrou que ela não decorre da ação atual, e uma extensão
  $\Omega(\eta)R_g$ produziria termo extra $H\dot\eta/(1-\eta)$ ausente
  na forma usada.
- **Nível exigido:** 1 ou 2a.
- **Se falhar:** adotar (B). A narrativa de "separação estrutural
  acumulada" continua válida — ela passa a ser carregada por
  $r_\star(t)$, que é derivado, em vez de por η, que era postulado.

---

# Passo 10 — Interpretação, por último

Só agora se escreve o capítulo conceitual, e ele descreve **o que foi
derivado**. Se a dinâmica produziu bifurcação, variável relacional
monotônica e aceleração efetiva, esses são resultados. Se não produziu,
a narrativa muda — não os resultados.

**Pendência a resolver aqui:** a v1 tem *três* fórmulas de tempo
relacional ($T=f(H_1-H_2)$, $\tau\sim\ln\sigma$, $t\sim\ln r/\Delta H$),
nunca unificadas. A v2 deve ou definir **um** funcional relacional
covariante, com monotonicidade e condições de relógio demonstradas, ou
declarar as três explicitamente como metáfora.

### Gate 10
- **Critério:** nenhuma afirmação interpretativa sem apontar para o
  passo que a derivou.
- **Nível exigido:** 1 (rastreabilidade é verificável).

---

# Afirmação mínima enquanto o plano roda

Até que os gates fechem, esta é a formulação honesta do que a teoria
afirma:

> A TDCP postula que o estado primordial contém dois graus de liberdade
> fundamentais correlacionados, cuja dinâmica diferencial pode produzir
> uma bifurcação cosmológica. A existência de dupla geometria, de uma
> variável temporal relacional e de aceleração emergente são **hipóteses
> a serem derivadas e testadas**, não postulados estabelecidos.

---

# Onde o plano provavelmente morre, se morrer

Ordenado por probabilidade de falha, para calibrar expectativa:

1. **Gate 3.5 (Higuchi)** — a D8 já falhou 60/60 na v1. A esperança
   concreta é que o ramo algébrico dê ξ muito menor que o ramo dinâmico
   ($\xi=3.497$ no benchmark da v1), o que muda o sinal de
   $\beta_1+\beta_2(\xi+r)$. Mas é uma esperança, não um resultado.
2. **Gate 4(d) (corredor seguro)** — a degenerescência na raiz exata é
   um resultado real da D1, e o ramo algébrico *é* a raiz. A tensão é
   estrutural.
3. **Gate 6 (região viável)** — mesmo passando 1–5, a interseção pode
   ser vazia.
4. **Gate 2 (ghost)** — tecnicamente o mais grave, mas com bom
   argumento a priori de que passa.

Os gates 3.5 e 4 são baratos e vêm cedo justamente por isso: se o
programa vai morrer, que morra em semanas, não em vinte capítulos.
