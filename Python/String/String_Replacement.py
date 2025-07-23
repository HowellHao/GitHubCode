def is_invalid_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if not validation_func(value):
            print(error_message)
        else:
            return value
 
def is_valid_name(name):
     return name.isalpha()

def is_valid_age(age):
     return age.isdigit() and int(age) >= 0 

def is_valid_phone(phone):
     return phone.isdigit()

def is_valid_address(address):
     return any(address.isalpha() for address in address) and any(address.isdigit() for address in address)

def create_string():
    name = is_invalid_input("Enter your name: ", is_valid_name, "Invalid name. Please enter a valid name.")
    age = is_invalid_input("Enter your age: ", is_valid_age, "Invalid age. Please enter a valid age.")
    address = is_invalid_input("Enter your address: ", is_valid_address, "Invalid address. Please enter a valid address.")
    phone = is_invalid_input("Enter your phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number.")
    return "Name: " + name + ", Age: " + age + ", Address: " + address + ", Phone: " + phone + ", "

my_string = create_string()
print(my_string)

my_string_word_to_replacement = input("Enter the word to replace to the existing string: ")
print(my_string_word_to_replacement)

my_string_replacement_word = input("Enter the word to replace with: ")
print(my_string_replacement_word)

my_string = my_string.replace(my_string_word_to_replacement, my_string_replacement_word)

print(my_string)

if isinstance(my_string, str):
    print("The input is a string.")
else:
    print("The input is not a string.")