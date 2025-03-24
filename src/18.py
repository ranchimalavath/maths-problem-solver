def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Example usage:
result = calculate(5, 2, "add")
print(result)

result = calculate(5, 3, "subtract")
print(result)

result = calculate(5, 4, "multiply")
print(result)

result = calculate(5, 10, "divide")
print(result)
