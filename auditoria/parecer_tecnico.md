# Parecer Técnico sobre a TDCP — Síntese por Capítulo e Avaliação de Viabilidade

Data: 2026-08-06. Base: auditoria sequencial das 856 equações
(`registro/`, sumários em `lotes/lote_01…lote_11`) + as 8 derivações
(`derivations/`, âncoras D1–D8) + `integration_assessment.md`.

**O que este parecer é.** Uma síntese avaliativa, capítulo a capítulo,
do que se sustenta matematicamente, do que não se sustenta, e do que
fazer com cada bloco. Ao final, uma opinião sobre a viabilidade da
teoria.

**O que este parecer não é.** Um julgamento sobre a verdade física da
TDCP. A auditoria verifica se cada afirmação segue do que a precede —
não se o universo funciona assim. Onde digo "não se sustenta", leia
"não decorre do que o corpus estabelece", não "é falso".

**Legenda de ação:**
`VALIDAR` (aceitar como está) · `REVER` (correção pontual, estrutura
preservada) · `REESCREVER` (a seção precisa ser refeita sobre outra
base) · `INVALIDAR` (remover ou rebaixar a conjectura declarada) ·
`DECIDIR` (escolha editorial/física que só o autor pode fazer).

---

# Parte I — Corpo principal (Cap.1–26)

## Cap.1 — Bifurcação e vácuo dinâmico
**Sustenta-se:** a narrativa da bifurcação como instabilidade de modo
diferencial é coerente e bem colocada; a estrutura Φ₊/Φ₋ é legítima.
**Não se sustenta:** `H²=8πGρ/(3(1−η))` não é derivável da ação
(D4) — é extensão postulada. `T(x)=f(H₁−H₂)` tem f nunca especificada
e RHS independente de x em fundo homogêneo. `V(Φ±)` nunca é
especificado em lugar nenhum, o que deixa `m_−²<0` como hipótese, não
resultado. `η̇=Γ(H₁−H₂)²` conflita com a lei do Anexo E/H.
**Ação:** `REVER` (reclassificar H² como extensão, com o regime
adiabático declarado) + `DECIDIR` (qual é A lei de η).

## Cap.2 — Formalização do vácuo dinâmico
**Sustenta-se:** consistente com o Cap.1 no que reprisa.
**Não se sustenta:** herda H² (D4). Sobrecarga Φ (Cap.1) vs φ (Cap.2).
**Ação:** `REVER` junto com o Cap.1.

## Cap.3 — Estrutura bimétrica Hassan–Rosen
**Sustenta-se:** quase tudo. Ação HR, K=√(g⁻¹f), V=Σβₙeₙ, limite de RG,
Higuchi citado corretamente. É material importado e bem transcrito.
**Não se sustenta:** §3.4 escreve as equações de campo com prefator
`m²` sem normalização — `V^(g)_μν` nunca é definido e, com a definição
padrão, o prefator é `m²M_eff²/M_g²` (o Anexo A §A.1 traz a ação de
onde isso viria). Setor f ainda carrega √−g/√−f não declarado.
**Ação:** `REVER` (definir V^(g)_μν e corrigir a normalização).

## Cap.4 — Troca de energia entre setores
**Sustenta-se:** §4.4 estabelece corretamente ∇_f^μV^(f)_μν=0 e a
identidade que a acompanha.
**Não se sustenta:** as duas coisas juntas implicam **Q_ν≡0** — não há
troca. Isso contradiz a narrativa central do próprio capítulo (§4.3,
§4.6) e é justamente a conservação separada que o Cap.5 §5.5 precisa
para derivar a constraint de Bianchi. §4.7 soma tensores de métricas
diferentes sob ∇ não especificado, com um T^(f) de matéria que não
existe na teoria.
**Ação:** `REESCREVER` §§4.3–4.7 — a troca é nula on-shell; o vácuo
dinâmico age via potencial, não via transferência. Este é o achado A1,
e é um dos mais graves do corpus por ser uma contradição interna, não
um erro de conta.

