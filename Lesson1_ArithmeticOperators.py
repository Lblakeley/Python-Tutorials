##Python Tutorials
##Lesson 1: Arithmetic Operators

##Arithmetic Operators are used to perform basic mathematical operations like (but not limited to): addition, subtraction, multiplication, and division.
##While not material, notice the '\n' following each print statement. This is known as the newline character and signifies a new line. In this case, it adds a line above 
##each Python statement, making the terminal, which shows the print statements, more readable. 

# Addition
print('\nAddition:',2 + 5)
##Output is 7

# Subtraction
print('\nSubtraction:',15-9)
##Output is 6

# Unary Plus and Minus
x = 5
print('\nUnary Operator(+):',+x)  
print('\nUnary Operator(-):',-x)  
##Output of Unary Operator(+) is 5 and output of unary operator(-) is -5. This example also utilizes a variable (x), variables will be addressed more in later lessons. 

##Unary operators in Python are useful for various tasks. The unary minus (-) can quickly negate numbers, such as inverting a sign or converting a string value to a 
##number (i.e., int("-5") becomes -5). The not operator is valuable for inverting boolean values or checking truey/false conditions
##(i.e., not value checks if value is false). Unary operators also simplify financial calculations, such as if all loss values were recorded in positives and you
##need to ensure the final value printed is negative, and help toggle boolean flags in conditional checks. Additionally, they are useful in indexing, 
##like accessing elements from the end of a list with negative indices (i.e., arr[-2]).

# Multiplication
print('\nMultiplication:',10*12)
##Output is 120

# Division (float)
print('\nDivision (float):',100/40)
##Output is 2.5


# Division (floor)
print('\nDivision (floor):',10//3)
##Output is 3

##Floor division is performed using two forward slashes and calculates the number of times the divisor (in the above case, 3) 
##goes into the dividend (in the above case, 10).

# Modulus
print('\nModulus:',10%3)
##Output is 1

##The modulus operator is performed using the percent symbol (%) and calculates the remainder. For instance, 3 goes into 10 3 times. 
##3*3 = 9, so 10-9 =1. Meaning, the remainder is one. 


# Minutes to hours example with Division(floor) and Modulus Operators

print('\nMinutes converted to hours:',90//60,":",90%60)
##Output is 1:30

##To arrive at the number of hours in 90 minutes, we start by using the double forward slash so floor division is performed. This tells us how many times 60 minutes 
##fully goes into 90 minutes. To arrive at the number of minutes left, we use the modulus operator. The modulus operator subtracts 60 from 90 and arrives at the remainder,
##30 minutes. Put together, floor division and the modulus operator can quickly convert the number of minutes into hours and minutes.

# Exponentation
print('\nExponentation:',250**3)
##Output is 15,625,000

#Arithmetic operators in Python do follow PEMDAS

print('\nArithmetic operators following PEMDAS:',10 + 5*(8-3))
##Output is 35

##Python read the above formula and first subtracted 3 from 8 to arrive at 5. Then, python multiplied the 5 that was in the parentheses by 5 to arrive at 25. Finally, 10
##was added to 25 to arrive at 35. This is an example of how Python adheres to the PEMDAS order of operations when performing calculations. 