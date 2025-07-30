def gcd(a,b):
    while b:
        a,b = b,a % b
        return a
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The GCD of", a, "and", b, "is", gcd(a,b))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
                                               