## Cap.5 — Cosmologia de fundo bimétrica
**Sustenta-se:** o esqueleto todo. K diagonal no fundo FLRW, os cinco
e_n, as duas Friedmann (incl. ρ_int sem β₄ — D3), a constraint de
Bianchi. Verificado simbolicamente pelas derivações.
**Não se sustenta:** §5.5B — a equação do ramo dinâmico confere, mas a
legenda "aqui r(t) evolui dinamicamente" é falsa (ṙ≡0, D5). §5.7 tem
erro de sinal na fonte (+∂V_int/∂φ deveria ser −) e V_int não é
definida no capítulo.
**Ação:** `REVER` (sinal, legenda) — o capítulo é sólido no essencial.

## Cap.6 — Perturbações e contagem de modos
**Sustenta-se:** a contagem HR padrão importada (§6.1) está correta
como importação.
**Não se sustenta:** §6.2 (expansão técnica) tem ação tensorial com
gradientes dimensionalmente inconsistentes, cinético de ℓ sem 1/ξ e
massa com prefator errado; a diagonalização por rotação ortogonal é
mal-formulada (cinéticos desiguais exigem a base ponderada do Anexo D
§D.4). §6.5 reintroduz a troca de energia J^ν (mesma família do A1).
O capítulo tem duas numerações internas e muda o nome da base no meio.
**Ação:** `REESCREVER` §6.2 (forma correta na D2 §3.1) + `REVER` §6.5
+ `DECIDIR` a dupla numeração.

## Cap.6.2 — Versão expandida
**Sustenta-se:** a contagem de 3 modos (ζ,σ,δφ) do §6.4 é
**confirmada** pela D1 — este capítulo acerta o que o Anexo C erra.
**Não se sustenta:** §6.3 fixa gauge Newtoniano na ação, que perde as
constraints de B,E (armadilha diagnosticada na D1). §§6.6–6.8 usam
condições que as derivadas substituem.
**Ação:** `VALIDAR` a contagem; `REVER` as condições e a nota de gauge.

## Cap.7 — Observáveis lineares
**Sustenta-se:** as definições observacionais (μ, η_slip, G_eff) são
padrão e bem transcritas. §7.6 antecipa dois mediadores — qualitativamente
na direção certa (a estrutura real é multi-polo).
**Não se sustenta:** a fórmula de μ de 2 polos, e a prosa ao lado dela
que diz o oposto do que a fórmula diz (achado B1). A_σ, A_φ, Π₁, Π₂
nunca são definidos.
**Ação:** `REESCREVER` §7.6 sobre a forma multi-polo (D6).

## Cap.8 — Crescimento linear
**Sustenta-se:** praticamente tudo. Reconstruído, internamente
consistente, e honesto sobre os próprios limites. A cadeia
δ̈+2Hδ̇=4πGμρδ é passo QS legítimo.
**Ação:** `VALIDAR` (condicionado ao μ correto entrar no lugar).

## Cap.9 — Espectro e transferência
**Sustenta-se:** P(k), T(k), C_ℓ padrão e corretos.
**Não se sustenta:** reprisa a fórmula μ refutada.
**Ação:** `REVER` (substituir μ).

## Cap.10 — Modo σ e espectro primordial
**Sustenta-se:** σ_k∼k^(−3/2) confere **sob a hipótese** |m²|≪H²; a
D7 dá a forma geral k^(−ν) com ν=√(9/4+|m²|/H²) e uma **previsão nova**
que o corpus não tinha: n_σ−1≈−(2/3)|m_σ²|/H².
**Não se sustenta:** muda de tempo cósmico para conforme sem aviso;
ζ=δρ/(ρ+p) colide com o ζ do Cap.6.2/7/8; γ e τ~ln σ sem definição.
**Ação:** `REVER` + `VALIDAR` a previsão nova da D7 (é ganho líquido).

