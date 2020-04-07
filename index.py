#!/usr/bin/env python

from sympy import symbols, init_printing, Integral, oo

x = symbols("x")
init_printing()

j = Integral(x**2, (x, -oo, oo))
print(j)