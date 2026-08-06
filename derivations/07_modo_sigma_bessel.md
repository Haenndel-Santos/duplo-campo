# Derivação 7 — Solução Exata do Modo σ_k por Funções de Hankel (Cap.10 §10.3)

**Skill invocado:** `stability-constraints-auditor`.
**Script:** `code/07_bessel_sigma_k.py` (saída: `code/out/07_output.txt`).

## 1. O que está sendo derivado e por que é necessário

O Cap.10 §10.3 escreve a equação do modo relativo primordial (massa
taquiônica $m_\sigma^2<0$, fundo quase-de Sitter) e afirma:
*"Para $k\ll aH$: $\sigma_k\sim k^{-3/2}$"*, gerando espectro
"aproximadamente invariante de escala". A equação nunca é resolvida no
texto. Esta derivação resolve exatamente e verifica o expoente.

## 2. Ponto de partida

$$ \sigma_k''+2\frac{a'}{a}\sigma_k'+\big(k^2-a^2|m_\sigma^2|\big)\sigma_k=0, \qquad a=-\frac{1}{H\tau},\ \tau<0. $$

## 3. Derivação

Variável canônica $u=a\sigma_k$:

$$ u''+\Big(k^2-\frac{\nu^2-1/4}{\tau^2}\Big)u=0, \qquad \boxed{\ \nu^2=\frac94+\frac{|m_\sigma^2|}{H^2}\ } $$

(a massa taquiônica **soma** ao termo $a''/a$ e aumenta ν). Solução com
vácuo de Bunch–Davies:

$$ u=\frac{\sqrt{\pi}}{2}\,e^{i\pi(\nu+1/2)/2}\sqrt{-\tau}\,H_\nu^{(1)}(-k\tau) $$

— verificada simbolicamente (resíduo da EDO = 0 após a recorrência de
Bessel $H_{\nu-2}+H_\nu=\tfrac{2(\nu-1)}{x}H_{\nu-1}$). Assintótica
super-horizonte $-k\tau\to0$ com $H_\nu^{(1)}(x)\approx-\tfrac{i}{\pi}\Gamma(\nu)(x/2)^{-\nu}$:

$$ \boxed{\ |\sigma_k|\ \propto\ k^{-\nu}, \qquad \Delta_\sigma^2(k)\propto k^{\,3-2\nu},\qquad n_\sigma-1=3-2\nu\ \approx\ -\frac{2}{3}\frac{|m_\sigma^2|}{H^2}\ } $$

Verificação numérica (integração scipy de sub- a super-horizonte,
condição de Bunch–Davies): expoente medido coincide com $-\nu$ a
$10^{-6}$ para $|m^2|/H^2=0,1,3$ ($\nu=1.5000,\ 1.8028,\ 2.2913$).

## 4. Veredito sobre o Cap.10 §10.3

A claim $\sigma_k\sim k^{-3/2}$ vale **somente** no limite
$|m_\sigma^2|\ll H^2$ ($\nu\to3/2$). Com massa taquiônica não
desprezível, o espectro é red-tilted com desvio quantitativo
$n_\sigma-1\approx-\tfrac23|m_\sigma^2|/H^2$. A condição
"$|m_\sigma^2|\ll H^2$ durante a fase primordial" precisa ser
**declarada** no §10.3 (ela é coerente com o §10.7, que pede "massa
efetiva pequena", mas o texto nunca liga as duas coisas). Bônus: a
fórmula do índice espectral é uma **previsão nova e testável** que o
capítulo pode adotar ($n_s\approx0.965$ exigiria
$|m_\sigma^2|/H^2\approx0.05$ na fase primordial).

## 5. Classificação final

**DERIVADO SOB HIPÓTESE ADICIONAL** (fundo exatamente de Sitter +
vácuo de Bunch–Davies — hipóteses padrão, mas não declaradas no texto).
A claim original é o caso-limite $\nu\to3/2$; deve ser corrigida para
$k^{-\nu}$ com a condição de validade explícita.
