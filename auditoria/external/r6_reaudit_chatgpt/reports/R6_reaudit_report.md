# TDCP F1 — Reauditoria ADM/Faddeev–Jackiw do setor escalar

**Data:** 12 agosto 2026  
**Regra epistemológica:** somente execuções concluídas com `return code 0` entram como evidência. Rodadas abortadas por gate ou timeout foram descartadas.

## 1. Veredito executivo

A reauditoria **não confirma o terceiro modo escalar de norma negativa do Gate F**.

No fundo tardio beta-constante, a redução ADM simbólica dá exatamente

\[
K_{\rm metric}=
\begin{pmatrix}0&0\\0&K_E\end{pmatrix},
\qquad \det K_{\rm metric}=0,
\]

deixando **um escalar métrico físico + \(\delta\chi\) = dois DOFs escalares**.

Ao longo da trajetória dinâmica com \(\beta_1(\phi_-)\), a menor direção do Schur permanece alinhada com \(\Psi_f\) e é suprimida em relação à escala cinética dominante por aproximadamente \(10^{-24}\)–\(10^{-30}\), conforme época e modo. Depois de tratar \(\Psi_f\) como constraint secundária via Faddeev–Jackiw, **nenhum autovalor cinético negativo permanece** nos modos/épocas testados.

Consequência: a cadeia anterior

`modo negativo -> omega_0 -> omega_0/Lambda_3 -> H-SC`

deve ser **suspensa**, pois a premissa “modo negativo propagante” não passa a redução ADM/FJ.

## 2. Controles independentes

### 2.1 GR + escalar canônico

`r6i_gr_adm_selfcheck.py` produziu exatamente:

- \(K_{\delta\chi\delta\chi}=a^3/2\);
- \(W_{\delta\chi\delta\chi}=a(k^2+a^2U'')/2\);
- todos os acoplamentos \(K,C,W\) entre \(\delta\chi\) e os multiplicadores métricos = 0;
- \(c_s^2=1\);
- nenhum DOF métrico escalar em GR.

**Status: PASS.**

### 2.2 Fundo dinâmico

A reintegração independente do fundo usado pelo R4b terminou em:

- \(r_{\rm fim}=0.497885\);
- \(\phi_-/v=0.931649\).

Esses números reproduzem as âncoras do cálculo antigo.

### 2.3 Constraint dinâmica

No diagnóstico float64:

- `max row(Psi_f)/||K|| = 3.284e-19`;
- `max |lambda_min|/scale = 9.117e-26`;
- autovetor nulo mediano em \((\Psi_f,E_f,\delta\chi)\):
  \((1,\ 4.49\times10^{-22},\ 1.58\times10^{-19})\).

Controle com matrizes simbólicas avaliadas a 70–80 dígitos:

| a | k/H | menor autovalor / escala |
|---:|---:|---:|
| 100 | 21.054 | `7.79798512872170619205145051744e-29` |
| 4000 | 1.000 | `2.00871364795231020032127772254e-26` |
| 15000 | 0.277 | `1.07895514513008946223238355257e-30` |

Os resíduos absolutos ainda carregam a precisão da trajetória de fundo, que foi integrada em float64. O dado estável é a razão extremamente pequena e o alinhamento com \(\Psi_f\). No ponto fixo, onde as relações de fundo foram impostas simbolicamente, o determinante é **zero exato**.

## 3. Mapa cinético dinâmico sem artefato de borda

Uma rodada preliminar gerou uma cinética negativa somente no primeiro ponto \(a=20\). Ela foi descartada. A derivada de \(C\) foi então recalculada em uma grade estendida \(a=10\rightarrow10^5\), com a região interpretada restrita a \(20\le a\le8\times10^4\).

| a_cross | autovalores negativos | menor razão cinética | min |W_aux(Psi_f)| |
|---:|---:|---:|---:|
| 500 | 0 / 6303 | 1.111e-12 | 1.644e+04 |
| 1000 | 0 / 6303 | 1.452e-13 | 4.743e+04 |
| 1600 | 0 / 6303 | 9.173e-14 | 6.078e+04 |
| 2500 | 0 / 6303 | 2.002e-14 | 1.455e+05 |
| 4000 | 0 / 6303 | 5.962e-15 | 3.316e+05 |
| 8000 | 0 / 6303 | 8.161e-16 | 1.227e+06 |
| 15000 | 0 / 6303 | 6.703e-17 | 4.335e+06 |
| 30000 | 0 / 6303 | 4.368e-18 | 1.735e+07 |

**Resultado:** zero direções cinéticas negativas em todos os oito modos.

## 4. O crescimento canônico tardio foi identificado

No ramo beta-constante, depois da redução correta, \(E_f\) e \(\delta\chi\) ficam exatamente desacoplados em \(K,C,W\) no cálculo numérico (`max relative offdiag = 0`).

A equação medida para \(\delta\chi\) é

\[
\ddot{\delta\chi}+3H\dot{\delta\chi}
+\left(\frac{k^2}{a^2}+0.3\right)\delta\chi=0,
\]

com erro relativo da massa na faixa \(10^{-16}\) e erro da fricção convergindo para \(1.2\times10^{-7}\).

A taxa positiva do quadro canônico é reproduzida por

