def Min_Max(a,b,c):
    if b <= a and c <= a:
        return a
    elif a <= b and c <= b:
        return  b
    else:
        return c
try:
    Number_1 = int(input("Insert Number 1: "))
    Number_2 = int(input("Insert Number 2: "))
    Number_3 = int(input("Insert Number 3: "))
    Result = Min_Max(Number_1,Number_2,Number_3)
    print(f"The Max value is: {Result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")