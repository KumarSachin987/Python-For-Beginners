# Arithematic Operators
a = 10
b = 3

print('Result of Addition is=',a + b)  # 13
print('Result of Substraction is=',a - b)  # 7
print('Result of Multiplication is=',a * b)  # 30
print('Result of Division is=',a / b)  # 3.3333...
print('Result of Modules operator is=',a % b)  # 1
print('Result of Exponential is=',a ** b) # 1000  10*10*10
print('Result of floor division is=',a // b) # 3


# Comparison Operators

x = 5
y = 10

print('Result of == is=',x == y)  # False
print('Result of != is=',x != y)  # True
print('Result of < is=',x < y)   # True
print('Result of > is=',x > y)   # False
print('Result of <= is=',x <= y)  # True
print('Result of >= is=',x >= y)  # False


# Logical Operators

p = True
q = False

print('Result of AND is=',p and q)  # False
print('Result of OR is=',p or q)   # True
print('Result of NOT is=',not p)    # False


# Assignment Operators

# = (Assignment)
# += (Add and assign)
# -= (Subtract and assign)
# *= (Multiply and assign)
# /= (Divide and assign)
# %= (Modulus and assign)
# **= (Exponentiate and assign)
# //= (Floor divide and assign)

a = 5
b = 3

a += b  # equivalent to a = a + b
print('Result of += is=',a)  # 8

a -= b  # equivalent to a = a - b
print('Result of -= is=',a) 


# Bitwise Operators

x = 5  # 101 in binary
y = 3  # 011 in binary

print(x & y)  # 1 (result of bitwise AND)
print(x | y)  # 7 (result of bitwise OR)
print(x ^ y)  # 6 (result of bitwise XOR)
print(~x)     # -6 (result of bitwise NOT)
print(x << 1)  # 10 (result of left shift by 1)
print(x >> 1)  # 2  (result of right shift by 1)

'''
1). Arithmetic Operators:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus - returns the remainder of the division)
** (Exponentiation)
// (Floor Division - returns the quotient of the division, discarding the remainder)

a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a % b)  # 1
print(a ** b) # 1000
print(a // b) # 3



2). Comparison Operators:

== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)

x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False


3).Logical Operators:

and (Logical AND)  If all the conditions are true then it returns true otherwise false
or (Logical OR)    If any of the conditions are true then it returns true otherwise false
not (Logical NOT)  If condition is true then it returns false and wise versa.

p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False

4).Assignment Operators:

= (Assignment)
+= (Add and assign)
-= (Subtract and assign)
*= (Multiply and assign)
/= (Divide and assign)
%= (Modulus and assign)
**= (Exponentiate and assign)
//= (Floor divide and assign)

a = 5
b = 3

a += b  # equivalent to a = a + b
print(a)  # 8

5). Bitwise Operators:

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
~ (Bitwise NOT)
<< (Left shift)
>> (Right shift)

x = 5  # 101 in binary
y = 3  # 011 in binary

print(x & y)  # 1 (result of bitwise AND)
print(x | y)  # 7 (result of bitwise OR)
print(x ^ y)  # 6 (result of bitwise XOR)
print(~x)     # -6 (result of bitwise NOT)
print(x << 1)  # 10 (result of left shift by 1)
print(x >> 1)  # 2  (result of right shift by 1)

'''