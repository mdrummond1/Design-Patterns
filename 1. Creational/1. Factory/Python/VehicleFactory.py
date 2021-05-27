from Vehicles import ChevyVehicle, FordVehicle, VehicleType

class IVehicleFactory:
    def __init__(self):
        pass
    
    def GetVehicle(self, type):
        pass

class VehicleFactory(IVehicleFactory):

    def GetVehicle(self, type, year, make, model):
        if make == VehicleType['Ford']:
            return FordVehicle(year, model, type)
        elif make == VehicleType['Chevy']:
            return ChevyVehicle(year, model, type)

        return None

