# Question: Create a Python program where a class Robot has attributes name and model. Write a subclass FlyingRobot that adds an attribute altitude. 
# Then, implement a method in FlyingRobot that overrides a method from Robot to display the robot's name, model, and current altitude, 
# but also ensure this method maintains Liskov Substitution Principle.

class Robot:
    def __init__(self, name , model):
        self.name = name
        self.model = model
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")

class FlyingRobot(Robot):
    def __init__(self, name, model, altitude):
        super().__init__(name, model)
        self.altitude = altitude

    def display(self):
        super().display()
        print(f"Altitude: {self.altitude} Meters")


robo1 = Robot("Omega", "T100")
flyrobo1 = FlyingRobot("Bumblebee", "B450", 3000)

robo1.display()

flyrobo1.display()