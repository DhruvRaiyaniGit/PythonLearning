# Method Overloading
# Python does not support the method overloading in the traditional sense

class Mathfn:
    def addition(self, a, b):
        print(a+b)

    def addition(self, a, b, c):
        print(a+b+c)


math_obj = Mathfn()
math_obj.addition(3,4)


# If we pass only 2 parametes then it will not work, for working with 1,2,or 3 parameters we need another trick to use it, check Seventeen.py