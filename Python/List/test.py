from typing import List

def get_choice() -> int:
    while True:
        try:
            return int(input("Enter 1 to insert a number to the list and print the list, 2 to exit: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_number_to_insert() -> int:
    while True:
        try:
            return int(input("Enter a number to insert to the list: "))
        except ValueError:
            print("Invalid input. Please enter a valid number to insert.")

def main() -> None:
    number: List[int] = list(range(1, 10))
    while True:
        choice = get_choice()
        if choice == 1:
            num_to_insert = get_number_to_insert()
            number.insert(0, num_to_insert)
            print(number)
        elif choice == 2:
            print("Exit Program")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()