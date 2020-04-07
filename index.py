#!/usr/bin/env python

from sympy import symbols, init_printing, Integral, oo

x = symbols("x")
init_printing()

i = Integral(x, (x, -oo, oo))
print(i)