##Python Tutorials
##Lesson 2: Assignment Operators

##Assignment operators are used to assign values to variables. They are related to arithmetic operators which is why I am covering them in the second lesson.
##While variables will be covered more in depth in the next lesson, notice how the assignment operators are performed on a variable, not a value. Assignment operators
##must be performed on a variable. Variables can be assigned new values as often as wanted/needed. In this case, x is used as the variable in every assignment operator 
##example. The variable x changes its value many times in this lesson.

# Basic Assignment (=)
x = 10
print("\nBasic Assignment (=):", x)  
##Output is 10

# Addition Assignment (+=)
x = 10
x += 5  
print("\nAddition Assignment (+=):", x)  
##Output is 15

# Subtraction Assignment (-=)
x = 10
x -= 3  
print("\nSubtraction Assignment (-=):", x)  
##Output is 7

# Multiplication Assignment (*=)
x = 10
x *= 2  
print("\nMultiplication Assignment (*=):", x)  
##Output is 20

# Division Assignment (/=)
x = 10
x /= 2  
print("\nDivision Assignment (/=):", x) 
## Output is 5.0

# Floor Division Assignment (//=)
x = 10
x //= 3  
print("\nFloor Division Assignment (//=):", x)  
##Output is 3

# Modulus Assignment (%=)
x = 10
x %= 3  
print("\nModulus Assignment (%=):", x)  
##Output is 1

# Exponentiation Assignment (**=)
x = 10
x **= 3 
print("\nExponentiation Assignment (**=):", x) 
##Output is 1000

##There are also Bitwise Assignment Operators but those it is not essential knowledge for becoming a competent data scientist, and they are a more complicated concept
##so those will be saved for a later lesson.