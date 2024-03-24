# creation of strings
name = 'Sachin'
name1 = "Rahul"
name2 = '''Sagar'''
name3 = """Devinder"""
print('type of name is=',type(name))
print('value of name is=',name)
print('type of name1 is=',type(name1))
print('value of name1 is=',name1)
print('type of name2 is=',type(name2))
print('value of name2 is=',name2)
print('type of name3 is=',type(name3))
print('value of name3 is=',name3)

# Concatenation of string
first_name = 'Tejinder '
second_name = 'Singh '
full_name = first_name+second_name
print('value of full name is=',full_name)

# repetetion of string
print('repetetion of string is')
print(full_name * 5)


'Tejinder Singh '
print(full_name[9])
print(full_name[-3])
# String Slicing
print(full_name[2:8])

# Get String length
print('length of full_name is=',len(full_name))


'''
In Python, a string is a sequence of characters enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes. Strings are immutable, meaning their values cannot be changed after creation. Here's an overview of various operations and methods you can perform on strings in Python:

String Creation:
single_quoted_string = 'Hello, World!'
double_quoted_string = "Python Programming"
triple_single_quoted_string = Triple-quoted string
triple_double_quoted_string = """Another triple-quoted string"""

String Concatenation:
str1 = 'Hello'
str2 = 'World'
result = str1 + ' ' + str2  # Concatenation using the + operator

String Repetition:
repeated_str = 'abc' * 3  # Results in 'abcabcabc'

String Indexing:
my_string = 'Python'
first_char = my_string[0]  # Accessing the first character (indexing starts from 0)

String Slicing:
substring = my_string[1:4]  # Extracting a substring from index 1 to 3

String Length:
length = len(my_string)  # Returns the length of the string
'''