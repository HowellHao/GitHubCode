my_dict={}
while True:
    try:
        my_dict['name'] = input("Enter name to dict: ")
        my_dict['age'] = int(input("Enter age to dict: "))
        my_dict['address'] = input("Enter address to dict: ")
        my_dict['phone'] = int(input("Enter phone number to dict: "))
        print(my_dict)
        break
    except ValueError:
        print("Please enter a valid input.")
key_to_find = input("Enter the key to find in the dictionary: ")
if key_to_find in my_dict:
    value=my_dict[key_to_find]
    print(f"The value of the key '{key_to_find}' is '{value}'.")
else:
    print(f"The key '{key_to_find}' is not present in the dictionary.")