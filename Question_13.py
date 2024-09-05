# Write a program that defines a base class Animal with a method speak(). Create a subclass Dog that overrides the speak() method. 
# Implement another class RobotDog that inherits from both Dog and a class Robot using multiple inheritance. 
# Ensure that the speak() method uses the super() function correctly to call the Dog's method.

class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        print("Animal is Speaking!")

class Dog(Animal):
    def __init__(self, name ):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} : Woof!")

class Robot:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Name: {self.name}")

class RobotDog(Dog, Robot):
    def __init__(self, name):
        Dog.__init__(self, name)
        Robot.__init__(self, name)


    def speak(self):
        super().speak()

tom = RobotDog("TOMY")
tom.speak()