\[
\frac{\sigma_{\rm can}}{H}
=
\sqrt{\frac94-\frac{0.3}{H^2}-\left(\frac{k}{aH}\right)^2},
\]

que vem da transformação \(x\propto a^{3/2}\delta\chi\). Já a taxa física lenta é

\[
\frac{\sigma_{\rm phys}}{H}
=
-\frac32+\frac{\sigma_{\rm can}}{H}<0
\]

nos pontos testados. Portanto o `sigma_can > 0` tardio não representa crescimento físico de \(\delta\chi\).

## 5. R4b estático refeito no espaço físico

O R4b antigo maximizava sobre quatro ICs métricas, incluindo duas ICs independentes em \(\Psi_f\). Depois da constraint, essas duas ICs não pertencem ao espaço físico. A comparação correta usa \(E_f,\dot E_f\).

| beta1 | lnA antigo | lnA novo: ICs métricas físicas | mediana(tx Phi_g - tx qmet) | mediana |Phi_g|/qmet | ln Phi_g (Ef-pos) | ln Phi_g (Ef-vel) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | +3.97 | -8.07016 | +0.24172 | 0.099159 | -6.92692 | -8.30381 |
| 4.47 | +3.62 | -7.95743 | -0.07289 | 0.134863 | -6.90734 | -8.31418 |

O fato de \(|\Phi_g|/q_{met}\sim0.1\) permanecer finito **não significa amplificação**: ambos estão decaindo.

## 6. R4b dinâmico/pousado refeito

Valores novos abaixo usam 14k pontos. A coluna final mostra a mudança da medida ao passar de 7k para 14k.

| a_cross | lnA antigo | lnA novo Ef-IC | max sobre todos os 4 estados físicos | max Δln|Phi_g| | Δ(14k-7k) |
|---:|---:|---:|---:|---:|---:|
| 500 | -0.21 | -12.93501 | -0.09983 | +2.72574 | +0.02921 |
| 1000 | +3.26 | -14.27341 | -4.88237 | -0.54153 | +0.03555 |
| 1600 | +1.57 | -13.21491 | -3.56598 | -0.05391 | -0.62514 |
| 2500 | +3.17 | -14.00524 | -7.29653 | -2.08297 | -0.25588 |
| 4000 | +4.80 | -14.33270 | -8.43495 | -1.13741 | +0.15358 |
| 8000 | +4.03 | -13.52391 | -8.46013 | -2.93716 | -0.55311 |
| 15000 | +4.52 | -12.32593 | -7.34294 | -5.41143 | -1.60958 |

O caso \(a_{cross}=30000\) permanece sem passagem completa \(kh=20\rightarrow0.2\), tal como no cálculo antigo.

**Resultado robusto:** em todas as passagens completas, as ICs métricas físicas decaem fortemente. Nenhuma das amplificações antigas \(+1.6\rightarrow+4.8\) é reproduzida.

`max Δln|Phi_g|` é mantido apenas como diagnóstico de componente. Quando \(\Phi_g\) inicial está perto de zero, esse log é sensível a zero-crossings e não pode ser convertido diretamente em previsão de ISW.

## 7. Consequências para Gate F, R4 e R5

### Gate F — suspender

- contagem de 3 DOFs escalares;
- ramo propagante de norma negativa;
- \(\omega_0/H\sim7-12\) atribuído a esse ramo;
- fechamento H-SC baseado em \(\omega_0/\Lambda_3\).

### R4 — reabrir

A banda métrica com \(\ln A\sim+4\) **não é reproduzida** no sistema ADM/FJ físico. Os dados são consistentes com a banda antiga tendo sido gerada pela promoção numérica da direção de constraint a terceiro DOF.

### R5 / ISW — suspender a previsão antiga

A cadeia

`banda f amplifica -> Phi_g carrega banda -> excesso ISW baixo-l`

perde a primeira premissa numérica. Isso **não prova** compatibilidade observacional; apenas torna inválido usar o excesso ISW antigo como previsão da F1 sem refazer o sistema de perturbações.

## 8. O que permanece aberto

Ainda não foram calculados sobre o sistema corrigido:

1. perturbações acopladas de baryons/CDM/fótons/neutrinos;
2. potenciais de Bardeen com a hierarquia completa de matéria/radiação;
3. \(C_\ell^{TT,TE,EE}\), lensing e \(P(k)\);
4. cutoff/interações não lineares dos **dois modos físicos restantes**.

Esses cálculos devem partir da redução ADM/FJ de 2 DOFs. Reutilizar o backend antigo de 3 DOFs reintroduziria precisamente a direção que esta auditoria identifica como constraint.

## 9. Conclusão

\[
\boxed{\text{o terceiro modo escalar usado pelo Gate F não é confirmado como DOF físico}}
\]

e, após sua remoção,

\[
\boxed{\text{não foi encontrada direção cinética negativa nos fundos e modos testados}}
\]

enquanto a amplificação métrica do R4/R5 desaparece e é substituída por decaimento.

Isso melhora substancialmente a saúde interna da F1, mas **não estabelece viabilidade observacional**. O próximo gate legítimo é matéria/radiação + \(C_\ell\) sobre a nova redução.
