# Steps to Create and Raise Custom Exceptions
# Define a Custom Exception Class: Create a new class that inherits from Exception.
# Raise the Custom Exception: Use the raise statement to raise an instance of the custom exception.

# Let's create a custom exception called InvalidAgeError and use it to handle a specific error condition.

# Step 1: Define the Custom Exception Class


class InvalidAgeError(Exception):
    """Exception raised for invalid age input."""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Step 2: Raise the Custom Exception

def set_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"Age has been set to {age}")

try:
    age = int(input("Enter your age: "))
    set_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")


# Explanation
# Custom Exception Class:

# The InvalidAgeError class inherits from Exception.
# It includes an __init__ method to initialize the age and message attributes.
# The __str__ method is overridden to provide a custom string representation of the exception, which is useful for printing the error message.
# Raising the Custom Exception:

# The set_age function checks if the provided age is within the valid range (0 to 120).
# If the age is not valid, it raises an InvalidAgeError with the invalid age as an argument.
# The try block attempts to get the age from user input and calls set_age.
# The except block catches InvalidAgeError and prints the custom error message.
# An additional except block catches ValueError to handle cases where the input is not a valid integer.