# Overriding - Same name in the parent and child
# Child always override the parent function
# Super means call my parent function

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        super().sound()    # Using super will call the sound method from the parent class
        print("Dog Sound")


dog_obj = Dog()
dog_obj.sound() # here the sound function from the animal class also called because of using the super function
