my_dict = {}
my_dict_2 = {}
while True:
    try:
        my_dict['name'] = input("Enter name to dict: ")
        while not my_dict['name'].isalpha():
            print("Please enter a valid name.")
            my_dict['name'] = input("Enter name to dict: ")
        my_dict['age'] = int(input("Enter age to dict: "))
        while my_dict['age'] < 0 or not my_dict['age'].isnumeric():
            print("Please enter a positive number.")
            my_dict['age'] = int(input("Enter age to dict: "))
        my_dict['address'] = input("Enter address to dict: ")
        my_dict['phone'] = input("Enter phone number to dict: ")
        while not my_dict['phone'].isnumeric():
            print("Please enter a valid phone number.")
            my_dict['phone'] = input("Enter phone number to dict: ")
        
        #Second Dictionary input#
        
        my_dict_2['name'] = input("Enter name to dict 2: ")
        while not my_dict_2['name'].isalpha():
            print("Please enter a valid name.")
            my_dict_2['name'] = input("Enter name to dict 2: ")
        my_dict_2['age'] = int(input("Enter age to dict 2: "))
        while my_dict_2['age'] < 0 or not my_dict_2['age'].isnumeric():
            print("Please enter a positive number.")
            my_dict_2['age'] = int(input("Enter age to dict 2: "))
        my_dict_2['address'] = input("Enter address to dict 2: ")
        my_dict_2['phone'] = input("Enter phone number to dict 2: ")
        while not my_dict_2['phone'].isnumeric():
            print("Please enter a valid phone number.")
            my_dict_2['phone'] = input("Enter phone number to dict 2: ")
        print(my_dict)
        print(my_dict_2)
        break
    except ValueError:
        print("Please enter a valid input.")
