class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make : {self.make} Model : {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f" машинка называеться {self.make} моделька {self.model} и кушает она {self.fuel_type}"


a = Vehicle('BMW', 'e38')
print(a.get_info())

car = Car('Ford', 'Mustang', '98')
print(car.get_info())