class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}", f"Grade: {self.grade}")
    def is_passing(self):
        if self.grade <= 50:
            return "Failing"
        else:
            return "Passing"
Student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 22, 45)
Student1.display()
print(f"{Student1.name} is {Student1.is_passing()}.")
student2.display()
print(f"{student2.name} is {student2.is_passing()}.")