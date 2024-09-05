# Implement a base class Appliance with an abstract method calculate_power_usage(). 
# Create two subclasses WashingMachine and Refrigerator that implement this method. 
# Additionally, create a mixin class EcoFriendly that adds an energy_saving_mode() method to reduce power usage by a percentage. 
# Combine inheritance and mixin to create an EcoWashingMachine.
from abc import ABC, abstractmethod

class Appliance(ABC):
    def __init__(self, wattage):
        self.wattage = wattage

    @abstractmethod
    def calculate_power_usage(self):
        pass

class WashingMachine(Appliance):
    def __init__(self, wattage, hours):
        super().__init__(wattage)
        self.hours = hours
    
    
    def calculate_power_usage(self):
        power_used = (self.wattage * self.hours) / 1000
        return power_used
        
class Refrigerator(Appliance):
    def __init__(self, wattage, hours):
        super().__init__(wattage)
        self.hours = hours
    
    
    def calculate_power_usage(self):
        power_used = (self.wattage * self.hours) / 1000
        return power_used
        
class Ecofriendly:
    def __init__(self, saving_percentage):
        self.saving_percentage = saving_percentage

    def energy_saving_mode(self):
        current_usage = self.calculate_power_usage()
        saved_amount = current_usage * (self.saving_percentage / 100)
        new_usage = current_usage - saved_amount
        print(f"Eco Washing Machine will use {new_usage:.2f} KWh of energy after {self.hours} hours of usage, saving {saved_amount:.2f} KWh")
        return new_usage, saved_amount

    
class EcoWashingMachine(WashingMachine, Ecofriendly):
    def __init__(self, wattage, hours, saving_percentage):
        WashingMachine.__init__(self, wattage, hours)
        Ecofriendly.__init__(self, saving_percentage)



wash = WashingMachine(100, 5)
print(f"Washing Machine: {wash.calculate_power_usage():.2f} KWh")
ref = Refrigerator(300, 24)
print(f"Refrigerator: {ref.calculate_power_usage():.2f} KWh")


ecowash = EcoWashingMachine(100 , 5, 20)
ecowash.energy_saving_mode()