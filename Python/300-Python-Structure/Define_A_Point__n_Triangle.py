def A_Point_in_Triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Calculate area of the triangle using the determinant method
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

    # Area of the triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)
    
    # Area of the triangle PAB
    A1 = area(px, py, x1, y1, x2, y2)
    
    # Area of the triangle PBC
    A2 = area(px, py, x2, y2, x3, y3)
    
    # Area of the triangle PCA
    A3 = area(px, py, x3, y3, x1, y1)
    
    # Check if point P is inside the triangle ABC
    return A == A1 + A2 + A3
def main():
    px = float(input("Enter the x-coordinate of the point P: "))
    py = float(input("Enter the y-coordinate of the point P: "))
    x1 = float(input("Enter the x-coordinate of vertex A: "))
    y1 = float(input("Enter the y-coordinate of vertex A: "))
    x2 = float(input("Enter the x-coordinate of vertex B: "))
    y2 = float(input("Enter the y-coordinate of vertex B: "))
    x3 = float(input("Enter the x-coordinate of vertex C: "))
    y3 = float(input("Enter the y-coordinate of vertex C: "))
    
    if A_Point_in_Triangle(px, py, x1, y1, x2, y2, x3, y3):
        print(f"The point P({px}, {py}) is inside the triangle formed by points A({x1}, {y1}), B({x2}, {y2}), and C({x3}, {y3}).")
    else:
        print(f"The point P({px}, {py}) is outside the triangle formed by points A({x1}, {y1}), B({x2}, {y2}), and C({x3}, {y3}).")
if __name__ == "__main__":
    main()
    