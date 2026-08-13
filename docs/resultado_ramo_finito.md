# O Ramo Finito Corrigido — Resultado

**Data:** 2026-08-07. Consequência do `auditoria/erratum_01_bianchi.md`.
Script: `auditoria/code/ramo_dinamico_correto.py`.

---

## 1. O que foi estabelecido

Com a constraint de Bianchi **corrigida**, o ramo dinâmico (agora
identificado como o **ramo finito** da cosmologia bimétrica) entrega:

| | Resultado | Status |
|---|---|---|
| Evolução estrutural | $\dot r\neq0$, $r$ cresce de ~0 até ~0.33 | **confirmado** |
| Lapso físico | $\xi>0$ em toda a história | **confirmado** |
| Limite GR primordial | $H^2/(\rho/3M_g^2)=1.0000$ | **exato** |
| Higuchi | 400/400 pontos, $m_T^2>0$ em todos | **satisfeito** |
| Cosmologia | $\Omega_m\approx0.25$ hoje, universo acelerando | **razoável** |

**O ramo dinâmico não está morto.** Ele estava mal identificado.

## 2. A estrutura do ramo finito

A cúbica $m^2M_{\rm eff}^2\mathcal W(r)=\rho$ tem duas famílias de raiz:

- $r\sim\sqrt{\tilde\rho}\to\infty$ — **ramo infinito**, patológico:
  dá $\xi<0$, isto é, lapso negativo no setor $f$;
- $r\sim\beta_1/\tilde\rho\to0$ — **ramo finito**, físico.

