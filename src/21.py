def calculate_squares(nums):
    """
    Calculate the sum of squares of elements in the given list.
    
    Args:
        nums (list): A list of numbers.
    
    Returns:
        int: The sum of squares of the elements in the list.
    """
    return sum(num ** 2 for num in nums)

# Example usage
numbers = [1, 2, 3]
result = calculate_squares(numbers)
print(f"The sum of squares is {result}")
