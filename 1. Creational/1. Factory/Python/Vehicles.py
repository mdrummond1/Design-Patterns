from IVehicle import IVehicle

VehicleType = {
    'Ford': 0,
    'Chevy': 1
}


class Vehicle(IVehicle):
    def __init__(self, year, make, model, type):
        self.Year = year
        self.Make = make
        self.Model = model
        self.Type = type

    def ShowInfo(self):
        print(f"this {self.Make}, {self.Model} is a {self.Type} that was made in {self.Year}")

class FordVehicle(Vehicle):
    def __init__(self, year, model, type):
        super().__init__(year, "Ford", model, type)

class ChevyVehicle(Vehicle):
    def __init__(self, year, model, type):
        super().__init__(year, "Chevrolet", model, type)

