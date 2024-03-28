from bicycle import Bicycle
from car import Car
from vehicle import Vehicle

#Test Cases
#1. Create and Display Vehicles:
vehicle = Vehicle("Ford", "Mustang", 2022)
vehicle.display_info()
car = Car("Toyota","Corolla", 2020, "Petrol")
car.display_info()
bicycle = Bicycle("Giant","Anthem", 2019, "Mountain Bike")
bicycle.display_info()

#2. Access Attributes and Methods
print(f"\nCar fuel type: {car.get_fuel_type()}")
print(f"Bicycle type: {bicycle.get_type()}")
