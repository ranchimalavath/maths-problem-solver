  import random
def solve_math_problem(problem):
    if problem == "addition":
        return str(random.randint(1, 10)) + " + " + str(random.randint(1, 10))
    elif problem == "subtraction":
        return str(random.randint(1, 10)) + " - " + str(random.randint(1, 10))
    elif problem == "multiplication":
        return str(random.randint(1, 10)) + " x " + str(random.randint(1, 10))
    elif problem == "division":
        return str(random.randint(1, 10)) + " / " + str(random.randint(1, 10))
    else:
        return "Invalid Problem"

print(solve_math_problem("addition"))