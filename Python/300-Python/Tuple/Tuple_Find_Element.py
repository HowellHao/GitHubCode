create_tuple = tuple(map(int, input("Enter the elements for the new tuple separated by commas: ").split(' ')))
print(create_tuple)
while True:
    try:
        element = int(input("Enter the element you want to find: "))
        if element in create_tuple:
            print(f"{element} is in the tuple.")
        else:
            print(f"{element} is not in the tuple.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

