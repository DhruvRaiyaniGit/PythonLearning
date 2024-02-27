# Method Overloading
# Python does not support the method overloading in the traditional sense
# to overcome this, we are giving the default value of parameters as 0
# it means in python we are using the default parameters and we are not using the method overloading


class Mathfn:
    def addition(self, a, b=0, c=0): # to overcome method overloading, we are giving the default value of parameters as 0
        return a+b+c


math_obj = Mathfn()
op1 = math_obj.addition(3,4)
op2 = math_obj.addition(1,2,3)
op3 = math_obj.addition(9)  # 9 will be assign to the value of a, and we need to pass atleast value of a because there is no default value of a

print(op1)
print(op2)
print(op3)
