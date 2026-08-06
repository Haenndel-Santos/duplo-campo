# Registro de Fórmulas — Anexo B

Fonte: `manuscript/apendices/Appendix-B.md` — 71 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AB.01]  (linha 13)

```
$$ S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2\int d^4x\,\sqrt{-g}\,F(\chi)\,V(\mathcal{K}) + S_\chi + S_m. $$
```

- **Seção:** B.1 Ação no Fundo e Convenções
- **Contexto:** …**B.1 Ação no Fundo e Convenções** / Começamos da ação bimétrica (Hassan--Rosen) com modulação TDCP:
- **Segue:** com:
- **Classe (sugerida):** importada-da-literatura
- **Depende de:** Anexo A §A.1 (AA.02)
- **Veredito:** CONFERE (reprise da ação HR de AA.02, agora com a modulação F(χ) — consistente com Cap.3/Cap.14/Cap.20)

### [AB.02]  (linha 17)

```
$$ V(\mathcal{K})=\sum_{n=0}^4\beta_n e_n(\mathcal{K}), \qquad \mathcal{K}=\sqrt{g^{-1}f}. $$
```

- **Seção:** B.1 Ação no Fundo e Convenções
- **Contexto:** …[equação anterior] / com:
- **Segue:** O setor escalar mínimo é:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.1 (AA.04/05)
- **Veredito:** CONFERE (reprise de AA.04/05)

### [AB.03]  (linha 21)

```
$$ S_\chi = \int d^4x\,\sqrt{-g}\left[-\frac12 g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi - U(\chi)\right]. $$
```

- **Seção:** B.1 Ação no Fundo e Convenções
- **Contexto:** …[equação anterior] / O setor escalar mínimo é:
- **Segue:** Assumimos matéria S_m acoplada ao setor visível g.
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (ação padrão de campo escalar mínimo, importada)

### [AB.04]  (linha 29)

```
$ds_g^2 = -N_g^2(t)dt^2 + a^2(t)\delta_{ij}dx^i dx^j,$
```

- **Seção:** B.2 Ansatz FLRW Duplo (com lapses independentes)
- **Contexto:** …**B.2 Ansatz FLRW Duplo (com lapses independentes)** / Tomamos o fundo cosmológico mais geral homogêneo e isotrópico:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Anexo A §A.6 (AA.18)
- **Veredito:** CONFERE (reprise de AA.18)

### [AB.05]  (linha 31)

```
$ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j.$
```

- **Seção:** B.2 Ansatz FLRW Duplo (com lapses independentes)
- **Contexto:** …Tomamos o fundo cosmológico mais geral homogêneo e isotrópico: / [equação anterior]
- **Segue:** Definimos as taxas de expansão:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.6 (AA.19)
- **Veredito:** CONFERE (reprise de AA.19)

### [AB.06]  (linha 35)

```
$$ H_g \equiv \frac{1}{N_g}\frac{\dot a}{a}, \qquad H_f \equiv \frac{1}{N_f}\frac{\dot b}{b}. $$
```

- **Seção:** B.2 Ansatz FLRW Duplo (com lapses independentes)
- **Contexto:** …[equação anterior] / Definimos as taxas de expansão:
- **Segue:** E as variáveis estruturais:
- **Classe (sugerida):** definicao
- **Depende de:** Cap.14 §14.2
- **Veredito:** CONFERE (definição padrão, consistente com Cap.14 §14.2)

### [AB.07]  (linha 39)

```
$$ r(t)\equiv \frac{b(t)}{a(t)}, \qquad \xi(t)\equiv \frac{N_f(t)}{N_g(t)}. $$
```

- **Seção:** B.2 Ansatz FLRW Duplo (com lapses independentes)
- **Contexto:** …[equação anterior] / E as variáveis estruturais:
- **Segue:** A invariância por reparametrização temporal permite fixar N_g=1 ao final, mas manteremos N_g durante a variação para obt
- **Classe (sugerida):** definicao
- **Depende de:** Anexo A §A.6 (AA.23)
- **Veredito:** CONFERE (reprise de AA.23)

### [AB.08]  (linha 47)

```
$\mathcal{K}=\mathrm{diag}(\xi,r,r,r).$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …**B.3 Potencial HR no Fundo FLRW** / No Anexo A obtivemos:
- **Segue:** Logo os polinômios:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.6 (AA.22)
- **Veredito:** CONFERE (reprise de AA.22)

### [AB.09]  (linha 51)

```
$e_0=1,$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / Logo os polinômios:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** Anexo A §A.7 (AA.24-27)
- **Veredito:** CONFERE (reprise de AA.24-27, já verificada por álgebra explícita no lote 6)

