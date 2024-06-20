"""
Program: Generovani souctovych vzorcu se sympy
Autor: David Kolar
Email: davidkolar325@gmail.com
"""

import sympy
from math import comb
import re
from decimal import Decimal

def hrubou_silou(polynom, q, exp):
    soucet = 0
    for i in range(exp+1):
        soucet += eval(polynom.replace("x", f"""Decimal({i})"""))*Decimal(q)**i
    return soucet

def spocitej_mocniny(stupen):
    nulty_clen = "(q**(x+1) - 1)/(q - 1)"
    stupne = [sympy.sympify(nulty_clen)]
    for exp in range(1, stupen+1):
        novy_clen = sympy.sympify("0")
        for k in range(exp):
            novy_clen += sympy.sympify(comb(exp, k)*stupne[k])
            novy_clen = sympy.simplify(novy_clen)
        novy_clen = sympy.sympify(f"""(x+1)**{exp}*q**(x+1)""") - sympy.sympify("q")*novy_clen
        novy_clen /= sympy.sympify("q - 1")
        stupne.append(sympy.simplify(novy_clen))
    return stupne

def vyres(polynom, q, x):
    vzorec = sympy.sympify(polynom)
    vzorec = vzorec.expand()
    try:
        koeficienty = sympy.Poly(vzorec).all_coeffs()[::-1]
    except:
        koeficienty = [int(str(vzorec))]
    stupne = spocitej_mocniny(len(koeficienty) - 1)
    soucet = 0
    vzorec = ""
    for index, k in enumerate(koeficienty):
        val = str(stupne[index])
        vzorec += f"""+({k}*{val})"""
    vzorec = sympy.sympify(vzorec)
    v2 = vzorec.simplify()
    vzorec = str(vzorec)
    soucet = eval(vzorec.replace("x", "Decimal("+str(x)+")").replace("q", f"""Decimal({q})"""))
    v2 = str(v2)
    vzorec = v2.replace("x", "n")
    return soucet, vzorec

while(True):
    polynom = input("Zadejte polynom: ")
    q = Decimal(input("Zadejte zaklad: "))
    n = int(input("Zadejte n: "))
    print("Soucet hrubou silou:", hrubou_silou(polynom, q, n))
    soucet, vzorec = vyres(polynom, q, n)
    print("Pomoci vzorce:      ", soucet)
    print("Vzorec:", vzorec)
