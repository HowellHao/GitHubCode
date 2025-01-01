def input_value(prompt, validation_func, error_message):
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
    name = input_value("Enter your name: ", is_valid_name, "Invalid name. Please enter a valid name.")
    age = int(input_value("Enter your age: ", is_valid_age, "Invalid age. Please enter a valid age."))
    address = input("Enter your address: ")
    phone = input_value("Enter your phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number.")
    return {'name': name, 'age': age, 'address': address, 'phone': phone}

my_dict = create_dict()

key_to_find = input("Enter the key to find in the dictionary: ")
if key_to_find in my_dict:
    value=my_dict[key_to_find]
    print(f"The value of the key '{key_to_find}' is '{value}'.")
else:
    print(f"The key '{key_to_find}' is not present in the dictionary.")