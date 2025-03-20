import random
def solve_math_problem(max_value):
    problem = str(random.randint(1, max_value)) + ' x ' + str(random.randint(1, max_value))
    return problem

def get_solution(problem):
    nums = problem.split('x')
    solution = int(nums[0]) * int(nums[1])
    return solution
