def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

expression = "2 + 3 * (5 - 1)"
result = calculate(expression)
if result is not None:
    print(result)
