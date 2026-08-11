# C1 — Derivação de Stückelberg: Resultado

**Data:** 2026-08-11. Script: `auditoria/code/stuckelberg_goldstone.py`
(saída em `auditoria/code/out/stuckelberg_goldstone.txt`). Executa o
caminho para 2a nomeado em `docs/gate1c_nota_trilema.md` §7. Âncoras de
continuidade reproduzidas (σ/H=3.6510; kN=−1.616e-5) — resultado
interpretável.

---

## 1. Placar (critérios pré-declarados no cabeçalho do script)

| Critério | Conteúdo | Resultado |
|---|---|---|
| **C1** (estrutura, 2a) | órbitas de Goldstone derivadas por 2 rotas + controle negativo; quebra = potencial puro (K_int=C_int≡0); órbitas geram o bloco-f | **PASSA** |
| **C2** (composição, 2b) | 17/17 modos patológicos com ≥0.95 do autovetor em {órbita+multiplicadores} | **PASSA** |
| **C3** (origem da massa, 2b) | taquiões com rI≥0.5 (potencial dominado pela quebra) | **FALHA** (6 de 9) — ver §4 |

**Leitura de uma linha:** a premissa estrutural da circularidade
HR–Goldstone **sobe a 2a e a composição a confirma com identidade
específica** (§2–3); o que caiu foi a glosa mecânica "pseudo-Goldstone
ganha massa da quebra" — a massa taquiônica é, em k=1, o resíduo de
~0.5–1% de um **cancelamento** entre o termo de quebra e o setor
EH/vínculos (§4). O §8(i) do `gate1c` (composição divergente
enfraqueceria a nota) **não disparou**.

## 2. O que subiu a nível 2a (Parte A)

1. **Vetores de órbita das difeos relativas** (gauge plano-g;
   transformação representável agindo só em f, módulo o diagonal
   fixado): δΦ_f=−Ṫ−(ξ̇/ξ)T, δΨ_f=ξH_f T, δB_f=ξT/b+bŻ/(ξk),
   δE_f=Z/k. Derivados por derivada de Lie automatizada casada contra a
   parametrização da própria biblioteca, conferidos contra formas
   fechadas independentes, com controle negativo detectando corrupção
   deliberada. **Duas rotas + poder de detecção = 2a.**
2. **A quebra entra puramente como potencial**: K7 e C7 não contêm
   Fb/Fp/Fpp (simbólico e numérico). Consequência imediata: **doença
   cinética (fantasma) não pode nascer diretamente do termo de
   quebra** — a norma negativa nasce da eliminação de vínculos do setor
   EH na presença do potencial de quebra.
3. **O setor de Goldstone é o bloco-f inteiro** (det da matriz de
   órbitas ≠ 0 em todos os fundos): o espaço de campos fatora em
   {multiplicadores-g} ⊕ {órbitas de Goldstone} ⊕ {δφ₋}. Combinado com
   o G1-b (projeção δφ₋ = 0), segue **por derivação** que os modos
   patológicos vivem no setor {Goldstone + multiplicadores}.

## 3. A identidade de Goldstone dos modos doentes (Parte B, 2b)

Decomposição exata do bloco-f de cada autovetor na base de órbitas —
π⁰ = Goldstone temporal (T,Ṫ); π_L = longitudinal (Z,Ż), o helicity-0
"clássico" do gráviton massivo:

| Regime | Modo doente | Identidade medida |
|---|---|---|
| k=1, REF μ∈{0.3,1,3,10} | taquião do dubleto | **π_L = 0.994–0.998** (via Ż→B_f) + ~0.47 multiplicador B_g |
| k=1, REF (parceiro) | fantasma | π_L = 0.86–0.96 |
| k=10, REF | taquião | **π⁰ = 0.99–1.00** |
| k=10, REF | fantasma | π⁰ = 0.95–0.97 |
| k=1, fresta μ=0.1 | fantasma quase-nulo | **π⁰ = 0.998** — consistente com a composição Φ_f:1.00 já medida em `estrutura_par_relativo.md` |

Três achados:

1. **O taquião de k=1 É o helicity-0** (π_L ~0.995) — a afirmação da
   circularidade na sua forma mais literal, agora medida, não citada.
2. **A identidade é k-dependente**: em k=1 o par doente é da família
   π_L; em k=10, da família π⁰. Consistente com a dependência-em-k dos
   diagnósticos já documentada no no-go.
