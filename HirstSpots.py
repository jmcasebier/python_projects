#!/usr/bin/env python3
# Hirst Spots

# Imports
from random import randint
import turtle

# Constants
FORWARD = 75#4
ANGLE = 90
SIZE = 50#3
WIDTH = 850
HEIGHT = 550

# Create turtle and screen instances
t = turtle.Turtle()
screen = turtle.Screen()

# Screen sizing
screen.setup(WIDTH + ((SIZE + FORWARD) * 2), HEIGHT + ((SIZE + FORWARD) * 2), startx=15, starty=15)

# Change turtle colormode to 255
turtle.colormode(255)
t.speed('fastest')
t.hideturtle()
t.penup()

# Returns a random rgb color
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# TODO: Create Hirst spot painting
t.setposition(-abs(WIDTH / 2), -abs(HEIGHT / 2))
columns = round(WIDTH / FORWARD)
rows = round(HEIGHT / FORWARD)
current_row = 1
for _ in range(rows):
    for _ in range(columns):
        t.dot(SIZE, random_color())
        t.forward(FORWARD)
    t.dot(SIZE, random_color())
    if current_row % 2 == 0:
        t.right(ANGLE)
        t.forward(FORWARD)
        t.right(ANGLE)
    else:
        t.left(ANGLE)
        t.forward(FORWARD)
        t.left(ANGLE)
    current_row += 1
for _ in range(columns):
    t.dot(SIZE, random_color())
    t.forward(FORWARD)
t.dot(SIZE, random_color())

# Screen configuration
screen.title('Hirst Spots')
screen.exitonclick()

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