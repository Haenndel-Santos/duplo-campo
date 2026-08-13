# Glossário de Termos, Siglas e Conceitos — TDCP

Manual introdutório. Complementa `dicionario_simbolos.md` (que é
normativo, para quem escreve) — este é descritivo, para quem lê.

---

## 1. A teoria e seus objetos centrais

**TDCP — Teoria do Duplo Campo Primordial.** A hipótese do projeto:
o universo primordial contém dois campos escalares fundamentais
correlacionados (φ₁, φ₂) cuja dinâmica diferencial produziria uma
"bifurcação" — a separação do universo em dois setores geométricos.

**F1.** A primeira implementação matemática da TDCP, construída sobre
gravidade bimétrica de Hassan–Rosen. "F1" nomeia a versão com β₃ = 0 e
matéria acoplada só à métrica g. Uma "F2" seria outra implementação
(por exemplo, com β₃ ≠ 0).

**Gravidade bimétrica.** Teoria com **duas** métricas dinâmicas em vez
de uma. Cada métrica define suas próprias distâncias, tempos e cones de
luz; um termo de interação as acopla.

**g_μν (métrica g).** A métrica do setor visível. Toda a matéria comum
(e a luz) acopla só a ela — por isso é a métrica que define o que
observamos.

**f_μν (métrica f).** A segunda métrica, do "setor estrutural". Não
acopla diretamente à matéria; interage com g apenas pelo potencial.

**Hassan–Rosen (HR).** A formulação de gravidade bimétrica que é livre
do fantasma de Boulware–Deser. A F1 é construída sobre ela. O termo de
interação tem forma muito específica — não é arbitrário: é justamente
essa forma que garante a ausência do fantasma.

**𝒦 = √(g⁻¹f).** A "raiz quadrada matricial" das duas métricas. É o
objeto que aparece no potencial de HR. (Cuidado: é diferente da matriz
cinética `K`, que é outra coisa — ver §4.)

**β_n (coeficientes beta).** Os cinco números (β₀…β₄) que pesam os
termos do potencial de interação entre g e f. São os parâmetros livres
da teoria bimétrica. Na TDCP, β₁ depende do campo φ₋ — é essa
dependência que dá o nome "modulação".

**φ₊ e φ₋ (modos comum e diferencial).** As combinações
φ± = (φ₁±φ₂)/√2 do par primordial. **φ₋ é o modo diferencial** — o que
mede a diferença entre os dois campos, e o que a teoria identifica com
o "grau relacional primordial" que modula os β_n. Essa identificação é
**normativa** (uma decisão), não derivada.

**Modulação.** O fato de β₁ ser função de φ₋: β₁(φ₋) = β₁⁽⁰⁾(1+φ₋²/v★²).
É o mecanismo pelo qual a dinâmica dos campos primordiais mexeria na
estrutura geométrica.

---

## 2. Fundo cosmológico (a expansão média do universo)

**Fundo (background).** A descrição do universo como perfeitamente
homogêneo e isotrópico — sem estruturas. É a "média" sobre a qual as
perturbações se propagam.

**FLRW.** Friedmann–Lemaître–Robertson–Walker: a métrica-padrão do
universo homogêneo em expansão.

**a (fator de escala).** Mede o "tamanho" do universo. Cresce com o
tempo; a = 1 costuma marcar o presente (neste projeto, o "hoje" varia
com a família de fundo e é sempre declarado).

**z (redshift).** Medida de época equivalente ao fator de escala:
1 + z = a₀/a. z = 0 é hoje; z alto é passado remoto (z ≈ 1100 é a
recombinação).

**H (parâmetro de Hubble).** A taxa de expansão. H₀ é o valor de hoje.

**N (número de e-folds).** Tempo medido em ln(a). "Um e-fold" = o
universo expandiu por um fator e ≈ 2.7.

**r = b/a (razão de fatores de escala).** A variável central da TDCP:
o quociente entre o fator de escala da métrica f e o da métrica g. Mede
a **separação estrutural** entre os dois setores. Se r é constante, os
dois setores expandem juntos; se evolui, eles se separam.

