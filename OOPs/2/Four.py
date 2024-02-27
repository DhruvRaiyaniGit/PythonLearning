#Program 1
#default constructor __init__


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('You created init constructor with name and age')
#
#
#     def persondetails(self):
#         print('Your name is', self.name, 'and your age is', self.age)
#
# personOne = Person('dhruv', 27)
# personOne.persondetails()



#Program 2
#default constructor __init__, using 2 times in a class


class Person:

    def __init__(self):
            # self.name = name
            # self.age = age
            print('You created 2nd init constructor with only name')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('You created init constructor with name and age')




    def persondetails(self):
        print('Your name is', self.name, 'and your age is', self.age)

    def persondetails2(self):
        print('Your name is', self.name)


personOne = Person('dhruv', 27)
personOne.persondetails()




