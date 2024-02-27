# Program 1
# class Myclass:
#     name = None
#
#     def printMyName(self):
#         print('My name is', self.name)
#
#
# mc1 = Myclass()
# mc1.printMyName() #My name is None
# mc1.name = 'Dhruv Raiyani'
# mc1.printMyName() #My name is Dhruv Raiyani


#Program 2
# class Myclass2:
#     def printMyName(self, firstname, lastname):
#         self.fn = firstname
#         self.ln = lastname
#         print('My name is', self.ln, self.fn)
#
# mc2 = Myclass2()
# mc2.printMyName('Dhruv','Raiyani')

#Program 3 (simplified version of program 2)
class Myclass2:
    def printMyName(self, firstname, lastname):
        # self.fn = firstname
        # self.ln = lastname
        print('My name is', firstname,lastname)

mc2 = Myclass2()
mc2.printMyName('Dhruv','Raiyani')

