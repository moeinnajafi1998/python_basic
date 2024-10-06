# comment in python:
# Each line needs a `#`
# Python ignores these lines
# some notes
# some notes
# some notes

# o	Single-line comments start with #.
# This is a single-line comment
# o	Multi-line comments can be written using triple quotes """ or '''.
"""
This is a multi-line comment
"""

# what are indents used to in python
# In Python, indentation is used to define the structure and flow of the code. 
# Unlike many other programming languages that use curly braces {} or keywords to define blocks of code, Python uses indentation to signify blocks of code.

# Key Points about Indentation in Python
# 1.	Defining Code Blocks: Indentation is used to group statements into blocks. 
#       These blocks could be part of control structures like loops and conditionals, or function and class definitions.
# 2.	Consistency is Crucial: All lines of code in a block must have the same level of indentation. 
#       Mixing tabs and spaces can lead to errors.
# 3.	Indentation Level: The standard indentation level is four spaces, although the actual number of spaces can vary. 
#       The important thing is consistency within a block of code.

# Examples
# Example 1: If-Else Statement
x = 10
if x > 0:
    print("Positive number")
else:
    print("Non-positive number")
# Here, the print statements are indented to indicate they belong to the if and else blocks respectively.

# Example 2: Loop
for i in range(5):
    print(i)
    if i % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
# In this example, the print statements inside the loop are indented to show they are part of the for loop. 
# Additionally, the if and else blocks within the loop have further indentation.

# Example 3: Function Definition
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python programming.")

greet("MoeinNajafi1998")
# The body of the function greet is indented to indicate that the print statements are part of the function definition.

# Importance of Indentation
# •	Readability: Indentation makes the code more readable and organized.
# •	Syntax Requirement: In Python, indentation is not just for readability; it's a part of the syntax. Incorrect indentation will result in an IndentationError.

# Indentation Error Example => uncomment code to see result
# def greet(name):
# print(f"Hello, {name}!")
#     print("Welcome to Python programming.")

# In this example, the code will raise an IndentationError because the second print statement does not match the indentation level of the first print statement within the function block.

# In summary, indentation in Python is used to define the logical structure of the code. It's essential for both readability and proper functioning of the program

