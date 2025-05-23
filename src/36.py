def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Example usage of the functions
result1 = add_numbers(5, 3)
print(f"Result: {result1}")

result2 = subtract_numbers(8, 4)
print(f"Result: {result2}")

result3 = multiply_numbers(6, 7)
print(f"Result: {result3}")

try:
    result4 = divide_numbers(9, 0)
except ValueError as e:
    print(e)

# You can add more examples or modify the code as per your project's needs
