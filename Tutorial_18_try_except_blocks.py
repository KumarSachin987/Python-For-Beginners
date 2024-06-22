# a = 10
# b = 0
# res = a / b
# print(res)
# print('Hello')
# In Python, the try and except blocks are used for error handling. They allow you to gracefully handle exceptions (errors) that may occur during the execution of your code.

# Syntax:

# try:
#     # Code block where exceptions may occur
#     # Place the code you want to try here
# except ExceptionType:
#     # Code block to handle the exception
#     # Place the code to handle the exception here

# Examples:
# Example 1: Handling Division by Zero Error

try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
print('print after ZeroDivisionError exception')

# Example 2: Handling File Not Found Error
# file = open('nonexistent_file.txt', 'r')
try:
    file = open('nonexistent_file.txt', 'r')
except FileNotFoundError:
    print("Error: File not found.")

print('Print statement after FileNotFoundError')

# Example 3: Handling Multiple Exceptions

try:
    result = 10 / 0  # Division by zero
    file = open('nonexistent_file.txt', 'r')  # File not found
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except FileNotFoundError:
    print("Error: File not found.")

# Example 4: Using the except Block without Specifying an Exception Type

try:
    result = 10 / 0  # Division by zero
except:
    print("An error occurred.")

