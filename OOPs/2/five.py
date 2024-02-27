#Program 1
# class Car:
#     def __init__(self, fuel_level):
#         self.fuel_level = fuel_level
#
#     def check_fuel(self):
#         if self.fuel_level > 0:
#             return True
#         else:
#             print("Car has low fuel!")
#             return False
#
#     def start_engine(self):
#         if self.check_fuel():
#             print("Engine started!")
#         else:
#             print("Cannot start engine - low fuel!")
#
# Flevel = int(input('enter the fuel level- '))
# car1 = Car(Flevel)
# car1.start_engine()  # Prints: Engine started!
#

# Program - 2 (with minimal syntax change)

class Car:
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level

    # def check_fuel(self):
    #     if self.fuel_level > 0:
    #         return True
    #     else:
    #         print("Car has low fuel!")
    #         return False

    def start_engine(self):
        if self.fuel_level > 0:
            print("Engine started!")
        else:
            print("Cannot start engine - low fuel!")

Flevel = int(input('enter the fuel level- '))
car1 = Car(Flevel)
car1.start_engine()  # Prints: Engine started!

