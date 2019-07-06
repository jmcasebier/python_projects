#!/usr/bin/env python3

import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
r = 0
g = 100
b = 255
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            r = randrange(256)
            g = randrange(256)
            b = randrange(256)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    #screen.fill((0, 0, 0))
    color = (r, g, b)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 5, 5))

    pygame.display.flip()
    clock.tick(60)
