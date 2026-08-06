# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote05.py — vereditos do Lote 5 (C22-C26).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

D1 = "âncora D1 (derivations/01_setor_escalar_K_Omega.md)"
D6 = "âncora D6 (derivations/06_mu_alpha_quase_estatico.md)"
D8 = "âncora D8 (derivations/08_mS0_dinamica_F.md)"
GALSCRIPT = "auditoria/code/lote05_C22_galileon_stability.py (criado nesta auditoria)"

V = [
 # ================= C22 (30) — screening/Vainshtein, continua território sem âncora =================
 ("C22", r"\mathcal V_{HR}(g,f) mantém o conjunto de restrições",
  "Cap.17 §17.4 (C17.15)",
  "CONFERE (importada da literatura — resultado padrão de Hassan-Rosen ghost-free, mesma nota de C17.15; flag sem-delimitador: a extração capturou uma frase de prosa, não uma fórmula, mas o conteúdo é uma afirmação substantiva)", False),
 ("C22", r"m^2F(\phi)\,\mathcal V_{HR}(g,f).", "Cap.14/Cap.20 (ação HR completa)",
  "CONFERE (reprise — consistente com a ação de Cap.14/Cap.20)", False),
 ("C22", r"\mathcal{L}_{\pi} = -\frac{1}{2}Z(\phi)(\partial\pi)^2 + \frac{c_3(\phi)}{\Lambda_3^3}(\partial\pi)^2\square\pi + \frac{\alpha_V}{M_{\rm Pl}}\pi\,T",
  "Cap.20 §20.4 (C20.09)",
  "CONFERE (reprise exata de C20.09 — mesma nota: Z(φ),c3(φ),αV postulados por analogia dRGT, não derivados dos β_n reais)", False),
 ("C22", r"\Lambda_3^3 \sim m^2 F(\phi)\,M_{\rm eff} \;\;\approx\;\; m^2F_0\,M_{\rm Pl}",
  "Cap.20 §20.3 (C20.07/08)",
  "CONFERE (reprise combinada de C20.07/08)", False),
 ("C22", r"\pi(x)=\bar\pi(r)+\varphi(x), \qquad r\ll r_V.", "—",
  "CONFERE (decomposição padrão background+flutuação; usa \\varphi para a flutuação de π, distinto de \\phi — o campo escalar da TDCP-F1 usado em F(φ) — disambiguação correta apesar da semelhança visual dos dois símbolos)", False),
 ("C22", r"S^{(2)}_\varphi = \frac12\int d^4x\; K^{\mu\nu}(\bar\pi)\;\partial_\mu\varphi\,\partial_\nu\varphi",
  "—",
  "CONFERE (forma padrão de ação quadrática para flutuações em torno de um background não-trivial — técnica padrão de EFT tipo Galileon)", False),
 ("C22", r"K^{\mu\nu} = Z\,\eta^{\mu\nu} + \frac{2c_3}{\Lambda_3^3} \left[ 2\,\partial^\mu\partial^\nu\bar\pi - \eta^{\mu\nu}\,\Box\bar\pi \right]",
  "C22.06",
  "CONFERE (importada — forma padrão da matriz cinética de flutuações do galileon cúbico, resultado bem estabelecido na literatura, ex. Nicolis-Rattazzi-Trincherini)", False),
 ("C22", r"\Box\bar\pi = \bar\pi''+\frac{2}{r}\bar\pi'.", "—",
  "CONFERE (verificado nesta auditoria: laplaciano radial padrão em 3D, ∇²f=f''+2f'/r, consistente com a assinatura (-,+,+,+) usada desde Cap.18)", False),
 ("C22", r"\partial_i\partial_j \bar\pi = \left(\bar\pi''-\frac{\bar\pi'}{r}\right)n_i n_j + \frac{\bar\pi'}{r}\delta_{ij}, \qquad n_i=\frac{x_i}{r}.",
  "C22.08",
  "CONFERE (álgebra verificada nesta auditoria: decomposição padrão da Hessiana de uma função radial em partes radial e transversa)", False),
 ("C22", r"Z_t = Z + \frac{4c_3}{\Lambda_3^3} \left( \bar\pi''+\frac{2}{r}\bar\pi' \right)",
  f"C22.07, C22.09; {GALSCRIPT}",
  "CONFERE SOB HIPÓTESE — forma operacional padrão citada da literatura de Galileon esférico, com a ressalva do próprio texto (\"até fatores convencionais de sinal\"); a rederivação direta desta auditoria a partir de C22.07+C22.09 (K^00=-Z+(2c3/Λ3³)□π̄, mostrado por álgebra explícita) NÃO reproduziu exatamente este coeficiente; script de verificação simbólica criado — pendente de execução local antes de aceitar ou corrigir", False),
 ("C22", r"Z_r = Z + \frac{8c_3}{\Lambda_3^3} \left( \frac{\bar\pi'}{r} \right)",
  f"C22.07, C22.09; {GALSCRIPT}",
  "CONFERE SOB HIPÓTESE (mesma pendência de C22.10 — script de verificação criado, rederivação manual desta auditoria deu K^zz=Z+(2c3/Λ3³)(π̄''-2π̄'/r), diferente do valor em caixa)", False),
 ("C22", r"Z_\Omega = Z + \frac{4c_3}{\Lambda_3^3} \left( \bar\pi''+\frac{\bar\pi'}{r} \right)",
  f"C22.07, C22.09; {GALSCRIPT}",
  "CONFERE SOB HIPÓTESE (mesma pendência de C22.10/11 — script de verificação criado)", False),
 ("C22", r"Z_t>0,\qquad Z_r>0,\qquad Z_\Omega>0.", "C22.10-12",
  "CONFERE (critério padrão de ausência de ghost/instabilidade de gradiente — independente da forma exata de Z_t,Z_r,Z_Ω, que é o que fica pendente em C22.10-12)", False),
 ("C22", r"c_r^2 = \frac{Z_r}{Z_t}, \qquad c_\Omega^2=\frac{Z_\Omega}{Z_t}.", "C22.10-13",
  "CONFERE (definição padrão de velocidade de propagação a partir da razão dos coeficientes cinéticos — mesma nota de pendência sobre a forma exata de C22.10-12)", False),
 ("C22", r"y(r)\equiv \frac{\bar\pi'}{r} \propto r^{-3/2}",
  "Cap.20 §20.6 (C20.15)",
  "ARTEFATO DE CONVERSÃO na continuação da fórmula — a fração \"π̄''/(espaço vazio)\" (comando \\; sem conteúdo) tem denominador ausente, erro de conversão/digitação; o texto também se contradiz (usa \"≫\" e na sequência qualifica como \"mesma ordem paramétrica\" a mesma comparação); fisicamente, para y∝r^{-3/2} tanto π̄'/r quanto π̄'' escalam como r^{-3/2} — mesma ordem, consistente com a legenda, não com o símbolo ≫. A proporcionalidade y∝r^{-3/2} em si CONFERE (consistente com C20.15: y²∝1/r³)", False),
 ("C22", r"Z_t \sim \frac{4c_3}{\Lambda_3^3}\left(\bar\pi''+\frac{2\bar\pi'}{r}\right), \qquad Z_r \sim \frac{8c_3}{\Lambda_3^3}\left(\frac{\bar\pi'}{r}\right), \qquad Z_\Omega \sim \frac{4c_3}{\Lambda_3^3}\left(\bar\pi''+\frac{\bar\pi'}{r}\right).",
  "C22.10-12",
  "CONFERE SOB HIPÓTESE (consistente internamente com C22.10-12 no limite Z desprezível — mesma pendência de verificação, script criado)", False),
 ("C22", r"\frac{c_3}{Z} > 0 \quad\text{(escolha de ramo/parametrização que garante }Z_t,Z_r,Z_\Omega>0\text{ no Vainshtein).}",
  "C22.16",
  "CONFERE SOB HIPÓTESE (condição qualitativa razoável dado o padrão de sinais assumido em C22.16 — mesma pendência de verificação dos coeficientes exatos)", False),
 ("C22", r"c_r^2 \gtrsim 1,", "—",
  "CONFERE (qualitativa, consistente com a literatura de Galileon cúbico — superluminalidade efetiva é um resultado conhecido, ex. Adams et al. 2006)", False),
 ("C22", r"\text{TDCP-F1 (como HR/dRGT-like) pode herdar cones efetivos modificados no Vainshtein; isso exige monitoramento, não invalidação imediata.}",
  "C22.18",
  "CONFERE (postura científica bem calibrada — consistente com a literatura sobre superluminalidade em EFTs de Galileon sem UV completion assumida; o capítulo não superestima a implicação)", False),
 ("C22", r"Z\,y \sim \frac{4c_3}{\Lambda_3^3}y^2 \quad\Rightarrow\quad y \sim \frac{Z\Lambda_3^3}{4c_3} \quad\text{em }r\sim r_V,",
  "Cap.20 §20.7 (C20.16/17)",
  "CONFERE (reprise da lógica de C20.16-17)", False),
 ("C22", r"\left|\frac{\partial^2\bar\pi}{\Lambda_3^3}\right| \lesssim \mathcal{O}(1) \quad\text{no raio de interesse (ex.: em AU).}",
  "—",
  "CONFERE (critério operacional razoável de validade de truncamento EFT, qualitativo mas fisicamente sensato)", True),
 ("C22", r"\text{Escolher a hierarquia de coeficientes }(c_3,c_4,c_5,\dots) \text{ para que o operador dominante permaneça controlado e a série EFT não colapse.}",
  "C22.21",
  "CONFERE (qualitativa — reafirma o critério de C22.21 como estratégia, não introduz conteúdo matemático novo)", False),
 ("C22", r"\Lambda_3^3 \propto m^2F(\phi),", "Cap.20 §20.3 (C20.07)",
  "CONFERE (reprise, consistente com C20.07/C22.04)", False),
 ("C22", r"\left|\frac{\delta F}{F_0}\right| \ll 1 \quad\text{em escalas solares.}",
  "Cap.21 §21.7 (C21.23)",
  "CONFERE (reprise da condição de C21.23 — mesma pendência: m_φ nunca é calculada a partir de ℒ_φ, ver C21.24)", False),
 ("C22", r"|\nabla \phi| \;\text{pequeno no Sistema Solar} \;\Rightarrow\; \text{nenhuma força adicional relevante além do helicity-0 já screened.}",
  "Cap.21 §21.7 (C21.24); Cap.20 §20.11 (C20.33)",
  "CONFERE (consistente com a condição já estabelecida em C21.24/C20.33 — mesma pendência: nunca fica claro como |∇φ| pequeno é garantido, pois m_φ nunca é calculada)", False),
 ("C22", r"\text{BD ghost ausente (potencial HR ghost-free preservado por }F(\phi)\text{ multiplicativo).}",
  "C22.01/02",
  "CONFERE (reprise da conclusão de §22.2 — mesma nota de C22.01: importada da literatura HR)", False),
 ("C22", r"Z_t>0,\; Z_r>0,\; Z_\Omega>0 \;\;\Rightarrow\;\; \text{sem ghost e sem instabilidade de gradiente.}",
  "C22.13",
  "CONFERE (reprise de C22.13 — mesma pendência sobre a forma exata de Z_t,Z_r,Z_Ω herdada de C22.10-12)", False),
 ("C22", r"c_3/Z > 0 \quad (\text{com o sinal do perfil escolhido fisicamente}).",
  "C22.17", "CONFERE SOB HIPÓTESE (reprise de C22.17)", False),
 ("C22", r"\left|\partial^2\bar\pi/\Lambda_3^3\right|\lesssim \mathcal O(1) \;\;\text{(ou hierarquia de coeficientes que mantém truncamento válido).}",
  "C22.21/22", "CONFERE (reprise de C22.21)", False),
 ("C22", r"|\delta F/F_0|\ll 1 \text{ em escalas solares e sem acoplamento direto }\phi T.",
  "C22.24; Cap.17 §17.4 (C17.14); Cap.21 §21.7",
  "CONFERE (reprise combinando C22.24 e o acoplamento mínimo já estabelecido — Cap.17 §17.4, Cap.21 §21.7)", False),

 # ================= C23 (17) — RASCUNHO RECONSTRUÍDO, base em Cap.18/19/22 =================
 ("C23", r"\mu(k,a) = 1 + \frac{\alpha(a)\,k^2/a^2}{k^2/a^2 + m_S^2(a)}",
  D6,
  "ERRO (repete o ansatz Yukawa de 1 polo já refutado — âncora D6; ver C18.09)", False),
 ("C23", r"\eta_{\rm slip}(k,a) = 1 + \frac{\beta(a)\,k^2/a^2}{k^2/a^2 + m_S^2(a)}",
  D6,
  "ERRO (repete a forma de 1 polo já refutada — âncora D6; ver C18.21)", False),
 ("C23", r"\Sigma(k,a) = \frac{\mu(k,a)}{2}\Big(1+\eta_{\rm slip}^{-1}(k,a)\Big)",
  "Cap.18 §18.15 (C18.22/45), Cap.19 §19.7 (C19.18)",
  "ERRO DE CÁLCULO (repete o erro de álgebra já identificado no lote 4: dado η_slip≡Φ/Ψ, a fórmula correta é Σ=(μ/2)(1+η_slip), não (μ/2)(1+η_slip⁻¹) — quarta ocorrência do mesmo erro, verificado por substituição em η_slip=2: correto dá Σ=1.5μ, esta forma dá 0.75μ)", False),
 ("C23", r"\ddot\delta + 2H\dot\delta = 4\pi G\,\mu(k,a)\,\rho\,\delta.",
  "Cap.8 (confirmado no lote 2)",
  "CONFERE (mesma forma já confirmada no Cap.8 — lote 2; citação \"Do Capítulo 8\" correta)", False),
 ("C23", r"f\sigma_8(z) \equiv f(z)\,\sigma_8(z), \qquad \sigma_8(z)=\sigma_8\,\frac{D(z)}{D(0)},", "—",
  "CONFERE (definições padrão, importadas)", False),
 ("C23", r"D_C(z) = \int_0^z \frac{c\,dz'}{H(z')}, \qquad D_A(z) = \frac{D_C(z)}{1+z}, \qquad D_H(z) = \frac{c}{H(z)},", "—",
  "CONFERE (definições padrão de distâncias cosmológicas, importadas)", False),
 ("C23", r"D_V(z) \equiv \left[ (1+z)^2 D_A(z)^2\, c\,z / H(z) \right]^{1/3}.", "C23.06",
  "CONFERE (importada — forma padrão de Eisenstein et al. 2005, D_V=[D_M²cz/H]^{1/3} com D_M=(1+z)D_A; verificada)", False),
 ("C23", r"P_\kappa^{ij}(\ell) = \int_0^{\chi_{\rm max}} d\chi\; \frac{W_i(\chi)W_j(\chi)}{\chi^2}\; \Sigma^2\!\left(\frac{\ell}{\chi},z(\chi)\right) P\!\left(\frac{\ell}{\chi},z(\chi)\right),",
  "—",
  "CONFERE (forma padrão de Limber para WL, modificada pela inserção de Σ² — prática padrão em MG, ex. hi_class/EFTCAMB)", False),
 ("C23", r"\text{TDCP pode imitar } w_0-w_a \text{ ou massa de neutrinos.}", "—",
  "CONFERE (qualitativa, diagnóstico razoável e padrão na literatura de MG)", False),
 ("C23", r"\{\Omega_m, H_0, \sigma_8, w_0, w_a, \sum m_\nu\}", "C23.09",
  "CONFERE (conjunto de parâmetros razoável para controlar as degenerescências de C23.09)", False),
 ("C23", r"\mu(k,a),\quad \Sigma(k,a)", "—",
  "CONFERE (qualitativa — lista de implementação)", False),
 ("C23", r"\mathcal L = \mathcal L_{BAO}\times \mathcal L_{RSD}\times \mathcal L_{WL}", "—",
  "CONFERE SOB HIPÓTESE (fatoração padrão assumindo probes independentes — simplificação comum, mas na prática costuma haver covariância entre BAO/RSD/WL do mesmo survey)", False),
 ("C23", r"m_{S0} \sim 30--300\,H_0", "Cap.19 §19.3 (C19.07)",
  "NÃO-DERIVÁVEL (repete a faixa de C19.07 — âncora D8: design observacional, não consequência dinâmica)", False),
 ("C23", r"\alpha_0 \sim 0.1--1", "Cap.18 §18.6/18.12 (C18.19/35)",
  "ERRO (herdado — âncora D6: α(a) não existe como função física bem definida; ADICIONALMENTE conflito interno: a faixa α0∼0.1–1 aqui excede o próprio limite de segurança \"|α(a0)|≲0.1\" que o Cap.18 §18.6 (C18.19) havia estabelecido poucos capítulos antes — a maior parte do intervalo proposto viola essa condição)", False),
 ("C23", r"p,q \sim \mathcal{O}(1)", D6,
  "CONFERE SOB HIPÓTESE (faixa qualitativa razoável enquanto ordem de grandeza; mas p,q parametrizam uma função m_S(a) cuja base física foi refutada — âncora D6)", False),
 ("C23", r"\text{Joelho escala-dependente em } f\sigma_8(k)", D6,
  "ERRO (herdado — âncora D6: não existe um \"joelho\" único; a estrutura real é multi-polo com ~7 polos — a assinatura qualitativa de \"dependência de escala\" pode sobreviver, mas não na forma de um joelho único)", True),
 ("C23", r"\text{RSD escala-dependente é o teste mais limpo.}", D6,
  "CONFERE SOB HIPÓTESE (conclusão estratégica razoável mesmo que a forma específica do sinal — joelho único — esteja refutada; a multi-polaridade real, âncora D6, também é escala-dependente e distinguível de w0-wa)", False),

 # ================= C24 (5) — RASCUNHO RECONSTRUÍDO =================
 ("C24", r"3M_g^2 H_g^2 = \rho_m + \rho_\phi + \rho_{\rm int}^{(g)}(r,\phi).", "Cap.14 (confirmado no lote 3)",
  "CONFERE (reprise da Friedmann-g de Cap.14 — já confirmada no lote 3)", False),
 ("C24", r"k^2\Psi = -4\pi G a^2\,\mu(k,a)\,\rho\,\delta \qquad \text{(Capítulo 7, §7.5).}",
  "Cap.7 §7.5 (confirmado no lote 2); equivalente a C18.03",
  "CONFERE (equivalente a C18.03 rearranjada; cita Cap.7 §7.5 como origem — consistente com o resumo do lote 2 sobre as definições observacionais do Cap.7)", False),
 ("C24", r"\eta_{\rm slip}(k,a) = \Phi/\Psi \qquad \text{(Capítulo 7, §7.8; forma explícita no Capítulo 18, §18.7).}",
  "Cap.18 §18.5 (C18.05)",
  "CONFERE (reprise da definição padrão)", False),
 ("C24", r"\Psi = \frac{1}{2k^2}\left(\ddot h + 6\ddot\eta_s\right) + \mathcal{H}\,\alpha_T, \qquad \Phi = \eta_s - \mathcal{H}\,\alpha_T,",
  "—",
  "CONFERE (importada da literatura padrão de teoria de perturbações cosmológicas — transformação síncrono↔newtoniano tipo Ma-Bertschinger; não específica da TDCP, conferência de coeficientes exatos fora do escopo desta auditoria)", False),
 ("C24", r"\{\Omega_b,\Omega_c,H_0,A_s,n_s,\tau,\alpha_0,m_{S0},p,q\}", "Cap.18/19/23 (α0,mS0,p,q)",
  "CONFERE (conjunto de parâmetros razoável para MCMC — inclui os parâmetros TDCP já discutidos, com a mesma pendência sobre α0,mS0,p,q — âncora D6/D8)", False),

 # ================= C25 (3) — RASCUNHO RECONSTRUÍDO =================
 ("C25", r"\left(\frac{\Delta T}{T}\right)_{\rm ISW} = \int d\eta\; \partial_\eta(\Phi+\Psi)\big(\eta,\,\vec{x}(\eta)\big),",
  "—",
  "CONFERE (importada — fórmula padrão do efeito ISW tardio)", False),
 ("C25", r"\partial_\eta(\Phi+\Psi) = 2\Big[\Sigma(k,a)\,\partial_\eta\Phi_{\rm GR}(k,a) \;+\; \Phi_{\rm GR}(k,a)\,\partial_\eta\Sigma(k,a)\Big].",
  "Cap.18 §18.1 (C18.04)",
  "CONFERE (álgebra verificada: regra do produto sobre Φ+Ψ=2ΣΦ_GR, que por sua vez segue corretamente da definição de Σ em C18.04 combinada com o limite GR: -k²(Φ+Ψ)=8πGa²Σρδ e -k²Φ_GR=4πGa²ρδ ⟹ Φ+Ψ=2ΣΦ_GR)", False),
 ("C25", r"C_\ell^{\phi\phi} = \int_0^{\chi_*} d\chi\; \frac{W_{\rm CMB}^2(\chi)}{\chi^2}\; \Sigma^2\!\left(\frac{\ell}{\chi},z(\chi)\right) P\!\left(\frac{\ell}{\chi},z(\chi)\right).",
  "Cap.23 §23.5 (C23.08)",
  "CONFERE (mesma estrutura de Limber de C23.08, com kernel de lentes do CMB — prática padrão)", False),

 # ================= C26 (7) — §26.1-4 reconstruído, §26.5-8 original preservado =================
 ("C26", r"\mathcal{L}_{\rm total} = \mathcal{L}_{\rm CMB}\times\mathcal{L}_{BAO}\times\mathcal{L}_{RSD}\times\mathcal{L}_{WL},",
  "Cap.23 §23.7 (C23.12)",
  "CONFERE SOB HIPÓTESE (extensão de C23.12 — mesma nota sobre a hipótese de independência entre probes)", False),
 ("C26", r"\mathcal{L}_{\rm total}, usando a linha de base como ponto de", "C26.01",
  "CONFERE (qualitativa — fragmento de prosa referenciando L_total de C26.01; flag sem-delimitador)", False),
 ("C26", r"\text{joelho escala-dependente em } f\sigma_8(k)", "Cap.23 §23.9 (C23.16)",
  "ERRO (repete a linguagem de \"joelho único\" já refutada — âncora D6; ver C23.16)", False),
 ("C26", r"C_\ell^{\phi\phi} \text{ e } f\sigma_8(z)", "Cap.25 §25.5 (C25.03); Cap.23 §23.3 (C23.05)",
  "CONFERE (qualitativa — nomeia observáveis já definidos em C25.03/C23.05)", False),
 ("C26", r"\alpha_0 \to 0", D6,
  "CONFERE SOB HIPÓTESE (critério de falseabilidade razoável em espírito, mas expresso em termos do α0 de 1 polo já refutado — âncora D6; precisa ser reformulado sobre a estrutura multi-polo real)", False),
 ("C26", r"\text{A teoria está em nível de confronto observacional real.}", f"{D6}, {D8}",
  "CONFERE SOB HIPÓTESE (qualitativa; mas ver âncora D6 — a forma específica do pipeline (μ,Σ,η_slip de 1 polo) usada para chegar a essa conclusão precisa ser reconstruída sobre a estrutura multi-polo real antes que a afirmação valha para a teoria derivada, não apenas para o ansatz fenomenológico)", False),
 ("C26", r"S_8 \text{ e } \alpha_0,m_{S0}", "—",
  "CONFERE (qualitativa — proposta de trabalho futuro, não uma afirmação a verificar)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("C22", "C23", "C24", "C25", "C26")
    textos = {}
    for pref in arquivos:
        with open(os.path.join(REG, pref + ".md"), encoding="utf-8") as fh:
            textos[pref] = re.split(r"(?=### \[)", fh.read())
    for pref, key, dep, ver, multi in V:
        blocos = textos[pref]
        hits = [i for i, b in enumerate(blocos)
                if b.startswith("### [") and key in b and "_(pendente)_" in b]
        if not hits:
            problemas.append(f"{pref}: '{key[:60]}' -> 0 pendentes")
            continue
        if len(hits) > 1 and not multi:
            problemas.append(f"{pref}: '{key[:60]}' -> {len(hits)} blocos")
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
