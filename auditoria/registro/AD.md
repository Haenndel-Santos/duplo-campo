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
- **Depende de:** —
- **Veredito:** CONFERE (condição TT padrão)

### [AD.02]  (linha 35)

```
$$ ds_g^2 = -dt^2 + a^2(t)\left(\delta_{ij}+h_{ij}\right)dx^i dx^j. $$
```

- **Seção:** D.2 Perturbações tensoriais nas duas métricas
- **Contexto:** …[equação anterior] / Para a métrica g:
- **Segue:** Para a métrica f:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (perturbação TT padrão do setor g, com N_g=1 fixado)

### [AD.03]  (linha 39)

```
$$ ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\left(\delta_{ij}+\ell_{ij}\right)dx^i dx^j. $$
```

- **Seção:** D.2 Perturbações tensoriais nas duas métricas
- **Contexto:** …[equação anterior] / Para a métrica f:
- **Segue:** onde h_{ij} e \ell_{ij} são tensores TT.
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (perturbação TT do setor f, mantendo N_f geral — consistente com Cap.16/âncora D2)

### [AD.04]  (linha 51)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 b^3 N_f^{-1}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 N_g F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$
```

- **Seção:** D.3 Ação quadrática tensorial: estrutura geral
- **Contexto:** …Expandimos a ação até segunda ordem em h_{ij},\ell_{ij}. / A ação tensorial quadrática assume a forma padrão:
- **Segue:** Aqui:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md) §3.1/§3.2
- **Veredito:** CONFERE — âncora D2 §3.1: cinético e gradiente do setor f verificados exatamente (M_f²b³/N_f, com N_f=ξ quando N_g=1, e o termo de gradiente N_f²k²/b² correspondendo a c_f²=ξ²/r²); a estrutura de massa ∝(h-ℓ)² também confirmada (D2 §3.2), com M(r,ξ) deixado genérico aqui e especializado em §D.5

### [AD.05]  (linha 63)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 \frac{b^3}{N_f}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right]. $$
```

- **Seção:** D.3 Ação quadrática tensorial: estrutura geral
- **Contexto:** …- \mathcal{M}(r,\xi) é uma função do background derivada das combinações \beta_n (abaixo). / No gauge N_g=1, fica:
- **Segue:** **D.4 Identificação da "massa efetiva" do modo massivo**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AD.04; âncora D2 (derivations/02_setor_tensorial_mT2.md) §3.1
- **Veredito:** CONFERE — âncora D2 §3.1: mesma verificação de AD.04, agora com N_g=1 explícito; K_ℓℓ=M_f²b³/ξ e c_f²=ξ²/r² confirmados exatamente — verificado nesta auditoria por álgebra direta (N_f²k²/b²=(N_fa/b)²(k²/a²)=(ξ/r)²(k²/a²))

### [AD.06]  (linha 71)

```
$$ h_+ \equiv \frac{M_g h + M_f r^{3/2}\ell}{\sqrt{M_g^2 + M_f^2 r^3}}, $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …O termo que acopla (h-\ell)^2 define o modo massivo. / Para tornar isso explícito, fazemos combinação linear:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** definicao
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md) §4
- **Veredito:** CONFERE — âncora D2 §4: esta é exatamente a "base ponderada do Anexo D §D.4" que a derivação cita como a forma correta de diagonalização (superior à combinação ingênua M_gh+M_frℓ do Cap.16 §16.3, que carece do expoente r^{1/2} e da normalização adequada); ortogonalidade verificada nesta auditoria: h_+·h_- ∝ M_g(M_fr^{3/2})+(M_fr^{3/2})(-M_g)=0

### [AD.07]  (linha 73)

```
$$ h_- \equiv \frac{M_f r^{3/2} h - M_g \ell}{\sqrt{M_g^2 + M_f^2 r^3}}. $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …Para tornar isso explícito, fazemos combinação linear: / [equação anterior]
- **Segue:** - h_+: modo efetivamente massless (a "gravidade usual").
- **Classe (sugerida):** definicao
- **Depende de:** AD.06
- **Veredito:** CONFERE (par ortogonal de AD.06 — mesma verificação)

