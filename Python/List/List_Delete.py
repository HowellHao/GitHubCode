number = list(range(1, 10))
while True:
    try:
        choice = int(input("Enter 1 to delete an element from the list and print the list, 2 to exit: "))
        if choice == 1:
            try:
                element_to_delete = int(input("Enter the element to delete: "))
                number.remove(element_to_delete)
                print(number)
            except ValueError:
                print("Invalid input. Please enter a valid number to delete.")
        elif choice == 2:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
