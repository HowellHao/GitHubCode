def check_number(n):
    if n < 0:
        return "Negative"
    elif n > 0:
        return "Positive"
    else:
        return "Zero"
try:
    Number = int(input("Insert number: "))
    Result = check_number(Number)
    print(Result)
except ValueError:
    print("Error number")