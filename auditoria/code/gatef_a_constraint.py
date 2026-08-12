# -*- coding: utf-8 -*-
"""
gatef_a_constraint.py — GATE F, etapa F-a: a direcao K<0 e um vinculo
disfarcado? (H-CONSTRAINT; docs/gate_fantasma_estrutural.md sec.2).
Inclui F-a3: a certificacao da banda do R-4 na superficie fisica —
pre-requisito do bloco observacional (decisao de sequencia do autor,
2026-08-12: F-a antes do bloco 3).

INTERPRETACAO OPERACIONAL DECLARADA (ajuste do enunciado do gate ao
nivel quadratico-dinamico; o autor pode vetar): a especificacao pedia
"a consistencia temporal das equacoes dos multiplicadores". Na rota
lagrangiana da nossa maquinaria, as equacoes dos 4 multiplicadores
sao resolvidas EXATAMENTE pela reducao (D1) — a consistencia temporal
delas e automatica, e o par primaria+secundaria do setor auxiliar ja
esta consumido. O conteudo testavel de H-CONSTRAINT que RESTA e a
versao dependente do tempo da constraint secundaria: uma das 3
direcoes reduzidas e RIGIDA (frequencia propria -> infinito, cresce
com a — R-2: "quer ser vinculo") e a dinamica fisica a expulsa
adiabaticamente: o fluxo colapsa sobre a superficie algebrica
  q_c ~ q_c*(q_l, qdot_l) = -(B'_cc)^-1 (B'_cl q_l + A'_cl qdot_l)
(linha c da EOM reduzida K q'' + A q' + B q = 0 na base propria de
K_red, com os termos cineticos da direcao rigida desprezados — ordem
adiabatica lider), deixando 2 graus de liberdade efetivos. Se essa
direcao rigida for a K<0, o fantasma estrutural e artefato de
representacao no nivel linear-dinamico. A construcao hamiltoniana
exata (teorema) fica para F-b se alguem exigir — aqui e medida.

FUNDOS: beta-constantes estaticos beta1=1 e beta1=4.47 (a classe; a
estrutura e universal se valer nos dois). Grade a=[100,80000],
npts=24000, k_c = 45*H(100)*100 (kh 45 -> 0.056: todos os regimes de
kh em uma rodada; mesma configuracao do R-4b -> lnA de referencia).

MEDIDAS E CRITERIOS PRE-DECLARADOS:
  F-a2 (IDENTIDADE; independencia de construcao): v_c = autovetor
      NEGATIVO de K_red (assinatura); v_h = autovetor do modo de MAIOR
      |omega^2| do QEP reduzido pre-escalado (K,C,W juntos). Criterio:
      mediana de |<v_h, v_c>| > 0.9 nos marcos com hierarquia R>=10.
      (R-2 viu "quer ser vinculo" congelado; aqui e ao longo do fluxo
      e por construcoes independentes.)
  F-a1-ADIA (RIGIDEZ): R = |omega_h|/max(|omega_2|, H) cresce e
      R_final >= 100; adiabaticidade eps = |Delta ln omega_h|/
      (omega_h Delta t) << 1 (impressa). Sem hierarquia nao ha
      vinculo dinamico — criterio necessario.
  F-a1-SUP (INVARIANCIA DA SUPERFICIE; o teste central): 4 ICs
      construidas SOBRE a superficie (q'_l ou qdot'_l unitarios;
      q'_c = q_c*; qdot'_c = 0) evoluidas com a maquinaria real.
      delta_rel = |q'_c - q_c*| / (|q_c*| + |q'_l|) nos marcos com
      R>=10. Criterio: mediana de delta_rel < 0.1 nas QUATRO ICs ->
      superficie quasi-invariante (contagem efetiva 2).
  F-a1-PODER (controle de poder; abortivo p/ SUP): a MESMA construcao
      com uma direcao LEVE como candidata falsa (autovalor positivo
      maior de K_red; ICs na direcao leve restante, com a direcao c
      posta na propria superficie p/ nao poluir). Criterio: mediana de
      delta_rel_fake >= 0.3 nas duas ICs — o teste TEM que reprovar a
      direcao errada; se "passar", SUP nao discrimina e NAO se
      interpreta.
  F-a-DESAC (diagnostico): IC puramente na direcao c (q'_c = 1, resto
      0): fracao leve L = |q'_l|/|q'| nos marcos — excitar o
      candidato a vinculo nao pode injetar dinamica leve (L < 0.2
      esperado; reportar).
  F-a3 (A BANDA NA SUPERFICIE; certificacao p/ o bloco 3): lnA de
      passagem (kh 20 -> 0.2, norma metrica, convencao R-4b) das ICs
      SOBRE a superficie vs das ICs genericas (medidas na mesma
      rodada; BASE: genericas devem reproduzir o R-4b: +3.97 em
      beta1=1, +3.62 em 4.47, tolerancia 0.4).
        |lnA_sup - lnA_gen| < 0.5      -> BANDA FISICA (certificada;
                                          bloco 3 em terreno firme);
        lnA_sup < 0.5 * lnA_gen        -> BANDA OFF-SURFACE (artefato
                                          de representacao — rever o
                                          R-4 antes de qualquer
                                          confronto observacional);
        senao                          -> intermediario (reportar).
  AGREGADO (ramos do gate, sec.3 do doc):
      F-a2 SIM + ADIA SIM + SUP SIM (com PODER ok) nos dois fundos ->
        H-CONSTRAINT (versao dinamica) CONFIRMADA: a direcao K<0 e a
        direcao rigida expulsa pela estrutura dependente do tempo;
        contagem efetiva tardia = 2; o fantasma estrutural e artefato
        de representacao NO NIVEL LINEAR-DINAMICO. Gate F fecha no
        ramo H-CONSTRAINT (enunciado com a honestidade declarada:
        versao adiabatica-dinamica, nao teorema hamiltoniano).
      Qualquer NAO -> H-CONSTRAINT nao confirmada neste nivel ->
        seguir para F-b (normalizacao canonica), como pre-declarado.

Requer sympy, numpy, scipy. ~5-9 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/gatef_a_constraint.py
Saida em auditoria/code/out/gatef_a_constraint.txt
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

from tdcp_pert_lib import (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
IDX_MET_IC_GEN = [0, 1, 3, 4]  # ICs metricas do conjunto generico
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 24000
KH_EDGES = [40.0, 20.0, 10.0, 6.0, 4.0, 2.5, 1.6, 1.0,
            0.7, 0.45, 0.3, 0.2, 0.1]
KH_PASS = (20.0, 0.2)
MARCAS = list(np.geomspace(150.0, 75000.0, 40))
R_HIER = 10.0
LNA_REF = {1.0: 3.97, 4.47: 3.62}

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("GATE F-a — A DIRECAO K<0 E VINCULO DISFARCADO? (+ F-a3: a banda)")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem + fatias (verbatim)
# ------------------------------------------------------------------
if not d1.gr_selfcheck():
    say("[!] V1 (GR selfcheck da biblioteca) falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

say("[fatias] {Fb,Fp,Fpp} x {b0..b4}, taxas livres ...")
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),
                      ('Fp', {Fb: 0, Fp: 1, Fpp: 0}),
                      ('Fpp', {Fb: 0, Fp: 0, Fpp: 1})):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW = fatias(K7), fatias(C7), fatias(W7)
say("[fatias] prontas")


def monta(fat, args, bvals, bp, bpp):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
        if bp[n]:
            M += bp[n] * np.array(fat[('Fp', n)](*args), float)
        if bpp[n]:
            M += bpp[n] * np.array(fat[('Fpp', n)](*args), float)
    return M


# ------------------------------------------------------------------
# fundo beta-constante + builder (verbatim R-4b)
# ------------------------------------------------------------------
def fundo_bconst(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-14:
        return None
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = meff2 * r * r * Vf / (3.0 * MU)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


def builder_bconst(B1V):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V)
            if f is None:
                raise RuntimeError(f"fundo beta-constante invalido em "
                                   f"a={a:.1f}")
            Hs_arr[p] = f['H']
            args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                    f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                    f['Ub'], 0.0, 0.3, kc, MF2, ME2)
            bvals = (B0V, B1V, B2V, 0.0, B4V)
            Ms['K'][p] = monta(FK, args, bvals, (0,) * 5, (0,) * 5)
            Ms['C'][p] = monta(FC, args, bvals, (0,) * 5, (0,) * 5)
            Ms['W'][p] = monta(FW, args, bvals, (0,) * 5, (0,) * 5)
        return Ns, Hs_arr, Ms
    return build


def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError(f"linha K do multiplicador {i} nao-nula")
        for j in range(n):
            cij = C[i, j]
            cd = Cdot[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(mult, mult)]
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(dyn, dyn)] + C[np.ix_(dyn, mult)] @ WXXi
            @ C[np.ix_(dyn, mult)].T,
            C[np.ix_(dyn, dyn)] - C[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)],
            W[np.ix_(dyn, dyn)] - W[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)])


def reduz_trilha(Ms, Ns, Hs_arr):
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    Kr = np.zeros((npts, 3, 3))
    Cr = np.zeros((npts, 3, 3))
    Wr = np.zeros((npts, 3, 3))
    p_fim = npts
    for p in range(npts):
        try:
            Kr[p], Cr[p], Wr[p] = reduz_ponto(
                Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], MULT, DYN)
        except RuntimeError as e:
            say(f"    [ESTRUTURA] reducao falhou em a={np.exp(Ns[p]):.1f}: "
                f"{e} — trilha truncada")
            p_fim = p
            break
    Ns_t, Hs_t = Ns[:p_fim], Hs_arr[:p_fim]
    Kr, Cr, Wr = Kr[:p_fim], Cr[:p_fim], Wr[:p_fim]
    Krd = np.gradient(Kr, Ns_t, axis=0) * Hs_t[:, None, None]
    Crd = np.gradient(Cr, Ns_t, axis=0) * Hs_t[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t


def janelas_kh(kc, Ns, Hs_arr):
    aas = np.exp(Ns)
    khs = kc / (aas * Hs_arr)
    a_of_kh = {}
    for kh in set(KH_EDGES) | set(KH_PASS):
        if khs[0] <= kh or khs[-1] >= kh:
            a_of_kh[kh] = None
        else:
            idx = int(np.argmax(khs <= kh))
            a_of_kh[kh] = float(aas[idx])
    jans = []
    for j in range(len(KH_EDGES) - 1):
        hi_kh, lo_kh = KH_EDGES[j], KH_EDGES[j + 1]
        a_in, a_out = a_of_kh[hi_kh], a_of_kh[lo_kh]
        if a_in is None or a_out is None:
            continue
        jans.append((f"kh{hi_kh:g}-{lo_kh:g}", a_in, a_out))
    if a_of_kh[KH_PASS[0]] is not None and a_of_kh[KH_PASS[1]] is not None:
        jans.append(("passagem", a_of_kh[KH_PASS[0]], a_of_kh[KH_PASS[1]]))
    return jans


# ------------------------------------------------------------------
# evolucao de UMA IC com diagnosticos de superficie nos marcos
# ------------------------------------------------------------------
def evolui_ic(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, q0, qd0,
              marcos):
    """marcos: lista de dicts {a, idx, E, Ap, Bp, H}. Devolve
    (dln_met por janela, registros por marco: (delta_c, delta_fake,
    L_leve, ln_met))."""
    npts = len(Ns)
    aas = np.exp(Ns)
    q = q0.copy()
    qd = qd0.copy()
    tcum = 0.0
    reg = {nome: [None] * 4 for nome, _, _ in janelas}
    recs = []
    im = 0
    for p in range(npts - 1):
        dN = Ns[p + 1] - Ns[p]
        dt = dN / Hs_arr[p]
        Ki = np.linalg.inv(Kr[p])
        A = Krd[p] + Cr[p] - Cr[p].T
        B = Crd[p] + Wr[p]

        def rhs(qq, vv):
            return -Ki @ (A @ vv + B @ qq)

        k1q, k1v = qd, rhs(q, qd)
        k2q, k2v = qd + .5 * dt * k1v, rhs(q + .5 * dt * k1q,
                                           qd + .5 * dt * k1v)
        k3q, k3v = qd + .5 * dt * k2v, rhs(q + .5 * dt * k2q,
                                           qd + .5 * dt * k2v)
        k4q, k4v = qd + dt * k3v, rhs(q + dt * k3q, qd + dt * k3v)
        q = q + dt * (k1q + 2 * k2q + 2 * k3q + k4q) / 6
        qd = qd + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        tcum += dt
        aa = aas[p + 1]
        n2_m = q[0]**2 + q[1]**2 + qd[0]**2 + qd[1]**2
        ln_m = np.log(max(np.sqrt(n2_m), 1e-300))
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is None and aa >= lo:
                r[0], r[1] = ln_m, tcum
            if r[2] is None and aa >= hi:
                r[2], r[3] = ln_m, tcum
        while im < len(marcos) and aa >= marcos[im]['a']:
            mk = marcos[im]
            E = mk['E']
            qp = E.T @ q
            qdp = E.T @ qd
            drec = {}
            for rot, jc in (('c', 0), ('fake', 2)):
                ol = [i for i in range(3) if i != jc]
                Bp, Ap = mk['Bp'], mk['Ap']
                qstar = -(Bp[jc, ol] @ qp[ol] + Ap[jc, ol] @ qdp[ol]) \
                    / Bp[jc, jc]
                esc = abs(qstar) + np.linalg.norm(qp[ol]) + 1e-300
                drec[rot] = abs(qp[jc] - qstar) / esc
            L = np.linalg.norm(qp[1:]) / max(np.linalg.norm(qp), 1e-300)
            recs.append((mk['a'], drec['c'], drec['fake'], L, ln_m))
            im += 1
    dln = {}
    tx = {}
    for nome, lo, hi in janelas:
        r = reg[nome]
        if r[0] is not None and r[2] is not None and r[3] > r[1]:
            dln[nome] = r[2] - r[0]
            tx[nome] = (r[2] - r[0]) / (r[3] - r[1])
        else:
            dln[nome] = float('nan')
            tx[nome] = float('nan')
    return dln, tx, recs


def qep_red(Kp, Cp, Wp):
    sK = max(np.max(np.abs(Kp)), 1e-30)
    return d1.agrupa_pares(d1.qep_modes(Kp / sK, Cp / sK, Wp / sK))


def mediana(xs):
    xs = [x for x in xs if np.isfinite(x)]
    return float(np.median(xs)) if xs else float('nan')


# ------------------------------------------------------------------
# analise por fundo
# ------------------------------------------------------------------
def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    say(f"    H(100)={f0['H']:.4f} -> k_c={kc:.1f} (kh 45 -> "
        f"{kc/(A_MAX*f0['H']):.3f})")
    build = builder_bconst(B1V)
    Ns, Hs_arr, Ms = build(kc, NPTS)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr)
    aas_t = np.exp(Ns_t)
    jans = janelas_kh(kc, Ns_t, Hs_t)

    # marcos: eigh de K_red + blocos A',B' na base propria + QEP
    marcos = []
    tab_qep = []
    for am in MARCAS:
        if am > aas_t[-1]:
            break
        idx = int(np.argmin(np.abs(aas_t - am)))
        Ksym = 0.5 * (Kr[idx] + Kr[idx].T)
        lam, E = np.linalg.eigh(Ksym)
        if lam[0] >= 0 or lam[1] <= 0:
            say(f"    [!] assinatura inesperada de K_red em a={am:.0f}: "
                f"{lam} — marco pulado")
            continue
        A = Krd[idx] + Cr[idx] - Cr[idx].T
        B = Crd[idx] + Wr[idx]
        mk = dict(a=float(aas_t[idx]), idx=idx, E=E,
                  Ap=E.T @ A @ E, Bp=E.T @ B @ E, H=Hs_t[idx])
        pares = qep_red(Kr[idx], Cr[idx], Wr[idx])
        proj = R = omh = float('nan')
        if len(pares) >= 2:
            pares.sort(key=lambda mm: abs(mm['omega2']))
            vh = np.asarray(pares[-1]['v'], complex)
            omh = abs(np.sqrt(complex(pares[-1]['omega2'])))
            om2 = abs(np.sqrt(complex(pares[-2]['omega2'])))
            R = omh / max(om2, Hs_t[idx])
            vc = E[:, 0]
            proj = abs(np.conjugate(vh) @ vc) / max(
                np.linalg.norm(vh) * np.linalg.norm(vc), 1e-300)
        mk['R'] = R
        mk['proj'] = proj
        mk['omh'] = omh
        marcos.append(mk)
        tab_qep.append(mk)

    if not tab_qep:
        say("    [!] nenhum marco valido — abortando este fundo")
        return dict(ok_a2=False, ok_adia=False, ok_sup=False,
                    ok_poder=False, v_a3='INDISPONIVEL',
                    lnA_gen=float('nan'), lnA_sup=float('nan'),
                    proj=float('nan'), ok_base=False)
    say("")
    say("    F-a2/ADIA — hierarquia e identidade ao longo do fluxo:")
    say(f"    {'a':>8} {'kh':>7} {'|om_h|/H':>9} {'R':>9} "
        f"{'|<v_h,v_c>|':>11}")
    for mk in tab_qep[::4] + [tab_qep[-1]]:
        kh = kc / (mk['a'] * mk['H'])
        say(f"    {mk['a']:8.0f} {kh:7.2f} {mk['omh']/mk['H']:9.1f} "
            f"{mk['R']:9.1f} {mk['proj']:11.3f}")
    marcos_h = [mk for mk in marcos if np.isfinite(mk['R'])
                and mk['R'] >= R_HIER]
    proj_med = mediana([mk['proj'] for mk in marcos_h])
    R_fim = tab_qep[-1]['R']
    a_hier = marcos_h[0]['a'] if marcos_h else float('nan')
    say(f"    hierarquia R>={R_HIER:g} a partir de a~{a_hier:.0f} "
        f"({len(marcos_h)}/{len(marcos)} marcos); R_final={R_fim:.0f}")
    ok_a2 = np.isfinite(proj_med) and proj_med > 0.9
    ok_adia = np.isfinite(R_fim) and R_fim >= 100 and len(marcos_h) >= 10
    say(f"    [F-a2 {'SIM' if ok_a2 else 'NAO'}] mediana |<v_h,v_c>| = "
        f"{proj_med:.3f} (criterio > 0.9, marcos com R>={R_HIER:g})")
    say(f"    [F-a1-ADIA {'SIM' if ok_adia else 'NAO'}] R_final = "
        f"{R_fim:.0f} (criterio >= 100)")

    # conjuntos de ICs
    mk0_idx = 0
    Ksym0 = 0.5 * (Kr[mk0_idx] + Kr[mk0_idx].T)
    lam0, E0 = np.linalg.eigh(Ksym0)
    A0 = Krd[mk0_idx] + Cr[mk0_idx] - Cr[mk0_idx].T
    B0 = Crd[mk0_idx] + Wr[mk0_idx]
    Ap0, Bp0 = E0.T @ A0 @ E0, E0.T @ B0 @ E0

    def ic_superficie(jc, lightset):
        """lightset: lista de (tipo, indice-proprio). Poe q'_jc na
        superficie do candidato jc; demais direcoes dadas."""
        ics = []
        ol = [i for i in range(3) if i != jc]
        for tipo, li in lightset:
            qp = np.zeros(3)
            qdp = np.zeros(3)
            if tipo == 'q':
                qp[li] = 1.0
            else:
                qdp[li] = 1.0
            qp[jc] = -(Bp0[jc, ol] @ qp[ol] + Ap0[jc, ol] @ qdp[ol]) \
                / Bp0[jc, jc]
            ics.append((E0 @ qp, E0 @ qdp))
        return ics

    ics_gen = []
    for ic in range(6):
        q0 = np.zeros(3)
        qd0 = np.zeros(3)
        if ic < 3:
            q0[ic] = 1.0
        else:
            qd0[ic - 3] = 1.0
        ics_gen.append((q0, qd0))
    ics_sup = ic_superficie(0, [('q', 1), ('q', 2), ('qd', 1), ('qd', 2)])
    # fake: candidato = direcao propria 2 (autovalor positivo maior);
    # ICs na direcao leve 1, com a direcao c posta na propria superficie
    ics_fake = []
    for tipo in ('q', 'qd'):
        qp = np.zeros(3)
        qdp = np.zeros(3)
        if tipo == 'q':
            qp[1] = 1.0
        else:
            qdp[1] = 1.0
        qp[2] = -(Bp0[2, [0, 1]] @ qp[[0, 1]]
                  + Ap0[2, [0, 1]] @ qdp[[0, 1]]) / Bp0[2, 2]
        qp[0] = -(Bp0[0, [1, 2]] @ qp[[1, 2]]
                  + Ap0[0, [1, 2]] @ qdp[[1, 2]]) / Bp0[0, 0]
        ics_fake.append((E0 @ qp, E0 @ qdp))
    ics_des = [(E0 @ np.array([1.0, 0.0, 0.0]), np.zeros(3))]

    def roda_set(rot, ics):
        outs = []
        for (q0, qd0) in ics:
            outs.append(evolui_ic(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t,
                                  jans, q0, qd0, marcos))
        return outs

    say("")
    say("    evoluindo conjuntos de ICs (6 gen + 4 sup + 2 fake + 1 des)...")
    o_gen = roda_set('gen', ics_gen)
    o_sup = roda_set('sup', ics_sup)
    o_fake = roda_set('fake', ics_fake)
    o_des = roda_set('des', ics_des)

    a_ok = set(mk['a'] for mk in marcos_h)

    def med_delta(outs, campo):
        meds = []
        for (_, _, recs) in outs:
            vals = [rc[1] if campo == 'c' else rc[2]
                    for rc in recs if rc[0] in a_ok]
            meds.append(mediana(vals))
        return meds

    med_sup = med_delta(o_sup, 'c')
    med_fake = med_delta(o_fake, 'fake')
    med_gen = med_delta(o_gen, 'c')
    ok_sup = all(np.isfinite(m) and m < 0.1 for m in med_sup)
    ok_poder = all(np.isfinite(m) and m >= 0.3 for m in med_fake)
    say("")
    say(f"    [F-a1-SUP {'SIM' if ok_sup else 'NAO'}] mediana delta_rel "
        f"(4 ICs na superficie, marcos R>={R_HIER:g}): "
        + " ".join(f"{m:.3f}" for m in med_sup) + "  (criterio < 0.1)")
    say(f"    [F-a1-PODER {'OK' if ok_poder else 'FALHOU'}] mediana "
        f"delta_rel da superficie FALSA (2 ICs): "
        + " ".join(f"{m:.3f}" for m in med_fake)
        + "  (criterio >= 0.3 — o teste tem que reprovar a direcao leve)")
    say(f"    diagnostico: delta_rel das ICs GENERICAS (colapso ao "
        f"longo do fluxo): " + " ".join(f"{m:.2f}" for m in med_gen))
    recs_d = o_des[0][2]
    Ls = [rc[3] for rc in recs_d if rc[0] in a_ok]
    L_max = max(Ls) if Ls else float('nan')
    say(f"    [F-a-DESAC] fracao leve max da IC pura-c: {L_max:.3f} "
        f"(esperado < 0.2; diagnostico)")
    say("    perfis delta_rel (IC 1 de cada conjunto; ~8 marcos):")
    say(f"    {'a':>8} {'sup(c)':>8} {'fake':>8} {'gen(c)':>8}")
    rs, rf, rg = o_sup[0][2], o_fake[0][2], o_gen[0][2]
    passo = max(1, len(rs) // 8)
    for j in range(0, len(rs), passo):
        say(f"    {rs[j][0]:8.0f} {rs[j][1]:8.3f} "
            f"{rf[j][2] if j < len(rf) else float('nan'):8.3f} "
            f"{rg[j][1] if j < len(rg) else float('nan'):8.3f}")

    # F-a3 — a banda na superficie
    vg = [o_gen[i][0].get('passagem', float('nan'))
          for i in IDX_MET_IC_GEN]
    vg = [v for v in vg if np.isfinite(v)]
    lnA_gen = max(vg) if vg else float('nan')
    vs = [dln.get('passagem', float('nan')) for (dln, _, _) in o_sup]
    vs = [v for v in vs if np.isfinite(v)]
    lnA_sup = max(vs) if vs else float('nan')
    ok_base = (np.isfinite(lnA_gen)
               and abs(lnA_gen - LNA_REF[B1V]) < 0.4)
    say("")
    say(f"    [F-a3-BASE {'OK' if ok_base else 'FALHOU'}] lnA_passagem "
        f"generico = {lnA_gen:+.2f} (ref R-4b {LNA_REF[B1V]:+.2f}, "
        f"tol 0.4)")
    say(f"    lnA_passagem na SUPERFICIE = {lnA_sup:+.2f}")
    if np.isfinite(lnA_sup) and np.isfinite(lnA_gen):
        if abs(lnA_sup - lnA_gen) < 0.5:
            v_a3 = 'BANDA-FISICA'
        elif lnA_sup < 0.5 * lnA_gen:
            v_a3 = 'BANDA-OFF-SURFACE'
        else:
            v_a3 = 'INTERMEDIARIO'
    else:
        v_a3 = 'INDISPONIVEL'
    say(f"    [F-a3 => {v_a3}]")
    say("    forma comparada (taxa met por faixa de kh, max ICs):")
    say(f"    {'janela':<12} {'gen':>7} {'sup':>7}")
    for nome, lo, hi in jans:
        if nome == 'passagem':
            continue
        tg = max((tx[nome] / 1.0 for (_, tx, _) in
                  [o_gen[i] for i in IDX_MET_IC_GEN]
                  if np.isfinite(tx[nome])), default=float('nan'))
        ts = max((tx[nome] for (_, tx, _) in o_sup
                  if np.isfinite(tx[nome])), default=float('nan'))
        Hj = Hs_t[int(np.argmin(np.abs(aas_t - np.sqrt(lo * hi))))]
        say(f"    {nome:<12} {tg/Hj:+7.2f} {ts/Hj:+7.2f}")

    return dict(ok_a2=ok_a2, ok_adia=ok_adia, ok_sup=ok_sup,
                ok_poder=ok_poder, v_a3=v_a3, lnA_gen=lnA_gen,
                lnA_sup=lnA_sup, proj=proj_med, ok_base=ok_base)


RES = {}
for B1V in (1.0, 4.47):
    RES[B1V] = analisa(B1V)

# ------------------------------------------------------------------
# veredito agregado
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO GATE F-a (criterios pre-declarados no cabecalho)")
say("=" * 72)
for B1V, r in RES.items():
    say(f"  beta1={B1V:g}: F-a2 {'SIM' if r['ok_a2'] else 'NAO'} "
        f"(proj {r['proj']:.3f}); ADIA {'SIM' if r['ok_adia'] else 'NAO'}; "
        f"SUP {'SIM' if r['ok_sup'] else 'NAO'} "
        f"(PODER {'ok' if r['ok_poder'] else 'FALHOU'}); "
        f"F-a3 {r['v_a3']} (gen {r['lnA_gen']:+.2f} / sup "
        f"{r['lnA_sup']:+.2f}; BASE {'ok' if r['ok_base'] else 'FALHOU'})")
say("")
todos = list(RES.values())
poder_ok = all(r['ok_poder'] for r in todos)
base_ok = all(r['ok_base'] for r in todos)
if not poder_ok:
    say("  >>> PODER FALHOU: o teste de superficie nao discrimina a")
    say("  direcao errada — NAO INTERPRETAR SUP; rever a construcao")
    say("  antes de qualquer ramo do gate.")
elif not base_ok:
    say("  >>> BASE FALHOU: o generico nao reproduz o R-4b — drift de")
    say("  ambiente/arquivo; diagnosticar antes de interpretar.")
elif all(r['ok_a2'] and r['ok_adia'] and r['ok_sup'] for r in todos):
    say("  >>> H-CONSTRAINT (VERSAO DINAMICA) CONFIRMADA nos dois")
    say("  fundos: a direcao K<0 e a direcao RIGIDA que a estrutura")
    say("  dependente do tempo expulsa (superficie quasi-invariante;")
    say("  identidade v_h~v_c; hierarquia crescente). Contagem efetiva")
    say("  tardia = 2. O FANTASMA ESTRUTURAL E ARTEFATO DE")
    say("  REPRESENTACAO no nivel linear-dinamico — o gate fecha no")
    say("  ramo H-CONSTRAINT (honestidade declarada: versao")
    say("  adiabatica-dinamica; a construcao hamiltoniana exata fica")
    say("  como fronteira, F-b opcional). A F1 fica SEM patologia")
    say("  escalar linear conhecida alem do transiente de banda do")
    say("  R-4 — e o F-a3 acima diz se a banda e fisica.")
else:
    say("  >>> H-CONSTRAINT NAO confirmada neste nivel (ver qual")
    say("  criterio falhou acima) — seguir para F-b (normalizacao")
    say("  canonica), como pre-declarado no gate.")
say("")
say("  F-a3 agregado: " + "; ".join(
    f"beta1={B1V:g}: {r['v_a3']}" for B1V, r in RES.items()))
say("  (BANDA-FISICA nos dois -> bloco 3 em terreno firme;")
say("  BANDA-OFF-SURFACE em qualquer um -> rever R-4 antes do bloco 3.)")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "gatef_a_constraint.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/gatef_a_constraint.txt")
