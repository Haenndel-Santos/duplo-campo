# TDCP v2 (enxuta) — Estrutura

**Criado:** 2026-08-11, executando a Decisão 1
(`docs/decisao1_congelamento_v1.md`). Este arquivo é o esqueleto
comentado; cada capítulo vira um arquivo `NN_titulo.md` nesta pasta.

**REVISÃO 2026-08-12 (pós-Erratum-02):** o esqueleto original tinha o
no-go escalar como resultado central (cap. 07) e excluía os capítulos
observacionais por falta de base saudável. O Erratum-02
(`auditoria/erratum_02_reducao_numerica.md`) mostrou que o 3º DOF
escalar era artefato de um bug da redução numérica; a cascata R-7
(`docs/resultado_r7_cascata.md`, `resultado_r7e_saude_interna.md`)
estabeleceu o sistema físico de 2 DOFs são em todos os regimes
testados; R-8a/b (`resultado_r8a_quase_estatico.md`,
`resultado_r8b_limite_mH0.md`) abriram o confronto observacional.
Caps. 01–02 e 07–10 e a lista de exclusões foram atualizados abaixo;
caps. 03–06 ficam como estavam (fundo, Bianchi e tensor não mudaram).

**Regras da pasta (vinculantes):**

1. **Ordem do plano:** ação → derivação → resultado → interpretação por
   último (`docs/plano_v2_reconstrucao.md`). Nenhuma afirmação
   interpretativa sem apontar a derivação que a sustenta (Gate 10).
2. **Gate 0 ativo:** `python auditoria/code/verifica_simbolos.py --alvo v2`
   contra esta pasta a cada sessão de escrita; critério = zero
   violações. O `docs/dicionario_simbolos.md` é normativo — inclusive
   as flags epistêmicas (a identificação "φ₋ modula β_n" é normativa,
   não derivada; G1-a).
3. **Toda afirmação quantitativa cita fonte versionada** — o doc de
   resultado E o script/saída em `derivations/code/out/` ou
   `auditoria/code/out/`.
4. **Nível epistêmico declarado** (1/2a/2b/3) em todo resultado
   enunciado; fronteiras de varredura sempre declaradas.
5. **Três nomes distintos** para o que a v1 chamava "modo relativo"
   (σ escalar, S isocurvatura, h₋ tensorial) — a sobrecarga catalogada
   no G1-a não entra na v2.

---

## Esqueleto

### 01 — O que este documento é
A tese em uma página: uma hipótese conceitual (dois campos primordiais
correlacionados; separação estrutural), uma implementação matemática
(TDCP-F1 sobre Hassan–Rosen) levada até o fim — incluindo a queda e a
revogação do próprio no-go que o programa havia produzido. O
resultado honesto atual: fundo ✓, setor tensorial ✓, setor escalar
SÃO (2 DOFs: 1 métrico overdamped + espectador δχ) em todos os
regimes testados; nenhuma validação observacional ainda (sub-horizonte
consistente com GR; quase-horizonte em aberto); a identificação
ontológica (φ₋ como grau primordial) segue normativa, não derivada.
Relação com a v1 (congelada; auditoria como ponte).
*Fontes: decisao1, erratum-02, resultado_r7_cascata,
resultado_r7e_saude_interna, resultado_r8a/b.*

### 02 — Método (agora com o caso máximo)
Estratificação epistêmica (1/2a/2b/3); gates com critério de falha
pré-declarado; auto-teste de poder; rota dupla. O capítulo ganha seu
caso definitivo: o ERRATUM-02 — um bug de 1.4–6% numa rotina de
redução produziu, por meses, um "3º DOF", um fantasma, uma banda e
uma previsão observacional, tudo internamente consistente e validado
pelos gates de representação única; a queda veio de auditoria externa
independente + prova de equivalência de ações (r6c) + localização
linha a linha (r6d). Lições codificadas: V-XREP-a/b, equilibração de
variáveis, normalização congelada para ganhos, gates SUSPEITO. O
método não é ornamento: derrubou cinco testes vácuos, um erro
estrutural do corpus (Bianchi) e o próprio resultado central anterior.
*Fontes: parecer Parte III-B, erratum-01 §8, erratum-02,
resultado_r7_cascata §0.*

### 03 — A ação e o dicionário
A ação completa (F1), simetrias, dimensões; o potencial V(φ₊,φ₋)
explícito; o dicionário como contrato de notação. A escolha
arquitetural "modulador = φ₋" apresentada COM a flag: decisão
normativa, testada e reprovada adiante (cap. 07).
*Fontes: docs/acao_v2.md, dicionario_simbolos.md, gate1a (flag).*

### 04 — Vínculos e a constraint de Bianchi correta
Minisuperespaço; as duas rotas (canônica e lagrangiana) para
B(r)·(N_f·ȧ−N_g·ḃ)=0; por que a forma do corpus v1 era impossível
(constraint canônica não contém lapso); os dois ramos da fatoração; o
resíduo −M_eff²m²p_φβ₁′ quando β₁=β₁(φ₋) (a constraint não fatora com
modulação — Gate 2). Aqui o Erratum 01 vira conteúdo, não errata.
*Fontes: erratum_01_bianchi.md, gate2_ghost.md, gate2_bracket.py,
bianchi_rota_lagrangiana.py.*

