# Gate F — A Letalidade da Direção Cinética Negativa

**Data:** 2026-08-11 (noite). **Decisão de prioridade do autor**,
tomada após leitura crítica de D2/R-1/R-2: *"Não partiria agora para
'TDCP-2'. A F1 ganhou uma sobrevida real. Eu terminaria R-3/R-4 e,
sobretudo, faria da normalização canônica + Hamiltoniano/strong
coupling da direção K<0 o próximo grande Gate."* Este documento
formaliza esse gate, no método do projeto (critérios pré-declarados;
estratificação epistêmica; ramos de falha nomeados).

---

## 1. O problema

Após D2/R-1/R-2, o estado do setor escalar da F1 é
(`resultado_r2_fantasma.md` §3): dinamicamente estável no tardio;
instabilidade real transiente na transição; e **uma direção cinética
negativa estrutural universal** — assinatura invariante (Sylvester),
uniforme em k∈[1,300], persistente em a∈[30,1900], presente nas 14
células amostradas. A evolução linear não a testa (energia negativa
não gera crescimento linear sem acoplamento); as tentativas de
quantificar sua energia esbarraram em dependência de normalização.

**A pergunta do gate** (formulação do autor): *que tipo de grau de
liberdade é esse que possui uma direção cinética negativa na ação
quadrática instantânea, mas cuja evolução física completa é amortecida
no regime tardio?*

As cinco hipóteses em disputa (do autor, numeradas para referência):

1. **H-GHOST**: fantasma físico genuíno — vácuo instável na
   quantização/com interações; a F1 morre aqui, com precisão.
2. **H-NORM**: direção cuja interpretação muda após normalização
   canônica completa (a "negatividade" é artefato de base comóvel).
3. **H-SC**: strong coupling/degenerescência — a expansão quadrática é
   insuficiente nesse setor (a leitura moderna da literatura,
   2507.11526).
4. **H-CONSTRAINT**: grau removido/reorganizado pela constraint
   secundária dependente do tempo (invisível ao congelado).
5. **H-EFT**: estrutura mais sutil da teoria efetiva.

**Evidência já em mãos favorecendo H-CONSTRAINT** (2b, a testar
primeiro por ser barata): (i) contagem congelada = 3 onde a
pós-secundária esperada = 2 (D1; resolve a disputa Cap.6.2 vs
Anexo C); (ii) a frequência congelada do modo K<0 cresce com a
(ω²: ~6e3 → ~1.4e9, R-2) — direção que "quer ser vínculo".

## 2. Protocolo (três etapas, custo crescente)

### F-a — O teste da constraint (H-CONSTRAINT; barato; alvo 2a/2b)
Construir explicitamente a constraint secundária LINEARIZADA
dependente do tempo: a consistência temporal das equações dos
multiplicadores ao longo do fluxo (a maquinaria de redução do D2 já
tem todos os ingredientes — as equações dos auxiliares e suas
derivadas temporais numéricas). Impor a constraint sobre o sistema
reduzido 3×3 e verificar:
- **Critério F-a1:** a contagem cai de 3 para 2?
- **Critério F-a2:** a direção removida coincide com a direção K<0
  (projeção > 0.9)?
- **Se SIM em ambos:** o fantasma é artefato de representação
  (H-CONSTRAINT confirmada) — a F1 fica SEM patologia escalar
  conhecida no nível linear; o gate fecha com upgrade radical da F1.
- **Se NÃO:** H-CONSTRAINT cai; seguir para F-b.

### F-b — Normalização canônica (H-NORM/H-SC; médio; alvo 2b)
Transformação canônica dependente do tempo para variáveis de norma
unitária ao longo da trajetória (diagonalização simplética de K_red
por ponto, com os termos de conexão temporais retidos — a lição do
D2: nunca descartar termos ∝ Ṡ). Verificar:
- **Critério F-b1:** a assinatura negativa sobrevive nas variáveis
  canônicas? (Se a "negatividade" for consumida pelos termos de
  conexão, H-NORM confirmada.)