## Cap.11 — Setor tensorial primordial
**Sustenta-se:** decomposição P_T, r=P_T/P_ζ, limite observacional de
massa do gráviton — todos padrão.
**Não se sustenta:** `h_m∼e^{−m_T t}` — um modo pesado **oscila** com
envelope a^{−3/2}, não decai exponencialmente. `c_T=1` "não-negociável"
precisa de qualificação (c_f²=ξ²/r²; só vale exatamente se ξ=r).
**Sobrecarga grave:** r = razão tensor-escalar aqui vs r=b/a, a
variável estrutural central.
**Ação:** `REVER` (amortecimento, c_T) + `DECIDIR` (renomear um dos r).

## Cap.12 — Tempo relacional
**Não se sustenta:** a única equação do capítulo, t∼(1/ΔH)ln r, tem ΔH
não definido e é a **terceira** variante heurística de tempo relacional
do corpus (T=f(H₁−H₂) no Cap.1; τ~ln σ no Cap.10), nunca unificadas nem
derivadas.
**Ação:** `DECIDIR` — unificar em uma formulação e derivá-la, ou
rebaixar as três a metáfora declarada.

## Cap.13 — Ramo proporcional e isocurvatura
**Sustenta-se:** f=c²g, ρ_int com F(φ) na forma correta (D3), a
condição observacional P_S/P_ζ≪1, a adiabaticidade.
**Não se sustenta:** `S∝a^{−3/2}e^{−m_S t}` (mesmo erro do Cap.11).
𝓕 é mais uma variante do símbolo F.
**Ação:** `REVER`.

## Cap.14 — Fundo F1 completo
**Sustenta-se:** **é o capítulo mais rigoroso do corpus.** Ação HR
completa com S_m e S_φ explícitos; definições COM lapses (sana a
pendência do Cap.5); ρ_int nas formas corretas (acerta exatamente o que
o Anexo B §B.5 erra); r★=−β₁/(2β₂); β₁β₂<0; U(r★)=β₀−3β₁²/(4β₂)
verificada; o conjunto fechado de restrições confere. §14.11 deriva
ṙ=0 **corretamente**.
**Não se sustenta:** o cluster §§14.12–14.17 — em vez de aceitar ṙ=0,
o texto o contorna trocando silenciosamente a constraint por
(H_b−ξH_g)=0, que não é a de Bianchi (coincidem só se ξ=1). Onze
equações herdam o erro em cascata. §14.16-iii afirma H_f=H_g no ramo
proporcional, falso (com f=c²g, H_f=H_g/c).
**Ação:** `REESCREVER` o cluster (adotar ṙ≡0 e a via da raiz móvel,
D5 §4.1) + `VALIDAR` o resto, que é excelente.

## Cap.15 — Setor escalar e isocurvatura
**Não se sustenta:** o núcleo. `M_eff²(β₁+2β₂r)>0` como no-ghost e
`m_S²∼m²F(β₁+2β₂r)` (e todas as variantes e condições que herdam) são
**refutadas** pela D1: o espectro real tem par com cinética negativa
nos dois lados da raiz no ramo dinâmico, degenerescência **cinética**
(não de massa) na raiz, e massas O(1) sem relação com o fator. §15.10
("um único fator estrutural controla tudo") cai junto. Mais o erro de
amortecimento e^{−m_S t} e a terceira definição de ζ.
**Ação:** `REESCREVER` §§15.4–15.7 e `INVALIDAR` §15.10.

## Cap.16 — Setor tensorial F1
**Não se sustenta:** **é o capítulo mais refutado do corpus** (15 de 28
equações). Parte de uma ação tensorial errada (cinético do setor f sem
1/ξ e com r² em vez de r³; sem c_f²=ξ²/r² no gradiente) e propaga:
m_mix², o "fator estrutural", m_T² com prefator M_eff²/M_g² em vez de
M_eff²(1/M_g²+ξ/(M_f²r³)), Higuchi instanciado com a forma errada, e
`m_T²∼r·m_S²` — cuja refutação é dupla, porque **os dois lados** da
relação caíram (D1 e D2). A conclusão do §16.9 cai com eles.
**Sustenta-se:** as perturbações TT (§16.1) e os bounds como enunciados
importados.
**Ação:** `REESCREVER` §§16.2–16.9 sobre a D2 (forma fechada pronta) +
`INVALIDAR` §16.6.

