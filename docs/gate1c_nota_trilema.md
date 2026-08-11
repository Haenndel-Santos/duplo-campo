# G1-c — Nota do Trilema: a Seta Φ₋ → (g,f)

**Data:** 2026-08-11. Executa o G1-c de
`docs/gate1_identidade_relacional.md` §4 ("nota formalizando a
obstrução do trilema: ou uma prova adaptada ao contexto, ou a demolição
do prior — em qualquer caso, o trilema vira decisão documentada, não
default tácito"). Com G1-a e G1-b já fechados, esta nota **fecha o
Gate 1**.

**Resultado em uma linha:** o prior, como declarado, estava forte
demais e é parcialmente demolido (Weinberg–Witten não proíbe spin-2
massivo composto); em seu lugar entra uma obstrução mais precisa e
mais perigosa — a **circularidade HR–Goldstone** — que vira critério
de projeto pré-declarado para a Investigação 2.

---

## 1. O prior, como foi declarado

`gate1_identidade_relacional.md` §3, nível 3 declarado:

> "um segundo spin-2 não se compõe de escalares (obstruções tipo
> Weinberg–Witten; gráviton exige termo cinético próprio)"

O escrutínio é obrigatório pelo método: **dois priors de literatura já
caíram por cálculo neste projeto** (a "cura padrão" M_f≫M_g era 100%
taquiônica na varredura; o Higuchi da D8 era artefato do fundo errado).
Prior não escrutinado não decide nada.

## 2. Exame do prior — Weinberg–Witten diz menos do que o prior afirmava

**O teorema, com suas hipóteses** (nível 3 — literatura, mas enunciado
com as hipóteses explícitas para ser conferível): numa teoria com
tensor energia-momento conservado e Lorentz-covariante, não existem
partículas **sem massa** de helicidade |h|>1 no espectro (parte 2 do
teorema; a parte 1, com corrente conservada, proíbe |h|>1/2 carregada).

**O que o teorema NÃO cobre:** partículas de spin 2 **massivas**
compostas. Isso não é brecha especulativa — é fato experimental: a
f₂(1270) da QCD é uma ressonância spin-2 massiva composta de quarks.
Spin-2 massivo emergente de constituintes existe na natureza.

**Consequência para o trilema:** o prior "um segundo spin-2 não se
compõe de escalares" **sobrealcança**. A restrição correta é: um
gráviton *sem massa* composto é obstruído (dadas as hipóteses do
teorema); um multiplete spin-2 *massivo* composto, não.

Isso **bifurca o braço (b)** do trilema em dois alvos de custo muito
diferente:

- **(b1) g fundamental; só o multiplete massivo emerge de 𝓡.**
  Não bloqueado por Weinberg–Witten. E é o alvo *natural* no contexto:
  o ramo finito tem **limite GR primordial exato no setor g**
  (`resultado_ramo_finito.md`, nível 2b in-repo) — o polo não-massivo
  já é bem carregado por g fundamental; o que falta à teoria é
  exatamente o setor massivo/relacional.
- **(b2) g E f ambas emergentes.** Aí o gráviton sem massa também é
  composto, e Weinberg–Witten morde — a construção precisa das rotas
  de fuga padrão da gravidade emergente (ausência de T^μν covariante
  conservado no substrato, Lorentz só emergente, etc.). Custo muito
  maior; não é o alvo primário.

**Estado do prior após o exame: parcialmente demolido.** O que
sobrevive dele é a metade "gráviton exige termo cinético próprio"
aplicada ao polo sem massa — que (b1) contorna por construção,
mantendo g fundamental.

## 3. A obstrução que o prior não via: circularidade HR–Goldstone

Esta é a contribuição central da nota, e o risco real do braço (b).

**O argumento** (nível 3 na estrutura geral + suporte 2b in-repo):

1. O termo de interação bimétrico quebra diff_g × diff_f → diff_diag.
   Na linguagem de Stückelberg (estrutura padrão da EFT de gravidade
   massiva), os campos que restauram a simetria são os "Goldstones"
   das difeos **relativas** quebradas — e o **helicity-0 (σ_HR) é
   precisamente o escalar de Stückelberg** desse setor.
