def QuadraticEquation(a, b, c):
    """
    This function calculates the roots of a quadratic equation
    of the form ax^2 + bx + c = 0 using the quadratic formula.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    tuple: A tuple containing the two roots (root1, root2)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        raise ValueError("The equation has no real roots.")
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    # If discriminant is positive, calculate both roots
    
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return (root1, root2)
def main():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    
    try:
        roots = QuadraticEquation(a, b, c)
        if len(roots) == 1:
            print(f"The equation has one root: {roots[0]}")
        else:
            print(f"The roots of the equation are: {roots[0]} and {roots[1]}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()