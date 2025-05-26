def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return num ** 0.5

try:
    print(square_root(-4))  # This will raise an exception because -4 is not a positive number.
except ValueError as e:
    print(e)  # Print the error message
