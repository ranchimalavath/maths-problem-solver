def calculate_sum(x, y):
    return x + y

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def sort_list(list1):
    list2 = []
    for num in sorted(list1):
        if not list2:
            list2.append(num)
        else:
            list2[-1] = num
    return list2

def is_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2

# Example usage
matrix = [
    [5, 6, 7],
    [8, 9, 10]
]

print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

sorted_matrix = sort_list(matrix)
print("\nSorted Matrix:")
for row in sorted_matrix:
    for element in row:
        print(element, end=' ')
    print()
