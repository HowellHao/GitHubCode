number = list(range(1, 10))
while True:
    try:
        choice = int(input("Enter 1 to insert a number to the list and print the list, 2 to exit: "))
        if choice == 1:
            try:
                num_to_insert = int(input("Enter a number to insert to the list: "))
                number.insert(0,num_to_insert)
                print(number)
            except ValueError:
                print("Invalid input. Please enter a valid number to insert.")
        elif choice == 2:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")