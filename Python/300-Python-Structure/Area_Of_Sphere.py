def AreaofSphere(radius):
    """
    Calculate the surface area of a sphere given its radius.
    
    Parameters:
    radius (float): The radius of the sphere.
    
    Returns:
    float: The surface area of the sphere.
    """
    import math
    return 4 * math.pi * (radius ** 2)
def main():
    radius = float(input("Enter the radius of the sphere: "))
    area = AreaofSphere(radius)
    print(f"The surface area of the sphere with radius {radius} is: {area}")
if __name__ == "__main__":
    main()