## Cap.17 — Consistência UV e EFT
**Sustenta-se:** dois blocos autocontidos e **corretos**: §§17.1–17.2
(Λ_TDCP∼(m²M_eff)^{1/3}, H≪Λ) e §17.5 (naturalidade — a conta
δβₙ∼m^{2/3}/(16π²M_eff^{2/3}) foi verificada e confere). §17.4 (sem BD
ghost) é importação correta.
**Não se sustenta:** só §17.3, que herda m_T² do Cap.16 (7 equações).
A conclusão qualitativa ("Higuchi não expulsa a teoria do regime EFT")
provavelmente sobrevive à correção, mas a fórmula precisa ser refeita.
**Ação:** `REVER` §17.3; `VALIDAR` o resto.

## Cap.18 — μ(k,a), Σ e testes
**Não se sustenta:** **maior densidade de erro do corpus** (32 de 48).
Quase toda a segunda metade deriva consequências do ansatz Yukawa de 1
polo, que a D6 refuta: μ real é racional de grau 7/7 (~7 polos, com
pares complexos/positivos no ramo instável), **α_∞=0 exato**, e os
desvios vivem em escalas **intermediárias** — o oposto qualitativo do
que o capítulo assume. §18.5 apresenta μ→1 em k grande como exigindo
tuning (m_S grande OU α pequeno), quando é **automático**.
**Erro autocontido, independente de âncora:** a fórmula
Σ=(μ/2)(1+η_slip⁻¹) está errada — das próprias definições do capítulo
sai Σ=(μ/2)(1+η_slip). Repetida quatro vezes no corpus.
**Ação:** `REESCREVER` §§18.3–18.16 sobre a forma multi-polo +
`REVER` Σ (correção trivial).

## Cap.19 — Confronto observacional
**Sustenta-se:** a aritmética inteira. H₀/c≈3.3×10⁻⁴ h/Mpc e as
inversões (0.01/k_H0≈30, 0.1/k_H0≈300) conferem.
**Não se sustenta:** a conclusão. `m_S0∼(30–300)H₀` é **design
observacional** — inverte a posição desejada do joelho —, não
consequência da dinâmica (D8). E o joelho único que ela posiciona **não
existe** na estrutura real (D6). Benchmarks B1/B2 herdam.
**Ação:** `REESCREVER` — reclassificar como benchmark de projeto e
reconstruir sobre a forma multi-polo.

## Cap.20 — Screening de Vainshtein
**Sustenta-se:** quase tudo (29 de 34), e verifiquei numericamente a
cadeia inteira: r_S≈2954 m; r_V≈120,6 pc (m=H₀) e ≈5,6 pc (m=100H₀);
1 AU≈4,85×10⁻⁶ pc; critério PPN exige r_V≳0,0104 pc — **satisfeito com
margem de 2 a 3 ordens de grandeza**. O mecanismo é metodologicamente
padrão (Stückelberg, galileon cúbico, EOM por Euler–Lagrange).
**Não se sustenta:** [C20.28] erra ~2 ordens de grandeza no limite
inferior (10⁻¹⁰–10⁻¹², não 10⁻¹⁰–10⁻¹⁴) — sem consequência
qualitativa. Z(φ), c₃(φ), α_V são postulados por analogia dRGT, não
derivados dos β_n reais. **Sobrecarga:** ξ reaproveitado em
F(φ)=1+ξφ/M_Pl, colidindo com ξ=N_f/N_g.
**Ação:** `REVER` (número + renomear ξ); `VALIDAR` o mecanismo.

