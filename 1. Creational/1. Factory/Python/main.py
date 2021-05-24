from Vehicles import *
from VehicleFactory import *

factory = VehicleFactory()
ford = factory.GetVehicle("sports car", 2021, VehicleType['Ford'], "mustang")
chevy = factory.GetVehicle("sports car", 2021, VehicleType['Chevy'], "camaro")
ford.ShowInfo()
chevy.ShowInfo()