- **Critério F-b2:** a escala de energia física da direção negativa
  (agora invariante) — comparável a H? à massa do gráviton? ao cutoff
  Λ₃ ~ (m²M_Pl)^{1/3}? Se a direção viver em/além do cutoff,
  H-SC confirmada (o veredito honesto vira o da literatura: "fora do
  alcance da ordem quadrática" — e o setor não exclui a F1).
- **Se a direção sobreviver canônica e abaixo do cutoff:** fantasma
  físico no espectro linear → F-c.

### F-c — Interações (H-GHOST; caro; só se F-b indicar fantasma físico)
Estimativa da taxa de decaimento do vácuo via acoplamentos cúbicos da
direção negativa canônica (ordem de grandeza basta: se a taxa for
~cutoff, morte imediata; se for suprimida por potências de μ ou do
acoplamento, pode ser cosmologicamente inócua — fantasma "benigno" à
la EFT com cutoff baixo declarado). Escopo declarado: estimativa, não
teorema.

## 3. Ramos de saída (pré-declarados)

| Desfecho | Consequência |
|---|---|
| H-CONSTRAINT (F-a) | F1 sem patologia escalar linear conhecida; Gate F fecha; prioridade vira R-4 (transiente vs observações) e o cap. 07 é reescrito como "viabilidade condicional" |
| H-NORM (F-b1) | idem, com o aviso metodológico ampliado (mais um artefato de base) |
| H-SC (F-b2) | setor declarado fora do alcance quadrático; F1 não excluída; paper alinha com a literatura e a fronteira é honesta |
| H-GHOST (F-c) | a F1 morre com precisão cirúrgica — e a 2ª geração sabe exatamente o que substituir (o programa (b1)/anti-circularidade do gate1c reassume o centro) |
| H-EFT | o que sobrar que não se encaixe — documentar e decidir |

**Em qualquer desfecho, o gate produz o enunciado final do setor
escalar para o cap. 07.**

## 4. Reordenação da fila (decisão do autor)

1. **R-3** (Fase B por evolução real — decide também se o modo de
   condensação δφ₋, o candidato dinâmico mais próximo da narrativa do
   Cap.1, sobrevive à dinâmica real; a Fase B era congelada).
2. **R-4** (mapa lnA(célula, k) do transiente vs vínculos — a
   sobrevida da F1 é condicional a isto; a literatura morreu nesta
   praia).
3. **GATE F** (este documento) — F-a primeiro (barato e já com
   evidência a favor).
4. Só então: enunciado final → cap. 07 → paper.
5. O programa de emergência (TDCP-2 / trilema (b1)) fica em espera —
   não cancelado: o critério anti-circularidade e a genealogia do
   gate1c permanecem como ativos, reativados na hora que o Gate F der
   H-GHOST (e só então).

## 4-bis. ATUALIZAÇÃO — o gate foi executado (2026-08-12)

**F-a** (`resultado_gatef_a.md`): inconclusivo por instrumento em
coordenadas comóveis (o portão de poder abortou como desenhado); o
F-a3 certificou a banda do R-4 como física. **F-b**
(`resultado_gatef_b.md`, v2 com validação de resíduo): (i)
**H-CONSTRAINT falsificada em coordenadas válidas** — sem hierarquia
(R satura em 5–10), ω₀ satura, e a direção é fortemente acoplada
(DESAC 0.77–0.96): o "quer ser vínculo" do R-2 era artefato da base
comóvel; contagem = 3 dof (disputa D1 resolvida); (ii) o fantasma é
um **ramo espectral canônico propagante de norma-η ≈ −0.97 com
frequência invariante ω₀ = 12.0H (β₁=1) / 7.4H (β₁=4.47) ≈
3.4–4.3·Λ₃** — acima do cutoff → **fecho H-SC** pelo critério F-b2
(F-c fora de validade EFT; só por decisão do autor); (iii) bônus
CONF-BANDA: o congelado CANÔNICO assenta (ε_W→0.03) e **prevê a
banda** (σ_can 1.13/1.41 vs +0.93/+1.06 reais) — o aviso metodológico
ganha resolução construtiva. Enunciado final v4 do setor escalar no
§6 do doc F-b.

## 5. Nota sobre a conversa do "modo relativo" (Gate 1)

A motivação *"σ precisa ser emergente porque, como campo clássico
fundamental, é taquiônico"* está **anulada** pelo D2 — o taquião
tardio não é dinâmico. O que o Gate 1 estabeleceu documentalmente
(G1-a: a seta Φ₋→σ nunca foi derivada; zero elos de identidade) e as
medidas de composição (G1-b, C1 — corretas como afirmações sobre
autovetores congelados) permanecem. A pergunta estrutural continua
excelente por mérito próprio, mas sem o taquião como evidência. E a
nova dinâmica (crescimento transiente → estabilização tardia) é
qualitativamente mais próxima da narrativa fundacional do que o
"taquião eterno" jamais foi — com o caveat de mecanismo: a transiente
real é tipo-gradiente; a bifurcação do Cap.1 é de massa. A
identificação segue prematura (aguarda R-3).
