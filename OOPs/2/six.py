#Program 1

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def print_details(self):
        print("Your details -> Name & Age:", self.__name, self.__age)


perOne = Person("Dhruv", 27)
perOne.print_details()

setting_new_name = perOne.set_name("Lipika")

updated_name = perOne.get_name()
print(updated_name)

perOne.print_details()