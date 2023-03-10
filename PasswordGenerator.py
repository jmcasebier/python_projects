#!/usr/bin/env python3
# Password Generator

#Password Generator Project
from sys import exit
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# # generate letters
# for i in range(nr_letters):
#     password += letters[random.randint(0, len(letters) - 1)]

# # generate numbers
# for i in range(nr_numbers):
#     password += numbers[random.randint(0, len(numbers) - 1)]

# # generate symbols
# for i in range(nr_symbols):
#     password += symbols[random.randint(0, len(symbols) - 1)]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_characters = nr_letters + nr_numbers + nr_symbols
for i in range(total_characters):
    # create list of remaining character types
    char_types = []
    if nr_letters > 0:
        char_types.append("letter")
    if nr_numbers > 0:
        char_types.append("number")
    if nr_symbols > 0:
        char_types.append("symbol")
    # generate random number to decide character type
    char_type = char_types[random.randint(0, len(char_types) - 1)]
    if char_type == "letter":
        password += letters[random.randint(0, len(letters) - 1)]
        nr_letters -= 1
    elif char_type == "number":
        password += numbers[random.randint(0, len(numbers) - 1)]
        nr_numbers -= 1
    elif char_type == "symbol":
        password += symbols[random.randint(0, len(symbols) - 1)]
        nr_symbols -= 1
    else:
        print("I ran into an unexpected problem: char_type", char_type, "is not valid.")
        exit()

# output generated password
print(password)

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