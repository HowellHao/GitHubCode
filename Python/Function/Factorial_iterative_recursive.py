def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    else:
        return n * factorial_recursive(n-1)
try:
    print(factorial_recursive(5))
except ValueError:
    print("Factorial is not defined for negative numbers")
    