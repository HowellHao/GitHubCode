def factorial_iterative(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    number = int(input("Insert Number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"Factorial of {number} is {factorial_iterative(number)}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
        