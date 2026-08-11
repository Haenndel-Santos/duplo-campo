# D1 — Redução Explícita de Vínculos: Resultado

**Data:** 2026-08-11. Script: `auditoria/code/d1_reducao_vinculos.py`
(saída em `auditoria/code/out/d1_reducao_vinculos.txt`). Resolve o item
D1 de `docs/posicionamento_literatura.md` §2 — o desafio de referee
crítico contra o no-go tardio.

---

## 1. Veredito em uma linha

**O par doente sobrevive à redução explícita de vínculos.** O espectro
do QEP 7×7 é idêntico, modo a modo, ao do sistema físico obtido por
redução Faddeev–Jackiw exata (multiplicadores eliminados por
Schur/IPP em aritmética racional, fundo a 30 dígitos), nos 4 pontos
testados (REF μ=1 e fresta μ=0.1, k_phys ∈ {1, 10}, ponto fixo a=10).
O taquião persiste com a mesma taxa e o fantasma vira enunciado
**invariante**: autovalor negativo da matriz cinética reduzida.

## 2. Os números

Âncora GR pela rota de redução: 1 modo (δχ), K_red=+0.5, ω² = 1.7119
(k=1) e 100.7119 (k=10) — **iguais aos do QEP a 4 casas**. Poder de
detecção da rota confirmado.

| Ponto | Redução | Contagem | eig(K_red) | Espectro vs QEP |
|---|---|---|---|---|
| REF μ=1, k=1 | 4 multiplicadores eliminados em 1 rodada | 3 (Ψ_f, E_f, δχ) | **(−0.105, +0.034, +0.500)** | **idêntico** |
| REF μ=1, k=10 | idem | 3 | (−6.55, +0.50, +18.0) | idêntico |
| fresta μ=0.1, k=1 | idem | 3 | **(−3.37e-4, +1.29e-4, +0.500)** | idêntico |
| fresta μ=0.1, k=10 | idem | 3 | (−2.58e-2, +6.50e-2, +0.50) | idêntico |

- **Taquião no sistema reduzido**: SIM — ω²=−4.35, σ/H=3.74 (REF,
  k=1); par complexo com σ/H=2.99 em k=10.
- **Fantasma como assinatura de K_red**: SIM — a fresta tem exatamente
  1 direção cinética negativa (−3.4e-4 em k=1), e a REF μ=1 **também**
  (−0.105): o parceiro do dubleto é fantasma cinético genuíno no
  sistema reduzido, não ambiguidade da norma QEP em 7 campos.

**Nota de convenção (para o paper):** este script reescala a→1 (k
físico); a Investigação 1/G1-b usou a=10 com k comóvel. Os valores
batem exatamente sob k_phys=k/10 — ex.: o taquião ω²=−4.3467 de hoje
(k_phys=1) é idêntico ao valor "k=10" da Investigação 1. Âncoras
cruzadas perfeitas; declarar a convenção em qualquer tabela.

## 3. O que isto estabelece (e o que ainda não)

**Estabelecido (a objeção do referee nº 1 dissolve):** as análises
publicadas integram lapso/shift antes de diagnosticar; fizemos o mesmo,
exatamente, e nada muda. Os 3 pares finitos do QEP **são** os modos do
sistema fisicamente reduzido; o diagnóstico de fantasma agora é
assinatura da matriz cinética reduzida (invariante, sem a
k-dependência da norma de autovetor que o próprio
`no_go_beta_constante.md` flagava como ressalva técnica). Nível: 2b
nos pontos testados, com a álgebra da redução exata (racional).

**A fronteira que permanece — agora afiada:** a contagem reduzida é
**3** no nível congelado. A contagem esperada da teoria completa
(com a constraint **secundária**, que o nível congelado
comprovadamente não enxerga — cegueira declarada em `gate2_ghost.md`
§4) seria 2 (helicity-0 + δχ). Isto **resolve a disputa interna do
corpus** (Cap.6.2 §6.4 dizia 3; Anexo C §C.3 dizia 2 — G1-a linha 19):
ambos podiam estar certos, em níveis diferentes — 3 é a contagem
congelada (confirmada por dupla rota), 2 é a pós-secundária. E
transforma o item D2 do posicionamento na pergunta exata:

> Das 3 direções congeladas, qual é a que a secundária removeria — e o
> taquião vive na direção física (helicity-0) ou na removida?

A resposta decide o enunciado final do no-go tardio. O suporte
existente aponta para o taquião ser físico (a C1 mediu o taquião como
π_L=0.995 — o helicity-0, que É o modo físico esperado; o candidato
natural a direção-removida é o parceiro de norma quase nula), mas isso
é inferência, não redução — o D2 fecha.

## 4. Efeito no posicionamento

- D1 do `posicionamento_literatura.md` §2: **RESOLVIDO A FAVOR** — com
  a reformulação acima do que resta (a pergunta da secundária passa a
  ser parte do D2).
- O parágrafo de método do paper ganha força: QEP e redução explícita
  são rotas independentes com espectros idênticos; a GR calibra as
  duas.
- A ressalva técnica antiga sobre a k-dependência do diagnóstico de
  fantasma (`no_go_beta_constante.md` §"Ressalva técnica") fica
  **superada** pela assinatura de K_red.

## 5. Próximo passo

**D2** — comparação com a literatura nos mesmos fundos: reproduzir a
redução dependente do tempo (estilo Comelli–Crisostomi–Pilo, com a
secundária ativa) e (i) confirmar a contagem 2 pós-secundária, (ii)
localizar o taquião (físico vs removido), (iii) confrontar com a
instabilidade de gradiente deles. É o último item técnico antes do
cap. 07 poder enunciar o no-go tardio na forma final. **D3** (constante
da era de radiação) segue barato e independente.
