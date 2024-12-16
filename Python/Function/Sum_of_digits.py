def sum_of_digits(n):
    n =abs(n)
    digit = 0
    while n > 0:
        digit += n % 10
        n //= 10
    return digit
while True:
    try:
        numbers = int(input("Insert Numbers: "))
        sum = sum_of_digits(numbers)
        print(f"Sum of digits is {sum}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.") 
                  