**ξ = N_f/N_g (razão de lapsos).** O quociente entre os "lapsos" (as
taxas de passagem do tempo) das duas métricas. Se ξ < 0, o tempo do
setor f corre "para trás" — patológico.

**Lapso (N).** A função que relaciona o tempo coordenado com o tempo
próprio; em gravidade, é um multiplicador de Lagrange, não um grau
dinâmico.

**Ramo finito / ramo infinito.** As duas famílias de solução da equação
que fixa r. No **ramo finito**, r → 0 no universo primordial e cresce
até um valor fixo; é o ramo que a TDCP usa. No **ramo infinito**,
r → ∞ no primordial. A literatura bimétrica discute qual dos dois é
viável.

**Ramo algébrico / ramo cinemático.** Os dois modos de satisfazer a
constraint de Bianchi: ou ℬ(r) = 0 (algébrico, r fica travado num
valor), ou N_f ȧ = N_g ḃ (cinemático, r evolui).

**Ponto fixo tardio.** O valor para o qual r converge quando a
densidade de matéria dilui a zero — o estado assintótico do universo.

**Aceleração / energia escura.** A expansão acelerada observada hoje.
Em bimétrica, ela pode surgir do próprio potencial de interação, sem
constante cosmológica — é a "auto-aceleração".

**w (parâmetro da equação de estado).** Razão pressão/densidade de um
fluido: w = 0 para matéria, 1/3 para radiação, −1 para constante
cosmológica. Define a era cosmológica.

**Ω_m.** Fração da densidade total do universo que está em matéria
hoje (≈ 0.3 nas observações).

**BBN — Big Bang Nucleosynthesis.** A formação dos núcleos leves nos
primeiros minutos. Vínculo forte sobre a expansão em z muito alto.

**z_eq (igualdade matéria–radiação).** A época em que as densidades de
matéria e radiação se igualam (z ≈ 3400).

**Recombinação.** z ≈ 1100, quando o universo esfria o bastante para
os elétrons se ligarem aos núcleos e a luz viajar livre. É de lá que
vem o CMB.

---

## 3. Perturbações (as estruturas sobre o fundo)

**Perturbação linear.** A aproximação em que os desvios da homogeneidade
são pequenos (δ ≪ 1) e as equações podem ser tratadas como lineares.
Vale enquanto as estruturas não colapsam.

**Regime não-linear.** Quando δ ~ 1 ou maior — galáxias, halos. As
equações lineares deixam de valer.

**k (número de onda) e k/aH.** k rotula a escala espacial de uma
perturbação (k grande = escala pequena). A razão **k/aH** (no projeto,
`kh`) compara a escala com o horizonte: kh ≫ 1 é sub-horizonte,
kh ≪ 1 é super-horizonte. É adimensional e depende da época.

**Horizonte.** A distância que a luz percorreu desde o Big Bang;
modos maiores que ele não "sentem" a causalidade local.

**Setor escalar / tensorial / vetorial.** As perturbações se separam em
três classes independentes no fundo homogêneo. Escalares fazem
estrutura e potenciais gravitacionais; tensoriais são ondas
gravitacionais.

**TT (transverso-sem-traço).** A polarização das perturbações
tensoriais — as ondas gravitacionais propriamente ditas.

**Ψ e Φ (potenciais de Bardeen).** Os dois potenciais gravitacionais
das perturbações escalares: Ψ é o **temporal** (governa o movimento da
matéria) e Φ o **espacial** (curvatura). Em GR sem tensão anisotrópica,
Φ = Ψ.

**η_slip (slip).** A razão Φ/Ψ. Vale 1 em GR; desvios indicam gravidade
modificada.

**ζ (perturbação de curvatura comóvel).** A quantidade conservada em
grandes escalas — a "semente" que liga inflação às estruturas.