### [AB.10]  (linha 53)

```
$e_1=\xi+3r,$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …Logo os polinômios: / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.24)
- **Veredito:** CONFERE (reprise de AA.24, verificada)

### [AB.11]  (linha 55)

```
$e_2=3\xi r+3r^2,$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.25)
- **Veredito:** CONFERE (reprise de AA.25, verificada)

### [AB.12]  (linha 57)

```
$e_3=3\xi r^2+r^3,$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.26)
- **Veredito:** CONFERE (reprise de AA.26, verificada)

### [AB.13]  (linha 59)

```
$e_4=\xi r^3.$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** O potencial explícito:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.27)
- **Veredito:** CONFERE (reprise de AA.27, verificada)

### [AB.14]  (linha 63)

```
$$ V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3). $$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / O potencial explícito:
- **Segue:** Na TDCP:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.28)
- **Veredito:** CONFERE (reprise de AA.28)

### [AB.15]  (linha 67)

```
$V\to F(\chi)V(\xi,r).$
```

- **Seção:** B.3 Potencial HR no Fundo FLRW
- **Contexto:** …[equação anterior] / Na TDCP:
- **Segue:** **B.4 Redução da Ação ao "minisuperspace"**
- **Classe (sugerida):** pendente
- **Depende de:** Cap.3 §3.8/Cap.14
- **Veredito:** CONFERE (modulação TDCP padrão, consistente com Cap.3 §3.8/Cap.14)

### [AB.16]  (linha 73)

```
$$ S = \int dt\,\mathcal{L}(a,\dot a,N_g;\,b,\dot b,N_f;\,\chi,\dot\chi). $$
```

- **Seção:** B.4 Redução da Ação ao "minisuperspace"
- **Contexto:** …**B.4 Redução da Ação ao "minisuperspace"** / No fundo FLRW, a ação reduz-se a uma integral temporal:
- **Segue:** **B.4.1 Termos de Einstein--Hilbert**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** —
- **Veredito:** CONFERE (afirmação estrutural padrão da redução minisuperespaço)

### [AB.17]  (linha 79)

```
$\mathcal{L}_g = -3M_g^2\,\frac{a\dot a^2}{N_g}.$
```

- **Seção:** B.4.1 Termos de Einstein--Hilbert
- **Contexto:** …**B.4.1 Termos de Einstein--Hilbert** / Para a métrica g, o termo de Einstein--Hilbert reduz (ignorando termos de borda) a:
- **Segue:** Para o setor f:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (forma padrão de redução minisuperespaço do termo de Einstein-Hilbert em FLRW — importada, consistente com o uso implícito em todo o corpus desde Cap.14)

### [AB.18]  (linha 83)

```
$\mathcal{L}_f = -3M_f^2\,\frac{b\dot b^2}{N_f}.$
```

- **Seção:** B.4.1 Termos de Einstein--Hilbert
- **Contexto:** …[equação anterior] / Para o setor f:
- **Segue:** Essas expressões são as formas padrão no minisuperspace FLRW.
- **Classe (sugerida):** pendente
- **Depende de:** AB.17 (mesma forma, setor f)
- **Veredito:** CONFERE (mesma forma padrão, setor f)

### [AB.19]  (linha 91)

```
$\sqrt{-g} = N_g a^3.$
```

- **Seção:** B.4.2 Termo de interação (potencial HR)
- **Contexto:** …**B.4.2 Termo de interação (potencial HR)** / O determinante do setor g no fundo:
- **Segue:** Logo o termo de interação na Lagrangiana é:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (verificado: det(g)=diag(-N_g²,a²,a²,a²) ⟹ det=-N_g²a⁶ ⟹ √-g=N_g a³)

### [AB.20]  (linha 95)

```
$$ \mathcal{L}_{int} = - m^2 M_{eff}^2\,(N_g a^3)\,F(\chi)\,V(\xi,r). $$
```

- **Seção:** B.4.2 Termo de interação (potencial HR)
- **Contexto:** …[equação anterior] / Logo o termo de interação na Lagrangiana é:
- **Segue:** **B.4.3 Setor escalar χ**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.19
- **Veredito:** CONFERE (substituição direta de AB.19 no termo de interação da ação)

### [AB.21]  (linha 99)

```
$$ \sqrt{-g}\left(-\frac12 g^{00}\dot\chi^2 - U(\chi)\right) = N_g a^3\left(\frac{1}{2N_g^2}\dot\chi^2 - U(\chi)\right). $$
```

- **Seção:** B.4.3 Setor escalar χ
- **Contexto:** …[equação anterior] / **B.4.3 Setor escalar χ**
- **Segue:** Portanto:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (álgebra verificada: g^00=-1/N_g² ⟹ -½g^00χ̇²=χ̇²/(2N_g²); multiplicando por √-g=N_g a³ dá exatamente a forma escrita)

### [AB.22]  (linha 103)

```
$$ \mathcal{L}_\chi = a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right). $$
```

- **Seção:** B.4.3 Setor escalar χ
- **Contexto:** …[equação anterior] / Portanto:
- **Segue:** **B.4.4 Matéria**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.21
- **Veredito:** CONFERE (simplificação algébrica direta de AB.21: N_g a³/(2N_g²)=a³/(2N_g) ✓)

### [AB.23]  (linha 109)

```
$$ \delta S_m = -\frac12\int d^4x \sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}. $$
```

- **Seção:** B.4.4 Matéria
- **Contexto:** …**B.4.4 Matéria** / Definimos a densidade de energia de matéria por:
- **Segue:** No fundo, isso implica contribuição de energia:
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de T_μν, importada)

### [AB.24]  (linha 113)

```
$\mathcal{L}_m = -N_g a^3 \rho_m.$
```

- **Seção:** B.4.4 Matéria
- **Contexto:** …[equação anterior] / No fundo, isso implica contribuição de energia:
- **Segue:** **B.4.5 Lagrangiana total no minisuperspace**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.23
- **Veredito:** CONFERE SOB HIPÓTESE (forma padrão para o setor de matéria em minisuperespaço — o passo intermediário ligando AB.23 a este resultado específico não é mostrado explicitamente, mas a forma final é a usual: T_00=ρ_m integrado com o elemento de volume N_g a³)

### [AB.25]  (linha 119)

```
$$ \mathcal{L} = -3M_g^2\,\frac{a\dot a^2}{N_g} -3M_f^2\,\frac{b\dot b^2}{N_f} - m^2 M_{eff}^2 N_g a^3 F(\chi)V(\xi,r) + a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right) - N_g a^3 \rho_m. $$
```

- **Seção:** B.4.5 Lagrangiana total no minisuperspace
- **Contexto:** …**B.4.5 Lagrangiana total no minisuperspace** / Somando:
- **Segue:** A partir dessa Lagrangiana obtemos as equações de Friedmann pela variação em relação aos lapses N_g e N_f.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.17, 18, 20, 22, 24
- **Veredito:** CONFERE (soma direta e correta de AB.17+18+20+22+24, termo a termo)

### [AB.26]  (linha 127)

```
$\frac{\partial\mathcal{L}}{\partial N_g}=0.$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …**B.5 Equação de Friedmann do Setor g (variação em N_g)** / Calculamos:
- **Segue:** Termos dependentes de N_g:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (princípio variacional padrão — N_g é multiplicador de Lagrange/lapso não-dinâmico, extremizar dá uma constraint)

