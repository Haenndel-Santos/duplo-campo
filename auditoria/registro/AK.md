# Registro de Fórmulas — Anexo K

Fonte: `manuscript/apendices/Appendix-K.md` — 16 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AK.01]  (linha 49)

```
$$w = - 1$$
```

- **Seção:** K.2 Dinâmica da Energia Escura
- **Contexto:** …No **modelo ΛCDM**, a energia escura é descrita por uma constante / cosmológica com equação de estado:
- **Segue:** Na TDCP, a energia escura tem uma contribuição dinâmica associada ao
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (padrão, ΛCDM, citado para contraste)

### [AK.02]  (linha 56)

```
$$\rho_{DE} = \rho_{\Lambda} + \rho_{\chi}$$
```

- **Seção:** K.2 Dinâmica da Energia Escura
- **Contexto:** …campo $\chi$. / A densidade efetiva pode ser escrita como:
- **Segue:** A equação de estado pode então variar com o redshift:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE SOB HIPÓTESE (parametrização razoável em si, mas não conectada à estrutura real de ρ_int(r) do corpo F1 — mesmo padrão de parâmetros paralelos, `integration_assessment.md` (Pergunta 4: parâmetros paralelos))

### [AK.03]  (linha 60)

```
$$w(z) = - 1 + \epsilon(z)$$
```

- **Seção:** K.2 Dinâmica da Energia Escura
- **Contexto:** …[equação anterior] / A equação de estado pode então variar com o redshift:
- **Segue:** onde $\epsilon(z)$ depende da evolução do campo $\chi$.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** —
- **Veredito:** CONFERE (parametrização padrão de energia escura dinâmica, forma genérica — tipo CPL)

### [AK.04]  (linha 66)

```
$$\mid w + 1 \mid \sim 10^{- 2} - 10^{- 3}$$
```

- **Seção:** K.2 Dinâmica da Energia Escura
- **Contexto:** …onde $\epsilon(z)$ depende da evolução do campo $\chi$. / Previsão da TDCP:
- **Segue:** Essa variação pode ser detectada por levantamentos cosmológicos de alta
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** NÃO-DERIVÁVEL (previsão numérica sem cálculo mostrado a partir de nenhum parâmetro do modelo — nem os da linha exploratória (χ,S_ent) nem os do corpo F1, m_S0/α0/p/q)

### [AK.05]  (linha 83)

```
$$\ddot{\delta} + 2H\dot{\delta} = 4\pi G_{eff}\rho_{m}\delta$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …**K.3 Crescimento de Estruturas** / O crescimento da densidade de matéria é descrito pela equação:
- **Segue:** Na TDCP, o acoplamento entre universos modifica a constante
- **Classe (sugerida):** pendente
- **Depende de:** Anexo J (AJ.09)
- **Veredito:** CONFERE (mesma forma padrão já confirmada, reprise de AJ.09/Cap.8/Cap.18)

### [AK.06]  (linha 88)

```
$$G_{eff} = G(1 + \alpha)$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …Na TDCP, o acoplamento entre universos modifica a constante / gravitacional efetiva:
- **Segue:** onde $\alpha$ depende da intensidade da interação entre os dois
- **Classe (sugerida):** pendente
- **Depende de:** Anexo J (AJ.10); âncora D6
- **Veredito:** NÃO-DERIVÁVEL (mesma nota de AJ.10 — α não conectado à estrutura μ(k,a) real da âncora D6)

### [AK.07]  (linha 99)

```
$$f(z) = \Omega_{m}(z)^{\gamma}$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …uma pequena modificação na taxa de crescimento de estruturas. / Essa taxa é frequentemente parametrizada como:
- **Segue:** No modelo padrão:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE (importada — parametrização padrão do índice de crescimento γ, Peebles/Linder 2005)

### [AK.08]  (linha 103)

```
$$\gamma \approx 0.55$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …[equação anterior] / No modelo padrão:
- **Segue:** Na TDCP:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE (valor padrão de ΛCDM, aproximadamente correto — literatura dá γ≈0.545-0.55)

### [AK.09]  (linha 107)