**Modo adiabático / isocurvatura.** No adiabático, todas as espécies
flutuam juntas (é o que a inflação simples prevê e os dados favorecem).
No **isocurvatura**, há flutuação relativa entre espécies — teorias com
dois campos primordiais tendem a produzi-lo, e os dados o limitam
fortemente.

**Espectador (spectator).** Um campo que existe e flutua, mas não
domina a energia do universo nem afeta a expansão — "assiste".

**Condições iniciais (ICs).** Os valores de partida das perturbações.
"Adiabáticas" e "WKB-casadas" são escolhas fisicamente motivadas;
condições arbitrárias produzem transientes espúrios.

**δχ / δφ₋.** A perturbação do campo escalar modulador. No sistema
corrigido do projeto, é o modo saudável e "espectador".

**Modo métrico escalar.** O grau de liberdade escalar que vem das
métricas (não dos campos) — no sistema 2-DOF da F1, é o modo associado
a E_f.

---

## 4. Estabilidade: os quatro modos de uma teoria ser doente

**Grau de liberdade (DOF).** Um modo que se propaga de fato — que tem
dinâmica própria e condições iniciais independentes.

**Vínculo (constraint).** Uma relação entre variáveis que reduz o
número de graus de liberdade. Variáveis vinculadas não são dinâmicas:
seus valores são determinados pelas outras.

**Multiplicador de Lagrange.** Variável que aparece na ação sem
derivada temporal; sua equação de movimento é um vínculo, não uma
evolução (os lapsos e shifts são assim).

**Matriz cinética K.** Os coeficientes dos termos com derivada
temporal ao quadrado. Seus sinais dizem se os modos têm energia
cinética positiva.

**Fantasma (ghost).** Modo com energia cinética **negativa** (K < 0).
Instabilidade catastrófica: o vácuo decai criando pares de partículas
de energia positiva e negativa indefinidamente.

**Fantasma de Boulware–Deser (BD).** O fantasma específico que aparece
em gravidade massiva/bimétrica genérica — um sexto grau de liberdade
indesejado. A estrutura de Hassan–Rosen existe precisamente para
removê-lo, via um par de vínculos.

**Táquion.** Modo com massa ao quadrado negativa (m² < 0). Cresce
exponencialmente, mas a taxa é limitada (~ |m|) e não depende da
escala — é uma instabilidade "branda" comparada à de gradiente.

**Instabilidade de gradiente.** Quando c_s² < 0: a taxa de crescimento
é |c_s|·k/a, ou seja, **cresce com k** — escalas pequenas explodem
arbitrariamente rápido. É a instabilidade mais violenta das quatro, e é
a que o projeto encontrou na F1 em alto redshift.

**c_s² (velocidade do som ao quadrado).** O coeficiente do termo k² na
frequência do modo. c_s² = 1 significa propagação à velocidade da luz;
c_s² < 0 é instabilidade de gradiente; c_s² > 1 é superluminalidade.

**Vínculo de Higuchi.** Uma cota inferior sobre a massa do gráviton em
espaço-tempo curvo (m² ≥ 2H²); abaixo dela, o modo helicidade-0 vira
fantasma.

**ω² (frequência efetiva ao quadrado).** O termo de "mola" da equação
de movimento. ω² > 0 = oscilação; ω² < 0 = crescimento exponencial.

**Formalismo de Faddeev–Jackiw / redução de vínculos.** Métodos para
eliminar as variáveis vinculadas e ficar só com os graus de liberdade
físicos. É a operação onde o projeto teve o erro do Erratum-02.

**Complemento de Schur.** A operação algébrica que executa essa
eliminação: resolve as variáveis auxiliares e as substitui de volta.

**Primeira / segunda classe.** Classificação dos vínculos: os de
primeira classe geram simetrias de gauge; os de segunda classe reduzem
graus de liberdade em pares.

**Matriz de Dirac.** A matriz de brackets entre vínculos de segunda
classe; se degenera, a contagem de graus de liberdade muda.

---

## 5. Massa do gráviton, escalas e screening

**Gráviton.** O quantum do campo gravitacional. Em GR não tem massa (2
polarizações); em bimétrica há um gráviton sem massa e um **massivo**
(5 polarizações).

