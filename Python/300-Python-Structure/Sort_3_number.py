def sort_3_numbers(a, b, c):
    """
    Sort three numbers in ascending order.
    
    Parameters:
    a (float): First number.
    b (float): Second number.
    c (float): Third number.
    
    Returns:
    tuple: A tuple containing the three numbers sorted in ascending order.
    """
    return tuple(sorted([a, b, c]))
def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    
    sorted_numbers = sort_3_numbers(a, b, c)
    print(f"The numbers in ascending order are: {sorted_numbers}")
if __name__ == "__main__":
    main()