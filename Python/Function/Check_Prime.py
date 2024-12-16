def Is_prime (n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
try:
    n = int(input("Enter a number: "))
    if Is_prime (n):
        print (n, "is a prime number")
    else:
        print (n, "is not a prime number")
except ValueError:
    print ("Invalid input. Please enter a valid number.")
        
