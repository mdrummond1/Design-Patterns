#include <iostream>
#include "../src/Vehicles.cpp"


class VehicleFactory{//} : IVehicleFactory{
    private:
        FactoryMake _make;
    public:
        VehicleFactory(FactoryMake make){
            _make = make;
        }

        Vehicle* CreateVehicle(int year, string model, VehicleType category){
            if (category == E_SUV){
                return new SUV(year, _make, model);
            } else if (category == E_COMPACT){
                return new Compact(year, _make, model);
            } else if (category == E_TRUCK){
                return new Truck(year, _make, model);
            }
        }
};

class FordVehicleFactory : public VehicleFactory{
    public:
        FordVehicleFactory()
            : VehicleFactory(E_FORD){}
};

class ChevyVehicleFactory : public VehicleFactory{
    public:
        ChevyVehicleFactory()
            : VehicleFactory(E_CHEVY){}
};

class NissanVehicleFactory : public VehicleFactory{
    public:
        NissanVehicleFactory()
            : VehicleFactory(E_NISSAN){}
};