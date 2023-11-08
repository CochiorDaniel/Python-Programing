class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return self.mileage


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return self.mileage


class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, towing_capacity):
        super().__init__(make, model, year)
        self.mileage = mileage
        self.towing_capacity = towing_capacity

    def calculate_mileage(self):
        return self.mileage

    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car('Dacia', 'Logan', 2002, 500233)
print("Kilometraj masina: ", car.calculate_mileage())

truck = Truck('Volvo', 'FLN', 2020, 13000, 6000)
print("Kilometraj camion: ", truck.calculate_mileage())
print("Capacitate tractare: ", truck.calculate_towing_capacity())

