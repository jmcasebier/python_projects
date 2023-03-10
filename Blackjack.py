#!/usr/bin/env python3
# Blackjack

# imports
from random import randint
import sys
import os

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###########################################################

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# greet user
print(logo)

# function that returns a random card
def deal_card():
    """returns random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 is the Ace, 10's include Jack, Queen, and King.
    return cards[randint(0, len(cards) - 1)]

#Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# function that takes a List of cards as input and returns the score.
def calculate_score(cards):
    """returns sum of cards in list taken as input"""
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
def check_for_game_over():
    if calculate_score(computer_cards) == 0:
        print("Delaer hand:", computer_cards)
        print("Dealer has Blackjack! You lose.")
        sys.exit()
    elif calculate_score(user_cards) == 0:
        print("Hand:", user_cards)
        print("Blackjack! You win!")
        sys.exit()
    elif calculate_score(user_cards) > 21:
        print("Hand:", user_cards)
        print("Bust! You lose.")
        sys.exit()
    else:
        return False

#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended. The score will need to be rechecked with every new card drawn.
while not check_for_game_over():
    print("Hand:", user_cards)
    draw_card = input("Would you like to draw another card? (Enter 'y' for yes, or 'n' for no)\n").strip().lower()
    while draw_card not in ["y", "n"]:
        draw_card = input("Please enter 'y' for yes, or 'n' for no:\n").strip().lower()
    if draw_card == "y":
        user_cards.append(deal_card())
        check_for_game_over()
    elif draw_card == "n":
        break
    else:
        print("An unexpected error has ocurred, causing the program to terminate.")
        sys.exit()

#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
while not check_for_game_over() and calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())

#If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    print("Your hand:", user_cards)
    print("Dealer hand:", computer_cards)
    if user_score == computer_score:
        print("It's a draw.")
    elif computer_score == 21:
        print("You lose.")
    elif computer_score > 21:
        print("Dealer busts! You win!")
    elif computer_score > user_score:
        print("You lose.")
    else:
        print("You win.")

if not check_for_game_over():
    compare(calculate_score(user_cards), calculate_score(computer_cards))

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