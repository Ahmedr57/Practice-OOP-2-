# Write a program with a class Inventory that uses a metaclass to enforce that all attributes of any object of Inventory class must be integers only. 
# Raise a TypeError if any non-integer attribute is added to an instance

class Inverntry:
    def __init__(self, attri: int):
        self.attri = attri
        if type(attri) != int:
            raise TypeError("Only Integer values can be added!") 
        print(attri)


inv = Inverntry(56)
#inv2 = Inverntry("Abc")  # Uncomment to check TypeError
