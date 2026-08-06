# Registro de Fórmulas — Anexo A

Fonte: `manuscript/apendices/Appendix-A.md` — 30 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AA.01]  (linha 21)

```
$g_{\mu\nu}, \quad f_{\mu\nu}.$
```

- **Seção:** A.1 Estrutura Geral da Teoria Bimétrica
- **Contexto:** …**A.1 Estrutura Geral da Teoria Bimétrica** / Consideramos duas métricas dinâmicas:
- **Segue:** A ação ghost-free mais geral construída por Hassan e Rosen é:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE (definição básica, consistente com todo o corpus desde Cap.3)

### [AA.02]  (linha 25)

```
$$ S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2 \int d^4x\,\sqrt{-g}\,V(\mathcal{K}) + S_m. $$
```

- **Seção:** A.1 Estrutura Geral da Teoria Bimétrica
- **Contexto:** …[equação anterior] / A ação ghost-free mais geral construída por Hassan e Rosen é:
- **Segue:** onde:
- **Classe (sugerida):** importada-da-literatura
- **Depende de:** Cap.3/Cap.14/Cap.20 (reprises já confirmadas)
- **Veredito:** CONFERE (ação HR completa — mesma estrutura já confirmada em todo o corpus desde Cap.3; NOTA: esta é a definição que sana a pendência do achado A4/lote 1 — o prefator m²M_eff² aqui, não m² isolado, é a origem do fator M_eff²/M_g² esperado nas equações de campo após variação)

### [AA.03]  (linha 29)

```
$M_{\mathrm{eff}}^{-2} = M_g^{-2} + M_f^{-2}.$
```

- **Seção:** A.1 Estrutura Geral da Teoria Bimétrica
- **Contexto:** …[equação anterior] / onde:
- **Segue:** O termo crucial é o potencial:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (importada — definição padrão de M_eff em gravidade bimétrica de Hassan-Rosen)

### [AA.04]  (linha 33)

```
$V(\mathcal{K}) = \sum_{n=0}^4 \beta_n e_n(\mathcal{K}),$
```

- **Seção:** A.1 Estrutura Geral da Teoria Bimétrica
- **Contexto:** …[equação anterior] / O termo crucial é o potencial:
- **Segue:** com:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (reprise — estrutura já usada em todo o corpus)

### [AA.05]  (linha 37)

```
$$ \mathcal{K}^\mu_{\ \nu} = \left(\sqrt{g^{-1}f}\right)^\mu_{\ \nu}. $$
```

- **Seção:** A.1 Estrutura Geral da Teoria Bimétrica
- **Contexto:** …[equação anterior] / com:
- **Segue:** **A.2 Definição da Matriz Raiz**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de K como raiz matricial)

### [AA.06]  (linha 43)

```
$(g^{-1}f)^\mu_{\ \nu} = g^{\mu\alpha} f_{\alpha\nu}.$
```

- **Seção:** A.2 Definição da Matriz Raiz
- **Contexto:** …**A.2 Definição da Matriz Raiz** / Definimos:
- **Segue:** Queremos uma matriz \mathcal{K} tal que:
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (definição algébrica direta)

### [AA.07]  (linha 47)

```
$$ \mathcal{K}^\mu_{\ \alpha}\mathcal{K}^\alpha_{\ \nu} = (g^{-1}f)^\mu_{\ \nu}. $$
```

- **Seção:** A.2 Definição da Matriz Raiz
- **Contexto:** …[equação anterior] / Queremos uma matriz \mathcal{K} tal que:
- **Segue:** Isto é, \mathcal{K} é a raiz matricial da matriz mista g^{-1}f.
- **Classe (sugerida):** pendente
- **Depende de:** AA.05/06
- **Veredito:** CONFERE (definição da raiz matricial — consistente com AA.05)

### [AA.08]  (linha 55)

```
$e_0 = 1,$
```

- **Seção:** A.3 Polinômios Elementares Simétricos
- **Contexto:** …**A.3 Polinômios Elementares Simétricos** / Se \lambda_i são autovalores de \mathcal{K}, definimos:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de polinômio simétrico elementar)

### [AA.09]  (linha 57)

```
$e_1 = \sum_i \lambda_i = [\mathcal{K}],$
```

- **Seção:** A.3 Polinômios Elementares Simétricos
- **Contexto:** …Se \lambda_i são autovalores de \mathcal{K}, definimos: / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão)

