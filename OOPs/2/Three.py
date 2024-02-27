#Program 1
# class with the user input

class Car:
    color = None
    model = None

    def car_details(self):
        print('Your car color is:',self.color, 'and model is', self.model)


car_color = input('Enter your car color: ')
car_model = input('Enter your car model: ')

car_obj = Car()

car_obj.color = car_color
car_obj.model = car_model
car_obj.car_details()

