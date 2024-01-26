# Creaton of tuple
my_tuple = (1, 2, 3, 'a', 'b')
print(type(my_tuple))

# Accessing elements of tuple
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-2])

# Immutable nature
# my_tuple[0] = 10

# getting length of tuple
print('length of the tuple is=',len(my_tuple))

# Concatenation of tuple
print('concatenation of tuple is=',my_tuple + (100,200,300))

# Repetition of tuples
print('Repetition of tuple=',my_tuple * 3)

# Membership test
print(100 in my_tuple)
print(1 in my_tuple)
print(100 not in my_tuple)
print(1 not in my_tuple)

# Tuple packing and unpacking
packed_tuple = 1, 2, 3 # packing
print(packed_tuple)

a, b, c = packed_tuple # unpacking
print('a is=',a)
print('b is=',b)
print('c is=',c)

# Tuple functions

print('length of tuple is=',len(my_tuple)) #5
lst = [1,2,3,4,5,6,7,8]
print(tuple(lst))
print('maximum element is=',max(lst)) #8
print('Minimum elements is=',min(lst)) #1
print('Sum of all the elements is=',sum(lst))

print('Count of 1 is=',my_tuple.count(1))
print('Index of 3 is=',my_tuple.index(3))



'''
Certainly! In Python, a tuple is an ordered, immutable collection of elements. This means that once a tuple is created, you cannot modify its contents - you cannot add, remove, or change elements. Tuples are often used to store related pieces of data, and they are defined using parentheses ().

Here are some key aspects of tuples in Python:

Creation of Tuples:
Tuples can be created using parentheses. Elements are separated by commas.
Example: my_tuple = (1, 2, 3, 'a', 'b')


Accessing Elements:
Elements in a tuple are accessed using indexing. Indexing starts from 0.
Example: element = my_tuple[0] # Access the first element


Immutable Nature:
Tuples are immutable, meaning their elements cannot be changed or modified after creation.
Example: my_tuple[0] = 10 # This will raise an error


Length of Tuple:
The len() function returns the number of elements in a tuple.
Example: length = len(my_tuple)


Tuple Concatenation:
Tuples can be concatenated using the + operator.
Example: new_tuple = my_tuple + (4, 5)


Repetition:
Tuples can be repeated using the * operator.
Example: repeated_tuple = my_tuple * 3


Membership Test:
You can use the in operator to check if an element is present in a tuple.
Example: check = 2 in my_tuple


Tuple Packing and Unpacking:
Tuple packing is the process of putting values into a tuple without using parentheses.
Tuple unpacking is the reverse, extracting values from a tuple into variables.
packed_tuple = 1, 2, 3
a, b, c = packed_tuple


Built-in Functions:
Some of the built-in functions for tuples include:
len(): Returns the number of elements in the tuple.
max(): Returns the maximum value in the tuple.
min(): Returns the minimum value in the tuple.
sum(): Returns the sum of all elements in the tuple.
tuple(): Converts a sequence (list, string, etc.) into a tuple.
count(): Returns the number of occurrences of a specified value.
index(): Returns the index of the first occurrence of a specified value.

# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b')

# Accessing elements
element = my_tuple[0]

# Length of tuple
length = len(my_tuple)

# Tuple concatenation
new_tuple = my_tuple + (4, 5)

# Repetition
repeated_tuple = my_tuple * 3

# Membership test
check = 2 in my_tuple

# Tuple packing and unpacking
packed_tuple = 1, 2, 3
a, b, c = packed_tuple

# Built-in functions
max_value = max(my_tuple)
min_value = min(my_tuple)
sum_values = sum(my_tuple)
occurrences = my_tuple.count('a')
index_of_a = my_tuple.index('a')

'''