### [AB.27]  (linha 133)

```
$$ \frac{\partial}{\partial N_g}\left(-3M_g^2\frac{a\dot a^2}{N_g}\right) = -3M_g^2 a\dot a^2\left(-\frac{1}{N_g^2}\right) = \frac{3M_g^2 a\dot a^2}{N_g^2}. $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …Termos dependentes de N_g: / 1. -3M_g^2 a\dot a^2/N_g → derivada:
- **Segue:** 2. interação:
- **Classe (sugerida):** pendente
- **Depende de:** AB.17
- **Veredito:** CONFERE (álgebra verificada: d/dN_g(1/N_g)=-1/N_g², sinais conferem)

### [AB.28]  (linha 137)

```
$$ \frac{\partial}{\partial N_g}\left(-m^2M_{eff}^2 N_g a^3F V\right) = - m^2 M_{eff}^2 a^3 F V. $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / 2. interação:
- **Segue:** 3. escalar:
- **Classe (sugerida):** pendente
- **Depende de:** âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** ERRO DE CÁLCULO — âncora D3: falta o termo da regra da cadeia. ξ=N_f/N_g depende explicitamente de N_g (∂ξ/∂N_g=-ξ/N_g), então V(ξ,r) TAMBÉM depende de N_g através de ξ — este cálculo trata V como se ∂ξ/∂N_g=0. A derivada completa é ∂/∂N_g(-m²M_eff²N_ga³FV) = -m²M_eff²a³F[V-ξ∂V/∂ξ], não -m²M_eff²a³FV; o próprio Anexo B, ao variar em N_f na seção seguinte (§B.6, ver AB.40), aplica a regra da cadeia corretamente — a assimetria de tratamento entre as duas variações é a origem do erro

