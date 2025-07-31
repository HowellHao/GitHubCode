def define_location_in_circle(x, y, radius):
    """
    Determines the location of a point (x, y) relative to a circle centered at the origin with a given radius.
    
    Parameters:
    x (float): x-coordinate of the point
    y (float): y-coordinate of the point
    radius (float): radius of the circle
    
    Returns:
    str: "inside", "on", or "outside" based on the point's location relative to the circle
    """
    distance_squared = x**2 + y**2
    radius_squared = radius**2
    
    if distance_squared < radius_squared:
        return "inside"
    elif distance_squared == radius_squared:
        return "on"
    else:
        return "outside"
def main():
    x = float(input("Enter the x-coordinate of the point: "))
    y = float(input("Enter the y-coordinate of the point: "))
    radius = float(input("Enter the radius of the circle: "))
    
    location = define_location_in_circle(x, y, radius)
    print(f"The point ({x}, {y}) is {location} the circle with radius {radius}.")

if __name__ == "__main__":
    main()