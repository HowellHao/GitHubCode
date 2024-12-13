def Calulate_taxi(km):
    if km <= 1:
        return 1
    elif 2 <= km <= 10:
        return 1 + ((km - 1) * 0.85)
    else:
        return 1 + 8.5+ ((km-10) * 0.75)
try:
    Km = float(input("Enter the distance in km: "))
    Total = Calulate_taxi(Km)
    print(f"The total taxi fare is: ${Total:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    