### [AB.29]  (linha 141)

```
$$ \frac{\partial}{\partial N_g}\left(a^3\frac{1}{2N_g}\dot\chi^2\right) = -\frac{a^3}{2N_g^2}\dot\chi^2, $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / 3. escalar:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** AB.22
- **Veredito:** CONFERE (álgebra verificada: d/dN_g(1/N_g)=-1/N_g²)

### [AB.30]  (linha 143)

```
$$ \frac{\partial}{\partial N_g}\left(-a^3 N_g U\right) = - a^3 U. $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …3. escalar: / [equação anterior]
- **Segue:** 4. matéria:
- **Classe (sugerida):** pendente
- **Depende de:** AB.22
- **Veredito:** CONFERE (derivada linear trivial, verificada)

### [AB.31]  (linha 147)

```
$\frac{\partial}{\partial N_g}(-N_g a^3\rho_m)= -a^3\rho_m.$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / 4. matéria:
- **Segue:** Somando:
- **Classe (sugerida):** pendente
- **Depende de:** AB.24
- **Veredito:** CONFERE (derivada linear trivial, verificada)

### [AB.32]  (linha 151)

```
$$ \frac{3M_g^2 a\dot a^2}{N_g^2} - m^2 M_{eff}^2 a^3F V - \frac{a^3}{2N_g^2}\dot\chi^2 - a^3U - a^3\rho_m =0. $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / Somando:
- **Segue:** Dividimos por a^3 e identificamos:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.27+28+29+30+31; âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** ERRO DE CÁLCULO (herda o erro de AB.28 — âncora D3: falta o termo -ξ∂V/∂ξ; correção: substituir "-m²M_eff²a³FV" por "-m²M_eff²a³F[V-ξ∂V/∂ξ]")

### [AB.33]  (linha 155)

```
$$ H_g = \frac{1}{N_g}\frac{\dot a}{a} \quad\Rightarrow\quad \frac{\dot a^2}{N_g^2 a^2} = H_g^2. $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / Dividimos por a^3 e identificamos:
- **Segue:** Então:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.06
- **Veredito:** CONFERE (identidade trivial a partir de AB.06, elevada ao quadrado)

### [AB.34]  (linha 159)

```
$$ 3M_g^2 H_g^2 = \rho_m + \left(\frac12\frac{\dot\chi^2}{N_g^2}+U\right) + m^2M_{eff}^2 F(\chi)V(\xi,r). $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / Então:
- **Segue:** Fixando gauge N_g=1 (opcional):
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.32, AB.33; âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** ERRO DE CÁLCULO (herda o erro de AB.28/32 — âncora D3: o último termo deveria ser m²M_eff²F(χ)[V(ξ,r)-ξ∂V/∂ξ], que colapsa para m²M_eff²F(χ)(β0+3β1r+3β2r²+β3r³) — sem ξ, sem β4)

### [AB.35]  (linha 163)

```
$3M_g^2 H_g^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)},$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / Fixando gauge N_g=1 (opcional):
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** AB.34
- **Veredito:** CONFERE (forma estrutural correta — reprise de AB.34 com nomes; a definição de ρ_int^(g) na equação seguinte é que carrega o erro herdado)

### [AB.36]  (linha 167)

```
$$ \rho_\chi = \frac12\dot\chi^2+U(\chi), \qquad \rho_{int}^{(g)} = m^2M_{eff}^2F(\chi)V(\xi,r). $$
```

- **Seção:** B.5 Equação de Friedmann do Setor g (variação em N_g)
- **Contexto:** …[equação anterior] / onde:
- **Segue:** **B.6 Equação de Friedmann do Setor f (variação em N_f)**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.8 (AA.30); âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** ERRO DE CÁLCULO ; CONFLITA COM [AA.30] — âncora D3: a definição de ρ_int^(g) aqui (=m²M_eff²F(χ)V(ξ,r), retendo ξ e β4) herda a derivada incompleta de AB.28 (falta o termo -ξ∂V/∂ξ); a forma correta, m²M_eff²F(χ)(β0+3β1r+3β2r²+β3r³), coincide com o Anexo A §A.8 (AA.30) e com o que todo o corpo principal usa (ex. Cap.14 §14.7); ρ_χ=½χ̇²+U(χ) está correta (densidade padrão de Klein-Gordon)

### [AB.37]  (linha 173)

```
$\frac{\partial\mathcal{L}}{\partial N_f}=0.$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …**B.6 Equação de Friedmann do Setor f (variação em N_f)** / Agora variamos:
- **Segue:** O termo EH de f:
- **Classe (sugerida):** pendente
- **Depende de:** AB.26
- **Veredito:** CONFERE (princípio variacional padrão, análogo a AB.26)

