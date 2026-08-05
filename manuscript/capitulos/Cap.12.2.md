Perfeito --- esses quatro pontos são exatamente o "núcleo duro" que transforma a TDCP de uma cosmologia bonita em uma teoria que não cai quando encosta em dados e consistência interna.

Vou trabalhar cada um em camadas, mantendo o estilo conceitual (livro) mas com matemática e critérios claros (tese). E vou amarrar tudo num plano operacional: o que medir, o que impor, o que ajustar.

**1) Ajuste de parâmetros \beta_n**

Na linguagem Hassan--Rosen (HR), os \beta_n definem o potencial de interação:

$$ V(\mathcal{K})=\sum_{n=0}^{4}\beta_n\, e_n(\mathcal{K}), \qquad \mathcal{K}=\sqrt{g^{-1}f}. $$

No fundo FLRW, isso vira funções algébricas de r(t)=b/a e \xi=N_f/N_g, e gera as densidades efetivas de interação (do Cap.4/5). O primeiro objetivo prático do "ajuste" é:

**(i) Fixar o limite GR + \LambdaCDM como subcaso**

Você quer que, quando o desacoplamento estrutural é pequeno, a TDCP "pareça" GR.

Isso normalmente significa impor:

- r(t)\to 1 em algum regime (ou r\to c constante no ramo proporcional),

- o modo massivo suficientemente pesado em escalas locais,

- e a aceleração tardia emergindo como termo efetivo.

Um subcaso controlado é o ramo proporcional:

$$ f_{\mu\nu} = c^2\, g_{\mu\nu} \quad \Rightarrow \quad r=c=\text{const.} $$

Nesse caso, a energia efetiva tipo-\Lambda no setor g fica:

$$ \rho_{\text{int}}^{(g)}= m^2 M_{\text{eff}}^2 F(\phi)\left(\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3\right). $$

Tradução prática:

o combo \beta_0,\beta_1,\beta_2,\beta_3 define o "\Lambda emergente", enquanto \beta_4 é mais relevante do lado f.

**(ii) Evitar instabilidades conhecidas do bimetric**

O ajuste não é livre: ele é restringido por:

- estabilidade cosmológica (ramo dinâmico vs algébrico),

- ausência de fantasma (estrutura HR já ajuda),

- Higuchi no setor tensorial (vamos já chegar).

Uma heurística útil é trabalhar em "famílias":

**Família mínima (boa para começar)**

- \beta_0,\beta_1,\beta_4 não nulos, \beta_2=\beta_3=0 (ou vice-versa).

- Menos parâmetros = menos degenerescência.

**Família "cosmológica"**

- \beta_0,\beta_1,\beta_2,\beta_3 ativos para controlar \rho_{\text{int}}^{(g)}(r)

- \beta_4 para consistência do setor f.

Sugestão TDCP (operacional):

1. Fixar um ramo (proporcional ou dinâmico).

2. Escolher uma família de \beta_n.

3. Impor: H(z) desejado (expansão tardia).

4. Verificar: Higuchi + G_{\rm eff} (crescimento).

5. Ajustar só depois.

**2) Controle de isocurvatura**

Esse ponto é muito sério porque a CMB (Planck e sucessores) põe limites fortes em modos isocurvatura.

Na TDCP, isocurvatura surge naturalmente porque existem dois setores e um modo relativo \sigma. Em notação padrão:

- modo adiabático: \zeta

- modo isocurvatura: S

Um modelo multifield típico tem:

$S \neq 0 \quad \text{no início}.$

Você quer um mecanismo que:

- permita S existir na bifurcação (filosoficamente natural),

- mas faça S morrer antes de ficar observável.

O mecanismo matemático mais limpo é o "isocurvatura pesada":

$\ddot S + 3H\dot S + m_S^2 S = 0, \qquad m_S^2 \gg H^2$

\Rightarrow solução decai:

$S \propto a^{-3/2}\, e^{-m_S t}.$

O que controla m_S na TDCP?

- a massa efetiva do modo relativo \sigma,

- derivadas dos \beta_n(\phi) se houver modulação,

- a dinâmica de r(t).

Estratégia recomendada:

- No regime primordial: permitir uma janela curta com m_S^2 \lesssim H^2 (gera sementes).

- Após isso: transição para m_S^2 \gg H^2 (mata isocurvatura).

Como obter isso sem "mágica"?

