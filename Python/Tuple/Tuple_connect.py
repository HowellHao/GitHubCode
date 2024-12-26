mytuple = (1, 2, 3, 4, 5)
print(mytuple)
while True:
    try:
        choice = int(input("1 to find an element from the tuple \n2 to create a new tuple \n3 to delete an element from the tuple \n4 to exit: "))
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
            mytuple = new_tuple
            print(mytuple)
            try:
                element_to_delete = int(input("Enter the element to delete: "))
                if element_to_delete in mytuple:
                    mytuple = mytuple[:mytuple.index(element_to_delete)] + mytuple[mytuple.index(element_to_delete) + 1:]
                    print(mytuple)
                else:
                    print(f"{element_to_delete} is not in the tuple.")
            except ValueError:
                print("Invalid input. Please enter a valid number to delete.")
        elif choice == 4:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")