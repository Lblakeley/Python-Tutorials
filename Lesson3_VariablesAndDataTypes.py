##Python Tutorials
##Lesson 3: Variables & Data Types


#Variables in Python 
##Variables are simple, yet very important to know when coding in Python. A variable is used to store data and can hold different types
##of values(i.e. strings, numbers, boolean values, etc). A variable is created by assigning a value to it using the '='.

name = "Taco"
age = 7
is_cat = True

print("Name:", name)  
##Output is Name: Taco

print("Age:", age)    
##Output is Age: 7

print("Is cat:", is_cat)  
##Output is Is cat: True

#Data Types in Python

# Integer (int)
##An integer is a whole number which can be negative, zero, or positive, with no decimal. 

x = 10  
y = -5  
z = 0
print("\nInteger:")
print("x:", x)  
##Ouput is x: 10
print("y:", y)  
##Output is y: -5
print("z:", z)
##Output is z: 0

# Float (float)
##A float represents a number with a decimal point, also known as a real number.

height =  65.5
temperature = -10.6
print("\nHeight:", height)  
##Output is Height: 65.5
print("\nTemperature:", temperature)  
##Output is Temperature: -10.6

# String (str)
##A string value is a sequence of characters enclosed in quotation marks. String can be enclosed in single quotes, double quotes, or triple quotes.

name = "Lauren"
greeting = "Hello, world!"
print("\nName:", name) 
##Output is Name: Lauren
print("\nGreeting:", greeting)  
##Output is Greeting: Hello, world!

# Boolean (bool)
##A boolean value represents one of two possible values: True or False. 
is_cold = True
has_coat = False
print("\nIs it cold?", is_cold)  
##Output is Is it cold? True
print("\nDo you have a coat?", has_coat) 
##Output is Do you have a coat? False

# 3. Type Conversion (Casting)

# Integer to Float
x = 5  
y = float(x)  
print("\nInteger to Float:")
print(f"Converted {x} from type integer to type float {y}.")  
##Output is 5.0

# String to Integer
x = "10"  
y = int(x)  
print("\nString to Integer:")
print(f"Converted {x} from type string to type integer {y}.")
##Output is 10

# Float to Integer
x = 3.7  
y = int(x)  # Convert float to integer (truncates the decimal part)
print("\nFloat to Integer")
print(f"Converted {x} from type float to type integer {y}.")
##Output is 3

# 4. Checking Data Types
x = 5
print("\nChecking Data Types:")
print("The type of x is:", type(x))  

y = "Hello"
print("The type of y is:", type(y))  

# 5. Common Operations with Data Types

# Strings: Concatenation (combining two strings)
greeting = "Hello"
name = "Lauren"
message = greeting + " " + name
print("\nString Concatenation:")
print(message)  
##Output is Hello Lauren

# F-Strings are also great ways to combine strings
print("\nF-String Greeting:")
print(f"{greeting} {name}")
##Output is Hello Lauren but there was no need to create the term message to print the combined strings simply. 

# Strings: Repetition (repeating a string multiple times)
word = "Hi! "
print("\nString Repetition:")
print(word * 3)  
##Output is Hi! Hi! Hi!

# Strings: Indexing and Slicing
##Indexing allows you to access a specific character in a string using its position (starting from 0).
##Slicing allows you to extract a portion of a string using a range of indices.
text = "Python"
print("\nString Indexing and Slicing:")
print("First letter:", text[0])  
##Output is P
print("Last letter:", text[-1])  
##Output is n
print("Slice (first three letters):", text[0:3]) 
##Output is Pyt
print("Slice (from index 2 onward):", text[2:])  
##Output is thon

# Integers and Floats: Addition
a = 10
b = 2.5
result = a + b
print("\nInteger and Float Addition:")
print(result)  
##Output is 12.5

# Integers and Floats: Division
a = 10
b = 3
result = a / b
print("\nInteger and Float Division:")
print(result)  
##Output is 3.3333333333333335

# Booleans: Boolean Expressions
is_tall = True
is_adult = False
print("\nBoolean Expressions:")
print("Is she tall and an adult?", is_tall and is_adult)  
print("Is she tall or an adult?", is_tall or is_adult)   
print("Is she not an adult?", not is_adult)
##Output is Is she tall and an adult? False
##Is she tall or an adult? True
##Is she not an adult? True

# 6. Summary of Python Data Types
# Integers: Whole numbers (int).
# Floats: Decimal numbers (float).
# Strings: Sequences of characters (str).
# Booleans: Logical values (True or False).

