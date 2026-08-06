# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote08.py — vereditos do Lote 8 (Anexos C+D / AC+AD).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

D1 = "âncora D1 (derivations/01_setor_escalar_K_Omega.md)"
D2 = "âncora D2 (derivations/02_setor_tensorial_mT2.md)"

V = [
 # ================= AC (24) — setor escalar, território da âncora D1 =================
 ("AC", r"\bar g_{\mu\nu}dx^\mu dx^\nu = -dt^2 + a^2(t)\delta_{ij}dx^i dx^j,", "Anexo B §B.2",
  "CONFERE (fundo FLRW com N_g=1 fixado desde o início — escolha de gauge legítima, consistente com Anexo B §B.2)", False),
 ("AC", r"\bar f_{\mu\nu}dx^\mu dx^\nu = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j.", "Anexo B §B.2",
  "CONFERE (mesma forma padrão, setor f, com N_f geral)", False),
 ("AC", r"ds_g^2 = -(1+2\Phi_g)dt^2 + 2a\,\partial_i B_g\,dt\,dx^i + a^2\left[(1-2\Psi_g)\delta_{ij} + 2\partial_i\partial_j E_g\right]dx^i dx^j.",
  "—", "CONFERE (ansatz escalar geral padrão, 4 potenciais Φ,B,Ψ,E — forma-padrão da literatura de perturbações cosmológicas)", False),
 ("AC", r"ds_f^2 = -N_f^2(1+2\Phi_f)dt^2 + 2bN_f\,\partial_i B_f\,dt\,dx^i + b^2\left[(1-2\Psi_f)\delta_{ij} + 2\partial_i\partial_j E_f\right]dx^i dx^j.",
  "—", "CONFERE (mesma forma padrão, setor f, com o fator N_f do fundo)", False),
 ("AC", r"\chi(t,\mathbf{x}) = \bar\chi(t) + \delta\chi(t,\mathbf{x}).", "—",
  "CONFERE (decomposição padrão fundo+perturbação)", False),
 ("AC", r"\Delta\Psi \equiv \Psi_f - \Psi_g, \qquad \Delta E \equiv E_f - E_g, \qquad \delta\chi.", "—",
  "CONFERE (definições razoáveis de variáveis relativas)", False),
 ("AC", r"S = S^{(0)} + S^{(1)} + S^{(2)} + \cdots,", "—",
  "CONFERE (fato padrão de teoria de perturbações: o termo linear se anula em torno de uma solução clássica das equações de fundo)", False),
 ("AC", r"S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q_i\,K_{ij}(t,k)\,\dot Q_j - Q_i\,\Omega_{ij}(t,k)\,Q_j \right],",
  f"{D1}",
  "CONFERE SOB HIPÓTESE (forma template padrão da ação quadrática — kinética menos \"Ω\"; correta como estrutura genérica, mas a especialização para \"2 modos\" (§C.3) que a acompanha é a contagem refutada pela âncora D1 — real: 3 modos na análise de fundo congelado)", False),
 ("AC", r"\Omega_{ij} = \frac{k^2}{a^2}G_{ij}(t) + M_{ij}(t).", "—",
  "CONFERE (decomposição padrão gradiente+massa, forma geral esperada de uma ação quadrática relativística)", False),
 ("AC", r"\mathcal{C}_A(Q,\dot Q;k,t)=0.", "—",
  "CONFERE (fato padrão de sistemas com vínculos — variáveis sem derivada temporal geram constraints algébricas ao serem variadas)", False),
 ("AC", r"F(\chi)>0, \qquad \left|\frac{\dot F}{F}\right| \ll H, \qquad \left|\frac{F'}{F}\right|\Delta\chi \ll 1.",
  "Cap.6.2 §6.10 (lote 2)",
  "CONFERE (condições qualitativas razoáveis, análogas à adiabaticidade já usada no Cap.6.2 §6.10/lote 2)", False),
 ("AC", r"\det\left(c_s^2 K - G\right)=0.", "—",
  "CONFERE (forma padrão do problema de autovalor generalizado para extrair velocidades do som de um sistema com matriz cinética K e matriz de gradiente G)", False),
 ("AC", r"K^{-1}G.", "—",
  "CONFERE (equivalente padrão: c_s² são autovalores de K⁻¹G)", False),
 ("AC", r"c_s^2 \le 1", "—",
  "CONFERE (o próprio texto qualifica corretamente esta condição como \"não estritamente necessária em teorias efetivas, mas desejável\" — calibração adequada, sem superclaim)", False),
 ("AC", r"\exp\left(|c_s| \frac{k}{a} t\right),", "AC.14",
  "CONFERE (forma padrão de instabilidade de gradiente exponencial — consistente com ω imaginário quando c_s²<0)", False),
 ("AC", r"m_{eff}^2 \ge 2H^2.", "—",
  "CONFERE (importada — bound de Higuchi padrão para um campo spin-2 massivo genérico em dS, Higuchi 1987)", False),
 ("AC", r"K_{11} \to 0 \quad \text{em } m_{eff}^2\to 2H^2,", f"AC.17; {D1}",
  "ERRO DE FORMULAÇÃO — âncora D1: a identificação K_11↔Higuchi de um único campo massivo genérico não corresponde à estrutura real do setor escalar da TDCP-F1; o cômputo explícito (D1) encontra um par fantasma/degenerado que persiste \"dos dois lados\" de qualquer cruzamento de raiz (benchmarks A→B), não um K_11 único que troca de sinal suavemente em m_eff²=2H² — a intuição de gravidade massiva de campo único não se aplica diretamente ao sistema acoplado de 3 modos", False),
 ("AC", r"K_{11} > 0, \qquad K_{22} > 0, \qquad K_{11}K_{22}-K_{12}^2 > 0.",
  f"{D1}",
  "CONFERE (critério estrutural correto — cinética positiva definida ⟺ ausência de fantasma, válido para qualquer dimensão); mas herda a contagem de 2 modos de §C.3, já refutada pela âncora D1 (real: 3 modos, mesma tensão do Cap.6.2×Anexo C) — a matriz relevante deveria ser 3×3", False),
 ("AC", r"c_{s,\pm}^2 > 0.", f"AC.19; {D1}",
  "CONFERE (condição padrão de estabilidade de gradiente; mesma nota de AC.19 sobre a dimensão da matriz — critério estrutural correto, mas construído sobre a contagem de 2 modos refutada pela âncora D1)", True),
 ("AC", r"m^2F(\chi) \ge 2H^2.", "AC.18",
  "ERRO (herdado de AC.18 — a identificação com Higuchi de campo único não corresponde à estrutura real de 3 modos, âncora D1)", False),
 ("AC", r"\left|\frac{\dot F}{F}\right| \ll H.", "AC.11",
  "CONFERE (condição de adiabaticidade padrão, razoável independentemente da contagem de modos)", False),
 ("AC", r"\sqrt{-g}\,V(\mathcal{K}) \quad\to\quad \sqrt{-g}\,F(\chi)V(\mathcal{K}).",
  f"{D1}",
  "NÃO-DERIVÁVEL — âncora D1: \"SEM SUPORTE nos fundos testados — o terceiro modo escalar está presente e patológico no ramo dinâmico.\" O argumento qualitativo (F(χ) sem derivadas preserva a estrutura de constraints) pode valer para a ausência específica do ghost de Boulware-Deser, mas isso não implica ausência de OUTRAS patologias — o cômputo explícito de D1 encontra um par fantasma/taquiônico genuíno no ramo dinâmico, que este argumento qualitativo não previne nem menciona", False),
 ("AC", r"S^{(2)}_{\text{esc}} = \frac12\int dt\,d^3k\,a^3 \left[ \dot Q^T K \dot Q - Q^T\left(\frac{k^2}{a^2}G+M\right)Q \right].",
  f"AC.08; {D1}",
  "CONFERE (forma template padrão — kinética menos gradiente-e-massa; consistente com a forma que a âncora D1 de fato calculou explicitamente, embora com dimensão 3 em vez de 2 na análise real)", False),

 # ================= AD (19) — setor tensorial, território da âncora D2 =================
 ("AD", r"\partial_i h^{ij} = 0, \qquad h^i_{\ i}=0.", "—",
  "CONFERE (condição TT padrão)", False),
 ("AD", r"ds_g^2 = -dt^2 + a^2(t)\left(\delta_{ij}+h_{ij}\right)dx^i dx^j.", "—",
  "CONFERE (perturbação TT padrão do setor g, com N_g=1 fixado)", False),
 ("AD", r"ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\left(\delta_{ij}+\ell_{ij}\right)dx^i dx^j.", "—",
  "CONFERE (perturbação TT do setor f, mantendo N_f geral — consistente com Cap.16/âncora D2)", False),
 ("AD", r"S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 b^3 N_f^{-1}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 N_g F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right].",
  f"{D2} §3.1/§3.2",
  "CONFERE — âncora D2 §3.1: cinético e gradiente do setor f verificados exatamente (M_f²b³/N_f, com N_f=ξ quando N_g=1, e o termo de gradiente N_f²k²/b² correspondendo a c_f²=ξ²/r²); a estrutura de massa ∝(h-ℓ)² também confirmada (D2 §3.2), com M(r,ξ) deixado genérico aqui e especializado em §D.5", False),
 ("AD", r"S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ M_g^2 a^3\left(\dot h^2 - \frac{k^2}{a^2}h^2\right) + M_f^2 \frac{b^3}{N_f}\left(\dot \ell^2 - N_f^2\frac{k^2}{b^2}\ell^2\right) - 2m^2 M_{eff}^2 a^3 F(\chi)\,\mathcal{M}(r,\xi)\,(h-\ell)^2 \right].",
  f"AD.04; {D2} §3.1",
  "CONFERE — âncora D2 §3.1: mesma verificação de AD.04, agora com N_g=1 explícito; K_ℓℓ=M_f²b³/ξ e c_f²=ξ²/r² confirmados exatamente — verificado nesta auditoria por álgebra direta (N_f²k²/b²=(N_fa/b)²(k²/a²)=(ξ/r)²(k²/a²))", False),
 ("AD", r"h_+ \equiv \frac{M_g h + M_f r^{3/2}\ell}{\sqrt{M_g^2 + M_f^2 r^3}},",
  f"{D2} §4",
  "CONFERE — âncora D2 §4: esta é exatamente a \"base ponderada do Anexo D §D.4\" que a derivação cita como a forma correta de diagonalização (superior à combinação ingênua M_gh+M_frℓ do Cap.16 §16.3, que carece do expoente r^{1/2} e da normalização adequada); ortogonalidade verificada nesta auditoria: h_+·h_- ∝ M_g(M_fr^{3/2})+(M_fr^{3/2})(-M_g)=0", False),
 ("AD", r"h_- \equiv \frac{M_f r^{3/2} h - M_g \ell}{\sqrt{M_g^2 + M_f^2 r^3}}.", "AD.06",
  "CONFERE (par ortogonal de AD.06 — mesma verificação)", False),
 ("AD", r"S_T^{(2)}= \frac{1}{8}\int dt\,d^3k \left[ \mathcal{A}_+(t)\left(\dot h_+^2 - c_+^2\frac{k^2}{a^2}h_+^2\right) + \mathcal{A}_-(t)\left(\dot h_-^2 - c_-^2\frac{k^2}{a^2}h_-^2 - m_T^2(t) h_-^2\right) \right].",
  f"AD.06/07; {D2} §4",
  "CONFERE SOB HIPÓTESE (usa a base ponderada correta de AD.06/07 — melhor que o Cap.16 §16.3 — mas herda a mesma ressalva geral da âncora D2 §4: os gradientes c_g²≠c_f²=ξ²/r² não são simultaneamente diagonalizáveis com a massa em geral; a forma exatamente diagonal com c_+²,c_-² escalares é aproximação, mais precisa que a do Cap.16 por usar os pesos corretos, mas não exata)", False),
 ("AD", r"m_T^2(t) = m^2 F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f).", f"{D2} §3.3",
  "CONFERE (estrutura correta — μ_T² explicitamente função de ξ, ao contrário da omissão do Cap.16 §16.4; a forma fechada é dada pela âncora D2 §3.3)", True),
 ("AD", r"\mathcal{B}(r)\equiv \beta_1 + 2\beta_2 r + \beta_3 r^2.", "Anexo B §B.8 (AB.54)",
  "CONFERE (definição consistente com a mesma combinação usada na constraint de Bianchi, Anexo B §B.8/AB.54 — reduz a β1+2β2r quando β3=0, família F1)", False),
 ("AD", r"m_T^2(t)\propto m^2 F(\chi)\,\mathcal{B}(r)\,\left(\frac{1+r}{r}\right) \times \left(\text{fator de normalização em }M_g,M_f\right).",
  f"{D2} §3.3/§4",
  "ERRO DE CÁLCULO — âncora D2 §3.3/§4: esta forma (∝B(r)(1+r)/r, SEM ξ) é explicitamente substituída pela forma exata derivada: m_T²=m²F·M_eff²(1/M_g²+ξ/(M_f²r³))·r[β1+β2(ξ+r)+β3ξr] — que DEPENDE de ξ (ausente aqui) e cujo fator estrutural é β1+β2(ξ+r), não B(r)=β1+2β2r+β3r² (só coincidem se ξ=r); mesmo como \"forma representativa\" (o próprio texto hedge isso), está estruturalmente incompleta — falta a dependência em ξ que a âncora D2 mostra ser essencial, inclusive determinante do sinal de m_T² no benchmark testado", False),
 ("AD", r"\ddot h_- + 3H\dot h_- + \left(\frac{k^2}{a^2} + m_T^2(t)\right)h_- = 0.", "AD.08",
  "CONFERE SOB HIPÓTESE (forma padrão de EOM para um modo massivo em FLRW, consequência direta de AD.08 — herda a mesma ressalva sobre diagonalização aproximada)", True),
 ("AD", r"a(t)\propto e^{Ht}, \qquad H=\text{constante}.", "—",
  "CONFERE (definição padrão de fundo de Sitter)", False),
 ("AD", r"m_{\text{spin-2}}^2 \ge 2H^2.", "—",
  "CONFERE (importada — bound de Higuchi padrão para spin-2 massivo em de Sitter, Higuchi 1987)", False),
 ("AD", r"m_{\text{spin-2}}^2 \equiv m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots).", "AD.09",
  "CONFERE (identificação direta, consistente com AD.09)", False),
 ("AD", r"m_T^2(t) = m^2F(\chi)\,\mu_T^2(\cdots).", "AD.09/15 (reprise em §D.11)",
  "CONFERE (reprise de AD.09/15 na conclusão do anexo)", False),
 ("AD", r"m^2F(\chi)\,\mu_T^2(r,\xi,\beta_n,M_g,M_f) \ge 2H^2.", f"AD.09, AD.14; {D2}",
  "CONFERE (forma do bound correta e genérica — ao contrário do Cap.16, que substitui uma forma explícita errada, aqui μ_T² permanece genérico; usar a forma exata de μ_T² da âncora D2 para avaliar a condição)", False),
 ("AD", r"m_T^2(t)\ge 2H^2.", f"AD.16; {D2}",
  "CONFERE (reprise do bound de Higuchi genérico — âncora D2 para a forma exata de μ_T²)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AC", "AD")
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
