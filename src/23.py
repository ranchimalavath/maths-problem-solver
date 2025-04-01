def calculate(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y

# Example usage:
result = calculate(10, 5, "+")
print(result) # Output: 15