2. Logo: qualquer construção do braço (b) cujo padrão de quebra IR
   seja *difeomorfismos relativos* tem, como EFT de baixa energia, a
   própria classe HR/F1 — **a classe que o no-go acabou de matar** (β
   constante em ~1500 pontos; modulação β₁(φ₋); ramo finito; ramo
   algébrico — todos com fronteira declarada).
3. **Suporte in-repo (2b) de que isso não é abstração:** a composição
   dos autovetores patológicos é o dubleto de shifts B_g±B_f (μ~1) e
   o lapso Φ_f (μ→0) — `estrutura_par_relativo.md`. Lapsos e shifts
   são exatamente o setor de vínculos/gauge onde vivem os Goldstones
   das difeos quebradas. O modo doente da F1 **é** o setor da quebra
   relativa de difeos, medido, não presumido.

**A circularidade, nomeada:** "emergência com quebra G_g×G_f→G_diag"
lida como quebra de difeos relativas não é uma saída do no-go — é o
no-go com vocabulário novo. O modo mais provável de o programa R2
falhar não é dar errado: é **dar certo de volta para dentro da F1**.

**Critério anti-circularidade (pré-declarado, vinculante para a
Investigação 2 e para qualquer construção R2 futura):**

> Toda construção do braço (b) deve **nomear os geradores quebrados**.
> - Se forem (redutíveis a) difeos relativas: a construção só escapa
>   do no-go se demonstrar que cai fora do domínio varrido, por uma
>   das saídas **já declaradas** no veredito (β₃≠0/família F2;
>   acoplamento de matéria não-mínimo; regime p_φ≠0 onde a constraint
>   não fatora). Sem essa demonstração, é F1 renomeada — reprovada por
>   herança.
> - Se forem simetrias **internas/globais** (padrão U(1)×U(1)→U(1) de
>   condensados acoplados, modo de fase relativa tipo Josephson):
>   valem as duas cautelas já registradas — (i) o modo de fase pode
>   ser gapeado OU dinamicamente instável (contrafluxo; a analogia
>   organiza, não garante saúde — `gate1_identidade_relacional.md` §3);
>   (ii) um Goldstone interno **não é um grau métrico** — a construção
>   continua devendo o multiplete spin-2 massivo por outra via, e essa
>   dívida deve ficar explícita, não escondida na troca de vocabulário.

## 4. O trilema, redecidido

Com o prior examinado e a obstrução real nomeada, a decisão documentada
(que o gate exigia) é:

| Braço | Estado | Base |
|---|---|---|
| **(a)** f fundamental; Φ₋ = modulador | **FECHADO** — testado e reprovado | no-go da modulação β₁(φ₋) (`veredito_setor_escalar_final.md`); G1-b: projeção zero |
| **(b)** g/f efetivas de 𝓡 | **BRAÇO DE TRABALHO** — alvo primário **(b1)** (só o setor massivo emerge); teste atual: Investigação 2 (p_φ≠0) | W–W não bloqueia (b1); limite GR exato em g torna (b1) natural; sujeito ao critério anti-circularidade §3 |
| **(c)** grau relacional sem segunda métrica | **FALLBACK DECLARADO** — só se (b) falhar com fronteira declarada | custo já registrado: perde o setor tensorial da v2 (Higuchi automático, m_T²/H²→12) |

A Investigação 2 (condensação dinâmica, p_φ≠0) é o teste certo na fila
por uma razão estrutural: **é o único regime onde a constraint não
fatora** (resíduo −M_eff²m²p_φβ₁′ do Gate 2) — ou seja, o único regime
que já está, por construção, fora da estrutura de vínculos varrida
pelo no-go. É a saída declarada nº 5 do veredito, e agora com critério
anti-circularidade acoplado.

## 5. Critérios pré-declarados para a Investigação 2

Herdando as regras de método do projeto:

1. **Nomear o padrão de quebra** (critério §3) antes de interpretar
   qualquer resultado como "emergência".
2. **Declarar a classe da EFT resultante**: se a teoria efetiva no
   fundo condensado for da família β_n de HR, dizer em qual região do
   espaço (β, μ) ela cai — e conferir contra o mapa do no-go.
3. **Saúde espectral = σ E kN, em k=1 E k=10 no mínimo; ponto fixo
   como juiz** (regras vigentes).
