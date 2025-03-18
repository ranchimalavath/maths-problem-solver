import random

def solve_math_problem(problem):
    # Check if the problem is already solved
    if "solution" in problem:
        return problem["solution"]

    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Add the random number to the problem
    problem["random_number"] = random_number

    # Return the updated problem
    return problem
