# -*- coding: utf-8 -*-
"""
r8a_quase_estatico_mu_sigma.py — R-8a (opcao C do dicionario de
epocas): mu(a,k), Sigma(a,k) e eta(a,k) QUASE-ESTATICOS do sistema
escalar 2-DOF corrigido — o "tamanho do alvo" observacional da F1.

CONTEXTO: saude interna fechada (resultado_r7e_saude_interna.md); a
viabilidade da F1 e agora pergunta exclusivamente observacional. A
opcao C (r8_dicionario_epocas_opcoes.md) calcula, antes de qualquer
Boltzmann, os parametros de gravidade modificada no regime
sub-horizonte:
    mu(a,k)    = resposta de Phi (potencial 00; dirige crescimento)
    Sigma(a,k) = resposta de (Phi+Psi)/2 (lensing)
    eta(a,k)   = Psi/Phi (slip)
Se mu,Sigma ~ 1 em toda a janela observavel, a F1 e viavel-mas-
indistinguivel no linear sub-horizonte; se ha desvio, ele dimensiona
o R-8 completo.

DESENHO (as tres decisoes que tornam isto limpo):
  1. GAUGE NEWTONIANO no setor g (a lib suporta): campos
     q = (Phi_g, Psi_g, Phi_f, Psi_f, B_f, E_f, dchi) — os potenciais
     de crescimento/lensing sao LIDOS DIRETO (sem mapa de Bardeen
     dependente do tempo). Convencoes da lib: g00 = -(1+2 Phi_g),
     gij = a^2(1-2 Psi_g) — padrao.
  2. LIMITE QUASE-ESTATICO: sub-horizonte (kh = k/aH >= 5), os
     potenciais respondem algebricamente: -W q + J = 0 => q* = W^-1 J
     (termos K/C caem com (aH/k)^2; a dispersao real do sistema —
     R-7a M3: omega ~ k/a — garante resposta rapida). Termos de massa
     de materia (rho_bar x metrica^2) caem na MESMA ordem e sao
     descartados NOS DOIS lados (declarado; erro ~(aH/k)^2 <= 4% em
     kh=5, some como 1/kh^2 — medido pela tendencia em kh).
  3. RAZAO BIMETRICO/GR: mu e Sigma sao definidos como razoes de
     resposta com a MESMA fonte unitaria J = e_{Phi_g} (a variacao
     dS_m/dPhi_g e a densidade: dust acopla so a g via T^00; T^ij=0)
     e o MESMO fundo H(a), rho(a) — toda normalizacao (fatores a^3,
     media-z, sinais, 4piG) CANCELA. O ramo GR = EH(g) + chi com
     Ub_GR = 3H^2 - rho_bar (o chi faz o papel da Lambda efetiva;
     mesmo H(a), mesmo Hd).

MEDIDAS (pre-declaradas): para beta1 in {1.0, 4.47}:
  grid a in {0.1, 0.3, 0.84, 3, 30, 300, 3000, 75000}
      (a_eq interna ~ 0.84: rho(a)=Lambda_eff; era de materia a<0.84)
  x kh in {5, 10, 30, 100, 300}:
      mu, Sigma, eta_bi, eta_GR, cond(W_bi).

GATES (pre-declarados; v2 apos a 1a rodada — a 1a esta no historico
git e ensinou o modelo de erro):
  V-GR-ETA v2: no ramo GR, eta_GR - 1 tem que escalar como C/kh^2
      (sao os termos H^2/Hdot da equacao de traco — fisica
      subdominante QS conhecida, NAO erro; a 1a rodada mediu o
      escalonamento quadratico perfeito com C ~ 14). Gate: ajuste
      eta_GR - 1 = C/kh^2 com residuo relativo < 0.15; C reportado.
      O C medido DEFINE a regiao QS-confiavel:
      kh_QS = sqrt(C/0.02) (erro QS < 2%).
  V-IR-MASSA: mu(kh=300) -> 1 dentro de 2% (o setor massivo
      desliga em k >> m — se nao, ha erro de montagem).
  V-COND: cond(W_bi equilibrada) < 1e10; ponto singular = reportar
      (possivel ressonancia fisica), nao abortar o grid.
  Fundo invalido em a pequeno (raiz do cubico) -> reportar e pular.

LEITURA (pre-declarada, v2 — restrita a regiao QS-CONFIAVEL
kh >= kh_QS; fora dela os numeros sao contaminados pela propria
aproximacao e NAO sao enunciado):
  max |mu-1|, |Sigma-1| <= 0.01 na regiao confiavel ->
      ALVO-SUBPERCENTUAL no sub-horizonte profundo; a janela
      quase-horizonte (kh < kh_QS) fica INDECIDIDA por esta sonda e
      vira o alvo do R-8 completo.
  desvios >= 0.05 na regiao confiavel -> ALVO-REAL: janela e forma.
  intermediario -> quantificar.
  Adicional: expoente de queda de |mu-1| vs kh (ajuste log-log nas
      colunas confiaveis + kh=10): p=2 e o esperado de (m a/k)^2;
      p>~4 indica cancelamento do termo lider (informativo de
      estrutura).

FRONTEIRA declarada: benchmark beta-constante (F'=F''=0), materia
so como fonte (sem massa-rho na metrica, valido kh>=5), unidades de
codigo (o mapeamento para z/k fisicos usa o dicionario — decisao do
autor; a_eq interna marcada como ancora).

Requer sympy, numpy. ~3-6 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r8a_quase_estatico_mu_sigma.py
Saida em auditoria/code/out/r8a_quase_estatico_mu_sigma.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (t, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices, lagrangian_GG,
                           interaction_lagrangian, chi_lagrangian,
                           scalar_metric_g, scalar_metric_f,
                           substitute_bg_functions, make_bg_functions,
                           z_average, eps_part, cut, symbolize)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'Psi_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
A_GRID = [0.1, 0.3, 0.84, 3.0, 30.0, 300.0, 3000.0, 75000.0]
KH_GRID = [5.0, 10.0, 30.0, 100.0, 300.0]
B1S = [1.0, 4.47]

MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-8a — mu(a,k), Sigma(a,k), eta(a,k) QUASE-ESTATICOS (opcao C)")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

# ------------------------------------------------------------------
# L2 BIMETRICA em gauge Newtoniano no setor g
# ------------------------------------------------------------------
say("[montagem] L2 bimetrica, gauge Newtoniano no setor g ...")
Phi_gF = sp.Function('Phi_g')(t)
Psi_gF = sp.Function('Psi_g')(t)
Phi_fF = sp.Function('Phi_f')(t)
Psi_fF = sp.Function('Psi_f')(t)
B_fF = sp.Function('B_f')(t)
E_fF = sp.Function('E_f')(t)
dchiF = sp.Function('dchi')(t)
FUNCS = [Phi_gF, Psi_gF, Phi_fF, Psi_fF, B_fF, E_fF, dchiF]

aF, bF, xiF, bg_rules = make_bg_functions()
gN = substitute_bg_functions(
    scalar_metric_g(Phi_gF, Psi_gF, None, None), aF, bF, xiF)
fN = substitute_bg_functions(
    scalar_metric_f(Phi_fF, Psi_fF, B_fF, E_fF), aF, bF, xiF)

Lg = lagrangian_GG(gN, Mg2)
Lf = lagrangian_GG(fN, Mf2)
Lint = interaction_lagrangian(gN, fN, dchi=dchiF)
Lchi = chi_lagrangian(gN, dchi=dchiF)
L2_bi = z_average(eps_part(cut(Lg + Lf + Lint + Lchi), 2))
L2s_bi, fields_bi, vels_bi = symbolize(L2_bi, FUNCS, bg_rules)
if [str(f) for f in fields_bi] != NOMES:
    raise RuntimeError(f"ordem de campos: {[str(f) for f in fields_bi]}")
_, _, W7 = quadratic_matrices(L2s_bi, fields_bi, vels_bi)
say("[montagem] W7 bimetrica pronta")

# ramo GR: EH(g Newtoniano) + chi (Ub = Lambda efetiva)
say("[montagem] L2 GR (EH_g + chi) ...")
FUNCS_GR = [Phi_gF, Psi_gF, dchiF]
L2_gr = z_average(eps_part(cut(lagrangian_GG(gN, Mg2)
                               + chi_lagrangian(gN, dchi=dchiF)), 2))
L2s_gr, fields_gr, vels_gr = symbolize(L2_gr, FUNCS_GR, bg_rules)
if [str(f) for f in fields_gr] != ['Phi_g', 'Psi_g', 'dchi']:
    raise RuntimeError("ordem de campos GR mudou")
_, _, W3 = quadratic_matrices(L2s_gr, fields_gr, vels_gr)
say("[montagem] W3 GR pronta")

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FW_BI = fatias(W7)
FW_GR = sp.lambdify(LIVRES, W3.subs(FIXOS).subs(
    {Fb: 0, Fp: 0, Fpp: 0}), modules='numpy')
say("[fatias] prontas")


def monta_bi(args, bvals):
    M = np.array(FW_BI['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(FW_BI[('Fb', n)](*args), float)
    return M


def fundo_bconst(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    r_esc = max(1e-14, 1e-6 * kap * B1V / max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-14:
        return None
    drdN = -3 * rho_til / dW
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = meff2 * r * r * Vf / (3.0 * MU)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int, rho=rho)


IDX = {n: i for i, n in enumerate(NOMES)}
J7 = np.zeros(7)
J7[IDX['Phi_g']] = 1.0
J3 = np.zeros(3)
J3[0] = 1.0


def matriz_D(kc):
    D = np.ones(7)
    D[IDX['B_f']] = 1.0 / kc
    D[IDX['E_f']] = 1.0 / kc**2
    return np.diag(D)


def resolve(B1V, a, kh):
    f = fundo_bconst(a, B1V)
    if f is None:
        return None
    kc = kh * a * f['H']
    args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
            f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
            f['Ub'], 0.0, 0.3, kc, 1.0, ME2)
    bvals = (B0V, B1V, B2V, 0.0, B4V)
    Wbi = monta_bi(args, bvals)
    D = matriz_D(kc)
    Wt = D @ (0.5 * (Wbi + Wbi.T)) @ D
    Jt = D @ J7
    cond = np.linalg.cond(Wt)
    if cond > 1e10:
        return dict(cond=cond, singular=True)
    qt = np.linalg.solve(Wt, Jt)
    q = D @ qt
    # ramo GR: mesmo fundo (H, Hd), Ub_GR = 3H^2 - rho (Lambda eff.)
    Ub_gr = 3.0 * f['H']**2 - f['rho']
    args_gr = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
               f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
               Ub_gr, 0.0, 0.3, kc, 1.0, ME2)
    Wgr = np.array(FW_GR(*args_gr), float)
    Wgr = 0.5 * (Wgr + Wgr.T)
    qg = np.linalg.solve(Wgr, J3)
    phi_bi, psi_bi = q[IDX['Phi_g']], q[IDX['Psi_g']]
    phi_gr, psi_gr = qg[0], qg[1]
    return dict(cond=cond, singular=False,
                mu=phi_bi / phi_gr,
                Sig=(phi_bi + psi_bi) / (phi_gr + psi_gr),
                eta_bi=psi_bi / phi_bi,
                eta_gr=psi_gr / phi_gr)


resultados = {}
for B1V in B1S:
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    # a_eq: igualdade rho_m = rho_Lambda = 3 H_tardio^2 (corrigido
    # pos-review: a 1a versao imprimia 0.84 hard-coded, errado)
    f_late = fundo_bconst(1e6, B1V)
    rho_L = 3.0 * f_late['H']**2
    a_eq = (RHO0 / rho_L) ** (1.0 / 3.0)
    say(f"    a_eq interna = {a_eq:.3f} (rho_m = rho_Lambda = "
        f"{rho_L:.3f}); m_T/H e funcao da epoca (~3.5 no Lambda "
        f"profundo)")
    say("")
    say(f"    {'a':>8} | " + " | ".join(f"kh={kh:g}".center(25)
                                        for kh in KH_GRID))
    say(f"    {'':>8} | " + " | ".join(f"{'mu':>8}{'Sigma':>9}"
                                       f"{'eta_bi':>8}"
                                       for kh in KH_GRID))
    mu_ir = []
    etas_gr = {}
    for a in A_GRID:
        linha = f"    {a:8.2f} |"
        for kh in KH_GRID:
            r = resolve(B1V, a, kh)
            if r is None:
                linha += " " + "fundo-inv".center(25) + " |"
                continue
            if r['singular']:
                linha += " " + f"SINGULAR c={r['cond']:.0e}".center(25) \
                    + " |"
                resultados[(B1V, a, kh)] = r
                continue
            linha += (f" {r['mu']:8.4f}{r['Sig']:9.4f}"
                      f"{r['eta_bi']:8.4f} |")
            etas_gr[(a, kh)] = r['eta_gr'] - 1.0
            if kh == 300.0:
                mu_ir.append(abs(r['mu'] - 1.0))
            resultados[(B1V, a, kh)] = r
        say(linha)
    say("")
    # V-GR-ETA v2: eta_GR - 1 = C/kh^2 (fisica QS subdominante)
    # fit de C em kh >= 10 (em kh=5 a propria serie QS esta a ~50% e
    # o termo D/kh^4 contamina o ajuste puro-quadratico)
    res_fit = 0.0
    Cs = []
    for a in A_GRID:
        pares = [(kh, etas_gr[(a, kh)]) for kh in KH_GRID
                 if (a, kh) in etas_gr and kh >= 10.0]
        if len(pares) < 3:
            continue
        C_a = np.mean([e * kh * kh for kh, e in pares])
        Cs.append(C_a)
        for kh, e in pares:
            res_fit = max(res_fit, abs(e - C_a / kh**2)
                          / max(abs(e), 1e-12))
    C_med = float(np.median(Cs)) if Cs else float('nan')
    ok_eta = res_fit < 0.15
    kh_qs = float(np.sqrt(abs(C_med) / 0.02)) if Cs else float('nan')
    say(f"    [V-GR-ETA v2 {'OK' if ok_eta else 'FALHOU'}] "
        f"eta_GR - 1 = C/kh^2 com C ~ {C_med:.1f} (residuo rel max "
        f"{res_fit:.3f} < 0.15); regiao QS-confiavel: kh >= "
        f"{kh_qs:.0f}")
    ok_ir = (max(mu_ir) < 0.02) if mu_ir else False
    say(f"    [V-IR-MASSA {'OK' if ok_ir else 'FALHOU'}] "
        f"max|mu(kh=300) - 1| = "
        f"{max(mu_ir) if mu_ir else float('nan'):.2e} (< 0.02)")
    # expoente de queda de |mu-1| vs kh (na era de materia, a=0.1)
    pares_p = [(kh, abs(resultados[(B1V, 0.1, kh)]['mu'] - 1.0))
               for kh in KH_GRID
               if (B1V, 0.1, kh) in resultados
               and not resultados[(B1V, 0.1, kh)].get('singular')
               and abs(resultados[(B1V, 0.1, kh)]['mu'] - 1.0) > 1e-6]
    if len(pares_p) >= 3:
        lx = np.log([p[0] for p in pares_p])
        ly = np.log([p[1] for p in pares_p])
        p_exp = -float(np.polyfit(lx, ly, 1)[0])
        say(f"    expoente de queda |mu-1| ~ kh^-p (a=0.1): "
            f"p = {p_exp:.2f} (p=2 esperado do termo (m a/k)^2; "
            f"p>~4 = cancelamento do lider)")
    resultados[(B1V, 'kh_qs')] = kh_qs

say("")
say("=" * 72)
say("VEREDITO R-8a (criterios pre-declarados no cabecalho)")
say("=" * 72)
des_max = 0.0
onde = None
des_max_all = 0.0
onde_all = None
for chave, r in resultados.items():
    if len(chave) != 3:
        continue
    B1V, a, kh = chave
    if r.get('singular') or 'mu' not in r:
        continue
    kh_qs = resultados.get((B1V, 'kh_qs'), 30.0)
    for nome, v in (('mu', r['mu']), ('Sigma', r['Sig'])):
        d = abs(v - 1.0)
        if d > des_max_all:
            des_max_all = d
            onde_all = (nome, B1V, a, kh, v)
        if kh >= kh_qs and d > des_max:
            des_max = d
            onde = (nome, B1V, a, kh, v)
if onde:
    say(f"  desvio maximo na regiao QS-CONFIAVEL: |{onde[0]}-1| = "
        f"{des_max:.4f} em beta1={onde[1]:g}, a={onde[2]:g}, "
        f"kh={onde[3]:g}")
if onde_all:
    say(f"  (grid inteiro, informativo: |{onde_all[0]}-1| = "
        f"{des_max_all:.4f} em beta1={onde_all[1]:g}, a={onde_all[2]:g},"
        f" kh={onde_all[3]:g} — mas kh < kh_QS e QS-contaminado; a")
    say("  janela quase-horizonte fica INDECIDIDA por esta sonda)")
sing = [chave for chave, r in resultados.items()
        if len(chave) == 3 and r.get('singular')]
if sing:
    say(f"  pontos SINGULARES (possivel ressonancia): {sing}")
if des_max <= 0.01:
    say("  >>> ALVO-SUBPERCENTUAL no sub-horizonte profundo: mu e")
    say("  Sigma dentro de 1% de GR na regiao QS-confiavel, nas duas")
    say("  eras e nos dois fundos. A janela quase-horizonte")
    say("  (kh <~ 10-25) e o alvo proprio do R-8 completo (dinamico),")
    say("  junto com as escalas super-horizonte do C_ell de baixo-ell.")
elif des_max >= 0.05:
    say("  >>> ALVO-REAL: desvio >= 5% na regiao confiavel — janela e")
    say("  forma acima; insumo do R-8 completo e do confronto com")
    say("  vinculos de crescimento.")
else:
    say(f"  >>> ALVO-INTERMEDIARIO: desvio maximo {des_max:.3f} na")
    say("  regiao confiavel — quantificado acima.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r8a_quase_estatico_mu_sigma.txt'),
          'w', encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r8a_quase_estatico_mu_sigma.txt")