### [AA.10]  (linha 59)

```
$e_2 = \sum_{i<j} \lambda_i \lambda_j,$
```

- **Seção:** A.3 Polinômios Elementares Simétricos
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão)

### [AA.11]  (linha 61)

```
$e_3 = \sum_{i<j<k} \lambda_i \lambda_j \lambda_k,$
```

- **Seção:** A.3 Polinômios Elementares Simétricos
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão)

### [AA.12]  (linha 63)

```
$e_4 = \prod_i \lambda_i = \det \mathcal{K}.$
```

- **Seção:** A.3 Polinômios Elementares Simétricos
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** Esses polinômios são as únicas combinações que mantêm:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão)

### [AA.13]  (linha 75)

```
$e_1 = [\mathcal{K}],$
```

- **Seção:** A.4 Forma Explícita em Índices
- **Contexto:** …**A.4 Forma Explícita em Índices** / Os polinômios podem ser escritos como:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** AA.09
- **Veredito:** CONFERE (reprise em forma de traço)

### [AA.14]  (linha 77)

```
$e_2 = \frac12\left([\mathcal{K}]^2 - [\mathcal{K}^2]\right),$
```

- **Seção:** A.4 Forma Explícita em Índices
- **Contexto:** …Os polinômios podem ser escritos como: / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (verificado: identidade de Newton padrão e2=(p1²-p2)/2, com p1=[K], p2=[K²] — forma correta)

### [AA.15]  (linha 79)

```
$$ e_3 = \frac16\left([\mathcal{K}]^3 - 3[\mathcal{K}][\mathcal{K}^2] + 2[\mathcal{K}^3]\right), $$
```

- **Seção:** A.4 Forma Explícita em Índices
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (verificado: identidade de Newton padrão e3=(p1³-3p1p2+2p3)/6 — forma correta)

### [AA.16]  (linha 81)

```
$e_4 = \det \mathcal{K}.$
```

- **Seção:** A.4 Forma Explícita em Índices
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** AA.12
- **Veredito:** CONFERE (reprise)

### [AA.17]  (linha 85)

```
$[\mathcal{K}] = \mathcal{K}^\mu_{\ \mu}.$
```

- **Seção:** A.4 Forma Explícita em Índices
- **Contexto:** …[equação anterior] / onde:
- **Segue:** **A.5 Eliminação do Ghost de Boulware--Deser**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de traço)

### [AA.18]  (linha 115)

```
$ds_g^2 = -N_g^2 dt^2 + a^2 \delta_{ij} dx^i dx^j,$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …**A.6 Especialização ao Caso FLRW** / Assumimos:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** postulado
- **Depende de:** —
- **Veredito:** CONFERE (ansatz FLRW padrão com lapse)

### [AA.19]  (linha 117)

```
$ds_f^2 = -N_f^2 dt^2 + b^2 \delta_{ij} dx^i dx^j.$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …Assumimos: / [equação anterior]
- **Segue:** Então:
- **Classe (sugerida):** postulado
- **Depende de:** —
- **Veredito:** CONFERE (ansatz FLRW padrão com lapse)

### [AA.20]  (linha 121)

```
$(g^{-1}f)^0_{\ 0} = \frac{N_f^2}{N_g^2},$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …[equação anterior] / Então:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AA.18/19
- **Veredito:** CONFERE (álgebra verificada: g^00 f_00 = (-1/N_g²)(-N_f²) = N_f²/N_g² ✓)

### [AA.21]  (linha 123)

```
$(g^{-1}f)^i_{\ j} = \frac{b^2}{a^2}\delta^i_j.$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …Então: / [equação anterior]
- **Segue:** Logo:
- **Classe (sugerida):** pendente
- **Depende de:** AA.18/19
- **Veredito:** CONFERE (álgebra verificada: g^ij f_kj = (δ^ik/a²)(b²δ_kj) = (b²/a²)δ^i_j ✓)

### [AA.22]  (linha 127)