### [AB.38]  (linha 177)

```
$$ -3M_f^2\frac{b\dot b^2}{N_f} \quad\Rightarrow\quad \frac{\partial}{\partial N_f} = \frac{3M_f^2 b\dot b^2}{N_f^2}. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / O termo EH de f:
- **Segue:** O termo de interação depende de N_f via:
- **Classe (sugerida):** pendente
- **Depende de:** AB.18
- **Veredito:** CONFERE (álgebra verificada, análoga a AB.27)

### [AB.39]  (linha 181)

```
$\xi = \frac{N_f}{N_g}.$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / O termo de interação depende de N_f via:
- **Segue:** Como V(\xi,r) depende de \xi, então:
- **Classe (sugerida):** pendente
- **Depende de:** AB.07
- **Veredito:** CONFERE (reprise de AB.07, destacada aqui pela dependência relevante à regra da cadeia que segue)

### [AB.40]  (linha 185)

```
$$ \frac{\partial}{\partial N_f}\left(-m^2M_{eff}^2N_ga^3F V(\xi,r)\right) = -m^2M_{eff}^2N_ga^3F \frac{\partial V}{\partial \xi} \frac{\partial\xi}{\partial N_f}. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Como V(\xi,r) depende de \xi, então:
- **Segue:** Mas:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.20, AB.39
- **Veredito:** CONFERE (regra da cadeia aplicada corretamente — diferente de AB.28, aqui não há termo de produto adicional pois N_g,a,F não dependem de N_f, só ξ dentro de V depende)

### [AB.41]  (linha 189)

```
$\frac{\partial\xi}{\partial N_f}=\frac{1}{N_g}.$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Mas:
- **Segue:** Logo:
- **Classe (sugerida):** pendente
- **Depende de:** AB.39
- **Veredito:** CONFERE (álgebra verificada: derivada parcial trivial de ξ=N_f/N_g em relação a N_f, com N_g fixo)

### [AB.42]  (linha 193)

```
$$ \frac{\partial\mathcal{L}_{int}}{\partial N_f} = -m^2M_{eff}^2a^3F \frac{\partial V}{\partial \xi}. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** Então a equação N_f é:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.40, AB.41
- **Veredito:** CONFERE (álgebra verificada: substituindo AB.41 em AB.40, N_g cancela exatamente)

### [AB.43]  (linha 197)

```
$$ \frac{3M_f^2 b\dot b^2}{N_f^2} - m^2M_{eff}^2a^3F\frac{\partial V}{\partial \xi} =0. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Então a equação N_f é:
- **Segue:** Dividimos por a^3, escrevemos b=ra:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.38, AB.42
- **Veredito:** CONFERE (soma direta e correta de AB.38+AB.42)

### [AB.44]  (linha 201)

```
$$ \frac{3M_f^2 r^3 a^3}{a^3}\left(\frac{\dot b^2}{N_f^2 b^2}\right) = m^2M_{eff}^2F\frac{\partial V}{\partial \xi}. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Dividimos por a^3, escrevemos b=ra:
- **Segue:** Identificando:
- **Classe (sugerida):** pendente
- **Depende de:** AB.43
- **Veredito:** CONFERE (álgebra verificada: 3M_f²bḃ²/(N_f²a³) com b=ra reduz a 3M_f²r³(ḃ²/(N_f²b²)) — a manipulação a³/a³=1 é um passo redundante mas não afeta a correção)

### [AB.45]  (linha 205)

```
$H_f = \frac{1}{N_f}\frac{\dot b}{b},$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Identificando:
- **Segue:** obtemos:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.06
- **Veredito:** CONFERE (reprise de AB.06)

### [AB.46]  (linha 209)

```
$$ 3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\frac{\partial V}{\partial \xi}. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / obtemos:
- **Segue:** Agora calculamos \partial V/\partial\xi explicitamente:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.44, AB.45
- **Veredito:** CONFERE (substituição direta de AB.45 em AB.44)

### [AB.47]  (linha 213)

```
$$ V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3). $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Agora calculamos \partial V/\partial\xi explicitamente:
- **Segue:** Logo:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.7 (AA.28)
- **Veredito:** CONFERE (reprise de AA.28)

### [AB.48]  (linha 217)

