#!/usr/bin/env python3
# Number Game

# imports
from random import randint
from sys import exit

number = randint(0, 100)

# check guess
def check_guess(guess):
    if guess == number:
        print("You guessed the number!")
        exit()
    elif guess < number:
        if guesses > 1:
            print("Too low, the number is higher.")
    elif guess > number:
        if guesses > 1:
            print("Too high, the number is lower.")
    else:
        print("An unexpected error was encountered, causing the program to terminate.")
        exit()

# introduce game
print("Welcome to the Number Game!")
# set difficulty
difficulty = input("Choose your difficulty level:\n('Easy', 'Hard', or 'Insane'):\n").strip().lower()
while difficulty not in ["easy", "hard", "insane"]:
    difficulty = input("Please enter 'Easy', 'Hard', or 'Insane':\n").strip().lower()
if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5
elif difficulty == "insane":
    guesses = 3
else:
    print("An unexpected error was encountered, causing the program to terminate.")
    exit()

print("I am thinking of a number between 1 and 100...can you guess what it is?")

# prompt user to guess
while guesses > 0:
    print("You have", guesses, "guesses left.")
    user_guess = int(input("Enter your guess:\n").strip())
    check_guess(user_guess)
    guesses -= 1

print("Game Over...you ran out of guesses.")
print("The number was", number)

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