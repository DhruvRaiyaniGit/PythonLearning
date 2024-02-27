# Hybrid Inheritance

class AA:
    def methodAA(self):
        return 'This is the method of AA class'


class BB(AA):
    def methodBB(self):
        return 'This is the method of BB class'


class CC(AA):
    def methodCC(self):
        return 'This is the method of CC class'


class DD(CC,BB):
    def methodDD(self):

        return 'This is the method of DD class', AA().methodAA(), BB().methodBB(), CC().methodCC()


DD_obj = DD()
print(DD_obj.methodDD())
#this is i am editing to commit second time

print("Thanks to me for doing the work")