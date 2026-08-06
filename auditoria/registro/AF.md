# Registro de Fórmulas — Anexo F

Fonte: `manuscript/apendices/Appendix-F.md` — 17 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AF.01]  (linha 53)

```
$\{ m,\beta_0,\beta_1,\beta_2,\beta_3,\beta_4,M_g,M_f \}$
```

- **Seção:** F.2.1 Bloco Gravitacional Bimétrico
- **Contexto:** …Separaremos os parâmetros em três blocos: / **F.2.1 Bloco Gravitacional Bimétrico**
- **Segue:** Estes controlam:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (lista de parâmetros, consistente com o corpo principal)

### [AF.02]  (linha 67)

```
$\{ U(\chi),F(\chi),\Gamma \}$
```

- **Seção:** F.2.2 Bloco Estrutural (χ)
- **Contexto:** …- limite GR. / **F.2.2 Bloco Estrutural (χ)**
- **Segue:** Estes controlam:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (lista de parâmetros)

### [AF.03]  (linha 79)

```
$\chi_i,\dot\chi_i,r_i,\eta_i.$
```

- **Seção:** F.2.3 Bloco Inicial
- **Contexto:** …- dinâmica da aceleração. / **F.2.3 Bloco Inicial**
- **Segue:** Controla trajetória cosmológica específica.
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (lista de condições iniciais)

### [AF.04]  (linha 91)

```
$\boxed{F(\chi) > 0}$
```

- **Seção:** F.3.1 Positividade de F(χ)
- **Contexto:** …**F.3.1 Positividade de F(χ)** / Para evitar inversão de sinal do termo de massa:
- **Segue:** Se F<0:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Anexo C §C.7 (AC.11)
- **Veredito:** CONFERE (reprise da condição de positividade já em AC.11/Anexo C §C.7)

### [AF.05]  (linha 107)

```
$\boxed{m_T^2(t) \ge 2H^2}$
```

- **Seção:** F.3.2 Condição de Higuchi
- **Contexto:** …**F.3.2 Condição de Higuchi** / Em regime acelerado:
- **Segue:** Como:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Anexo D §D.7 (AD.14)
- **Veredito:** CONFERE (bound de Higuchi padrão, repete AD.14/AC.17)

### [AF.06]  (linha 111)

```
$m_T^2 = m^2F(\chi)\mu_T^2(r,\beta_n),$
```

- **Seção:** F.3.2 Condição de Higuchi
- **Contexto:** …[equação anterior] / Como:
- **Segue:** então:
- **Classe (sugerida):** pendente
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** INCOMPLETA (μ_T² aqui é listada como função de (r,βn) apenas, omitindo ξ — ao contrário da forma mais completa do Anexo D §D.4/AD.09, μ_T²(r,ξ,βn,M_g,M_f); a âncora D2 mostra que a dependência em ξ é essencial, inclusive determinante de sinal)

### [AF.07]  (linha 115)

```
$m^2F(\chi)\mu_T^2 \ge 2H^2.$
```

- **Seção:** F.3.2 Condição de Higuchi
- **Contexto:** …[equação anterior] / então:
- **Segue:** Isso define uma superfície no espaço:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AF.06
- **Veredito:** INCOMPLETA (herda a omissão de ξ de AF.06)

### [AF.08]  (linha 119)

```
$\mathcal{S}_{\text{Higuchi}}.$
```

- **Seção:** F.3.2 Condição de Higuchi
- **Contexto:** …[equação anterior] / Isso define uma superfície no espaço:
- **Segue:** Abaixo dessa superfície → região excluída.
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (notação — define o nome da superfície de Higuchi no espaço de parâmetros)

### [AF.09]  (linha 127)

```
$K_{11}>0, \quad K_{22}>0, \quad \det K>0.$
```

- **Seção:** F.3.3 Ausência de Ghost Escalar
- **Contexto:** …**F.3.3 Ausência de Ghost Escalar** / Do Anexo C:
- **Segue:** Isso impõe desigualdades envolvendo:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Anexo C §C.10 (AC.19)
- **Veredito:** CONFERE (reprise direta de Anexo C §C.10/AC.19 — mesma nota sobre a contagem de 2 modos refutada pela âncora D1, real: 3 modos)

### [AF.10]  (linha 139)

```
$\mathcal{B}(r)=\beta_1+2\beta_2 r+\beta_3 r^2.$
```

