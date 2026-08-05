# Plano de Derivações — Lista Estruturada de Equações (formato de prova)

**Método acordado:** antes de resolver qualquer coisa no computador, este
documento lista **todas as equações que precisam ser desenvolvidas e
derivadas**, em ordem de dependência, no formato de prova: *entrada
citada → operação → resultado esperado → critério de fechamento*. Na
etapa seguinte, os scripts Python (sympy/numpy/scipy) serão criados para
resolver os passos marcados **[SCRIPT]**; o usuário roda os scripts e
retorna os resultados para interpretação e redação final dos arquivos
`derivations/NN_titulo.md`.

**Notação de numeração:** todas as citações usam a numeração **atual**
do corpus (pós-renumeração da Tarefa 2d). Mapa para o prompt original:
Cap.13→Cap.14, Cap.14→Cap.15, Cap.15→Cap.16, Cap.17→Cap.18,
Cap.18→Cap.19. Cap.10 e Anexos A–H inalterados.

---

## Status: já concluídas (commitadas)

| # | Resultado | Classificação |
|---|-----------|---------------|
| 3 | Regra da cadeia completa em ∂V/∂N_g: ξ e β₄ cancelam exatamente; ρ_int^(g) = m²M_eff²F(χ)(β₀+3β₁r+3β₂r²+β₃r³) = forma do Anexo A + F(χ). Anexo B §B.5 tinha um passo faltando. | **DERIVADO** |
| 4 | H²=(8πG/3)ρ/(1−η) não é derivável da ação atual (η ausente da Lagrangiana). Extensão mínima proposta: Ω(η)=M_g²(1−η) acoplada a R_g — reproduz a forma postulada só no regime adiabático \|η̇\|≪H, com termo extra Hη̇/(1−η) caso contrário. | **NÃO DERIVÁVEL SEM ACOPLAMENTO ADICIONAL** |
| 5 | No ramo dinâmico literal (H_g=ξH_f), ṙ≡0 exatamente; §14.12 usa condição diferente não-equivalente (H_b=ξH_g). Via consistente para r(t): raiz móvel r_⋆(φ(t)) com β_n(φ) adiabático. | **DERIVADO** (+ hipótese adicional p/ r(t)) |

Restantes: **1, 2, 6, 7, 8** — planejadas abaixo. Dependências:
D1 → (D6, D8); D2 independente; D7 independente.

---

## 0. Fundo comum (equações de entrada compartilhadas)

- **(F.1)** Lagrangiana minisuperespaço (Anexo B §B.4.5):
  $$\mathcal{L} = -3M_g^2\frac{a\dot a^2}{N_g} - 3M_f^2\frac{b\dot b^2}{N_f} - m^2M_{eff}^2N_g a^3F(\chi)V(\xi,r) + a^3\Big(\frac{\dot\chi^2}{2N_g}-N_gU(\chi)\Big) - N_ga^3\rho_m$$
- **(F.2)** Potencial HR no fundo FLRW:
  $$V(\xi,r)=\beta_0+\beta_1(\xi+3r)+\beta_2(3\xi r+3r^2)+\beta_3(3\xi r^2+r^3)+\beta_4\,\xi r^3$$
  Para a ação covariante completa (necessária nas perturbações):
  $$V(\mathcal K)=\sum_{n=0}^4\beta_n e_n(\mathcal K),\qquad \mathcal K=\sqrt{g^{-1}f},\qquad \mathcal K^{(0)}=\mathrm{diag}(\xi,r,r,r)$$
- **(F.3)** Friedmann g (Anexo E §E.3(1); validada na Derivação 3):
  $3M_g^2H^2=\rho_m+\tfrac12\dot\chi^2+U+m^2M_{eff}^2F(\chi)(\beta_0+3\beta_1r+3\beta_2r^2)$ (F1: β₃=0)
- **(F.4)** Friedmann f (Anexo B §B.6; validada):
  $3M_f^2H_f^2=m^2M_{eff}^2F(\chi)(\beta_4+3\beta_3r^{-1}+3\beta_2r^{-2}+\beta_1r^{-3})$
- **(F.5)** Constraint de Bianchi: $(\beta_1+2\beta_2r+\beta_3r^2)(H_g-\xi H_f)=0$
- **(F.6)** Família F1: $(\beta_0,\beta_1,\beta_2,0,\beta_4)$, $\beta_1\beta_2<0$, $r_\star=-\beta_1/(2\beta_2)$
- **(F.7)** Gauge cosmológico: $N_g=1$ **imposto só depois de variar** (lição da Derivação 3)

