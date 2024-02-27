#abstraction and encapsulation

# class car:
#     def __init__(self):
#         self.engine = False
#         self.accleration = False
#         self.clutch = False
#
#     def start(self):
#         self.engine = True
#         self.accleration = True
#         self.clutch = True
#         print('The car is started with expected conditions')
#
#
# carStart = car()
# carStart.start()


# deleting the attribute

class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student('Dhruv')
#print(stu1.name)

del stu1.name
print(stu1.name)
