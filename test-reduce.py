
import sympy as sym
import numpy as np

x= sym.symbols("x")
eq = sym.Eq(x+1)
a=sym.solve(eq)
print(type(a))
print(a)
#help(sym.solve)