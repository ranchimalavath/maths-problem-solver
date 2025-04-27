def solve_math_problem(problems):
    solutions = {}
    for problem in problems:
        if problem in solutions:
            continue
        else:
            solution = solve_problems(problem)
            solutions[problem] = solution
    return solutions

def solve_problems(problems):
    solution = 0
    for problem in problems:
        result = evaluate_expression(problem)
        solution += result
    return solution

def evaluate_expression(expression):
    try:
        expression_result = eval(expression)
        return expression_result
    except Exception as e:
        print(f"Error: {e}")
        return None
