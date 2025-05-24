import numpy as np
from scipy.optimize import fsolve

def equation(x):
    return 2 * x**3 - 3*x**2 + 1

solution = fsolve(equation, 1)
print(solution)
