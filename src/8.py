
import random

def solve_math_problem(problem):
    # Implement your solution here
    return None

# Test cases
assert solve_math_problem("2 + 2") == 4
assert solve_math_problem("10 - 5") == 5
assert solve_math_problem("3 * 4") == 12
assert solve_math_problem("10 / 2") == 5
assert solve_math_problem("(2 + 3) * 4") == 20
assert solve_math_problem("2 ^ 8") == 256

# Generate a random math problem for testing
problem = str(random.randint(1, 100)) + " " + chr(random.choice(["+", "-", "*", "/"])) + " " + str(random.randint(1, 100))
assert solve_math_problem(problem) == None