```
$$ \frac{\partial V}{\partial\xi} = \beta_1 +3\beta_2 r +3\beta_3 r^2 +\beta_4 r^3. $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** Portanto:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.47
- **Veredito:** CONFERE (álgebra verificada: derivada parcial de AB.47 em relação a ξ, termo a termo — ∂V/∂ξ=β1+3β2r+3β3r²+β4r³ ✓)

### [AB.49]  (linha 221)

```
$$ 3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_1+3\beta_2 r+3\beta_3 r^2+\beta_4 r^3\right). $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Portanto:
- **Segue:** Dividindo por r^3:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.46, AB.48
- **Veredito:** CONFERE (substituição direta de AB.48 em AB.46)

### [AB.50]  (linha 225)

```
$$ 3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right). $$
```

- **Seção:** B.6 Equação de Friedmann do Setor f (variação em N_f)
- **Contexto:** …[equação anterior] / Dividindo por r^3:
- **Segue:** Esta é a equação de Friedmann do setor f.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.49; verificação cruzada §3.4 da âncora D3
- **Veredito:** CONFERE (álgebra verificada: divisão termo a termo de AB.49 por r³ ✓ — esta é a equação de Friedmann do setor f, já usada como checagem cruzada independente pela âncora D3 §3.4)

### [AB.51]  (linha 237)

```
$$ M_g^2(2\dot H_g + 3H_g^2) = - (p_m + p_\chi + p_{int}^{(g)}), $$
```

- **Seção:** B.7 Equações de aceleração (variação em a e b)
- **Contexto:** …Para obter equações dinâmicas (análogas à equação de Raychaudhuri), variamos a Lagrangiana em relação a a e b. / De modo esquemático, para g:
- **Segue:** onde:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** INCOMPLETA (o próprio texto declara isso como esquemático — "de modo esquemático" — e que "as expressões completas são extensas"; a forma segue o padrão esperado de uma equação tipo Raychaudhuri para um fluido efetivo, mas p_int^(g) nunca é calculado explicitamente aqui nem em nenhum lugar anterior do corpus)

### [AB.52]  (linha 241)

```
$p_\chi=\frac12\dot\chi^2-U(\chi),$
```

- **Seção:** B.7 Equações de aceleração (variação em a e b)
- **Contexto:** …[equação anterior] / onde:
- **Segue:** e p_{int}^{(g)} é obtido pela projeção espacial do tensor de interação.
- **Classe (sugerida):** pendente
- **Depende de:** AB.36 (ρ_χ)
- **Veredito:** CONFERE (pressão padrão de Klein-Gordon, complementar a ρ_χ=½χ̇²+U de AB.36)

### [AB.53]  (linha 255)

```
$\nabla_g^\mu X_{\mu\nu}=0$
```

- **Seção:** B.8 Dedução da Constraint de Bianchi (passo a passo)
- **Contexto:** …O termo de interação produz tensores efetivos X_{\mu\nu} e \tilde{X}_{\mu\nu}. / No formalismo HR, a consistência exige:
- **Segue:** (e de forma equivalente no setor f).
- **Classe (sugerida):** pendente
- **Depende de:** Cap.4 §4.4 (confirmado no lote 1, achado A1)
- **Veredito:** CONFERE (importada — resultado padrão do formalismo HR: invariância por difeomorfismo do potencial de interação implica esta identidade tipo Bianchi; consistente com Cap.4 §4.4, já confirmado no lote 1 como a base correta do achado A1 — não há troca de energia entre setores, Q≡0)

### [AB.54]  (linha 263)

```
$$ \left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0. $$
```

- **Seção:** B.8 Dedução da Constraint de Bianchi (passo a passo)
- **Contexto:** …No fundo FLRW, isso implica uma relação entre r,\xi,H_g,H_f. / O resultado padrão (para bimetric HR) é:
- **Segue:** Vamos mostrar por que essa estrutura aparece.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.53; Cap.5/Cap.14 (lotes 1/3)
- **Veredito:** CONFERE SOB HIPÓTESE (resultado padrão de gravidade bimétrica HR — Comelli-Nesti-Pilo e sucessores; a derivação explícita de AB.53 até esta forma polinomial específica não é mostrada em detalhe, "vamos mostrar por que" é seguido de um argumento qualitativo, não uma conta passo a passo — mas a forma é consistente com o uso confirmado em todo o corpo principal, ex. Cap.5/Cap.14, lotes 1/3)

### [AB.55]  (linha 271)

```
$$ \nabla_g^\mu T^{(m)}_{\mu\nu}=0, \quad \nabla_g^\mu T^{(\chi)}_{\mu\nu} = (\Box\chi-U')\partial_\nu\chi, $$
```

