def distance_of_2_points(x1, y1, x2, y2):
    """
    Calculate the distance between two points in a 2D space.
    
    Parameters:
    x1, y1 : coordinates of the first point
    x2, y2 : coordinates of the second point
    
    Returns:
    float : the distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def main():
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    
    distance = distance_of_2_points(x1, y1, x2, y2)
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")
if __name__ == "__main__":
    main()