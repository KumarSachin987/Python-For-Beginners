# try block: The code that might raise an exception is placed inside the try block.
# except block: This block catches and handles the exceptions raised by the try block.
# else block: This block is executed if no exceptions were raised in the try block.
# finally block: This block is executed no matter what, whether an exception was raised or not, and is typically used for cleanup actions.
# Here are examples illustrating the use of each block:

# Example 1: Using else with try and except

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# else:
#     print(f"Result is: {result}")
# In this example:

# The try block attempts to convert the user input to an integer and then divides 10 by that number.
# The except blocks handle ValueError (invalid integer input) and ZeroDivisionError (division by zero).
# The else block executes only if no exceptions were raised, printing the result of the division.
# Example 2: Using finally with try and except

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print(content)
    # print('locals is=',locals())
finally:
    print('print before if statement')
    if 'file' in locals():
        file.close()
        print("File closed.")
        

# In this example:

# The try block attempts to open and read from a file named "example.txt".
# The except block handles the FileNotFoundError if the file does not exist.
# The else block executes if no exception is raised, printing the content of the file.
# The finally block ensures that the file is closed whether or not an exception was raised.
# Example 3: Combining else and finally

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# else:
#     print(f"Result is: {result}")