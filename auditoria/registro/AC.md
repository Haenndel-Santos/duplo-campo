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
- **Depende de:** Anexo B §B.2
- **Veredito:** CONFERE (fundo FLRW com N_g=1 fixado desde o início — escolha de gauge legítima, consistente com Anexo B §B.2)

### [AC.02]  (linha 57)

```
$$ \bar f_{\mu\nu}dx^\mu dx^\nu = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j. $$
```

- **Seção:** C.2 Perturbações escalares: duas métricas + χ
- **Contexto:** …Trabalharemos no espaço-tempo com simetria de fundo FLRW: / [equação anterior]
- **Segue:** Definimos perturbações escalares no espaço de Fourier (modo k).
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.2
- **Veredito:** CONFERE (mesma forma padrão, setor f, com N_f geral)

### [AC.03]  (linha 65)

```
$$ ds_g^2 = -(1+2\Phi_g)dt^2 + 2a\,\partial_i B_g\,dt\,dx^i + a^2\left[(1-2\Psi_g)\delta_{ij} + 2\partial_i\partial_j E_g\right]dx^i dx^j. $$
```

- **Seção:** C.2.1 Setor g (escalar)
- **Contexto:** …**C.2.1 Setor g (escalar)** / No gauge genérico:
- **Segue:** **C.2.2 Setor f (escalar)**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (ansatz escalar geral padrão, 4 potenciais Φ,B,Ψ,E — forma-padrão da literatura de perturbações cosmológicas)

### [AC.04]  (linha 69)

```
$$ ds_f^2 = -N_f^2(1+2\Phi_f)dt^2 + 2bN_f\,\partial_i B_f\,dt\,dx^i + b^2\left[(1-2\Psi_f)\delta_{ij} + 2\partial_i\partial_j E_f\right]dx^i dx^j. $$
```

- **Seção:** C.2.2 Setor f (escalar)
- **Contexto:** …[equação anterior] / **C.2.2 Setor f (escalar)**
- **Segue:** **C.2.3 Campo χ**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (mesma forma padrão, setor f, com o fator N_f do fundo)

### [AC.05]  (linha 73)

```
$\chi(t,\mathbf{x}) = \bar\chi(t) + \delta\chi(t,\mathbf{x}).$
```

- **Seção:** C.2.3 Campo χ
- **Contexto:** …[equação anterior] / **C.2.3 Campo χ**
- **Segue:** **C.3 Escolha de gauge e contagem de variáveis**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (decomposição padrão fundo+perturbação)

### [AC.06]  (linha 111)

```
$$ \Delta\Psi \equiv \Psi_f - \Psi_g, \qquad \Delta E \equiv E_f - E_g, \qquad \delta\chi. $$
```

- **Seção:** C.4 Variáveis invariantes e base física
- **Contexto:** …- e a flutuação de χ. / Uma escolha padrão é trabalhar com:
- **Segue:** E fixar um gauge para remover redundâncias, por exemplo:
- **Classe (sugerida):** definicao
- **Depende de:** —
- **Veredito:** CONFERE (definições razoáveis de variáveis relativas)

### [AC.07]  (linha 125)

```
$S = S^{(0)} + S^{(1)} + S^{(2)} + \cdots,$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …**C.5 Estrutura da ação quadrática** / Ao expandir a ação até segunda ordem:
- **Segue:** o termo S^{(1)}=0 quando o fundo satisfaz as equações de Friedmann (Anexo B).
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (fato padrão de teoria de perturbações: o termo linear se anula em torno de uma solução clássica das equações de fundo)

### [AC.08]  (linha 133)

```
$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q_i\,K_{ij}(t,k)\,\dot Q_j - Q_i\,\Omega_{ij}(t,k)\,Q_j \right], $$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …O termo relevante para estabilidade é S^{(2)}. / A forma geral para 2 modos escalares Q_i (após integrar constraints) é:
- **Segue:** onde:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE SOB HIPÓTESE (forma template padrão da ação quadrática — kinética menos "Ω"; correta como estrutura genérica, mas a especialização para "2 modos" (§C.3) que a acompanha é a contagem refutada pela âncora D1 — real: 3 modos na análise de fundo congelado)

### [AC.09]  (linha 145)

```
$\Omega_{ij} = \frac{k^2}{a^2}G_{ij}(t) + M_{ij}(t).$
```

- **Seção:** C.5 Estrutura da ação quadrática
- **Contexto:** …- \Omega_{ij} contém termos de gradiente (\propto k^2) e massa. / É comum decompor:
- **Segue:** **C.6 Integração das variáveis não-dinâmicas**
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** —
- **Veredito:** CONFERE (decomposição padrão gradiente+massa, forma geral esperada de uma ação quadrática relativística)

### [AC.10]  (linha 159)

