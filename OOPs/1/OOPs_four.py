# Practice Question
''' define a employee class with attributes role, dept, and salary.
this class also has showdetails() methods
create and engineer class that inherits properties form  employee and has additional attribures
name and age'''

class Emp:
    def __init__(self, role, dept, sal):
        self.role = role
        self.department = dept
        self.salary = sal

    def showDetails(self):
        print('Role is: ', self.role)
        print('Department is: ', self.department)
        print('salary is: ', self.salary)



class Engr(Emp):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'tester', '90000')

E1 = Engr('Dhruv', '28')
E1.showDetails()