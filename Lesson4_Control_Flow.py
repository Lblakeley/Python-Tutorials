## Python Tutorials  
### Lesson 4: Control Flow in Python


##Control flow is a key concept in programming that allows you to make decisions in your code, repeat actions, and handle different 
##conditions. In Python, control flow is achieved through if statements, loops, and various flow-control keywords.

# 1. If Statements

age = 65
if age >= 65:
    print("\nYou are eligible for the senior discount.")
else:
    print("\nYou are not eligible for the senior discount")

# 2. Elif Statements

age = 10
if age >= 65:
    print("\nYou are eligible for the senior discount.")
elif age >= 13:
    print("\nYou are not eligible for an age-based discount.")
else:
    print("\nYou are eligible for the 'kid's eat free' discount.")

# 3. Boolean Expressions

is_cold = True
has_coat = True
if is_cold and not has_coat:
    print("\nIt's cold and I need a coat!")
elif not is_cold or has_coat:
    print("\nEither it's not cold or I have a coat.")

# 4. Loops

## For Loop
##A for loop in Python is used to iterate over a sequence (like a list, range, or string) and runs a block of code 
##once for each item in the sequence.

pets = ["Cat", "Dog", "Chinchilla", "Turtle"]
for pet in pets:
    print(pet)

## While Loop
##A while loop in Python repeatedly executes a block of code as long as a specified condition remains True.

count = 2
while count < 5:
    print("\nCount is:", count)
    count += 1

# 5. Breaking and Continuing Loops

##A break is used to stop code from executing once a specified condition is met.
for num in range(5):
    if num == 3:
        print("Breaking out of the loop at num =", num)
        break
    print(num)

for num in range(5):
    if num == 3:
        continue  
    print(num)

# 6. Pass Statement
##A pass statement in Python is a placeholder that does nothing when executed and is used when a block of code is syntactically required
##but no action needs to be taken yet, such as in empty functions, classes, or loops under development.

for num in range(5):
    if num == 2:
        pass  # Placeholder for future code, does nothing here
    else:
        print(f"\nProcessing number: {num}")

# Summary of Control Flow Concepts:
# - If Statements: Make decisions based on conditions (if, elif, else)
# - Loops: Repeat actions (for, while)
# - Break, Continue, Pass: Control the flow of loops and conditional statements