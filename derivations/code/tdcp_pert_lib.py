# -*- coding: utf-8 -*-
"""
tdcp_pert_lib.py — Biblioteca compartilhada de teoria de perturbacoes
cosmologicas para a TDCP bimetrica (usada pelos scripts 01, 02 e 06).

Conteudo:
  - aritmetica de series truncadas em epsilon (ordem 2);
  - inversa e sqrt de matrizes por series;
  - Lagrangiana de Einstein "Gamma-Gamma" (so primeiras derivadas;
    difere de sqrt(-g)R por derivada total — verificado por assert
    contra a Lagrangiana minisuperespaco do Anexo B §B.4.5);
  - raiz quadrada matricial A = sqrt(g^{-1} f) ordem a ordem via
    equacoes de Sylvester (plano P1.2/P2.1);
  - polinomios simetricos elementares e_n(A) via tracos (P1.3);
  - media espacial em z dos modos cos(kz)/sin(kz);
  - extracao de matrizes K, C, W de uma Lagrangiana quadratica e
    absorcao da parte simetrica de C (W_eff = W + d/dt C_sym);
  - eliminacao iterativa de variaveis auxiliares (sem velocidade);
  - benchmark numerico de fundo consistente com as Friedmann g/f.

Rode  `python tdcp_pert_lib.py`  para executar os auto-testes.
"""
import sympy as sp

# ----------------------------------------------------------------------
# simbolos globais
# ----------------------------------------------------------------------
eps = sp.Symbol('epsilon')
t, z = sp.symbols('t z')
k = sp.Symbol('k', positive=True)

# fundo (simbolos "congelados no instante t", usados apos simbolizacao)
a_s, b_s, xi_s, r_s = sp.symbols('a b xi r', positive=True)
H_s, Hf_s, Hd_s, Hfd_s, xid_s = sp.symbols('H H_f Hdot H_fdot xidot')
chid_s, chidd_s = sp.symbols('chidot chiddot')
Mg2, Mf2, m2, Meff2 = sp.symbols('M_g^2 M_f^2 m^2 M_eff^2', positive=True)
b0, b1, b2, b3, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4')
Fb, Fp, Fpp = sp.symbols('Fbar Fprime Fpp')
Ub, Up, Upp = sp.symbols('Ubar Uprime Upp')
rho_s = sp.symbols('rho_m', positive=True)

BETAS = (b0, b1, b2, b3, b4)


# ----------------------------------------------------------------------
# series truncadas em epsilon
# ----------------------------------------------------------------------
def cut(expr, order=2):
    """Trunca uma expressao polinomial em eps mantendo ordens 0..order."""
    e = sp.expand(expr)
    return sp.Add(*[e.coeff(eps, i) * eps**i for i in range(order + 1)])


def cutM(M, order=2):
    return M.applyfunc(lambda e: cut(e, order))


def eps_part(expr, i):
    return sp.expand(expr).coeff(eps, i)


def series_inverse(M):
    """Inversa de M = M0 + eps M1 + eps^2 M2 ate O(eps^2)."""
    M0 = M.applyfunc(lambda e: eps_part(e, 0))
    M1 = M.applyfunc(lambda e: eps_part(e, 1))
    M2 = M.applyfunc(lambda e: eps_part(e, 2))
    M0i = M0.inv()
    inv = (M0i - eps * (M0i * M1 * M0i)
           + eps**2 * (M0i * M1 * M0i * M1 * M0i - M0i * M2 * M0i))
    return cutM(inv)


def series_sqrt_scalar(d):
    """sqrt(d0 + eps d1 + eps^2 d2) ate O(eps^2), d0 > 0."""
    d0, d1, d2 = eps_part(d, 0), eps_part(d, 1), eps_part(d, 2)
    u1, u2 = d1 / d0, d2 / d0
    return sp.sqrt(d0) * (1 + eps * u1 / 2 + eps**2 * (u2 / 2 - u1**2 / 8))


def sqrt_minus_det(g):
    return cut(series_sqrt_scalar(cut(-g.det())))


# ----------------------------------------------------------------------
# geometria: Christoffel e Lagrangiana Gamma-Gamma (1as derivadas)
# ----------------------------------------------------------------------
COORDS = (t, sp.Symbol('x'), sp.Symbol('y'), z)


