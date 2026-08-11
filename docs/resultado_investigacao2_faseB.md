# Investigação 2 — Fase B: Perturbações no Fundo de Rolagem — Resultado

**Data:** 2026-08-11. Script: `auditoria/code/investigacao2_faseB_pert.py`
(saída em `auditoria/code/out/investigacao2_faseB_pert.txt`). Conclui a
Investigação 2 — o teste direto de R2 e a última saída interna do
no-go (`veredito_setor_escalar_final.md` §3, item 5). Companheiro de
`resultado_investigacao2_faseA.md`.

---

## 1. Validações (todas passaram)

GR selfcheck ✓ · fundo reintegrado confere com a Fase A (r_fim=0.4979,
χ/v=0.932) ✓ · V2/T1-estendido: fatias com taxas livres reconstroem a
matriz direta num ponto rolante a **0.00e+00** ✓ · V3: espectro
taxas-vs-congelado no pré-rolagem difere <5% com mesma contagem ✓.
Primeira vez no programa em que o QEP roda com todos os símbolos de
taxa vivos (Ḣ, Ḣ_f, ξ̇, χ̇, χ̈).

## 2. Veredito

### G2b-CONTAGEM — sem fantasma BD na rota numérica
**3 pares finitos em todos os 18 pontos × 2 k.** Compatível com a
remoção do modo BD no regime não-fatorado; **não certifica** (a
assimetria do `gate2_ghost.md` §4 continua: o QEP congelado é cego à
remoção por constraint dependente do tempo — só a contagem 4
falsificaria, e ela não ocorreu).

### G2b-SAUDE — o no-go se ESTENDE ao regime não-fatorado
| trecho | max σ/H (k=1) | kN_min (k=1) |
|---|---|---|
| pré-rolagem (a=100) | 3.18 | −2.6e-5 |
| janela não-fatorada (a≈760–2050) | **13.08** (a≈1800) | −1.5e-3 |
| pós-pouso (a≈1e5, estacionário) | 4.25 | −6.2e-3 |

**Nenhum ponto limpo em lugar nenhum da trajetória** (k=1 e k=10). E o
achado central: **σ/H acompanha o deslocamento** — cresce
monotonicamente com \|H−rH_f\|/H, pica junto com ele e relaxa junto. O
regime não-fatorado não é um refúgio da doença: é a parte mais íngreme
dela. Amplificação estimada só na janela (ΔN≈1.0, σ/H médio ~8):
**ln A ~ 8** — catastrófico para teoria linear se o modo acopla.

**Âncora de continuidade (pós-hoc, consistente):** o ponto pousado
(fundo estacionário modulado com β₁eff≈4.47, g_eff=χ*/v*≈1.86) dá
σ/H≈4.25 — dentro da família 3.85–4.43 do scan estacionário de
`modulacao_qep.py`. As duas rotas se encontram onde deviam.

### G2b-BALANCO — a doença sobrevive a todo o espectro do balanço
O rI do taquião estrutural (k=1) varreu **0.07 → 0.66** ao longo da
rolagem (contra ~0.5 do cancelamento estacionário da C1) — o p_φ≠0
deformou o balanço quebra×EH como previsto. **E a doença persistiu em
todos os valores.** A rota "curar movendo o balanço" fica fechada
empiricamente nesta trajetória: não há ilha saudável na dimensão do
balanço explorada.

## 3. R1 no regime dinâmico — a separação mais limpa do programa

Com F′≠0 **e** χ̇≠0 (acoplamento genuíno de δφ₋, pela primeira vez),
os modos patológicos estruturais mantêm \|⟨v,δφ₋⟩\|² ≈ 0.000–0.004 em
toda a trajetória. A única exceção é instrutiva:

- Em a=100–1200 existe um taquião **δφ₋-dominado** (dchi 0.52→0.09)
  com w² ≈ −13.7 → −3.7 — é **a própria instabilidade de
  condensação** (w² ≈ m²_eff da origem, −13.7, calculado na Fase A).
