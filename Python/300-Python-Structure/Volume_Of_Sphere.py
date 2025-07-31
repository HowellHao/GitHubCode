def VolumeofSphere(radius):
    """
    Calculate the volume of a sphere given its radius.
    
    Parameters:
    radius (float): The radius of the sphere.
    
    Returns:
    float: The volume of the sphere.
    """
    from math import pi
    return (4/3) * pi * (radius ** 3)
def main():
    radius = float(input("Enter the radius of the sphere: "))
    volume = VolumeofSphere(radius)
    print(f"The volume of the sphere with radius {radius} is: {volume}")
if __name__ == "__main__":
    main()