#!/usr/bin/env python3
# Treasure Island

# imports
from sys import exit

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# introduce user to environment
print() # print blank line
print("After a long, perilous journey, you have finally arrived at Treasure Island!")
print("You disembark your ship at once and begin to follow a narrow, overgrown pathway into the densely wooded area covering the small island.")
print() # print blank line
print("You reach what appears to be a fork in the pathway.")

# prompt user for direction
user_response = input("Which way will you go? (Please enter 'left' or 'right')\n").strip()
print() # print blank line
if user_response.upper() == "LEFT":
    # continue journey
    print("You proceed down the path to the left.")
else:
    # game over
    print('''

    You fell into a hole!

         _.--""--._
        |  _    _  |
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    (_"=-.}______{.-="_)
     _  _.=("''")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}

          GAME OVER

    ''')
    exit()

# continue user journey
print() # print blank line
print("You walk for what seems like an eternity, though you know the island is less than a mile in diameter.")
print("Finally, you arrive at a waterway that seems to divide the island.")
print("You can see the continuation of the path on the opposite side of the waterway.")
print("The tide is high, but there may be a dry way to cross at low tide.")
print() # print blank line
print("You could attempt to swim across now, or wait for the tide to lower.")

# prompt user for direction
user_response = input("What will you do? (Please enter 'swim' or 'wait')\n").strip()
print() # print blank line
if user_response.upper() == "WAIT":
    # continue journey
    print("You wait patiently for the water level to drop.")
else:
    # game over
    print('''

 You were attacked by trout!

         _.--""--._
        |  _    _  |
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    (_"=-.}______{.-="_)
     _  _.=("''")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}

          GAME OVER

    ''')
    exit()

# continue user journey
print() # print blank line
print("As the water receeds, a natural bridge is revealed that reaches the other side.")
print("You continue on your trek, crossing the waterway and following the path onward.")
print("You begin to feel a tingling sensation, as if in the presence of magic.")
print("Picking up the pace, you nervously press on.")
print("At long last, you arrive at a clearing containing three doors.")
print("The doors each appear to lead to nowhere.")
print() # print blank line
print("Each of the three doors is a different color: red, yellow, and blue.")

# prompt user for direction
user_response = input("What door will you open? (Please enter 'red', 'yellow', or 'blue')\n").strip()
print() # print blank line
if user_response.upper() == "YELLOW":
    # continue journey
    print('''
    
                    _.--.
                _.-'_:-'||
            _.-'_.-::::'||
        _.-:'_.-::::::' ||
      . .'`-.-:::::::'  ||
    /.'";|:::::::'      ||_
    ||   ||::::::'     _.;._'-._
    ||   ||:::::'  _.-!oo @.!-._'-.
    |'.  ||:::::.-!()oo @!()@.-'_.|
    '.'-;|:.-'.&$@.& ()$%-'o.'" U||
        `>'-.!@%()@'@_%-'_.-o_.|'||
        ||-._'-.@.-'_.-' _.-o  |'||
        ||=[ '-._.-|U|.-'    o |'||
        || '-.]=|| |'|      o  |'||
        ||      || |'|        _| ';
        ||      || |'|    _.-'_.-'
        |'-._   || |'|_.-'_.-'
        '-._'-.|| |' `_.-'
            '-.||_..-'
        
        YOU FOUND THE TREASURE!
    
    ''')
    exit()
elif user_response.upper() == "RED":
    # game over
    print('''

  You were burned by fire!

         _.--""--._
        |  _    _  |
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    (_"=-.}______{.-="_)
     _  _.=("''")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}

          GAME OVER

    ''')
    exit()
else:
    # game over
    print('''

  You were eaten by beasts!

         _.--""--._
        |  _    _  |
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    (_"=-.}______{.-="_)
     _  _.=("''")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}

          GAME OVER

    ''')
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