# Write a class Shape that is abstract and has an abstract method area(). Implement two subclasses Rectangle and Circle that calculate the area. 
# Use decorators to log the time taken to compute the area of the shape each time the method is called.

from abc import ABC, abstractmethod
import math
import time

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def time_it(method):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Time taken to calculate area: {end_time - start_time:.4f} seconds")
            return result
        return wrapper

    @time_it   
    def area(self):
        Area = self.length * self.width
        return print(f"Area of Rectangle is: {Area}")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def time_it(method):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Time taken to calculate area: {end_time - start_time:.4f} seconds")
            return result
        return wrapper
    
    @time_it
    def area(self):
        Area = math.pi * self.radius**2
        return print(f"Area of Circle is: {Area:.2f}")



cir1 = Circle(50)
cir1.area()

rec1 = Rectangle(20,43)
rec1.area()

cir2 = Circle(6.1)
cir2.area()

rec2 = Rectangle(5,3)
rec2.area()