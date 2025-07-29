class people:
    def __init__(self, name, IDStaff, age, address, phone_number, email, position):
        self.name = name
        self.age = age
        self.IDStaff = IDStaff
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
    
    def display(self):
        print(f"Name: {self.name}, ID: {self.IDStaff}, Age: {self.age}, Address: {self.address}, Phone: {self.phone_number}, Email: {self.email}, Position: {self.position}")

class Student(people):
    def __init__(self, name, IDStudent, age, address, phone_number, email, major, grade):
        super().__init__(name, IDStudent, age, address, phone_number, email, "Student")
        self.major = major
        self.grade = float(grade)
    
    def display(self):
        super().display()
        print(f"Major: {self.major}")
        print(f"Grade: {self.grade}")

    def is_passing(self):
        if self.grade < 2.0:
            return "Failing"
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
def is_valid_grade(grade):
    try:
        grade_float = float(grade)
        return 0.0 <= grade_float <= 4.3
    except ValueError:
        return False

def create_student():
    name = get_valid_input("Enter student's full name: ", is_valid_name, "Invalid name. Please enter at least first and last name with alphabetic characters.")
    IDStudent = get_valid_input("Enter student ID (8 digits): ", is_valid_ID, "Invalid ID. Please enter an 8-digit number.")
    age = get_valid_input("Enter student's age: ", is_valid_age, "Invalid age. Please enter a non-negative integer.")
    address = get_valid_input("Enter student's address: ", is_valid_address, "Invalid address. Please include both letters and numbers.")
    phone_number = get_valid_input("Enter student's phone number: ", is_valid_phone, "Invalid phone number. Please enter digits only.")
    email = get_valid_input("Enter student's email: ", is_valid_email, "Invalid email. Please include '@' and '.' with a minimum length of 6 characters.")
    major = get_valid_input("Enter student's major: ", lambda x: x.isalpha() and len(x) > 0, "Invalid major. Please enter alphabetic characters only.")
    grade = get_valid_input("Enter student's grade (0.0 to 4.3): ", is_valid_grade, "Invalid grade. Please enter a number between 0.0 and 4.3.")

    return Student(name, IDStudent, age, address, phone_number, email, major, grade)   

print("Enter student details:")
student = create_student()
print("\nStudent Information:")
student.display()
print("\nStudent Status:")
print(f"{student.name} is {student.is_passing()}. Honors: {student.is_honors()}. Scholarship: {student.is_scholarship()}.")