- Esse modo **sara sozinho**: em a≈1500 cruza para w²=+7.7 (limpo) e
  no assentamento vira a oscilação estável de χ (w²≈+25 ≈ m²_χ,eff no
  mínimo).

**Duas instabilidades, destinos opostos:** a da bifurcação (δφ₋,
física, transiente, auto-curável ao condensar) e a do setor de
vínculos (métrica-relativa, δφ₋-espectadora, eterna). R1 sai do teste
dinâmico mais forte do que entrou — a identidade π_L/π⁰ dos modos
doentes também se mantém (taquião k=1 majoritariamente π_L; k=10 π⁰,
como na C1).

## 4. Caveats e fronteira (declarados)

1. **Leitura congelada ponto a ponto** (d/dt C_sym desprezado; taxas
   só nos coeficientes). No fundo da janela \|Ḣ/H²\| chega a ~1 —
   estresse máximo da aproximação. O veredito sobrevive porque não é
   marginal (σ/H 5–13 numa tendência monótona e correlacionada com o
   fundo) e porque o **endpoint pousado** — onde \|Ḣ/H²\|=0.003 e a
   leitura congelada é quase exata — é doente por si (σ/H 4.25, e
   coincide com a família estacionária conhecida).
2. Pontos a≈2050–3500 (virada da oscilação): adiab 2.4–4.9;
   classificações ali são as menos confiáveis (lidas apenas como parte
   da tendência).
3. **Fronteira: UMA trajetória (g=2, m_χ²=30, v*=1), UMA célula
   (REF μ=1), k∈{1,10}.** Não varrido: outras células/knobs, k
   intermediários, e as saídas restantes do veredito (modulação de
   β₂/β₄; β₃≠0/F2) — que seguem com os priors baixos já declarados.

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| 3 pares em toda a trajetória (sem BD na rota numérica) | 2b (não certificador — assimetria declarada) |
| No-go estendido ao regime não-fatorado (σ/H 5–13 na janela, sem ponto limpo) | 2b (fronteira do §4) |
| σ/H correlacionado com o deslocamento dos ramos | 2b (uma trajetória) |
| Modos estruturais δφ₋-espectadores também no regime dinâmico | 2b |
| Instabilidade de condensação = modo δφ₋ que sara ao assentar | 2b |
| Balanço rI varrido 0.07–0.66 sem ilha saudável | 2b |
| "O regime não-fatorado é a parte mais íngreme da mesma doença" | leitura da tendência (2b), não teorema |

## 6. Consequência para o programa

**A Investigação 2 está concluída, negativa.** Com ela:

1. **As duas saídas estruturais do veredito estão fechadas** (item 3.4,
   ramo algébrico — Investigação 1; item 3.5, p_φ≠0 — aqui). Restam as
   saídas de prior baixo (β₂/β₄; F2) e a mudança de classe (matéria
   não-mínima), nenhuma delas tocando o mecanismo agora medido três
   vezes (setor de vínculos; balanço; regime dinâmico).
2. **R2 perde a última sonda interna à F1.** Pela lógica pré-declarada
   do `gate1c_nota_trilema.md`: o braço (b) do trilema só continua
   **fora** da representação F1 — (b1) com simetrias não-geométricas
   (critério anti-circularidade) ou (c). Qualquer teste futuro de R2 é
   construção nova, não sondagem da F1.
3. **A ironia final do arco, registrada com o rótulo de interpretação
   (nível 3):** a Fase A mostrou que a condensação de φ₋ *realiza* a
   narrativa da bifurcação no fundo (r×16); a Fase B mostrou que esse
   é exatamente o regime de pior saúde escalar do programa inteiro. A
   F1 não falha em produzir a bifurcação — falha em *sobreviver* a
   ela.
4. **O arco computacional da reconstrução v2 está completo.** Fundo ✓,
   tensor ✓, escalar ✗ em todos os regimes acessíveis (constante,
   modulado-estacionário, algébrico, dinâmico não-fatorado). Tudo o
   que resta é escrita (v2 enxuta — este resultado entra nos caps.
   07–09) e as decisões 2–3 do autor.
