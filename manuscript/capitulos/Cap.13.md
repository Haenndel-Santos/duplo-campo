Perfeito --- a partir daqui a escrita vira técnica, objetiva e verificável. Vou estruturar esses quatro tópicos como um bloco de validação matemática (Cap.13--16) e já inicio o Cap.13 com o formalismo necessário para você conseguir checar consistência e delimitar espaço de parâmetros.

**BLOCO DE VALIDAÇÃO MATEMÁTICA (TDCP)**

**Cap.13 --- Espaço de parâmetros \beta_n, ramos cosmológicos e condições de consistência**

**Cap.14 --- Controle de isocurvatura (modos adiabático/isocurvatura) e condições observacionais**

**Cap.15 --- Massa efetiva do gravitón: Higuchi + limites GW + evolução temporal**

**Cap.16 --- Consistência UV (EFT): escala de corte, forte acoplamento, radiative stability**

Abaixo: Capítulo 13 completo (versão técnica).

**CAPÍTULO 13**

**Espaço de Parâmetros \beta_n, Ramos Cosmológicos e Consistência**

**13.1 Ação bimetric HR (base) e acoplamento TDCP**

Partimos do bimetric Hassan--Rosen (HR) com duas métricas dinâmicas g_{\mu\nu} e f_{\mu\nu}:

$$ S = \int d^4x\Bigg[ \frac{M_g^2}{2}\sqrt{-g}\,R[g] \;+\; \frac{M_f^2}{2}\sqrt{-f}\,R[f] \;-\; m^2 M_{\rm eff}^2 \sqrt{-g}\,V\!\left(\sqrt{g^{-1}f}\right) \Bigg] + S_m[g,\psi] + S_\phi $$

onde o potencial HR é

$$ V(\mathcal{K})=\sum_{n=0}^{4}\beta_n\,e_n(\mathcal{K}), \qquad \mathcal{K}=\sqrt{g^{-1}f}, $$

e a TDCP introduz modulação via campo estrutural \phi (ou \chi):

$$ \beta_n \rightarrow \beta_n(\phi) \quad\text{ou}\quad V \rightarrow F(\phi)\,V. $$

Nota técnica: a modulação \beta_n(\phi) é mais geral (e mais perigosa). A modulação global F(\phi) é mais controlável.

**13.2 Fundo FLRW bimetric e parametrização essencial**

Assumimos fundo homogêneo/isotrópico:

$$ ds_g^2=-N_g^2(t)dt^2+a^2(t)\delta_{ij}dx^i dx^j, \qquad ds_f^2=-N_f^2(t)dt^2+b^2(t)\delta_{ij}dx^i dx^j. $$

Definimos:

$$ H_g=\frac{1}{N_g}\frac{\dot a}{a}, \qquad H_f=\frac{1}{N_f}\frac{\dot b}{b}, \qquad r(t)=\frac{b}{a}, \qquad \xi(t)=\frac{N_f}{N_g}. $$

A matriz \mathcal{K}=\sqrt{g^{-1}f} no fundo é diagonal:

\mathcal{K}^\mu{}_\nu= {\rm diag}(\xi,r,r,r).

Então:

$$ e_0=1,\quad e_1=\xi+3r,\quad e_2=3\xi r+3r^2,\quad e_3=3\xi r^2+r^3,\quad e_4=\xi r^3. $$

Logo o potencial no fundo:

$$ V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3). $$

Se houver modulação global TDCP:

$$ V(\xi,r,\phi)=F(\phi)\,V(\xi,r). $$

**13.3 Equações de Friedmann e densidades de interação**

As equações de Friedmann tomam forma:

$$ 3M_g^2 H_g^2 = \rho_m + \rho_\phi + \rho_{\rm int}^{(g)}(r,\phi), $$

$$ 3M_f^2 H_f^2 = \rho_f + \rho_{\rm int}^{(f)}(r,\phi). $$

No caso HR padrão (e mantendo a notação usual), as densidades efetivas são:

$$ \rho_{\rm int}^{(g)}= m^2 M_{\rm eff}^2\,F(\phi)\, \Big(\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3\Big), $$

