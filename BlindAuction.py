#!/usr/bin/env python3
# Blind Auction

# imports
from os import system
from decimal import Decimal

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction_in_progress = True
bids = {}
highest_bid = Decimal(0)
highest_bidder = ""

while auction_in_progress:
    system("cls") # clear console
    print(logo) # print logo
    print("Welcome to the Blind Auction.") # greet user
    bidder_name = input("Please enter your name:\n").strip() # prompt for name
    # ensure name is unique
    while bidder_name in bids.keys():
        bidder_name = input("Sorry, that name already exists, please enter a unique name:\n")
    bid_amount = Decimal(input("Please enter your bid:\n$").strip()) # prompt for bid amount
    bids[bidder_name] = bid_amount # add bid to bids
    system("cls") # clear console
    more_bids = ""
    while more_bids != "yes" and more_bids != "no":
        more_bids = input("Are there more bids to be placed? (Please enter 'yes' or 'no')\n").lower().strip()
    if more_bids == "no":
        auction_in_progress = False

for key, value in bids.items():
    if value > highest_bid:
        highest_bid = value
        highest_bidder = key

system("cls") # clear console
print(highest_bidder, " won the auction with a bid of $", highest_bid, sep="") # print auction results

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