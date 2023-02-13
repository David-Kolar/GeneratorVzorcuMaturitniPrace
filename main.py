import sympy
from math import comb
import re

def hrubou_silou(vzorec, q, exp):
    vzorec = vzorec.replace("q", str(q))
    soucet = 0
    for i in range(exp+1):
        soucet += eval(vzorec.replace("x", str(i)))
    return soucet

def spocitej_mocniny(stupen):
    nulty_clen = "(q**(x+1) - 1)/(q - 1)"
    stupne = [sympy.sympify(nulty_clen)]
    for exp in range(1, stupen+1):
        novy_clen = sympy.sympify("0")
        for k in range(exp):
            novy_clen += sympy.sympify(comb(exp, k)*stupne[k])
        novy_clen = sympy.sympify(f"""(x+1)**{exp}*q**(x+1)""") - sympy.sympify("q")*novy_clen
        novy_clen /= sympy.sympify("q - 1")
        stupne.append(sympy.simplify(novy_clen))
    return stupne

def vyres(vzorec):
    vzorec = sympy.sympify(vzorec)
    print(vzorec.simplify().apart())


v = "x(x+1)"
vyres(v)