- **Seção:** F.3.3 Ausência de Ghost Escalar
- **Contexto:** …- $m^2F(\chi).$ / Essa condição é particularmente sensível a:
- **Segue:** Se \mathcal{B}(r)=0, sistema degenera (ponto crítico).
- **Classe (sugerida):** pendente
- **Depende de:** Anexo D §D.5 (AD.10); âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE SOB HIPÓTESE — a claim de que a degenerescência em B(r)=0 é um "ponto crítico" é consistente com o benchmark C da âncora D1 (ramo algébrico, r=r★: par degenerado, kN∼10⁻¹⁶); mas a caracterização de B(r) como o que a saúde do ghost é "particularmente sensível" superclaima — D1 mostra que o par fantasma dos benchmarks A/B persiste nos DOIS lados de qualquer cruzamento de B(r), não é B(r) que decide a saúde geral

### [AF.11]  (linha 145)

```
$c_{s,\pm}^2>0.$
```

- **Seção:** F.3.4 Estabilidade de Gradiente
- **Contexto:** …Se \mathcal{B}(r)=0, sistema degenera (ponto crítico). / **F.3.4 Estabilidade de Gradiente**
- **Segue:** Tipicamente impõe:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Anexo C §C.8/C.10 (AC.14/20)
- **Veredito:** CONFERE (reprise de AC.14/20)

### [AF.12]  (linha 155)

```
$m^2F(\chi) \to 0 \quad\text{ou}\quad r \to 0,\infty.$
```

- **Seção:** F.3.4 Estabilidade de Gradiente
- **Contexto:** …- \beta_2 não dominante com sinal incorreto. / Região de instabilidade aparece quando:
- **Segue:** **F.4 Regiões Estruturalmente Seguras**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE SOB HIPÓTESE (qualitativa, plausível como comportamento assintótico genérico, não derivada explicitamente aqui)

### [AF.13]  (linha 223)

```
$f\sigma_8(z)$
```

- **Seção:** F.6.1 Crescimento de Estrutura
- **Contexto:** …Agora adicionamos restrições observacionais: / **F.6.1 Crescimento de Estrutura**
- **Segue:** depende de:
- **Classe (sugerida):** pendente
- **Depende de:** Cap.8/Cap.23
- **Veredito:** CONFERE (nomeia observável já definido, Cap.8/Cap.23)

### [AF.14]  (linha 227)

```
$G_{\text{eff}}(k,z)$
```

- **Seção:** F.6.1 Crescimento de Estrutura
- **Contexto:** …[equação anterior] / depende de:
- **Segue:** Se m^2F(\chi) for grande demais:
- **Classe (sugerida):** pendente
- **Depende de:** Cap.9 (lote 2)
- **Veredito:** CONFERE (nomeia observável já definido no corpo principal — G_eff=Gμ, Cap.9/lote 2)

### [AF.15]  (linha 245)

```
$\chi_i \approx 0, \quad \dot\chi_i \approx 0.$
```

- **Seção:** F.6.2 CMB
- **Contexto:** …- χ congelado no regime primordial. / Impõe:
- **Segue:** **F.6.3 Ondas gravitacionais**
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Cap.10 (lote 2)
- **Veredito:** CONFERE (consistente com a discussão do modo adiabático do Cap.10, já confirmada no lote 2)

### [AF.16]  (linha 251)

```
$|c_T - 1| \ll 10^{-15}.$
```

- **Seção:** F.6.3 Ondas gravitacionais
- **Contexto:** …**F.6.3 Ondas gravitacionais** / LIGO/Virgo impõe:
- **Segue:** Na TDCP, como o termo de massa é ultraleve (\sim H_0),
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Cap.11 §11.4 (achado C6/lote 3)
- **Veredito:** CONFERE SOB HIPÓTESE (o argumento de supressão por massa ultraleve é válido para o modo MASSIVO não perturbar sinais de alta frequência; mas não cobre a ressalva do achado C6/lote 3 sobre o modo nominalmente massless: c_g²=1 mas c_f²=ξ²/r² — a combinação h_+ só propaga exatamente em c=1 se ξ=r, condição que precisa ser declarada antes de invocar GW170817 como "região segura" sem qualificação)

### [AF.17]  (linha 275)

```
$$ \mathcal{R}_{\text{permitida}} = \mathcal{R}_{\text{Higuchi}} \cap \mathcal{R}_{\text{no-ghost}} \cap \mathcal{R}_{\text{grad}} \cap \mathcal{R}_{\text{CMB}} \cap \mathcal{R}_{\text{late-accel}}. $$
```

- **Seção:** F.7 Representação Geométrica do Espaço de Parâmetros
- **Contexto:** …- Aceleração tardia → banda estreita m \sim H_0 / O espaço permitido é a interseção:
- **Segue:** **F.8 Insight Conceitual Importante**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (qualitativa — estrutura conceitual razoável de interseção de restrições, sem conteúdo matemático específico a verificar)

