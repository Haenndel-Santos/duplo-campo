# Registro de Fórmulas — Anexo E

Fonte: `manuscript/apendices/Appendix-E.md` — 57 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AE.01]  (linha 63)

```
$r(t)=\frac{b(t)}{a(t)}, \qquad \xi(t)=\frac{N_f(t)}{N_g(t)}.$
```

- **Seção:** E.2 Variáveis fundamentais do fundo
- **Contexto:** …- e a variável acumulada \eta(t). / Definimos:
- **Segue:** Escolhemos gauge cosmológico:
- **Classe (sugerida):** definicao
- **Depende de:** Anexo A/B (AA.23/AB.07)
- **Veredito:** CONFERE (reprise)

### [AE.02]  (linha 67)

```
$N_g=1.$
```

- **Seção:** E.2 Variáveis fundamentais do fundo
- **Contexto:** …[equação anterior] / Escolhemos gauge cosmológico:
- **Segue:** Logo:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.2
- **Veredito:** CONFERE (escolha de gauge padrão, consistente com Anexo B §B.2/E.2)

### [AE.03]  (linha 71)

```
$$ H \equiv \frac{\dot a}{a}, \qquad H_f = \frac{1}{N_f}\frac{\dot b}{b} = \frac{1}{\xi}\frac{\dot b}{b}. $$
```

- **Seção:** E.2 Variáveis fundamentais do fundo
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** **E.3 Equações fundamentais (fundo)**
- **Classe (sugerida):** definicao
- **Depende de:** Anexo B §B.2 (AB.06)
- **Veredito:** CONFERE (consistente com AB.06, especializado a N_g=1, logo H=H_g)

### [AE.04]  (linha 77)

```
$3M_g^2 H^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)}.$
```

- **Seção:** (1) Friedmann do setor visível g
- **Contexto:** …**E.3 Equações fundamentais (fundo)** / **(1) Friedmann do setor visível g**
- **Segue:** com
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.5 (AB.35)
- **Veredito:** CONFERE (reprise de AB.35, com H=H_g pois N_g=1)

### [AE.05]  (linha 81)

```
$\rho_\chi = \frac12\dot\chi^2 + U(\chi),$
```

- **Seção:** (1) Friedmann do setor visível g
- **Contexto:** …[equação anterior] / com
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.5 (AB.36)
- **Veredito:** CONFERE (reprise de AB.36 — densidade padrão de Klein-Gordon)

### [AE.06]  (linha 83)

```
$$ \rho_{int}^{(g)} = m^2M_{eff}^2 F(\chi) \left(\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3\right). $$
```

- **Seção:** (1) Friedmann do setor visível g
- **Contexto:** …com / [equação anterior]
- **Segue:** **(2) Friedmann do setor estrutural f**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.8 (AA.30); âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** CONFERE — âncora D3: forma correta (sem ξ, sem β4), idêntica ao Anexo A §A.8/AA.30 e à correção da âncora D3 para o Anexo B §B.5 (AB.36) — esta é a forma que o corpo principal de fato usa

### [AE.07]  (linha 87)

```
$3M_f^2 H_f^2 = \rho_{int}^{(f)},$
```

- **Seção:** (2) Friedmann do setor estrutural f
- **Contexto:** …[equação anterior] / **(2) Friedmann do setor estrutural f**
- **Segue:** com
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.11 (AB.70)
- **Veredito:** CONFERE (reprise de AB.70)

### [AE.08]  (linha 91)

```
$$ \rho_{int}^{(f)} = m^2M_{eff}^2 F(\chi) \left(\beta_4 + 3\beta_3 r^{-1} + 3\beta_2 r^{-2} + \beta_1 r^{-3}\right). $$
```

- **Seção:** (2) Friedmann do setor estrutural f
- **Contexto:** …[equação anterior] / com
- **Segue:** **(3) Equação de χ (com fonte do acoplamento)**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.6 (AB.50)
- **Veredito:** CONFERE (reprise exata de AB.50, já verificada por álgebra explícita no lote 7)

### [AE.09]  (linha 97)

```
$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,W(r,\xi), $$
```