$$ \rho_{\rm int}^{(f)}= m^2 M_{\rm eff}^2\,F(\phi)\, \Big(\beta_4 + 3\beta_3 r^{-1} + 3\beta_2 r^{-2} + \beta_1 r^{-3}\Big). $$

Essas expressões são a ponte direta entre \beta_n e a cosmologia de fundo.

**13.4 Constraint de Bianchi e ramos (condição estrutural)**

A identidade de Bianchi gera a condição (forma típica no fundo FLRW):

$$ (\beta_1+2\beta_2 r+\beta_3 r^2)\,\big(H_g-\xi H_f\big)=0. $$

Portanto, existem dois ramos:

**(A) Ramo Algébrico (solução com r constante)**

\beta_1+2\beta_2 r+\beta_3 r^2 = 0 \quad\Rightarrow\quad r=r_\star=\text{const.}

**(B) Ramo Dinâmico (evolução de r(t))**

H_g=\xi H_f \quad\Rightarrow\quad r(t)\ \text{evolui}.

Decisão de modelagem: para "aceleração tardia emergente" com memória estrutural, o ramo dinâmico costuma ser mais fértil; o ramo algébrico é excelente como limite controlado e para conectar com \LambdaCDM.

**13.5 Caso proporcional como subcaso controlado (calibração)**

Se

$$ f_{\mu\nu} = c^2 g_{\mu\nu}\quad\Rightarrow\quad r=c,\ \xi=c, $$

então

$$ \rho_{\rm int}^{(g)}= m^2 M_{\rm eff}^2F(\phi) \Big(\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3\Big), $$

que funciona como uma energia escura efetiva.

Se F(\phi) varia lentamente:

w_{\rm eff}\approx -1 \quad \text{com desvio controlado por}\ \dot\phi.

Isso serve como calibração: você garante que a TDCP recupera um comportamento tipo-\Lambda em um limite bem definido.

**13.6 Como "ajustar" \beta_n de forma matemática (não narrativa)**

Aqui está o procedimento objetivo de ajuste:

**Passo 1 --- Fixar normalizações e reduzir degenerescência**

Defina uma escala:

- reescale m^2 M_{\rm eff}^2 como escala cosmológica,

- fixe uma combinação como unidade (ex.: \beta_1=1 ou \beta_0=1) para remover degenerescência de escala.

**Passo 2 --- Escolher ramo e impor condição de aceleração tardia**

A aceleração requer:

$$ \frac{\ddot a}{a} = \dot H_g + H_g^2 \> 0 $$

que, usando Friedmann + equação de Raychaudhuri, vira uma condição sobre pressão efetiva. Defina:

$$ \rho_{\rm DE}^{\rm eff} \equiv \rho_\phi + \rho_{\rm int}^{(g)}, \quad p_{\rm DE}^{\rm eff}\equiv p_\phi + p_{\rm int}^{(g)}. $$

Então aceleração tardia exige:

$$ \rho_m + \rho_{\rm DE}^{\rm eff} + 3p_{\rm DE}^{\rm eff} \< 0. $$

Isso impõe sinal e escala em combinações (\beta_0,\beta_1,\beta_2,\beta_3) via \rho_{\rm int}^{(g)}(r) e seu "equivalente de pressão" no fundo (derivável do tensor de interação).

**Passo 3 --- Impor recuperação de GR em regime local**

Em termos efetivos, isso significa suprimir o modo extra em escalas locais (massa/grande ou acoplamento pequeno). Isso entra via:

- massa do modo tensorial massivo m_T^2(\beta_n,r),

- e depois via \mu(k,a) (Cap.7--8).

Na prática você impõe (para grandes k):

\mu(k,a)\to 1 \quad \text{quando}\quad k/a\gg m_{\rm screen}

o que requer m_\sigma e/ou m_T suficientemente grandes ou acoplamentos \Delta pequenos.

**Passo 4 --- Checar Higuchi e estabilidade (link com Cap.15)**

Ainda neste capítulo, você já deixa a condição escrita como restrição em \beta_n:

m_T^2(\beta_n,r,\phi)\ \ge\ 2H^2 \quad\text{no regime quasi-de Sitter relevante}.