def christoffel(g, ginv):
    n = 4
    dg = [[[cut(sp.diff(g[i, j], c)) for j in range(n)] for i in range(n)]
          for c in COORDS]
    Gam = [[[None] * n for _ in range(n)] for _ in range(n)]
    for lam in range(n):
        for mu in range(n):
            for nu in range(mu, n):
                s = sp.Integer(0)
                for sig in range(n):
                    s += ginv[lam, sig] * (dg[mu][sig][nu] + dg[nu][sig][mu]
                                           - dg[sig][mu][nu])
                s = cut(s / 2)
                Gam[lam][mu][nu] = s
                Gam[lam][nu][mu] = s
    return Gam


def lagrangian_GG(g, Mpl2):
    """
    Lagrangiana de Einstein na forma Gamma-Gamma (so 1as derivadas):
        L = (Mpl2/2) sqrt(-g) g^{mu nu} (Gam^s_{mu l} Gam^l_{nu s}
                                         - Gam^l_{mu nu} Gam^s_{l s})
    Igual a (Mpl2/2) sqrt(-g) R a menos de derivada total.
    Verificacao (auto-teste): para FLRW plano com lapse N,
    L_GG = -3 Mpl2 a adot^2 / N  (Anexo B §B.4.5).
    """
    ginv = series_inverse(g)
    Gam = christoffel(g, ginv)
    n = 4
    term = sp.Integer(0)
    for mu in range(n):
        for nu in range(n):
            s1 = sp.Integer(0)
            s2 = sp.Integer(0)
            for lam in range(n):
                for sig in range(n):
                    s1 += Gam[sig][mu][lam] * Gam[lam][nu][sig]
                s2 += Gam[lam][mu][nu] * sum(Gam[sig][lam][sig] for sig in range(n))
            term += ginv[mu, nu] * cut(s1 - s2)
    return cut(Mpl2 / 2 * sqrt_minus_det(g) * cut(term))


# ----------------------------------------------------------------------
# raiz quadrada matricial via Sylvester (P1.2/P2.1)
# ----------------------------------------------------------------------
def matrix_sqrt_series(M):
    """
    A = sqrt(M) ate O(eps^2), com M0 = A0^2 diagonal.
    Sylvester: A0 A1 + A1 A0 = M1;  A0 A2 + A2 A0 = M2 - A1^2.
    """
    M0 = M.applyfunc(lambda e: eps_part(e, 0))
    M1 = M.applyfunc(lambda e: eps_part(e, 1))
    M2 = M.applyfunc(lambda e: eps_part(e, 2))
    if not M0.is_diagonal():
        raise ValueError("M0 precisa ser diagonal para o solver de Sylvester")
    lam = [sp.sqrt(M0[i, i]) for i in range(4)]
    A0 = sp.diag(*lam)
    A1 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            A1[i, j] = sp.cancel(M1[i, j] / (lam[i] + lam[j]))
    R2 = M2 - A1 * A1
    A2 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            A2[i, j] = sp.cancel(sp.expand(R2[i, j]) / (lam[i] + lam[j]))
    A = A0 + eps * A1 + eps**2 * A2
    return cutM(A)


def elementary_symmetric(A):
    """e_0..e_4 de A (4x4) via tracos e determinante, truncados."""
    t1 = cut(A.trace())
    A2m = cutM(A * A)
    t2 = cut(A2m.trace())
    t3 = cut((A2m * A).trace())
    e0 = sp.Integer(1)
    e1 = t1
    e2 = cut((t1**2 - t2) / 2)
    e3 = cut((t1**3 - 3 * t1 * t2 + 2 * t3) / 6)
    e4 = cut(A.det())
    return e0, e1, e2, e3, e4


# ----------------------------------------------------------------------
# media espacial em z (modos cos(kz), sin(kz))
# ----------------------------------------------------------------------
def z_average(expr):
    """
    Media sobre um periodo em z. Valida para Lagrangianas quadraticas
    onde cada termo tem no maximo 2 fatores trigonometricos.
    """
    e = sp.expand(expr)
    e = e.subs(sp.sin(k * z) * sp.cos(k * z), 0)
    e = e.subs({sp.cos(k * z)**2: sp.Rational(1, 2),
                sp.sin(k * z)**2: sp.Rational(1, 2)})
    e = e.subs({sp.cos(k * z): 0, sp.sin(k * z): 0})
    return sp.expand(e)