**m_T (massa tensorial).** A massa do gráviton massivo neste projeto.
Resultado: m_T ≈ 2.3 H₀ — comparável à escala de Hubble, ou seja,
comprimento de onda Compton da ordem do raio do universo observável.

**Comprimento de Compton (λ_C = 1/m).** A escala além da qual uma
força mediada por partícula massiva é suprimida exponencialmente. Com
m ~ H₀, é ~ Gpc.

**Modo helicidade-0 (π).** A polarização escalar extra do gráviton
massivo. É a que costuma causar problemas (fantasmas, forte
acoplamento) e a que o mecanismo de Vainshtein precisa esconder.

**Stückelberg.** Truque técnico de reintroduzir simetria de gauge
adicionando campos auxiliares, que torna visíveis os modos de
helicidade escondidos na massa.

**Goldstone.** Modo que aparece quando uma simetria é quebrada
espontaneamente; no limite de altas energias, o helicidade-0 se
comporta como um Goldstone.

**Vainshtein (screening).** Mecanismo pelo qual a força extra do modo
escalar é **suprimida** perto de fontes densas, por causa de
não-linearidades — é o que permite a teorias modificadas passarem nos
testes do sistema solar.

**r_V (raio de Vainshtein).** O raio dentro do qual o screening opera.
Fora dele, a força extra aparece.

**Λ₃ (escala de forte acoplamento).** A energia acima da qual a teoria
efetiva perde validade e as interações não-lineares dominam.

**EFT (teoria efetiva de campos).** Descrição válida abaixo de um corte
de energia; não pretende valer em todas as escalas.

**Limite de desacoplamento.** Aproximação em que se isola o modo
helicidade-0 dos demais, simplificando a análise de não-linearidades.

**PPN (parametrized post-Newtonian) e γ_PPN.** Formalismo padrão para
testar gravidade no sistema solar; γ_PPN é a mesma razão Φ/Ψ do
η_slip, medida no regime local. **Cassini** é o experimento que a
limita a ~2×10⁻⁵.

---

## 6. Observáveis e experimentos

**CMB (Cosmic Microwave Background).** A radiação de fundo emitida na
recombinação — a "foto" mais antiga do universo.

**C_ℓ.** O espectro de potência angular do CMB: quanta flutuação existe
em cada escala angular ℓ. ℓ baixo = escalas grandes no céu.
**TT, TE, EE** são as combinações de temperatura (T) e polarização (E).

**Modos B.** A componente de polarização do CMB que ondas
gravitacionais primordiais produziriam; alvo de experimentos futuros.

**r_T (razão tensor-escalar).** Quanta onda gravitacional primordial há
em relação às perturbações de densidade — o alvo dos modos B.

**ISW (Integrated Sachs–Wolfe).** Efeito no CMB causado por potenciais
gravitacionais que **variam** enquanto o fóton os atravessa. Sensível a
energia escura e gravidade modificada; aparece em ℓ baixo.

**Sachs–Wolfe (SW).** O efeito "estático" correspondente, impresso na
própria superfície de recombinação.

**Variância cósmica.** O limite fundamental de precisão em escalas
grandes: só existe um universo, e há poucos modos independentes em ℓ
baixo — nenhum experimento futuro melhora isso.

**P(k) (espectro de potência da matéria).** Quanta estrutura existe em
cada escala espacial.

**Lensing (lente gravitacional).** O desvio da luz pela gravidade.
"Fraco" = distorções estatísticas das galáxias de fundo; sonda a soma
Φ+Ψ.

**μ(k,a) e Σ(k,a).** Os dois parâmetros-padrão de gravidade modificada:
**μ** modifica a equação de Poisson (governa o crescimento de
estrutura); **Σ** governa o lensing. Ambos valem 1 em GR.

**G_eff.** A constante gravitacional efetiva, = G·μ.

**fσ₈.** Combinação observável da taxa de crescimento de estrutura com
a sua normalização — o observável clássico de RSD.

