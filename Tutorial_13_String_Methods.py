# Capitalize Method
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello world


# casefold method
text = "HELLO WORLD"
casefolded_text = text.casefold()
print(casefolded_text)  # Output: hello world

#center method
text = "hello"
centered_text = text.center(10, '*')
print(centered_text)  # Output: **hello***

# COunt method
text = "hello world"
count_occurrences = text.count('o')
print(count_occurrences)  # Output: 3


# endsWith Method
text = "hello world"
ends_with_world = text.endswith("a")
print(ends_with_world)  # Output: False

# find Method
text = "hello world"
index_of_world = text.find("g")
print(index_of_world)  # Output: -1


# Format method
name = "Alice"
age = 30
formatted_text = "My name is {} and I am {} years old".format(name, age)
print(formatted_text)

# isalnum method
text = "abc123"
is_alphanumeric = text.isalnum()
print(is_alphanumeric)  # Output: True

# isalpha
text = "abcWETYU"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True

#isdigit
text = "1239597696796776whar"
is_digit = text.isdigit()
print(is_digit)  # Output: True
'''
capitalize():
Converts the first character to uppercase.
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello world


casefold():
Returns a casefolded string for case-insensitive comparisons.
text = "Hello World"
casefolded_text = text.casefold()
print(casefolded_text)  # Output: hello world


center(width[, fillchar]):
Returns a centered string.
text = "hello"
centered_text = text.center(10, '*')
print(centered_text)  # Output: **hello***


count(sub[, start[, end]]):
Returns the number of occurrences of a substring in the given range.
text = "hello world"
count_occurrences = text.count('l')
print(count_occurrences)  # Output: 3


endswith(suffix[, start[, end]]):
Returns True if the string ends with the specified suffix.
text = "hello world"
ends_with_world = text.endswith("world")
print(ends_with_world)  # Output: True


find(sub[, start[, end]]):
Returns the lowest index of the substring if found, -1 otherwise.
text = "hello world"
index_of_world = text.find("world")
print(index_of_world)  # Output: 6


**format(*args, kwargs):
Formats a string using positional and keyword arguments.
name = "Alice"
age = 30
formatted_text = "My name is {} and I am {} years old".format(name, age)
print(formatted_text)


isalnum():
Returns True if all characters in the string are alphanumeric.
text = "abc123"
is_alphanumeric = text.isalnum()
print(is_alphanumeric)  # Output: True


isalpha():
Returns True if all characters in the string are alphabetic.
text = "abc"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True


isdigit():
Returns True if all characters in the string are digits.
text = "123"
is_digit = text.isdigit()
print(is_digit)  # Output: True
'''