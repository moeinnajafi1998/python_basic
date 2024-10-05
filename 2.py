# how to get input in python:
# you can capture input from the command line using the built-in input() function

name = input("Enter your name: ")
print(f"Hello, {name}!")

# For numerical input, you can convert the result from input() to the appropriate type, like so:
age = int(input("Enter your age: "))
print(f"Your age is {age}.")

# Input Validation for Numbers
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        number = int(user_input)
        print(f"You entered the number: {number}")
        break
    else:
        print("Invalid input. Please enter a valid number.")
