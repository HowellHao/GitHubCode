def even_odd (n):
    if n % 2 == 0:
        return "even"
    elif n % 2 == 1:
        return "odd"
    else:
        return "Zero"
    
try:
    Number = int(input("Insert Number: "))
    Result = even_odd(Number)
    print(f"The number {Number} is {Result}")
except ValueError:
    print ("Error")