```
$$\gamma \approx 0.55 + \Delta\gamma$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …[equação anterior] / Na TDCP:
- **Segue:** com
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** AK.08
- **Veredito:** CONFERE SOB HIPÓTESE (parametrização razoável, mas Δγ não é calculado a partir de nenhuma estrutura derivada)

### [AK.10]  (linha 111)

```
$$\Delta\gamma \sim 0.01$$
```

- **Seção:** K.3 Crescimento de Estruturas
- **Contexto:** …[equação anterior] / com
- **Segue:** Esse efeito pode ser detectado através de medições de **distorção no
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** AK.09
- **Veredito:** NÃO-DERIVÁVEL (previsão numérica sem cálculo mostrado, mesma nota de AK.04)

### [AK.11]  (linha 131)

```
$$P(k) = P_{0}(k)\left( 1 + \eta\sin(k/k_{*}) \right)$$
```

- **Seção:** K.4 Assinaturas na CMB
- **Contexto:** …- assimetria hemisférica. / O espectro de potência primordial pode assumir a forma:
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** NÃO-DERIVÁVEL (forma fenomenológica assumida, sem cálculo mostrado a partir de S_ent ou de qualquer parâmetro derivado); NOVA sobrecarga de símbolo: η aqui é amplitude de modulação do espectro de potência primordial — um TERCEIRO uso de η no corpus, distinto do η de separação estrutural acumulada (Cap.1/Anexo E/H, achado A2) e do η_slip (Cap.18)

### [AK.12]  (linha 154)

```
$$(\square - m_{g}^{2})h_{\mu\nu} = \kappa h_{\mu\nu}^{(2)}$$
```

- **Seção:** K.5 Ondas Gravitacionais Primordiais
- **Contexto:** …adicionais. / A equação para as perturbações gravitacionais pode assumir a forma:
- **Segue:** Isso implica que as ondas gravitacionais podem exibir:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo J (AJ.08); âncora D2
- **Veredito:** NÃO-DERIVÁVEL (mesma nota de AJ.08 — forma assumida por analogia, sem derivação a partir de uma ação; κ introduzido livremente sem verificação de ausência de patologia)

### [AK.13]  (linha 166)

```
$$\omega^{2} = k^{2} + m_{g}^{2}$$
```

- **Seção:** K.5 Ondas Gravitacionais Primordiais
- **Contexto:** …- dispersão dependente da frequência. / A relação de dispersão torna-se:
- **Segue:** com
- **Classe (sugerida):** pendente
- **Depende de:** AK.12
- **Veredito:** CONFERE (relação de dispersão padrão de um campo massivo, consequência trivial da parte homogênea de AK.12 — ω²=k²+m² para □h+m²h=0)

### [AK.14]  (linha 170)

```
$$m_{g} \sim 10^{- 33} - 10^{- 30}\text{ eV}$$
```

- **Seção:** K.5 Ondas Gravitacionais Primordiais
- **Contexto:** …[equação anterior] / com
- **Segue:** Esses efeitos podem ser detectados por detectores futuros.
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Cap.19 (faixa m_S0~30-300H0)
- **Veredito:** CONFERE SOB HIPÓTESE (ordem de grandeza plausível — comparável a m∼H0 até ∼10³H0, mesma faixa usada como benchmark no corpo F1 principal, Cap.19 — mas não é calculada aqui a partir de nenhum parâmetro desta linha exploratória, apenas citada)

### [AK.15]  (linha 192)

```
$$P(k) = P_{\Lambda CDM}(k)\left( 1+\xi e^{- k/k_{c}} \right)$$
```

- **Seção:** K.6 Correlações Entre Universos
- **Contexto:** …galáxias. / O espectro de potência da matéria pode adquirir uma correção:
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** âncoras D1-D8 (ξ estrutural)
- **Veredito:** NÃO-DERIVÁVEL (forma fenomenológica assumida); NOVA sobrecarga de símbolo — grave: ξ aqui é a intensidade de um termo de correlação no espectro de matéria, colidindo com ξ=N_f/N_g, a variável estrutural central de todo o corpo F1 (usada em todas as âncoras D1-D8); mesma classe de problema do achado E6/lote 4 (ξ reaproveitado em Cap.20)

### [AK.16]  (linha 214)

```
$$H_{0}^{TDCP} > H_{0}^{\Lambda CDM}$$
```

- **Seção:** K.7 Tensão de Hubble
- **Contexto:** …expansão. / Previsão qualitativa:
- **Segue:** Essa diferença pode ajudar a reconciliar as medições.
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** —
- **Veredito:** CONFERE (previsão qualitativa razoável em espírito — energia escura dinâmica tardia pode geralmente deslocar H0 inferido; não quantificada aqui)

