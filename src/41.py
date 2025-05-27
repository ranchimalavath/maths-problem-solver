def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

# Example usage:
result = calculate(5, 3, "+")
print(result) # Output: 8

result = calculate(5, 3, "-")
print(result) # Output: 2

result = calculate(5, 3, "*")
print(result) # Output: 15

result = calculate(5, 3, "/")
print(result) # Output: 1.6666666666666667
