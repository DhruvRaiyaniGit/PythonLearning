
class Car:
    #attributes
    name = None
    color = None
    model = None
    speed = None
    engine = None

#methods
    def start_engine(self):
        print('Starting Engine')

    def drive(self):
        print('Drive')

    def car_brake(self):
        print('Brake')

    def whoisdriving(self):
        print('I am driving ->', self.name)


Tesla_obj = Car()
Lambo_obj = Car()

Tesla_obj.name = 'Tesla'
Lambo_obj.name = 'Lamborghini'

Tesla_obj.whoisdriving()
Lambo_obj.whoisdriving()