### [AD.08]  (linha 81)

```
$$ S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ \mathcal{A}_+(t)\left(\dot h_+^2 - c_+^2\frac{k^2}{a^2}h_+^2\right) + \mathcal{A}_-(t)\left(\dot h_-^2 - c_-^2\frac{k^2}{a^2}h_-^2 - m_T^2(t) h_-^2\right) \right]. $$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …- h_-: modo massivo (sensível ao potencial HR). / Nesta base, a ação se diagonaliza em:
- **Segue:** O modo h_+ propaga essencialmente como GR (com pequenas correções se r\neq 1 e N_f\neq 1).
- **Classe (sugerida):** pendente
- **Depende de:** AD.06/07; âncora D2 (derivations/02_setor_tensorial_mT2.md) §4
- **Veredito:** CONFERE SOB HIPÓTESE (usa a base ponderada correta de AD.06/07 — melhor que o Cap.16 §16.3 — mas herda a mesma ressalva geral da âncora D2 §4: os gradientes c_g²≠c_f²=ξ²/r² não são simultaneamente diagonalizáveis com a massa em geral; a forma exatamente diagonal com c_+²,c_-² escalares é aproximação, mais precisa que a do Cap.16 por usar os pesos corretos, mas não exata)

### [AD.09]  (linha 87)

```
$m_T^2(t) = m^2 F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f).$
```

- **Seção:** D.4 Identificação da "massa efetiva" do modo massivo
- **Contexto:** …O modo h_+ propaga essencialmente como GR (com pequenas correções se r\neq 1 e N_f\neq 1). / O modo h_- tem uma massa efetiva:
- **Segue:** O fator \mu_T^2 depende de combinações específicas do background.
- **Classe (sugerida):** pendente
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md) §3.3
- **Veredito:** CONFERE (estrutura correta — μ_T² explicitamente função de ξ, ao contrário da omissão do Cap.16 §16.4; a forma fechada é dada pela âncora D2 §3.3)

### [AD.10]  (linha 95)

```
$\mathcal{B}(r)\equiv \beta_1 + 2\beta_2 r + \beta_3 r^2.$
```

- **Seção:** D.5 Forma explícita de \mu_T^2 em FLRW
- **Contexto:** …**D.5 Forma explícita de \mu_T^2 em FLRW** / Na literatura de bimetric cosmology, surge uma combinação recorrente:
- **Segue:** Essa é a mesma combinação que aparece na constraint de Bianchi.
- **Classe (sugerida):** definicao
- **Depende de:** Anexo B §B.8 (AB.54)
- **Veredito:** CONFERE (definição consistente com a mesma combinação usada na constraint de Bianchi, Anexo B §B.8/AB.54 — reduz a β1+2β2r quando β3=0, família F1)

### [AD.11]  (linha 103)

```
$$ m_T^2(t)\propto m^2 F(\chi)\,\mathcal{B}(r)\,\left(\frac{1+r}{r}\right) \times \left(\text{fator de normalização em }M_g,M_f\right). $$
```

- **Seção:** D.5 Forma explícita de \mu_T^2 em FLRW
- **Contexto:** …No setor tensorial, a massa efetiva do modo relativo h-\ell é proporcional a \mathcal{B}(r) multiplicada por fatores de r e pelas escalas de Planck. / Uma forma representativa (em gauge padrão, e reabsorvendo fatores) é:
- **Segue:** O ponto-chave para a TDCP não é o detalhe exato do coeficiente --- é que:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md) §3.3/§4
- **Veredito:** ERRO DE CÁLCULO — âncora D2 §3.3/§4: esta forma (∝B(r)(1+r)/r, SEM ξ) é explicitamente substituída pela forma exata derivada: m_T²=m²F·M_eff²(1/M_g²+ξ/(M_f²r³))·r[β1+β2(ξ+r)+β3ξr] — que DEPENDE de ξ (ausente aqui) e cujo fator estrutural é β1+β2(ξ+r), não B(r)=β1+2β2r+β3r² (só coincidem se ξ=r); mesmo como "forma representativa" (o próprio texto hedge isso), está estruturalmente incompleta — falta a dependência em ξ que a âncora D2 mostra ser essencial, inclusive determinante do sinal de m_T² no benchmark testado

### [AD.12]  (linha 119)

```
$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$
```

- **Seção:** D.6 Equação de movimento tensorial do modo massivo
- **Contexto:** …**D.6 Equação de movimento tensorial do modo massivo** / Da ação diagonalizada obtemos:
- **Segue:** Este é o resultado central.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AD.08
- **Veredito:** CONFERE SOB HIPÓTESE (forma padrão de EOM para um modo massivo em FLRW, consequência direta de AD.08 — herda a mesma ressalva sobre diagonalização aproximada)

### [AD.13]  (linha 131)

```
$a(t)\propto e^{Ht}, \qquad H=\text{constante}.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …**D.7 Fundo de Sitter e a condição de Higuchi** / Agora consideramos o regime acelerado tardio ou de Sitter efetivo:
- **Segue:** Para um campo spin-2 massivo em de Sitter, a análise de representações do grupo de isometrias SO(1,4) mostra que:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE (definição padrão de fundo de Sitter)

