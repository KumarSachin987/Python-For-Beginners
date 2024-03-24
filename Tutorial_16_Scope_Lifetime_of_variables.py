# Example of Local scope

def firstName():
    name = 'Sachin'
    print(name)

firstName()
# print(name)

# Example of Enclosing Scope
def parent():
    varParent = 'Variable of parent function'

    def child():
        print(varParent)
    
    child()

parent()

# Example of Global Scope

globalVar = 'This is a global variable'
print('This valus is printing from outside the function',globalVar)

def testGlobalVariable():
    print('This variable is printing from inside the testGlobalVariable function')
    global globalVar
    print(globalVar)
   
    globalVar = 'this valus is updated by new value'
    print(globalVar)

testGlobalVariable()
'''
1. What is Scope?

Define scope as the region of code where a variable is visible.
Four main scopes in Python: Local, Enclosing, Global, and Built-in.

2. Local Scope:

Variables defined within a function have local scope.
How variables defined inside a function are inaccessible outside of it.

def my_function():
    x = 10
    print(x)

my_function()
# print(x)  # This will raise a NameError because x is not defined outside the function.

3. Enclosing Scope (Closure):

Concept of enclosing scope, which occurs in nested functions.
How inner functions can access variables from outer functions.

def outer_function():
    y = 20
    
    def inner_function():
        print(y)
    
    inner_function()

outer_function()  # Output: 20

4. Global Scope:

Global scope, where variables are defined outside of any function.
Explain that global variables can be accessed from anywhere in the code.

global_var = 30

def my_function():
    print(global_var)

my_function()  # Output: 30

5. Modifying Global Variables:

How to modify global variables from within a function using the global keyword.

global_var = 30

def modify_global():
    global global_var
    global_var = 40

modify_global()
print(global_var)  # Output: 40

6. Built-in Scope:

The built-in scope, which contains Python's built-in functions and modules.
Examples of using built-in functions like print() and len().
python
Copy code
print(len([1, 2, 3]))  # Output: 3
'''