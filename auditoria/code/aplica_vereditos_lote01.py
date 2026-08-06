# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote01.py — aplica os vereditos do Lote 1 (C01–C05)
aos registros, casando cada veredito por SUBSTRING DA FORMULA (robusto
a renumeracao de IDs). Reporta chaves nao casadas / ambiguas e entradas
que restarem pendentes.

Uso: python aplica_vereditos_lote01.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

# (arquivo, chave-substring-da-formula, depende, veredito)
V = [
 # ---------------- C01 ----------------
 ("C01", r"G_{\mu\nu} + \Lambda g_{\mu\nu}", "—",
  "CONFERE (importada: equação de Einstein com Λ, forma padrão)"),
 ("C01", r"\rho_\Lambda = \frac{\Lambda}", "eq. de Einstein acima",
  "CONFERE (importada: identificação padrão do ΛCDM)"),
 ("C01", r"10^{120}", "—",
  "CONFERE SOB HIPÓTESE (estimativa padrão com cutoff de Planck; o expoente citado varia entre ~60 e ~123 conforme o cutoff — declarar a convenção)"),
 ("C01", r"\Phi_1 \quad \text{e}", "—",
  "CONFERE (introdução de notação)"),
 ("C01", r"\Phi_+ = \frac{\Phi_1 + \Phi_2}", "Φ₁, Φ₂ acima",
  "CONFERE (rotação ortonormal padrão)"),
 ("C01", r"m_-^2 = \left", "Φ± acima",
  "CONFERE SOB HIPÓTESE (critério taquiônico padrão; V(Φ) nunca é especificado no corpus — a existência de V com m₋²<0 permanece hipótese)"),
 ("C01", r"\dot{\eta} = \Gamma (H_1 - H_2)^2", "—",
  "POSTULADO registrado; CONFLITA COM Anexo E §E.3(4)/Anexo H Postulado 5 (η̇=Γχ̇²: mesma variável η com lei diferente e Γ dimensionalmente incompatível — aqui [Γ]=tempo, lá não); H₁,H₂ só ganham definição formal no Cap.5"),
 ("C01", r"\frac{\rho}{1 - \eta}", "η̇ acima",
  "NÃO-DERIVÁVEL da ação (âncora D4) — reclassificar como extensão proposta (acoplamento não-mínimo + regime adiabático |η̇|≪H); manter o hedge 'pode modificar' e citar a Derivação 4"),
 ("C01", r"1 + \eta + \eta^2", "Friedmann com 1/(1−η) acima",
  "CONFERE (série geométrica; válida para |η|<1)"),
 ("C01", r"T(x^\mu) = f(H_1 - H_2)", "η̇ acima",
  "INCOMPLETA (f não especificada — definição heurística sem conteúdo verificável; em fundo homogêneo o lado direito independe de x, contradizendo a notação T(x^μ))"),
 # ---------------- C02 ----------------
 ("C02", r"$\phi(x)$", "—",
  "CONFERE (introdução de notação)"),
 ("C02", r"S_\phi = \int", "—",
  "CONFERE (importada: ação escalar mínima padrão; sinais corretos na assinatura −+++)"),
 ("C02", r"\phi_1(x), \quad \phi_2(x)", "φ(x) acima",
  "CONFERE (notação; NOTA: minúsculas φ₁,φ₂ aqui vs maiúsculas Φ₁,Φ₂ no Cap.1 §1.4 — unificar caixa)"),
 ("C02", r"\Phi_+ = \frac{\phi_1 + \phi_2}", "φ₁,φ₂ acima; Cap.1 §1.4",
  "CONFERE (repete a rotação do Cap.1 com a troca de caixa φ/Φ — unificar)"),
 ("C02", r"m_-^2 < 0", "Φ± acima; Cap.1 §1.4",
  "CONFERE SOB HIPÓTESE (idem Cap.1: V nunca especificado)"),
 ("C02", r"S = S_{\text{grav}}", "—",
  "CONFERE (decomposição esquemática bem-formada)"),
 ("C02", r"S_{\text{grav}} = \frac{1}{16\pi G}", "—",
  "CONFERE (importada: Einstein–Hilbert padrão; consistente com M²=1/(8πG) usado adiante)"),
 ("C02", r"H^\dagger H", "Φ₋ acima",
  "CONFERE como proposta (portal escalar dim-4, gauge-invariante; fenomenologia não auditada neste lote)"),
 ("C02", r"g_{\mu\nu}, \quad f_{\mu\nu}.$", "—",
  "CONFERE (introdução de notação)"),
 ("C02", r"S_{\text{int}}(g,f,\phi)", "g,f acima; S_grav acima",
  "CONFERE (estrutura; S_int só é especificada no Cap.3 §3.2 — referência adiantada inofensiva)"),
 ("C02", r"\eta(t) = \int^t \Gamma", "Cap.1 §1.6 (η̇)",
  "CONFERE como integral do postulado do Cap.1; herda o CONFLITO com Anexo E/H (lei η̇=Γχ̇²) e a pendência dimensional de Γ; usa H_g,H_f antes da definição formal (Cap.5)"),
 ("C02", r"H_g^2 = \frac{8\pi G}{3} \frac{\rho}{1-\eta}", "η(t) acima",
  "NÃO-DERIVÁVEL da ação (âncora D4) — mesma reclassificação da ocorrência no Cap.1 §1.6"),
 # ---------------- C03 ----------------
 ("C03", r"g_{\mu\nu} \quad \text{e} \quad f_{\mu\nu}", "Cap.2 §2.6",
  "CONFERE (notação)"),
 ("C03", r"V(\mathcal{K}) + S_{\text{matter}}", "Cap.2 §2.6 (estrutura)",
  "CONFERE (importada: ação Hassan–Rosen; é a base validada de todas as Derivações — o minisuperespaço desta ação reproduz F.1, auto-teste da biblioteca)"),
 ("C03", r"\mathcal{K} = \sqrt{g^{-1}f}.$", "ação HR acima",
  "CONFERE (raiz principal; construída ordem a ordem via Sylvester nas Derivações 1–2)"),
 ("C03", r"\sum_{n=0}^4 \beta_n e_n(\mathcal{K})", "K acima",
  "CONFERE (importada: estrutura dRGT/HR; e_n verificados no fundo — auto-teste da biblioteca)"),
 ("C03", r"m^2 V_{\mu\nu}^{(g)} = \frac{1}{M_g^2}", "ação HR acima",
  "INCOMPLETA (V_{μν}^{(g)} nunca é definido; com a definição padrão o prefator seria m²M_eff²/M_g², não m² — declarar a normalização absorvida)"),
 ("C03", r"m^2 V_{\mu\nu}^{(f)} = 0.$", "ação HR acima",
  "INCOMPLETA (idem; e a variação em f carrega o fator √−g/√−f dentro de V^{(f)} — não declarado)"),
 ("C03", r"f_{\mu\nu} \rightarrow g_{\mu\nu}", "—",
  "CONFERE (limite bem-definido)"),
 ("C03", r"\mathcal{K} \rightarrow I", "limite f→g acima; K",
  "CONFERE"),
 ("C03", r"m_g^2 \ge 2H^2", "—",
  "CONFERE (importada: bound de Higuchi em de Sitter); NOTA (âncora D2): as aplicações posteriores usam m_T² sem a dependência em ξ — refazer com a forma da Derivação 2"),
 ("C03", r"\beta_n \rightarrow \beta_n(\phi)", "V(K) acima",
  "POSTULADO registrado; a preservação do caráter ghost-free é afirmada mas não demonstrada (Anexo C §C.11 sem suporte — âncora D1)"),
 # ---------------- C04 ----------------
 ("C04", r"\nabla^\mu G_{\mu\nu} = 0", "—",
  "CONFERE (importada: identidade de Bianchi)"),
 ("C04", r"G_{\mu\nu} = 8\pi G T_{\mu\nu}", "Cap.1 §1.1",
  "CONFERE (GR sem Λ como referência)"),
 ("C04", r"\nabla^\mu T_{\mu\nu} = 0.$", "Bianchi + eq. de Einstein acima",
  "CONFERE"),
 ("C04", r"m^2 V_{\mu\nu}^{(g)} = \frac{1}{M_g^2}", "Cap.3 §3.4",
  "CONFERE (reprise do Cap.3; herda a INCOMPLETUDE de normalização registrada lá)"),
 ("C04", r"G_{\mu\nu}[f] + m^2 V_{\mu\nu}^{(f)} = 0", "Cap.3 §3.4",
  "CONFERE (reprise; idem)"),
 ("C04", r"G_{\mu\nu}[g] + m^2 \nabla_g^\mu", "eq. bimétrica g acima",
  "CONFERE (divergência aplicada corretamente)"),
 ("C04", r"\nabla_g^\mu G_{\mu\nu}[g] = 0", "Bianchi",
  "CONFERE"),
 ("C04", r"$$ m^2 \nabla_g^\mu V", "duas equações acima",
  "CONFERE"),
 ("C04", r"V_{\mu\nu}^{(g)} \neq 0", "equação acima",
  "CONFERE (condicional); ver o conflito registrado na identidade √−g∇V abaixo"),
 ("C04", r"\nabla_g^\mu T_{\mu\nu} \neq 0", "condicional acima",
  "CONFERE (condicional)"),
 ("C04", r"T_{\mu\nu} = Q_\nu", "equação m²∇V=∇T/M_g² acima",
  "CONFERE (definição de Q_ν)"),
 ("C04", r"G_{\mu\nu}[f] + m^2 \nabla_f^\mu", "eq. bimétrica f acima",
  "CONFERE"),
 ("C04", r"\nabla_f^\mu G_{\mu\nu}[f] = 0", "Bianchi",
  "CONFERE"),
 ("C04", r"\nabla_f^\mu V_{\mu\nu}^{(f)} = 0.$", "duas equações acima",
  "CONFERE (segue on-shell da eq. do setor f) — mas ver o conflito na entrada seguinte"),
 ("C04", r"= - \sqrt{-f}", "identidade tipo-HR; ∇_fV^{(f)}=0 acima",
  "CONFERE como identidade — PORÉM combinada com ∇_fV^{(f)}=0 implica ∇_gV^{(g)}≡0 e portanto Q_ν≡0 on-shell: CONFLITA COM a narrativa de troca de energia (§4.3, §4.6). É exatamente a conservação separada que o Cap.5 §5.5 usa para derivar a constraint de Bianchi — o corpus precisa escolher: ou há troca (Cap.4) ou há a constraint (Cap.5); com acoplamento mínimo, o correto padrão é Q≡0"),
 ("C04", r"Q_\nu = -Q_\nu^{(f)}", "identidade acima",
  "CONFERE (com ambos os lados nulos pelo conflito acima; Q^{(f)} é usado sem definição prévia)"),
 ("C04", r"m^2 V_{\mu\nu}.$", "—",
  "ARTEFATO DE CONVERSÃO (fragmento de expressão isolado, não é equação)"),
 ("C04", r"diag(-\rho, p, p, p)", "—",
  "CONFERE (importada: fluido perfeito comóvel)"),
 ("C04", r"3H(\rho + p) = Q_0", "definição de Q_ν; T=diag acima",
  "CONFERE formalmente (componente 0 de ∇T=Q); com Q₀≡0 pelo conflito da identidade √−g∇V, as consequências físicas de §4.6 ficam sem fonte"),
 ("C04", r"Se Q_0 > 0", "—",
  "ARTEFATO DE CONVERSÃO (prosa dentro de $)"),
 ("C04", r"Se Q_0 < 0", "—",
  "ARTEFATO DE CONVERSÃO (prosa dentro de $)"),
 ("C04", r"(T_{\mu\nu}^{(g)} + T_{\mu\nu}^{(f)})", "—",
  "ERRO DE FORMULAÇÃO: expressão mal-definida — soma tensores associados a métricas diferentes sob um único ∇ não especificado, e T^{(f)} (matéria do setor f) não existe na teoria (matéria acopla só a g). Reformular como enunciado próprio de conservação bimétrica ou remover"),
 ("C04", r"\beta_n \rightarrow \beta_n(\phi)", "Cap.3 §3.8",
  "CONFERE (reprise)"),
 ("C04", r"\Box \phi - V'(\phi) = \mathcal{S}(g,f)", "β_n(φ) acima",
  "INCOMPLETA (a fonte S(g,f) nunca é definida); ATENÇÃO ao sinal quando for definida: pela ação, a fonte é −m²M_eff²(∂_φF)V — mesmo erratum do Anexo E §E.3(3) (Derivações 2/8)"),
 # ---------------- C05 ----------------
 ("C05", r"-dt^2 + a^2(t)\,\delta_{ij}", "—",
  "CONFERE (importada: FLRW plano)"),
 ("C05", r"g_{\mu\nu}, \quad f_{\mu\nu}.$", "Cap.2 §2.6",
  "CONFERE (notação)"),
 ("C05", r"ds_g^2 = -N_g^2(t)", "FLRW acima",
  "CONFERE (ansatz homogêneo/isotrópico com lapse; 'forma mais geral' vale a menos de shift, nulo por isotropia)"),
 ("C05", r"ds_f^2 = -N_f^2(t)", "ansatz g acima",
  "CONFERE (idem)"),
 ("C05", r"r(t) = \frac{b(t)}{a(t)}", "ansätze acima",
  "CONFERE (definição)"),
 ("C05", r"\mathcal{K} = \sqrt{g^{-1}f}.$", "Cap.3 §3.3",
  "CONFERE (reprise)"),
 ("C05", r"diag(\xi, r, r, r)", "K acima; ξ abaixo",
  "CONFERE — verificada explicitamente (auto-teste da biblioteca: raiz por Sylvester no fundo); NOTA: usa ξ uma linha antes da definição — reordenar"),
 ("C05", r"\xi = \frac{N_f}{N_g}", "ansätze acima",
  "CONFERE (definição)"),
 ("C05", r"e_0 = 1", "K diagonal acima",
  "CONFERE — verificado (auto-teste)"),
 ("C05", r"e_1 = \xi + 3r", "K diagonal acima",
  "CONFERE — verificado (auto-teste)"),
 ("C05", r"e_2 = 3\xi r + 3r^2", "K diagonal acima",
  "CONFERE — verificado (auto-teste)"),
 ("C05", r"e_3 = 3\xi r^2 + r^3", "K diagonal acima",
  "CONFERE — verificado (auto-teste)"),
 ("C05", r"e_4 = \xi r^3", "K diagonal acima",
  "CONFERE — verificado (auto-teste)"),
 ("C05", r"V(\xi,r) = \sum", "e_n acima",
  "CONFERE"),
 ("C05", r"3M_g^2 H_g^2 = \rho_m + \rho_{\text{int}}", "ação HR (Cap.3 §3.2); gauge N_g=1 (§5.1)",
  "CONFERE (Friedmann-g; forma validada — âncora D3/F.3; setor escalar χ ausente porque a modulação só entra em §5.7)"),
 ("C05", r"H_g = \frac{\dot a}{a}", "gauge N_g=1 (§5.1)",
  "CONFERE (definição no gauge declarado)"),
 ("C05", r"\rho_{\text{int}} = m^2 M_{\text{eff}}^2 \left( \beta_0", "V(ξ,r) acima",
  "CONFERE — âncora D3: exatamente a forma correta (sem β₄ e sem ξ), confirmada pela regra da cadeia completa"),
 ("C05", r"3M_f^2 H_f^2 = m^2", "V(ξ,r) acima",
  "CONFERE — âncora D3/F.4; NOTA: H_f usado sem definição no capítulo (H_f≡ḃ/(N_f b)) — declarar"),
 ("C05", r"(H_g - \xi H_f) = 0", "Friedmanns acima",
  "CONFERE (constraint de Bianchi padrão — âncora D5); PRESSUPÕE conservação separada (Q≡0): CONFLITA COM a narrativa de troca do Cap.4 §§4.3–4.6 — reconciliar os dois capítulos"),
 ("C05", r"\beta_1 + 2\beta_2 r + \beta_3 r^2 = 0", "constraint acima",
  "CONFERE (definição do ramo algébrico)"),
 ("C05", r"H_g = \xi H_f.$", "constraint acima",
  "CONFERE como definição do ramo; a afirmação 'aqui r(t) evolui dinamicamente' é ERRO — âncora D5: neste ramo ṙ≡0 exatamente; r(t) genuíno exige raiz móvel β_n(φ)"),
 ("C05", r"-\frac{4\pi G}{3}(\rho + 3p)", "Friedmann-g acima",
  "CONFERE SOB HIPÓTESE (forma esquemática; os 'termos de interação' são deriváveis — equações de aceleração derivadas na biblioteca das Derivações)"),
 ("C05", r"\beta_n \rightarrow \beta_n(\phi)", "Cap.3 §3.8",
  "CONFERE (reprise)"),
 ("C05", r"\rho_{\text{int}} = F(\phi,r)", "ρ_int acima; β_n(φ)",
  "INCOMPLETA + sobrecarga de símbolo: F(φ,r) genérica aqui vs F(χ) multiplicativa dos anexos — unificar (a forma real é ρ_int=m²M_eff²F(φ)(β₀+3β₁r+3β₂r²), âncora D3)"),
 ("C05", r"\frac{\partial V_{\text{int}}}{\partial \phi}", "β_n(φ) acima",
  "ERRO DE CÁLCULO (sinal, provável): pela ação, com V_int como densidade de energia de interação, a fonte no RHS é −∂V_int/∂φ (mesmo erratum do Anexo E §E.3(3), verificado por Euler–Lagrange nas Derivações); além disso V_int não é definida no capítulo"),
 ("C05", r"\eta(t) \sim \int (H_g - H_f)^2", "Cap.2 §2.7",
  "CONFERE como reprise qualitativa (com '~'); herda o conflito do Cap.1 §1.6 com o Anexo E/H"),
 ("C05", r"r = \text{constante}", "ramo algébrico acima",
  "CONFERE (no ramo algébrico; e também no dito 'dinâmico', pela âncora D5)"),
 ("C05", r"\rho_{\text{int}} = \text{constante}", "ρ_int(r); r=const acima",
  "CONFERE (com β_n constantes)"),
]


