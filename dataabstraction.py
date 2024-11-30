from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod
    def get_fuel_type(self):
        pass
    
class Car(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type=fuel_type
    def start_engine(self):
        print("car engine started.")
    def stop_engine(self):
        print("car engine stopped.")
    def get_fuel_type(self):
        return self.fuel_type
class Motorcycle(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type=fuel_type
    def start_engine(self):
        print("Motorcycle engine started.")
    def stop_engine(self):
        print("Motorcycle engine stopped.")
    def get_fuel_type(self):
        return self.fuel_type
    
car=Car(fuel_type="Gasoline")
motorcycle=Motorcycle(fuel_type="Petrol")
Vehicles=[car,motorcycle]
for vehicle in Vehicles:
    print(f"Fuel type:{vehicle.get_fuel_type()}")
    vehicle.start_engine()
    vehicle.stop_engine()
    print()