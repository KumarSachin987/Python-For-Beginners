'''
1. Introduction to Inheritance
Theory:
Inheritance is a feature in object-oriented programming where a class (child class) can inherit attributes and methods from another class (parent class). This promotes code reuse and creates a logical hierarchy among classes.

Key Points:
Parent Class (Superclass): The class whose properties and methods are inherited.
Child Class (Subclass): The class that inherits properties and methods.
The child class can have additional methods and properties or override methods from the parent class.
'''
# Syntax of inheritance
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass


'''
Types of Inheritance
1). Single Inheritance
Single inheritance involves a single parent and a single child class. The child class inherits all the accessible properties and methods of the parent class.
'''
class Animal:
    def speak(self):
        print('Animal makes some sound')

class Dog(Animal):
    def bark(self):
        print('Dog barks')

dogObj = Dog()
dogObj.speak()
dogObj.bark()

'''
2). Multiple Inheritance
Multiple inheritance allows a class to inherit from more than one parent class. This enables the child class to use properties and methods from all parent classes. However, it can lead to complexity, especially when parent classes have methods with the same name.
'''

class Father:
    def walks(self):
        print('Father walks')

class Mother:
    def cooks(self):
        print('Mother cooks')

class Child(Father, Mother):
    def plays(self):
        print('child plays')

childObj = Child()
childObj.walks()
childObj.cooks()
childObj.plays()

'''
3). Multilevel Inheritance
In multilevel inheritance, a child class inherits from another child class, creating a chain of inheritance. It helps establish a clear hierarchy.
'''

class A:
    def printA(self):
        print('Method of A class')

class B(A):
    def printB(self):
        print('Method of B class')

class C(B):
    def printC(self):
        print('Method of C class')

cObj = C()
cObj.printA()
cObj.printB()
cObj.printC()

'''
4). Hierarchical Inheritance
In hierarchical inheritance, multiple child classes inherit from a single parent class. This allows shared behavior to be defined in the parent class.
'''

class Mother:
    def cooks(self):
        print('Mother cooks')

class Child1(Mother):
    def reads(self):
        print('Child1 is reading')

class Child2(Mother):
    def plays(self):
        print('Child2 is playing')

motherObj = Mother()

child1Obj = Child1()
child2Obj = Child2()

child1Obj.cooks()
child1Obj.reads()

child2Obj.cooks()
child2Obj.plays()


'''
5). Hybrid Inheritance
Hybrid inheritance is a combination of multiple and hierarchical inheritance. It often leads to a diamond problem, which is resolved using the Method Resolution Order (MRO) in Python.
'''

class A:
    def printA(self):
        print('Method of A class')

class B(A):
    def printB(self):
        print('Method of B class')

class C(A):
    def printC(self):
        print('Method of C class')

class D(B,C):
    def printD(self):
        print('Method of D class')

dObj = D()
dObj.printA()
dObj.printB()
dObj.printC()
dObj.printD()






