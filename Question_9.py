# Implement a class hierarchy where a base class Employee has subclasses Manager and Developer. 
# Use the __slots__ mechanism in Employee to restrict attribute creation. 
# Write methods to serialize and deserialize objects of these classes using the pickle module.

import pickle

class Employee:
    __slots__ = ['name', 'salary']
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
        
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display_info(self):
        return super().display_info()

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def display_info(self):
        return super().display_info()




# p1 = Manager("John", 5000)
# p2 = Manager("Jack", 4000)
# p3 = Developer("Jordan", 6500)
# p4 = Developer("Julie", 3500)

# To serialize the object using pickle
# with open('john.pickle', 'wb') as f:
#     pickle.dump(p1, f)

# To deserialize the object using pickle.
with open('john.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.display_info()
