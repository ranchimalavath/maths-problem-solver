import math

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points (x1, y1) and (x2, y2).
    
    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.
        
    Returns:
        The distance between the two points.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example usage
point1 = [0, 0]
point2 = [3, 4]

distance = calculate_distance(point1[0], point1[1], point2[0], point2[1])
print(f"The distance between the two points is: {distance}")
