# D2 — Evolução Temporal Real vs Espectro Congelado: Resultado

**Data:** 2026-08-11. Script: `auditoria/code/d2_evolucao_reduzida.py`
(2 rodadas; 1ª preservada em `out/d2_evolucao_reduzida_rodada1.txt`,
2ª — oficial — em `out/d2_evolucao_reduzida.txt`; sondas de diagnóstico
em scratchpad, resultados reproduzidos na 2ª rodada). Execução:
autorizada pelo autor, feita em sessão pelo `.venv`.

**Este é o resultado mais importante do dia — e vai na direção OPOSTA
à esperada.** O critério pré-declarado ("se não-genérico: reescrever o
enunciado tardio — melhor nós que o referee") disparou, e o que ele
revelou é maior que o enunciado tardio.

---

## 1. Veredito em três linhas

1. **O taquião tardio congelado NÃO é dinâmico.** No ponto fixo
   profundo (a∈[400,1900]), TODAS as soluções do bloco métrico diluem
   como osciladores saudáveis (−1.38H/−1.15H ≈ −3/2·H) contra
   previsões congeladas de σ/H = 2.97/6.83; a projeção no automodo
   taquiônico é drenada (0.46→0.03→…). O enunciado **"taquião eterno"
   (`resultado_setor_escalar.md` §7) CAI** para esta célula e estes k.
2. **A instabilidade real é transiente, limitada e tipo-gradiente**:
   crescimento só na época de transição (a∈[15,45]), com taxa
   crescendo com k (+0.23H em k_phys~1; +1.48H em k_phys~10) e
   amplificação total modesta (ln A ~ 4) antes de morrer —
   **exatamente o quadro da literatura** para o ramo finito
   ("instável cedo/transição, saudável tarde").
3. **Watershed metodológico**: autovalores congelados não são árbitro
   de saúde nesta classe. As matrizes comóveis reduzidas NUNCA
   assentam (K_r ~ a³; |K̇_r|/|K_r| ≈ 1.9H *no ponto fixo*) — o QEP
   congelado descarta exatamente os termos que dominam a dinâmica
   tardia (fricção de Hubble e reescalonamentos). Sondas: matrizes
   congeladas de verdade CRESCEM como previsto (integrador validado);
   as verdadeiras diluem.

## 2. A cadeia de evidência desta conclusão

1. 1ª rodada: taxas reais ~0.4–1.3H vs congelado 3.1–6.2H —
   discrepância impossível para coeficientes constantes → sondas.
2. Sondas: (P1) deriva de 375% das matrizes reduzidas entre a=15 e 45,
   com o fundo assentado — os fatores explícitos de a(t); (P2)
   evolução com matrizes artificialmente constantes cresce (validando
   o integrador; janela curta explica o valor parcial); (P3) projeção
   no automodo taquiônico drenada monotonicamente; (P4) taxa tardia
   real = −1.478H ≈ −3/2·H (diluição de oscilador).
3. 2ª rodada (oficial, endurecida): janela a∈[0.2, 2000], três janelas
   de ajuste, dois k_c, âncoras congeladas em a=30 E a=400 (a previsão
   congelada é persistente — e vácua), controles GR/δχ/halving todos
   PASSAM. Confirmação integral.

Nota numérica declarada: a janela tardia do controle GR dá NaN — na
era de matéria H→0 e o passo dt=dN/H explode (instabilidade do RK4 no
oscilador, não física). O bimétrico não sofre disso (H→const no ponto
fixo). Controle GR válido nas duas primeiras janelas (−1.2 a −1.9H ✓).

## 3. O que cai, o que fica, o que muda de estatuto

**CAI (para a célula REF μ=1, k_phys∈{1,10}, nesta trajetória):**
- O "taquião eterno" do ponto fixo — a peça central do no-go tardio.
- O uso de σ/H congelado como veredito de instabilidade nesta classe
  (as taxas congeladas nunca se realizam dinamicamente no tardio).

**FICA (intocado por este resultado):**
- Fundo do ramo finito (ṙ≠0, limite GR exato) e setor tensorial
  (enunciados de fundo/massa, não de espectro congelado escalar).
- **A assinatura cinética indefinida** (autovalor NEGATIVO de K_red,
  medido pela redução exata do D1: −0.105 na REF, −3.4e-4 na fresta).
  A evolução linear não testa fantasma (num sistema linear sem
  acoplamentos, direção de energia negativa não gera crescimento);
  o perigo do fantasma é de interação. O estatuto: afirmação
  ESTRUTURAL verdadeira, cuja letalidade física agora é a pergunta
  certa — e conecta diretamente com o debate de literatura
  ("breakdown of linear perturbation theory rather than physical
  instability", 2507.11526).
- As medidas de composição (G1-b, C1: projeções, identidade π_L/π⁰,
  balanço) — são afirmações sobre os autovetores congelados,
  corretas como tais; a *interpretação de saúde* herda a revisão.

**MUDA DE ESTATUTO (de veredito para "sob reavaliação"):**
- TODOS os vereditos de saúde escalar do programa baseados em espectro
  congelado: o no-go β-constante (~1500 pontos), o no-go da modulação,
  o ramo algébrico, e as tendências da Investigação 2 Fase B. Cada um
  precisa do teste de evolução real (a maquinaria agora existe e é
  barata) antes de qualquer enunciado final. Não estão "revogados" —
  estão suspensos como vereditos dinâmicos; permanecem como
  caracterizações do espectro congelado.

## 4. Convergência com a literatura — e o que sobra de novo

O quadro real medido (transiente limitado tipo-gradiente na
transição; saudável no tardio) é o consenso da literatura para o ramo
finito (Comelli et al.; Könnig et al.; leitura moderna). Isso é uma
**reconciliação**, e muda o paper:

- A alegação "no-go tardio novo" morre antes de nascer errada — o
  posicionamento (D1 dos desafios) tinha razão em exigir a prova.
- O que emerge como contribuição genuína: (i) a demonstração
  explícita, com dupla rota validada, de **por que** o diagnóstico
  congelado falha nesta classe (matrizes comóveis que não assentam;
  fricção estrutural ~2H no "ponto fixo") — um aviso metodológico
  quantificado para o campo; (ii) a maquinaria de redução dependente
  do tempo + evolução real (validada em GR, com halving); (iii) os
  resultados de fundo/tensor/estrutura que não dependem disso
  (m_T²/H²→12; o regime não-fatorado da Investigação 2 Fase A; o
  limiar de back-reaction; a assinatura cinética pela redução exata).

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Taxas reais tardias ≈ −3/2·H, todas as ICs, dois k_c; projeção drenada | 2b (célula REF, trajetória, k testados; controles ✓) |
| O QEP congelado prevê σ/H≈3 persistente nas MESMAS matrizes | 2b (dupla rota, D1) |
| Logo: o taquião tardio congelado não é dinâmico nesta célula | 2b |
| Mecanismo (matrizes comóveis não assentam; \|K̇\|/\|K\|~2H) | 2b (medido) |
| Crescimento transiente tipo-gradiente na transição | 2b (dois k; razão de taxas ~ razão de k) |
| "Todos os vereditos congelados do programa exigem reavaliação" | consequência metodológica — regra de método nova |
| Assinatura cinética indefinida permanece (D1) | 2b (estrutural; letalidade em aberto) |

## 6. Fila de reavaliação (a nova trilha de cálculo)

Com a maquinaria de evolução real pronta (barata: ~1 min/célula):

1. **R-1**: varredura de células do no-go β-constante (amostra
   representativa das ~1500) por evolução real — o no-go sobrevive
   dinamicamente em alguma região?
2. **R-2**: a fresta μ=0.1 e a questão do fantasma — evolução real +
   caracterização da direção de K negativa (acoplamentos, energia).
3. **R-3**: a janela não-fatorada da Investigação 2 (Fase B refeita
   por evolução real na trajetória de rolagem — as tendências
   congeladas de σ/H até 13 podem ser igualmente vácuas!).
4. **R-4**: k grandes (k_phys ≫ 10) — a instabilidade de gradiente da
   literatura deve aparecer em tempo real; medir e comparar taxas.
5. Só então: o enunciado final do setor escalar, e o cap. 07.

A ironia final do dia, registrada: o programa passou meses matando a
teoria com o instrumento congelado — e o item de posicionamento que o
referee teria usado contra nós acabou salvando **a nós** de publicar
um no-go vácuo, e possivelmente salvando **a teoria** de um veredito
que a dinâmica real não sustenta. A estratificação epistêmica e os
critérios pré-declarados funcionaram exatamente como desenhados.
