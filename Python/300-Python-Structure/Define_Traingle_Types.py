def define_triangle_type(a, b, c):
    """
    Determines the type of triangle based on the lengths of its sides.
    
    Parameters:
    a (float): length of side a
    b (float): length of side b
    c (float): length of side c
    
    Returns:
    str: "equilateral", "isosceles", or "scalene" based on the triangle's type
    """
    heron = (a + b + c) / 2
    if a <= 0 or b <= 0 or c <= 0 or heron <= a or heron <= b or heron <= c:
        return "not a triangle"
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"
def area_of_triangle(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.
    
    Parameters:
    a (float): length of side a
    b (float): length of side b
    c (float): length of side c
    
    Returns:
    float: area of the triangle
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    
    triangle_type = define_triangle_type(a, b, c)
    area = area_of_triangle(a, b, c)
    if triangle_type != "not a triangle":
        print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")
    print(f"The triangle with sides {a}, {b}, and {c} is {triangle_type}.")
    
if __name__ == "__main__":
    main()