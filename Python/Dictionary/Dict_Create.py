my_dict = {}
my_dict_2 = {}
while True:
    try:
        my_dict['name'] = input("Enter name to dict: ")
        my_dict['age'] = int(input("Enter age to dict: "))
        my_dict['address'] = input("Enter address to dict: ")
        my_dict['phone'] = int(input("Enter phone number to dict: "))
        my_dict_2['name'] = input("Enter name to dict 2: ")
        my_dict_2['age'] = int(input("Enter age to dict 2: "))
        my_dict_2['address'] = input("Enter address to dict 2: ")
        my_dict_2['phone'] = int(input("Enter phone number to dict 2: "))
        print(my_dict)
        print(my_dict_2)
        break
    except ValueError:
        print("Please enter a valid input.")
