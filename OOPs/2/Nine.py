#Inheritance
#single inheriance

class Animal:
    def animal_breed(self):
        print('Bull Dog')

    def animal_speak(self):
        print('Dog can bark')


class Dog(Animal):
    def dog_voice(self):
        Animal().animal_speak()

dog_obj = Dog()
dog_obj.dog_voice()
dog_obj.animal_breed()