- usando \beta_n(\phi) com perfil tipo "step" suave (adiabático), ou

- usando potencial V(\phi) que muda a massa efetiva naturalmente quando \phi atravessa um ponto crítico.

Condição de "controle" que vamos impor como regra de projeto:

$\frac{P_S}{P_\zeta}\bigg|_{\text{recomb}} \ll 1.$

(Depois, quando formos formalizar, colocamos um alvo numérico e comparamos com limites atuais.)

**3) Limites na massa do gravitón (modo tensorial massivo)**

Aqui entram duas coisas:

**(i) Higuchi (consistência em de Sitter)**

$m_T^2 \ge 2H^2.$

Isso é interno: não é dado experimental --- é sanidade da teoria no fundo.

**(ii) limites observacionais (propagação e dinâmica)**

O modo massivo não pode afetar ondas gravitacionais observadas de forma incompatível.

Na prática, o que você precisa como "regra de projeto":

- No regime tardio: m_T muito pequeno ou o acoplamento do modo massivo ao setor visível suprimido.

- Em escalas locais: efeitos do modo massivo devem ser screened/suprimidos.

Na TDCP, m_T^2 é uma função de m^2, \beta_n e r(t). Então:

Ajustar \beta_n também é ajustar m_T.

O caminho mais "limpo" é manter:

- m_T suficientemente pequeno hoje, mas

- não violar Higuchi no regime primordial onde H pode ser grande.

Isso parece contraditório, mas pode ser resolvido se m_T for dinâmico:

$m_T^2(a) = m^2\,\mathcal{F}\big(\beta_n(\phi(a)), r(a)\big).$

Ou seja: massa efetiva muda com a história cosmológica.

Isso é bem TDCP: "memória estrutural".

**4) Consistência UV (teoria efetiva?)**

A TDCP é uma teoria fundamental ou uma teoria efetiva (EFT) válida até certa escala?

A resposta mais defensável (e cientificamente honesta) é tratá-la como teoria efetiva.

Isso não a enfraquece --- quase toda física moderna é EFT em algum regime.

O que precisamos declarar e controlar:

**(i) Escala de corte \Lambda_{\rm cut}**

Existe uma escala acima da qual o formalismo não deve ser extrapolado.

No bimetric/massive gravity, a escala de forte acoplamento pode aparecer (dependendo de parâmetros). Em linguagem TDCP:

- o "vácuo dinâmico" e o modo relativo podem entrar em regime não-linear forte.

**(ii) Naturalidade e radiative stability**

Se você define \beta_n(\phi), loops quânticos podem "renormalizar" esses termos.

A pergunta é:

- os ajustes que fazemos são estáveis sob correções?

- ou exigem re-ajuste infinito?

A regra pragmática:

- restringir a forma funcional de \beta_n(\phi) para ser tecnicamente natural (simetrias, pequenas derivações),

- trabalhar com modulação adiabática:

$\left|\frac{\dot{\beta}_n}{\beta_n}\right| \ll H.$

**(iii) Domínio de validade cosmológica**

Você pode declarar explicitamente:

- TDCP válida do regime pós-bifurcação até hoje,

- sem pretender descrever o "momento zero" em escala de Planck.

Isso é completamente aceitável para publicação.

**Plano de trabalho (bem objetivo)**

Para transformar esses quatro "riscos" em capítulos robustos, eu sugiro escrevermos um módulo técnico em 4 seções (um mini-bloco dentro do livro):

**Capítulo 13 --- Espaço de parâmetros \beta_n e ramos cosmológicos**

- ramo proporcional vs dinâmico

- famílias mínimas de \beta_n

- como \rho_{\rm int}(r) gera aceleração

**Capítulo 14 --- Isocurvatura: geração e supressão controlada**

- decomposição (\zeta,S)

- condição m_S^2 \gg H^2 pós-bifurcação

- critérios de observabilidade

**Capítulo 15 --- Massa efetiva do gravitón e limites**

- Higuchi primordial

- regime tardio e supressão

- massa dinâmica m_T(a) via \phi(a) e r(a)

**Capítulo 16 --- TDCP como EFT: consistência UV e naturalidade**

- escala de validade

- radiative stability qualitativa

- regime não-linear e limites

**Pergunta prática para começarmos AGORA**

Minha recomendação estrutural é começar por \beta_n porque ele alimenta os outros três (isocurvatura, massa do gravitón, EFT).
