# Erratum 02 — Dobra de Ċ em W_XX na redução numérica (o "fantasma" do Gate F era artefato)

**Data:** 2026-08-12. **Gravidade:** alta — derruba a conclusão do
Gate F (fantasma canônico a ω₀ ~ 3–4 Λ₃) e contamina toda a cadeia
de dinâmica **reduzida**: D-2 (evolução reduzida), R-1, R-2, R-3/3b/3c,
R-4a/4b/4c (banda métrica), Gate F-a/F-b e R-5 (previsão ISW).

**Descoberto em:** reauditoria externa independente (sessão ChatGPT do
autor, 2026-08-12, pacote `TDCP_R6_reaudit_complete_2.zip`, preservado
em `auditoria/external/r6_reaudit_chatgpt/`), que refez o setor escalar
em ADM/Faddeev–Jackiw e obteve det K_métrico = 0 **simbólico** com
2 DOFs escalares — contra os 3 DOFs (um de norma negativa) de toda a
nossa cadeia. A verificação local (r6 → r6b → r6c → r6d) confirmou a
contagem externa e **localizou o erro no nosso código**.

---

## 1. O erro

A rotina numérica de absorção dos multiplicadores (`reduz_ponto`,
replicada de `d2_evolucao_reduzida.py` em diante — presente em
`d2`, `gatef_a`, `gatef_b`, `r1`, `r2`, `r3*`, `r4*`, `r5`) traduz o
`matrix_ipp_row` simbólico da lib para a trilha numérica com dois
desvios que, combinados, produzem um erro sistemático:

```python
cd = Cdot[i, j]        # (i) Cdot PRE-computado da C ORIGINAL (stale)
...
W[i, j] += cd          # (ii) soma incondicional — nao pula a entrada
W[j, i] += cd          #      ja zerada pela antissimetrizacao do
                       #      multiplicador anterior do par
```

Com `C_XX` simétrica (fato da nossa L2, verificado exatamente no r6c),
o par (i)+(ii) faz cada entrada **off-diagonal de `W_XX`** receber a
contribuição `Ċ` **duas vezes** (uma ao processar a linha de cada
multiplicador do par). A forma correta — derivada total
`d/dt(q S q)` com `S = −C_X` simétrica — soma **uma** vez por par
não-ordenado.

A lib simbólica está **correta** e nunca teve o bug:
`matrix_ipp_row` recalcula `cdot` da C **corrente** e pula `cij == 0`
(a segunda passada do par vê a entrada já antissimetrizada a zero);
`schur_eliminate` exige `C[X,:] = 0` e se recusa a rodar.

**Tamanho do bug:** 1.4–6.1% de `W_XX` (r6d, D2). Pequeno e **suave**
(Ċ é suave na trilha) — por isso produzia um "modo" liso, convergente
em resolução, com frequência estável: todos os sintomas de física.

## 2. Por que nenhum gate interno pegou

- **V1 (GR selfcheck)** valida a rota **simbólica** da lib (correta).
- **V-EQUIV-GR** (F-b) usa um sistema GR de **1 dof** — o bug precisa
  de ≥ 2 multiplicadores com `C_XX ≠ 0` para existir.
- **V-ETA / V-RES** (F-b) validam a consistência interna do sistema
  **já reduzido** — o bug está a montante deles. O sistema errado era
  internamente consistente.
- A normalização canônica divide por `√|λ₀|`; com λ₀ espúrio mas suave,
  produz ω₀/H ~ 7–12 estável — o "assentamento" do F-b era o artefato
  assentando.

## 3. Como foi verificado (4 etapas, scripts em `auditoria/code/`)

1. **r6_posto_K_reduzida** — espectro de K_red na máquina idêntica ao
   F-b: direção negativa = Ψ_f puro (|v₀·Ψ_f|² = 1.0000 em 40/40
   marcos, ambos os fundos); K7 bruto tem só o cruzado K[Ψ_f,E_f]
   grande. Métrica rho_K inconclusiva (ZONA CINZA declarada).
2. **r6b_degenerescencia_K** — o autovalor negativo é **estável** em
   dps = 15/30/60 e h = 1e-4→1e-6 (variação fator 1.0): NÃO é
   roundoff. Com o det=0 simbólico externo ⇒ as duas L2 diferem OU uma
   redução erra.
3. **r6c_confronto_L2** — confronto exato (racional, off-shell, por
   peças EH_g/EH_f/INT/CHI) das duas L2: **é a mesma ação** a menos de
   derivada total (ΔK = 0; S = ΔC simétrica; ΔW = −Ṡ — exatos nos 3
   pontos aleatórios). Com a MESMA rotina de redução: nossas matrizes
   dão det < 0, as deles det = 0 ⇒ o erro está na redução aplicada a
   matrizes com `C[mult,:] ≠ 0` (as nossas; as ADM têm `C[X,:] = 0` e
   são imunes).
