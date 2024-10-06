# Basic Definitions:

# 1.	Variable: A variable in Python is a name that refers to a value. 
# For example:
x = 5
name = "Alice"


# 2.	Data Types: Python supports various data types, including:
#     o	Integers: Whole numbers (e.g., 1, 42)
#     o	Floats: Decimal numbers (e.g., 3.14, 2.0)
#     o	Strings: Text (e.g., "hello", "Python")
#     o	Lists: Ordered collections (e.g., [1, 2, 3], ["apple", "banana"])
#     o	Tuples: Ordered, immutable collections (e.g., (1, 2, 3))
#     o	Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 30})
#     o	Booleans: True or False

# 3.	Functions: Blocks of reusable code that perform a specific task. 
#       Defined using the def keyword. For example:
def greet(name):
    return f"Hello, {name}!"
print(greet("MoeinNajafi1998"))

# Here's a simple example that combines variables, loops, and functions:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")
# This code defines a function to calculate the factorial of a number and then prints the factorial of 5.
# Feel free to ask more specific questions or dive deeper into any topic!

# Basic Operators
# 1.	Arithmetic Operators:
sum = 5 + 3
diff = 5 - 3
prod = 5 * 3
quot = 5 / 3
# 2.	Comparison Operators:
is_equal = (5 == 3)
is_not_equal = (5 != 3)
is_greater = (5 > 3)