---

## Derivação 1 — K_ij e Ω_ij explícitas do setor escalar

**Skill:** `bimetric-hr-formalism-guardian`.

### Entradas (citadas)

- **(E1.a)** Ansatz escalar setor g (Anexo C §C.2.1):
  $$ds_g^2=-(1+2\Phi_g)dt^2+2a\,\partial_iB_g\,dt\,dx^i+a^2[(1-2\Psi_g)\delta_{ij}+2\partial_i\partial_jE_g]dx^idx^j$$
- **(E1.b)** Ansatz escalar setor f (Anexo C §C.2.2):
  $$ds_f^2=-N_f^2(1+2\Phi_f)dt^2+2bN_f\,\partial_iB_f\,dt\,dx^i+b^2[(1-2\Psi_f)\delta_{ij}+2\partial_i\partial_jE_f]dx^idx^j$$
- **(E1.c)** $\chi=\bar\chi(t)+\delta\chi$; modulação $F(\chi)$ multiplicando $V(\mathcal K)$
- **(E1.d)** Gauge: Newtoniano no setor g, $B_g=E_g=0$ (Anexo C §C.4)
- **(E1.e)** Afirmações a verificar:
  - Cap.15 §15.4: no-ghost "reduz-se a $M_{eff}^2(\beta_1+2\beta_2r)>0$"
  - Cap.15 §15.5: $m_S^2\sim m^2F(\phi)(\beta_1+2\beta_2r)$ ("omitidos fatores de normalização positivos")
  - Cap.6.2 §6.4: vetor dinâmico $\mathbf Q=(\zeta,\sigma,\delta\phi)$ (3 modos)
  - Anexo C §C.3: **2** modos físicos (helicidade-0 + δχ) — *contradiz Cap.6.2*

### Achados preliminares que condicionam o plano (exploração sympy desta sessão)

- **(A1)** No truncamento minisuperespaço (k=0, sem B_f/E_f), o termo
  cinético de σ **cancela exatamente** após integrar o lapse perturbado
  do setor f. Conclusão estrutural: **K_ij só existe em k finito** — o
  cálculo tem de incluir B_f e E_f e manter k explícito do início ao fim.
- **(A2)** Contagem: sem perturbações de matéria, ζ não é modo
  independente (o Anexo C está certo; o Q de 3 componentes do Cap.6.2
  só se realiza com matéria incluída). Decisão de plano: **D1 deriva o
  setor vácuo+χ (2×2)**; matéria e ζ entram na **D6**, onde há fonte
  δρ_m.

### Cadeia de prova

- **(P1.1) [SCRIPT]** Montar $g^{-1}f$ até $O(\varepsilon^2)$ em modo de
  Fourier k, nas 7 variáveis pós-gauge $(\Phi_g,\Psi_g;\Phi_f,\Psi_f,B_f,E_f;\delta\chi)$.
- **(P1.2) [SCRIPT]** Raiz quadrada $\mathcal A=\sqrt{g^{-1}f}$ ordem a
  ordem, resolvendo as equações de Sylvester:
  $$\mathcal A^{(0)}\mathcal A^{(1)}+\mathcal A^{(1)}\mathcal A^{(0)}=(g^{-1}f)^{(1)},\qquad \mathcal A^{(0)}\mathcal A^{(2)}+\mathcal A^{(2)}\mathcal A^{(0)}=(g^{-1}f)^{(2)}-(\mathcal A^{(1)})^2$$
  com $\mathcal A^{(0)}=\mathrm{diag}(\xi,r,r,r)$.
