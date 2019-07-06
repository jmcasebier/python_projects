#!/usr/bin/env python3

import numpy as np
from PIL import Image

gscale = '@%#*+=-:. '

def computeAverage(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w * h))

def convertImageToAscii(fileName, cols, scale):
    image = Image.open(fileName).convert('L')
    W, H = image.size
    print('Input image dimensions: %d x %d' % (W, H))
    w = W // cols
    h = w // scale
    rows = int(H // h)
    print('Columns: %d, Rows: %d' % (cols, rows))
    print('Tile dimensions: %d x %d' % (w, h))
    if cols > W or rows > H:
        print('Image too small for specified columns.')
        exit(0)
    asciiImg = []
    for i in range(rows):
        y1 = int(i * h)
        y2 = int((i + 1) * h)
        if i == rows - 1:
            y2 = H
        asciiImg.append('')
        for n in range(cols):
            x1 = n * w
            x2 = (n + 1) * w
            if n == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(computeAverage(img))
            maxGradient = len(gscale) - 1
            character = gscale[int((avg * maxGradient) / 255)]
            asciiImg[i] += character
    return asciiImg

def main():
    imgFile = input('Enter a filename to read: ')
    outFile = input('Enter the name of the output file: ')
    scale = 0.43
    cols = 80
    print('Generating ACSII art...')
    asciiImg = convertImageToAscii(imgFile, cols, scale)
    f = open(outFile, 'w')
    for row in asciiImg:
        f.write(row + '\n')
    f.close()
    print('ASCII art written to %s' % outFile)

main()
