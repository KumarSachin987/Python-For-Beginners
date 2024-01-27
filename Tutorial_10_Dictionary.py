# Creation of dictionary
employee = {'name':'Sachin','empId':'9795746','department':'IT'}
print('Type of employee is=',type(employee))
print(employee)

# Accessing values of dictionary
print(employee['name']) #sachin

print(employee['department']) #IT

print(employee['empId']) #9795746


# Changing existing values
employee['department'] = 'Development'
print(employee)

# Adding new valu in dictionary
employee['Salary'] = 50000
print(employee)

# Deleting an element from dictionary
del employee['department']
print(employee)

# Iterating through dictionary
# print(employee.keys())
# using keys
for key in employee.keys():
    print('key=',key, 'value is=',employee[key])

for key in employee.keys():
    print('key=',key)
# using values
for val in employee.values():
    print('value is=',val)

# using items
for item in employee.items():
    print('item is=',item)


# Nested Dictionary
school = {
    'class1': {'teacher': 'Alice', 'students': 20},
    'class2': {'teacher': 'Bob', 'students': 18}
}

print(school['class1']) # {'teacher': 'Alice', 'students': 20}
print(school['class2']) # {'teacher': 'Bob', 'students': 18}
print(school['class2']['students']) # 18
print(school['class1']['teacher']) # Alice

#Dictionary Comprehensions:
squares = {x: x*x for x in range(1, 6)} #{1:1, 2:4, 3:9,4:16,5:25}
print(squares)

# Membership operators
print('department' in employee) # false
print('name' in employee) # true
print('name' not in employee) # false
print('department' not in employee) # true

# Functions in dictionary
print('Dictionary before clear=',school)
school.clear()
print('Dictionary after clear=',school)

new_emp = employee.copy()
print('copy of employee dictionary=',new_emp)

keys = ['name', 'age', 'city']
default_values = 0
new_dict = dict.fromkeys(keys, default_values)
print(new_dict)

name = employee.get('name', 0)
print(name)
# print(employee['ddfjkhghgkh'])
name = employee.get('bddgjgjkghh', 0)
print(name)

print(employee.items())

print(employee.keys())

print(employee.values())

# value = employee.pop('kfkjhgkhfgkh', 0)
# print(value)
# print(employee)
# value = employee.pop('Salary', 0)
# print(value)
# print(employee)


# key, value = employee.popitem()
# print(key, value)
# print(employee)

age = employee.setdefault('age', 30)
print(age)
print(employee)

sal = employee.setdefault('Salary', 30)
print(sal)
print(employee)

other_dict = {'city': 'New York', 'gender': 'Male'}
employee.update(other_dict)
print('After appending other_dict=',employee)

key, value = employee.popitem()
print(key, value)
print('after popitem=',employee)
'''
1. Introduction to Dictionaries:
Dictionaries are mutable, unordered collections of key-value pairs.


2. Creating a Dictionary:
Syntax: my_dict = {'key1': 'value1', 'key2': 'value2', ...}
Example:
student = {'name': 'John', 'age': 25, 'grade': 'A'}


3. Accessing Values:
Access values using keys.
Example:
print(student['name'])  # Output: John


4. Modifying Values:
Change, add, or remove key-value pairs.
Example:
student['age'] = 26
student['city'] = 'New York'
del student['grade']


5. Iterating through a Dictionary:
Using for loop with keys(), values(), or items().
Example:
for key in student.keys():
    print(key, student[key])


6.Nested Dictionaries:
Dictionaries within dictionaries.
Example:
school = {
    'class1': {'teacher': 'Alice', 'students': 20},
    'class2': {'teacher': 'Bob', 'students': 18}
}


7.Dictionary Comprehensions:
Create dictionaries in a single line.
Example:
squares = {x: x*x for x in range(1, 6)}


8.Membership Operators:
Checks an element is present in dictionary or not
Example:
print('age' in student)
print('age' not in student)


9. Dictionary Methods:
1. clear()
Removes all items from the dictionary.
my_dict.clear()

2. copy()
Returns a shallow copy of the dictionary.
new_dict = my_dict.copy()

3. fromkeys(seq[, value])
Returns a new dictionary with keys from seq and values set to value.
keys = ['name', 'age', 'city']
default_values = 0
new_dict = dict.fromkeys(keys, default_values)

4. get(key[, default])
Returns the value for the given key. If the key is not present, returns the default value or None.
age = my_dict.get('age', 0)

5. items()
Returns a view of the dictionary's key-value pairs as tuples.
key_value_pairs = my_dict.items()

6. keys()
Returns a view of the dictionary's keys.
keys = my_dict.keys()

7. values()
Returns a view of the dictionary's values.
values = my_dict.values()

8. pop(key[, default])
Removes and returns the value for the given key. If the key is not present and a default value is not provided, a KeyError is raised.
value = my_dict.pop('age', 0)

9. popitem()
Removes and returns an arbitrary key-value pair from the dictionary.
key, value = my_dict.popitem()

10. setdefault(key[, default])
Returns the value for the given key. If the key is not present, sets the key to the default value and returns the default value.
age = my_dict.setdefault('age', 0)

11. update([other])
Updates the dictionary with key-value pairs from another dictionary or iterable.
other_dict = {'city': 'New York', 'gender': 'Male'}
my_dict.update(other_dict)

12. popitem()
Removes and returns the last inserted key-value pair from the dictionary.
key, value = my_dict.popitem()

13. contains(key)
Returns True if the dictionary contains the specified key; otherwise, False.
contains_key = 'age' in my_dict

14. clear()
Removes all items from the dictionary.
my_dict.clear()

'''