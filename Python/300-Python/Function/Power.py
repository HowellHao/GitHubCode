def power(base,exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base,exponent-1)
while True:
    try:
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        print("The result is: ",power(base,exponent))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
    