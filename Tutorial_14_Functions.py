# num1 = 10
# num2 = 20
# result = num1 + num2
# print(result)


# num3 = 10
# num4 = 40
# result = num3 + num4
# print(result)


# num5 = 30
# num6 = 40
# result = num5 + num6
# print(result)


# function definition without parameters
def func1():
    print('Hello word')


func1()



# Function definition with parameters
def addition(num1, num2):
    result = num1 + num2
    print('Result is from function')
    return result

# function calling
res =  addition(10,30) #40
print('values of res is=',res)

res =  addition(30,40) #70
print('values of res is=',res)

res =  addition(50,20) #70
print('values of res is=',res)

# Function definition with default parameters
def addition(num1, num2=10):
    result = num1 + num2
    print('Result is from function')
    return result

# function calling
res =  addition(10,30) #30
print('values of res is=',res)

res =  addition(30,40) #50
print('values of res is=',res)

res =  addition(50) #70
print('values of res is=',res)
# addition(10,40)
# addition(30,40)

# Scope of variables
dummy = 'Hello'
def exp():
    dummy = 'word'   

exp()
print(dummy)

'''
In Python, a function is a block of reusable code designed to perform a specific task. Functions provide a way to organize code into modular and manageable pieces. They follow a specific syntax for definition and execution.


Function Definition:
To define a function in Python, you use the def keyword followed by the function name and a pair of parentheses. Inside the parentheses, you can specify parameters (inputs) that the function takes. The function body is then indented and contains the actual code to be executed.


def greet(name):
    print(f"Hello, {name}!")


In this example:
greet is the function name.
(name) is a parameter that the function takes.
Function Call:
To use a function, you "call" it by using its name followed by parentheses, and you may pass values (arguments) for the parameters if needed.

greet("John")
# Output: Hello, John!

Return Statement:
Functions can return a value using the return statement. This allows the function to produce a result that can be used elsewhere in the code.

def add_numbers(a, b):
    result = a + b
    return result


You can then capture the result when calling the function:
sum_result = add_numbers(3, 5)
print(sum_result)
# Output: 8


Parameters and Arguments:
Parameters are variables listed in a function's definition, and arguments are the values passed into the function when it is called. In the examples above, name, a, and b are parameters, while "John", 3, and 5 are arguments.

Default Values:
You can assign default values to parameters, making them optional when calling the function.

def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message

When calling this function, you can provide a value for greeting or use the default:
print(greet("John"))
# Output: Hello, John!

print(greet("Alice", "Hi"))
# Output: Hi, Alice!

Scope:
Variables defined within a function have local scope, meaning they are only accessible within that function. Variables defined outside functions have global scope, and they can be accessed from anywhere in the code.

Benefits of Functions:
Modularity: Functions help break down complex tasks into smaller, more manageable parts.
Reusability: Once a function is defined, it can be reused multiple times in different parts of the code.
Readability: Functions make the code more readable and organized.
In summary, functions in Python provide a way to structure and organize code, making it more modular, readable, and reusable. They play a crucial role in building scalable and maintainable programs.
'''