# ----------------------------------------------------------------------
# simbolizacao: Function(t) -> simbolos campo/velocidade
# ----------------------------------------------------------------------
def symbolize(expr, funcs, bg_rules):
    """
    funcs: lista de sp.Function aplicadas em t (perturbacoes).
    bg_rules: dict {Derivative(bgfunc, t): expressao, bgfunc: simbolo}.
    Retorna (expr_simbolizada, campos, velocidades).
    """
    fields, vels = [], []
    sub = {}
    for F in funcs:
        name = F.func.__name__
        fs = sp.Symbol(name)
        vs = sp.Symbol(name + 'dot')
        sub[sp.Derivative(F, t)] = vs
        sub[F] = fs
        fields.append(fs)
        vels.append(vs)
    e = expr.subs(sub)
    e = e.subs(bg_rules)
    return sp.expand(e), fields, vels


# derivada temporal total de expressoes simbolizadas (regras de fundo)
RATES = {
    a_s: a_s * H_s,
    b_s: b_s * xi_s * Hf_s,          # H_f = bdot/(N_f b), N_f = xi
    xi_s: xid_s,
    H_s: Hd_s,
    Hf_s: Hfd_s,
    chid_s: chidd_s,
    Fb: Fp * chid_s,
    Fp: Fpp * chid_s,
    Ub: Up * chid_s,
    Up: Upp * chid_s,
    rho_s: -3 * H_s * rho_s,        # materia fria
}


def dt_background(expr, extra_rates=None):
    rates = dict(RATES)
    if extra_rates:
        rates.update(extra_rates)
    out = sp.Integer(0)
    for s, rate in rates.items():
        d = sp.diff(expr, s)
        if d != 0:
            out += d * rate
    return sp.expand(out)


# ----------------------------------------------------------------------
# extracao K, C, W de L2 e absorcao de C_sym
# ----------------------------------------------------------------------
def quadratic_matrices(L2, fields, vels):
    """
    L2 = 1/2 qdot^T K qdot + qdot^T C q - 1/2 q^T W q  (+ const)
    Retorna (K, C, W).
    """
    n = len(fields)
    K = sp.zeros(n, n)
    C = sp.zeros(n, n)
    W = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            K[i, j] = sp.expand(sp.diff(L2, vels[i], vels[j]))
            C[i, j] = sp.expand(sp.diff(L2, vels[i], fields[j]))
            W[i, j] = sp.expand(-sp.diff(L2, fields[i], fields[j]))
    return K, C, W


def effective_mass_matrix(W, C, extra_rates=None):
    """W_eff = W + d/dt[(C + C^T)/2] (parte simetrica absorvida)."""
    S = (C + C.T) / 2
    dS = S.applyfunc(lambda e: dt_background(e, extra_rates))
    return sp.expand(W + dS), sp.expand((C - C.T) / 2)


# ----------------------------------------------------------------------
# reducao matricial (complemento de Schur) — evita substituicao em
# expressoes gigantes; todas as operacoes em blocos com cancel()
# ----------------------------------------------------------------------
def _cancelM(M):
    return M.applyfunc(lambda e: sp.cancel(sp.together(e)))


def schur_eliminate(K, C, W, idx_aux, verbose=True):
    """
    Elimina variaveis auxiliares por complemento de Schur.
    L = 1/2 qdot^T K qdot + qdot^T C q - 1/2 q^T W q, q = (Q, X):
    exige K[X,:] = 0 e C[X,:] = 0 (sem Xdot em L).
    X* = W_XX^{-1} (C_QX^T Qdot - W_XQ Q); substituindo:
      K_eff = K_QQ + C_QX W_XX^{-1} C_QX^T
      C_eff = C_QQ - C_QX W_XX^{-1} W_XQ
      W_eff = W_QQ - W_QX W_XX^{-1} W_XQ
    Retorna (K_eff, C_eff, W_eff, idx_dyn).
    """
    n = K.shape[0]
    idx_dyn = [i for i in range(n) if i not in idx_aux]
    for i in idx_aux:
        for j in range(n):
            if sp.cancel(K[i, j]) != 0 or sp.cancel(C[i, j]) != 0:
                raise ValueError(f"variavel {i} tem velocidade em L "
                                 f"(K/C linha nao nula) — nao e auxiliar")
    KQQ = K[idx_dyn, idx_dyn]
    CQQ = C[idx_dyn, idx_dyn]
    CQX = C[idx_dyn, idx_aux]
    WQQ = W[idx_dyn, idx_dyn]
    WQX = W[idx_dyn, idx_aux]
    WXQ = W[idx_aux, idx_dyn]
    WXX = W[idx_aux, idx_aux]
    if verbose:
        print(f"   [schur] invertendo bloco {len(idx_aux)}x{len(idx_aux)} ...")
    WXXi = _cancelM(WXX.inv())
    K_eff = _cancelM(KQQ + CQX * WXXi * CQX.T)
    C_eff = _cancelM(CQQ - CQX * WXXi * WXQ)
    W_eff = _cancelM(WQQ - WQX * WXXi * WXQ)
    return K_eff, C_eff, W_eff, idx_dyn


