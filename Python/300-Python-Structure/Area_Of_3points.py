def Area_3points(x1, y1, x2, y2, x3, y3):
    """
    Calculate the area of a triangle given its vertices.
    
    Parameters:
    x1, y1: Coordinates of the first vertex.
    x2, y2: Coordinates of the second vertex.
    x3, y3: Coordinates of the third vertex.
    
    Returns:
    float: The area of the triangle.
    """
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
def main():
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    x3 = float(input("Enter the x-coordinate of the third point: "))
    y3 = float(input("Enter the y-coordinate of the third point: "))
    
    area = Area_3points(x1, y1, x2, y2, x3, y3)
    print(f"The area of the triangle formed by points ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) is: {area}")
if __name__ == "__main__":
    main()
    