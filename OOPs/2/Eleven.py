# Hierarchical Inheritance

class Father:
    def properties(self):
        flats = 5
        agriland = 100
        print('we have total', flats, 'and total agrilands in vigha =', agriland)


class Son(Father):
    def property_owner(self):
        Father().properties()

class Daughter(Father):
    def property_owner(self):
        Father().properties()



#son's inherit property from the father's property
son_obj = Son()
son_obj.property_owner()

#daughter's inherit property from the father's property
daughter_obj = Daughter()
daughter_obj.property_owner()