# Derivação 1 — Setor Escalar: K_ij, Ω_ij e o Espectro Físico em k Finito

**Skill invocado:** `bimetric-hr-formalism-guardian`.
**Script:** `code/01_setor_escalar_K_Omega.py` (v5; saídas:
`code/out/01_output.txt`, matrizes simbólicas em `code/out/01_matrices.txt`).

## 1. O que está sendo derivado e por que é necessário

O Cap.15 (§15.4–15.5) afirma que no setor escalar F1 (i) a condição de
ausência de fantasma "reduz-se a $\beta_1+2\beta_2r>0$" e (ii)
$m_S^2\sim m^2F(\beta_1+2\beta_2r)$. O Cap.6.2 §6.4 conta 3 modos
escalares dinâmicos $(\zeta,\sigma,\delta\phi)$; o Anexo C §C.3 conta 2.
O Anexo C §C.11 afirma que a modulação $F(\chi)$ não reintroduz o modo
de Boulware–Deser. Nenhuma dessas afirmações vinha acompanhada das
matrizes $K_{ij},\Omega_{ij}$ — que este item derivou do zero.

## 2. Método (e o histórico que faz parte do resultado)

Ação completa (EH g + EH f na forma Γ–Γ + potencial HR a O(ε²) via
Sylvester + setor χ com F′, F″), 7 campos escalares em **gauge plano no
setor g** ($\Psi_g=E_g=0$; todos os multiplicadores $\Phi_g,B_g,\Phi_f,B_f$
mantidos), modo de Fourier k explícito. O espectro físico vem do
**problema de autovalor quadrático** $(\lambda^2K+\lambda C_a+W)v=0$
por linearização, por k: vínculos = autovalores infinitos (filtrados);
modos físicos = pares finitos; fantasma detectado por
$\mathrm{Re}(v^\dagger Kv)<0$; acoplamento giroscópico $C_a$ tratado
exatamente.

Três tentativas anteriores foram descartadas por razões instrutivas,
todas pegas por testes internos:

1. *Gauge Newtoniano fixado na ação* → perde as constraints de
   $B_g/E_g$ (posto cinético 3 sem controle);
2. *Sem fixação de gauge* → em fundo congelado os modos de gauge não
   aparecem como direções nulas de K (o auto-teste GR reprovou com 3
   modos);
3. *Redução simbólica de Faddeev–Jackiw em k simbólico* → explosão de
   memória (funções racionais com coeficientes exatos gigantes).

**Auto-teste GR embutido** (mesmo pipeline, só EH g + χ): exatamente 1
modo em todo k, $c_s^2=+1.000000$ — validado também pela via de redução
independente (Faddeev–Jackiw matricial), com as duas rotas concordando.

## 3. Resultados (benchmarks numéricos consistentes com Friedmann g/f)

As matrizes simbólicas completas $K_{7\times7},C_{7\times7},W_{7\times7}$
(os $K_{ij},\Omega_{ij}$ explícitos pedidos) estão em
`code/out/01_matrices.txt`. Espectro físico:

| Benchmark | r | ξ | β₁+2β₂r | Modos | Estrutura |
|---|---|---|---|---|---|
| A (ramo dinâmico) | 1.20 | 3.497 (=H/H_f) | +0.04 | **3** | δχ saudável (c²=1, m²=+0.88, kN>0) + **par fantasma** (kN<0, c²=8.49, m²=−4.03, ω² complexo em k baixo) |
| B (ramo dinâmico) | 1.30 | 3.499 | −0.04 | **3** | idem: δχ saudável (m²=+0.90) + par fantasma (c²=7.24, m²=−3.95) |
| C (ramo algébrico, r=r★, ξ=1) | 1.25 | 1 | 0 | **3** | δχ saudável (c²=1, m²=+0.83) + par **degenerado** (kN∼10⁻¹⁶: fortemente acoplado, não-propagante na ordem quadrática) |

**Assinatura estrutural em todos os benchmarks:** o par bimétrico
propaga no cone causal do setor f, $c^2=\xi^2/r^2$ (8.49, 7.24 e 0.64,
exatamente), o mesmo $c_f^2$ derivado no setor tensorial (Derivação 2).

## 4. Vereditos

1. **Cap.15 §15.4 (no-ghost ⟺ β₁+2β₂r>0): REFUTADO.** Cruzar a raiz
   (A→B) não muda nada qualitativamente; o fantasma do ramo dinâmico
   está presente dos dois lados, e no ramo algébrico o par degenera —
   em nenhum caso o sinal de $\beta_1+2\beta_2r$ decide a saúde do setor.
2. **Cap.15 §15.5 ($m_S^2\sim m^2F(\beta_1+2\beta_2r)$): REFUTADO.**
   Nenhuma massa do espectro se relaciona com $\pm0.04$; as massas
   reais são O(1) e taquiônicas no setor relativo.
3. **Contagem (Cap.6.2 §6.4 = 3 vs Anexo C §C.3 = 2):** na análise de
   fundo congelado, **3** modos — a contagem do Cap.6.2. Ressalva
   honesta: a remoção do terceiro modo por constraint secundária
   dependente do tempo não é visível em fundo congelado; a contagem 2
   do Anexo C só poderia ser recuperada por esse mecanismo, que
   permanece **não demonstrado no corpus**.
4. **Anexo C §C.11 (F(χ) não reintroduz o modo BD): SEM SUPORTE** nos
   fundos testados — o terceiro modo escalar está presente e patológico
   no ramo dinâmico.
5. **Instabilidade do ramo dinâmico:** o par fantasma/taquiônico com
   ω² complexo no ramo $\xi=H/H_f$ reproduz a patologia conhecida de
   cosmologias bimétricas no ramo dinâmico (tipo
   Comelli–Crisostomi–Pilo) — exatamente o ramo que o Anexo E §E.3(6)
   declara como "escolha TDCP principal". Combinado com a Derivação 5
   (ṙ≡0 nesse ramo), o ramo dinâmico fica **duplamente inviável**:
   não produz r(t) e é instável.

## 5. Caveats declarados

Fundo quase-de Sitter congelado (Ḣ=Ḣ_f=ξ̇=0); análise por benchmark
numérico (F1: β₁=1, β₂=−2/5, β₄=1/2, M_g=M_f=M_eff=m=1), não varredura
completa do espaço de parâmetros; frequências via QEP com coeficientes
congelados (correções O(H) na evolução dos coeficientes não incluídas).
Nenhum desses caveats afeta os vereditos de sinal/contagem acima.

## 6. Classificação final

**DERIVADO** (matrizes explícitas + espectro verificado por duas rotas
independentes e auto-teste GR). As claims do Cap.15 §15.4/§15.5 e a
contagem do Anexo C §C.3 **não devem ser mantidas como estão**; o
Cap.6.2 §6.4 (3 modos) é confirmado no nível da análise congelada, com
a ressalva da constraint temporal registrada.
