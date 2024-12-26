mytuple = (1, 2, 3, 4, 5)
print(mytuple)
while True:
    try:
        choice = int(input("Enter 1 to find an element from the tuple, 2 to create a new tuple, 3 to exit: "))
        if choice == 1:
            try:
                element = int(input("Enter the element you want to find: "))
                if element in mytuple:
                    print(f"{element} is in the tuple.")
                else:
                    print(f"{element} is not in the tuple.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 2:
            try:
                second_tuple = tuple(map(int, input("Enter the elements for the new tuple separated by space: ").split(' ')))
                print(second_tuple)
                new_tuple = mytuple + second_tuple
                print(new_tuple)
            except ValueError:
                print("Invalid input. Please enter valid numbers separated by space.")
        elif choice == 3:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")