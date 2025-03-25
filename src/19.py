import sympy as sp
from sympy import *
x = symbols('x')

# Example equation
eq1 = x**2 - 3*x + 2

# Solve the equation
solution = solve(eq1, x)
print(solution)
