# break statement in for loop
for i in range(1,11):
    print(i)
    if i == 5:
        break

print("Print statement after the for loop")

# break statement in while loop
count = 1
while count < 11:
    print(count)
    count +=1
    if count == 5:
        break

print("Print statement after the for loop")

# continue in for loop
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# continue in while loop
i = 0
while i < 11:
    i += 1
    if i == 5:
        continue
    print(i)

'''
In Python, break and continue are control flow statements that are used in loops to alter the normal flow of execution.

1). break statement:

The break statement is used to exit a loop prematurely, before its normal termination.
When the break statement is encountered inside a loop, the loop is immediately terminated, and the program continues with the next statement after the loop.

2). continue statement:

The continue statement is used to skip the rest of the code inside a loop for the current iteration and proceed to the next iteration of the loop.
'''