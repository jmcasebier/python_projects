#!/usr/bin/env python3
# Band Name Generator

# imports
import time
import os

#1. Create a greeting for your program.
os.system("cls") # clear console
print("""
The
 ____    ____  ____   ___        ____    ____  ___ ___    ___   
|    \  /    ||    \ |   \      |    \  /    ||   |   |  /  _]  
|  o  )|  o  ||     ||    \     |     ||  o  ||       | /  [_   
|     ||     ||  |  ||  D  |    |  |  ||     ||  \_/  ||    _]  
|  O  ||     ||  |  ||     |    |  |  ||     ||   |   ||   [_   
|     ||  |  ||  |  ||     |    |  |  ||  |  ||   |   ||     |  
|_____||__|__||__|__||_____|    |__|__||__|__||___|___||_____|  
                                                                
  ____    ___  ____     ___  ____    ____  ______   ___   ____  
 /    |  /  _]|    \   /  _]|    \  /    ||      | /   \ |    \ 
|   __| /  [_ |     | /  [_ |  D  )|  o  ||      ||     ||  D  )
|  | __|    _]|  |  ||    _]|    / |     ||_|  |_||  O  ||    / 
|  |_|||   [_ |  |  ||   [_ |    \ |     |  |  |  |     ||    \ 
|     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||  .  |
|___,_||_____||__|__||_____||__|\_||__|__|  |__|   \___/ |__|\_|
                                                                
                                                            2023
""")
time.sleep(3) # sleep for 3 seconds
os.system("cls") # clear console
time.sleep(1) # sleep for 1 second
print("Welcome to the BAND NAME GENERATOR!")
time.sleep(2) # sleep for 2 seconds
print("Before generating a band name, you must answer two questions:\n")

#2. Ask the user for the city that they grew up in.
time.sleep(3) # sleep for 3 seconds
city = input("\n1) What city did you grow up in?\n").strip()

#3. Ask the user for the name of a pet.
time.sleep(1) # sleep for 1 second
pet = input("\n2) What is the name of your pet?\n").strip()

#4. Combine the name of their city and pet and show them their band name.
time.sleep(1) # sleep for 1 second
os.system("cls") # clear console
time.sleep(1) # sleep for 1 second
print("Generating band name", end="", flush=True)
for i in range(4):
  time.sleep(1) # sleep for 1 second
  print(".", end="", flush=True)

time.sleep(1) # sleep for 1 second
os.system("cls") # clear console
time.sleep(1) # sleep for 1 second
print("Your band name is", end="", flush=True)
for i in range(4):
  time.sleep(0.5) # sleep for 0.5 seconds
  print(".", end="", flush=True)
time.sleep(0.5) # sleep for 0.5 seconds
print(city.upper(), pet.upper() + "!")

#5. Make sure the input cursor shows on a new line:
time.sleep(3) # sleep for 3 seconds
print("Thank you for using the BAND NAME GENERATOR!")

# Solution: https://replit.com/@appbrewery/band-name-generator-end

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