def transform_basis(K, C, W, S, extra_rates=None):
    """
    Mudanca de base q = S u (S pode depender do fundo):
      K_u = S^T K S
      C_u = S^T K Sdot + S^T C S
      W_u = S^T W S - Sdot^T K Sdot - (Sdot^T C S + (Sdot^T C S)^T)
    """
    Sd = S.applyfunc(lambda e: dt_background(e, extra_rates))
    K_u = _cancelM(S.T * K * S)
    C_u = _cancelM(S.T * K * Sd + S.T * C * S)
    X = Sd.T * C * S
    W_u = _cancelM(S.T * W * S - Sd.T * K * Sd - X - X.T)
    return K_u, C_u, W_u


def matrix_ipp_row(K, C, W, i, extra_rates=None):
    """
    Remove a linha i de C por integracao por partes (exige K[i,:] = 0):
      C[i,j] udot_i u_j -> -Cdot[i,j] u_i u_j - C[i,j] u_i udot_j
    Atualiza W (parte -Cdot, simetrizada na convencao -1/2 u W u) e
    move -C[i,j] para C[j,i]; zera a linha i de C.
    """
    n = K.shape[0]
    for j in range(n):
        if sp.cancel(K[i, j]) != 0:
            raise ValueError(f"K[{i},:] nao nula — {i} e dinamica")
    C2 = C.copy()
    W2 = W.copy()
    for j in range(n):
        cij = C[i, j]
        if sp.cancel(cij) == 0:
            continue
        cdot = dt_background(cij, extra_rates)
        if i == j:
            # C[i,i] udot_i u_i = (C/2) d(u_i^2)/dt -> -(Cdot/2) u_i^2
            # na convencao -1/2 W[i,i] u_i^2  =>  Delta W[i,i] = Cdot
            W2[i, i] = sp.cancel(W2[i, i] + cdot)
        else:
            W2[i, j] = sp.cancel(W2[i, j] + cdot)
            W2[j, i] = sp.cancel(W2[j, i] + cdot)
            C2[j, i] = sp.cancel(C2[j, i] - cij)
        C2[i, j] = 0
    return K, C2, W2


# ----------------------------------------------------------------------
# eliminacao de variaveis auxiliares
# ----------------------------------------------------------------------
def eliminate_auxiliaries(L2, fields, vels, aux_fields, verbose=True):
    """
    Elimina variaveis cuja velocidade NAO aparece em L2:
    resolve dL2/dX = 0 (sistema linear) e substitui de volta.
    """
    aux = list(aux_fields)
    for X in aux:
        Xdot = sp.Symbol(str(X) + 'dot')
        if L2.has(Xdot):
            raise ValueError(f"{X} tem velocidade em L2 — nao e auxiliar pura")
    eqs = [sp.expand(sp.diff(L2, X)) for X in aux]
    sol = sp.solve(eqs, aux, dict=True)
    if not sol:
        raise RuntimeError("sistema de constraints sem solucao unica")
    sol = sol[0]
    if verbose:
        for X in aux:
            print(f"   [constraint] {X} resolvido (tamanho "
                  f"{sp.count_ops(sol[X])} ops)")
    L2r = sp.expand(L2.subs(sol))
    keep_f = [f for f in fields if f not in aux]
    keep_v = [sp.Symbol(str(f) + 'dot') for f in keep_f]
    return L2r, keep_f, keep_v, sol


def iterative_reduction(L2, fields, vels, verbose=True, max_rounds=4):
    """
    Remove iterativamente variaveis estritamente algebricas (sem
    velocidade em L2) ate estabilizar. Retorna L2 reduzida e listas.
    """
    L2c, fs, vs = sp.expand(L2), list(fields), list(vels)
    for rnd in range(max_rounds):
        aux = [f for f, v in zip(fs, vs) if not L2c.has(v) and L2c.has(f)]
        if not aux:
            break
        if verbose:
            print(f"   rodada {rnd+1}: eliminando {aux}")
        L2c, fs, vs, _ = eliminate_auxiliaries(L2c, fs, vs, aux, verbose)
    return L2c, fs, vs


# ----------------------------------------------------------------------
# construtores de metricas perturbadas (setor escalar)
# ----------------------------------------------------------------------
def scalar_metric_g(Phi_g, Psi_g):
    """Setor g, gauge Newtoniano (B_g=E_g=0), N_g=1. Modos cos(kz)."""
    c = sp.cos(k * z)
    g = sp.zeros(4, 4)
    g[0, 0] = -(1 + 2 * eps * Phi_g * c)
    for i in (1, 2, 3):
        g[i, i] = a_s**2 * (1 - 2 * eps * Psi_g * c)
    return g


