# Registro de Fórmulas — Anexo C

Fonte: `manuscript/apendices/Appendix-C.md` — 24 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AC.01]  (linha 55)

```
$$ \bar g_{\mu\nu}dx^\mu dx^\nu = -dt^2 + a^2(t)\delta_{ij}dx^i dx^j, $$
```

- **Seção:** C.2 Perturbações escalares: duas métricas + χ
- **Contexto:** …**C.2 Perturbações escalares: duas métricas + χ** / Trabalharemos no espaço-tempo com simetria de fundo FLRW:
- **Segue:** [equação seguinte]
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.02]  (linha 57)

```
$$ \bar f_{\mu\nu}dx^\mu dx^\nu = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j. $$
```

- **Seção:** C.2 Perturbações escalares: duas métricas + χ
- **Contexto:** …Trabalharemos no espaço-tempo com simetria de fundo FLRW: / [equação anterior]
- **Segue:** Definimos perturbações escalares no espaço de Fourier (modo k).
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.03]  (linha 65)

```
$$ ds_g^2 = -(1+2\Phi_g)dt^2 + 2a\,\partial_i B_g\,dt\,dx^i + a^2\left[(1-2\Psi_g)\delta_{ij} + 2\partial_i\partial_j E_g\right]dx^i dx^j. $$
```

- **Seção:** C.2.1 Setor g (escalar)
- **Contexto:** …**C.2.1 Setor g (escalar)** / No gauge genérico:
- **Segue:** **C.2.2 Setor f (escalar)**
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.04]  (linha 69)

```
$$ ds_f^2 = -N_f^2(1+2\Phi_f)dt^2 + 2bN_f\,\partial_i B_f\,dt\,dx^i + b^2\left[(1-2\Psi_f)\delta_{ij} + 2\partial_i\partial_j E_f\right]dx^i dx^j. $$
```

- **Seção:** C.2.2 Setor f (escalar)
- **Contexto:** …[equação anterior] / **C.2.2 Setor f (escalar)**
- **Segue:** **C.2.3 Campo χ**
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.05]  (linha 73)

```
$\chi(t,\mathbf{x}) = \bar\chi(t) + \delta\chi(t,\mathbf{x}).$
```

- **Seção:** C.2.3 Campo χ
- **Contexto:** …[equação anterior] / **C.2.3 Campo χ**
- **Segue:** **C.3 Escolha de gauge e contagem de variáveis**
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.06]  (linha 111)

```
$$ \Delta\Psi \equiv \Psi_f - \Psi_g, \qquad \Delta E \equiv E_f - E_g, \qquad \delta\chi. $$
```

- **Seção:** C.4 Variáveis invariantes e base física
- **Contexto:** …- e a flutuação de χ. / Uma escolha padrão é trabalhar com:
- **Segue:** E fixar um gauge para remover redundâncias, por exemplo:
- **Classe (sugerida):** definicao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.07]  (linha 125)

```
$S = S^{(0)} + S^{(1)} + S^{(2)} + \cdots,$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …**C.5 Estrutura da ação quadrática** / Ao expandir a ação até segunda ordem:
- **Segue:** o termo S^{(1)}=0 quando o fundo satisfaz as equações de Friedmann (Anexo B).
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.08]  (linha 133)

```
$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q_i\,K_{ij}(t,k)\,\dot Q_j - Q_i\,\Omega_{ij}(t,k)\,Q_j \right], $$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …O termo relevante para estabilidade é S^{(2)}. / A forma geral para 2 modos escalares Q_i (após integrar constraints) é:
- **Segue:** onde:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.09]  (linha 145)