## Cap.21 — Solução estática e PPN
**Sustenta-se:** 28 de 31. Refiz a álgebra de γ(r)−1 passo a passo e
confere; o bound de Cassini é satisfeito com folga.
**Não se sustenta:** **Φ e Ψ trocam de papel** em relação ao Cap.18
(lá Ψ é o temporal, aqui é o espacial) — mesmos símbolos, convenção
invertida no mesmo corpus. c_Φ, c_Ψ nunca são calculados; m_φ (que
fecharia o argumento "sem quinta força via φ") também não.
**Ação:** `REVER` (unificar convenção); `VALIDAR` o resultado.

## Cap.22 — Estabilidade não-linear
**Sustenta-se:** 29 de 30. A matriz cinética do galileon, o laplaciano
radial e a decomposição da Hessiana foram verificados. **Ponto alto de
calibração científica:** o capítulo reconhece que c_r²≳1 é comum em
galileons cúbicos e **recusa** a inferência apressada "superluminal ⇒
inconsistente" sem hipóteses de UV completion — postura correta.
**Pendente:** as fórmulas Z_t/Z_r/Z_Ω (§22.5) não foram reproduzidas
pela minha rederivação manual; o texto ressalva "até fatores
convencionais de sinal". Script criado para decidir.
**Ação:** rodar `auditoria/code/lote05_C22_galileon_stability.py`; até
lá, `VALIDAR` sob ressalva.

## Cap.23 — Pipeline BAO+RSD+WL
**Sustenta-se:** o aparato padrão (distâncias BAO na forma de Eisenstein
et al., integral de Limber) está correto.
**Não se sustenta:** herda μ, η_slip e Σ (com o η_slip invertido pela
quarta vez). **Conflito interno novo:** propõe α₀∼0.1–1, intervalo cuja
maior parte **viola** o limite |α(a₀)|≲0.1 que o próprio Cap.18 fixou.
**Ação:** `REVER`.

## Cap.24 — Implementação em CLASS
**Sustenta-se:** tudo (5 de 5). Pontos de injeção corretos,
transformação de gauge síncrono↔newtoniano padrão, testes de sanidade
bem escolhidos.
**Ação:** `VALIDAR`.

## Cap.25 — CMB e Planck
**Sustenta-se:** tudo (3 de 3). A derivada
∂η(Φ+Ψ)=2[Σ∂ηΦ_GR+Φ_GR∂ηΣ] foi verificada por regra do produto e
confere. A identificação de um termo de ISW **específico da TDCP**
(vindo da evolução temporal de Σ) é uma consequência matemática
legítima.
**Ação:** `VALIDAR`.

## Cap.26 — Ajuste global
**Sustenta-se:** a estrutura de likelihood e a matriz de
degenerescências.
**Não se sustenta:** a linguagem de "joelho único" persiste; o critério
de falseabilidade é expresso em α₀, já refutado como função física.
**Ação:** `REVER` após a reconstrução dos Cap.18–19.

---

# Parte II — Anexos

## Anexo A — Formalismo HR
**O anexo mais limpo do corpus** (30/30). É a fonte canônica de ξ, r,
K e e_n que todo o corpo cita. Verifiquei os e_n(ξ,r,r,r) e as
identidades de Newton. [AA.02] traz a ação com prefator m²M_eff², que
resolve a pendência de normalização do Cap.3.
**Ação:** `VALIDAR`.

## Anexo B — Friedmann bimétricas e Bianchi
**Sustenta-se:** a redução minisuperespaço inteira (verificada termo a
termo), a Friedmann do setor f (§B.6 completo), e §B.9 — que contém a
derivação **correta** de ṙ≡0, fonte do resultado que a D5 confirmou.
**Não se sustenta:** §B.5 erra a regra da cadeia (trata V(ξ,r) como se
não dependesse de N_g via ξ=N_f/N_g) — e a **mesma regra é aplicada
corretamente duas seções depois**, em §B.6. Curiosidade reveladora: a
forma correta reaparece em §B.10, contradizendo §B.5 dentro do próprio
anexo. Isso indica deslize pontual, não crença física diferente.
**Ação:** `REVER` §B.5 (correção fechada na D3); `VALIDAR` o resto.

