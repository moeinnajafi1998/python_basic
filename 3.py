# 1. Conditional Statements (if, elif, else)
# Conditional statements example
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
# Explanation:
# if checks the first condition (age < 18).
# elif (else if) checks the second condition if the first one is false.
# else executes if none of the previous conditions are met.

# 2. Loops
# for Loop
# For loop example
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# while Loop
# While loop example
counter = 0
while counter < 5:
    print(f"Counter is at: {counter}")
    counter += 1
# Explanation:
# The for loop iterates over a list of numbers and prints each one.
# The while loop keeps running as long as the condition (counter < 5) is true.

# 3. Break and Continue Statements
# break Statement
# Break example in a loop
for num in range(1, 10):
    if num == 5:
        print("Stopping loop at 5.")
        break  # Exits the loop
    print(f"Number: {num}")

# continue Statement
# Continue example in a loop
for num in range(1, 6):
    if num == 3:
        print("Skipping 3.")
        continue  # Skips the rest of the loop body when num is 3
    print(f"Number: {num}")
# Explanation:
# break is used to exit a loop prematurely when a condition is met (in this case, when num is 5).
# continue is used to skip the current iteration and move to the next one when a condition is met (when num is 3, it skips printing).