# OOps - Abstraction
# Hiding the details and showing only required details
# ABC = Abstract Base Class | Abstract base methods

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bow Bow"


class Cat(Animal):

    def sound(self):
        return "meow meow"


class Lion(Animal):
    def sound(self):
        return "roar roar"


dog_obj = Dog()
print(dog_obj.sound())

cat_obj = Cat()
print(cat_obj.sound())

lion_obj = Lion()
print(lion_obj.sound())