def scalar_metric_f(Phi_f, Psi_f, B_f, E_f):
    """Setor f completo (Anexo C §C.2.2), N_f = xi. Modos cos(kz)."""
    c, s = sp.cos(k * z), sp.sin(k * z)
    f = sp.zeros(4, 4)
    f[0, 0] = -xi_s**2 * (1 + 2 * eps * Phi_f * c)
    # f_0i = b N_f d_i B_f ;  d_z(B_f cos(kz)) = -k B_f sin(kz)
    f[0, 3] = f[3, 0] = -b_s * xi_s * k * eps * B_f * s
    f[1, 1] = b_s**2 * (1 - 2 * eps * Psi_f * c)
    f[2, 2] = b_s**2 * (1 - 2 * eps * Psi_f * c)
    # f_zz inclui 2 d_z d_z E_f = -2 k^2 E_f cos(kz)
    f[3, 3] = b_s**2 * (1 - 2 * eps * Psi_f * c - 2 * k**2 * eps * E_f * c)
    return f


def tensor_metric_g(hx):
    """Setor g TT, polarizacao cruzada g_xy = a^2 eps h cos(kz)."""
    c = sp.cos(k * z)
    g = sp.diag(-1, a_s**2, a_s**2, a_s**2)
    g[1, 2] = g[2, 1] = a_s**2 * eps * hx * c
    return g


def tensor_metric_f(lx):
    c = sp.cos(k * z)
    f = sp.diag(-xi_s**2, b_s**2, b_s**2, b_s**2)
    f[1, 2] = f[2, 1] = b_s**2 * eps * lx * c
    return f


# ----------------------------------------------------------------------
# Lagrangiana de interacao HR ate O(eps^2)
# ----------------------------------------------------------------------
def interaction_lagrangian(g, f, dchi=None):
    """
    L_int = -m^2 M_eff^2 sqrt(-g) F(chi) sum beta_n e_n(sqrt(g^-1 f)).
    dchi: perturbacao delta-chi (Function-symbol ja em modo cos) ou None.
    F(chi) expandida: Fb + Fp*eps*dchi*cos + (1/2)Fpp*(eps*dchi*cos)^2.
    """
    ginv = series_inverse(g)
    M = cutM(ginv * f)
    A = matrix_sqrt_series(M)
    # verificacao interna: A*A = M ate O(eps^2), por avaliacao numerica
    # aleatoria (simplify simbolico explode em memoria no setor escalar)
    resid = cutM(A * A - M)
    import random
    from sympy.core.function import AppliedUndef
    rng = random.Random(20260806)
    atoms = set()
    for i in range(4):
        for j in range(4):
            atoms |= resid[i, j].atoms(sp.Symbol)
            atoms |= resid[i, j].atoms(AppliedUndef)
    sub_rand = {s: sp.Rational(rng.randint(2, 60), rng.randint(2, 60))
                for s in atoms}
    for i in range(4):
        for j in range(4):
            val = sp.N(resid[i, j].subs(sub_rand), 30)
            if abs(float(val)) > 1e-20:
                raise RuntimeError(f"sqrt matricial falhou em ({i},{j})")
    e0, e1, e2, e3, e4 = elementary_symmetric(A)
    V = b0 * e0 + b1 * e1 + b2 * e2 + b3 * e3 + b4 * e4
    if dchi is not None:
        c = sp.cos(k * z)
        Fchi = Fb + Fp * eps * dchi * c + sp.Rational(1, 2) * Fpp * (eps * dchi * c)**2
    else:
        Fchi = Fb
    return cut(-m2 * Meff2 * sqrt_minus_det(g) * cut(Fchi * V))


def chi_lagrangian(g, dchi=None):
    """
    L_chi = sqrt(-g) [ -1/2 g^{mu nu} d_mu chi d_nu chi - U(chi) ].
    dchi=None: só o campo de fundo chibar(t) (necessario mesmo assim,
    pois sqrt(-g) e g^{00} perturbados geram termos quadraticos).
    """
    c = sp.cos(k * z)
    chibarF = sp.Function('chibarF')(t)
    chi = chibarF if dchi is None else chibarF + eps * dchi * c
    ginv = series_inverse(g)
    dchi_mu = [cut(sp.diff(chi, mu)) for mu in COORDS]
    kin = sp.Integer(0)
    for mu in range(4):
        for nu in range(4):
            kin += ginv[mu, nu] * dchi_mu[mu] * dchi_mu[nu]
    kin = cut(-kin / 2)
    dch = chi - chibarF
    U = Ub + Up * dch + sp.Rational(1, 2) * Upp * cut(dch**2)
    L = cut(sqrt_minus_det(g) * cut(kin - U))
    # substitui derivadas do fundo chibar
    L = L.subs({sp.Derivative(chibarF, t): chid_s, chibarF: sp.Symbol('chibar')})
    return cut(L)


