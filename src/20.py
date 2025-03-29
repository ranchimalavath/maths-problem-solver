def find_minimal_value(numbers):
    minimal_value = float('inf')
    current_value = numbers[0]
    
    for number in numbers:
        if abs(number) < abs(current_value):
            current_value = number
    
    return current_value

# Example usage
numbers = [4, -3, 2, -1, 5]
minimal_value = find_minimal_value(numbers)
print("Minimal value:", minimal_value)
