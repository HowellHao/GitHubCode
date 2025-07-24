class Student:
    def __init__(self, name, IDStudent, age, address, phone_number, email, major, grade):
        self.name = name
        self.age = age
        self.IDStudent = IDStudent
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.major = major
        self.grade = float(grade)

    def display(self):
        print(f"Name: {self.name}, ID: {self.IDStudent}, Age: {self.age}, Address: {self.address}, Phone: {self.phone_number}, Email: {self.email}, Major: {self.major}, Grade: {self.grade}")

    def is_passing(self):
        if self.grade < 2.0:
            return "F"
        elif 2.0 <= self.grade < 3.0:
            return "C"
        elif 3.0 <= self.grade < 3.5:
            return "B"
        elif 3.5 <= self.grade <= 4.0:
            return "A"
        else:
            return "A++"
        
    def is_honors(self):
        if 3.5 <= self.grade < 3.7:
            return "Cum Laude"
        elif 3.7 <= self.grade < 4.0:
            return "Magna Cum Laude"
        elif 4.0 <= self.grade <= 4.3:
            return "Summa Cum Laude"
        else:
            return "No Honors"

    def is_scholarship(self):
        if self.grade >= 3.5:
            return "Eligible for Scholarship"
        else:
            return "Not Eligible for Scholarship"

def get_valid_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

def is_valid_name(name):
    parts = name.strip().split()
    return len(parts) >= 2 and all(part.isalpha() for part in parts)

def is_valid_age(age):
    return age.isdigit() and int(age) >= 0

def is_valid_phone(phone):
    return phone.isdigit()

def is_valid_address(address):
    return any(c.isalpha() for c in address) and any(c.isdigit() for c in address)

def is_valid_email(email):
    return "@" in email and "." in email and len(email) > 5

def is_valid_ID(ID):
    return ID.isdigit() and len(ID) == 8

def is_valid_major(major):
    return major.isalpha() and len(major) > 0

def is_valid_grade(grade):
    try:
        grade = float(grade)
        return 0.0 <= grade <= 4.3
    except ValueError:
        return False 

def create_student():
    name = get_valid_input("Enter your name (first and last): ", is_valid_name, "Invalid name. Please enter at least first and last name, letters only.")
    IDStudent = get_valid_input("Enter your student ID (8 digits): ", is_valid_ID, "Invalid ID. Please enter an 8-digit ID.")
    age = get_valid_input("Enter your age: ", is_valid_age, "Invalid age. Please enter a valid age.")
    address = get_valid_input("Enter your address: ", is_valid_address, "Invalid address. Please enter a valid address (must contain letters and numbers).")
    phone_number = get_valid_input("Enter your phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number.")
    email = get_valid_input("Enter your email: ", is_valid_email, "Invalid email. Please enter a valid email.")
    major = get_valid_input("Enter your major: ", is_valid_major, "Invalid major. Please enter a valid major.")
    grade = get_valid_input("Enter your GPA (0.0 - 4.3): ", is_valid_grade, "Invalid GPA. Please enter a valid GPA between 0.0 and 4.3.") 
    return Student(name, IDStudent, age, address, phone_number, email, major, grade)

print("Enter student details:")
student = create_student()
student.display()
print(f"{student.name} is {student.is_passing()}. Honors: {student.is_honors()}. Scholarship: {student.is_scholarship()}.")