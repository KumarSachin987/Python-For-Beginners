'''
What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design software. It allows you to create classes, which act as blueprints for objects. This approach helps in organizing and structuring code in a more modular and reusable way.

Classes
A class in Python is like a blueprint or template for creating objects. It defines a set of attributes and methods that the objects created from the class will have. Think of a class as a car factory where you design the blueprint for different types of cars.

Objects
Objects are instances of a class. When you create an object from a class, you are instantiating the class. An object represents a specific example of the class.
'''

class Car:
    def __init__(self,model, color):
        self.model = model
        self.color = color

    def showInfo(self):
        print(f"The model of the car is {self.model} and color of the car is {self.color}")

# alto = Car('Alto', 'White')
alto = Car(model='Alto', color='White')
swift = Car(model='Swift', color='Black')
alto.showInfo()
swift.showInfo()

    