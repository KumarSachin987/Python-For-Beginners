# creating empty list
empty_lst = []
print(type(empty_lst))
print(empty_lst)



# creating list with different types of elements
my_list = [1, 2, 3,'e','t','g','b','sachin','aman',]
print('Elements of my_list are=',my_list)

# Accessing list elements

print(my_list[3])
print(my_list[4])
print(my_list[-1])
print(my_list[-2])
print(my_list[0:5])
print(my_list[2:-1])


# creating list with list() method
new_list_1 = list(("abc","sachin","Aman"))  
print('type of the new_list is=',type(new_list_1))

new_list = list("abc")  
print('Elements of the new_list are=',new_list)


# List operations

# Combining list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
    
combined_list = list1 + list2
print(combined_list)

# Repeating list
repeated_list = [1,2,3,4,54,5,6,] * 4
print(repeated_list)

# Length of a List:
length = len(repeated_list)
print(length)

# membership functions
print(54 in repeated_list)

print(100 not in repeated_list)

# Modifying list
my_list = [1, 2, 3,'e','t','g','b','sachin','aman',]
my_list[0] = 100
print(my_list)

# List comprehension
squares = [x**2 for x in range(10)]   
print(squares)

even_numbers = [x for x in range(101) if x%2==0]   
print(even_numbers)
# for x in range(5):
#     print(x)

# nested list
nested_list = [[1, 2, 3], 
               [4, 5, 6]]
print(nested_list)
print(nested_list[0][0])  #1
print(nested_list[1][0])  #4

# list functions

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


my_list = [1, 2, 3]
my_list_2 = [4, 5, 6]
my_list.extend(my_list_2)
print(my_list)


my_list = [1, 2, 3]
my_list.insert(3, 4)
print(my_list)


my_list = [1, 2, 3, 2]
my_list.remove(3)
print(my_list)


my_list = [1, 2, 3]
popped_value = my_list.pop()
print(my_list)


my_list = [1, 2, 3]
my_list.clear()
print(my_list)


my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)


# by giving the starting index
my_list_1 = [1, 2, 3, 2]
index = my_list_1.index(2,2)
print(index)


my_list = [1, 2, 3, 2,2,2,2,2,2,2]
count = my_list.count(2)
print(count)


my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort(reverse=True)
print(my_list)


my_list_3 = [3, 1, 4, 1, 5, 9, 2]
my_list_3.sort()
print(my_list_3)


my_list = [1, 2, 3]
my_list.reverse()
print(my_list)


my_list = [1, 2, 3]
new_list = my_list.copy()
my_list.append(10)
print(my_list)
print(new_list)

'''
1. Introduction to Lists:

Definition: A list is a mutable, ordered sequence of elements in Python. Mutable means you can change the elements after the list is created.

2. Creating Lists:
    
    Different Ways:
    # Using square brackets
    my_list = [1, 2, 3]

    # Using the list() constructor
    another_list = list("abc")

    Lists with Various Data Types:
    mixed_list = [1, "hello", 3.14, True]

    Empty Lists:
    empty_list = []

3. Accessing Elements:

    Indexing:
    my_list = [10, 20, 30, 40, 50]
    print(my_list[0])  # Output: 10
    print(my_list[-1]) # Output: 50

    Slicing:
    print(my_list[1:4])  # Output: [20, 30, 40]

4. List Operations:

    Concatenation:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    combined_list = list1 + list2

    Repetition:
    repeated_list = [1] * 3  # Output: [1, 1, 1]

    Length of a List:
    length = len(combined_list)

    Membership Check:
    print(2 in combined_list)   # Output: True
    print(7 not in combined_list)  # Output: True

5. Modifying Lists:

    Changing Elements:
    my_list[0] = 100

    Adding Elements:
    my_list.append(60)
    my_list.insert(2, 25)

    Removing Elements:
    my_list.remove(30)
    popped_value = my_list.pop(1)
    del my_list[0]

6. List Comprehensions:

    Basic Syntax:
    squares = [x**2 for x in range(5)]

7. Nested Lists:

    Creating and Accessing:
    nested_list = [[1, 2, 3], [4, 5, 6]]
    print(nested_list[1][0])  # Output: 4

8. List Methods:

    1. append(x):
    Adds an element x to the end of the list.
    my_list = [1, 2, 3]
    my_list.append(4)
    # Result: [1, 2, 3, 4]

    2. extend(iterable):
    Extends the list by appending elements from the iterable.
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    # Result: [1, 2, 3, 4, 5, 6]

    3. insert(i, x):
    Inserts element x at the specified index i.
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    # Result: [1, 4, 2, 3]

    4. remove(x):
    Removes the first occurrence of element x from the list.
    my_list = [1, 2, 3, 2]
    my_list.remove(2)
    # Result: [1, 3, 2]

    5. pop([i]):
    Removes and returns the element at index i. If i is not provided, it removes and returns the last element.
    my_list = [1, 2, 3]
    popped_value = my_list.pop(1)
    # Result: popped_value = 2, my_list = [1, 3]

    6. clear():
    Removes all elements from the list.
    my_list = [1, 2, 3]
    my_list.clear()
    # Result: []

    7. index(x, start, end):
    Returns the index of the first occurrence of element x in the list. Optional start and end parameters can be used to specify the search range.
    my_list = [1, 2, 3, 2]
    index = my_list.index(2)
    # Result: index = 1

    8. count(x):
    Returns the number of occurrences of element x in the list.
    my_list = [1, 2, 3, 2]
    count = my_list.count(2)
    # Result: count = 2

    9. sort(key=None, reverse=False):
    Sorts the elements of the list in ascending order. The key and reverse parameters are optional.
    my_list = [3, 1, 4, 1, 5, 9, 2]
    my_list.sort()
    # Result: [1, 1, 2, 3, 4, 5, 9]

    10. reverse():
    Reverses the elements of the list in-place.
    my_list = [1, 2, 3]
    my_list.reverse()
    # Result: [3, 2, 1]

    11. copy():
    Returns a shallow copy of the list.
    my_list = [1, 2, 3]
    new_list = my_list.copy()
    # Result: new_list = [1, 2, 3]
'''