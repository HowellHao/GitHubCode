mytuple = (1, 2, 3, 4, 5)
print(mytuple)
while True:
    try:
        choice = int(input("Enter 1 to find an element from the tuple, 2 to delete an element from the tuple, 3 to exit: "))
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
                element_to_delete = int(input("Enter the element to delete: "))
                if element_to_delete in mytuple:
                    mytuple = mytuple[:mytuple.index(element_to_delete)] + mytuple[mytuple.index(element_to_delete) + 1:]
                    print(mytuple)
                else:
                    print(f"{element_to_delete} is not in the tuple.")
            except ValueError:
                print("Invalid input. Please enter a valid number to delete.")
        elif choice == 3:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")