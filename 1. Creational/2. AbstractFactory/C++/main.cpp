#include <iostream>
#include "./src/VehicleFactories.cpp"

VehicleFactory* GetFactory(FactoryMake make){
    if (make == E_FORD){
        return new FordVehicleFactory();
    } else if (make == E_CHEVY){
        return new ChevyVehicleFactory();
    } else if (make == E_NISSAN){
        return new NissanVehicleFactory();
    }
    return NULL;
}

int main(int, char**) {
    VehicleFactory* factory = GetFactory(E_FORD);
    Vehicle* fordCompact = factory->CreateVehicle(2012, "mustang", E_COMPACT);
    fordCompact->PrintInfo();
    Vehicle* fordTruck = factory->CreateVehicle(2012, "F-150", E_TRUCK);
    fordTruck->PrintInfo();
    Vehicle* fordSUV = factory->CreateVehicle(2012, "Escape", E_SUV);
    fordSUV->PrintInfo();

    factory = GetFactory(E_CHEVY);
    Vehicle* chevyCompact = factory->CreateVehicle(2021, "Cobalt", E_COMPACT);
    chevyCompact->PrintInfo();
    Vehicle* chevyTruck = factory->CreateVehicle(2021, "Silverado", E_TRUCK);
    chevyTruck->PrintInfo();
    Vehicle* chevySUV = factory->CreateVehicle(2021, "Expedition", E_SUV);
    chevySUV->PrintInfo();

    factory = GetFactory(E_NISSAN);
    Vehicle* nissanCompact = factory->CreateVehicle(2021, "Altima", E_COMPACT);
    nissanCompact->PrintInfo();
    Vehicle* nissanTruck = factory->CreateVehicle(2021, "truckTruck",E_TRUCK);
    nissanTruck->PrintInfo();
    Vehicle* nissanSUV = factory->CreateVehicle(2021, "bankshot", E_SUV);
    nissanSUV->PrintInfo();
    
    return 0;
};
