from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Dog(Animal):
    def make_sound(self):
        return "Woof"

    def move(self):
        return "Runs on four legs" 
class Cat(Animal):
    def make_sound(self):
        return "Meow"

    def move(self):
        return "Pounces gracefully"
class Cow(Animal):
    def make_sound(self):
        return "Moo"

    def move(self):
        return "Walks slowly on four legs"

def create_animal():
    name = input("Enter animal name: ")
    age = input("Enter animal age: ")
    animal_type = input("Enter animal type (Dog/Cat/Cow): ").strip().lower()

    if animal_type == "dog":
        return Dog(name, age)
    elif animal_type == "cat":
        return Cat(name, age)
    elif animal_type == "cow":
        return Cow(name, age)
    else:
        print("Invalid animal type. Please try again.")
        return create_animal()

animal = create_animal()
animal.display_info()
print(f"Sound: {animal.make_sound()}")
print(f"Movement: {animal.move()}")
print(f"{animal.name} is {animal.age} years old.")