## Anexo C — Setor escalar
**Não se sustenta:** §C.3 conta 2 modos (real: 3, D1 — e o Cap.6.2
acerta); §C.9 identifica K₁₁↔Higuchi por analogia de campo único, que
não corresponde ao sistema acoplado real; §C.11 (F(χ) não reintroduz
BD ghost) fica sem suporte — o argumento pode valer para o BD ghost
especificamente, mas nada diz sobre o par fantasma que a D1 encontra.
**Sustenta-se:** todo o aparato genérico (ação quadrática, K positiva
definida, c_s² como autovalores de K⁻¹G).
**Ação:** `REVER` §C.3/§C.9; `INVALIDAR` a claim de §C.11 como
demonstrada (rebaixar a conjectura).

## Anexo D — Setor tensorial
**Sustenta-se:** §D.3/§D.4 são **confirmados pela D2** — a ação
tensorial correta e a base de diagonalização ponderada (com r^{3/2}),
que é exatamente o que o Cap.16 deveria ter usado.
**Não se sustenta:** §D.5 (m_T²∝B(r)(1+r)/r, sem ξ) — único erro real
do anexo, com forma fechada pronta na D2.
**Ação:** `VALIDAR` §D.3/§D.4 (e promovê-los sobre o Cap.16);
`REVER` §D.5.

## Anexo E — Sistema dinâmico
**Sustenta-se:** a conversão inteira para variáveis adimensionais e
N=ln a, verificada passo a passo; o fechamento algébrico de ξ(N);
§E.9, que reconhece ṙ≡0 **honestamente** e propõe r constante — na
direção que a D5 recomenda.
**Não se sustenta:** o erro de sinal da equação de χ está aqui, na
origem (§E.3(3)), e se propaga por 6 equações. [AE.27] tem um fator
M_g extra (que não se propaga — a equação seguinte já usa o valor
certo). §E.3(6) declara o ramo dinâmico "escolha TDCP principal" — o
ramo que D1 e D5 mostram ser duplamente inviável. §E.7 traz a equação
não-derivável (D4).
**Ação:** `REVER` (sinal, fator) + `DECIDIR` (o ramo).

## Anexo F — Espaço de parâmetros
**Sustenta-se:** a estrutura de restrições cruzadas é conceitualmente
boa e o insight final ("teorias boas são restritas") é correto.
**Não se sustenta:** μ_T² perde ξ do próprio argumento; §F.3.3 mistura
um achado real (degenerescência em B(r)=0, benchmark C da D1) com uma
generalização que a D1 refuta; §F.6.3 invoca GW170817 sem a
qualificação sobre c_f².
**Ação:** `REVER`.

## Anexo G — Fundamentos filosóficos
**Sustenta-se:** internamente honesto sobre os próprios limites (§G.13
declara que a teoria não quantiza nem explica a origem da bifurcação).
**Não se sustenta:** a interpretação de §G.9 herda a equação
não-derivável; §G.5 herda a lei de η conflitante.
**Ação:** `REVER` após as decisões estruturais.

## Anexo H — Formalização canônica
**Aqui está o problema mais visível do corpus.** O anexo que se propõe
como "núcleo lógico" e "versão axiomática consolidada" contém:
**Postulado 4** com o sinal errado da equação de χ; **Postulado 5**
com a lei de η que conflita com o Cap.1/2; e §H.6 — a "Forma Compacta
Final da Teoria", a equação que resume a TDCP em uma linha — é
exatamente a que a D4 mostra não ser derivável da ação.
**Sustenta-se:** os Postulados 1, 2, 3 e 6 não têm problema; as
Friedmann consolidadas usam as formas já corrigidas.
**Ação:** `REVER` (sinal) + `DECIDIR` (η) + `REESCREVER` §H.6 como
extensão declarada. **Enquanto isso não for feito, a formalização
canônica não está fechada.**