```
$\mathcal{K}^\mu_{\ \nu} = \mathrm{diag}(\xi, r, r, r),$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** com:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AA.20/21/23
- **Veredito:** CONFERE (consequência da raiz quadrada de uma matriz diagonal com entradas positivas — consistente com AA.23)

### [AA.23]  (linha 131)

```
$\xi = \frac{N_f}{N_g}, \quad r = \frac{b}{a}.$
```

- **Seção:** A.6 Especialização ao Caso FLRW
- **Contexto:** …[equação anterior] / com:
- **Segue:** **A.7 Polinômios no Fundo FLRW**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (definições fundamentais de ξ e r — consistentes com todo o corpus; esta é a definição canônica que os capítulos posteriores citam, ex. Cap.14 §14.2)

### [AA.24]  (linha 137)

```
$e_1 = \xi + 3r,$
```

- **Seção:** A.7 Polinômios no Fundo FLRW
- **Contexto:** …**A.7 Polinômios no Fundo FLRW** / Autovalores: \{\xi, r, r, r\}.
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** AA.09, AA.22/23
- **Veredito:** CONFERE (álgebra verificada: e1=ξ+r+r+r=ξ+3r — mesmos valores já confirmados em Cap.14 §14.2/lote 3)

### [AA.25]  (linha 139)

```
$e_2 = 3\xi r + 3r^2,$
```

- **Seção:** A.7 Polinômios no Fundo FLRW
- **Contexto:** …Autovalores: \{\xi, r, r, r\}. / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** AA.10, AA.22/23
- **Veredito:** CONFERE (álgebra verificada: pares (ξ,r)×3 + (r,r)×3 = 3ξr+3r² ✓)

### [AA.26]  (linha 141)

```
$e_3 = 3\xi r^2 + r^3,$
```

- **Seção:** A.7 Polinômios no Fundo FLRW
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** AA.11, AA.22/23
- **Veredito:** CONFERE (álgebra verificada: triplas (ξ,r,r)×3 + (r,r,r)×1 = 3ξr²+r³ ✓)

### [AA.27]  (linha 143)

```
$e_4 = \xi r^3.$
```

- **Seção:** A.7 Polinômios no Fundo FLRW
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** O potencial explícito torna-se:
- **Classe (sugerida):** pendente
- **Depende de:** AA.12, AA.22/23
- **Veredito:** CONFERE (álgebra verificada: ξ·r·r·r=ξr³ ✓)

### [AA.28]  (linha 147)

```
$$ V(\xi,r) = \beta_0 + \beta_1(\xi+3r) + \beta_2(3\xi r+3r^2) + \beta_3(3\xi r^2+r^3) + \beta_4(\xi r^3). $$
```

- **Seção:** A.7 Polinômios no Fundo FLRW
- **Contexto:** …[equação anterior] / O potencial explícito torna-se:
- **Segue:** **A.8 Derivação da Densidade de Energia de Interação**
- **Classe (sugerida):** pendente
- **Depende de:** AA.04, AA.24-27
- **Veredito:** CONFERE (substituição direta e correta de AA.24-27 em V=Σβn·en)

### [AA.29]  (linha 153)

```
$$ \rho_{int}^{(g)} = - \frac{1}{\sqrt{-g}} \frac{\delta}{\delta g^{00}} \left( \sqrt{-g}V \right). $$
```

- **Seção:** A.8 Derivação da Densidade de Energia de Interação
- **Contexto:** …**A.8 Derivação da Densidade de Energia de Interação** / A densidade efetiva é obtida via:
- **Segue:** No fundo FLRW isso resulta em:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE SOB HIPÓTESE (técnica padrão de extrair densidade efetiva via derivada funcional em g^00, análoga à definição de T_00 a partir da ação de matéria; prescrição operacional razoável, não uma definição de livro-texto único)

### [AA.30]  (linha 157)

```
$$ \rho_{int}^{(g)} = m^2 M_{eff}^2 (\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3). $$
```

- **Seção:** A.8 Derivação da Densidade de Energia de Interação
- **Contexto:** …[equação anterior] / No fundo FLRW isso resulta em:
- **Segue:** Expressão usada no corpo principal.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** âncora D3 (derivations/03_dV_dNg_regra_cadeia.md); Cap.14 §F.3 (confirmado no lote 3)
- **Veredito:** CONFERE — âncora D3: verificada explicitamente por regra da cadeia completa (ξ e β4 cancelam exatamente ao converter ∂V/∂N_g em ρ_int); esta é a forma CORRETA que o Anexo B §B.5 erra ao tentar reproduzir; mesma quantidade já confirmada nos capítulos principais (Cap.14 §14.7/F.3, lote 3)