### [AD.14]  (linha 139)

```
$m_{\text{spin-2}}^2 \ge 2H^2.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …- a helicidade-0 do spin-2 se torna ghost se a massa for pequena demais. / O resultado é a condição de Higuchi:
- **Segue:** No contexto da TDCP:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** —
- **Veredito:** CONFERE (importada — bound de Higuchi padrão para spin-2 massivo em de Sitter, Higuchi 1987)

### [AD.15]  (linha 143)

```
$$ m_{\text{spin-2}}^2 \equiv m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots). $$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …[equação anterior] / No contexto da TDCP:
- **Segue:** Portanto, o bound se torna:
- **Classe (sugerida):** definicao
- **Depende de:** AD.09
- **Veredito:** CONFERE (identificação direta, consistente com AD.09)

### [AD.16]  (linha 147)

```
$m^2F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f) \ge 2H^2.$
```

- **Seção:** D.7 Fundo de Sitter e a condição de Higuchi
- **Contexto:** …[equação anterior] / Portanto, o bound se torna:
- **Segue:** Esse é um constrangimento duro: ele seleciona uma região do espaço de parâmetros e do background.
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AD.09, AD.14; âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** CONFERE (forma do bound correta e genérica — ao contrário do Cap.16, que substitui uma forma explícita errada, aqui μ_T² permanece genérico; usar a forma exata de μ_T² da âncora D2 para avaliar a condição)

### [AD.17]  (linha 219)

```
$$ \ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0. $$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …- Dois modos tensoriais aparecem: massless h_+ e massivo h_-. / - O modo massivo obedece:
- **Segue:** - A massa efetiva é dinâmica:
- **Classe (sugerida):** pendente
- **Depende de:** AD.08
- **Veredito:** CONFERE SOB HIPÓTESE (forma padrão de EOM para um modo massivo em FLRW, consequência direta de AD.08 — herda a mesma ressalva sobre diagonalização aproximada)

### [AD.18]  (linha 223)

```
$m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots).$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …[equação anterior] / - A massa efetiva é dinâmica:
- **Segue:** - A estabilidade em fundo acelerado impõe Higuchi:
- **Classe (sugerida):** pendente
- **Depende de:** AD.09/15 (reprise em §D.11)
- **Veredito:** CONFERE (reprise de AD.09/15 na conclusão do anexo)

### [AD.19]  (linha 227)

```
$m_T^2(t)\ge 2H^2.$
```

- **Seção:** D.11 Conclusão do Anexo D
- **Contexto:** …[equação anterior] / - A estabilidade em fundo acelerado impõe Higuchi:
- **Segue:** Isso conecta diretamente:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AD.16; âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** CONFERE (reprise do bound de Higuchi genérico — âncora D2 para a forma exata de μ_T²)

