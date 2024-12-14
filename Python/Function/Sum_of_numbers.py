def Sum_of_numbers(n):
    if  n < 0:
        return "Number should be Positive Number"
    elif n == 0:
        return 0
    else:
        return n + Sum_of_numbers(n-1)
try:
    number = int (input("Insert Number: "))
    if number < 0:
        print("Number should be Positive Number")
    else:
        print(f"Sum of number {number} is {Sum_of_numbers(number)}")
except ValueError:
    print("Invalid Input")
        