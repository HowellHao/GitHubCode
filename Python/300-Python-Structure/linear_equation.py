def linear_equation(a, b, c):
    """
    Solves the linear equation of the form ax + b = c.
    
    Parameters:
    a (float): Coefficient of x
    b (float): Constant term
    c (float): Right-hand side value
    
    Returns:
    float: The value of x that satisfies the equation
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    
    x = (c - b) / a
    return x
def main():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the constant term b: "))
    c = float(input("Enter the right-hand side value c: "))
    
    try:
        solution = linear_equation(a, b, c)
        print(f"The solution to the equation {a}x + {b} = {c} is x = {solution}")
    except ValueError as e:
        print(e)    
if __name__ == "__main__":
    main()