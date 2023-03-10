#!/usr/bin/env python3
# Check Splitter

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# imports
import time
import os
from decimal import Decimal

# greet user
os.system("cls") # clear console
print("CHECK SPLITTER")
print("Calculates tip and splits final check")
print("Requires total bill amount, preferred tip percentage, and number of paying parties")

print() # print blank line

# request total bill amount
time.sleep(2) # sleep for 1 second
bill_amount = Decimal(input("What is the total bill amount?\nPlease enter the numerical amount only (Do not include $)\n").strip())

# request preferred tip percentage
time.sleep(1) # sleep for 1 second
tip_percentage = Decimal(input("What is the preffered tip percentage?\nPlease enter a numerical value (Do not include %)\n").strip())

# request number of paying parties
time.sleep(1) # sleep for 1 second
paying_parties = int(input("How many parties will be paying?\n").strip())

print() # print blank line

# calculate total including tip for each paying party
fair_share = round(bill_amount * ((tip_percentage / 100) + 1) / paying_parties, 2)

# output fair share to user
time.sleep(2) # sleep for 1 second
print("**Including the tip, each party should contribute $", fair_share, sep="")

print() # print blank line

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