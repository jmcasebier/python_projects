#!/usr/bin/env python3

#imports
import turtle
from random import randrange

def main():
    #choose random numbers for di faces
    face_1 = randrange(1, 7)
    face_2 = randrange(1, 7)
    #draw dice
    draw_die(-160, 0, 150, face_1)
    draw_die(10, 0, 150, face_2)
    #hide turtle
    turtle.hideturtle()
    #wait for user to click before closing
    turtle.Screen().exitonclick()

#draw di outlines
def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

#draw di faces
def draw_dot(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(size)

#draw dice
def draw_die(x, y, size, face):
    dot_size = size / 8
    x1 = x + size / 4
    x2 = x + size / 2
    x3 = x + 3 * size / 4
    y1 = y + size / 4
    y2 = y + size / 2
    y3 = y + 3 * size / 4
    draw_square(x, y, size)
    if face % 2 == 1:
        draw_dot(x2, y2, dot_size)
    if face > 1:
        draw_dot(x1, y1, dot_size)
        draw_dot(x3, y3, dot_size)
    if face >= 4:
        draw_dot(x1, y3, dot_size)
        draw_dot(x3, y1, dot_size)
    if face == 6:
        draw_dot(x1, y2, dot_size)
        draw_dot(x3, y2, dot_size)

#run dice generator
main()
