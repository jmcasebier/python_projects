#!/usr/bin/env python3

from turtle import *
from random import randrange

speed(0)
bgcolor('black')
'''
penup()
goto(-28, -28)
pendown()
'''
x = 1
while x < 500:
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)

    colormode(255)
    pencolor(r, g, b)

    forward(55 + x)
    left(91)

    x += 1

hideturtle()
exitonclick()
