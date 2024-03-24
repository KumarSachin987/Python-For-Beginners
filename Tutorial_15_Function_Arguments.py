# Default Arguments
def greetings(name='Sachin'):
    print('Good Morning ',name)

greetings()


# Positional Arguments
def add_numbers(x, y):
    print('value of x is=',x)
    print('value of y is=',y)
    return x + y

res = add_numbers(10,20)
print('Result is=',res)


# Keyword Arguments
def add_numbers(x, y):
    print('value of x is=',x)
    print('value of y is=',y)
    return x + y

res = add_numbers(y=10,x=20)
print('Result is=',res)


# variable lenght arguments
def addition(*args):
    result = 0
    for data in args:
        result = result + data
    return result

res = addition(1,2,3,4,5,6)
print(res)
res1 = addition(1,2,3,4)
print(res1)
res2 = addition(1,2,3,4,5)
print(res2)


def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(name="sachin", age="29", Salary="60000", company="abc", city="chandigarh" )

'''
In Python, function arguments are the values that you pass to a function when calling it. Python supports several types of function arguments, including positional arguments, keyword arguments, default arguments, and variable-length arguments. Let's explore each of them with examples:


Positional Arguments:
These are the most common type of arguments, and they are matched based on their position in the function call.
The order in which you pass the values matters.
Example:
def add_numbers(x, y):
    return x + y

result = add_numbers(3, 5)
print(result)  # Output: 8


Keyword Arguments:
You can also pass arguments to a function by explicitly mentioning the parameter names.
This allows you to pass the values in any order, as long as you specify the parameter names.
Example:
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet(age=25, name="Alice")
# Output: Hello Alice, you are 25 years old!


Default Arguments:
You can provide default values for function parameters. If the caller doesn't provide a value, the default is used.
Example:
def power(x, exponent=2):
    return x ** exponent

result1 = power(3)      # Uses default exponent (2)
result2 = power(3, 3)   # Uses provided exponent (3)

print(result1)  # Output: 9
print(result2)  # Output: 27


Variable-Length Arguments:
Python allows you to define functions that can accept a variable number of arguments.
There are two types: *args for positional arguments and **kwargs for keyword arguments.
Example:
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="John", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'John', 'age': 30}
In this example, *args collects any number of positional arguments into a tuple, and **kwargs collects any number of keyword arguments into a dictionary.

These are the main types of function arguments in Python. Depending on the situation, you can use a combination of these argument types to make your functions more flexible and versatile.
'''