```
$\mathcal{C}_A(Q,\dot Q;k,t)=0.$
```

- **Seção:** C.6 Integração das variáveis não-dinâmicas
- **Contexto:** …entram sem derivadas temporais. Elas são multiplicadores de Lagrange. / Variação em relação a elas gera equações algébricas (constraints) do tipo:
- **Segue:** Resolvendo essas constraints e substituindo de volta na ação, obtemos a ação reduzida.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** —
- **Veredito:** CONFERE (fato padrão de sistemas com vínculos — variáveis sem derivada temporal geram constraints algébricas ao serem variadas)

### [AC.11]  (linha 205)

```
$$ F(\chi)>0, \qquad \left|\frac{\dot F}{F}\right| \ll H, \qquad \left|\frac{F'}{F}\right|\Delta\chi \ll 1. $$
```

- **Seção:** Interpretação na TDCP
- **Contexto:** …F(\chi) deve ser positiva e variar lentamente para evitar mistura forte e inversão de sinal efetiva. / Condições práticas (regime adiabático):
- **Segue:** **C.8 Velocidade do som e estabilidade de gradiente**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** Cap.6.2 §6.10 (lote 2)
- **Veredito:** CONFERE (condições qualitativas razoáveis, análogas à adiabaticidade já usada no Cap.6.2 §6.10/lote 2)

### [AC.12]  (linha 213)

```
$\det\left(c_s^2 K - G\right)=0.$
```

- **Seção:** C.8 Velocidade do som e estabilidade de gradiente
- **Contexto:** …O termo de gradiente define G_{ij}. / Os modos propagantes têm velocidades do som obtidas de:
- **Segue:** Ou seja, os c_s^2 são autovalores da matriz:
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (forma padrão do problema de autovalor generalizado para extrair velocidades do som de um sistema com matriz cinética K e matriz de gradiente G)

### [AC.13]  (linha 217)

```
$K^{-1}G.$
```

- **Seção:** C.8 Velocidade do som e estabilidade de gradiente
- **Contexto:** …[equação anterior] / Ou seja, os c_s^2 são autovalores da matriz:
- **Segue:** **Condição de estabilidade de gradiente**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (equivalente padrão: c_s² são autovalores de K⁻¹G)

### [AC.14]  (linha 223)

```
$c_{s,\pm}^2 > 0.$
```

- **Seção:** Condição de estabilidade de gradiente
- **Contexto:** …**Condição de estabilidade de gradiente** / Para evitar instabilidade exponencial em escalas sub-horizonte:
- **Segue:** Além disso, em teoria relativística estável, usualmente esperamos:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AC.19; âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE (condição padrão de estabilidade de gradiente; mesma nota de AC.19 sobre a dimensão da matriz — critério estrutural correto, mas construído sobre a contagem de 2 modos refutada pela âncora D1)

### [AC.15]  (linha 227)

```
$c_s^2 \le 1$
```

