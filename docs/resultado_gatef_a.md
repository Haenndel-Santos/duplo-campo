# Gate F-a — Resultado: a Banda é Física (F-a3); H-CONSTRAINT Escala para o F-b

**Data:** 2026-08-12. Script: `auditoria/code/gatef_a_constraint.py`
(saída em `auditoria/code/out/gatef_a_constraint.txt`). Execução:
autor (.venv). Primeira etapa do Gate F
(`gate_fantasma_estrutural.md` §2), com o F-a3 (certificação da banda
do R-4) que motivou a sequência F-a → bloco 3 decidida pelo autor.

**Resumo em duas linhas:** o F-a3 entregou — **a banda é física**
(sobrevive intacta na superfície do candidato a vínculo, nos dois
fundos; bloco 3 liberado). O teste principal (F-a1/F-a2) foi
**inconclusivo por instrumento**: o portão abortivo de poder disparou
como desenhado, e o diagnóstico é exatamente a parede de normalização
que o R-2 §2 declarou — a saída pré-declarada é o F-b.

---

## 1. F-a3 — a certificação da banda (o resultado da rodada)

| fundo | lnA_passagem genérico | na superfície | BASE (vs R-4b) | veredito |
|---|---|---|---|---|
| β₁=1 | +3.97 | **+3.98** | ok (+3.97) | **BANDA-FÍSICA** |
| β₁=4.47 | +3.62 | **+3.15** | ok (+3.62) | BANDA-FÍSICA (marginal: Δ=0.47 < 0.5) |

As ICs construídas **sobre** a superfície adiabática do candidato —
i.e., com excitação livre nula da direção K<0 nestas coordenadas —
produzem a MESMA amplificação de passagem que as genéricas (que
carregam componente O(1) nessa direção). **A banda do R-4 não é
alimentada pela componente fora-da-superfície do candidato a
vínculo.** O medo que motivou a ordem F-a → bloco 3 está descartado.

Caveat herdado e declarado: a certificação vale **nas coordenadas do
instrumento** (comóveis) — como toda quantificação do programa desde
o R-2. A consistência interna é forte (gen/sup coincidem; BASE
reproduz R-4b ao centésimo), e a forma por faixa de kh da superfície
acompanha a genérica nas faixas dominantes. No 4.47 a diferença 0.47
fica logo abaixo do limiar — anotada, não interpretada.

## 2. F-a1/F-a2 — inconclusivo por instrumento (o portão funcionou)

O veredito impresso foi "PODER FALHOU → NÃO INTERPRETAR SUP" — o
desenho abortivo evitou qualquer conclusão falsa. A autópsia, em três
camadas:

1. **O QEP não vê o modo rígido verdadeiro.** O "quer ser vínculo" do
   R-2 (ω² crescendo até ~10⁹) nunca aparece nos pares agrupados: o
   modo mais pesado SOBREVIVENTE tem ω/H ≤ 18.5 com R≈1 (par de |ω|
   quase igual — assinatura de par/quarteto, não de hierarquia). O
   pareamento ±λ descarta o modo rígido nas escalas comóveis extremas
   — o mesmo aviso de mau condicionamento do D1/R-2. A régua de
   hierarquia ficou cega (R≥10 em 0/40 marcos) → medianas nan → o
   portão disparou.
2. **A construção de superfície herda a poluição de normalização do
   R-2.** Os perfis medem δ_rel ≡ 0.000 tanto para a superfície do
   candidato QUANTO para a superfície FALSA (direção leve), enquanto
   as genéricas ficam em O(1): em coordenadas com escalas díspares,
   os autovetores de K_red são dominados pela escala, e a "relação
   algébrica" de qualquer direção escala-dominante é trivialmente
   satisfeita — o teste perde o dente. Não é um bug de código; é a
   física da base errada.
3. **A saída correta não é remendo de base ad-hoc** (rescalonamentos
   diagonais etc. são meias-medidas com as mesmas patologias): é a
   normalização canônica simplética por ponto, com os termos de
   conexão temporais retidos — **exatamente o F-b**, como o gate
   pré-declarou ("qualquer quantificação de letalidade exige
   normalização canônica", R-2 §2; ramo "se NÃO → F-b").

Dado aproveitável (descritivo): a partir de a≈1000, o pesado
sobrevivente alinha exatamente com a direção K<0 (proj = 1.000) e seu
ω/H cresce lentamente (5.6 → 18.5) — consistente com o quadro do R-2,
mas nas coordenadas poluídas isso não sobe de nível.

## 3. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Banda sobrevive na superfície do candidato (lnA_sup ≈ lnA_gen; BASE ✓) | 2b (nas coordenadas do instrumento; caveat R-2 herdado) |
| Bloco 3 liberado (o confronto não herda a dúvida do vínculo) | consequência da linha acima |
| H-CONSTRAINT (contagem 3→2; identidade da direção) | **NÃO DECIDIDA** — inconclusiva por instrumento; F-b necessário |
| Diagnóstico da falha (QEP cego ao rígido; base escala-dominada) | 2b (sintomas medidos: R≈1, δ≡0 dupla, proj tardio 1.000) |
| Fantasma estrutural (assinatura) | inalterado (R-2): robusto; letalidade segue aberta |

## 4. Fila (sequência do autor mantida)

1. **Bloco 3 do R-4** (liberado pelo F-a3): dicionário de épocas +
   confronto e^lnA vs vínculos — aguarda a decisão de desenho do
   autor (opções A/B/C na sessão; recomendação B+C: integral parcial
   da era Λ real ~0.7 e-fold + braço de modos ENTRANDO na era de
   matéria, nunca sondado).
2. **F-b** (agora necessário para o fantasma, depois do bloco 3):
   transformação simplética dependente do tempo por ponto
   (diagonalização canônica de K_red com termos ∝ Ṫ retidos — a
   lição do D2), critérios F-b1/F-b2 do doc do gate. O F-a desta
   rodada vira o "antes" do par antes/depois: os mesmos testes
   (hierarquia, superfície, poder) rodados nas variáveis canônicas.
3. Anomalia IR do pousado e demais sub-estruturas: inalteradas.
