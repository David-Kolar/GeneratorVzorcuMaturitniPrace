import sympy
from math import comb
import re

def hrubou_silou(polynom, q, exp):
    soucet = 0
    for i in range(exp+1):
        soucet += eval(polynom.replace("x", str(i)))*q**i
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

def vyres(polynom, q, x):
    vzorec = sympy.sympify(polynom)
    vzorec = vzorec.expand()
    koeficienty = sympy.Poly(vzorec).all_coeffs()[::-1]
    stupne = spocitej_mocniny(len(koeficienty) - 1)
    soucet = 0
    for index, k in enumerate(koeficienty):
        val = str(stupne[index])
        val = eval(val.replace("q", str("q").replace("x", str(x))))*k
        soucet += val
    return int(soucet)

polynom = "100*x**5 - 3*x + 2587*x*(x + 1)"
q, x = 10, 5
print(hrubou_silou(polynom, q, x))
print(vyres(polynom, q, x))