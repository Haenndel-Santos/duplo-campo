# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote03.py — vereditos do Lote 3 (C11–C15).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes. Ordem importa (especificas antes de genericas).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

V = [
 # ================= C11 =================
 ("C11", r"h_{ij}^{(g)} , \quad h_{ij}^{(f)}", "Cap.6", "CONFERE (notação)", False),
 ("C11", r"\frac{1}{2} a^3 \dot{h}_0^2", "Cap.6", "CONFERE SOB HIPÓTESE (normalização canônica implícita — sem M² e sem os fatores distintos dos dois setores; forma exata na âncora D2; a passagem (h,ℓ)→(h₀,h_m) canônicos é silenciosa)", False),
 ("C11", r"\ddot{h}_0 + 3H \dot{h}_0", "ação acima", "CONFERE (modo massless existe — âncora D2)", False),
 ("C11", r"\ddot{h}_m + 3H \dot{h}_m", "ação acima", "CONFERE SOB HIPÓTESE (esquemática; m_T² real com ξ e c² misto — âncora D2)", False),
 ("C11", r"m_T^2 \sim m^2 \times F(\beta_n, r)", "—", "CONFERE SOB HIPÓTESE (proporcionalidade; forma exata na âncora D2 — depende TAMBÉM de ξ); NOTA: F(β_n,r) genérica colide com F(φ) multiplicativa — renomear", False),
 ("C11", r"$c_T^2 = 1$", "—", "CONFERE SOB HIPÓTESE (âncora D2: c_g²=1 mas c_f²=ξ²/r²; G e M não são simultaneamente diagonalizáveis, então a combinação massless só tem c=1 exato se ξ=r — declarar o regime antes de invocar GW170817)", False),
 ("C11", r"$m_T^2 \ge 2H^2$", "—", "CONFERE (importada: Higuchi; usar m_T²(ξ) — âncora D2)", False),
 ("C11", r"$m_T^2 < 2H^2$", "—", "CONFERE (condicional)", False),
 ("C11", r"h_k'' + 2\frac{a'}{a} h_k'", "—", "CONFERE (forma em tempo conforme; a mudança de tempo não é declarada — mesma nota do Cap.10 §10.3)", False),
 ("C11", r"Se m_T \ll H", "—", "ARTEFATO DE CONVERSÃO (prosa dentro de $)", False),
 ("C11", r"Se m_T \gg H", "—", "ARTEFATO DE CONVERSÃO (prosa dentro de $)", False),
 ("C11", r"r = \frac{P_T}{P_\zeta}", "—", "CONFERE (definição padrão); SOBRECARGA GRAVE: r aqui é tensor-to-scalar ratio, r=b/a é a variável estrutural central — renomear um dos dois", False),
 ("C11", r"P_T = P_{T,0} + P_{T,m}", "—", "CONFERE (decomposição declarada)", False),
 ("C11", r"P_{T,m} \approx 0", "—", "CONFERE SOB HIPÓTESE (modo massivo pesado no primordial)", False),
 ("C11", r"r \approx r_{\text{inflaton-like}}", "—", "CONFERE SOB HIPÓTESE (mesma sobrecarga de r)", False),
 ("C11", r"h_m \sim e^{-m_T t}", "—", "ERRO DE CÁLCULO: para m_T≫H o modo massivo OSCILA com envelope a^{−3/2} (número de ocupação conservado), não decai como e^{−m_T t}; correção: h_m ∝ a^{−3/2}cos(m_T t+φ₀)", False),
 ("C11", r"10^{-23}", "—", "CONFERE (importada: limite observacional de massa do gráviton)", False),
 # ================= C12 =================
 ("C12", r"\frac{1}{\Delta H} \ln r", "Cap.1 §1.7; Cap.10 §10.6", "INCOMPLETA (ΔH não definido; TERCEIRA fórmula heurística de tempo relacional do corpus — T=f(H₁−H₂) no Cap.1, τ~ln σ no Cap.10, t~(1/ΔH)ln r aqui — nunca unificadas nem derivadas)", False),
 # ================= C13 =================
 ("C13", r"\beta_n\, e_n(\mathcal{K})", "Cap.3 §3.3", "CONFERE (reprise da estrutura HR)", False),
 ("C13", r"f_{\mu\nu} = c^2\, g_{\mu\nu}", "—", "CONFERE (ramo proporcional: √(g⁻¹f)=c·I ⇒ r=ξ=c)", False),
 ("C13", r"3\beta_2 c^2+\beta_3 c^3", "ramo proporcional acima", "CONFERE (âncora D3: forma correta com F(φ))", False),
 ("C13", r"$S \neq 0", "—", "CONFERE (condição inicial multifield)", False),
 ("C13", r"3H\dot S + m_S^2 S = 0", "—", "CONFERE SOB HIPÓTESE (mecanismo de isocurvatura pesada, esquemático; o m_S real do setor relativo não é o do Cap.15 — âncora D1)", False),
 ("C13", r"e^{-m_S t}", "eq. de S acima", "ERRO DE CÁLCULO: com m_S≫H a solução oscila com envelope a^{−3/2}; NÃO há fator de decaimento e^{−m_S t}; correção: S ∝ a^{−3/2}cos(m_S t+φ₀) — a supressão observacional vem da diluição/média, não de decaimento exponencial", False),
 ("C13", r"P_S}{P_\zeta}", "—", "CONFERE (condição observacional de projeto)", False),
 ("C13", r"$m_T^2 \ge 2H^2.$", "—", "CONFERE (importada: Higuchi; âncora D2)", False),
 ("C13", r"m_T^2(a) = m^2\,\mathcal{F}", "—", "CONFERE (definição de massa dinâmica; a forma real de 𝓕 está na âncora D2 e inclui ξ; NOTA: 𝓕 é mais uma variante do símbolo F — unificar)", False),
 ("C13", r"\frac{\dot{\beta}_n}{\beta_n}", "Cap.6.2 §6.10", "CONFERE (reprise da adiabaticidade)", False),
 # ================= C14 =================
 ("C14", r"S_m[g,\psi] + S_\phi", "Cap.3 §3.2", "CONFERE (ação HR completa com matéria e setor φ explícitos — base validada das Derivações)", False),
 ("C14", r"\beta_n\,e_n(\mathcal{K})", "ação acima", "CONFERE (reprise)", False),
 ("C14", r"V \rightarrow F(\phi)\,V", "Cap.3 §3.8", "CONFERE (postulado reprise; a nota do texto — F global mais controlável que β_n(φ) — é correta e coerente com a âncora D5 §4.1)", False),
 ("C14", r"ds_g^2=-N_g^2(t)dt^2", "Cap.5 §5.1", "CONFERE (reprise)", False),
 ("C14", r"\xi(t)=\frac{N_f}{N_g}", "ansatz acima", "CONFERE (definições COM lapses — sana a pendência de H_f do Cap.5 §5.4)", False),
 ("C14", r"{\rm diag}(\xi,r,r,r)", "K (Cap.3 §3.3)", "CONFERE — verificada (auto-teste); flag sem-delimitador", False),
 ("C14", r"e_1=\xi+3r,\quad", "K diagonal acima", "CONFERE — verificados (auto-teste)", False),
 ("C14", r"+\beta_4(\xi r^3)", "e_n acima", "CONFERE", False),
 ("C14", r"V(\xi,r,\phi)=F(\phi)", "modulação acima", "CONFERE (definição)", False),
 ("C14", r"\rho_m + \rho_\phi + \rho_{\rm int}^{(g)}(r,\phi)", "ação acima", "CONFERE (Friedmann-g com setor φ — âncora D3/F.3)", False),
 ("C14", r"= \rho_f + \rho_{\rm int}^{(f)}(r,\phi)", "ação acima", "CONFERE (F.4; NOTA: ρ_f de matéria no setor f não existe no resto da teoria — placeholder a declarar)", False),
 ("C14", r"3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3\Big)", "V(ξ,r) acima", "CONFERE — âncora D3 (forma correta com F(φ), sem β₄, sem ξ — confirmada pela regra da cadeia completa)", False),
 ("C14", r"3\beta_3 r^{-1}", "V(ξ,r) acima", "CONFERE — âncora D3/F.4", False),
 ("C14", r"\big(H_g-\xi H_f\big)=0", "Friedmanns acima", "CONFERE (constraint de Bianchi — âncora D5; pressupõe Q≡0, ver achado A1)", False),
 ("C14", r"r=r_\star=\text{const.}", "constraint acima", "CONFERE (ramo algébrico)", False),
 ("C14", r"r(t)\ \text{evolui}", "constraint acima", "ERRO na legenda: a implicação 'H_g=ξH_f ⇒ r(t) evolui' é falsa — a PRÓPRIA §14.11 deste capítulo deriva ṙ=0 dessa condição (âncora D5)", False),
 ("C14", r"c^2 g_{\mu\nu}\quad\Rightarrow\quad r=c,\ \xi=c", "—", "CONFERE (proporcional com ξ=c explícito — mais completo que o Cap.13)", False),
 ("C14", r"\Big(\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3\Big)", "proporcional acima", "CONFERE (âncora D3)", False),
 ("C14", r"w_{\rm eff}\approx -1", "—", "CONFERE SOB HIPÓTESE (F lento; esquemática)", False),
 ("C14", r"\dot H_g + H_g^2 > 0", "—", "CONFERE (identidade ä/a e condição de aceleração)", False),
 ("C14", r"p_{\rm DE}^{\rm eff}\equiv", "—", "CONFERE (definições; p_int^(g) 'derivável do tensor de interação' nunca é derivado no corpus — pendência)", False),
 ("C14", r"3p_{\rm DE}^{\rm eff} < 0", "definições acima", "CONFERE (condição de aceleração padrão)", False),
 ("C14", r"k/a\gg m_{\rm screen}", "—", "CONFERE (requisito de projeto; flag sem-delimitador); NOTA âncora D6: o μ derivado satisfaz μ→1 em k→∞ AUTOMATICAMENTE (α_∞=0) — o requisito vale sem ajuste, ao contrário do que o Cap.18 assume", False),
 ("C14", r"m_T^2(\beta_n,r,\phi)\ \ge\ 2H^2", "—", "CONFERE (Higuchi como restrição; usar m_T²(ξ) — âncora D2)", False),
 ("C14", r"0<r_{\min}", "—", "CONFERE (requisito de regularidade)", False),
 ("C14", r"não deve cruzar", "—", "CONFERE (qualitativa)", False),
 ("C14", r"(\beta_0,\beta_1,0,\beta_3,\beta_4)", "—", "CONFERE (definição da família F2)", False),
 ("C14", r"(\beta_0,\beta_1,\beta_2,0,\beta_4)", "—", "CONFERE (definição/reprise da família F1)", True),
 ("C14", r"\Big(\beta_0+3\beta_1r+3\beta_2r^2\Big)", "F1 acima", "CONFERE (âncora D3, β₃=0)", False),
 ("C14", r"\Big(\beta_4+3\beta_2r^{-2}+\beta_1r^{-3}\Big)", "F1 acima", "CONFERE (F.4, β₃=0)", False),
 ("C14", r"U(r)\equiv \beta_0+3\beta_1r+3\beta_2r^2", "F1 acima", "CONFERE (definições U, Ũ); SOBRECARGA: U(r) colide com U(χ)/U(φ) potencial do campo nos Anexos B–H — renomear", False),
 ("C14", r"F(\phi)\,U(r), \qquad", "definições acima", "CONFERE", False),
 ("C14", r"r+\beta_3r^2)(H_g-\xi H_f)", "—", "CONFERE (reprise da constraint)", False),
 ("C14", r"e com \beta_3=0", "—", "ARTEFATO DE CONVERSÃO (prosa dentro de $)", False),
 ("C14", r"r_\star=-\frac{\beta_1}{2\beta_2}}", "constraint F1 acima", "CONFERE (âncora D5/F.6)", False),
 ("C14", r"r_\star>0\ \Rightarrow", "r★ acima", "CONFERE (condição de existência física)", False),
 ("C14", r"\boxed{H_g=\xi H_f.}", "constraint acima", "CONFERE como definição do ramo (com ṙ≡0 — §14.11/âncora D5)", False),
 ("C14", r"\xi\left(\frac{1}{\xi}\frac{\dot b}{b}\right)", "definições §14.2", "CONFERE — âncora D5: cancelamento de ξ correto (verificado em sympy)", False),
 ("C14", r"\ln\left(\frac{b}{a}\right)=0", "equação acima", "CONFERE — âncora D5: ṙ=0 é o resultado CORRETO do ramo dinâmico (esta é a derivação certa do capítulo)", False),
 ("C14", r"(\dot r - (\xi-1)Hr)=0", "—", "ERRO: forma 'alternativa' da constraint introduzida sem derivação — âncora D5 §3.3 prova que ela NÃO é equivalente à constraint de Bianchi (coincide só se ξ=1); é a origem da inconsistência do capítulo", False),
 ("C14", r"H_b \equiv \frac{\dot b}{b}", "—", "CONFERE (definição auxiliar legítima)", False),
 ("C14", r"H_f = \frac{1}{N_f}\frac{\dot b}{b}=\frac{H_b}{\xi}", "definições acima", "CONFERE (identidade)", False),
 ("C14", r"(H_b-\xi H_g)=0 }", "—", "ERRO — âncora D5 §3.3: (H_b−ξH_g) NÃO é a constraint de Bianchi ((H_g−ξH_f) traduz-se em H_g=H_b, não H_b=ξH_g); troca silenciosa e não-equivalente", False),
 ("C14", r"(\beta_1+2\beta_2r)\,(H_b-\xi H_g)", "—", "ERRO (idem, versão F1)", False),
 ("C14", r"\boxed{H_b=\xi H_g}", "—", "ERRO — âncora D5: condição não derivada e incompatível com a constraint original (exceto ξ=1)", False),
 ("C14", r"r(H_b-H_g)=r(\xi-1)H_g", "—", "ERRO na 2ª igualdade: ṙ=r(H_b−H_g) é cinemática correta, mas usar H_b=ξH_g (inválida) dá o resultado errado; com a constraint correta, ṙ=0 (âncora D5)", False),
 ("C14", r"\dot r = r(\xi-1)H_g. }", "—", "ERRO (âncora D5: no ramo dinâmico real, ṙ≡0; este resultado não deve ser mantido)", False),
 ("C14", r"3M_f^2H_f^2=\rho_f+\rho_{\rm int}", "F.4", "CONFERE (reprise)", False),
 ("C14", r"H_f=\frac{H_g+\dot r/r}{\xi}", "identidades acima", "CONFERE (cinemática)", False),
 ("C14", r"\boxed{H_f=H_g.}", "—", "ERRO — consequência de H_b=ξH_g (inválida); com a constraint correta, H_f=H_g/ξ", False),
 ("C14", r"3M_f^2H_g^2=\rho_f+m^2", "—", "ERRO (herda H_f=H_g; a forma correta é 3M_f²(H_g/ξ)²=ρ_f+m²M_eff²FŨ(r) — é a F.4)", False),
 ("C14", r"3M_g^2H_g^2=\rho_m+\rho_\phi+m^2", "F.3", "CONFERE (Friedmann-g correta)", False),
 ("C14", r"3(M_g^2-M_f^2)H_g^2", "—", "ERRO (subtração de uma equação inválida — refazer com H_f=H_g/ξ)", False),
 ("C14", r"U(r_\star)+\rho_\phi(a)", "baseline algébrico", "CONFERE (consistente com a via da raiz móvel — âncora D5 §4.1)", False),
 ("C14", r"$\boxed{\beta_1\beta_2<0.}$", "r★>0", "CONFERE (reprise)", False),
 ("C14", r"(r_\star)=m^2M_{\rm eff}^2F(\phi)\,U(r_\star)", "—", "CONFERE", False),
 ("C14", r"U(r_\star)>0 \quad \text{(assumindo", "—", "CONFERE (condição)", False),
 ("C14", r"Com r_\star=-\beta_1/(2\beta_2):", "—", "ARTEFATO DE CONVERSÃO (prosa dentro de $)", False),
 ("C14", r"-\frac{3\beta_1^2}{2\beta_2}", "r★ acima", "CONFERE (conta verificada: U(r★)=β₀−3β₁²/(4β₂) ✓)", False),
 ("C14", r"\beta_0-\frac{3\beta_1^2}{4\beta_2}>0. }", "conta acima", "CONFERE (condição derivada corretamente)", False),
 ("C14", r"3M_f^2H_g^2-\rho_f = m^2", "—", "ERRO: 'no ramo proporcional H_f=H_g' é falso — com f=c²g, H_f=H_g/c; a equação precisa do fator c² (e para c=r★ genérico não some)", False),
 ("C14", r"não deve forçar }H_g^2<0", "—", "CONFERE (requisito qualitativo; equação subjacente a corrigir — entrada anterior)", False),
 ("C14", r"\tilde U(r)=\beta_4+3\beta_2r^{-2}", "—", "CONFERE (reprise definição)", False),
 ("C14", r"H^2(z)\approx", "—", "CONFERE (aproximação declarada)", False),
 ("C14", r"\approx 3M_g^2H_0^2-\rho_{m0}", "—", "CONFERE (normalização; fixa m²M_eff²U(r★))", False),
 ("C14", r"4\beta_2}>0,\qquad", "—", "CONFERE (reprise do conjunto fechado de restrições)", False),
 ("C14", r"após a fase primordial", "—", "CONFERE (requisito; o 'm_S²' real do setor relativo não é m²F(β₁+2β₂r) — âncora D1)", False),
 # ================= C15 =================
 ("C15", r"$(\beta_0,\beta_1,\beta_2,0,\beta_4)$", "Cap.14 §14.7", "CONFERE (reprise F1)", False),
 ("C15", r"2a\partial_i B_g dx^i dt", "Cap.6.2", "CONFERE (ansatz escalar completo do setor g)", False),
 ("C15", r"2\xi b\partial_i B_f", "Cap.6.2", "CONFERE (ansatz setor f)", False),
 ("C15", r"\phi(t) \rightarrow \phi(t) + \delta\phi", "—", "CONFERE", False),
 ("C15", r"\frac{\rho_g \Psi_g + \rho_f \Psi_f}{\rho_g + \rho_f}", "—", "INCOMPLETA + sobrecarga: ρ_g,ρ_f não definidos no capítulo; e esta é a TERCEIRA definição de ζ no corpus (curvatura efetiva no Cap.6.2, δρ/(ρ+p) no Cap.10, média ponderada aqui) — unificar", False),
 ("C15", r"S \propto \Psi_f - \Psi_g", "—", "CONFERE (definição do modo relativo)", False),
 ("C15", r"\dot{\vec Q}^T K \dot{\vec Q}", "ansatz acima", "CONFERE (estrutura; matrizes reais na âncora D1)", False),
 ("C15", r"Q_\zeta \\ Q_S", "—", "CONFERE (base 2D; flag sem-delimitador); NOTA: 2 modos aqui vs 3 no Cap.6.2 §6.4 — a tensão de contagem (âncora D1: 3 na análise congelada) vive também entre Cap.15 e Cap.6.2", False),
 ("C15", r"\det(K) > 0, \quad {\rm Tr}(K) > 0", "—", "CONFERE (condição de positividade 2×2)", False),
 ("C15", r"M_{\rm eff}^2 \left(\beta_1 + 2\beta_2 r\right) > 0", "—", "ERRO — âncora D1: a condição no-ghost NÃO se reduz a β₁+2β₂r>0 (par com cinética negativa presente no ramo dinâmico em AMBOS os lados da raiz; no ramo algébrico o par degenera). Não deve ser mantida", False),
 ("C15", r"U(r)=\beta_0+3\beta_1 r+3\beta_2 r^2", "Cap.14 §14.9", "CONFERE (reprise; mesma sobrecarga U(r) vs U(φ))", False),
 ("C15", r"\frac{dU}{dr}=3\beta_1+6\beta_2 r", "U(r) acima", "CONFERE (derivada correta)", False),
 ("C15", r"m_S^2 \sim m^2 F(\phi)\, \left(\beta_1+2\beta_2 r\right)", "—", "ERRO — âncora D1: nenhuma massa do espectro real segue essa proporcionalidade (massas O(1), setor relativo taquiônico no ramo dinâmico); a estrutura correta está em derivations/code/out/01_matrices.txt", False),
 ("C15", r"m_S^2 \propto \beta_1+2\beta_2 r. }", "—", "ERRO (idem âncora D1)", False),
 ("C15", r"\frac{P_S}{P_\zeta} \ll 1", "—", "CONFERE (condição observacional)", False),
 ("C15", r"$\boxed{ m_S^2 \gg H^2 }$", "—", "CONFERE (condição de supressão, dado um m_S real)", False),
 ("C15", r"a^{-3/2} e^{-m_S t}", "—", "ERRO DE CÁLCULO (mesmo do Cap.13 §2: modo pesado oscila com envelope a^{−3/2}; não há decaimento e^{−m_S t}; correção: S∝a^{−3/2}cos(m_S t+φ₀))", False),
 ("C15", r"\left(\beta_1+2\beta_2 r\right) \gg H^2. } $$", "—", "ERRO (herda a fórmula de m_S² refutada — âncora D1; reformular a condição de supressão com a massa real)", False),
 ("C15", r"r_\star=-\frac{\beta_1}{2\beta_2}.$", "Cap.14 §14.10", "CONFERE (reprise)", False),
 ("C15", r"= 2\beta_2 (r-r_\star)", "r★ acima", "CONFERE (álgebra correta)", False),
 ("C15", r"m_S^2 \propto 2\beta_2 (r-r_\star)", "—", "ERRO (herda âncora D1; a degenerescência na raiz é real — benchmark C — mas é CINÉTICA, não de massa)", False),
 ("C15", r"$\beta_1+2\beta_2 r > 0.$", "—", "ERRO (como condição no-ghost — âncora D1: refutada nos dois lados da raiz)", False),
 ("C15", r"m^2 F(\phi)(\beta_1+2\beta_2 r) \gg H^2.$", "—", "ERRO (reprise da condição herdada)", False),
 ("C15", r"\beta_0-\frac{3\beta_1^2}{4\beta_2}>0", "Cap.14 §14.16", "CONFERE (reprise das condições de fundo)", False),
 ("C15", r"$\beta_1+2\beta_2 r.$", "—", "CONFERE como expressão isolada; NOTA: o papel de 'fator estrutural único' caiu — no tensor o fator real é β₁+β₂(ξ+r) (âncora D2) e no escalar a saúde não é decidida por ele (âncora D1)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("C11", "C12", "C13", "C14", "C15")
    textos = {}
    for pref in arquivos:
        with open(os.path.join(REG, pref + ".md"), encoding="utf-8") as fh:
            textos[pref] = re.split(r"(?=### \[)", fh.read())
    for pref, key, dep, ver, multi in V:
        blocos = textos[pref]
        hits = [i for i, b in enumerate(blocos)
                if b.startswith("### [") and key in b and "_(pendente)_" in b]
        if not hits:
            problemas.append(f"{pref}: '{key[:45]}' -> 0 pendentes")
            continue
        if len(hits) > 1 and not multi:
            problemas.append(f"{pref}: '{key[:45]}' -> {len(hits)} blocos")
            continue
        for i in hits:
            b = blocos[i]
            b = b.replace("- **Depende de:** _(a preencher)_",
                          f"- **Depende de:** {dep}")
            b = b.replace("- **Veredito:** _(pendente)_",
                          f"- **Veredito:** {ver}")
            blocos[i] = b
            aplicados += 1
    for pref in arquivos:
        texto = "".join(textos[pref])
        with open(os.path.join(REG, pref + ".md"), "w", encoding="utf-8") as fh:
            fh.write(texto)
        print(f"{pref}: {texto.count('_(pendente)_')} pendentes")
    print(f"\naplicados: {aplicados}")
    for p in problemas:
        print("  -", p)


if __name__ == "__main__":
    main()