**Passo 5 --- Checar consistência do ramo dinâmico (evitar singularidades em r)**

Se o ramo dinâmico é usado, é comum que certas escolhas de \beta_n levem r a regiões problemáticas (ex.: r\to 0 ou r\to\infty). Impõe-se:

$$ 0\<r_{\min}\le r(t)\le r_{\max}\<\infty $$

e isso vira restrição nas combinações polinomiais:

\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3 \quad \text{não deve cruzar regiões que gerem instabilidade/ghost.}

**13.7 Famílias mínimas recomendadas (para varrer espaço de parâmetros)**

Para uma varredura inicial objetiva, recomendo duas famílias, porque reduzem dimensionalidade e ainda capturam fenomenologia:

**Família F1 (minimal cosmological)**

$$ (\beta_0,\beta_1,\beta_2,\beta_3,\beta_4) = (\beta_0,\beta_1,\beta_2,0,\beta_4) $$

Vantagem: reduz termos cúbicos em r, simplifica análise do ramo algébrico/dinâmico.

**Família F2 (late-time acceleration tuned)**

$$ (\beta_0,\beta_1,\beta_2,\beta_3,\beta_4) = (\beta_0,\beta_1,0,\beta_3,\beta_4) $$

Vantagem: mantém termo r^3 que é eficiente para gerar energia efetiva em grandes escalas.

Meta matemática: escolher uma família, resolver background (Cap.5), então impor:

- aceleração tardia,

- Higuchi,

- e GR local.

**13.8 Entregável deste capítulo (critério de conclusão)**

Este capítulo está "fechado" quando você consegue produzir um conjunto explícito de restrições em \beta_n do tipo:

1.  Existência de ramo cosmológico desejado (A ou B).

2.  Aceleração tardia com w_{\rm eff}\approx -1 (ou o comportamento alvo).

3.  Higuchi satisfeita no regime relevante.

4.  \mu(k,a)\to 1 em escalas locais (condição de retorno a GR).

5.  r(t) não diverge (faixa finita).

**Próximo passo (Cap.14 --- Isocurvatura)**

A isocurvatura vai depender diretamente de:

- se você usa \beta_n(\phi) (mistura multifield),

- e da massa efetiva do modo relativo escalar m_S^2(\beta_n,r,\phi).

Ou seja: Cap.14 usa o que definimos aqui.

**Para avançar agora sem travar**

Eu vou seguir o caminho mais objetivo possível:

✅ Escolha técnica imediata (sem debate longo):

Vamos começar com uma família mínima e derivar as restrições formais.

Minha recomendação para a TDCP, pela coerência com "memória estrutural" e aceleração tardia, é começar com F1:

$$ (\beta_0,\beta_1,\beta_2,0,\beta_4) $$

e trabalhar no ramo dinâmico, mantendo o ramo proporcional como limite de checagem.

Se você concorda, eu escrevo o Cap.13.9 com:

- forma explícita do polinômio do ramo algébrico (para comparação),

- equação diferencial efetiva para r(t) no ramo dinâmico,

- e como isso fixa a combinação de \beta_0,\beta_1,\beta_2,\beta_4 para reproduzir H(z).

Quer que eu siga com F1 + ramo dinâmico, ou prefere que a varredura inicial seja pelo ramo proporcional (mais simples para "calibrar" antes)?

Perfeito --- seguimos com F1:

$$ (\beta_0,\beta_1,\beta_2,\beta_3,\beta_4)=(\beta_0,\beta_1,\beta_2,0,\beta_4). $$

A partir daqui vou ser 100% técnico: escrever as equações no fundo, extrair o que dá para extrair analiticamente, e deixar claro quais combinações de \beta_n são fixadas por: (i) existência do ramo, (ii) aceleração tardia, (iii) recuperação de GR, (iv) estabilidade.

**CAP.13 (continuação) --- F1: Equações fechadas e restrições**

**13.9 Potenciais efetivos no fundo para F1**

Com \beta_3=0, as densidades de interação reduzem a:

$$ \rho_{\rm int}^{(g)}(r,\phi)=m^2M_{\rm eff}^2F(\phi)\Big(\beta_0+3\beta_1r+3\beta_2r^2\Big), $$