- **Seção:** B.8.1 Forma física da conservação
- **Contexto:** …**B.8.1 Forma física da conservação** / No setor g, assumimos matéria conservada:
- **Segue:** logo a conservação total exige que a divergência do termo de interação seja cancelada pela fonte de \chi quando F(\chi) 
- **Classe (sugerida):** postulado
- **Depende de:** —
- **Veredito:** CONFERE (identidades padrão: conservação de matéria por acoplamento mínimo, e a identidade de Klein-Gordon ∇^μT^(χ)_μν=(□χ-U')∂νχ — que se anula on-shell)

### [AB.56]  (linha 283)

```
$$ \left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0 $$
```

- **Seção:** B.8.2 Decomposição em ramos
- **Contexto:** …**B.8.2 Decomposição em ramos** / A condição:
- **Segue:** implica:
- **Classe (sugerida):** pendente
- **Depende de:** AB.54
- **Veredito:** CONFERE SOB HIPÓTESE (reprise de AB.54)

### [AB.57]  (linha 289)

```
$$ \beta_1 + 2\beta_2 r + \beta_3 r^2 = 0 \quad\Rightarrow\quad r = \text{constante}. $$
```

- **Seção:** (A) Ramo Algébrico
- **Contexto:** …implica: / **(A) Ramo Algébrico**
- **Segue:** Nesse ramo, a razão de escalas é fixada por uma equação quadrática.
- **Classe (sugerida):** pendente
- **Depende de:** AB.56; Cap.14 §14.10 (âncora D5)
- **Veredito:** CONFERE (consequência lógica direta de AB.56: uma equação algébrica em r fixa r em suas raízes, que são constantes — consistente com a "raiz r★" usada extensivamente em Cap.14, âncora D5)

### [AB.58]  (linha 297)

```
$H_g = \xi H_f.$
```

- **Seção:** (B) Ramo Dinâmico
- **Contexto:** …Isso geralmente gera um termo efetivo semelhante a Λ (combinando \beta_n). / **(B) Ramo Dinâmico**
- **Segue:** Aqui, r(t) pode evoluir.
- **Classe (sugerida):** pendente
- **Depende de:** AB.56; Cap.14 §14.10
- **Veredito:** CONFERE (a outra alternativa lógica de AB.56 — consistente com a constraint usada no Cap.14 §14.10, âncora D5)

### [AB.59]  (linha 307)

```
$r=\frac{b}{a}.$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …**B.9 Dinâmica de r(t) e relação com o ramo dinâmico** / Definimos:
- **Segue:** Derivando:
- **Classe (sugerida):** definicao
- **Depende de:** AB.07
- **Veredito:** CONFERE (reprise de AB.07)

### [AB.60]  (linha 311)

```
$$ \dot r = \frac{\dot b}{a} - \frac{b\dot a}{a^2} = r\left(\frac{\dot b}{b} - \frac{\dot a}{a}\right). $$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …[equação anterior] / Derivando:
- **Segue:** Substituindo:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.59
- **Veredito:** CONFERE (álgebra verificada: regra do quociente padrão, d/dt(b/a)=ḃ/a-bȧ/a²=r(ḃ/b-ȧ/a))

### [AB.61]  (linha 315)

```
$\frac{\dot b}{b}=N_f H_f, \quad \frac{\dot a}{a}=N_g H_g.$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …[equação anterior] / Substituindo:
- **Segue:** Logo:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.06
- **Veredito:** CONFERE (rearranjo direto de AB.06)

### [AB.62]  (linha 319)

```
$\dot r = r(N_f H_f - N_g H_g) = rN_g(\xi H_f - H_g).$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.60, AB.61, AB.07
- **Veredito:** CONFERE (álgebra verificada: substituindo AB.61 em AB.60 e fatorando N_g com ξ=N_f/N_g)

### [AB.63]  (linha 321)

```
$Se N_g=1:$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …Logo: / [equação anterior]
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** B.2
- **Veredito:** ARTEFATO DE CONVERSÃO (prosa dentro de $, mesmo padrão de "Se Q_0>0:" no Cap.4/Cap.9 — condição de gauge N_g=1, válida por invariância de reparametrização temporal já mencionada em B.2)

### [AB.64]  (linha 323)

```
$\dot r = r(\xi H_f - H_g).$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …[equação anterior] / [equação anterior]
- **Segue:** Portanto, no ramo dinâmico H_g=\xi H_f:
- **Classe (sugerida):** pendente
- **Depende de:** AB.62
- **Veredito:** CONFERE (consequência direta de AB.62 com N_g=1)

### [AB.65]  (linha 327)

```
$\dot r=0$
```

- **Seção:** B.9 Dinâmica de r(t) e relação com o ramo dinâmico
- **Contexto:** …[equação anterior] / Portanto, no ramo dinâmico H_g=\xi H_f:
- **Segue:** se a igualdade for estrita em todo tempo.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AB.58, AB.64; âncora D5 (derivations/05_rdot_ramo_dinamico.md)
- **Veredito:** CONFERE — âncora D5: ṙ≡0 verificado exatamente por substituição direta de H_g=ξH_f (o "ramo dinâmico", AB.58) em AB.64; esta é a derivação CORRETA que o Cap.14 §14.12 (lote 3, achado C1) contorna incorretamente ao trocar a constraint por uma condição não-equivalente (H_b-ξH_g=0) — o Anexo B, na fonte, já tinha o resultado certo; o erro do Cap.14 é dele mesmo, não herdado daqui

### [AB.66]  (linha 343)

```
$f_{\mu\nu} = c^2 g_{\mu\nu}.$
```

- **Seção:** B.10 Limite Proporcional como Subcaso Analítico
- **Contexto:** …**B.10 Limite Proporcional como Subcaso Analítico** / Um subcaso útil é:
- **Segue:** No fundo FLRW:
- **Classe (sugerida):** pendente
- **Depende de:** Cap.13/Cap.14 (lote 3)
- **Veredito:** CONFERE (mesmo ansatz proporcional já usado em Cap.13/Cap.14, lote 3)

### [AB.67]  (linha 347)

```
$b = c a \Rightarrow r=c=\text{constante}.$
```

- **Seção:** B.10 Limite Proporcional como Subcaso Analítico
- **Contexto:** …[equação anterior] / No fundo FLRW:
- **Segue:** Nesse caso, o potencial gera densidade efetiva constante (se F constante):
- **Classe (sugerida):** pendente
- **Depende de:** AB.66
- **Veredito:** CONFERE (consequência direta de AB.66 no fundo FLRW: b²=c²a² ⟹ b=ca ⟹ r=b/a=c)

### [AB.68]  (linha 351)

```
$$ \rho_{int}^{(g)} = m^2M_{eff}^2F(\chi) (\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3). $$
```

- **Seção:** B.10 Limite Proporcional como Subcaso Analítico
- **Contexto:** …[equação anterior] / Nesse caso, o potencial gera densidade efetiva constante (se F constante):
- **Segue:** Na TDCP, se F(\chi) evolui lentamente, isso se torna uma "Λ efetiva" quase constante, oferecendo ponte formal direta com
- **Classe (sugerida):** pendente
- **Depende de:** Anexo A §A.8 (AA.30); âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** CONFERE — âncora D3: usa corretamente a forma sem ξ e sem β4 (idêntica ao Anexo A §A.8/AA.30, com r→c), diferente da citação errada de AB.36 na mesma seção B.5; NOTA: evidência adicional a favor do achado D3 — a forma correta reaparece aqui, de memória, dentro do próprio Anexo B

### [AB.69]  (linha 361)

```
$> 3M_g^2 H_g^2=\rho_m+\rho_\chi+\rho_{int}^{(g)}.$
```

- **Seção:** B.11 Conclusão do Anexo B
- **Contexto:** …Neste anexo derivamos, a partir da ação reduzida no minisuperspace: / 1. Equação de Friedmann do setor g:
- **Segue:** 2. Equação de Friedmann do setor f:
- **Classe (sugerida):** pendente
- **Depende de:** AB.35
- **Veredito:** CONFERE (reprise estrutural de AB.35 — mesma nota: a definição de ρ_int^(g) é que carrega o erro, não esta forma)

### [AB.70]  (linha 365)

```
$> 3M_f^2 H_f^2=\rho_{int}^{(f)}.$
```

- **Seção:** B.11 Conclusão do Anexo B
- **Contexto:** …[equação anterior] / 2. Equação de Friedmann do setor f:
- **Segue:** 3. Constraint de Bianchi, que impõe a estrutura de ramos:
- **Classe (sugerida):** pendente
- **Depende de:** AB.50
- **Veredito:** CONFERE (reprise compacta e correta do resultado de AB.50, agora nomeado ρ_int^(f))

### [AB.71]  (linha 369)

```
$> (\beta_1+2\beta_2 r+\beta_3 r^2)(H_g-\xi H_f)=0.$
```

- **Seção:** B.11 Conclusão do Anexo B
- **Contexto:** …[equação anterior] / 3. Constraint de Bianchi, que impõe a estrutura de ramos:
- **Segue:** Esses resultados são a base matemática do corpo principal da TDCP, e são a fundação para:
- **Classe (sugerida):** pendente
- **Depende de:** AB.54/56
- **Veredito:** CONFERE SOB HIPÓTESE (reprise de AB.54/56)

