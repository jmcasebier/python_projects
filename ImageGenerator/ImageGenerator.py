#!/usr/bin/env python3
# Image Generator

# Imports
import numpy as np
import turtle
from PIL import Image

# Constants
SCALE = 1
COLS = 100
FORWARD = 6
ANGLE = 90
SIZE = 5

# Colors
rainbow_color_scale = ['#000033', '#000066', '#330033', '#330000', '#000099', '#330066', '#003300', '#330099', '#660033', '#660000', '#003366', '#333300', '#0000CC', '#003333', '#333333', '#660066', '#3300CC', '#333366', '#660099', '#333399', '#003399', '#663300', '#0000FF', '#663333', '#6600CC', '#663366', '#3333CC', '#0033CC', '#3300FF', '#990000', '#663399', '#990033', '#990066', '#6600FF', '#3333FF', '#990099', '#0033FF', '#993300', '#6633CC', '#993333', '#9900CC', '#6633FF', '#006600', '#993366', '#006633', '#336600', '#993399', '#9900FF', '#336633', '#9933CC', '#CC0000', '#006666', '#CC0033', '#666600', '#9933FF', '#CC0066', '#CC0099', '#0066CC', '#CC3300', '#006699', '#CC00CC', '#CC3333', '#3366FF', '#0066FF', '#336666', '#3366CC', '#CC00FF', '#CC3366', '#666633', '#336699', '#996600', '#CC3399', '#6666CC', '#FF0000', '#CC33FF', '#FF0033', '#CC33CC', '#6666FF', '#666699', '#FF0066', '#996633', '#FF3300', '#666666', '#9966FF', '#009900', '#FF3333', '#CC6600', '#FF0099', '#FF00FF', '#9966CC', '#339900', '#996666', '#FF00CC', '#009933', '#996699', '#FF3366', '#339933', '#FF3399', '#CC6633', '#FF33CC', '#FF33FF', '#669900', '#CC6666', '#009966', '#339966', '#CC66FF', '#669933', '#CC66CC', '#FF6600', '#CC6699', '#FF6633', '#009999', '#999900', '#FF66FF', '#FF6666', '#669966', '#0099FF', '#339999', '#FF6699', '#FF66CC', '#33CC00', '#00CC00', '#0099CC', '#3399FF', '#999933', '#00CC33', '#CC9900', '#6699FF', '#33CC33', '#66CC00', '#3399CC', '#FF9900', '#CC9933', '#00CC66', '#9999FF', '#66CC33', '#00FF00', '#33FF00', '#FF9933', '#33CC66', '#99CC00', '#00FF33', '#66FF00', '#33FF33', '#66FF33', '#99CC33', '#669999', '#6699CC', '#66CC66', '#99FF00', '#CCCC00', '#00FF66', '#99FF33', '#33FF66', '#999966', '#CC99FF', '#00CC99', '#CCFF00', '#FFCC00', '#FFFF00', '#FF9966', '#66FF66', '#CCFF33', '#FF99FF', '#33CC99', '#CC9966', '#CCCC33', '#FFCC33', '#FFFF33', '#CC99CC', '#99FF66', '#FF99CC', '#9999CC', '#00FF99', '#00CCCC', '#33FF99', '#99CC66', '#FF9999', '#66CC99', '#66FF99', '#33CCCC', '#CCFF66', '#FFFF66', '#CC9999', '#00CCFF', '#CCCC66', '#00FFCC', '#33FFCC', '#33CCFF', '#99FF99', '#FFCC66', '#66CCCC', '#99CC99', '#66FFCC', '#00FFFF', '#999999', '#CCFF99', '#33FFFF', '#66CCFF', '#99FFCC', '#66FFFF', '#FFFF99', '#FFCCFF', '#99CCFF', '#99FFFF', '#FFCC99', '#CCFFCC', '#CCCCFF', '#CCCC99', '#99CCCC', '#FFCCCC', '#FFFFCC', '#CCFFFF', '#CCCCCC']
purple_color_scale = ['#4A235A', '#5B2C6F', '#6C3483', '#7D3C98', '#8E44AD', '#A569BD', '#BB8FCE', '#D2B4DE', '#E8DAEF', '#F4ECF7']
color_scale = rainbow_color_scale

# Compute average brightness
def computeAverage(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w * h))

# Read image and create art
def convertImageToArt(fileName, outFile):
    image = Image.open(fileName).convert('L')
    W, H = image.size
    print('Input image dimensions: %d x %d' % (W, H))
    w = W // COLS
    h = w // SCALE
    rows = int(H // h)
    print('Columns: %d, Rows: %d' % (COLS, rows))
    print('Tile dimensions: %d x %d' % (w, h))
    # Turtle configuration
    t = turtle.Turtle()
    t.speed('fastest')
    t.hideturtle()
    t.penup()
    screen = turtle.Screen()
    screen.setup(width=COLS * FORWARD, height=rows * FORWARD, startx=2, starty=2)
    t.setposition(-abs(screen.window_width() / 2), abs(screen.window_height() / 2) - SIZE)
    if COLS > W or rows > H:
        print('Image too small for specified columns.')
        exit(0)
    for i in range(rows):
        y1 = int(i * h)
        y2 = int((i + 1) * h)
        if i == rows - 1:
            y2 = H
        for n in range(COLS):
            x1 = n * w
            x2 = (n + 1) * w
            if n == COLS - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(computeAverage(img))
            # TODO: Choose color
            maxGradient = len(color_scale) - 1
            color = color_scale[int((avg * maxGradient) / 255)]
            t.dot(SIZE, color)
            t.forward(FORWARD)
        # End of row
        t.setposition(-abs(screen.window_width() / 2), t.pos()[1] - FORWARD)
    # Save art image
    screen.getcanvas().postscript(file=outFile)
    print('Art written to %s' % outFile)
    screen.exitonclick()

# Prompt user for image and output filename
def main():
    imgFile = input('Enter a filename to read: ')
    outFile = input('Enter the name of the output file: ')
    print('Generating art...')
    convertImageToArt(imgFile, outFile)

main()

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