'''#def space(k):
    return " " *k
def Multiplication_tables():
    for h in range(10):
        i= h+1
        for j in range(1, 6):
            print (f"{i} * {j} = {i * j}" .rjust(2), end=" | ")
        print()
    print()
    
    for h in range(10):
        i = h + 1
        for j in range (6 ,11):
            print (f"{i} * {j} = {i * j}" .rjust(2), end=" | ")
        print()
Multiplication_tables()'''

def Multiplication_tables():
    for i in range(1,11):
        for j in range(1,11):
            print (f"{j} * {i} = {i * j}".center(5), end="\t")
        print()
    print()
Multiplication_tables()