# ----------------------------------------------------------------------
# regras de fundo p/ simbolizacao das metricas (a(t), b(t), xi(t))
# ----------------------------------------------------------------------
def make_bg_functions():
    """Retorna versoes Function(t) de a, b, xi e as regras p/ simbolizar."""
    aF = sp.Function('aF', positive=True)(t)
    bF = sp.Function('bF', positive=True)(t)
    xiF = sp.Function('xiF', positive=True)(t)
    rules = {
        sp.Derivative(aF, t): a_s * H_s,
        sp.Derivative(bF, t): b_s * xi_s * Hf_s,
        sp.Derivative(xiF, t): xid_s,
        aF: a_s, bF: b_s, xiF: xi_s,
    }
    return aF, bF, xiF, rules


def substitute_bg_functions(expr_matrix_or_expr, aF, bF, xiF):
    """Troca os simbolos a_s,b_s,xi_s pelas Function(t) (pre-derivadas)."""
    sub = {a_s: aF, b_s: bF, xi_s: xiF}
    if hasattr(expr_matrix_or_expr, 'applyfunc'):
        return expr_matrix_or_expr.applyfunc(lambda e: e.subs(sub))
    return expr_matrix_or_expr.subs(sub)


# ----------------------------------------------------------------------
# equacoes de fundo on-shell (aceleracoes, Friedmann, eq. de chi)
# ----------------------------------------------------------------------
def background_onshell_rules():
    """
    Deriva as equacoes de fundo da Lagrangiana minisuperespaco validada
    (F.1, com N_g=1, N_f=xi, materia fria: sqrt(-g) rho_m = const):
      - eq. de aceleracao do setor g (variacao em a)  -> resolve Hdot
      - eq. de aceleracao do setor f (variacao em b)  -> resolve H_fdot
      - Friedmann g (F.3)                             -> resolve Ubar
      - Friedmann f (F.4)                             -> resolve H_f^2
      - eq. de chi (Anexo E §E.3(3))                  -> resolve chiddot
    Retorna dict {'Hd','Hfd','Ub','Hf2','chidd'}.
    """
    aB = sp.Function('aB', positive=True)(t)
    bB = sp.Function('bB', positive=True)(t)
    xiB = sp.Function('xiB', positive=True)(t)
    chiB = sp.Function('chiB')(t)
    rB = bB / aB
    V = (b0 + b1 * (xiB + 3 * rB) + b2 * (3 * xiB * rB + 3 * rB**2)
         + b3 * (3 * xiB * rB**2 + rB**3) + b4 * xiB * rB**3)
    FchiB = sp.Function('FB', positive=True)(chiB)
    UchiB = sp.Function('UB')(chiB)
    rho0 = sp.Symbol('rho_m0', positive=True)
    Lmini = (-3 * Mg2 * aB * sp.diff(aB, t)**2
             - 3 * Mf2 * bB * sp.diff(bB, t)**2 / xiB
             - m2 * Meff2 * aB**3 * FchiB * V
             + aB**3 * sp.diff(chiB, t)**2 / 2 - aB**3 * UchiB
             - rho0)

    def EL(q):
        return sp.expand(sp.diff(Lmini, q)
                         - sp.diff(sp.diff(Lmini, sp.diff(q, t)), t))

    chibar = sp.Symbol('chibar')
    subs1 = {
        sp.Derivative(aB, (t, 2)): a_s * (Hd_s + H_s**2),
        sp.Derivative(bB, (t, 2)): b_s * (xi_s * Hfd_s + xid_s * Hf_s
                                          + xi_s**2 * Hf_s**2),
        sp.Derivative(aB, t): a_s * H_s,
        sp.Derivative(bB, t): b_s * xi_s * Hf_s,
        sp.Derivative(xiB, t): xid_s,
        sp.Derivative(chiB, (t, 2)): chidd_s,
        sp.Derivative(chiB, t): chid_s,
    }

    def to_syms(e):
        e = e.subs(subs1).doit().subs(subs1)
        e = e.replace(sp.Derivative(sp.Function('FB', positive=True)(chiB), chiB), Fp)
        e = e.replace(sp.Derivative(sp.Function('UB')(chiB), chiB), Up)
        e = e.subs({aB: a_s, bB: b_s, xiB: xi_s, chiB: chibar})
        e = e.subs({sp.Function('FB', positive=True)(chibar): Fb,
                    sp.Function('UB')(chibar): Ub})
        return sp.expand(e)

    Hd_sol = sp.solve(sp.Eq(to_syms(EL(aB)), 0), Hd_s)[0]
    Hfd_sol = sp.solve(sp.Eq(to_syms(EL(bB)), 0), Hfd_s)[0]
    chidd_sol = sp.solve(sp.Eq(to_syms(EL(chiB)), 0), chidd_s)[0]

    rr = b_s / a_s
    rho_int_g = m2 * Meff2 * Fb * (b0 + 3 * b1 * rr + 3 * b2 * rr**2 + b3 * rr**3)
    Ub_sol = 3 * Mg2 * H_s**2 - rho_s - chid_s**2 / 2 - rho_int_g
    Hf2_sol = (m2 * Meff2 * Fb * (b4 + 3 * b3 / rr + 3 * b2 / rr**2 + b1 / rr**3)
               / (3 * Mf2))

    return {'Hd': sp.simplify(Hd_sol), 'Hfd': sp.simplify(Hfd_sol),
            'chidd': sp.simplify(chidd_sol),
            'Ub': Ub_sol, 'Hf2': Hf2_sol}


