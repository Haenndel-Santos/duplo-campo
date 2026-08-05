> **APÊNDICE L --- PONTES CONCEITUAIS ENTRE A LINHA EXPLORATÓRIA (APÊNDICES
> I--K) E O CORPO PRINCIPAL F1**
>
> Apêndice curto, produzido na Tarefa 5 como consolidação da Tarefa 4
> (`integration_assessment.md`). Registra **apenas** a reinterpretação que
> o veredito de integração parcial considerou absorvível ao corpo F1 sem
> alterar nenhuma equação já derivada nos Capítulos 1--26. Não introduz
> física nova, não substitui `integration_assessment.md` (que permanece a
> referência técnica completa, com os cálculos e o checklist HR) e não
> deve ser lido como uma reconciliação formal --- é um guia de leitura.

**L.1 O que este apêndice é e não é**

Os Apêndices I, J e K (originalmente capítulos em inglês sem numeração
formal) descrevem um mecanismo cosmogônico próprio — colapso de uma
função de onda universal, dois domínios emaranhados, um termo de
interação L_int e uma energia escura de emaranhamento Λ_ent. A Tarefa 4
avaliou esse material contra o formalismo bimétrico Hassan-Rosen +
campo escalar φ + família F1 já demonstrado nos Capítulos 1--26 e
concluiu **integração parcial**: as equações específicas dos Apêndices
I--K não são recicláveis como estão (ver `integration_assessment.md`
para o porquê, com cálculo explícito), mas a intuição física por trás
delas tem uma leitura legítima em termos do que já foi derivado. Este
apêndice documenta *apenas* essa leitura.

**L.2 "Dois domínios correlacionados" já é o Capítulo 1**

Não é necessário importar g^{(1)}/g^{(2)} nem o mecanismo de colapso
quântico |Ψ⟩=α|g₁⟩+β|g₂⟩ para ter "dois domínios que já foram
correlacionados": os Capítulos 1--2 já postulam exatamente isso — dois
núcleos primordiais correlacionados Φ₁,Φ₂, cuja bifurcação (instabilidade
do modo Φ₋) gera os dois setores que o formalismo bimétrico depois
descreve como g e f. Quem quiser uma linguagem de "emaranhamento" para
essa correlação primordial pode aplicá-la **como glosa narrativa** sobre
Φ₁,Φ₂ (Capítulo 1) ou sobre g,f (Capítulos 2--5) — não como uma estrutura
matemática adicional. Nenhuma equação muda.

**L.3 "Energia escura como remanescente de interação" já é o ramo
algébrico + η**

O Capítulo 5 (§5.9) e o Capítulo 13 (ramo algébrico, U(r⋆)>0) já mostram
que a TDCP-F1 produz um termo tipo constante-cosmológica como
remanescente da interação entre g e f (via ρ_int(r)). O vácuo dinâmico η
(Capítulo 1; forma canônica no Anexo H: η̇=Γχ̇², H²∝1/(1-η)) já é o
mecanismo formal para uma contribuição tardia e lentamente variável à
energia escura, sourced por separação estrutural entre os dois setores.
Quem quiser chamar isso de "energia de emaranhamento" pode fazê-lo como
**nome alternativo** para o que ρ_int(r) e η já produzem — **nunca como
um termo adicional Λ_ent somado por fora**, o que contaria a mesma física
duas vezes. Se uma equação de movimento explícita para uma quantidade
chamada "Λ_ent" for desejada no futuro, a via consistente é defini-la
como função de η (p.ex. Λ_ent≡f(η)), não introduzi-la solta.

**L.4 O que continua fora, mesmo nesta leitura permissiva**

- O aparato de colapso quântico (|Ψ⟩, amplitudes α,β) permanece fora: não
  tem ponte demonstrada com a ação clássica bimétrica, e nenhuma
  reinterpretação muda isso sem um trabalho técnico novo (redução de
  minisuperespaço/Wheeler-DeWitt para a ação de Cap.2--5).
- Qualquer acoplamento de matéria a f (ou a g^{(2)}) simétrico ao de g
  permanece incompatível com a contagem de graus de liberdade livre de
  fantasma do Capítulo 6.
- L_int como termo lagrangiano independente permanece descartado: se a
  intenção é um termo de interação quadrático, ele já existe — é o setor
  quadrático de V(K)=Σβₙeₙ(K) (Capítulos 3, 13), não um termo novo.

**L.5 Se o autor quiser revisitar a integração no futuro**

O caminho tecnicamente honesto, caso o autor queira retomar esta linha de
pesquisa com intenção de integração total, é: (i) reescrever o
acoplamento de matéria dos Apêndices I--K para que apenas um domínio
acople matéria; (ii) expressar qualquer termo de interação novo
diretamente em K=√(g⁻¹f), não em (g^{(1)}-g^{(2)})²; (iii) definir Λ_ent
como função explícita de η com uma equação de movimento; (iv) rodar
`stability-constraints-auditor` e `bimetric-hr-formalism-guardian` sobre
o resultado antes de qualquer alegação de consistência. Até que isso seja
feito, os Apêndices I--K permanecem, corretamente, fora do corpo numerado
F1.
