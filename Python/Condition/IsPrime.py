def is_Prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def Print_prime_100():
    for i in range(1,101):
        if is_Prime(i):
            print(i, end=" ")
    print()

Print_prime_100()
    
    