```
$\Omega_{ij} = \frac{k^2}{a^2}G_{ij}(t) + M_{ij}(t).$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …- \Omega_{ij} contém termos de gradiente (\propto k^2) e massa. / É comum decompor:
- **Segue:** **C.6 Integração das variáveis não-dinâmicas**
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.10]  (linha 159)

```
$\mathcal{C}_A(Q,\dot Q;k,t)=0.$
```

- **Seção:** C.6 Integração das variáveis não-dinâmicas
- **Contexto:** …entram sem derivadas temporais. Elas são multiplicadores de Lagrange. / Variação em relação a elas gera equações algébricas (constraints) do tipo:
- **Segue:** Resolvendo essas constraints e substituindo de volta na ação, obtemos a ação reduzida.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.11]  (linha 205)

```
$$ F(\chi)>0, \qquad \left|\frac{\dot F}{F}\right| \ll H, \qquad \left|\frac{F'}{F}\right|\Delta\chi \ll 1. $$
```

- **Seção:** Interpretação na TDCP
- **Contexto:** …F(\chi) deve ser positiva e variar lentamente para evitar mistura forte e inversão de sinal efetiva. / Condições práticas (regime adiabático):
- **Segue:** **C.8 Velocidade do som e estabilidade de gradiente**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.12]  (linha 213)

```
$\det\left(c_s^2 K - G\right)=0.$
```

- **Seção:** C.8 Velocidade do som e estabilidade de gradiente
- **Contexto:** …O termo de gradiente define G_{ij}. / Os modos propagantes têm velocidades do som obtidas de:
- **Segue:** Ou seja, os c_s^2 são autovalores da matriz:
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.13]  (linha 217)

```
$K^{-1}G.$
```

- **Seção:** C.8 Velocidade do som e estabilidade de gradiente
- **Contexto:** …[equação anterior] / Ou seja, os c_s^2 são autovalores da matriz:
- **Segue:** **Condição de estabilidade de gradiente**
- **Classe (sugerida):** pendente
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.14]  (linha 223)

```
$c_{s,\pm}^2 > 0.$
```

- **Seção:** Condição de estabilidade de gradiente
- **Contexto:** …**Condição de estabilidade de gradiente** / Para evitar instabilidade exponencial em escalas sub-horizonte:
- **Segue:** Além disso, em teoria relativística estável, usualmente esperamos:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.15]  (linha 227)

```
$c_s^2 \le 1$
```

- **Seção:** Condição de estabilidade de gradiente
- **Contexto:** …[equação anterior] / Além disso, em teoria relativística estável, usualmente esperamos:
- **Segue:** (não estritamente necessário em teorias efetivas, mas desejável para evitar superluminalidade sistemática e problemas de
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.16]  (linha 235)

```
$\exp\left(|c_s| \frac{k}{a} t\right),$
```

- **Seção:** Interpretação física
- **Contexto:** …**Interpretação física** / - Se c_s^2<0, então para k/a grande, o modo cresce como:
- **Segue:** o que destrói a teoria imediatamente.
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.17]  (linha 251)

```
$m_{eff}^2 \ge 2H^2.$
```

- **Seção:** C.9 Conexão com Higuchi e com o modo helicidade-0
- **Contexto:** …**C.9 Conexão com Higuchi e com o modo helicidade-0** / Em fundos próximos a de Sitter, para um campo spin-2 massivo, a helicidade-0 é saudável apenas se:
- **Segue:** Quando essa condição é violada:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.18]  (linha 261)

```
$K_{11} \to 0 \quad \text{em } m_{eff}^2\to 2H^2,$
```

- **Seção:** C.9 Conexão com Higuchi e com o modo helicidade-0
- **Contexto:** …- e torna-se ghost. / Logo, em linguagem da matriz cinética:
- **Segue:** e se m_{eff}^2<2H^2, então K_{11}<0.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.19]  (linha 273)

```
$$ K_{11} > 0, \qquad K_{22} > 0, \qquad K_{11}K_{22}-K_{12}^2 > 0. $$
```

- **Seção:** (1) Ghost-free (cinética positiva)
- **Contexto:** …A TDCP é escalarmente estável se, ao longo da evolução cosmológica relevante: / **(1) Ghost-free (cinética positiva)**
- **Segue:** **(2) Gradiente estável**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.20]  (linha 277)

```
$c_{s,\pm}^2 > 0.$
```

- **Seção:** (2) Gradiente estável
- **Contexto:** …[equação anterior] / **(2) Gradiente estável**
- **Segue:** **(3) Higuchi (regime acelerado)**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.21]  (linha 281)

```
$m^2F(\chi) \ge 2H^2.$
```

- **Seção:** (3) Higuchi (regime acelerado)
- **Contexto:** …[equação anterior] / **(3) Higuchi (regime acelerado)**
- **Segue:** **(4) Adiabaticidade da modulação**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.22]  (linha 285)

```
$\left|\frac{\dot F}{F}\right| \ll H.$
```

- **Seção:** (4) Adiabaticidade da modulação
- **Contexto:** …[equação anterior] / **(4) Adiabaticidade da modulação**
- **Segue:** **C.11 Comentário técnico: por que F(\chi) não reintroduz o ghost BD**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.23]  (linha 293)

```
$$ \sqrt{-g}\,V(\mathcal{K}) \quad\to\quad \sqrt{-g}\,F(\chi)V(\mathcal{K}). $$
```

- **Seção:** C.11 Comentário técnico: por que F(\chi) não reintroduz o ghost BD
- **Contexto:** …O ghost BD é removido em HR pela estrutura especial do potencial com \sqrt{g^{-1}f}, que gera constraints não-lineares adicionais. / A TDCP modifica o termo:
- **Segue:** Como F(\chi) não depende de derivadas de métricas e não altera a forma funcional em \mathcal{K}, a estrutura de constrai
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

### [AC.24]  (linha 311)

```
$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q^T K \dot Q - Q^T\left(\frac{k^2}{a^2}G+M\right)Q \right]. $$
```

- **Seção:** C.12 Conclusão do Anexo C
- **Contexto:** …- flutuação do campo estrutural \chi. / 2. A ação quadrática reduzida pode ser escrita na forma canônica:
- **Segue:** 3. As condições fundamentais de saúde dinâmica são:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** _(a preencher)_
- **Veredito:** _(pendente)_

