#!/usr/bin/env python3
# Rock Paper Scissors

# imports
from random import randint
from sys import exit

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# greet user
print("Welcome to ROCK PAPER SCISSORS!")
print("**RULES: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
print() # print blank line

# prompt user for choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip())
if user_choice == 0:
    user = rock
elif user_choice == 1:
    user = paper
elif user_choice == 2:
    user = scissors
else:
    print("That was an invalid choice...apparently you don't like to follow rules.")
    print("Game over, you rebel.")
    exit()

# randomize computer choice
comp_choice = randint(0, 2)
if comp_choice == 0:
    comp = rock
elif comp_choice == 1:
    comp = paper
else:
    comp = scissors

# display choices
print() # print blank line
print("User choice:", user, sep="\n")
print() # print blank line
print("Computer choice:", comp, sep="\n")
print() # print blank line

# determine winner
if user_choice == 0:
    if comp_choice == 1:
        result = "YOU LOSE."
    if comp_choice == 2:
        result = "YOU WIN."
elif user_choice == 1:
    if comp_choice == 2:
        result = "YOU LOSE."
    if comp_choice == 0:
        result = "YOU WIN."
else:
    if comp_choice == 0:
        result = "YOU LOSE."
    if comp_choice == 1:
        result = "YOU WIN."

# check for a valid result
if "result" not in locals():
    result = "TIE."

# display result
print(result)

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