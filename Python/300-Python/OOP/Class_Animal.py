from abc import ABC, abstractmethod
class Animal(ABC):
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow"
class Cow(Animal):
    def sound(self):
        return "Moo"
dog = Dog()
cat = Cat()
cow = Cow()
print(f"Dog: {dog.sound()}")
print(f"Cat: {cat.sound()}")
print(f"Cow: {cow.sound()}")