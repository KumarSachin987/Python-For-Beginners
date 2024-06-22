'''
What is a Constructor?
"A constructor is a special type of method in Python that is automatically called when an object of a class is created. It is used to initialize the attributes of the class."

Syntax of Constructors
"In Python, the constructor method is always named __init__. Let's see the syntax."
"The __init__ method is defined with two underscores before and after the word init. This method can take parameters, which are used to initialize the object's attributes."
'''
# Example of non parameterized constructor
class Person:
    def __init__(self):
        self.name = 'Sachin'
        self.age = 29
        self.height = '5.6 ft'
        self.weight = 62

    def showProperties(self):
        print('Name is=', self.name)
        print('age is=', self.age)
        print('height is=', self.height)
        print('weight is=', self.weight)


    def walk(self):
        print('Person is walking')

    def talk(self):
        print('Person is talking')

p1 = Person()
p1.showProperties()
p1.talk()
p1.walk()


# Parameterized constructor
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def showProperties(self):
        print('Name is=', self.name)
        print('age is=', self.age)
        print('height is=', self.height)
        print('weight is=', self.weight)


    def walk(self):
        print('Person is walking')

    def talk(self):
        print('Person is talking')

p1 = Person('Pankaj', 30, '6.0 ft', 80)
p1.showProperties()
p1.talk()
p1.walk()


# Constructor with default values
class Person:
    def __init__(self, name, age=50, height='5.5 ft', weight='80 kg'):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def showProperties(self):
        print('Name is=', self.name)
        print('age is=', self.age)
        print('height is=', self.height)
        print('weight is=', self.weight)


    def walk(self):
        print('Person is walking')

    def talk(self):
        print('Person is talking')

p1 = Person('Pankaj', 30, '6.0 ft', '90 kg')
p1.showProperties()
p1.talk()
p1.walk()


# Default constructor
class Person:
    name = 'Sachin'
    age = 29
    height = '5.6 ft'
    weight = 62

    def showProperties(self):
        print('Name is=', self.name)
        print('age is=', self.age)
        print('height is=', self.height)
        print('weight is=', self.weight)


    def walk(self):
        print('Person is walking')

    def talk(self):
        print('Person is talking')

p1 = Person()
p1.showProperties()
p1.talk()
p1.walk()