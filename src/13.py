def solve_math_problem(problem):
    # Check if the problem is already solved
    if "=" in problem:
        return problem
    
    # Split the problem into parts
    parts = problem.split(" ")
    
    # Check if the first part of the problem is a number
    try:
        left_side = float(parts[0])
    except ValueError:
        left_side = 0
    
    # Check if the second part of the problem is a number
    try:
        right_side = float(parts[1])
    except ValueError:
        right_side = 0
    
    # Check which operation to perform
    if parts[2] == "+":
        result = left_side + right_side
    elif parts[2] == "-":
        result = left_side - right_side
    elif parts[2] == "*":
        result = left_side * right_side
    elif parts[2] == "/":
        result = left_side / right_side
    
    # Return the solution
    return f"{left_side} {parts[2]} {right_side} = {result}"
