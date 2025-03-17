import random

def solve_math_problem(problem):
    """
    Solves a math problem using the given problem string.
    The problem string should be in the format of:
        operator1 operand1 operator2 operand2
    where operator is one of +, -, *, /, or ^, and operands are integers.
    The function returns the result of the problem.
    """
    # Split the problem string into tokens
    tokens = problem.split()
    if len(tokens) != 4:
        raise ValueError("Invalid problem string")

    # Get the operators and operands
    operator1 = tokens[0]
    operand1 = int(tokens[1])
    operator2 = tokens[2]
    operand2 = int(tokens[3])

    # Perform the operation
    if operator1 == "+":
        result = operand1 + operand2
    elif operator1 == "-":
        result = operand1 - operand2
    elif operator1 == "*":
        result = operand1 * operand2
    elif operator1 == "/":
        result = operand1 // operand2
    elif operator1 == "^":
        result = pow(operand1, operand2)
    else:
        raise ValueError("Invalid operator")

    # Return the result
    return result
