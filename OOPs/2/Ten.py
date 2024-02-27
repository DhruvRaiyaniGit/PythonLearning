#Multilevel Inheritance

class Grandfather:
     def grandfather_method(self):
         return "This is a grandfather's method"

class Father(Grandfather):
    def father_method(self):
        return "This is a father's method"

class Son(Father):
    def son_method(self):
        return "This is a son's method"


family = Son()
print(family.son_method())
print(family.father_method())
print(family.grandfather_method())  #all the methods of the parents called from the child class