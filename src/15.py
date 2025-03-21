import sympy as sp
from sympy import symbols

x = symbols('x')
f(x) = x**2 - 3*x + 1

def find_root(f):
    start = 0
    end = 5
    if f.subs(x, end) > 0:
        return None
    while True:
        mid = (start + end) / 2
        if f.subs(x, mid) == 0:
            return mid
        elif f.subs(x, mid) < 0 and start != 5:
            start = mid
        else:
            end = mid

root = find_root(f)
print(root)
