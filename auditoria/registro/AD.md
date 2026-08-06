# Registro de Fórmulas — Anexo D

Fonte: `manuscript/apendices/Appendix-D.md` — 19 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AD.01]  (linha 31)

```
$\partial_i h^{ij} = 0, \qquad h^i_{\ i}=0.$
```

- **Seção:** D.2 Perturbações tensoriais nas duas métricas
- **Contexto:** …**D.2 Perturbações tensoriais nas duas métricas** / No fundo FLRW (com curvatura espacial nula), definimos perturbações tensoriais transversas e sem traço (TT):
- **Segue:** Para a métrica g:
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.02]  (linha 35)

```
$$ ds_g^2 = -dt^2 + a^2(t)\left(\delta_{ij}+h_{ij}\right)dx^i dx^j. $$
```

- **Seção:** D.2 Perturbações tensoriais nas duas métricas
- **Contexto:** …[equação anterior] / Para a métrica g:
- **Segue:** Para a métrica f:
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.03]  (linha 39)

```
$$ ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\left(\delta_{ij}+\ell_{ij}\right)dx^i dx^j. $$
```

- **Seção:** D.2 Perturbações tensoriais nas duas métricas
- **Contexto:** …[equação anterior] / Para a métrica f:
- **Segue:** onde h_{ij} e \ell_{ij} são tensores TT.
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.04]  (linha 51)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 b^3 N_f^{-1}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 N_g F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$
```

- **Seção:** D.3 Ação quadrática tensorial: estrutura geral
- **Contexto:** …Expandimos a ação até segunda ordem em h_{ij},\ell_{ij}. / A ação tensorial quadrática assume a forma padrão:
- **Segue:** Aqui:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.05]  (linha 63)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 \frac{b^3}{N_f}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$
```

- **Seção:** D.3 Ação quadrática tensorial: estrutura geral
- **Contexto:** …- \mathcal{M}(r,\xi) é uma função do background derivada das combinações \beta_n (abaixo). / No gauge N_g=1, fica:
- **Segue:** **D.4 Identificação da "massa efetiva" do modo massivo**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.06]  (linha 71)

```
$$ h_+ \equiv \frac{M_g h + M_f r^{3/2}\ell}{\sqrt{M_g^2 + M_f^2 r^3}}, $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …O termo que acopla (h-\ell)^2 define o modo massivo. / Para tornar isso explícito, fazemos combinação linear:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.07]  (linha 73)

```
$$ h_- \equiv \frac{M_f r^{3/2} h - M_g \ell}{\sqrt{M_g^2 + M_f^2 r^3}}. $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …Para tornar isso explícito, fazemos combinação linear: / [equação anterior]
- **Segue:** - h_+: modo efetivamente massless (a "gravidade usual").
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.08]  (linha 81)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ \mathcal{A}_+(t)\left(\dot h_+^2 - c_+^2\frac{k^2}{a^2}h_+^2\right) + \mathcal{A}_-(t)\left(\dot h_-^2 - c_-^2\frac{k^2}{a^2}h_-^2 - m_T^2(t) h_-^2\right) \right]. $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …- h_-: modo massivo (sensível ao potencial HR). / Nesta base, a ação se diagonaliza em:
- **Segue:** O modo h_+ propaga essencialmente como GR (com pequenas correções se r\neq 1 e N_f\neq 1).
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.09]  (linha 87)

```
$m_T^2(t) = m^2 F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f).$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …O modo h_+ propaga essencialmente como GR (com pequenas correções se r\neq 1 e N_f\neq 1). / O modo h_- tem uma massa efetiva:
- **Segue:** O fator \mu_T^2 depende de combinações específicas do background.
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.10]  (linha 95)

```
$\mathcal{B}(r)\equiv \beta_1 + 2\beta_2 r + \beta_3 r^2.$
```

- **Seção:** D.5 Forma explícita de \mu_T^2 em FLRW
- **Contexto:** …**D.5 Forma explícita de \mu_T^2 em FLRW** / Na literatura de bimetric cosmology, surge uma combinação recorrente:
- **Segue:** Essa é a mesma combinação que aparece na constraint de Bianchi.
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.11]  (linha 103)

```
$$ m_T^2(t)\propto m^2 F(\chi)\,\mathcal{B}(r)\,\left(\frac{1+r}{r}\right) \times \left(\text{fator de normalização em }M_g,M_f\right). $$
```

- **Seção:** D.5 Forma explícita de \mu_T^2 em FLRW
- **Contexto:** …No setor tensorial, a massa efetiva do modo relativo h-\ell é proporcional a \mathcal{B}(r) multiplicada por fatores de r e pelas escalas de Planck. / Uma forma representativa (em gauge padrão, e reabsorvendo fatores) é:
- **Segue:** O ponto-chave para a TDCP não é o detalhe exato do coeficiente --- é que:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.12]  (linha 119)

```
$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$
```

- **Seção:** D.6 Equação de movimento tensorial do modo massivo
- **Contexto:** …**D.6 Equação de movimento tensorial do modo massivo** / Da ação diagonalizada obtemos:
- **Segue:** Este é o resultado central.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.13]  (linha 131)

```
$a(t)\propto e^{Ht}, \qquad H=\text{constante}.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …**D.7 Fundo de Sitter e a condição de Higuchi** / Agora consideramos o regime acelerado tardio ou de Sitter efetivo:
- **Segue:** Para um campo spin-2 massivo em de Sitter, a análise de representações do grupo de isometrias SO(1,4) mostra que:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.14]  (linha 139)

```
$m_{\text{spin-2}}^2 \ge 2H^2.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …- a helicidade-0 do spin-2 se torna ghost se a massa for pequena demais. / O resultado é a condição de Higuchi:
- **Segue:** No contexto da TDCP:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.15]  (linha 143)

```
$$ m_{\text{spin-2}}^2 \equiv m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots). $$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …[equação anterior] / No contexto da TDCP:
- **Segue:** Portanto, o bound se torna:
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.16]  (linha 147)

```
$m^2F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f) \ge 2H^2.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …[equação anterior] / Portanto, o bound se torna:
- **Segue:** Esse é um constrangimento duro: ele seleciona uma região do espaço de parâmetros e do background.
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.17]  (linha 219)

```
$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …- Dois modos tensoriais aparecem: massless h_+ e massivo h_-. / - O modo massivo obedece:
- **Segue:** - A massa efetiva é dinâmica:
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.18]  (linha 223)

```
$m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots).$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …[equação anterior] / - A massa efetiva é dinâmica:
- **Segue:** - A estabilidade em fundo acelerado impõe Higuchi:
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AD.19]  (linha 227)

```
$m_T^2(t)\ge 2H^2.$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …[equação anterior] / - A estabilidade em fundo acelerado impõe Higuchi:
- **Segue:** Isso conecta diretamente:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

