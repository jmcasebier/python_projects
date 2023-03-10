#!/usr/bin/env python3
# Higher Lower

# imports
from art import logo, vs
from game_data import data
from random import randint
from os import system
from sys import exit

# game controller
game_over = False
score = 0

# play game
while not game_over:
    system("cls") # clear console
    print(logo) # print logo

    # select random celebrities from data
    a = data[randint(0, len(data) - 1)]
    b = data[randint(0, len(data) - 1)]
    while a == b:
        b = data[randint(0, len(data) - 1)]

    # display score
    if score > 0:
        print("You have", score, "points!")

    # display matchup
    print("Contestant A: {0}, {1} from {2}".format(a["name"], a["description"], a["country"]))
    print(vs) # print vs
    print("Contestant B: {0}, {1} from {2}".format(b["name"], b["description"], b["country"]))
    print() # print blank line

    # prompt user for guess
    guess = input("Who has more Instagram followers?\n(Enter 'A' or 'B'):\n").lower().strip()
    while guess not in ["a", "b"]:
        guess = input("Please enter 'A' or 'B':\n").lower().strip()

    # check answer
    if guess == "a":
        if a["follower_count"] > b["follower_count"]:
            print("Correct!")
            score += 1
        else:
            system("cls") # clear console
            print(logo) # print logo
            print("Game over.")
            print("You got", score, "correct.")
            game_over = True
    elif guess == "b":
        if b["follower_count"] > a["follower_count"]:
            print("Correct!")
            score += 1
        else:
            system("cls") # clear console
            print(logo) # print logo
            print("Game over.")
            print("You got", score, "correct.")
            game_over = True
    else:
        system("cls") # clear console
        print("An unexpected error was encountered.")
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