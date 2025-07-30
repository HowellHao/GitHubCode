number = list(range(1, 10))
while True:
    try:
        choice = int(input("Enter 1 to append a number to the list and print the list, 2 to exit: "))
        if choice == 1:
            try:
                num_to_append = int(input("Enter a number to append to the list: "))
                number.append(num_to_append)
                print(number)
            except ValueError:
                print("Invalid input. Please enter a valid number to append.")
        elif choice == 2:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")