> **[REABERTURA — 2026-08-13, R-12i]** *Nota acrescentada; o texto
> acima permanece intacto.* Este é o parágrafo que originou a exclusão
> do ramo infinito no corpus, e ele está hoje **duplamente
> qualificado**. (i) *Época* (R-10c Parte A): "dá ξ < 0" só vale no
> regime **primordial** — a segunda raiz torna-se viável em a ≳ 1
> (r ≈ 2.23, ξ ≈ 2.23, H² > 0); o que o R-10c usava para excluir era
> ξ **cruzar zero** no caminho. (ii) *Fonte* (R-12i): esse critério
> **não se sustenta**. Como `b = ra`, o nosso `ξ = r + dr/dN` é
> `ξ = X/a` com o `X ≡ ḃ/ℋ` de Könnig et al. — mesmo sinal, mesmo
> zero —, e 1407.4331 §II/§VI trata esse quique de `b`
> **explicitamente**, defendendo-o como físico por três razões
> declaradas (f não acopla à matéria e não tem interpretação
> geométrica; nenhuma variável de fundo ou perturbada é singular;
> `√(−det f)·R̄(f)` é finita e não-nula, logo as equações de movimento
> existem em todo instante). A *infinite-branch bigravity* é o único
> modelo estável em todos os tempos daquele paper. **Estado: a
> exclusão está REABERTA e exige reavaliação** — não é "fechada" nem
> "aberta e viável" —, e o alvo do reexame é o ramo infinito da F1
> **com β₄ ≠ 0** (o IBB viável exige `0 < β₄ < 2β₁`; a nossa célula
> mínima tem β₄ = 0). *Fonte:
> `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b);
> `docs/resultado_r10c_saidas.md` Parte A.*

No ramo finito, no universo primordial:

$$r\propto a^3 \;\Rightarrow\; \frac{dr}{dN}=3r \;\Rightarrow\; \boxed{\xi = 4r > 0}$$

e $r$ cresce monotonicamente até um ponto fixo tardio (raiz da cúbica
com $\rho=0$), que no benchmark é $r_\infty\approx0.33$.

**É este o mecanismo de separação estrutural que a v1 procurava.** Não
precisa de $\beta_n(\phi_-)$, nem de campo modulador, nem de hipótese
adicional: $r$ é fixado pela densidade a cada instante e evolui porque
$\rho$ cai.

## 3. Resultado derivado: $m_T^2/H^2 \to 12$ no universo primordial

Este é um resultado estrutural, não numérico. No ramo finito, com
$r\to0$ e $\xi=4r$, o termo dominante de $m_T^2$ (âncora D2) é

$$m_T^2 \simeq m^2M_{\rm eff}^2\frac{\xi}{M_f^2r^3}\,r\,\beta_1
= \frac{4m^2M_{\rm eff}^2\beta_1}{M_f^2\,r}$$

e a Friedmann do setor $f$ dá

$$H^2 = \frac{m^2M_{\rm eff}^2\,r^2\mathcal V_f(r)}{3M_f^2}
\;\xrightarrow[r\to0]{}\; \frac{m^2M_{\rm eff}^2\beta_1}{3M_f^2\,r}$$

Logo

$$\boxed{\;\frac{m_T^2}{H^2}\;\longrightarrow\;12\;}$$

**Independente de todos os parâmetros** — $M_f^2$, $M_{\rm eff}^2$,
$m^2$ e $\beta_1$ cancelam. Verificado numericamente: em $a=0.02$ o
script dá $m_T^2/H^2 = 12.002$.

Consequência: **Higuchi ($m_T^2\ge2H^2$) é automaticamente satisfeito
no universo primordial neste ramo**, com margem de fator 6. A razão cai
para $\approx4$ hoje — ainda o dobro do limite.

## 4. O que isto faz com a âncora D8

A D8 concluiu que Higuchi falha em **60/60** pontos da grade, e o
parecer registrou isso como "o resultado mais preocupante de toda a
auditoria".

Aquele scan impôs $\xi=H_g/H_f$, que **não satisfaz a constraint
correta** (no ramo correto, $H_g/H_f=r$, não $\xi$). Com $r=1.2$ e
$\xi=3.497$, o fator estrutural ficava

$$\beta_1+\beta_2(\xi+r) = 1-0.4(4.697) = -0.88 < 0$$

forçando $m_T^2<0$ **por construção**. No fundo correto, o mesmo fator
hoje vale $+0.7224$.

**A D8 fica invalidada no seu resultado numérico.** O achado documental
(a faixa $m_{S0}\sim30$–$300H_0$ é design observacional, não dinâmica)
permanece — é independente.

## 5. Limites deste resultado — o que NÃO foi estabelecido

O scan deu 225/225, e é preciso ser preciso sobre o que isso significa:

**(a) Só duas das quatro constantes foram varridas.** $\beta_0$ e
$\beta_4$ variaram; $\beta_1=1$ e $\beta_2=-0.4$ ficaram fixos nos
valores de benchmark de D1/D2. São justamente $\beta_1,\beta_2$ que
entram em $\mathcal B(r)$ e no fator estrutural. "225/225" significa
"para estes $\beta_1,\beta_2$", não "em todo o espaço".

**(b) Parte do 225/225 é estrutural, não informativa.** O limite
$m_T^2/H^2\to12$ vale independentemente dos $\beta_n$ — então no
universo primordial *nenhum* ponto poderia falhar. O teste só
discrimina em tempos tardios.

**(c) Só Higuchi foi testado.** Não foram verificados: ausência de
fantasma escalar, estabilidade de gradiente, validade EFT,
$f\sigma_8$, screening solar.

**(d) O setor escalar continua em aberto — e é o risco principal.**
A D1 encontrou par fantasma/taquiônico "no ramo dinâmico", mas naquele
fundo incorreto. Refazer a D1 **neste** fundo é o próximo passo, e é o
que decide se o ramo é viável de fato.

## 6. Consequência para o plano v2

A motivação da arquitetura muda substancialmente.

A v2 adotou $\beta_n(\phi_-)$ porque "os dois ramos estão mortos". Essa
premissa caiu: o ramo finito corrigido produz evolução estrutural
sozinho, com $\beta_n$ **constantes**.

Isso não invalida o trabalho dos Passos 1 e 2 — a ação está bem posta,
o Gate 2 Parte A está resolvido, e o achado de que a constraint não
fatora com $\beta_1(\phi_-)$ continua válido. Mas a **ordem** muda:

1. **Primeiro:** setor escalar no ramo finito com $\beta_n$ constantes.
   Se for saudável, a TDCP-F1 corrigida pode já ser consistente, e a
   modulação vira extensão opcional em vez de necessidade.
2. **Só se falhar:** retomar $\beta_n(\phi_-)$ como mecanismo de
   reparo, agora por motivo verificado e não herdado.

## 7. O que isto diz sobre a v1

A narrativa central da TDCP — *dois setores geométricos cuja separação
estrutural evolui com a história cósmica e produz aceleração tardia* —
**está correta e é realizada pelo formalismo**, no ramo finito.

O que a v1 tinha de errado não era a física; era uma constraint. E a
constraint errada a empurrou para os dois becos documentados no
parecer: o ramo algébrico (onde $r$ é constante) e um "ramo dinâmico"
que, com o segundo fator errado, também congelava $r$.

O Cap.14 §14.12 — que a auditoria criticou com dureza por contornar
$\dot r=0$ — estava certo ao desconfiar. Errou o método e a condição
substituta, mas a intuição de que $r$ **tinha** que evoluir era boa.
