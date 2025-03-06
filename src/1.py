
import random

def solve_math_problem(problem):
    numbers = [random.randint(1, 10) for _ in range(2)]
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    result = eval(f"{numbers[0]} {operator} {numbers[1]}")
    return f"What is {problem}? {result}"