def onshell(expr, R):
    """Impoe as equacoes de fundo em uma expressao simbolizada."""
    e = sp.expand(expr)
    e = e.subs({Hd_s: R['Hd'], Hfd_s: R['Hfd'], chidd_s: R['chidd']})
    e = sp.expand(e).subs(Ub, R['Ub'])
    e = sp.expand(e).subs(Hf_s**2, R['Hf2'])
    return sp.simplify(e)


# ----------------------------------------------------------------------
# benchmark numerico consistente (usado pelos scripts p/ checagens)
# ----------------------------------------------------------------------
def benchmark(delta_offroot=sp.Rational(1, 25)):
    """
    Valores numericos consistentes com as Friedmann g/f (F.3/F.4):
    F1 (beta3=0), beta1=1, beta2=-2/5 -> r_star=5/4;
    r = r_star(1-delta_offroot) fica ligeiramente fora da raiz.
    Hdot=Hfdot=xidot=0 (aproximacao quase-de Sitter p/ o benchmark).
    """
    vals = {b0: -1, b1: 1, b2: sp.Rational(-2, 5), b3: 0, b4: sp.Rational(1, 2),
            Mg2: 1, Mf2: 1, m2: 1, Meff2: 1,
            Fb: 1, Fp: sp.Rational(1, 10), Fpp: sp.Rational(1, 20),
            a_s: 1, H_s: 1, chid_s: sp.Rational(3, 10),
            Up: sp.Rational(-1, 5), Upp: sp.Rational(3, 10),
            rho_s: sp.Rational(9, 10),
            Hd_s: 0, Hfd_s: 0, xid_s: 0}
    r_star = sp.Rational(5, 4)
    rv = r_star * (1 - delta_offroot)
    vals[b_s] = rv * vals[a_s]
    # Friedmann f (F.4): 3 Mf2 Hf^2 = m2 Meff2 F (b4 + 3 b3/r + 3 b2/r^2 + b1/r^3)
    Hf2 = (vals[m2] * vals[Meff2] * vals[Fb] *
           (vals[b4] + 3 * vals[b3] / rv + 3 * vals[b2] / rv**2 + vals[b1] / rv**3)
           ) / (3 * vals[Mf2])
    vals[Hf_s] = sp.sqrt(Hf2)
    vals[xi_s] = vals[H_s] / vals[Hf_s]      # ramo dinamico: xi = H/H_f
    # Friedmann g (F.3): Ubar = 3 Mg2 H^2 - rho_m - chidot^2/2 - rho_int
    rho_int = (vals[m2] * vals[Meff2] * vals[Fb] *
               (vals[b0] + 3 * vals[b1] * rv + 3 * vals[b2] * rv**2 + vals[b3] * rv**3))
    vals[Ub] = (3 * vals[Mg2] * vals[H_s]**2 - vals[rho_s]
                - vals[chid_s]**2 / 2 - rho_int)
    # eq. de chi derivada de F.1: chidd = -3H chid - U' - m2 Meff2 F' V
    # (atencao: Anexo E §E.3(3) declara o sinal OPOSTO da fonte F'V —
    #  o sinal aqui e o que segue da Lagrangiana; ver saida do script 01)
    Vbg = (vals[b0] + vals[b1] * (vals[xi_s] + 3 * rv)
           + vals[b2] * (3 * vals[xi_s] * rv + 3 * rv**2)
           + vals[b3] * (3 * vals[xi_s] * rv**2 + rv**3)
           + vals[b4] * vals[xi_s] * rv**3)
    vals[chidd_s] = (-3 * vals[H_s] * vals[chid_s] - vals[Up]
                     - vals[m2] * vals[Meff2] * vals[Fp] * Vbg)
    return {kk: sp.nsimplify(vv, rational=False) for kk, vv in vals.items()}