## Anexos I, J, K — Linha exploratória
**Não se sustenta como física integrável:** o colapso |Ψ⟩=α|g₁⟩+β|g₂⟩
não tem ponte com a ação clássica; L_int=λχ(g⁽¹⁾−g⁽²⁾)² não especifica
a contração de Fierz–Pauli e, na leitura literal, **reintroduz o ghost
de Boulware–Deser**; Λ_ent é aditivo e sem equação de movimento (o η é
multiplicativo e tem). Energia própria em ambos os domínios conflita
com a exigência de matéria só em g. Previsões numéricas (|w+1|∼10⁻²⁻³,
Δγ∼0.01) sem cálculo mostrado. Mais duas sobrecargas graves: ξ e η
reutilizados com significados novos.
**Sustenta-se:** a formalização quântica em si (von Neumann, notação de
estado) é correta; a intuição física é legítima.
**Ação:** `INVALIDAR` como parte do corpo F1 (já está fora, e
corretamente).

## Anexo L — Ponte conceitual
Zero equações. **É o documento mais bem calibrado do corpus** em
controle de claims: diz exatamente o que pode ser absorvido (glosa
narrativa) e o que não pode, sem inventar equivalência.
**Ação:** `VALIDAR`.

---

# Parte III — Os quatro problemas transversais

Acima dos erros individuais, quatro questões atravessam o corpus e
**não são corrigíveis por patch** — exigem decisão:

**1. O ramo dinâmico está duplamente morto.** Declarado "escolha TDCP
principal" (Anexo E §E.3(6)) e canonizado no Anexo H, ele: (a) tem
ṙ≡0 exatamente (D5) — não produz a evolução de r que a narrativa
precisa; e (b) tem par escalar fantasma/taquiônico em todos os
benchmarks (D1). A via consistente identificada é o **ramo algébrico
com raiz móvel r★(φ(t)) via β_n(φ)** (D5 §4.1) — que exige hipótese
adicional e leva o par relativo à degenerescência na raiz exata (D1,
benchmark C). O corpo precisa escolher e enfrentar uma das duas.

**2. η é postulado, não derivado — e tem duas leis.** `η̇=Γ(H₁−H₂)²`
(Cap.1/2) vs `η̇=Γχ̇²` (Anexo E/H, Postulado 5), com dimensões de Γ
incompatíveis e nenhuma das duas jamais declarando essa dimensão. E a
equação que o usa, H²=8πGρ/(3(1−η)), não decorre da ação (D4).

**3. A assinatura observacional prometida não existe na forma
descrita.** O "joelho Yukawa" em fσ₈(k) pressupõe μ de 1 polo. O μ real
é multi-polo com α_∞=0. Toda a cadeia Cap.18→19→23→26 foi construída
sobre a parametrização refutada.

**4. O "fator estrutural único" β₁+2β₂r caiu dos dois lados.** Era a
claim de elegância da família F1 — um fator controlando estabilidade,
massa escalar e massa tensorial. No tensor o fator real é β₁+β₂(ξ+r)
(D2); no escalar, a saúde não é decidida por ele (D1).

---

# Parte IV — Opinião geral sobre a viabilidade

Vou separar o que a auditoria autoriza dizer do que é juízo meu.

## O que está estabelecido

A TDCP **não é uma teoria arbitrária mal construída**. Ela se apoia em
Hassan–Rosen — um framework bimétrico real, livre de ghost, bem
estudado na literatura — e o transcreve corretamente. O Anexo A, o
Anexo B (fora de §B.5), o Cap.14, o bloco solar (Cap.20–22) e o
pipeline observacional padrão (Cap.23–25) são trabalho técnico
competente. Verifiquei numericamente que o screening de Vainshtein
funciona e bate o bound de Cassini com 2–3 ordens de margem — esse é
um teste que muitas teorias de gravidade modificada não passam.

O que caiu não foi o alicerce. Foram **as quatro claims que faziam a
TDCP ser TDCP** em vez de gravidade bimétrica padrão: o ramo dinâmico,
o η que emerge da geometria, o joelho observacional e o fator
estrutural único.

## Isso é um beco sem saída?

**Não — mas o caminho adiante é reconstrução, não correção.** Três
razões concretas para não ser beco sem saída:

