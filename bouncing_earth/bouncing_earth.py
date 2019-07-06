#!/usr/bin/env python3

import sys, pygame

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
angle = 1
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
space = pygame.image.load('space.jpg')
space_rect = space.get_rect()
earth = pygame.image.load('earth.png')
earth_rect = earth.get_rect()
earth_rect.right = 300
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if earth_rect.left < 0 or earth_rect.right > width:
        speed[0] = -speed[0]
    if earth_rect.top < 0 or earth_rect.bottom > height:
        speed[1] = -speed[1]

    if speed == [2, 2]:
        angle += -1
    if speed == [2, -2]:
        angle += 1
    if speed == [-2, -2]:
        angle += -1
    if speed == [-2, 2]:
        angle += -2
    angle %= 360
    
    rotated_earth = pygame.transform.rotate(earth, angle)
    earth_rect = earth_rect.move(speed)

    screen.fill(black)
    screen.blit(space, space_rect)
    screen.blit(rotated_earth, earth_rect)
    pygame.display.flip()
    clock.tick(100)
