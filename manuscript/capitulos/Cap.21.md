**CAPÍTULO 21 --- Solução Estática Completa + Limites PPN na TDCP-F1**

**21.1 Objetivo e estratégia**

O Cap.20 mostrou que o helicity-0 do modo massivo (representado por \pi) entra em regime Vainshtein e suprime a quinta força em escalas solares. Agora precisamos fechar o bloco solar de maneira formal:

1. Construir a solução estática fraca no gauge isotrópico para g_{\mu\nu} (métrica física acoplada à matéria).

2. Expressar as correções induzidas por \pi nos potenciais \Phi(r), \Psi(r).

3. Traduzir isso nos parâmetros PPN, principalmente

$$ > \gamma_{\rm PPN}(r)=\frac{\Psi(r)}{\Phi(r)}\,,\qquad \beta_{\rm PPN}. $$

4. Obter desigualdades paramétricas (em termos de \alpha_V, Z, c_3, m^2F(\phi)) que garantem compatibilidade com limites solares (Cassini etc.).

5. Incorporar corretamente o efeito de F(\phi) e controlar a possibilidade de "quinta força" adicional via \phi.

**21.2 Ansätze: métrica estática isotrópica e regime fraco**

Assumimos, para o setor g_{\mu\nu} (métrica física), um ansatz estático e fraco (PN de primeira ordem):

$$ ds_g^2 = -(1+2\Phi(r))\,dt^2 + (1-2\Psi(r))\,(dr^2 + r^2 d\Omega^2), $$

$com |\Phi|,|\Psi|\ll 1.$

A matéria é não-relativística, T_{00}\simeq \rho, T\simeq -\rho.

A teoria contém, além do modo sem massa (gráviton usual), um setor massivo cujo helicity-0 efetivo \pi mistura com h_{\mu\nu}. Na linguagem do limite de desacoplamento (Cap.20), o acoplamento efetivo é:

$$ \mathcal{L}_{\pi T} \simeq \frac{\alpha_V}{M_{\rm Pl}}\pi\,T. $$

A modulação TDCP-F1 entra por:

$$ m_{\rm eff}^2 = m^2 F(\phi),\qquad \Lambda_3^3 \sim m^2F(\phi)\,M_{\rm eff}. $$

No Sistema Solar, tomamos \phi\simeq \phi_0 + \delta\phi(r) e trataremos \delta\phi como subdominante (a consistência disso será explicitada em 21.7).

**21.3 Potenciais em presença de um escalar acoplado: decomposição física**

Em teorias com um grau escalar que acopla ao traço T, a correção à gravitação newtoniana pode ser parametrizada por um fator "quinta força" Q(r), definido por:

$$ \frac{d\Phi}{dr} = \frac{GM}{r^2}\big[1+Q(r)\big], \qquad \frac{d\Psi}{dr} = \frac{GM}{r^2}\big[1+\tilde Q(r)\big]. $$

No GR puro, Q=\tilde Q=0 e \Phi=\Psi=-GM/r.

Na TDCP-F1, a origem de Q,\tilde Q é o setor massivo (helicity-0) e sua mistura com o modo tensorial. Para fontes solares e r\ll m_S^{-1}, o Yukawa não corta nada; a supressão vem do Vainshtein, então:

$$ Q(r)\propto \left(\frac{r}{r_V}\right)^{3/2} \quad (r\ll r_V). $$

O ponto PPN é que o parâmetro \gamma é sensível à diferença entre \Psi e \Phi.

**21.4 Relação entre \Phi,\Psi e o helicity-0 no limite de desacoplamento**

No limite de desacoplamento de teorias HR/dRGT-like, após diagonalizar o modo massless (GR) e o setor massivo, a métrica física pode ser escrita esquematicamente como:

$$ g_{\mu\nu} = \eta_{\mu\nu} +\frac{1}{M_{\rm Pl}}\Big(h^{(0)}_{\mu\nu} + \kappa\,h^{(m)}_{\mu\nu}\Big) +\frac{\kappa_\pi}{M_{\rm Pl}}\pi\,\eta_{\mu\nu} +\cdots $$

- h^{(0)}_{\mu\nu}: modo massless (gera o potencial GR).

- h^{(m)}_{\mu\nu}: modo massivo tensorial (Yukawa no regime linear).

- \pi: helicity-0 associado ao modo massivo, com acoplamento efetivo \sim \alpha_V.

No regime solar relevante para screening:

- o tensor massivo é suprimido por mistura (e/ou Yukawa se m não for ultraleve)

- o helicity-0 domina a correção potencial, mas é screened por auto-interações.

Para uma fonte esférica, a solução screened do Cap.20 fornece:

$$ \frac{F_\pi}{F_N} \equiv \frac{\pi'/M_{\rm Pl}}{GM/r^2} \sim \alpha_V^2\left(\frac{r}{r_V}\right)^{3/2}, \qquad (r\ll r_V). $$

Logo, o efeito do helicity-0 sobre os potenciais pode ser capturado por:

$$ \Phi(r)= -\frac{GM}{r}\left[1+\epsilon_\Phi(r)\right],\qquad \Psi(r)= -\frac{GM}{r}\left[1+\epsilon_\Psi(r)\right], $$

$com \epsilon_{\Phi,\Psi}(r)\sim \mathcal{O}(F_\pi/F_N).$

Em modelos dRGT/HR-like, a estrutura típica é:

$$ \epsilon_\Phi(r) = +c_\Phi\,\frac{F_\pi}{F_N},\qquad \epsilon_\Psi(r) = +c_\Psi\,\frac{F_\pi}{F_N}, $$

onde c_\Phi,c_\Psi são números \mathcal{O}(1) determinados pela mistura e pelo gauge escolhido.

Portanto, o parâmetro PPN \gamma é:

$$ \gamma(r)\equiv\frac{\Psi}{\Phi} = \frac{1+\epsilon_\Psi(r)}{1+\epsilon_\Phi(r)} \simeq 1+\left[\epsilon_\Psi(r)-\epsilon_\Phi(r)\right] \quad (\text{em ordem linear}). $$

Logo:

$$ \boxed{ \gamma(r)-1 \simeq (c_\Psi-c_\Phi)\,\alpha_V^2\left(\frac{r}{r_V}\right)^{3/2}. } $$

Este é o resultado operacional principal: \gamma-1 é proporcional ao mesmo fator screened, com coeficiente \mathcal{O}(1).

**21.5 Inclusão correta de F(\phi) no raio de Vainshtein e nos limites**

Do Cap.20 consolidado:

$$ r_V \sim \left(\frac{GM}{m^2F_0}\right)^{1/3}\left(\frac{\alpha_V c_3}{Z^2}\right)^{1/3}, \qquad F_0\equiv F(\phi_0). $$

Assim, para r\ll r_V:

$$ \gamma(r)-1 \sim (c_\Psi-c_\Phi)\,\alpha_V^2 \left[ \frac{r^3\,m^2F_0}{GM} \left(\frac{Z^2}{\alpha_V c_3}\right) \right]^{1/2}. $$

Ou seja:

$$ \boxed{ |\gamma(r)-1| \;\propto\; \alpha_V^{3/2}\, \left(\frac{Z}{\sqrt{c_3}}\right)\, \left(\frac{m\sqrt{F_0}\,r^{3/2}}{\sqrt{GM}}\right). } $$

A dependência em F_0 é suave: r_V\propto F_0^{-1/3} e, portanto, o screening melhora se F_0 cresce.

**21.6 Bound de Cassini: desigualdade paramétrica explícita**

O limite clássico de Cassini (tomado como referência) é, em ordem de grandeza:

$|\gamma-1| \lesssim 2.3\times 10^{-5}.$

Aplique em r\simeq r_{\rm AU} (ou em raio de impacto solar típico; aqui usamos AU como estimativa conservadora).

Usando:

$$ |\gamma(r)-1| \simeq \mathcal{C}_\gamma\, \alpha_V^2\left(\frac{r}{r_V}\right)^{3/2}, \qquad \mathcal{C}_\gamma \equiv |c_\Psi-c_\Phi|\sim \mathcal{O}(1), $$

obtemos o critério:

$$ \boxed{ r_V \gtrsim r_{\rm AU} \left(\frac{\mathcal{C}_\gamma\,\alpha_V^2}{2.3\times10^{-5}}\right)^{2/3}. } $$

Como r_V^\odot\sim 5\text{--}120 pc (para m\sim 100\text{--}1\,H_0/c e F_0\sim\mathcal{O}(1)), isso satisfaz a desigualdade com margem enorme mesmo para \alpha_V\sim 1.

**21.7 Quinta força adicional via \phi: condição de inocuidade local**

A TDCP-F1 contém um escalar \phi que modula a massa efetiva:

$m_{\rm eff}^2 = m^2F(\phi).$

Existem duas vias potenciais de violação solar:

1. \phi acoplar diretamente à matéria (termo do tipo \phi T/M).

2. \phi gerar gradientes locais que alteram F(\phi) e, portanto, r_V ou a força extra.

Pela construção fornecida, a matéria acopla apenas a g:

$\mathcal{L}_m[g],$

logo não há acoplamento conforme direto de \phi à matéria no nível fundamental, a menos que \mathcal{L}_\phi introduza explicitamente tal termo (o que não foi assumido).

O efeito residual vem apenas de F(\phi) na interação bimetric. Para ser inócuo no Sistema Solar, basta garantir que:

- \delta\phi(r) seja pequena no entorno solar, ou

- que F(\phi) varie lentamente: |\nabla F|/F \ll 1/r_{\rm AU}.

Um critério operacional é:

$$ \boxed{ \left|\frac{\delta F}{F_0}\right|_{r\sim {\rm AU}} \ll 1 \quad\Rightarrow\quad \delta r_V/r_V \simeq -\frac{1}{3}\,\delta F/F_0 \ \text{desprezível}. } $$

Em termos da dinâmica de \phi, uma condição suficiente típica é:

$m_\phi^2 \gg \frac{1}{{\rm AU}^2}$

(ou, equivalentemente, \lambda_\phi\ll {\rm AU}), pois isso impede perfis longos de \phi em torno do Sol. Mesmo se m_\phi for leve cosmologicamente, outra possibilidade é que \phi seja "stiff" localmente (grande Z_\phi).

Resumo: o Cap.21 fecha o bloco solar exigindo que \phi não introduza uma nova quinta força não-screened. Na TDCP-F1, isso é obtido se \phi não acopla diretamente à matéria e suas variações locais forem pequenas.

**21.8 Parâmetro \beta_{\rm PPN}: estrutura e hierarquia esperada**

O parâmetro \beta_{\rm PPN} mede não-linearidades de segunda ordem no potencial (ordem \Phi^2). Em teorias com screening forte, a expectativa é:

$$ \beta_{\rm PPN}-1 \sim \mathcal{O}\!\left(\left(\frac{F_\pi}{F_N}\right)^2\right) \sim \alpha_V^4\left(\frac{r}{r_V}\right)^3, $$

portanto ainda mais suprimido que \gamma-1.

Assim, para r\sim {\rm AU} e r_V^\odot\gg{\rm AU}, espera-se:

$\boxed{ |\beta_{\rm PPN}-1|\ll |\gamma_{\rm PPN}-1| }$

e o bound dominante é o de \gamma.

**Conclusão do Capítulo 21 (Bloco Solar)**

1. O helicity-0 screened induz correções nos potenciais:

$$ > \epsilon_{\Phi,\Psi}(r)\sim \alpha_V^2\left(\frac{r}{r_V}\right)^{3/2}. $$

2. O parâmetro PPN principal:

$$ > \boxed{ \gamma(r)-1 \simeq \mathcal{C}_\gamma\,\alpha_V^2\left(\frac{r}{r_V}\right)^{3/2}, \qquad \mathcal{C}_\gamma\sim \mathcal{O}(1). } $$

3. O raio de Vainshtein na TDCP-F1 inclui corretamente F(\phi):

$$ > \boxed{ r_V \sim \left(\frac{GM}{m^2F_0}\right)^{1/3}\times \mathcal{O}(1). } $$

4. Para o Sol, com m\sim 30\text{--}300\,H_0 (e mesmo m\sim 100H_0):

$$ > r_V^\odot \gg 1\,{\rm AU} \Rightarrow |\gamma-1|\ \text{é automaticamente pequeno}. $$

5. Condição adicional TDCP-específica:

$$ > \boxed{ \left|\delta F/F_0\right|_{AU}\ll 1 \quad\Rightarrow\quad \phi \text{ não reintroduz quinta força local relevante}. } $$

**Próximo passo (Cap.22)**

**CAPÍTULO 22 --- Estabilidade Não-Linear: ausência de ghosts/gradientes e consistência do setor helicity-0**

onde vamos formalizar:

- estabilidade do background screened

- condições de positividade do Hamiltoniano efetivo

- ausência de instabilidade superluminal patológica (quando aplicável)

- consistência do EFT no regime Vainshtein (\partial^2\pi \ll \Lambda_3^3 ou regime controlado)