# ----------------------------------------------------------------------
# auto-testes
# ----------------------------------------------------------------------
def _selftest():
    print("== auto-teste tdcp_pert_lib ==")

    # 1) series_inverse
    p1, p2 = sp.symbols('p1 p2')
    M = sp.diag(2, 3, 5, 7) + eps * sp.Matrix(4, 4, lambda i, j: (i + 2 * j) * p1) \
        + eps**2 * sp.Matrix(4, 4, lambda i, j: (i * j + 1) * p2)
    resid = cutM(M * series_inverse(M)) - sp.eye(4)
    assert all(sp.simplify(resid[i, j]) == 0 for i in range(4) for j in range(4))
    print("   [ok] series_inverse")

    # 2) Gamma-Gamma reproduz minisuperespaco: L = -3 M^2 a adot^2 / N
    aF = sp.Function('aF', positive=True)(t)
    NF = sp.Function('NF', positive=True)(t)
    gbg = sp.diag(-NF**2, aF**2, aF**2, aF**2)
    LGG = lagrangian_GG(gbg, Mg2)
    target = -3 * Mg2 * aF * sp.diff(aF, t)**2 / NF
    assert sp.simplify(LGG - target) == 0
    print("   [ok] Lagrangiana Gamma-Gamma == -3 M^2 a adot^2 / N (F.1)")

    # 3) sqrt matricial + e_n no fundo bimetrico
    gd = sp.diag(-1, a_s**2, a_s**2, a_s**2)
    fd = sp.diag(-xi_s**2, b_s**2, b_s**2, b_s**2)
    A = matrix_sqrt_series(cutM(series_inverse(gd) * fd))
    e0, e1, e2, e3, e4 = elementary_symmetric(A)
    rr = b_s / a_s
    assert sp.simplify(e1 - (xi_s + 3 * rr)) == 0
    assert sp.simplify(e2 - (3 * xi_s * rr + 3 * rr**2)) == 0
    assert sp.simplify(e3 - (3 * xi_s * rr**2 + rr**3)) == 0
    assert sp.simplify(e4 - xi_s * rr**3) == 0
    print("   [ok] e_n(sqrt(g^-1 f)) fundo = (F.2)")

    # 4) interacao no fundo = -m2 Meff2 a^3 F V(xi,r)  (N_g=1)
    Lint0 = eps_part(interaction_lagrangian(gd, fd), 0)
    Vbg = (b0 + b1 * (xi_s + 3 * rr) + b2 * (3 * xi_s * rr + 3 * rr**2)
           + b3 * (3 * xi_s * rr**2 + rr**3) + b4 * xi_s * rr**3)
    assert sp.simplify(Lint0 + m2 * Meff2 * a_s**3 * Fb * Vbg) == 0
    print("   [ok] L_int fundo = -m2 Meff2 a^3 F V(xi,r) (F.1/F.2)")

    # 5) media em z
    X = sp.Symbol('X')
    assert z_average(X * sp.cos(k * z)**2) == X / 2
    assert z_average(X * sp.sin(k * z) * sp.cos(k * z)) == 0
    assert z_average(X * sp.cos(k * z)) == 0
    print("   [ok] z_average")

    # 6) benchmark satisfaz Friedmann f
    v = benchmark()
    rv = v[b_s] / v[a_s]
    lhs = 3 * v[Mf2] * v[Hf_s]**2
    rhs = v[m2] * v[Meff2] * v[Fb] * (v[b4] + 3 * v[b2] / rv**2 + v[b1] / rv**3)
    assert sp.simplify(lhs - rhs) == 0
    print("   [ok] benchmark consistente com Friedmann f")

    print("== todos os auto-testes passaram ==")


if __name__ == '__main__':
    _selftest()
