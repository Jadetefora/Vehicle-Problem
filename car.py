from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, new_make, new_model, new_year, new_fuel_type):
        super().__init__(new_make, new_model, new_year)
        self.fuel_type = new_fuel_type

    def get_fuel_type(self):
        return self.fuel_type
    def display_info(self):
        """Dislay the make, model, year and fuel type of Car object."""
        print(f"\nCar:\nMake: {self.get_make()}\nModel: {self.get_model()}\nYear: {self.get_year()}\nFuel Type: {self.get_fuel_type()}")


# # Create instances of cars.
# car = Car("Toyota", "Corolla", 2020, "Petrol")
# car.display_info()
#
# car_two = Car(input("Type your car make: "), input("What is your car's model: "),
#               int(input("What year did you buy your car?: ")), input("What is your car's fuel type?: "))
# car_two.display_info()
