# Practice Question
'''Define a circle class to create a circle with radius r using the constructor.
Define an area() method of a class which calculates the area of the circle
Define a Perimeter() method of a calss which calculares the perimeter of the circle'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    #area of a circle
    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius


C1 = Circle(14)
print(C1.area())
print(C1.perimeter())