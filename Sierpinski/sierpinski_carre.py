#!/usr/bin/python
# coding: utf-8

import pygame, sys

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
size = [1000,1000]

fenetre = pygame.display.set_mode(size)
fenetre.fill(white)


length = 800
size = (length, length)
a = (0, 0)
b = (length, 0)
c = (length, length)
d = (0, length)
coord = (a, b, c, d)

# voir https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
pygame.draw.rect(fenetre, green, (a, c))

def sierpinski(n, coord):
    if n >= 0:
        a, b, c, d = coord
        e = (b[0]/3, b[1])
        f = (2*b[0]/3, b[1])
        g = (f[0], 2*c[1]/3)
        h = (e[0], g[1])
        pygame.draw.polygon(fenetre, blue, (e, f, g, h))
        pygame.display.flip()
#        sierpinski(n-1, (coord[0], e, g))
#        sierpinski(n-1, (e, coord[1], f))
pygame.display.flip()
sierpinski(13, coord)
#
# Boucle infinie qui attend l'événement QUIT pour terminer le programme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