4. **r6d_reducao_corrigida** — absorção corrigida (one-shot, S
   simétrica, Ċ contada uma vez por par): det₂/esc² despenca de
   ~1e-8 (estável, "modo") para **1e-33…1e-40 em dps=40** — zero
   numérico; λ₀ cai ~11 ordens; direção nula = Ψ_f. O nosso pipeline
   corrigido **reproduz independentemente** o resultado ADM externo.

## 4. Física resultante (benchmark β-constante, F′ = F″ = 0)

O benchmark é Hassan–Rosen puro + escalar espectador. Com a redução
correta:

- **2 DOFs escalares**: 1 escalar métrico (E_f-tipo) + δχ. Ψ_f é
  direção de vínculo (o vínculo secundário que remove o modo
  Boulware–Deser — exatamente a estrutura do teorema HR e do setor
  escalar FRW de Comelli–Crisostomi–Pilo, que os nossos 3 DOFs
  contradiziam).
- Cinéticas dos dois modos **positivas** nos dois fundos (K_E > 0;
  r < 1/√3 satisfeito: r = 0.332 e 0.516).
- **Não há fantasma no espectro linear escalar.** A cadeia
  "ω₀/H ≈ 7–12 → ω₀/Λ₃ → H-SC" perde o objeto.

## 5. Consequências (cascata)

| Conclusão anterior | Estado |
|---|---|
| Gate F-b: fantasma canônico, ω₀ ~ 3–4 Λ₃, "H-SC com número" | **CAI** (artefato do bug) |
| Gate F-a: BANDA-FISICA, expulsão dinâmica | **CAI** (mesma redução) |
| R-2: direção K<0 estrutural | **CAI** (K_red errada) |
| D-2/R-1/R-3*: dinâmica reduzida (3 DOFs) | **SUSPENSA** — reexecutar com redução corrigida |
| R-4a/b/c: banda métrica lnA ~ +4 | **SUSPENSA** — a reauditoria externa corrigida dá **decaimento** (~−13); reexecução própria pendente |
| R-5: excesso ISW 2–8× em baixo-ℓ (TENSAO) | **SUSPENSA** — perde a premissa (a banda) |
| Setor tensorial (m_T², D-5, pouso, background) | fica de pé (não usa a redução escalar) |
| Erratum-01 (Bianchi), Gate 1 (ação), lib simbólica | ficam de pé |
| Viabilidade observacional da F1 | **REABERTA** — melhor que antes (sem fantasma), mas C_ℓ sobre o sistema 2-DOF ainda não calculado |

**Nota:** a suspensão de R-4/R-5 não afirma o contrário das conclusões
antigas; afirma que os números vieram do sistema errado. A reauditoria
externa (r6d–r6h dela) já indica banda → decaimento e ISW sem suporte,
mas a reexecução no nosso pipeline (com V-XREP, abaixo) é o que
promove isso a resultado do repo.

## 6. Correção permanente

1. **Fix** (r6d, `reduz_ponto_novo`): absorção one-shot com S
   simétrica — nas entradas X–X, `W[i,j] += Ċ[i,j]` uma única vez por
   par; jamais reutilizar `Ċ` da C original para linhas já
   antissimetrizadas. Aplicar em toda reexecução da cascata.
2. **Novo gate obrigatório V-XREP** (validação cruzada de
   representação): toda redução numérica passa a ser executada nas
   duas formas IBP-inequivalentes — Γ–Γ (C_X ≠ 0, com absorção) e ADM
   (C_X = 0, Schur puro) — exigindo espectros de K_red idênticos. O
   bug era invisível a todos os gates de uma única representação.

   **Nota de nomenclatura (2026-08-12, pós-review):** a cascata R-7
   implementou sob o nome "V-XREP" um gate DISTINTO do definido
   acima: a comparação de dois canais independentes de Ċ (gradiente
   de grade vs `dt_background` simbólico) DENTRO da representação
   Γ–Γ. Fica renomeado: **V-XREP-a** = dois canais de Ċ (o dos R-7,
   pega erros de derivada/fundo — pegou a inconsistência Euler do
   pousado); **V-XREP-b** = Γ–Γ vs ADM como definido acima —
   executado no r6c/r6d (T1–T4: mesma ação provada exata; mesma
   redução sobre os dois conjuntos de matrizes) e coberto de forma
   independente pelo pacote ADM externo. Scripts futuros: V-XREP-a
   obrigatório por trilha; V-XREP-b obrigatório a cada mudança da
   maquinaria de redução (referência: r6c).

## 7. Crédito

A contagem 2-DOF, a L2 ADM de referência e a previsão de que a
direção canonizada era vínculo vêm da reauditoria externa (sessão
ChatGPT do autor, 12/08/2026). A demonstração de que as duas ações são
idênticas (fechando a lacuna "teorias diferentes"), a localização do
bug no código (mecanismo linha a linha) e a reprodução independente do
det = 0 no pipeline corrigido são deste repositório (r6c/r6d).
