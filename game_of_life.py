#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

on = 255
off = 0

def update(frameNum, img, grid, n):
    new_grid = grid.copy()
    for i in range(n):
        for j in range(n):
            total = (grid[(i - 1) % n, (j - 1) % n]
            + grid[(i - 1) % n, j]
            + grid[(i - 1) % n, (j + 1) % n]
            + grid[i, (j - 1) % n]
            + grid[i, (j + 1) % n]
            + grid[(i + 1) % n, (j - 1) % n]
            + grid[(i + 1) % n, j]
            + grid[(i + 1) % n, (j + 1) % n]) / 255

            if grid[i, j] == on and (total < 2 or total > 3):
                new_grid[i, j] = off
            elif grid[i, j] == off and total == 3:
                new_grid[i, j] = on

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

def main():
    n = 100
    grid = np.random.choice([on, off], (n, n), p=[0.2, 0.8])
    fig, axs = plt.subplots()
    img = axs.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, n), frames=1000, save_count=50)
    plt.show()

main()
