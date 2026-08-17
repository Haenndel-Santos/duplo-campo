"""Regra 6b aplicada aos numeros do R-12f/R-12h: eles movem com h?

O caso que impos a regra 6b esta em r ~ 1e8 (ramo infinito). O dominio
do R-12f/R-12h e o ramo FINITO com r <= 0.33. A regra diz que o h
necessario depende do fundo, entao verifica-se em vez de supor.

Reusa a maquinaria do r12g (fundo em forma fechada + estencil de 8a
ordem), que ja aceita hN como parametro.
"""
import os

src = open('auditoria/code/r12g_isola_ruido_e_classe.py',
           encoding='utf-8').read().split('BENCH = celula')[0]
ns = {'__file__': os.path.abspath('auditoria/code/r12g_isola_ruido_e_classe.py'),
      '__name__': 'chk'}
exec(compile(src, 'r12g', 'exec'), ns)

import mpmath as mp
import sympy as sp

celula, cs2 = ns['celula'], ns['cs2']
B = celula(sp.Integer(1), sp.Rational(-2, 5), sp.Rational(1, 2), sp.Integer(1))
HS = ['1e-3', '1e-4', '1e-5']

print()
print('c_s^2 do modo metrico, celula de benchmark, dps=60, estencil 8a ordem')
print(f"{'a':>8} {'r':>10} {'kh':>7} " + ' '.join(f'h={h:<8}'.rjust(22)
                                                 for h in HS))
mp.mp.dps = 60
for aval in ('1000', '2.0', '0.578', '0.316', '0.01'):
    for kh in (30, 1000):
        vals, rv = [], None
        for h in HS:
            v = cs2(B, aval, mp.mpf(kh), ordem=8, hN=mp.mpf(h))
            vals.append(mp.nstr(v[0], 16))
            rv = v[3]
        print(f'{aval:>8} {float(rv):10.3e} {kh:7d} '
              + ' '.join(x.rjust(22) for x in vals))

# a_cross com h refinado
print()
print('a_cross (troca de sinal de c_s^2, kh=1e4) por h:')
for h in HS:
    lo, hi = mp.mpf('0.3'), mp.mpf('2.0')
    flo = cs2(B, lo, mp.mpf(10000), ordem=8, hN=mp.mpf(h))[0]
    for _ in range(40):
        mid = mp.sqrt(lo * hi)
        fm = cs2(B, mid, mp.mpf(10000), ordem=8, hN=mp.mpf(h))[0]
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
        if hi / lo - 1 < mp.mpf('1e-9'):
            break
    ac = mp.sqrt(lo * hi)
    print(f'   h={h:<7} a_cross = {mp.nstr(ac, 10):>14}'
          f'   z_cross = {mp.nstr(mp.mpf("0.931")/ac - 1, 8)}')