### 05 — O fundo do ramo finito
ṙ=H_g(ξ−r); a cúbica e a seleção de raiz (menor positiva + filtros
que abortam); r∝a³ e ξ=4r no primordial; limite GR exato; ponto fixo
tardio; Ω_m≈0.25. O mecanismo de separação estrutural que a v1
procurava — sem campo modulador nenhum.
*Fontes: resultado_ramo_finito.md, ramo_dinamico_correto.py.*

### 06 — Setor tensorial
m_T²/H²→12 universal no primordial (todos os parâmetros cancelam);
Higuchi automático com margem 6; a razão ≈4 hoje. A invalidação do
0/60 da D8 como estudo de caso do método (fundo errado ⇒ resultado
errado por construção).
*Fontes: resultado_ramo_finito.md §3–4, D2 (forma fechada).*

### 07 — O setor escalar: do falso no-go à saúde derivada (resultado central)
A história completa em três atos, com números: (i) o no-go aparente
(taquião/fantasma/1500 pontos) e o que ele realmente media — o
sistema espúrio de 3 DOFs criado pelo bug da redução (Erratum-02);
(ii) a queda: auditoria externa (det K=0 simbólico) + prova local de
mesma-ação (r6c, exato) + o bug linha a linha (r6d) + reprodução
independente; (iii) o setor corrigido: 2 DOFs (1 métrico overdamped
decadente + δχ espectador saudável), zero direções cinéticas
negativas em todos os regimes (benchmarks, classe μ×β₁ incl. fresta,
trajetória de rolagem/pouso incl. janela de deslocamento — W00 sem
trocas, sem FJ-quebra), consistente com o teorema HR e
Comelli–Crisostomi–Pilo. Banda, ISW e "strong coupling" retirados
como artefatos. Fronteiras e pendências declaradas (ramo algébrico
deferido; halving fino do kh=10).
*Fontes: erratum_02_reducao_numerica.md, resultado_r7_cascata.md,
resultado_r7e_saude_interna.md, saídas r6c/r6d/r7a–f.*

### 08 — O enquadramento R1 e a identificação normativa (a fronteira que fica)
Gate 1 completo, RELIDO pós-erratum: os quatro objetos identificados
só por decreto (G1-a) continuam por decreto — a saúde da F1 NÃO prova
a identidade φ₋ ↔ grau primordial; a projeção-δφ₋ (G1-b) e o trilema
(G1-c) mantêm-se como delimitação do que está derivado vs postulado.
O que muda: sem no-go, a F1 deixa de ser "órfã de implementação
saudável" — o problema aberto passa a ser a DERIVAÇÃO do vínculo
Φ₋/φ₋/χ/r, não a sobrevivência da implementação.
*Fontes: gate1_identidade_relacional.md, gate1a, gate1c; releitura:
resultado_r7e_saude_interna §6.*

### 09 — O programa observacional (o novo centro de gravidade)
O que já foi medido: sub-horizonte consistente com GR (μ, Σ dentro do
piso QS ~2%, valores centrais ≤0.66% em kh≥22 — R-8a, com o fraseado
de precisão honesto); a família do benchmark tem m_T/H₀ ≈ 2.3–2.4
CRAVADO pelo fundo (fold em s≈5.7): o postulado 30–300 H₀ do corpus é
INALCANÇÁVEL sem outra forma-β — vira escolha estrutural a declarar,
com o ajuste fino (U0 negativo) explicitado (R-8b). O que falta e
decide: a janela quase-horizonte kh ≲ 22 (baixo-ℓ, ISW, Gpc) com o
sistema dinâmico 2-DOF + matéria/radiação acopladas → C_ℓ, P(k),
lensing (R-8 completo); dicionário de épocas como decisão declarada.
Ativos da v1 que atravessam, reavaliados.
*Fontes: resultado_r8a_quase_estatico.md, resultado_r8b_limite_mH0.md,
r8_dicionario_epocas_opcoes.md.*

### 10 — Interpretação (por último, como manda o plano)
O que a narrativa significa À LUZ do estado atual: a separação
estrutural existe e evolui (cap. 05); a implementação F1 é
internamente sã mas a "memória da bifurcação" segue SEM portador
derivado (cap. 08 — a fronteira honesta não mudou de natureza, mudou
de urgência); as fórmulas de tempo relacional da v1 continuam
metáfora até derivação; η aposentado do núcleo. O que o episódio
erratum-02 significa para o programa: a teoria sobreviveu ao seu
próprio processo — o resultado é o par (implementação sã, método que
se autocorrige), não uma validação.
*Fontes: caps. anteriores; plano_v2 Passos 9–10.*

---

## O que fica de fora (por decisão, não esquecimento)

- **[REVISADO 2026-08-12]** Reconstrução dos capítulos observacionais
  da v1 (Cap.18–25): a base saudável para μ/Σ/fσ₈ EXISTE agora
  (R-8a/b); a reconstrução entra CONDICIONADA ao R-8 completo e ao
  dicionário de épocas — não antes (números da v1 permanecem
  inutilizáveis: eram do sistema espúrio).
- Anexos I–K (linha exploratória quântica): permanecem na v1
  congelada; sem ponte com a ação (G1-a linha 18).
- O ramo algébrico e a Investigação 2 original: substituídos pela
  releitura pós-erratum (R-7e/f); o ramo algébrico segue deferido com
  prior declarado.
