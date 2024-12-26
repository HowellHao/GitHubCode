def celsius_to_farenheit(cel):
    return (cel * 9/5) + 32
def farenheit_to_celsius(far):
    return (far - 32) * 5/9
def farenheit_to_kelvin(far):
    return (far - 32) * 5/9 + 273.15
def kelvin_to_farenheit(kel):
    return (kel - 273.15) * 9/5 + 32
def kelvin_to_celsius(kel):
    return kel - 273.15
def celsius_to_kelvin(cel):
    return cel + 273.15
while True:
    try:
        print("\nTemperature Conversion Menu")
        print("1. Celsius to Farenheit")
        print("2. Farenheit to Celsius")
        print("3. Farenheit to Kelvin")
        print("4. Kelvin to Farenheit")
        print("5. Kelvin to Celsius")
        print("6. Celsius to Kelvin")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            cel = float(input("Enter temperature in Celsius: "))
            print(f"{cel}°C is equal to {celsius_to_farenheit(cel)}°F")
        elif choice == 2:
            far = float(input("Enter temperature in Farenheit: "))
            print(f"{far}°F is equal to {farenheit_to_celsius(far )}°C")
        elif choice == 3:
            far = float(input("Enter temperature in Farenheit: "))
            print(f"{far}°F is equal to {farenheit_to_kelvin(far)}°K")
        elif choice == 4:
            kel = float(input("Enter temperature in Kelvin: "))
            print(f"{kel}°K is equal to {kelvin_to_farenheit(kel)}°F")
        elif choice == 5:
            kel = float(input("Enter temperature in Kelvin: "))
            print(f"{kel}°K is equal to {kelvin_to_celsius(kel)}°C")
        elif choice == 6:
            cel = float(input("Enter temperature in Celsius: "))
            print(f"{cel}°C is equal to {celsius_to_kelvin(cel)}°K")
        elif choice == 7:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")