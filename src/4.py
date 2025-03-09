import random
from decimal import Decimal

def solve_math_problem(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {op}")

def generate_math_problem(min_value, max_value):
    a = random.randint(min_value, max_value)
    b = random.randint(min_value, max_value)
    op = random.choice(["+", "-", "*", "/"])
    return f"{a} {op} {b}"

def check_answer(problem, answer):
    try:
        expected_answer = float(solve_math_problem(**eval(problem)))
        if abs(expected_answer - answer) <= 0.001:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    problem = generate_math_problem(1, 100)
    print(f"Problem: {problem}")
    answer = float(input("Enter your answer: "))
    if check_answer(problem, answer):
        print("Correct!")
    else:
        print("Incorrect. Try again.")
