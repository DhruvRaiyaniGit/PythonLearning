# Multiple Inheritance

class Father:
    def money(self):
        return 1000000000

class Mother:
    def mom_money(self):
        return 5000000

class Son(Father, Mother):
    def total_inheritence(self):
        return int(Father().money() + Mother().mom_money())


son_obj = Son()
print(son_obj.total_inheritence())