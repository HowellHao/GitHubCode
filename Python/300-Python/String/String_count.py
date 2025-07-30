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

def is_valid_address(address):
    return any(address.isalpha() for address in address) and any(address.isdigit() for address in address)

def create_string():
    name = get_valid_input("Enter your name: ", is_valid_name, "Invalid name. Please enter a valid name.")
    age = get_valid_input("Enter your age: ", is_valid_age, "Invalid age. Please enter a valid age.")
    address = get_valid_input("Enter your address: ", is_valid_address, "Invalid address. Please enter a valid address.")
    phone = get_valid_input("Enter your phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number.")
    return "Name: " + name + ", Age: " + age + ", Address: " + address + ", Phone: " + phone + ", "

my_string = create_string()
print(my_string)
if isinstance(my_string, str):
    print("The input is a string.")
else:
    print("The input is not a string.")

char_count = input("Enter the string to add to the existing string: ")
count = my_string.count(char_count)
print(f"The number of times the string '{char_count}' appears in the string is: {count}")

