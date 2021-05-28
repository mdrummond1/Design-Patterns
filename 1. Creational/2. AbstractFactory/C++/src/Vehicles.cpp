#include <iostream>
using namespace std;

enum FactoryMake{
    E_FORD,
    E_CHEVY,
    E_NISSAN
};

enum VehicleType{
    E_SUV,
    E_TRUCK,
    E_COMPACT
};

class Vehicle{
    protected:
        VehicleType _category;
        FactoryMake _make;
        int _year;
        string _model;

        string GetCategory(){
            if (_category == E_SUV){
                return "SUV";
            } else if (_category == E_TRUCK){
                return "Truck";
            } else if (_category == E_COMPACT){
                return "Compact";
            }
            return "";
        }

        string GetMake(){
            if (_make == E_FORD){
                return "Ford";
            } else if (_make == E_CHEVY){
                return "Chevrolet";
            } else if (_make == E_NISSAN){
                return "Nissan";
            }
            return "";
        }

    protected:
        Vehicle(int year, FactoryMake make, string model, VehicleType category){
            _year = year;
            _make = make;
            _model = model;
            _category = category;
        }
    public:
        void PrintInfo(){
            cout << "this " << GetCategory() << " is a " << _year << " " << GetMake() << " " << _model << endl;
        }
};


class SUV :public Vehicle{
    public:
        SUV(int year, FactoryMake make, string model)
            : Vehicle(year, make, model, E_SUV) { }
};

class Compact :public Vehicle{
    public:
        Compact(int year, FactoryMake make, string model)
            : Vehicle(year, make, model, E_COMPACT){}
};

class Truck :public Vehicle{
    public:
        Truck(int year, FactoryMake make, string model)
            : Vehicle(year, make, model, E_TRUCK){}
};
