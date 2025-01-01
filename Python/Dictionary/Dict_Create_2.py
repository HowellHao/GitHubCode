def get_valid_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

def is_valid_name(name):
    return name.isalpha()

def is_valid_age(age):
    return age.isdigit() and int(age) >= 0

def is_valid_phone(phone):
    return phone.isdigit()

def create_dict():
    my_dict = {}
    my_dict['name'] = get_valid_input("Enter name to dict: ", is_valid_name, "Please enter a valid name.")
    my_dict['age'] = int(get_valid_input("Enter age to dict: ", is_valid_age, "Please enter a positive number."))
    my_dict['address'] = input("Enter address to dict: ")
    my_dict['phone'] = get_valid_input("Enter phone number to dict: ", is_valid_phone, "Please enter a valid phone number.")
    return my_dict

while True:
    try:
        my_dict = create_dict()
        my_dict_2 = create_dict()
        print(my_dict)
        print(my_dict_2)
        break
    except ValueError:
        print("Please enter a valid input.")