**RSD (Redshift-Space Distortions).** Distorções na distribuição de
galáxias causadas por suas velocidades peculiares; medem o crescimento.

**S₈.** Combinação de amplitude e densidade de matéria; há uma tensão
conhecida entre CMB e lensing.

**Tensão H₀.** A discrepância entre o valor de H₀ inferido do CMB
(≈ 67) e o medido localmente (≈ 73).

**BAO (Baryon Acoustic Oscillations).** Escala padrão impressa pelas
ondas sonoras primordiais; usada como régua para medir distâncias.

**GW170817.** A fusão de estrelas de nêutrons detectada com luz e ondas
gravitacionais simultaneamente; provou que a velocidade das ondas
gravitacionais é a da luz com precisão de 10⁻¹⁵.

**Planck, DESI, Euclid, Rubin, SKA, LiteBIRD, CMB-S4, LIGO/Virgo.**
Experimentos: Planck (CMB, concluído), DESI (galáxias/BAO), Euclid e
Rubin (lensing e estrutura), SKA (rádio), LiteBIRD e CMB-S4 (CMB
futuro, polarização), LIGO/Virgo (ondas gravitacionais).

**CLASS / CAMB, hi_class, EFTCAMB.** Programas que resolvem as
equações de Boltzmann e produzem C_ℓ e P(k). hi_class e EFTCAMB são
extensões para gravidade modificada (da classe Horndeski).

**Hierarquia de Boltzmann.** O sistema de equações que segue a
evolução acoplada de fótons, neutrinos, bárions e matéria escura — o
motor de qualquer previsão de CMB.

**Limber (aproximação de).** Simplificação usada em cálculos de
lensing, que envolve integrais em distância comóvel (χ).

---

## 7. Física quântica e primordial

**Inflação.** Período de expansão acelerada no universo primordial que
gera as perturbações iniciais a partir de flutuações quânticas.

**Inflaton.** O campo que dirige a inflação.

**Inflação híbrida / waterfall.** Variante em que um segundo campo
("waterfall") sofre uma transição abrupta que encerra a inflação.

**SSB (quebra espontânea de simetria).** Quando as leis têm uma
simetria mas o estado não. É como a TDCP descreve a "bifurcação".

**Z₂.** Simetria discreta de troca — aqui, φ₁ ↔ φ₂, equivalente a
φ₋ → −φ₋.

**Parâmetro de ordem.** A quantidade que é zero na fase simétrica e
não-zero na fase quebrada (aqui, ⟨φ₋⟩).

**Paredes de domínio.** Defeitos topológicos que se formam quando uma
simetria **discreta** é quebrada espontaneamente: regiões do universo
escolhem sinais diferentes e as fronteiras entre elas carregam energia.
Um problema cosmológico clássico — paredes pesadas dominariam o
universo.

**Kibble–Zurek.** O mecanismo que descreve a formação desses defeitos
durante uma transição de fase.

**Decoerência.** Processo pelo qual superposições quânticas se tornam
alternativas clássicas por interação com o ambiente.

**Emaranhamento.** Correlação quântica entre subsistemas, sem análogo
clássico.

**Bunch–Davies.** O estado de vácuo padrão usado para definir as
condições iniciais quânticas em espaço-tempo em expansão.

**Collider cosmológico.** Ideia de que partículas massivas durante a
inflação deixam assinaturas oscilatórias características nas
correlações primordiais — uma "espectroscopia" do universo primordial.

**Estabilidade radiativa / naturalidade técnica.** Se uma escolha de
parâmetros sobrevive às correções quânticas ou precisa de ajuste fino
a cada ordem.

---

## 8. Teorias e resultados de referência citados

**GR (Relatividade Geral).** A teoria-padrão da gravidade, com uma só
métrica; o limite que qualquer modificação precisa recuperar.

**ΛCDM.** O modelo cosmológico padrão: constante cosmológica (Λ) +
matéria escura fria (CDM). O que qualquer alternativa precisa igualar
ou superar.