- **Seção:** (3) Equação de χ (com fonte do acoplamento)
- **Contexto:** …**(3) Equação de χ (com fonte do acoplamento)** / Forma geral:
- **Segue:** onde W(r,\xi) representa a combinação efetiva que surge ao variar o termo F(\chi)V(\xi,r) em relação a χ.
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** âncora D2/D8 (erratum de sinal)
- **Veredito:** ERRO DE CÁLCULO (sinal da fonte trocado) — verificado por Euler-Lagrange nesta auditoria: variando a ação (termo -m²M_eff²√-g F(χ)V(K)) em relação a χ, e usando a convenção padrão do EOM livre de KG (χ̈+3Hχ̇+U'=0), obtém-se χ̈+3Hχ̇+U'(χ)=-m²M_eff²F'(χ)V(K) — sinal NEGATIVO, não positivo como escrito; mesmo erratum já documentado nas âncoras D2/D8 ("a ação dá −m²M_eff²F′V")

### [AE.10]  (linha 103)

```
$W(r,\xi) = V(\xi,r)$
```

- **Seção:** (3) Equação de χ (com fonte do acoplamento)
- **Contexto:** …onde W(r,\xi) representa a combinação efetiva que surge ao variar o termo F(\chi)V(\xi,r) em relação a χ. / Uma escolha natural, coerente com o fundo FLRW, é:
- **Segue:** isto é,
- **Classe (sugerida):** pendente
- **Depende de:** AE.09
- **Veredito:** CONFERE (a identificação W=V(ξ,r) é a estrutura correta — a única dependência em χ do termo de interação é via F(χ), então a fonte é proporcional a F'(χ)V(K); o problema não está aqui, mas no sinal geral já presente em AE.09)

### [AE.11]  (linha 107)

```
$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,V(\xi,r). $$
```

- **Seção:** (3) Equação de χ (com fonte do acoplamento)
- **Contexto:** …[equação anterior] / isto é,
- **Segue:** (Em aplicações, usa-se a forma completa de V.)
- **Classe (sugerida):** pendente
- **Depende de:** AE.09/10; âncora D2/D8
- **Veredito:** ERRO DE CÁLCULO (mesmo erro de sinal de AE.09, agora com W especializado — deveria ser χ̈+3Hχ̇+U'(χ)=−m²M_eff²F'(χ)V(ξ,r); erratum documentado nas âncoras D2/D8)

### [AE.12]  (linha 113)

```
$\dot\eta = \Gamma \dot\chi^2.$
```

- **Seção:** (4) Evolução de η
- **Contexto:** …(Em aplicações, usa-se a forma completa de V.) / **(4) Evolução de η**
- **Segue:** **(5) Conservação de matéria**
- **Classe (sugerida):** pendente
- **Depende de:** Cap.1 §1.6/Cap.2 §2.7; achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (forma internamente razoável, dimensionalmente coerente como definição isolada) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 — duas leis incompatíveis para η̇ no mesmo corpus (achado A2/lote 1): lá η̇=Γ(H1-H2)² com [Γ]=tempo, aqui η̇=Γχ̇² com Γ de dimensão diferente; nenhuma das duas declara a dimensão de Γ

### [AE.13]  (linha 119)

```
$$ \dot\rho_m + 3H\rho_m = 0 \quad\Rightarrow\quad \rho_m = \rho_{m0} a^{-3}. $$
```

- **Seção:** (5) Conservação de matéria
- **Contexto:** …**(5) Conservação de matéria** / Para matéria fria:
- **Segue:** (Para radiação: \rho_r\propto a^{-4}, se incluída.)
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (conservação padrão de matéria fria, importada)

### [AE.14]  (linha 125)

```
$(\beta_1 + 2\beta_2 r + \beta_3 r^2)(H - \xi H_f)=0.$
```

- **Seção:** (6) Constraint de Bianchi (ramos)
- **Contexto:** …(Para radiação: \rho_r\propto a^{-4}, se incluída.) / **(6) Constraint de Bianchi (ramos)**
- **Segue:** Escolha TDCP principal: ramo dinâmico, isto é:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.8 (AB.54/56/71)
- **Veredito:** CONFERE (reprise da constraint de Bianchi, Anexo B §B.8)

### [AE.15]  (linha 129)

```
$H = \xi H_f.$
```

- **Seção:** (6) Constraint de Bianchi (ramos)
- **Contexto:** …[equação anterior] / Escolha TDCP principal: ramo dinâmico, isto é:
- **Segue:** Esta equação é essencial para fechar o sistema, pois liga H, H_f e \xi.
- **Classe (sugerida):** pendente
- **Depende de:** âncora D1 (derivations/01_setor_escalar_K_Omega.md), âncora D5 (derivations/05_rdot_ramo_dinamico.md)
- **Veredito:** CONFLITA COM âncoras D1, D5 — esta é a "escolha TDCP principal" (ramo dinâmico) citada nominalmente pelas duas derivações como o ramo duplamente inviável: D5 mostra ṙ≡0 exatamente nesse ramo (ver AE.50/51 abaixo — não produz r(t) genuíno), e D1 encontra um par fantasma/taquiônico genuíno nesse mesmo ramo em todos os benchmarks testados. A equação em si (um dos dois ramos logicamente possíveis de AE.14) está correta; o problema é apresentá-la como "escolha principal" sem mencionar essas duas patologias já derivadas

### [AE.16]  (linha 151)

```
$H = \xi H_f \quad\Rightarrow\quad H_f = \frac{H}{\xi}.$
```

- **Seção:** E.4 Fechamento do sistema: incógnitas e equações
- **Contexto:** …- com \rho_m(a) conhecido. / No ramo dinâmico:
- **Segue:** Mas a equação de Friedmann f envolve H_f explicitamente, logo fornece uma relação algébrica para \xi dado H,r,\chi.
- **Classe (sugerida):** importada-da-literatura
- **Depende de:** AE.15; âncora D1 (derivations/01_setor_escalar_K_Omega.md), âncora D5 (derivations/05_rdot_ramo_dinamico.md)
- **Veredito:** CONFERE (rearranjo direto de AE.15 — mesma nota sobre o ramo dinâmico, âncoras D1/D5)

### [AE.17]  (linha 159)

```
$N\equiv \ln a, \qquad \frac{d}{dt} = H\frac{d}{dN}.$
```

- **Seção:** E.5 Forma adimensional: escolha de variável temporal N=\ln a
- **Contexto:** …**E.5 Forma adimensional: escolha de variável temporal N=\ln a** / Definimos:
- **Segue:** Definimos as variáveis adimensionais:
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de variável temporal N=ln a)

### [AE.18]  (linha 163)

```
$$ x \equiv \frac{\dot\chi}{\sqrt{6}M_g H}, \qquad y \equiv \frac{\sqrt{U(\chi)}}{\sqrt{3}M_g H}, \qquad \Omega_m \equiv \frac{\rho_m}{3M_g^2 H^2}. $$
```

- **Seção:** E.5 Forma adimensional: escolha de variável temporal N=\ln a
- **Contexto:** …[equação anterior] / Definimos as variáveis adimensionais:
- **Segue:** E também:
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (importada — variáveis adimensionais padrão da literatura de sistemas dinâmicos de quintessência, ex. Copeland-Sahni-Tsujikawa)

### [AE.19]  (linha 167)

```
$\Omega_{int} \equiv \frac{\rho_{int}^{(g)}}{3M_g^2 H^2}.$
```

- **Seção:** E.5 Forma adimensional: escolha de variável temporal N=\ln a
- **Contexto:** …[equação anterior] / E também:
- **Segue:** Então a Friedmann g vira um constraint:
- **Classe (sugerida):** definicao
- **Depende de:** AE.18
- **Veredito:** CONFERE (definição análoga a AE.18, para o setor de interação)

### [AE.20]  (linha 171)

```
$1 = \Omega_m + x^2 + y^2 + \Omega_{int}.$
```

- **Seção:** E.5 Forma adimensional: escolha de variável temporal N=\ln a
- **Contexto:** …[equação anterior] / Então a Friedmann g vira um constraint:
- **Segue:** **E.6 Equações diferenciais em N**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.04, AE.18, AE.19
- **Veredito:** CONFERE (álgebra verificada: dividindo AE.04 por 3M_g²H² e usando χ̇=√6M_gHx, U=3M_g²H²y² das definições de AE.18, obtém-se exatamente esta forma)

### [AE.21]  (linha 177)

```
$\frac{d\chi}{dN} = \frac{\dot\chi}{H} = \sqrt{6}M_g x.$
```

- **Seção:** E.6.1 Evolução de χ
- **Contexto:** …**E.6 Equações diferenciais em N** / **E.6.1 Evolução de χ**
- **Segue:** **E.6.2 Evolução de x**
- **Classe (sugerida):** pendente
- **Depende de:** AE.18
- **Veredito:** CONFERE (álgebra verificada: rearranjo direto de AE.18)

### [AE.22]  (linha 183)

```
$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V(\xi,r). $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …**E.6.2 Evolução de x** / Começamos de:
- **Segue:** Escrevemos \ddot\chi = H\frac{d\dot\chi}{dN}.
- **Classe (sugerida):** pendente
- **Depende de:** AE.11; âncora D2/D8
- **Veredito:** ERRO DE CÁLCULO (repete o erro de sinal de AE.11 — deveria ser −m²M_eff²F'(χ)V(ξ,r); erratum documentado nas âncoras D2/D8)

### [AE.23]  (linha 189)

```
$\dot\chi = \sqrt{6}M_g H x,$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …Escrevemos \ddot\chi = H\frac{d\dot\chi}{dN}. / Como:
- **Segue:** então:
- **Classe (sugerida):** pendente
- **Depende de:** AE.21
- **Veredito:** CONFERE (mesma relação de AE.21, forma direta)

### [AE.24]  (linha 193)

```
$$ \ddot\chi = \sqrt{6}M_g\left(\dot H x + H\dot x\right) = \sqrt{6}M_g H^2\left(\frac{d x}{dN} + x\frac{d\ln H}{dN}\right). $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / então:
- **Segue:** Substituindo:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.23
- **Veredito:** CONFERE (álgebra verificada: regra do produto em AE.23 + conversão para derivadas em N via Ḣ=H²dlnH/dN e ẋ=Hdx/dN)

### [AE.25]  (linha 197)

```
$$ \sqrt{6}M_g H^2\left(\frac{dx}{dN}+x\frac{d\ln H}{dN}\right) + 3H(\sqrt{6}M_g H x) + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V. $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / Substituindo:
- **Segue:** Dividindo por \sqrt{6}M_g H^2:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.22, AE.24; âncora D2/D8
- **Veredito:** ERRO DE CÁLCULO (herda o erro de sinal de AE.22 — o lado direito deveria ter sinal negativo)

### [AE.26]  (linha 201)

```
$$ \frac{dx}{dN}+x\frac{d\ln H}{dN}+3x + \frac{U'(\chi)}{\sqrt{6}M_g H^2} = \frac{m^2 M_{eff}^2}{\sqrt{6}M_g H^2}F'(\chi)V. $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / Dividindo por \sqrt{6}M_g H^2:
- **Segue:** Definimos os parâmetros de "inclinação":
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.25; âncora D2/D8
- **Veredito:** ERRO DE CÁLCULO (divisão de AE.25 por √6M_gH² algebricamente correta, mas herda o erro de sinal)

### [AE.27]  (linha 205)

```
$$ \lambda(\chi) \equiv M_g\frac{U'(\chi)}{U(\chi)}, \qquad \Rightarrow \frac{U'}{H^2} = 3M_g^2 \lambda y^2. $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / Definimos os parâmetros de "inclinação":
- **Segue:** Logo:
- **Classe (sugerida):** definicao
- **Depende de:** AE.18
- **Veredito:** ERRO DE CÁLCULO — verificado por álgebra direta nesta auditoria: de λ≡M_gU'/U e y²=U/(3M_g²H²) (AE.18), segue U'=λU/M_g=λ(3M_g²H²y²)/M_g=3M_gH²λy², logo U'/H²=3M_gλy² (um fator de M_g), não 3M_g²λy² (dois fatores) como escrito; o erro NÃO se propaga — a equação seguinte (AE.28) usa implicitamente o valor correto

### [AE.28]  (linha 209)

```
$\frac{U'}{\sqrt{6}M_g H^2} = \sqrt{\frac{3}{2}}\lambda y^2.$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** Portanto:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.27
- **Veredito:** CONFERE (verificado: usa implicitamente o valor CORRETO de U'/H²=3M_gλy² — não a versão com M_g² erroneamente escrita em AE.27 — resultando exatamente em √(3/2)λy²: 3M_gλy²/(√6M_g)=（3/√6)λy²=√(3/2)λy²)

### [AE.29]  (linha 213)

```
$$ \boxed{ \frac{dx}{dN} = -3x - x\frac{d\ln H}{dN} - \sqrt{\frac{3}{2}}\lambda y^2 + \mathcal{S}(r,\xi,\chi)\frac{m^2}{H^2} } $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / Portanto:
- **Segue:** onde
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.26, AE.28; âncora D2/D8
- **Veredito:** ERRO DE CÁLCULO (álgebra de combinação de AE.26+AE.28 verificada e correta EM SI, mas herda o erro de sinal de AE.09/11/22: o último termo deveria ser −𝒮(r,ξ,χ)m²/H², não +)

### [AE.30]  (linha 217)

```
$$ \mathcal{S}(r,\xi,\chi)= \frac{ M_{eff}^2}{\sqrt{6}M_g}F'(\chi)V(\xi,r). $$
```

- **Seção:** E.6.2 Evolução de x
- **Contexto:** …[equação anterior] / onde
- **Segue:** **E.6.3 Evolução de η**
- **Classe (sugerida):** pendente
- **Depende de:** AE.26, AE.28
- **Veredito:** CONFERE (definição de conveniência, consistente algebricamente com a extração de AE.26/28 — o sinal do termo em que aparece em AE.29 é que carrega o erro herdado, não esta definição em si)

### [AE.31]  (linha 221)

```
$$ \dot\eta = \Gamma \dot\chi^2 \Rightarrow \frac{d\eta}{dN} = \frac{\dot\eta}{H} = \Gamma \frac{\dot\chi^2}{H}. $$
```

- **Seção:** E.6.3 Evolução de η
- **Contexto:** …[equação anterior] / **E.6.3 Evolução de η**
- **Segue:** Como:
- **Classe (sugerida):** pendente
- **Depende de:** AE.12; achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (rearranjo correto para N; mesma nota de AE.12 — CONFLITA COM Cap.1 §1.6/Cap.2 §2.7, achado A2/lote 1)

### [AE.32]  (linha 225)

```
$\dot\chi^2 = 6M_g^2 H^2 x^2,$
```

- **Seção:** E.6.3 Evolução de η
- **Contexto:** …[equação anterior] / Como:
- **Segue:** então:
- **Classe (sugerida):** pendente
- **Depende de:** AE.23
- **Veredito:** CONFERE (álgebra verificada: quadrado direto de AE.23)

### [AE.33]  (linha 229)

```
$\boxed{ \frac{d\eta}{dN} = 6\Gamma M_g^2 H x^2 }$
```

- **Seção:** E.6.3 Evolução de η
- **Contexto:** …[equação anterior] / então:
- **Segue:** Em forma totalmente adimensional, absorve-se o fator dimensional definindo \tilde\Gamma = \Gamma M_g^2 H_0, mas deixamos
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.31, AE.32; achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (álgebra verificada: substituição direta de AE.32 em AE.31; mesma nota de AE.12/31 sobre a lei conflitante de η)

### [AE.34]  (linha 235)

```
$De \rho_m\propto a^{-3}:$
```

- **Seção:** E.6.4 Evolução de \Omega_m
- **Contexto:** …Em forma totalmente adimensional, absorve-se o fator dimensional definindo \tilde\Gamma = \Gamma M_g^2 H_0, mas deixamos aqui a forma geral. / **E.6.4 Evolução de \Omega_m**
- **Segue:** [equação seguinte]
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** ARTEFATO DE CONVERSÃO (prosa dentro de $ — "De ρm∝a⁻³:" é frase introdutória, não fórmula; mesmo padrão de outros fragmentos de prosa capturados pelo extrator)

### [AE.35]  (linha 237)

```
$\frac{d\ln\rho_m}{dN}=-3.$
```

- **Seção:** E.6.4 Evolução de \Omega_m
- **Contexto:** …**E.6.4 Evolução de \Omega_m** / [equação anterior]
- **Segue:** Como:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (consequência direta de ρm∝a⁻³: d(ln ρm)/dN=-3)

### [AE.36]  (linha 241)

```
$\Omega_m = \frac{\rho_m}{3M_g^2H^2},$
```

- **Seção:** E.6.4 Evolução de \Omega_m
- **Contexto:** …[equação anterior] / Como:
- **Segue:** temos:
- **Classe (sugerida):** pendente
- **Depende de:** AE.18
- **Veredito:** CONFERE (reprise de AE.18)

### [AE.37]  (linha 245)

```
$\frac{d\ln\Omega_m}{dN} = -3 - 2\frac{d\ln H}{dN}.$
```

- **Seção:** E.6.4 Evolução de \Omega_m
- **Contexto:** …[equação anterior] / temos:
- **Segue:** Logo:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.35, AE.36
- **Veredito:** CONFERE (álgebra verificada: derivada logarítmica de AE.36 usando AE.35)

### [AE.38]  (linha 249)

```
$$ \boxed{ \frac{d\Omega_m}{dN} = \Omega_m\left(-3 -2\frac{d\ln H}{dN}\right). } $$
```

- **Seção:** E.6.4 Evolução de \Omega_m
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** **E.7 Como obter d\ln H/dN**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.37
- **Veredito:** CONFERE (álgebra verificada: rearranjo direto de AE.37)

### [AE.39]  (linha 257)

```
$H^2 = \frac{8\pi G}{3}\frac{\rho_{tot}}{1-\eta}.$
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …Aqui está o "pulo do gato" do sistema. / No formalismo TDCP efetivo:
- **Segue:** Tomando log:
- **Classe (sugerida):** pendente
- **Depende de:** âncora D4 (derivations/04_friedmann_eta_acao.md)
- **Veredito:** NÃO-DERIVÁVEL — âncora D4: esta forma não é derivável da ação bimétrica atual (η está ausente da ação); uma extensão mínima Ω(η)R_g produziria um termo extra Hη̇/(1−η) não presente aqui; a forma só vale, quando muito, no regime adiabático |η̇|≪H — deve ser reclassificada como extensão proposta, não consequência da ação (mesma nota de Cap.1 §1.6/Cap.2 §2.7/Anexo H §H.6, lote 1)

### [AE.40]  (linha 261)

```
\ln H^2 = \ln\rho_{tot} - \ln(1-\eta) + const.
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …[equação anterior] / Tomando log:
- **Segue:** Derivando em N:
- **Flags:** sem-delimitador
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.39; âncora D4 (derivations/04_friedmann_eta_acao.md)
- **Veredito:** CONFERE (álgebra correta — logaritmo de AE.39; herda o status de extensão postulada, não derivada da ação — âncora D4; flag sem-delimitador)

### [AE.41]  (linha 265)

```
$$ \frac{d\ln H^2}{dN} = \frac{d\ln\rho_{tot}}{dN} + \frac{1}{1-\eta}\frac{d\eta}{dN}. $$
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …[equação anterior] / Derivando em N:
- **Segue:** Logo:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.40; âncora D4 (derivations/04_friedmann_eta_acao.md)
- **Veredito:** CONFERE (álgebra verificada: derivada de AE.40 — mesma nota de extensão postulada, âncora D4)

### [AE.42]  (linha 269)

```
$$ \boxed{ \frac{d\ln H}{dN} = \frac12\frac{d\ln\rho_{tot}}{dN} + \frac{1}{2(1-\eta)}\frac{d\eta}{dN}. } $$
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** No regime onde \rho_{tot}\approx \rho_m + \rho_\chi + \rho_{int}, podemos calcular \frac{d\ln\rho_{tot}}{dN} a partir da
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.41; âncora D4 (derivations/04_friedmann_eta_acao.md)
- **Veredito:** CONFERE (álgebra verificada: divisão de AE.41 por 2 — mesma nota de extensão postulada, âncora D4)

### [AE.43]  (linha 279)

```
$$ w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN}, $$
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …- usar a equação de aceleração (Raychaudhuri) derivada da variação em a, / - ou usar diretamente:
- **Segue:** e então:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE SOB HIPÓTESE (o próprio texto apresenta isto como escolha de conveniência — "é comum: usar diretamente" — não uma consequência direta e rigorosa de AE.39-42 mostrada explicitamente nesta seção)

### [AE.44]  (linha 283)

```
$$ \frac{d\ln H}{dN} = -\frac32\left(1+w_{\text{eff}}\right)\left(1-\Omega_r\right)+\cdots $$
```

- **Seção:** E.7 Como obter d\ln H/dN
- **Contexto:** …[equação anterior] / e então:
- **Segue:** dependendo de quais componentes foram incluídos.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.42, AE.43
- **Veredito:** INCOMPLETA (o próprio texto declara que a forma depende de "quais componentes foram incluídos" e usa reticências "+⋯" — fórmula esquemática, não fechada)

### [AE.45]  (linha 295)

```
$H=\xi H_f \Rightarrow H_f = \frac{H}{\xi}.$
```

- **Seção:** E.8 Fechamento com o setor f: obtenção de \xi
- **Contexto:** …**E.8 Fechamento com o setor f: obtenção de \xi** / No ramo dinâmico:
- **Segue:** A Friedmann f:
- **Classe (sugerida):** pendente
- **Depende de:** AE.16; âncora D1 (derivations/01_setor_escalar_K_Omega.md), âncora D5 (derivations/05_rdot_ramo_dinamico.md)
- **Veredito:** CONFERE (reprise de AE.16 — mesma nota sobre o ramo dinâmico, âncoras D1/D5)

### [AE.46]  (linha 299)

```
$$ 3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi) \left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right). $$
```

- **Seção:** E.8 Fechamento com o setor f: obtenção de \xi
- **Contexto:** …[equação anterior] / A Friedmann f:
- **Segue:** Substituindo H_f=H/\xi:
- **Classe (sugerida):** pendente
- **Depende de:** AE.07, AE.08
- **Veredito:** CONFERE (substituição direta de AE.08 em AE.07 — reprise, já verificada em AB.50)

### [AE.47]  (linha 303)

```
$$ 3M_f^2 \frac{H^2}{\xi^2} = m^2M_{eff}^2F(\chi)\,\mathcal{U}(r), $$
```

- **Seção:** E.8 Fechamento com o setor f: obtenção de \xi
- **Contexto:** …[equação anterior] / Substituindo H_f=H/\xi:
- **Segue:** onde:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.45, AE.46
- **Veredito:** CONFERE (substituição direta de AE.45 em AE.46, com a bracket renomeada 𝒰(r) — definida a seguir em AE.48)

### [AE.48]  (linha 307)

```
$$ \mathcal{U}(r)\equiv \beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}. $$
```

- **Seção:** E.8 Fechamento com o setor f: obtenção de \xi
- **Contexto:** …[equação anterior] / onde:
- **Segue:** Logo obtemos \xi algebraicamente:
- **Classe (sugerida):** definicao
- **Depende de:** AE.08/46
- **Veredito:** CONFERE (definição, idêntica à bracket de AE.08/46)

### [AE.49]  (linha 311)

```
$$ \boxed{ \xi(N) = H\sqrt{\frac{3M_f^2}{m^2M_{eff}^2F(\chi)\mathcal{U}(r)}} } $$
```

- **Seção:** E.8 Fechamento com o setor f: obtenção de \xi
- **Contexto:** …[equação anterior] / Logo obtemos \xi algebraicamente:
- **Segue:** (up to escolha de sinal físico).
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.47
- **Veredito:** CONFERE (álgebra verificada: solução direta de AE.47 para ξ, com a ressalva honesta do próprio texto sobre a escolha de sinal)

### [AE.50]  (linha 321)

```
$$ r=\frac{b}{a} \Rightarrow \dot r = r(N_fH_f - H)= r(\xi H_f - H). $$
```

- **Seção:** E.9 Dinâmica de r: escolha de parametrização
- **Contexto:** …**E.9 Dinâmica de r: escolha de parametrização** / Como:
- **Segue:** Mas no ramo dinâmico, H=\xi H_f, então formalmente:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Anexo B §B.9 (AB.60-62)
- **Veredito:** CONFERE (álgebra verificada, consistente com Anexo B §B.9/AB.60-62 especializado a N_g=1)

### [AE.51]  (linha 325)

```
$\dot r = 0.$
```

- **Seção:** E.9 Dinâmica de r: escolha de parametrização
- **Contexto:** …[equação anterior] / Mas no ramo dinâmico, H=\xi H_f, então formalmente:
- **Segue:** Isso significa que:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AE.15, AE.50; âncora D5 (derivations/05_rdot_ramo_dinamico.md)
- **Veredito:** CONFERE — âncora D5: ṙ≡0 confirmado de novo (também em Anexo B §B.9/AB.65) — mas ao contrário do Cap.14 §14.12 (achado C1/lote 3), este anexo NÃO tenta contornar o resultado: a prosa que segue (E.9.A/E.9.B) reconhece honestamente a implicação e propõe r constante como a prática mais simples, na linha do que a âncora D5 recomenda (raiz móvel/algébrica em vez de "r(t) dinâmico" genuíno no ramo H=ξHf)

### [AE.52]  (linha 353)

```
$H(z) \quad\text{com}\quad 1+z=a^{-1}.$
```

- **Seção:** (1) Hubble
- **Contexto:** …Uma simulação entrega, como funções de N ou z: / **(1) Hubble**
- **Segue:** **(2) Função efetiva w_{\text{eff}}**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (relação padrão redshift-fator de escala)

### [AE.53]  (linha 357)

```
$$ \boxed{ w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN}. } $$
```

- **Seção:** (2) Função efetiva w_{\text{eff}}
- **Contexto:** …[equação anterior] / **(2) Função efetiva w_{\text{eff}}**
- **Segue:** **(3) Frações de densidade**
- **Classe (sugerida):** pendente
- **Depende de:** AE.43
- **Veredito:** CONFERE SOB HIPÓTESE (reprise de AE.43 — mesma nota sobre ser uma parametrização de conveniência)

### [AE.54]  (linha 361)

```
$\Omega_m(N),\quad \Omega_\chi(N),\quad \Omega_{int}(N).$
```

- **Seção:** (3) Frações de densidade
- **Contexto:** …[equação anterior] / **(3) Frações de densidade**
- **Segue:** **(4) Massa efetiva do modo tensorial**
- **Classe (sugerida):** pendente
- **Depende de:** AE.18/19
- **Veredito:** CONFERE (lista de observáveis, consistente com as definições de AE.18/19; nota: Ω_χ não foi explicitamente definida antes — presumivelmente x²+y² por AE.20 — pequena incompletude notacional)

### [AE.55]  (linha 365)

```
$m_T^2(N)=m^2F(\chi)\mu_T^2(\cdots).$
```

- **Seção:** (4) Massa efetiva do modo tensorial
- **Contexto:** …[equação anterior] / **(4) Massa efetiva do modo tensorial**
- **Segue:** **(5) Checagem de Higuchi**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo D §D.4 (AD.09); âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** CONFERE (reprise da estrutura de AD.09 — âncora D2 para a forma exata de μ_T²)

### [AE.56]  (linha 369)

```
$m_T^2(N) \ge 2H^2(N).$
```

- **Seção:** (5) Checagem de Higuchi
- **Contexto:** …[equação anterior] / **(5) Checagem de Higuchi**
- **Segue:** **E.11 Procedimento de integração (roteiro prático)**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** CONFERE (reprise do bound de Higuchi — âncora D2 para a forma exata de m_T²)

### [AE.57]  (linha 375)

```
$> (m,\beta_n,M_g,M_f, U(\chi), F(\chi), \Gamma).$
```

- **Seção:** E.11 Procedimento de integração (roteiro prático)
- **Contexto:** …**E.11 Procedimento de integração (roteiro prático)** / 1. Fixe parâmetros:
- **Segue:** 2. Escolha condições iniciais em N=N_i (alta redshift):
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** —
- **Veredito:** ARTEFATO DE CONVERSÃO (resíduo de blockquote Markdown ">" preso dentro do "$", mesmo padrão de Anexo B §B.11/Cap.16 §16.9; conteúdo é apenas uma lista de parâmetros a fixar, não uma equação)

