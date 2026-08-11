# TDCP v2 (enxuta) — Estrutura

**Criado:** 2026-08-11, executando a Decisão 1
(`docs/decisao1_congelamento_v1.md`). Este arquivo é o esqueleto
comentado; cada capítulo vira um arquivo `NN_titulo.md` nesta pasta.

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
(TDCP-F1 sobre Hassan–Rosen) levada até o fim, e o resultado honesto:
fundo e setor tensorial funcionam; o setor escalar tem um no-go
localizado e quantificado; o enquadramento R1 delimita o que o no-go
mata e o que deixa vivo. Relação com a v1 (congelada como registro;
auditoria como ponte). A "afirmação mínima" do plano v2 como enunciado
de partida.
*Fontes: decisao1, plano_v2 (afirmação mínima), veredito §4.*

### 02 — Método
Estratificação epistêmica (1/2a/2b/3) como regra, não ornamento; gates
com critério de falha pré-declarado; auto-teste de poder de detecção;
rota dupla. Por que isso está aqui e não num apêndice: o método pegou
cinco testes vácuos e um erro estrutural do corpus — é resultado.
*Fontes: parecer Parte III-B, erratum §8, veredito §4.*

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

### 07 — O no-go do setor escalar (resultado central)
A cadeia completa, com fronteiras: taquião σ≈(3–4)H eterno (ponto fixo
como juiz) em μ≥0.3; fantasma |kN|~μ³ em μ=0.1; ~1500 pontos 4D; a
doença mora no setor de vínculos (dubleto B_g±B_f, lapso Φ_f); a
modulação β₁(φ₋) atua no lugar certo com o sinal errado (dois canais,
ambos pioram); o ramo algébrico também morre (degenerado E taquiônico
na raiz, sem corredor). Enunciado do no-go com as saídas não-cobertas.
*Fontes: resultado_setor_escalar.md, no_go_beta_constante.md,
estrutura_par_relativo.md, veredito_setor_escalar_final.md (+ §6),
resultado_investigacao1_ramo_algebrico.md.*

### 08 — O enquadramento R1: o que o no-go mata e o que não mata
Gate 1 completo: os quatro objetos identificados só por decreto (G1-a,
zero elos derivados); a projeção zero da patologia em δφ₋ (G1-b,
17/17); o trilema examinado (G1-c): W–W demolido parcialmente, a
circularidade HR–Goldstone como obstrução real, critério
anti-circularidade. Conclusão: o no-go é da representação F1; o grau
relacional primordial segue sem realização matemática que feche — vivo
como hipótese, órfão de implementação.
*Fontes: gate1_identidade_relacional.md (+ §7–9), gate1a, gate1c,
resultado_investigacao1 §3.*

### 09 — O programa aberto
R2 e a Investigação 2 (condensação dinâmica, p_φ≠0 — o único regime
fora da estrutura de vínculos varrida); alvo (b1) do trilema; fallback
(c) declarado; a derivação de Stückelberg como caminho a 2a. Ativos da
v1 que atravessam (bloco Vainshtein/PPN aritmético, CLASS/ISW, previsão
n_σ−1 da D7, formalismo HR limpo do Anexo A). Critérios pré-declarados
para tudo.
*Fontes: gate1c §4–5, veredito §3 (saídas), plano_v2 (ativos).*

### 10 — Interpretação (por último, como manda o plano)
O que a narrativa da TDCP significa À LUZ do que foi derivado: a
separação estrutural existe e evolui (cap. 05); a "memória da
bifurcação" NÃO tem portador identificado na F1 (cap. 08); as quatro
fórmulas de tempo relacional da v1 são metáfora até segunda ordem
(Passo 10 do plano: ou UM funcional covariante, ou declarar metáfora —
aqui se declara metáfora, salvo resultado futuro da trilha de cálculo).
η aposentado do núcleo (Gate 9, caminho B) salvo derivação futura.
*Fontes: caps. anteriores; plano_v2 Passos 9–10; gate1a §5 (quarta
fórmula).*

---

## O que fica de fora (por decisão, não esquecimento)

- Reconstrução dos capítulos observacionais da v1 (Cap.18–25): sem
  setor escalar saudável, μ/Σ/fσ₈ da F1 não têm base — entram só como
  ativo metodológico no cap. 09.
- Anexos I–K (linha exploratória quântica): permanecem na v1 congelada;
  o próprio corpus os declara sem ponte com a ação (G1-a linha 18).
- Qualquer conteúdo que dependa da Investigação 2: entra quando ela
  rodar, no cap. 09.
