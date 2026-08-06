# Derivação 2 — Setor Tensorial: Ação Quadrática TT e m_T²

**Skill invocado:** `bimetric-hr-formalism-guardian`.
**Script:** `code/02_setor_tensorial_mT2.py` (saída: `code/out/02_output.txt`).

## 1. O que está sendo derivado e por que é necessário

O corpus declara **três formas mutuamente incompatíveis** da mesma ação
quadrática tensorial e da massa do gráviton:

- Cap.16 §16.2: cinético de ℓ com fator $M_f^2\,r^2$, sem lapse ξ;
  $m_{mix}^2=m^2M_{eff}^2F(\beta_1r+2\beta_2r^2)$, sem ξ;
- Cap.16 §16.4: $m_T^2=m^2F\,\tfrac{M_{eff}^2}{M_g^2}(\beta_1r+2\beta_2r^2)$;
- Anexo D §D.3/§D.5: cinético $M_f^2\,b^3/N_f$, gradiente $N_f^2k^2/b^2$,
  e $m_T^2\propto\mathcal B(r)\tfrac{1+r}{r}$.

Esta derivação refaz tudo do zero (EH dos dois setores na forma Γ–Γ +
potencial HR expandido a O(h²) via equações de Sylvester + **setor χ**,
cuja contribuição via √(−g) é obrigatória — sem ela o gráviton ganharia
massa espúria até em GR) e decide as três discrepâncias.

## 2. Ponto de partida

Perturbações TT $h_{ij}$ (setor g) e $\ell_{ij}$ (setor f) sobre o fundo
FLRW bimétrico (F.1–F.7 do plano), uma polarização por vez. Fundo
imposto **on-shell**: equações de aceleração dos dois setores derivadas
por Euler–Lagrange da Lagrangiana minisuperespaço validada, Friedmann
g/f, e a equação de χ derivada da ação (sinal da fonte: $-m^2M_{eff}^2F'V$
— o Anexo E §E.3(3) declara o sinal oposto; registrado como erratum).

## 3. Resultados (derivados, verificados no script)

### 3.1 Cinético e gradiente — decide (i)

$$ K_{hh}=\frac{M_g^2a^3}{4},\qquad K_{\ell\ell}=\frac{M_f^2b^3}{4\xi},\qquad \frac{K_{\ell\ell}}{K_{hh}}=\frac{M_f^2}{M_g^2}\frac{r^3}{\xi}. $$

**O Anexo D §D.3 está correto; o Cap.16 §16.2 (fator $r^2$, sem ξ) está
errado.** Velocidades de propagação (normalizadas a $k^2/a^2$):

$$ c_g^2=1,\qquad \boxed{c_f^2=\frac{\xi^2}{r^2}} $$

— o modo do setor f propaga no cone causal de f, não no de g (o Anexo D
já continha essa estrutura; o Cap.16 a perde).

### 3.2 Estrutura da massa — decide (ii)

Com o setor χ incluído e o fundo on-shell, a matriz de massa é
**exatamente** proporcional a $(h-\ell)^2$:

$$ M_{hh}=M_{\ell\ell}=-M_{h\ell}=\frac{F M_{eff}^2 m^2\,ab}{4}\big(a\beta_1+a\beta_2\xi+b\beta_2+b\beta_3\xi\big). $$

### 3.3 Coeficiente e m_T² — decide (iii)

$$ m_{mix}^2 = \frac{m^2M_{eff}^2F}{2}\,r\big[\beta_1+\beta_2(\xi+r)+\beta_3\,\xi r\big] $$

**depende de ξ.** A forma do Cap.16 ($\beta_1r+2\beta_2r^2$, sem ξ) só é
recuperada no caso especial $\xi=r$. A massa física (autovalor não nulo
de $K^{-1}M$; o modo massless existe, $\det M=0$):

$$ \boxed{\,m_T^2 \;=\; m^2F\,M_{eff}^2\left(\frac{1}{M_g^2}+\frac{\xi}{M_f^2\,r^3}\right) r\big[\beta_1+\beta_2(\xi+r)+\beta_3\,\xi r\big]\,} $$

O prefator de escala é $M_{eff}^2\!\left(\tfrac1{M_g^2}+\tfrac{\xi}{M_f^2r^3}\right)$
— soma sobre os dois setores — e **não** $M_{eff}^2/M_g^2$ (Cap.16
§16.4). Resposta à pergunta do prompt: o fator $M_{eff}^2/M_g^2$ **não
cancela nem aparece sozinho**; a razão $m_T^2/m_S^2$ do §16.6 fica sem
fundamento também porque o $m_S^2$ do Cap.15 foi refutado na Derivação 1.

### 3.4 Consequência numérica (benchmark, ramo dinâmico ξ=H/H_f)

Com $r=1.2$, $\xi=3.497$: $\beta_1+\beta_2(\xi+r)=1-0.4(4.7)=-0.88<0$
⟹ $m_T^2=-3.19<0$ (taquiônico) e **Higuchi violado** ($m_T^2<2H^2$),
enquanto a fórmula sem ξ do Cap.16 daria $m_T^2\propto+0.04>0$. A
dependência em ξ **inverte o sinal** da massa tensorial no ramo que o
Anexo E §E.3(6) declara como escolha principal da TDCP.

## 4. Classificação final

**DERIVADO** (ação TT correta, estrutura $(h-\ell)^2$, $m_T^2$ fechado,
verificados por pipeline com auto-testes). As formas do Cap.16
§16.2/§16.4/§16.6 **não devem ser mantidas**; a do Anexo D §D.3 é
confirmada e a do §D.5 ($\propto\mathcal B(r)(1+r)/r$) é substituída
pela forma em caixa. Diagonalização exata exige a nota de que os
cinéticos dependem do tempo (condição adiabática $|\dot{\mathcal A}/\mathcal A|\ll H$)
e que os gradientes ($c_g^2\neq c_f^2$) não são simultaneamente
diagonalizáveis com a massa — a "diagonalização" do Cap.16 §16.3 é
aproximada, não exata.
