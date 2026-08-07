# A Estrutura da Doença do Par Relativo

**Data:** 2026-08-07. Script: `auditoria/code/estrutura_analitica_par.py`
(saída em `auditoria/code/out/`). Complementa
`no_go_beta_constante.md` com o **endereço** da patologia.

## 1. Onde a doença mora (Etapa A1 — composição dos autovetores)

| Regime | Modo patológico | Composição dominante |
|---|---|---|
| taquião μ=1 | w²=−4.14, kN=+0.33 | **B_f: 0.51, B_g: 0.48** |
| (par do mesmo) | w²=+6.11, kN=−0.24 | **B_f: 0.50, B_g: 0.47** |
| taquião μ=100 | w²=−3.22 | E_f: 0.44, B_f: 0.33, B_g: 0.18 |
| fantasma μ=0.1 | w²=+2380, kN=−1.6e−5 | **Φ_f: 1.00** |

Em μ=1 o par patológico é um **dubleto quase-degenerado dos shifts**
(combinações B_g±B_f — o shift relativo, consistente com o cone
c²=ξ²/r² do setor f). Em μ→0 o fantasma migra para o **lapso do setor
f** (Φ_f puro), pesado e quase desacoplado.

**Lapsos e shifts são os campos da estrutura de vínculos.** A doença
não é uma massa de campo escalar com sinal errado nem um termo
cinético invertido de amplitude física: é **estrutural-de-vínculo** —
vive nas direções que o potencial HR deveria transformar em
multiplicadores saudáveis.

### Consequência para a v2

O Gate 2 mostrou que a modulação β₁(φ₋) insere o termo novo
$p_\phi\beta_1'$ **na constraint secundária** — exatamente o setor
onde a doença mora. A modulação deforma a álgebra de vínculos, não uma
entrada qualquer da matriz de massa. Se ela cura, só o QEP modulado
decide (`modulacao_qep.py`) — mas a objeção "modular massa não
adianta se a doença for cinética" fica respondida: a modulação atua no
lugar certo por construção.

## 2. Lei de escala (Etapa A2)

$$|k_N^{\rm fantasma}| \sim \mu^{2.97} \approx \mu^3 \qquad (\mu\to0)$$

na célula fixa (β₁,β₂)=(0.5,−0.84). Transição fantasma→taquião entre
μ=0.2 e 0.5; os dois coexistem para μ≳0.5. Âncora empírica para
qualquer forma fechada futura.

## 3. Forma fechada em k=0 (Etapa B) — e seu alcance

Bloco de massa 4×4 em k=0: campos (Φ_g, Φ_f, Ψ_f, δχ), com δχ
desacoplado (F′=0). Estrutura de acoplamento: Φ_g↔Ψ_f, Φ_f↔Ψ_f
(Ψ_f é o pivô). Formas fatoradas (validadas contra o lambdify a
1.1×10⁻¹⁶):

$$\det W_{k=0} = \frac{5.4\,\mu^2 r}{(1+\mu)^3}\,P_3(\beta_1,\beta_2,\beta_4;r,\mu)$$

com $P_3$ cúbico nos β (expressão completa na saída do script), e

$$\mathrm{tr}\,W_{k=0} = \frac{6}{r(\mu+1)}\Big[\tfrac{\beta_1}{6}(1{+}\mu r^2) + \beta_2 r(\mu r^2{+}\tfrac12) + \beta_4 r^3(\tfrac{2\mu r^2}{3}{+}\tfrac16) + \tfrac{U''r(\mu{+}1)}{12}\Big]$$

**Limite declarado:** B_g, B_f e E_f **não têm entrada em W(k=0)** — a
massa efetiva do dubleto de shifts (o taquião de μ=1!) nasce da
eliminação de vínculos (complemento de Schur do pencil completo), não
do bloco W puro. O det acima descreve o setor dos lapsos; a condição
analítica completa do taquião de shifts fica como trabalho aberto.

## 4. Próximo passo

`modulacao_qep.py`: QEP com modulação **por coeficiente** β₁(φ₋),
via decomposição em fatias {Fb,Fp,Fpp}×{β₀..β₄} das matrizes já
construídas (sem alterar a biblioteca), fundo acoplado com ⟨φ₋⟩
estacionário, varredura em (g=χ̄/v∗, v∗, m_χ²). Pergunta: **existe
modulação que positiviza o par?**
