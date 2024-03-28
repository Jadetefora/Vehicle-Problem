class Vehicle:

    def __init__(self, new_make, new_model, new_year):
        self.__make = new_make      #private make attrib
        self.__model = new_model    #private model attrib
        self.__year = new_year      #private new year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def display_info(self):
        """Print the make, model and year attribute of Vehicle object."""
        print(f"Vehicle:\nMake: {self.get_make()}\nModel: {self.get_model()}\nYear: {self.get_year()}")


# # Create an instance of vehicle class.
# vehicle = Vehicle("Ford", "Mustang", 2022)
# vehicle.display_info()