def main():
    aplicados = 0
    problemas = []
    for pref in ("C01", "C02", "C03", "C04", "C05"):
        path = os.path.join(REG, pref + ".md")
        with open(path, encoding="utf-8") as fh:
            texto = fh.read()
        blocos = re.split(r"(?=### \[)", texto)
        regras = [(key, dep, ver) for (p, key, dep, ver) in V if p == pref]
        for key, dep, ver in regras:
            hits = [i for i, b in enumerate(blocos)
                    if b.startswith("### [") and key in b]
            if len(hits) != 1:
                problemas.append(f"{pref}: chave '{key[:50]}' -> {len(hits)} blocos")
                continue
            b = blocos[hits[0]]
            b2 = b.replace("- **Depende de:** _(a preencher)_",
                           f"- **Depende de:** {dep}")
            b2 = b2.replace("- **Veredito:** _(pendente)_",
                            f"- **Veredito:** {ver}")
            if b2 == b:
                problemas.append(f"{pref}: chave '{key[:50]}' casou mas campos ja preenchidos?")
            blocos[hits[0]] = b2
            aplicados += 1
        texto2 = "".join(blocos)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(texto2)
        pend = texto2.count("_(pendente)_")
        print(f"{pref}: {pend} entradas ainda pendentes")
    print(f"\nvereditos aplicados: {aplicados}")
    if problemas:
        print("PROBLEMAS:")
        for p in problemas:
            print("  -", p)


if __name__ == "__main__":
    main()