3. **A fresta fecha o círculo**: o fantasma quase-nulo é o Goldstone
   temporal puro — exatamente a direção do lapso Φ_f que
   `estrutura_par_relativo.md` mediu por outra rota.

## 4. C3: o que falhou, e o que os números dizem no lugar

O critério pré-declarado (taquiões com rI≥0.5, "a quebra domina o
potencial que o modo sente") falhou em 6 de 9 taquiões. Os números,
sem arredondar:

| Caso | wI = v†W_int v | wB = v†W_EH v | rI | Padrão |
|---|---|---|---|---|
| k=1, μ=0.3/1/3/10 | +139 / +250 / +295 / +270 | −141 / −252 / −296 / −272 | 0.498–0.499 | **cancelamento quase exato** |
| k=10, μ=1 | +57 | −477 | 0.106 | EH-dominado |
| k=10, μ=3 | −49 | −261 | 0.158 | EH-dominado |
| k=10, μ=0.3 | −77 | −20 | 0.792 | quebra-dominado |
| k=10, μ=10 (2 modos) | +499 / −112 | −420 / +33 | 0.543 / 0.773 | quebra-dominado |

**O caso k=1 é o achado**: rI≈0.499 não é "quase passou" — é a
assinatura de |wI|≈|wB| com sinais opostos. O termo de quebra
contribui **positivamente** (estabilizador) e o setor EH/vínculos
**negativamente**; a massa taquiônica líquida é o resíduo de ~0.5–1%
do cancelamento (μ=1: +250.4−251.7=−1.3; sanidade:
v†Wv/v†Kv=−3.9≈ω²=−4.14 ✓, correção giroscópica pequena).

**Leitura honesta:**

- A glosa "pseudo-Goldstone textbook" (massa do taquião vem da
  curvatura do termo de quebra) está **refutada como enunciada** — em
  nenhum regime de k=1 a quebra domina, e em k=10 o padrão é
  heterogêneo.
- Isso **não enfraquece a circularidade** — que se apoia na composição
  (§2–3, confirmada e elevada) — mas **corrige o mecanismo**: a doença
  vive no *balanço* entre o potencial de quebra e a estrutura
  EH/vínculos, não na quebra isolada.
- **Nota interpretativa (nível 3, rotulada como tal):** o cancelamento
  oferece uma explicação natural para o no-go da modulação — modular
  β₁(φ₋) mexe no lado wI de um balanço em que a massa líquida é ~1% de
  cada lado; o autovetor se reajusta e o resíduo não vira de sinal.
  Não é derivação; é consistência a posteriori. Se algum dia valer a
  pena, o teste seria: recomputar wI/wB sob modulação e ver o balanço.

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Órbitas de Goldstone = bloco-f; quebra = potencial puro | **2a** (era 3 na nota do trilema) |
| Modos patológicos ⊂ {Goldstone+multiplicadores}, δφ₋ espectador | **2a+2b** (derivação + medida) |
| Identidade π_L do taquião k=1; π⁰ do fantasma da fresta | 2b |
| Massa taquiônica de k=1 = resíduo de cancelamento quebra×EH | 2b (nos fundos testados) |
| "Cancelamento explica o no-go da modulação" | **3** (interpretativa, rotulada) |
| Glosa "massa vem da quebra" (pseudo-Goldstone textbook) | **refutada** (2b) |

## 6. Efeito sobre o gate1c e a Investigação 2

- A premissa 1 da circularidade (`gate1c` §3) sobe de nível 3 para
  **2a (estrutura) + 2b (composição)**. O critério anti-circularidade
  passa de argumento a resultado. §8(i) não disparou; §8(ii)/(iii)
  continuam como estavam.
- O desenho da Investigação 2 ganha um alvo adicional, agora com base
  empírica: **qualquer candidato a cura tem de alterar o BALANÇO
  quebra×EH — mexer só no termo de quebra já demonstrou ser
  insuficiente duas vezes** (modulação: empírico; agora: estrutural).
  O regime p_φ≠0 muda a estrutura de vínculos — exatamente o lado EH
  do balanço — o que torna a Investigação 2 o teste certo também por
  esta via.

## 7. Fila

C1 concluída. Trilha de cálculo: próximo passo é a **Investigação 2**
(condensação dinâmica, p_φ≠0), sob os critérios do `gate1c` §5 mais o
alvo do §6 acima. Trilha de escrita: v2 enxuta (o material deste doc
entra nos caps. 07–08).
