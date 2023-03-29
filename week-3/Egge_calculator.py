"""
Title: Egge_calculator
Written by: William Egge
Description: A python document that creates and uses basic mathematical operations
Date: 2023-03-29

"""

# Create a functions named add, subtract, divide, and multiply with two parameters each
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def divide(x, y):
    return x / y
def multiply(x, y):
    return x * y

# Create variables to test each function
num1 = 8
num2 = 4

# Use the variables to build strings for the results
add_result = f"{num1} + {num2} is {add(num1, num2)}"
subtract_result = f"{num1} - {num2} is {subtract(num1, num2)}"
divide_result = f"{num1} / {num2} is {divide(num1, num2)}"
multiply_result = f"{num1} * {num2} is {multiply(num1, num2)}"

# Call each function passing in the variables
# Print the results to the console window using an output variable and string concatenation
print(add_result)
print(subtract_result)
print(divide_result)
print(multiply_result)
