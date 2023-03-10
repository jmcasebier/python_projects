#!/usr/bin/env python3
# Calculator

# imports
from decimal import Decimal
from sys import exit

logo = """
      CALCULATOR
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
calculations_complete = False
valid_operations = ["+", "-", "*", "/"]
result = Decimal(0)
continue_calc = "n"

# add function
def add(num1, num2):
    """Returns the sum of num1 and num2"""
    return num1 + num2

# subtract function
def subtract(num1, num2):
    """Returns the difference of num1 and num2"""
    return num1 - num2

# multiply funciton
def multiply(num1, num2):
    """Returns the product of num1 and num2"""
    return num1 * num2

# divide function
def divide(num1, num2):
    """Returns the quotient of num1 and num2"""
    return num1 / num2

# greet user
print(logo)

while not calculations_complete:
    if continue_calc != "y":
        first_num = Decimal(input("Enter the first number:\n").strip())
    print("Addition (+)\nSubtraction (-)\nMultiplication (*)\nDivision (/)")
    operation = input("Select an operation (+, -, *, /):\n").strip()
    while operation not in valid_operations:
        operation = input(operation + "is not a valid operation.\nSelect an operation (+, -, *, /):\n").strip()

    second_num = Decimal(input("Enter the second number:\n").strip())
    if operation == "+":
        result = add(first_num, second_num)
    elif operation == "-":
        result = subtract(first_num, second_num)
    elif operation == "*":
        result = multiply(first_num, second_num)
    elif operation == "/":
        result = divide(first_num, second_num)
    else:
        print("An unexpected error ocurred causing the program to terminate.")
        exit()

    
    print(first_num, operation, second_num, "=", result)
    continue_calc = input("Enter 'y' to continue calculations with " + str(result) + ", enter 'n' to start a new calculation, or enter 'exit' to quit:\n").strip().lower()
    while continue_calc not in ["y", "n", "exit"]:
        continue_calc = input("'" + continue_calc + "' is not a vlaid option.\nEnter 'y' to continue calculations with " + str(result) + ", enter 'n' to start a new calculation, or enter 'exit' to quit:\n").strip().lower()

    if continue_calc == "y":
        first_num = result
    elif continue_calc == "n":
        result = Decimal(0)
    elif continue_calc == "exit":
        calculations_complete = True
    else:
        print("An unexpected error ocurred causing the program to terminate.")
        exit()

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#         000  0000000000    000000000    #
#         000  00000000000  00000000      #
#         001  001 001 001  100           #
#         101  101 101 101  101           #
#         110  011 110 010  101           #
#         101  101  10 101  101           #
#         111  111   1 111  111           #
#    111  111  111     111  111           #
#    111 1 11  111     11    111 111 1    #
#     1 111     1      1      1 11 11     #
#                                         #
#          http://jmcasebier.com          #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #