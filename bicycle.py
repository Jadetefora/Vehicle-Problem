from vehicle import Vehicle


class Bicycle(Vehicle):

    def __init__(self, new_make, new_model, new_year, new_type):
        super().__init__(new_make, new_model, new_year)
        self.type = new_type

    def get_type(self):
        return self.type

    def display_info(self):
        print(f"\nBicycle:\nMake: {self.get_make()}\nModel: {self.get_model()}\nYear: {self.get_year()}\nType: {self.get_type()}")


# bicycle = Bicycle("Giant", "Anthem", 2019, "Mountain Bike")
# bicycle.display_info()
