# fruits = {'apple', 'banana', 'orange'}
# print(type(fruits))
# print(fruits)

# Adding elements in set
# fruits.add('grape')
# print(fruits)

# Removing element from set
# fruits.remove('banana')
# print(fruits)

# discard function
# fruits.discard('orange')
# print(fruits)
# fruits.discard('Lichi')
# print(fruits)

# pop function
# removed_element = fruits.pop()
# print(removed_element)
# print(fruits)

#Union
# all_fruits = fruits.union({'kiwi', 'grape', 'pineapple'})
# print(all_fruits)

#Intersection
# common_fruits = fruits.intersection({'banana', 'orange', 'kiwi'})
# print(common_fruits)

# difference
# fruits = {'apple', 'banana', 'orange'}
# unique_fruits = fruits.difference({'banana', 'orange', 'kiwi'})
# print(unique_fruits)

#symmetric_difference
# fruits = {'apple', 'banana', 'orange'}
# exclusive_fruits = fruits.symmetric_difference({'banana', 'kiwi', 'mango'})
# print(exclusive_fruits)


# fruits.clear()
# print(fruits)

# fruits_copy = fruits.copy()

# print(fruits_copy)

# is_subset = fruits.issubset({'banana', 'orange', 'apple', 'kiwi'})
# print(is_subset)
fruits = {'apple', 'banana', 'orange'}

# is_superset = fruits.issuperset({'banana','orange'})
# print(is_superset)

no_common_elements = fruits.isdisjoint({'mango', 'pineapple'})
print(no_common_elements)

# Set comprehension
squares = {x*x for x in range(1, 6)}
print(squares)

# Using set method to change other datatype to set
numbers_set = set([1, 2, 3, 4, 5])
print(type(numbers_set))
print(numbers_set)


# 8. Length of a Set:
# len(): Returns the number of elements in the set.
num_elements = len(fruits)
print(num_elements)


#frozenset
normal_set = {1, 2, 3, 4, 5}
normal_set.add(10)
print(normal_set)
frozen_set = frozenset(normal_set)
frozen_set.add(100)
print(frozen_set)


'''
1. Introduction to Sets:
A set is an unordered collection of unique elements.


2. Creating a Set:
Syntax: my_set = {element1, element2, ...}
Example:
fruits = {'apple', 'banana', 'orange'}


3. Adding and Removing Elements:
add(element): Adds an element to the set.
fruits.add('grape')


remove(element): Removes an element from the set. Raises a KeyError if the element is not present.
fruits.remove('banana')


discard(element): Removes an element from the set if it is present, without raising an error if the element is not found.
fruits.discard('kiwi')


pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
removed_element = fruits.pop()


4. Set Operations:
union(other_set): Returns a new set with elements from both sets.
all_fruits = fruits.union({'kiwi', 'grape', 'pineapple'})

intersection(other_set): Returns a new set with elements common to both sets.
common_fruits = fruits.intersection({'banana', 'orange', 'kiwi'})

difference(other_set): Returns a new set with elements in the set but not in the other set.
unique_fruits = fruits.difference({'banana', 'orange', 'kiwi'})

symmetric_difference(other_set): Returns a new set with elements in either set, but not both.
exclusive_fruits = fruits.symmetric_difference({'banana', 'kiwi', 'mango'})


5. Set Methods:
clear(): Removes all elements from the set.
fruits.clear()

copy(): Returns a shallow copy of the set.
fruits_copy = fruits.copy()


discard(element): Removes an element from the set if it is present.
fruits.discard('apple')


issubset(other_set): Returns True if the set is a subset of the other set.
is_subset = fruits.issubset({'banana', 'orange', 'apple', 'kiwi'})


issuperset(other_set): Returns True if the set is a superset of the other set.
is_superset = fruits.issuperset({'banana', 'kiwi'})


isdisjoint(other_set): Returns True if the set has no elements in common with the other set.
no_common_elements = fruits.isdisjoint({'mango', 'pineapple'})


6. Set Comprehensions:
Creating sets using comprehensions.
squares = {x*x for x in range(1, 6)}


7. Conversion to Set:
set(iterable): Converts an iterable (e.g., list, tuple) to a set.
numbers_set = set([1, 2, 3, 4, 5])


8. Length of a Set:
len(): Returns the number of elements in the set.
num_elements = len(fruits)


9. Frozen Sets:
Immutable sets created using the frozenset() constructor.
# Creating a regular set
normal_set = {1, 2, 3, 4, 5}

# Creating a frozen set
frozen_set = frozenset(normal_set)

# Displaying the sets
print("Normal Set:", normal_set)
print("Frozen Set:", frozen_set)

# Attempting to modify the frozen set (will result in an error)
try:
    frozen_set.add(6)
except AttributeError as e:
    print(f"Error: {e}")

# Attempting to modify the normal set
normal_set.add(6)

# Displaying the sets after attempted modifications
print("Modified Normal Set:", normal_set)
print("Frozen Set (unchanged):", frozen_set)

'''