4. **Auto-teste de poder de detecção na mesma rota e mesmo fundo**
   (regra vigente; o teste deve provar que *detectaria* a patologia
   conhecida antes de ser acreditado quando não a encontrar).

## 6. Estratificação epistêmica desta nota

| Afirmação | Nível |
|---|---|
| Enunciado de W–W com hipóteses; escopo restrito a partículas sem massa | 3 (literatura, hipóteses explícitas — conferível) |
| Existência de spin-2 massivo composto (f₂(1270)) | 3 (fato experimental estabelecido) |
| Limite GR primordial exato no setor g (âncora de (b1)) | 2b (in-repo, `resultado_ramo_finito.md`) |
| σ_HR = escalar de Stückelberg das difeos relativas quebradas | 3 (estrutura padrão da EFT de gravidade massiva; **não derivado in-repo** — ver §7) |
| O modo doente da F1 vive no setor de vínculos (shifts/lapso) | 2b (in-repo, `estrutura_par_relativo.md`; corroborado por G1-b) |
| A circularidade (§3, passo 2) | consequência lógica de duas premissas nível 3 + 2b — herda o nível da mais fraca: **3, com suporte 2b** |
| A decisão do trilema (§4) | decisão de programa documentada (era o mandato do gate), não teorema |

**O gate pedia "nível 3→2a".** O honesto: a nota cumpre o mandato
(trilema decidido e documentado; prior parcialmente demolido — que o
próprio gate listava como desfecho válido: "também informação"), mas a
obstrução central fica em nível 3 com suporte 2b, não 2a.

## 7. O caminho nomeado para 2a

A peça que falta é uma **derivação de Stückelberg in-repo**: introduzir
os campos φ^a que restauram diff relativa na ação de minisuperespaço já
validada, extrair o setor escalar de Goldstone e verificar que sua
composição coincide com o dubleto B_g±B_f / lapso Φ_f dos autovetores
patológicos medidos. Se coincidir, a premissa 1 do §3 sobe de nível 3
para 2a e a circularidade vira resultado, não argumento. Custo estimado:
uma sessão simbólica com a maquinaria existente (`tdcp_pert_lib.py`).
**Opcional antes da Investigação 2; não a bloqueia** — o critério
anti-circularidade do §3 já é aplicável como está.

## 8. O que demoliria esta nota

Pré-declarado, pelo método: (i) a derivação do §7 encontrar composição
**diferente** do dubleto medido — enfraqueceria o suporte 2b da
circularidade; (ii) uma extensão de W–W cobrindo spin-2 massivo
composto — restauraria o prior forte (nada conhecido nessa direção);
(iii) a Investigação 2 encontrar setor saudável **com** quebra redutível
a difeos relativas dentro da família F1 varrida — contradiria o no-go
na fonte e reabriria tudo (improvável: exigiria erro na cadeia de
evidência já consolidada).

## 9. Resultado da derivação do §7 (2026-08-11) — EXECUTADA

`auditoria/code/stuckelberg_goldstone.py`; detalhe em
`docs/resultado_stuckelberg_goldstone.md`.

- **A premissa 1 do §3 subiu a 2a (estrutura) + 2b (composição).**
  Órbitas de Goldstone derivadas por duas rotas com controle negativo;
  quebra = potencial puro (K_int=C_int≡0); setor de Goldstone = bloco-f;
  e a identidade medida: o taquião de k=1 **é** o π_L (helicity-0,
  0.995+), o fantasma da fresta é o π⁰ puro (0.998, a direção Φ_f). O
  §8(i) **não disparou** — a composição bateu. A circularidade é
  resultado, não argumento.
- **Refinamento que a derivação trouxe (o critério C3 falhou como
  pré-declarado, informativamente):** a glosa "pseudo-Goldstone ganha
  massa da quebra" está refutada — em k=1 a massa taquiônica é o
  resíduo de ~0.5–1% de um **cancelamento** entre a quebra
  (estabilizadora, wI>0) e o setor EH/vínculos (desestabilizador,
  wB<0). A doença vive no *balanço* quebra×EH, não na quebra isolada.
  Consequência para a Investigação 2: candidato a cura tem de alterar
  o balanço — mexer só na quebra já falhou empiricamente (modulação) e
  agora estruturalmente.
