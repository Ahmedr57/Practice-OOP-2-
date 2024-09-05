# Implement a class Vehicle that uses private attributes and private methods. 
# Create a derived class Car that overrides one of the private methods from the Vehicle class using name mangling. 
# Demonstrate how to access these private members outside the class.

class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        
    def __display_info(self):
        print(f"Make: {self.__make}")
        print(f"Model: {self.__model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.__year = year

    def __display_info(self):
        super()._Vehicle__display_info()
        print(f"Year: {self.__year}")

my_car = Car("Toyota", "Camary", 2024)
print(my_car._Car__year)
my_car._Car__display_info()