- **Seção:** Condição de estabilidade de gradiente
- **Contexto:** …[equação anterior] / Além disso, em teoria relativística estável, usualmente esperamos:
- **Segue:** (não estritamente necessário em teorias efetivas, mas desejável para evitar superluminalidade sistemática e problemas de
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** —
- **Veredito:** CONFERE (o próprio texto qualifica corretamente esta condição como "não estritamente necessária em teorias efetivas, mas desejável" — calibração adequada, sem superclaim)

### [AC.16]  (linha 235)

```
$\exp\left(|c_s| \frac{k}{a} t\right),$
```

- **Seção:** Interpretação física
- **Contexto:** …**Interpretação física** / - Se c_s^2<0, então para k/a grande, o modo cresce como:
- **Segue:** o que destrói a teoria imediatamente.
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AC.14
- **Veredito:** CONFERE (forma padrão de instabilidade de gradiente exponencial — consistente com ω imaginário quando c_s²<0)

### [AC.17]  (linha 251)

```
$m_{eff}^2 \ge 2H^2.$
```

- **Seção:** C.9 Conexão com Higuchi e com o modo helicidade-0
- **Contexto:** …**C.9 Conexão com Higuchi e com o modo helicidade-0** / Em fundos próximos a de Sitter, para um campo spin-2 massivo, a helicidade-0 é saudável apenas se:
- **Segue:** Quando essa condição é violada:
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** —
- **Veredito:** CONFERE (importada — bound de Higuchi padrão para um campo spin-2 massivo genérico em dS, Higuchi 1987)

### [AC.18]  (linha 261)

```
$K_{11} \to 0 \quad \text{em } m_{eff}^2\to 2H^2,$
```

- **Seção:** C.9 Conexão com Higuchi e com o modo helicidade-0
- **Contexto:** …- e torna-se ghost. / Logo, em linguagem da matriz cinética:
- **Segue:** e se m_{eff}^2<2H^2, então K_{11}<0.
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AC.17; âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** ERRO DE FORMULAÇÃO — âncora D1: a identificação K_11↔Higuchi de um único campo massivo genérico não corresponde à estrutura real do setor escalar da TDCP-F1; o cômputo explícito (D1) encontra um par fantasma/degenerado que persiste "dos dois lados" de qualquer cruzamento de raiz (benchmarks A→B), não um K_11 único que troca de sinal suavemente em m_eff²=2H² — a intuição de gravidade massiva de campo único não se aplica diretamente ao sistema acoplado de 3 modos

### [AC.19]  (linha 273)

```
$$ K_{11} > 0, \qquad K_{22} > 0, \qquad K_{11}K_{22}-K_{12}^2 > 0. $$
```

- **Seção:** (1) Ghost-free (cinética positiva)
- **Contexto:** …A TDCP é escalarmente estável se, ao longo da evolução cosmológica relevante: / **(1) Ghost-free (cinética positiva)**
- **Segue:** **(2) Gradiente estável**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE (critério estrutural correto — cinética positiva definida ⟺ ausência de fantasma, válido para qualquer dimensão); mas herda a contagem de 2 modos de §C.3, já refutada pela âncora D1 (real: 3 modos, mesma tensão do Cap.6.2×Anexo C) — a matriz relevante deveria ser 3×3

### [AC.20]  (linha 277)

```
$c_{s,\pm}^2 > 0.$
```

- **Seção:** (2) Gradiente estável
- **Contexto:** …[equação anterior] / **(2) Gradiente estável**
- **Segue:** **(3) Higuchi (regime acelerado)**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AC.19; âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE (condição padrão de estabilidade de gradiente; mesma nota de AC.19 sobre a dimensão da matriz — critério estrutural correto, mas construído sobre a contagem de 2 modos refutada pela âncora D1)

### [AC.21]  (linha 281)

```
$m^2F(\chi) \ge 2H^2.$
```

- **Seção:** (3) Higuchi (regime acelerado)
- **Contexto:** …[equação anterior] / **(3) Higuchi (regime acelerado)**
- **Segue:** **(4) Adiabaticidade da modulação**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AC.18
- **Veredito:** ERRO (herdado de AC.18 — a identificação com Higuchi de campo único não corresponde à estrutura real de 3 modos, âncora D1)

### [AC.22]  (linha 285)

```
$\left|\frac{\dot F}{F}\right| \ll H.$
```

- **Seção:** (4) Adiabaticidade da modulação
- **Contexto:** …[equação anterior] / **(4) Adiabaticidade da modulação**
- **Segue:** **C.11 Comentário técnico: por que F(\chi) não reintroduz o ghost BD**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AC.11
- **Veredito:** CONFERE (condição de adiabaticidade padrão, razoável independentemente da contagem de modos)

### [AC.23]  (linha 293)

```
$$ \sqrt{-g}\,V(\mathcal{K}) \quad\to\quad \sqrt{-g}\,F(\chi)V(\mathcal{K}). $$
```

- **Seção:** C.11 Comentário técnico: por que F(\chi) não reintroduz o ghost BD
- **Contexto:** …O ghost BD é removido em HR pela estrutura especial do potencial com \sqrt{g^{-1}f}, que gera constraints não-lineares adicionais. / A TDCP modifica o termo:
- **Segue:** Como F(\chi) não depende de derivadas de métricas e não altera a forma funcional em \mathcal{K}, a estrutura de constrai
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** NÃO-DERIVÁVEL — âncora D1: "SEM SUPORTE nos fundos testados — o terceiro modo escalar está presente e patológico no ramo dinâmico." O argumento qualitativo (F(χ) sem derivadas preserva a estrutura de constraints) pode valer para a ausência específica do ghost de Boulware-Deser, mas isso não implica ausência de OUTRAS patologias — o cômputo explícito de D1 encontra um par fantasma/taquiônico genuíno no ramo dinâmico, que este argumento qualitativo não previne nem menciona

### [AC.24]  (linha 311)

```
$$ S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q^T K \dot Q - Q^T\left(\frac{k^2}{a^2}G+M\right)Q \right]. $$
```

- **Seção:** C.12 Conclusão do Anexo C
- **Contexto:** …- flutuação do campo estrutural \chi. / 2. A ação quadrática reduzida pode ser escrita na forma canônica:
- **Segue:** 3. As condições fundamentais de saúde dinâmica são:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** AC.08; âncora D1 (derivations/01_setor_escalar_K_Omega.md)
- **Veredito:** CONFERE (forma template padrão — kinética menos gradiente-e-massa; consistente com a forma que a âncora D1 de fato calculou explicitamente, embora com dimensão 3 em vez de 2 na análise real)