**Primeira: as derivações não só destruíram, elas substituíram.** A D6
não deixou um buraco onde estava μ; deixou uma estrutura multi-polo
derivada, com α_∞=0 exato. E isso é, em alguns aspectos, **melhor** do
que a teoria pedia: a recuperação de GR em pequenas escalas passa a ser
automática, sem tuning de massa — o Cap.14 §14.6 exigia isso como
requisito de projeto e a teoria real já o satisfaz de graça. Mais: a
assinatura derivada (μ≠1 com Σ≈1) é mais incomum e mais discriminante
do que um joelho Yukawa genérico, que dezenas de modelos produzem. A D7
entregou uma previsão que o corpus não tinha: n_σ−1≈−(2/3)|m_σ²|/H².

**Segunda: existe uma via consistente identificada.** A D5 §4.1 aponta
o ramo algébrico com raiz móvel β_n(φ) — que preserva a intuição
física central (separação estrutural evoluindo no tempo cósmico) sem as
patologias do ramo dinâmico. Não é um remendo; é uma reformulação com
endereço.

**Terceira: a teoria é testável.** Aqui quero corrigir uma premissa da
sua pergunta. Você perguntou se vale prosseguir "mesmo chegando a um
ponto onde não haja teste que possamos fazer". A auditoria não aponta
para essa direção. O problema **não é falta de testabilidade** — é que
os testes propostos foram construídos sobre uma parametrização
refutada. A estrutura real derivada é testável, e com assinaturas mais
nítidas. O que falta não é observável: é a cadeia derivacional que liga
a ação à assinatura.

## Onde está o risco real

Sendo honesto sobre o lado desfavorável:

A D8 rodou um scan de fundo e **não encontrou região viável**: com o
m_T² real (dependente de ξ), Higuchi falha em 60/60 pontos da grade.
Isso não é prova de impossibilidade — é uma grade, com escolhas
específicas de F(χ) e U(χ), que o corpus não fixa. Mas é um sinal ruim
e é o resultado mais preocupante de toda a auditoria. Se a
reconstrução no ramo algébrico também não achar região viável, aí sim a
questão muda de natureza.

E há um custo conceitual que precisa ser encarado: hoje, a narrativa
central da teoria — separação estrutural acumulada causando a
aceleração — **não tem mecanismo derivado**. η é postulado, r não
evolui no ramo escolhido. A história e a matemática se descolaram. Não
é fatal, mas é o que precisa ser reatado, e reatar isso é trabalho de
física nova, não de revisão.

## Recomendação

Prosseguir, com escopo redefinido e em três frentes, nesta ordem:

**1. O passe de correção do que já está fechado.** Os 115 erros têm
correção pronta. Corrigir as três raízes (D2, D6, D5) derruba a maior
parte. Isso é trabalho mecânico e deixa o corpus honesto — o que já
tem valor por si, independentemente do futuro da teoria.

**2. As decisões estruturais.** Qual lei de η. Qual ramo. Se
H²∝1/(1−η) fica como extensão declarada (o que é perfeitamente
publicável — "gravidade bimétrica com variável estrutural adicional")
ou se você tenta derivá-la de um acoplamento Ω(η)R_g, como a D4
sugere. Essas decisões mudam o que as correções devem dizer, então
tomá-las antes economiza retrabalho.

**3. A reconstrução propriamente dita.** Ramo algébrico com raiz móvel;
pipeline observacional sobre a forma multi-polo; novo scan de
viabilidade. Aí sim, física nova e código novo.

Se em (3) o scan continuar sem região viável, a resposta honesta será
diferente — mas não se chega lá sem passar por (1) e (2). No estado
atual, o veredito é: **a teoria não está morta, está inacabada — e a
parte inacabada é justamente a que a torna distinta.** O que existe
hoje é um framework sólido mais um conjunto de extensões postuladas que
ainda não decorrem dele. Isso é um ponto de partida legítimo para
trabalho sério; não é ainda uma teoria fechada.
