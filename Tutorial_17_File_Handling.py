# it will create a new file if it dosn't exist
# file = open('example.txt','w')
# it will write data in file
# file.write('Sachin\nKumar')

# It will read first line from file
# file = open("example.txt", "r")
# line = file.readline()
# print('The first line of the file is=',line)

# reading all lines 
# lines = file.readlines()
# print(lines)

# To read entire file
# content = file.read()
# print(content)


# To Append data in file
# file = open('example.txt', 'a')
# file.write('\nRohit Sharma\nVirat Kohli\nRonaldo\nMessi')

# file = open('example.txt','w')
# file.write('Ronaldo')
# file.close()

# use of with statement
with open('example.txt','a') as f:
    f.write('\nMessi\nNaymar\nSaka')
'''
File handling in Python allows you to work with files on your computer. You can read from files, write to files, and perform various operations like appending to files, closing files, and more. Here's a comprehensive guide to file handling in Python with examples:

1. Opening a File:
You can open a file using the open() function. It takes two arguments: the file path and the mode (read, write, append, etc.).


# Open a file in read mode
file = open("example.txt", "r")


2. Reading from a File:
You can read the contents of a file using various methods like read(), readline(), or readlines().

# Reading the entire file
content = file.read()

# Reading one line at a time
line = file.readline()

# Reading all lines into a list
lines = file.readlines()


3. Writing to a File:
You can write to a file using the write() method.

# Open a file in write mode
file = open("example.txt", "w")
file.write("Hello, World!\n")


4. Appending to a File:
You can append content to an existing file using the a mode in open().

python
Copy code
# Open a file in append mode
file = open("example.txt", "a")

# Appending to the file
file.write("This is a new line.")


5. Closing a File:
Always remember to close the file after performing operations on it.
file.close()


6. Using with Statement:
You can use the with statement to automatically close the file after usage.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
'''