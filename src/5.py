import random

def solve_math_problem(problem):
    numbers = [random.randint(1, 10) for _ in range(2)]
    operation = random.choice(['+', '-', '*', '/'])
    answer = eval(f"{numbers[0]} {operation} {numbers[1]}")
    return f"What is {problem}?"
