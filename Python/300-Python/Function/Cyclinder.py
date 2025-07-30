import math

def Circumference(radius):
    return 2 * math.pi * radius

def Area(radius):
    return math.pi * radius ** 2

def Volume(radius, height):
    return math.pi * radius ** 2 * heights

while True:
    try:
        choice = int(input("Enter 1 for Circumference, 2 for Area, 3 for Volume, 4 to exit: "))
        if choice == 1:
            radius = float(input("Enter the radius of the circle: "))
            print(f"The circumference of the circle is {Circumference(radius)}")
        elif choice == 2:
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is {Area(radius)}")
        elif choice == 3:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            print(f"The volume of the cylinder is {Volume(radius, height)} ")
        elif choice == 4:
            print("Exit Programs")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")