$$ \rho_{\rm int}^{(f)}(r,\phi)=m^2M_{\rm eff}^2F(\phi)\Big(\beta_4+3\beta_2r^{-2}+\beta_1r^{-3}\Big). $$

Defina abreviações úteis (técnica padrão para análise de bimetric FLRW):

$$ U(r)\equiv \beta_0+3\beta_1r+3\beta_2r^2, \qquad \tilde U(r)\equiv \beta_4+3\beta_2r^{-2}+\beta_1r^{-3}. $$

Então:

$$ \rho_{\rm int}^{(g)}=m^2M_{\rm eff}^2F(\phi)\,U(r), \qquad \rho_{\rm int}^{(f)}=m^2M_{\rm eff}^2F(\phi)\,\tilde U(r). $$

**13.10 Constraint de Bianchi e ramos para F1**

A constraint no fundo é:

$$ (\beta_1+2\beta_2r+\beta_3r^2)(H_g-\xi H_f)=0 $$

$$ e com \beta_3=0: $$

**(A) Ramo Algébrico**

$$ \beta_1+2\beta_2r=0 \quad\Rightarrow\quad \boxed{r_\star=-\frac{\beta_1}{2\beta_2}}. $$

Condição de existência física (evitar r\<0 para b=a r real e positivo):

$$ \boxed{r_\star\>0\ \Rightarrow\ \beta_1\beta_2\<0.} $$

Esse ramo é extremamente útil como limite: ele fixa r e transforma U(r) em constante (se F(\phi) for lento ou congelado).

**(B) Ramo Dinâmico**

$$ \boxed{H_g=\xi H_f.} $$

Esse é o ramo que permite r(t) evoluir, isto é, onde a TDCP ganha "memória estrutural" cosmológica.

**13.11 Escolha de gauge e relação cinemática para r(t)**

Fixe gauge N_g=1. Então H_g=\dot a/a.

Como H_f=\frac{1}{N_f}\frac{\dot b}{b}=\frac{1}{\xi}\frac{\dot b}{b}, a condição do ramo dinâmico:

$$ H_g=\xi H_f=\xi\left(\frac{1}{\xi}\frac{\dot b}{b}\right)=\frac{\dot b}{b}. $$

Logo:

$$ \frac{\dot b}{b}=\frac{\dot a}{a} \quad\Rightarrow\quad \frac{d}{dt}\ln\left(\frac{b}{a}\right)=0 \quad\Rightarrow\quad \boxed{\dot r=0.} $$

Resultado técnico importante:

No ansatz FLRW estritamente diagonal e com acoplamento HR puro, o "ramo dinâmico" como escrito acima força r=constante (porque a condição equivale a H_b=H_a).

Isso é um ponto sutil que explica por que, em bimetric FLRW, o "ramo dinâmico" não é simplesmente "r(t) livre" --- ele depende de como a constraint aparece (há formas equivalentes envolvendo \dot r e \xi). Em tratamentos completos, a constraint é frequentemente escrita como:

$$ (\beta_1+2\beta_2r+\beta_3r^2)\,(\dot r - (\xi-1)Hr)=0, $$

ou equivalente, onde o ramo dinâmico não fixa \dot r=0 trivialmente, mas fixa relação entre \xi e r. O ponto operacional para nós:

- se quisermos r(t) evoluindo, precisamos explicitar a forma completa da constraint com lapses e derivadas (ou introduzir a modulação TDCP F(\phi) e acoplamentos que geram \dot r\neq 0 de forma consistente).

Como você quer validar matematicamente, vou fazer do jeito correto: introduzir a variável de gauge-invariante e fechar o sistema.

**13.12 Forma fechada "padrão" do sistema FLRW bimetric (para evolução de r)**

Defina o "Hubble do setor f em tempo g":

$$ H_b \equiv \frac{\dot b}{b}, \quad (N_g=1). $$

Então

$$ H_f = \frac{1}{N_f}\frac{\dot b}{b}=\frac{H_b}{\xi}. $$

A constraint do ramo dinâmico, escrita como conservação do tensor de interação, pode ser posta na forma:

$$ \boxed{ (\beta_1+2\beta_2r+\beta_3r^2)\,(H_b-\xi H_g)=0 } $$

e para \beta_3=0:

$$ (\beta_1+2\beta_2r)\,(H_b-\xi H_g)=0. $$

No ramo dinâmico tomamos:

$$ \boxed{H_b=\xi H_g} $$

e então r=b/a evolui como:

$$ \dot r = \frac{d}{dt}\left(\frac{b}{a}\right)=r(H_b-H_g)=r(\xi-1)H_g. $$

Portanto:

$$ \boxed{ \dot r = r(\xi-1)H_g. } $$

Ou seja: r(t) evolui se e somente se \xi(t)\neq 1.

Isso é a forma operacional correta.

**13.13 Como eliminar \xi(t): usar a equação de Friedmann do setor f**

A equação do setor f (sem matéria, ou com \rho_f explícito) é:

$$ 3M_f^2H_f^2=\rho_f+\rho_{\rm int}^{(f)}(r,\phi). $$

Substituindo H_f=H_b/\xi e H_b=H_g+\dot r/r:

$$ H_f=\frac{H_g+\dot r/r}{\xi}. $$

Mas do ramo dinâmico H_b=\xi H_g\Rightarrow H_f=H_g. Então:

$$ \boxed{H_f=H_g.} $$

E a equação f vira restrição algébrica (em vez de dinâmica) para r:

$$ \boxed{ 3M_f^2H_g^2=\rho_f+m^2M_{\rm eff}^2F(\phi)\,\tilde U(r). } $$

Enquanto a equação g é:

$$ \boxed{ 3M_g^2H_g^2=\rho_m+\rho_\phi+m^2M_{\rm eff}^2F(\phi)\,U(r). } $$

Subtraindo as duas:

$$ 3(M_g^2-M_f^2)H_g^2 = \rho_m+\rho_\phi-\rho_f + m^2M_{\rm eff}^2F(\phi)\big(U(r)-\tilde U(r)\big). $$

Interpretação técnica:

No fundo FLRW, para HR puro, a consistência frequentemente força r a seguir de perto um valor quase algébrico determinado por H_g e pelas duas equações de Friedmann. A "dinâmica" de r é, na prática, controlada pela possibilidade de \xi\neq 1 e/ou pela presença de modulação F(\phi) que move o balanço entre U(r) e \tilde U(r).

**13.14 Estratégia TDCP específica para obter "evolução lenta" sem violar consistência**

Como você quer "memória estrutural" e aceleração tardia sem "forçar" \Lambda, o caminho mais controlável com F1 é:

**Escolha TDCP-1: modulação global lenta F(\phi) (recomendado)**

- mantenha \beta_n constantes,

- deixe F(\phi) variar lentamente em época tardia,

- e use o ramo proporcional/algébrico como baseline.

Então:

$$ \rho_{\rm DE}^{\rm eff}(a)=m^2M_{\rm eff}^2F(\phi(a))\,U(r_\star)+\rho_\phi(a). $$

Aqui o "ajuste" é matematicamente limpo:

- \beta_n determinam a forma e o sinal de U(r_\star),

- F(\phi) determina a evolução temporal de \rho_{\rm DE}^{\rm eff}.

Isso separa bem os problemas:

- Cap.13 fixa \beta_n,

- Cap.14 controla isocurvatura via massa efetiva do modo relativo,

- Cap.15 fixa m_T,

- Cap.16 estabelece EFT/corte.

**13.15 Restrições explícitas em F1 (primeiro conjunto "fechado")**

**(i) Existência do ramo algébrico com r_\star\>0**

$$ \boxed{\beta_1\beta_2\<0.} $$

**(ii) Energia efetiva positiva para aceleração (no setor g)**

A contribuição tipo-\Lambda efetiva (no ramo algébrico) é:

$$ \rho_{\rm int}^{(g)}(r_\star)=m^2M_{\rm eff}^2F(\phi)\,U(r_\star). $$

Aceleração tardia exige, aproximadamente, \rho_{\rm int}^{(g)}(r_\star)\>0 e pressão efetiva \approx -\rho. Então:

\boxed{U(r_\star)\>0 \quad \text{(assumindo }F(\phi)\>0\text{)}.}

$$ Com r_\star=-\beta_1/(2\beta_2): $$

$$ U(r_\star)=\beta_0+3\beta_1r_\star+3\beta_2r_\star^2 = \beta_0 -\frac{3\beta_1^2}{2\beta_2} +\frac{3\beta_1^2}{4\beta_2} = \boxed{\beta_0-\frac{3\beta_1^2}{4\beta_2}.} $$

Logo condição:

$$ \boxed{ \beta_0-\frac{3\beta_1^2}{4\beta_2}\>0. } $$

Como \beta_1\beta_2\<0, o termo -\frac{3\beta_1^2}{4\beta_2} tem sinal oposto ao de \beta_2. Isso já restringe fortemente o espaço.

**(iii) Consistência do setor f: positividade/realidade de H_f^2**

No ramo proporcional H_f=H_g, então precisamos que:

$$ 3M_f^2H_g^2-\rho_f = m^2M_{\rm eff}^2F(\phi)\tilde U(r_\star) $$

seja compatível com H_g^2\>0. Isso impõe:

\boxed{\tilde U(r_\star)\ \text{não deve forçar }H_g^2\<0.}

Com:

$$ \tilde U(r)=\beta_4+3\beta_2r^{-2}+\beta_1r^{-3} $$

e r=r_\star, isso vira restrição algébrica em \beta_4 dada (\beta_1,\beta_2). (Aqui costuma-se usar \beta_4 como "parametro de compensação".)

Resumo do que temos já, de forma fechada:

$$ - \beta_1\beta_2\<0 $$

$$ - \beta_0-\frac{3\beta_1^2}{4\beta_2}\>0 $$

- \beta_4 escolhido para manter o setor f consistente

Isso já é um primeiro conjunto de restrições matemáticas.

**13.16 Como "fit" de H(z) fixa combinações de \beta_n (sem rodar código)**

No ramo algébrico/proporcional e assumindo \rho_\phi subdominante (ou lenta), a equação do setor g se parece com:

$$ 3M_g^2H^2(z)\approx \rho_m(z)+m^2M_{\rm eff}^2F(\phi(z))\,U(r_\star). $$

Se F\approx 1 hoje, então o valor observado de H_0 fixa:

$$ \boxed{ m^2M_{\rm eff}^2\,U(r_\star)\approx 3M_g^2H_0^2-\rho_{m0}. } $$

Ou seja: a "escala" de energia escura efetiva fixa um produto m^2M_{\rm eff}^2U(r_\star). Em termos de ajuste, isso significa que um grau de liberdade é absorvido nessa normalização --- e sobra o ajuste fino real para crescimento, massa do gravitón e isocurvatura.

**Fechamento do Cap.13 (F1) --- o que está matematicamente estabelecido**

1.  Para F1, o ramo algébrico é explícito e fornece r_\star.

2.  A aceleração tardia pode ser obtida exigindo U(r_\star)\>0.

3.  Isso produz uma restrição analítica simples:

$$ \boxed{\beta_0-\frac{3\beta_1^2}{4\beta_2}\>0,\qquad \beta_1\beta_2\<0.} $$

4.  O parâmetro \beta_4 é usado para manter consistência do setor f (e afetará o setor tensorial via massa efetiva).

**Próximo passo: Cap.14 (Isocurvatura) --- ligação direta com F1**

Agora, com F1 definido, o próximo passo matemático é:

- escrever a ação quadrática dos modos escalares (\zeta,S),

- extrair a massa efetiva m_S^2(\beta_n,r,\phi),

- impor condição de supressão:

\boxed{m_S^2 \gg H^2 \quad \text{(após a fase primordial)}.}

Se você confirmar, eu inicio o Cap.14 já no mesmo nível técnico, começando por:

- decomposição adiabática/isocurvatura,

- matriz cinética K_{ij},

- matriz de massa \Omega_{ij},

- e condições de ausência de fantasma/gradiente no setor escalar (em função de F1).

Confirmo que avançamos para Cap.14 --- Isocurvatura agora?
