# Reeborg's Maze

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Lost in a maze
#Reeborg was exploring a dark maze and the battery in its flashlight ran out.

#Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

#What you need to know
#The functions move() and turn_left().
#Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#How to use a while loop and if/elif/else statements.

while not at_goal():
    if right_is_clear():
        for i in range(3):
            turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

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