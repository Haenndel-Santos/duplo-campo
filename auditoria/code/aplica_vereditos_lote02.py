# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote02.py — vereditos do Lote 2 (C06, C06E, C07, C08,
C09, C10), casados por substring da formula. Entradas com multi=True
aplicam o mesmo veredito a todas as ocorrencias ainda pendentes
(condicoes repetidas). Ordem da lista importa: chaves especificas antes
das genericas.

Uso: python aplica_vereditos_lote02.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

# (arquivo, chave, depende, veredito, multi)
V = [
 # ================= C06 =================
 ("C06", r"g_{\mu\nu}^{(0)}, \quad f_{\mu\nu}^{(0)}", "Cap.5", "CONFERE (notação de fundo)", False),
 ("C06", r"g_{\mu\nu} = g_{\mu\nu}^{(0)} + \delta g", "fundo acima", "CONFERE (expansão linear padrão)", False),
 ("C06", r"f_{\mu\nu} = f_{\mu\nu}^{(0)} + \delta f", "fundo acima", "CONFERE", False),
 ("C06", r"\phi = \phi_0(t) + \delta \phi", "Cap.2 §2.2", "CONFERE", False),
 ("C06", r"h_{ij}^{(g)}, \quad h_{ij}^{(f)}", "—", "CONFERE (notação TT)", False),
 ("C06", r"\ddot h_m + 3H \dot h_m", "decomposição acima", "CONFERE SOB HIPÓTESE (esquemática; forma exata com o m_T² dependente de ξ na âncora D2; o modo massivo não propaga com c²=1 puro — mistura dos cones c_g²=1 e c_f²=ξ²/r²)", False),
 ("C06", r"$m_g^2 > 0.$", "eq. do modo massivo acima", "CONFERE (condição; âncora D2: no ramo dinâmico do benchmark, m_T²<0 — a condição é violada exatamente no ramo declarado como principal)", False),
 ("C06", r"$m_g^2 \ge 2H^2.$", "—", "CONFERE (importada: Higuchi em dS; aplicar com o m_T² real da âncora D2)", False),
 ("C06", r"\mathcal{M} = \begin{pmatrix}", "—", "CONFERE (estrutura 2×2 esquemática; flag sem-delimitador — formatar); as matrizes reais são 3×3, âncora D1", False),
 ("C06", r"\mathcal{L}_{kin} = -\frac{1}{2} Z", "—", "CONFERE (convenção correta: saudável ⟺ Z>0 na assinatura −+++)", False),
 ("C06", r"\delta \ddot{\phi} + 3H \delta \dot{\phi}", "expansão linear acima", "CONFERE (esquemática padrão; δS_int calculado na âncora D1)", False),
 ("C06", r"$V''(\phi_0) < 0$", "eq. perturbada acima", "CONFERE (critério taquiônico)", False),
 ("C06", r"$7 + 1 = 8 \text{ graus", "—", "CONFERE (importada: contagem HR 2+5 + escalar); NOTA âncora D1: a análise em fundo congelado encontra 3 modos escalares onde a contagem padrão espera 2 — a remoção por constraint temporal não está demonstrada no corpus", False),
 ("C06", r"g_{ij} = a^2(t)(\delta_{ij} + h_{ij})", "—", "CONFERE", False),
 ("C06", r"f_{ij} = b^2(t)(\delta_{ij} + \ell_{ij})", "—", "CONFERE", False),
 ("C06", r"\partial_i h_{ij} = 0", "—", "CONFERE (condição TT)", False),
 ("C06", r"\frac{1}{2} M_f^2 b^3 \dot{\ell}^2", "ação HR (Cap.3 §3.2)", "ERRO DE CÁLCULO (âncora D2): gradientes sem M² e sem 1/a²,1/b² (dimensionalmente inconsistentes como escritos); cinético de ℓ sem o fator 1/ξ (correto: M_f²b³/ξ) e gradiente de ℓ sem ξ; termo de massa com prefator errado — forma correta na Derivação 2 §3.1", False),
 ("C06", r"h_0 = \cos\theta", "ação TT acima", "ERRO DE FORMULAÇÃO: rotação ortogonal só diagonaliza cinéticos IGUAIS; com M_g²a³ ≠ M_f²b³/ξ a base correta é a ponderada (M_g h + M_f r^{3/2}ℓ — Anexo D §D.4/âncora D2)", False),
 ("C06", r"h_m = -\sin\theta", "ação TT acima", "ERRO DE FORMULAÇÃO (idem entrada anterior)", False),
 ("C06", r"\ddot{h}_0 + 3H \dot{h}_0", "diagonalização acima", "CONFERE (âncora D2: o modo massless existe, det M=0)", False),
 ("C06", r"\ddot{h}_m + 3H \dot{h}_m + \left(\frac{k^2}{a^2} + m_T^2\right)", "diagonalização acima", "CONFERE SOB HIPÓTESE (esquemática; ver notas de c² e m_T²(ξ) — âncora D2)", False),
 ("C06", r"$m_T^2 \ge 2H^2.$", "—", "CONFERE (importada: Higuchi; refazer com m_T²(ξ) — âncora D2)", False),
 ("C06", r"\dot{Q}^T K \dot{Q} - Q^T \Omega Q", "decomposição escalar acima", "CONFERE (estrutura; matrizes explícitas em derivations/code/out/01_matrices.txt — âncora D1)", False),
 ("C06", r"Q = (\psi_g, \psi_f, \delta\phi)", "—", "CONFERE (base; NOTA: (ψ_g,ψ_f,δφ) aqui vs (ζ,σ,δφ) no Cap.6.2/7/8 — unificar)", False),
 ("C06", r"$\det K < 0$", "K acima", "CONFERE (condicional: fantasma)", False),
 ("C06", r"c_s^2 = \frac{\text{coeficiente espacial}}", "—", "CONFERE (esquemática; a forma correta é autovalor de K⁻¹G — Anexo C §C.8/âncora D1)", False),
 ("C06", r"\ddot{\chi} + 3H_{\text{eff}} \dot{\chi}", "redução acima", "CONFERE SOB HIPÓTESE (esquemática; assume sistema diagonalizado); NOTA de sobrecarga: χ aqui é o modo efetivo reduzido, χ nos Anexos B–H é o próprio campo estrutural", False),
 ("C06", r"m_{\text{eff}}^2 = V''(\phi_0) + \text{corre", "eq. efetiva acima", "INCOMPLETA (as 'correções de acoplamento' nunca são calculadas no corpus; calculadas na âncora D1 — massas reais O(1) e taquiônicas no setor relativo)", False),
 ("C06", r"$m_{\text{eff}}^2 > 0.$", "—", "CONFERE (condição de estabilidade tardia)", False),
 ("C06", r"$m_{\text{eff}}^2 < 0$", "—", "CONFERE (condicional: regime de bifurcação primordial)", False),
 ("C06", r"T^{\mu\nu}_{(g)} = J^\nu", "Cap.4 §4.4 (Q_ν)", "POSTULADO com conflito: on-shell J≡0 (achado A1 do Lote 1 — as identidades do Cap.4 §4.4 anulam a troca); manter J≠0 contradiz a constraint de Bianchi do Cap.5 §5.5", False),
 ("C06", r"T^{\mu\nu}_{(f)} = - J^\nu", "entrada anterior", "POSTULADO com conflito (idem; e T^{(f)} de matéria não existe na teoria — matéria acopla só a g)", False),
 ("C06", r"(T^{\mu\nu}_{(g)} + T^{\mu\nu}_{(f)}) = 0", "—", "ERRO DE FORMULAÇÃO (idem Cap.4 §4.7: soma de tensores de métricas diferentes sob ∇ único não especificado)", False),
 ("C06", r"1. m_T^2 > 2H^2", "—", "ARTEFATO DE CONVERSÃO (item de lista dentro de $); como condição: CONFERE com âncora D2 (usar m_T²(ξ))", False),
 ("C06", r"2. Z_{\text{esc}} > 0", "—", "ARTEFATO DE CONVERSÃO (idem); como condição: CONFERE", False),
 ("C06", r"3. c_s^2 > 0", "—", "ARTEFATO DE CONVERSÃO (idem); como condição: CONFERE", False),
 ("C06", r"5. \det K > 0", "—", "ARTEFATO DE CONVERSÃO (idem); como condição: CONFERE (avaliada de fato na âncora D1)", False),
 ("C06", r"$\det K > 0", "S(2) escalar acima", "CONFERE (condição no-ghost; âncora D1: no ramo dinâmico há par com cinética negativa — a condição falha lá independentemente de β₁+2β₂r)", False),
 ("C06", r"c_s^2 > 0", "—", "CONFERE (condição no-gradient)", True),
 ("C06", r"c_s^2 < 0", "—", "CONFERE (condicional: instabilidade de gradiente)", True),
 # ================= C06E =================
 ("C06E", r"ds_g^2 = -dt^2 + a^2(t)\delta_{ij}", "Cap.5 §5.1", "CONFERE (fundo, gauge N_g=1)", False),
 ("C06E", r"-X^2(t)\,dt^2", "Cap.5 §5.1", "CONFERE (fundo; NOTA: lapse chamado X(t) aqui vs N_f nos demais capítulos — unificar)", False),
 ("C06E", r"2a(t)\partial_i B\,dt\,dx^i", "fundo acima", "CONFERE (ansatz escalar completo do setor g)", False),
 ("C06E", r"2X(t)b(t)\partial_i B_f", "fundo acima", "CONFERE (ansatz escalar completo do setor f)", False),
 ("C06E", r"\phi(t,\vec{x}) = \phi_0(t) + \delta\phi", "—", "CONFERE", False),
 ("C06E", r"$B = 0,\qquad E = 0$", "ansatz acima", "CONFERE SOB HIPÓTESE com NOTA METODOLÓGICA (âncora D1): fixar B=E=0 NA AÇÃO descarta as constraints desses campos e fabrica modo espúrio — fixar nas equações ou usar gauge plano com multiplicadores mantidos", False),
 ("C06E", r"S = S^{(0)} + S^{(1)}", "—", "CONFERE (expansão padrão; S(1)=0 no fundo on-shell)", False),
 ("C06E", r"\dot{\mathbf{Q}}^T \mathbf{K}\, \dot{\mathbf{Q}}", "ansatz acima", "CONFERE (estrutura; matrizes explícitas na âncora D1)", False),
 ("C06E", r"\mathbf{Q} = (\zeta,\ \sigma,\ \delta\phi)", "redução acima", "CONFERE — âncora D1: contagem de 3 modos CONFIRMADA na análise de fundo congelado (contra os 2 do Anexo C §C.3); ressalva: remoção por constraint temporal não demonstrada", False),
 ("C06E", r"Q \sim e^{|c_s|k t/a}", "c_s²<0 acima", "CONFERE (crescimento de gradiente)", False),
 ("C06E", r"\left|\frac{\dot{\beta}_n}{\beta_n}\right| \ll H", "β_n(φ) (Cap.3 §3.8)", "CONFERE (condição de adiabaticidade; usada como hipótese da raiz móvel na âncora D5 §4.1)", False),
 ("C06E", r"|\dot{\beta}_n/\beta_n| \ll H", "idem", "CONFERE (reprise da condição de adiabaticidade)", False),
 ("C06E", r"$m_T^2 \ge 2H^2$", "—", "CONFERE (importada: Higuchi; usar m_T²(ξ) — âncora D2)", False),
 ("C06E", r"\ddot{Q}_i + 3H\dot{Q}_i", "S(2) acima", "CONFERE SOB HIPÓTESE (assume K e Ω simultaneamente diagonalizáveis — em geral não são; o sistema acoplado real está na âncora D1)", False),
 ("C06E", r"\mathbf{K} > 0", "S(2) acima", "CONFERE (condição no-ghost; sinais reais avaliados na âncora D1 — par com cinética negativa no ramo dinâmico; a condição NÃO equivale a β₁+2β₂r>0)", True),
 ("C06E", r"c_{s,i}^2 > 0", "—", "CONFERE (condição no-gradient)", True),
 ("C06E", r"m_i^2 > 0", "—", "CONFERE (condição no-taquion tardia; no regime primordial m²<0 é a bifurcação desejada)", True),
 # ================= C07 =================
 ("C07", r"\nabla^2 \Phi = 4\pi G a^2", "—", "CONFERE (importada: Poisson cosmológica padrão)", False),
 ("C07", r"$k \gg aH$", "—", "CONFERE (regime sub-horizonte)", False),
 ("C07", r"\left|\dot{X}\right| \ll", "—", "CONFERE (definição do limite quase-estático)", False),
 ("C07", r"(1+2\Phi)\,dt^2 + a^2(t)(1-2\Psi)", "Cap.6", "CONFERE (gauge Newtoniano; ver nota metodológica do Cap.6.2 sobre fixação na ação)", False),
 ("C07", r"$\Phi = \Psi.$", "—", "CONFERE (GR sem estresse anisotrópico; verificado na calibração GR da âncora D6: Φ/Ψ→1)", False),
 ("C07", r"\mathbf{Q} = (\zeta,\ \sigma,\ \delta\phi)", "Cap.6.2 §6.4", "CONFERE (âncora D1)", False),
 ("C07", r"k^2\Psi = -4\pi G a^2 \mu(k,a)", "Poisson acima", "CONFERE (definição observacional de μ — a mesma usada na âncora D6)", False),
 ("C07", r"\eta_{\text{slip}}(k,a) \equiv \frac{\Phi}{\Psi}", "—", "CONFERE (definição)", False),
 ("C07", r"\mu = 1,\qquad \eta_{\text{slip}} = 1", "definições acima", "CONFERE (limite GR)", False),
 ("C07", r"k^2\Psi \sim 4\pi G a^2\rho\delta + \mathcal{S}", "definições acima", "CONFERE (esquemática; a fonte S real está no sistema acoplado da âncora D6)", False),
 ("C07", r"m_\sigma^2\right)\sigma \approx A_\sigma", "—", "CONFERE SOB HIPÓTESE (estrutura de 1 polo por modo, com A_σ nunca calculado — INCOMPLETA; âncora D6: o sistema real é acoplado e multi-polo)", False),
 ("C07", r"m_\phi^2\right)\delta\phi \approx A_\phi", "—", "CONFERE SOB HIPÓTESE (idem; A_φ nunca calculado)", False),
 ("C07", r"\sigma \sim \frac{A_\sigma}", "eq. de σ acima", "CONFERE (dado o anterior)", False),
 ("C07", r"\delta\phi \sim \frac{A_\phi}", "eq. de δφ acima", "CONFERE (dado o anterior)", False),
 ("C07", r"1 + \frac{\Delta_\sigma}{1 + m_\sigma^2 a^2/k^2} + \frac{\Delta_\phi}{1 + m_\phi^2 a^2/k^2}\right]\rho\delta", "substituição acima", "ERRO (âncora D6): a retro-reação não é aditiva/desacoplada — o μ real é racional de grau 7/7 em k² com α_∞=0; ADEMAIS a prosa do §7.6 ('em escalas pequenas k→∞ os termos extras suprimem → GR recuperada') CONTRADIZ esta fórmula (que dá desvio máximo em k→∞) — ironicamente a prosa coincide com o resultado derivado e a fórmula não", False),
 ("C07", r"\mu(k,a)=1+\frac{\Delta_\sigma}{1+m_\sigma^2 a^2/k^2}", "equação acima", "ERRO (âncora D6: forma de 2 polos refutada — 7 polos, α_∞=0; e conflito prosa×fórmula registrado na entrada anterior)", False),
 ("C07", r"\eta_{\text{slip}}(k,a) = \frac{1+\Pi_1", "—", "INCOMPLETA (Π₁,Π₂ nunca definidos); âncora D6: η_slip real é não-monotônico e não se reduz a uma razão de 2 Yukawas", False),
 ("C07", r"G_{\text{eff}}(k,a)=G\mu(k,a)", "definição de μ acima", "CONFERE (definição; flag em-citacao)", False),
 ("C07", r"$> \Phi\neq\Psi$", "—", "CONFERE (âncora D6 confirma slip≠1; flag em-citacao)", False),
 ("C07", r"\ddot\delta + 2H\dot\delta = 4\pi G_{\text{eff}}", "μ acima", "CONFERE SOB HIPÓTESE (substituição G→G_eff; passo QS padrão — ver Cap.8)", False),
 # ================= C08 =================
 ("C08", r"\delta = \frac{\delta\rho}{\rho}", "—", "CONFERE (definição)", False),
 ("C08", r"2H\dot{\delta} = 4\pi G\rho\delta", "—", "CONFERE (importada: crescimento padrão de matéria em RG; o próprio rascunho registra que não há derivação própria aqui)", False),
 ("C08", r"G \rightarrow G_{\text{eff}}(k,a) = G\,\mu(k,a)", "Cap.7 §7.5", "CONFERE (definição)", False),
 ("C08", r"4\pi G\,\mu(k,a)\,\rho\delta $$", "substituição acima", "CONFERE SOB HIPÓTESE (equivalência com G_eff; μ deve ser o do potencial temporal — convenção da âncora D6)", False),
 ("C08", r"\frac{\Delta_\sigma}{1 + m_\sigma^2 a^2/k^2}", "Cap.7 §7.6", "ERRO (reprise da forma de 2 polos — âncora D6; e a prosa do §8.4 'em escalas pequenas μ→1' contradiz a fórmula, que dá μ→1+Δ em k→∞ — mesma inversão do Cap.7)", False),
 ("C08", r"D(a) = \frac{\delta(a)}", "—", "CONFERE (definição)", False),
 ("C08", r"f(a) = \frac{d\ln\delta}{d\ln a}", "—", "CONFERE (definição)", False),
 ("C08", r"(\zeta,\ \sigma,\ \delta\phi)", "Cap.6.2 §6.4", "CONFERE (âncora D1)", False),
 ("C08", r"\ddot{\delta}_k + 2H\dot{\delta}_k", "eq. de crescimento acima", "CONFERE (versão em Fourier)", False),
 ("C08", r"4\pi G_{\text{eff}}(k,a)\,\rho\delta", "μ/G_eff acima", "CONFERE SOB HIPÓTESE (equação-chave por substituição G→G_eff; derivação completa a partir das eqs. perturbadas permanece pendente no corpus — o rascunho já o declara)", True),
 # ================= C09 =================
 ("C09", r"\delta(\vec{x}) = \int \frac{d^3k}", "—", "CONFERE (definição)", False),
 ("C09", r"(2\pi)^3 \delta_D(\vec{k}+\vec{k}') P(k)", "—", "CONFERE (definição padrão do espectro)", False),
 ("C09", r"P(k) = P_{\text{primordial}}(k) \, T^2(k) \, D^2(a)", "—", "CONFERE (importada: decomposição padrão)", False),
 ("C09", r"P_{\text{prim}}(k) = P_\zeta(k) + P_\sigma(k) + 2P_{\zeta\sigma}", "Cap.10 (modos ζ,σ)", "CONFERE SOB HIPÓTESE (decomposição multifield; a convenção do espectro cruzado P_ζσ não é definida)", False),
 ("C09", r"= 4\pi G_{\text{eff}}(k,a)\rho\delta", "Cap.8 §8.3", "CONFERE (reprise)", False),
 ("C09", r"$G_{\text{eff}} = G \mu(k,a)$", "Cap.7 §7.5", "CONFERE (reprise)", False),
 ("C09", r"T(k) \rightarrow T_{\text{TDCP}}(k)", "—", "CONFERE (notação)", False),
 ("C09", r"\mu(k,a) = 1+\frac{\Delta_\sigma}", "Cap.7 §7.6", "ERRO (reprise da forma de 2 polos — âncora D6; prosa 'em escalas pequenas → GR recuperada' de novo contradiz a fórmula)", False),
 ("C09", r"P_{\text{TDCP}}(k,a) = P_{\text{prim}}", "decomposição acima", "CONFERE (estrutura)", False),
 ("C09", r"D_{\text{TDCP}}(a,k) \neq D_{\Lambda\text{CDM}}", "μ(k,a) acima", "CONFERE (crescimento dependente de escala — consequência real, âncora D6)", False),
 ("C09", r"Se \Delta_\sigma > 0", "—", "ARTEFATO DE CONVERSÃO (prosa dentro de $)", False),
 ("C09", r"$\Phi \neq \Psi$", "Cap.7 §7.8", "CONFERE (âncora D6)", False),
 ("C09", r"C_\ell \sim \int dk", "—", "CONFERE (esquemática padrão)", False),
 ("C09", r"|P_{\text{TDCP}}(k) - P_{\text{obs}}(k)|", "—", "CONFERE (condição qualitativa de compatibilidade)", False),
 # ================= C10 =================
 ("C10", r"m_{\text{eff}}^2 < 0", "Cap.6 §6.7", "CONFERE (regime primordial taquiônico)", False),
 ("C10", r"\ddot{\sigma} + 3H \dot{\sigma} - |m_\sigma^2|\sigma = 0", "σ (Cap.6.2 §6.9)", "CONFERE (eq. taquiônica em tempo cósmico, k→0)", False),
 ("C10", r"\sigma(\vec{x},t) = \int", "—", "CONFERE (definição)", False),
 ("C10", r"$a(t) \sim e^{Ht}$", "—", "CONFERE (quase-de Sitter)", False),
 ("C10", r"\sigma_k'' + 2\frac{a'}{a}\sigma_k'", "expansão acima", "CONFERE (âncora D7 resolve exatamente); NOTA: primas = tempo conforme, mas a passagem do tempo cósmico (eq. anterior) é silenciosa — declarar", False),
 ("C10", r"\sigma_k \sim k^{-3/2}", "eq. do modo acima", "CONFERE SOB HIPÓTESE (âncora D7: vale apenas se |m_σ²|≪H²; forma geral σ_k~k^(−ν), ν=√(9/4+|m_σ²|/H²); adotar a previsão n_σ−1≈−(2/3)|m_σ²|/H²)", False),
 ("C10", r"\zeta = \frac{\delta\rho}{\rho + p}", "—", "INCOMPLETA/sobrecarga: definição não-padrão de ζ (na literatura ζ é a perturbação de curvatura comóvel) e o MESMO símbolo ζ é usado no Cap.6.2/7/8 como 'curvatura efetiva' — unificar", False),
 ("C10", r"S = \zeta_g - \zeta_f", "ζ acima", "CONFERE (definição de isocurvatura relativa, dada a definição de ζ acima)", False),
 ("C10", r"P_\zeta(k) = A_s", "—", "CONFERE (parametrização declarada)", False),
 ("C10", r"\Delta_{\text{struct}}(k) \sim \frac{\lambda}{1 + k^2/k_c^2}", "parametrização acima", "CONFERE como ansatz declarado ('~'); NOTA: λ aqui colide com o λ do portal Higgs (Cap.2 §2.4) — renomear", False),
 ("C10", r"n_s \approx 0.965", "—", "CONFERE (importada: valor observacional)", False),
 ("C10", r"\sigma(t) \sim e^{\gamma t}", "instabilidade acima", "CONFERE (esquemática; γ não definido — ligá-lo a |m_σ| explicitamente)", False),
 ("C10", r"\tau \sim \ln \sigma", "crescimento acima", "INCOMPLETA (definição heurística; a ligação com T(x)=f(H₁−H₂) do Cap.1 §1.7 nunca é estabelecida)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("C06", "C06E", "C07", "C08", "C09", "C10")
    textos = {}
    for pref in arquivos:
        with open(os.path.join(REG, pref + ".md"), encoding="utf-8") as fh:
            textos[pref] = re.split(r"(?=### \[)", fh.read())
    for pref, key, dep, ver, multi in V:
        blocos = textos[pref]
        hits = [i for i, b in enumerate(blocos)
                if b.startswith("### [") and key in b
                and "_(pendente)_" in b]
        if not hits:
            problemas.append(f"{pref}: chave '{key[:45]}' -> 0 blocos pendentes")
            continue
        if len(hits) > 1 and not multi:
            problemas.append(f"{pref}: chave '{key[:45]}' -> {len(hits)} blocos (sem multi)")
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
    print(f"\nvereditos aplicados: {aplicados}")
    if problemas:
        print("PROBLEMAS:")
        for p in problemas:
            print("  -", p)


if __name__ == "__main__":
    main()
