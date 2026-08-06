# Derivação 6 — μ(k,a), η_slip e Σ Derivados (Não Postulados)

**Skill invocado:** `observational-pipeline-designer`.
**Script:** `code/06_mu_alpha_QS.py` (v4c; saídas: `code/out/06_output.txt`,
formas exatas com m² simbólico em `code/out/06_matrices.txt`).

## 1. O que está sendo derivado e por que é necessário

O Cap.18 §18.3 **postula por analogia** ("a correção típica tem forma"):

$$ \mu(k,a)=1+\frac{\alpha(a)\,k^2/a^2}{k^2/a^2+m_S^2(a)} \quad\text{(1 polo, Yukawa)}, $$

com §18.4 $\alpha(a)=\alpha_0\,r^2/(1+r^2)$, §18.7 uma forma de
η_slip com uma segunda função β(a), e §18.8 a parametrização
$m_S=m_{S0}a^{-p}$, $\alpha=\alpha_0a^q$ usada em todo o confronto
observacional (Cap.19). O Cap.7 §7.6 antecipa dois mediadores (2 polos),
com coeficientes nunca calculados. Este item deriva μ, η_slip e Σ da
teoria real.

## 2. Método (resposta estática exata com calibração GR)

Fonte de matéria fria $\delta\rho$ acoplada minimamente ao setor g
($L_{src}=-a^3\delta\rho\,\Phi_g/2$, de
$\tfrac12\sqrt{-\bar g}\,\delta T^{00}\delta g_{00}$). Ação com os
**9 campos sem fixar gauge**; as 9 equações estáticas exatas
($\dot q=0$, sem hierarquia assumida) são derivadas e **só então**
o gauge Newtoniano $B_g=E_g=0$ é imposto nas equações. Potenciais
resolvidos com a seleção validada por sondagem exaustiva contra a
calibração GR:

$$ \{\underbrace{00,\ \text{traço},\ \text{sem-traço}}_{\text{setor g completo}}\}\ \cup\ \{00_f,\ 0i_f,\ \text{sem-traço}_f\}\ \cup\ \{\delta\chi\}, $$

com a equação de **momento do setor g excluída** (é fonteada pela
velocidade da matéria, descartada no estático — incluí-la impõe
Φ=3Ψ espúrio) e a redundância estática no bloco f.
$\mu(k)\equiv$ resposta$(m^2)$/resposta$(m^2\to0)$, em que as correções
de fundo O(H²/k²) cancelam na razão.

**Calibração GR (aprovada nos dois benchmarks):**
$k^2\Psi/\delta\rho\to-1/2$ ($-0.499999$) e $\Phi/\Psi\to1$
($1.000045$ / $0.999950$) em k=1000.

O caminho até aqui derrubou, em sequência, três armadilhas clássicas de
derivações quase-estáticas — (i) fixar gauge na ação perde a equação
sem-traço (que impõe Φ=Ψ); (ii) truncagem por símbolos viola a
hierarquia que a Friedmann impõe (ρ_int ~ H² apesar de conter m²);
(iii) equação de momento sem fonte de velocidade — todas pegas pela
calibração GR embutida. O Cap.18 nunca teve como tropeçar nelas porque
postulou o resultado.

## 3. Resultados

### 3.1 Estrutura de polos — refuta o ansatz de 1 polo

μ(k,a) é racional de **grau 7/7 em k²** (não 1/1):

- **Benchmark A** (r=1.2 < r★, ramo dinâmico): 5 polos reais negativos
  (massas Yukawa $m^2a^2$ = 44.6, 1.62, 0.413, 0.279, 0.046) **+ 1 par
  complexo** ($-0.21\pm13.4i$) — o setor instável da Derivação 1
  aparecendo no observável.
- **Benchmark B** (r=1.3 > r★): 4 polos negativos **+ 3 polos em k²
  positivo** (+0.043, +14.1, +50.4) — **ressonâncias em escalas físicas**
  (instabilidade taquiônica atravessando o observável; visível na
  tabela como estrutura em k~1–10).

### 3.2 α derivado — refuta §18.4

$$ \boxed{\ \alpha_{exato}\ \equiv\ \mu(k\to\infty)-1\ =\ 0\ \text{(exatamente, nos dois benchmarks)}\ } $$

contra $\alpha_{Cap.18}=0.590$ (A) e $0.628$ (B). A força extra é
**totalmente blindada em pequenas escalas** (GR recuperada em
$k\to\infty$); os desvios reais de μ vivem em escalas **intermediárias**
(μ=1.12 em k=10 no A; μ=0.61 em k=10 no B) — o oposto qualitativo do
ansatz do Cap.18, em que $\mu\to1+\alpha$ em k grande.

### 3.3 η_slip e Σ

η_slip é **não-monotônico** e não se ajusta à forma de uma função
suave única do §18.7: no benchmark A, η_slip ≈ −0.006 em k≲1, 0.62 em
k=10, →1 em k grande; no B chega a 3.36 em k=10 (vizinhança de
ressonância). Σ fica ≈1±1% fora das ressonâncias (lensing pouco
afetado), o que é uma **assinatura em si**: μ≠1 com Σ≈1.

## 4. Vereditos

1. **Cap.18 §18.3 (ansatz Yukawa 1 polo): REFUTADO** — a estrutura real
   tem ~7 polos, incluindo pares complexos/positivos no ramo instável.
2. **Cap.18 §18.4 (α=α₀r²/(1+r²)): REFUTADO** — α_∞=0 exato; não há
   "quinta força residual" em pequenas escalas para blindar via m_S
   grande (Cap.18 §18.5 resolve um problema que a teoria real não tem).
3. **Cap.18 §18.7 (η_slip de 1 função): REFUTADO** na forma; η_slip
   real é multi-escala e não-monotônico.
4. **Cap.7 §7.6 (dois mediadores): qualitativamente na direção certa**
   (multi-polo), quantitativamente insuficiente.
5. **Consistência interna:** os polos patológicos de μ correspondem um
   a um às instabilidades do espectro da Derivação 1 (mesmo fundo).
6. **Gate P6.7 acionado:** as conclusões do Cap.19 (joelho Yukawa,
   benchmarks B1/B2, faixa de m_S0) pressupõem a forma de 1 polo e
   ficam sem fundamento derivado — ver Derivação 8.

## 5. Caveats declarados

Mesmos da Derivação 1 (fundo congelado, benchmark F1 específico), mais:
resposta estática ≠ μ dinâmico para k≲H (janela confiável: k≫H, onde a
calibração GR é exata); matéria como fonte externa estática (velocidade
descartada — consistente com a exclusão da equação de momento).

## 6. Classificação final

**DERIVADO** (com calibração GR embutida e seleção de equações validada
por sondagem exaustiva). O pipeline observacional dos Cap.18–19 precisa
ser reconstruído sobre a forma multi-polo derivada — ou, no mínimo,
re-parametrizado com α_∞=0 e desvios em escalas intermediárias.
