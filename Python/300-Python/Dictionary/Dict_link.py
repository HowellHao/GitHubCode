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
    return age.isdigit() and int(age) > 0
def is_valid_phone(phone):
    return phone.isdigit()
def create_dict():
    name = get_valid_input("Enter your name: ", is_valid_name, "Invalid name. Please enter a valid name.")
    age = get_valid_input("Enter your age: ", is_valid_age, "Invalid age. Please enter a valid age.")
    address = input("Enter your address: ")
    phone = get_valid_input("Enter your phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number.")
    return {'name': name, 'age': age, 'address': address, 'phone': phone}
my_dict = create_dict()
my_dict_2 = create_dict()
print("The dictionaries are:")
print(my_dict)
print(my_dict_2)
my_dict_3 = my_dict.copy()
my_dict_3.update(my_dict_2)
print("The updated dictionary is:")
print(my_dict_3)
my_dict_4 = {**my_dict, **my_dict_2}
print("The updated dictionary is:")
print(my_dict_4)