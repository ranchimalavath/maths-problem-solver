def area_of_triangle(base, height):
    """
    Calculate the area of a triangle using the formula: 
    (base * height) / 2
    """
    return (base * height) / 2

def main():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    
    area = area_of_triangle(base, height)
    print(f"The area of the triangle is {area:.2f}")

if __name__ == "__main__":
    main()
