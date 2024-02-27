# using the six.py, restrict the name 'Rahul' to set

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == 'Rahul':
            print("Don't set this name")
        else:
            self.__name = name

    def print_details(self):
        print("Your details -> Name & Age:", self.__name, self.__age)


perOne = Person("Dhruv", 27)
perOne.print_details()

setting_new_name = perOne.set_name("Rahul")

updated_name = perOne.get_name()
print(updated_name)

perOne.print_details()