**Gravidade massiva.** Teoria em que o gráviton tem massa; a bimétrica
é seu parente com a segunda métrica dinâmica.

**Quasidilaton, chameleon bigravity, mass-varying massive gravity.**
Variantes da literatura em que um campo escalar modula parâmetros da
gravidade massiva — os "primos" mais próximos da TDCP.

**Galileon.** Classe de teorias escalares com estrutura derivativa
especial, associada ao mecanismo de Vainshtein.

**Horndeski.** A classe mais geral de teorias escalar-tensoriais com
equações de segunda ordem. Bimétrica **não** pertence a ela — daí os
códigos padrão de gravidade modificada não servirem diretamente.

**Teorema de Weinberg–Witten.** Resultado que proíbe grávitons
compostos sem massa sob certas hipóteses (não se aplica a massivos).

**Comelli–Crisostomi–Pilo, Könnig–Amendola et al., Akrami et al.,
Hassan–Rosen.** Autores das referências centrais de cosmologia
bimétrica: estrutura de vínculos, ramos de solução, instabilidades de
perturbação e viabilidade cosmológica.

---

## 9. Vocabulário próprio do projeto (método e processo)

**Gate.** Um teste com critério de aprovação/reprovação **escrito antes
de rodar**. O veredito sai só pelos critérios declarados.

**Nível epistêmico (1 / 2a / 2b / 3).** Rótulo obrigatório em cada
resultado: **1** = derivado e verificado por duas rotas independentes;
**2a** = uma rota, verificado numericamente; **2b** = numérico com
fronteiras de varredura declaradas; **3** = adotado da literatura.

**Fronteira declarada.** O escopo explícito de um resultado (quais
parâmetros, quais épocas, quantos pontos) — para impedir que ele seja
lido como mais geral do que é.

**Erratum.** Documento que registra um erro encontrado no próprio
trabalho e suas consequências em cascata. O projeto tem dois:
**Erratum-01** (a constraint de Bianchi estava errada no corpus) e
**Erratum-02** (um erro numérico na redução de vínculos criou um grau
de liberdade inexistente).

**Tabela de supersessão.** A lista do que cada resultado novo
substitui — impede citar números de eras anteriores como se fossem
atuais.

**Auto-teste de poder de detecção.** Verificar que um teste é capaz de
**reprovar** um caso sabidamente falso. Sem isso, uma aprovação não
significa nada.

**V-XREP (validação cruzada de representação).** Rodar o mesmo cálculo
em duas formulações inequivalentes e exigir o mesmo resultado.
**V-XREP-a** = dois canais de derivada temporal; **V-XREP-b** = duas
formulações da ação (Γ–Γ vs ADM).

**ADM.** Formulação da relatividade que separa espaço e tempo
(lapso, shift, métrica espacial); é a linguagem natural para contar
graus de liberdade.

**Γ–Γ (Gamma-Gamma).** Forma alternativa da ação de Einstein que usa só
primeiras derivadas — a usada pela biblioteca simbólica do projeto.

**Normalização congelada.** Medir crescimento com um fator de
normalização **fixo**, não variável no tempo. Normalizações variáveis
já produziram três artefatos neste projeto.

**Equilibração.** Reescalar variáveis (por exemplo Ẽ = k²E) para que
os números tenham magnitudes comparáveis e os cancelamentos não sejam
destruídos pela precisão finita.

**Halving.** Teste de convergência: repetir o cálculo com metade do
passo e verificar que o resultado não muda.

**Benchmark β-constante.** A célula de referência do projeto, com os
β_n fixos — nela a teoria se reduz a Hassan–Rosen puro mais um campo
escalar espectador.

**Fundo pousado (landed).** A trajetória em que o campo φ₋ condensa e
"pousa" de volta num estado estacionário.

**Janela de deslocamento.** A época em que o fundo se afasta ordem-1
dos dois ramos padrão, durante a condensação.

**Banda.** Nome dado, na era anterior do projeto, a uma suposta
amplificação transiente de perturbações — hoje sabidamente artefato.