- **(P1.3) [SCRIPT]** $e_n(\mathcal A)$, $n=0\ldots4$, até $O(\varepsilon^2)$;
  montar $\sqrt{-g}\,F(\chi)V(\mathcal A)$ até $O(\varepsilon^2)$
  (incluindo a expansão de $\sqrt{-g}$ e de $F(\bar\chi+\delta\chi)$ até
  segunda ordem — termos $F'$, $F''$).
- **(P1.4) [SCRIPT]** Expansão quadrática dos dois termos de
  Einstein-Hilbert: setor g com $(\Phi_g,\Psi_g)$; setor f com
  $(\Phi_f,\Psi_f,B_f,E_f)$ e lapse de fundo $\xi$. (Recomputar do zero
  — não usar formas "de livro".)
- **(P1.5) [SCRIPT]** Setor χ quadrático: cinético canônico +
  $U''\delta\chi^2$ + acoplamentos cruzados via $F'(\chi)\delta\chi\times$
  (perturbações de $V$).
- **(P1.6)** Ação total $S^{(2)}$; identificar auxiliares (sem derivadas
  temporais): $\Phi_g,\Phi_f,B_f$ → três constraints algébricas
  $\mathcal C_A(Q,\dot Q;k,t)=0$.
- **(P1.7) [SCRIPT]** Resolver as constraints (sistema linear),
  substituir de volta. Sobram 4 variáveis $(\Psi_g,\Psi_f,E_f,\delta\chi)$
  para 2 modos físicos → a matriz cinética resultante deve ter **posto
  2**; identificar as direções nulas e mudar para variáveis
  invariantes (esperado: $\sigma\propto$ combinação de
  $\Psi_f-\Psi_g$ e $k^2(E_f)$, mais $\delta\chi$). *Risco mapeado: é
  aqui que o script precisa tratar degenerescência de posto
  explicitamente, não invertendo matrizes singulares.*
- **(P1.8) [SCRIPT]** Extrair, na base final $Q=(\sigma,\delta\chi)$:
  $$K_{ij}(t,k),\qquad \Omega_{ij}(t,k)=\frac{k^2}{a^2}G_{ij}(t)+M_{ij}(t)$$
  — impressão em LaTeX das seis funções independentes.
- **(P1.9)** Condições no-ghost: $K_{11}>0$, $\det K>0$. **Confrontar**
  com a claim (E1.e): a condição reduz-se a $\beta_1+2\beta_2r>0$?
  Registrar dependências extras reais (k, ξ, $M_f/M_g$, F, Ḟ).
- **(P1.10)** Velocidades do som: autovalores de $K^{-1}G>0$ (condição
  no-gradient — Anexo C §C.8).
- **(P1.11)** Massa do modo relativo: autovalor apropriado de $K^{-1}M$
  no regime sub-horizonte → $m_S^2$ **com todos os fatores de
  normalização explícitos** (nada de "∼").
- **(P1.12)** Veredito final: as condições "no-ghost" e "massa positiva"
  colapsam mesmo na única desigualdade $\beta_1+2\beta_2r>0$? (três
  saídas possíveis: sim / sim-mais-condições / não).

### Critério de fechamento

Arquivo `01_setor_escalar_K_Omega.md` com K, G, M explícitas,
confirmação ou correção das claims E1.e, e classificação
DERIVADO / DERIVADO SOB HIPÓTESE / NÃO DERIVÁVEL.

---

## Derivação 2 — m_T² explícito do setor tensorial

**Skill:** `bimetric-hr-formalism-guardian`.

### Entradas (citadas)

- **(E2.a)** Ansatz TT (Cap.16 §16.1 / Anexo D §D.2): $h_{ij}$ em g,
  $\ell_{ij}$ em f, ambos transversos e sem traço.
- **(E2.b)** **Discrepância interna já identificada** entre as duas
  formas declaradas da mesma ação quadrática tensorial:
  - Cap.16 §16.2: $S_T^{(2)}=\frac12\int a^3[M_g^2(\dot h^2-\tfrac{k^2}{a^2}h^2)+M_f^2\,r^2(\dot\ell^2-\tfrac{k^2}{a^2}\ell^2)-m_{mix}^2(h-\ell)^2]$
    (fator $r^2$ no cinético de ℓ; **sem** fatores de lapse ξ)
  - Anexo D §D.3: $S_T^{(2)}=\frac18\int[M_g^2a^3(\dot h^2-\tfrac{k^2}{a^2}h^2)+M_f^2\tfrac{b^3}{N_f}(\dot\ell^2-N_f^2\tfrac{k^2}{b^2}\ell^2)-2m^2M_{eff}^2a^3F\,\mathcal M(r,\xi)(h-\ell)^2]$
    (fator $b^3/N_f=r^3a^3/\xi$ no cinético; gradiente com $N_f^2/b^2$)
  As duas não são compatíveis; a derivação decide qual (se alguma) é a correta.
- **(E2.c)** Afirmações a verificar:
  - Cap.16 §16.2: $m_{mix}^2=m^2M_{eff}^2F(\phi)(\beta_1r+2\beta_2r^2)$ — sem ξ
  - Cap.16 §16.4: $m_T^2=m^2F\,\frac{M_{eff}^2}{M_g^2}(\beta_1r+2\beta_2r^2)$
  - Cap.16 §16.6: $m_T^2\sim r\,m_S^2$ (pergunta do prompt: o fator $M_{eff}^2/M_g^2$ cancela mesmo?)
  - Anexo D §D.5: $m_T^2\propto m^2F\,\mathcal B(r)\tfrac{1+r}{r}\times(\text{normalização})$ — *terceira forma, também diferente*
  - Anexo D §D.4: base de diagonalização $h_\pm$ com pesos $M_g$, $M_fr^{3/2}$

### Cadeia de prova

- **(P2.1) [SCRIPT]** $g^{-1}f$ e $\mathcal A=\sqrt{g^{-1}f}$ até
  $O(h^2)$ para perturbações TT (bloco espacial: raiz de matriz próxima
  de $r\,\delta$ — mesma técnica de Sylvester de P1.2, mais simples).
- **(P2.2) [SCRIPT]** $e_n(\mathcal A)$ até $O(h^2)$ → termo de massa do
  potencial HR: verificar se a estrutura é exatamente $\propto(h-\ell)^2$
  ou se há termos $h^2$, $\ell^2$ independentes (a estrutura
  $c_1h^2+c_2h\ell+c_3\ell^2$ só é proporcional a $(h-\ell)^2$ se
  $c_1=c_3=-c_2/2$ — o script decide). Obter o coeficiente **com a
  dependência em ξ explícita** (as formas do Cap.16 não têm ξ; se o
  coeficiente real depender de ξ, apontar em que limite — p.ex. ξ=r ou
  ξ=1 — as formas do texto são recuperadas).
- **(P2.3) [SCRIPT]** Einstein-Hilbert quadrático TT dos dois setores,
  recomputado (fatores de volume e lapse corretos: $a^3$ vs $b^3/N_f$)
  → resolve a discrepância E2.b.
- **(P2.4) [SCRIPT]** Normalização canônica + diagonalização exata do
  sistema 2×2 (cinéticos $\mathcal A_g$, $\mathcal A_f$ distintos; massa
  não-diagonal). Atenção: com $\mathcal A_g\neq\mathcal A_f$ e ambos
  dependentes do tempo, a diagonalização instantânea exige a condição
  adiabática $|\dot{\mathcal A}/\mathcal A|\ll H$ — declarar.
- **(P2.5)** $m_T^2$ final com **todos** os fatores ($m^2$, F, β_n, r,
  ξ, $M_g$, $M_f$, $M_{eff}$).
- **(P2.6)** Confrontos: (i) coeficiente $\beta_1r+2\beta_2r^2$ correto?
  (ii) o prefator de escala é $M_{eff}^2/M_g^2$, ou
  $M_{eff}^2(M_g^{-2}+M_f^{-2}r^{-3})$-tipo (soma sobre os dois
  setores)? (iii) razão $m_T^2/m_S^2$ com o $m_S^2$ real da D1: é $r$?
  depende de ξ e das massas de Planck? → veredito sobre §16.6.
- **(P2.7)** Reavaliar Higuchi (Cap.16 §16.5, Anexo D §D.7) com o
  $m_T^2$ corrigido.

### Critério de fechamento

`02_setor_tensorial_mT2.md` com a ação quadrática TT correta (resolvendo
E2.b), $m_T^2$ fechado, veredito sobre as quatro formas citadas em E2.c.

---

## Derivação 6 — μ(k,a) e α(a) derivados de K,Ω (não por analogia)

**Skill:** `observational-pipeline-designer`. **Depende de P1.8.**

### Entradas (citadas)

- **(E6.a)** Cap.7 §7.6 (forma conceitual, dois mediadores):
  $$\mu(k,a)=1+\frac{\Delta_\sigma}{1+m_\sigma^2a^2/k^2}+\frac{\Delta_\phi}{1+m_\phi^2a^2/k^2}$$
  (com $\Delta_\sigma,\Delta_\phi$ nunca calculados)
- **(E6.b)** Cap.18 §18.3 — **ansatz Yukawa postulado por analogia**
  ("a correção típica tem forma"):
  $$\mu(k,a)=1+\frac{\alpha(a)k^2/a^2}{k^2/a^2+m_S^2(a)}$$
  §18.4: $\alpha(a)\sim\epsilon^2/(1+\epsilon^2)$, $\epsilon=M_fr/M_g$;
  parametrização prática $\alpha(a)=\alpha_0r^2/(1+r^2)$;
  §18.7: forma de $\eta_{slip}$ com segunda função β(a);
  §18.8: $m_S(a)=m_{S0}a^{-p}$, $\alpha(a)=\alpha_0a^q$.
- **(E6.c)** Definições observacionais (Cap.18 §18.1):
  $-k^2\Psi=4\pi Ga^2\mu\rho_m\delta$, $-k^2(\Phi+\Psi)=8\pi Ga^2\Sigma\rho_m\delta$, $\eta_{slip}=\Phi/\Psi$.

### Cadeia de prova

- **(P6.1) [SCRIPT]** Estender o sistema da D1 com matéria fria
  minimamente acoplada ao setor g: $\delta\rho_m$, velocidade $v_m$
  (fluido irrotacional, $p=0$), restaurando $\Psi_g,\Phi_g$ com fonte.
- **(P6.2)** Novo conjunto de constraints com fonte de matéria
  (a constraint de $\Phi_g$ vira a equação de Poisson bimétrica).
- **(P6.3) [SCRIPT]** Limite quase-estático (Cap.7 §7.3):
  $|\dot X|\ll(k/a)|X|$, reter $k^2/a^2$ e massas, desprezar
  $\dot\Phi,\dot\Psi$ → sistema **algébrico** linear nas perturbações.
- **(P6.4) [SCRIPT]** Resolver para $k^2\Psi_g$ em função de
  $\rho_m\delta$ → **μ(k,a) exato da teoria** (forma racional em
  $k^2/a^2$).
- **(P6.5) [SCRIPT]** Idem para $\Phi_g$ → $\eta_{slip}(k,a)$ e
  $\Sigma(k,a)$ exatos.
- **(P6.6)** Confronto com o ansatz Yukawa: o μ exato tem **um** polo
  ($m_S^2$) ou **dois** ($m_\sigma^2$ e $m_\phi^2$, como Cap.7 §7.6
  antecipa)? Extrair a(s) função(ões) $\alpha(a)$ derivada(s) e comparar
  com $\alpha_0r^2/(1+r^2)$; determinar se $\alpha_0$ é mesmo
  $\sim\epsilon^2/(1+\epsilon^2)$.
- **(P6.7)** **Gate para D8:** se a forma exata difere do ansatz de um
  polo, refazer as conclusões dependentes do Cap.19 (posição do joelho,
  benchmarks B1/B2) na D8.

### Critério de fechamento

`06_mu_alpha_quase_estatico.md` com μ, η_slip, Σ exatos, dicionário
(forma exata) ↔ (parametrização do Cap.18), e veredito sobre o ansatz.

---

## Derivação 7 — Solução do modo σ_k por Bessel/Hankel (Cap.10 §10.3)

**Skill:** `stability-constraints-auditor`. Independente (analítica; script só confere).

### Entradas (citadas)

- **(E7.a)** Cap.10 §10.2–10.3: equação primordial do modo relativo com
  massa taquiônica ($m_\sigma^2<0$), em tempo conforme, fundo
  quase-de Sitter $a\sim e^{Ht}$:
  $$\sigma_k''+2\frac{a'}{a}\sigma_k'+(k^2-a^2|m_\sigma^2|)\sigma_k=0$$
- **(E7.b)** Claim a verificar: "Para $k\ll aH$: $\sigma_k\sim k^{-3/2}$"
  (§10.3), gerando espectro "aproximadamente invariante de escala".

### Cadeia de prova (analítica)

- **(P7.1)** Variável canônica $u\equiv a\sigma_k$:
  $$u''+\Big(k^2-\frac{a''}{a}-a^2|m_\sigma^2|\Big)u=0$$
  (sinal: massa taquiônica **soma** ao termo $a''/a$).
- **(P7.2)** De Sitter: $a=-1/(H\tau)$, $\tau<0$ → $a''/a=2/\tau^2$,
  $a^2=1/(H^2\tau^2)$:
  $$u''+\Big(k^2-\frac{\nu^2-1/4}{\tau^2}\Big)u=0,\qquad \boxed{\nu^2=\frac94+\frac{|m_\sigma^2|}{H^2}}$$
- **(P7.3)** Solução geral:
  $u=\sqrt{-\tau}\,[c_1H_\nu^{(1)}(-k\tau)+c_2H_\nu^{(2)}(-k\tau)]$;
  vácuo de Bunch–Davies ($u\to e^{-ik\tau}/\sqrt{2k}$ para $-k\tau\to\infty$)
  fixa $c_2=0$, $c_1=\sqrt{\pi}/2\,e^{i\pi(\nu+1/2)/2}$.
- **(P7.4)** Assintótica super-horizonte $-k\tau\to0$:
  $H_\nu^{(1)}(x)\approx-\tfrac{i}{\pi}\Gamma(\nu)(x/2)^{-\nu}$ →
  $$|\sigma_k|\propto k^{-\nu}\quad\Rightarrow\quad \Delta_\sigma^2(k)\equiv\frac{k^3|\sigma_k|^2}{2\pi^2}\propto k^{3-2\nu}$$
- **(P7.5)** Veredito esperado sobre E7.b: $\sigma_k\sim k^{-3/2}$ vale
  **apenas** no limite $|m_\sigma^2|\ll H^2$ (onde $\nu\to3/2$). Para
  massa taquiônica não desprezível, $\nu>3/2$ e o espectro é
  **red-tilted** com $n_\sigma-1=3-2\nu<0$ — a condição
  "$|m_\sigma^2|\ll H^2$ durante a fase primordial" precisa ser
  declarada no Cap.10 (coerente com §10.7, que já pede "massa efetiva
  pequena", mas sem ligar as duas coisas). Bonus: expressar
  $n_\sigma-1\approx-\tfrac23|m_\sigma^2|/H^2$ (expansão de ν) como
  previsão quantitativa.
- **(P7.6) [SCRIPT]** Verificações: (i) sympy — confirmar que a solução
  de P7.3 satisfaz a EDO e reproduzir os limites assintóticos; (ii)
  scipy — integrar numericamente o modo completo de sub- a
  super-horizonte para 2–3 valores de $|m_\sigma^2|/H^2$ e medir o
  expoente de $|\sigma_k|$ vs k, comparando com $-\nu$.

### Critério de fechamento

`07_modo_sigma_bessel.md` com a solução exata de Hankel, o expoente
correto $k^{-\nu}$, a condição de validade do claim do texto, e a
correção quantitativa do índice espectral.

---

## Derivação 8 — Faixa de m_S0 a partir da dinâmica de F(φ) e do fundo

**Skill:** `eft-and-screening-validator`. **Depende de P1.11 (m_S² real) e do gate P6.7.**

### Entradas (citadas)

- **(E8.a)** $m_S^2(a)=[\text{normalização da D1}]\times m^2F(\phi(a))(\beta_1+2\beta_2r(a))$
  — a proporcionalidade é do Cap.15 §15.5/Cap.18 §18.4; a normalização
  exata vem da D1.
- **(E8.b)** Sistema dinâmico de fundo (Anexo E §E.3, §E.6): ODEs para
  $\chi, x, \eta, \Omega_m$ em $N=\ln a$, com
  $\lambda(\chi)=M_gU'/U$ e fonte
  $\mathcal S\propto F'(\chi)V$.
- **(E8.c)** Vínculos a impor simultaneamente:
  1. Higuchi: $m^2Fr(\beta_1+2\beta_2r)\geq2H^2$ (Cap.16 §16.5) — usar a forma corrigida da D2
  2. Orçamento de energia: $\Omega_{int}=\rho_{int}^{(g)}/3M_g^2H^2\leq1-\Omega_m$ (Anexo E §E.5)
  3. EFT: $H\ll\Lambda_3\sim(m^2M_{eff})^{1/3}$ (Cap.17, Cap.19 §"EFT")
  4. Crescimento: $|\alpha(a_0)|\lesssim0.1$ (Cap.18 §18.6) — usar α derivado na D6
  5. Estabilidade escalar: $\beta_1+2\beta_2r>0$ ao longo de toda a evolução (forma corrigida da D1)
- **(E8.d)** Benchmark a testar: $m_{S0}\sim(30\text{–}300)H_0$.
  **Nota crítica já estabelecida:** no Cap.19 §19.1–19.3, essa faixa é
  obtida por **design observacional** (posição do joelho Yukawa dentro
  de $k\in[0.01,0.1]\,h/\mathrm{Mpc}$), não por dinâmica — é
  literalmente $k_\star/k_{H0}$ para os dois extremos. A D8 responde à
  pergunta inversa: *a dinâmica de F(φ) produz naturalmente essa faixa,
  ou ela é uma escolha externa?*

### Ponto de decisão prévio (a resolver antes do script)

- **(P8.0)** O corpus **não fixa** a forma funcional de $F(\chi)$ nem de
  $U(\chi)$ (Anexo E §E.8 os lista como entradas livres do sistema).
  Sem $F$ e $U$ explícitos, **não existe** derivação de $m_{S0}$ — o
  resultado honesto seria NÃO DERIVÁVEL SEM DADO EXTERNO. Plano: fazer
  a varredura sob a hipótese adicional declarada de formas de referência
  ($F(\chi)=e^{\lambda_F\chi/M_g}$, $U(\chi)=U_0e^{-\lambda_U\chi/M_g}$
  — as mais simples compatíveis com as condições de adiabaticidade do
  Anexo C §C.7), e classificar o resultado como **DERIVADO SOB HIPÓTESE
  ADICIONAL** com a faixa obtida, ou **NÃO DERIVÁVEL** se nem sob essas
  formas a faixa fechar.

### Cadeia de prova

- **(P8.1)** Fechar $m_S^2(a)$ com a expressão real da D1 (substituindo
  a proporcionalidade).
- **(P8.2) [SCRIPT numérico]** Integrar o sistema do Anexo E de
  $N_i$ (era da matéria profunda, $\eta\approx0$, $\Omega_m\approx1$)
  até hoje, no ramo algébrico com raiz móvel $r_\star(\phi(t))$
  (resultado da D5), para grades de $(m/H_0,\ \beta_1,\ \beta_2,\ \lambda_F,\ \lambda_U,\ \Gamma)$.
- **(P8.3) [SCRIPT numérico]** Filtrar a grade pelos vínculos E8.c
  (1–5); manter apenas trajetórias com
  $H(a)$ compatível com $\Omega_m\approx0.3$, $w_{eff}\approx-1\pm0.1$
  hoje (Anexo E §E.7).
- **(P8.4) [SCRIPT numérico]** Na região viável: extrair
  $m_{S0}=m_S(a_0)$ em unidades de $H_0$ e o expoente efetivo
  $p_{\rm eff}=-d\ln m_S/d\ln a|_{a_0}$ (comparar com o $p=1$ dos
  benchmarks B1/B2 do Cap.19).
- **(P8.5)** Comparar a faixa dinâmica obtida com $(30\text{–}300)H_0$;
  classificar conforme P8.0.

### Critério de fechamento

`08_mS0_dinamica_F.md` com a faixa derivada (ou a demonstração de que a
faixa é subdeterminada), a lista explícita das hipóteses usadas, e o
confronto com os benchmarks do Cap.19.

---

## Scripts a criar (próxima etapa)

| Script | Resolve | Tipo | Saída |
|--------|---------|------|-------|
| `code/01_setor_escalar_K_Omega.py` | P1.1–P1.8 | sympy | K, G, M em LaTeX + condições no-ghost/no-gradient avaliadas em F1 |
| `code/02_setor_tensorial_mT2.py` | P2.1–P2.5 | sympy | ação TT correta + $m_T^2$ fechado em LaTeX |
| `code/06_mu_alpha_QS.py` | P6.1–P6.5 | sympy | μ(k,a), η_slip, Σ exatos em LaTeX (importa resultados do 01) |
| `code/07_bessel_sigma_k.py` | P7.6 | sympy+scipy | verificação da solução de Hankel + expoente numérico vs ν |
| `code/08_mS0_background_scan.py` | P8.2–P8.4 | numpy/scipy | tabela da região viável + faixa de $m_{S0}/H_0$ + $p_{\rm eff}$ |

Todos autocontidos, comentados, com `print()`/`sympy.latex()` dos
resultados finais (especificação do prompt), e com `assert`s nas
checagens internas (fundo reproduz F.3/F.4; limites GR recuperados).

**Ordem de execução sugerida:** 01, 02, 07 (independentes, podem rodar
em paralelo) → 06 (usa saída do 01) → 08 (usa 01, 02 e 06).

**Fluxo:** usuário roda cada script e retorna a saída → interpretação e
redação de `NN_titulo.md` → só então `00_indice.md` (que também
proporá, sem executar, as atualizações necessárias nos capítulos).
