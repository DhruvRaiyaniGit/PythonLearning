# Polymorphism - one object can have many forms
# Object - behaves differently based on situation

class Shape:
    def area(self):
        print("This is the area of a shape")


class Rectangle(Shape):

    def __init__(self, lenght, breath):
        self.lenght = lenght
        self.breath = breath

    def area(self):
        return self.lenght * self.breath


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius



rec_obj = Rectangle(12,25)
print("The area of rectangle is: ", rec_obj.area())

circle_obj = Circle(22)
print("The area of circle is: ", circle_obj.area())

# In the above program the same object name 'area' is used in the multiple classes
# If the calling onject is not present in the class but it is present in the parent class then it will be called from the parent class


