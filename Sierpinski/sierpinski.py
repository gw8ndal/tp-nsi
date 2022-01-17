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



a = (0, 0)
b = (1000, 0)
c = (500, 1000)
coord = (a, b, c)

# voir https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
pygame.draw.polygon(fenetre, green, (a, b, c),0)

def milieu(a, b):
    xm = (a[0]+ b[0])//2
    ym = (a[1]+ b[1])//2
    return (xm, ym)

def sierpinski(n, coord):
    if n >= 0:
        e = milieu(coord[0], coord[1])
        f = milieu(coord[1], coord[2])
        g = milieu(coord[2], coord[0])
        
        pygame.draw.polygon(fenetre, black, (e, f, g),0)
        
        pygame.display.flip()
        sierpinski(n-1, (coord[0], e, g))
        sierpinski(n-1, (e, coord[1], f))
        sierpinski(n-1, (g, f, coord[2]))

sierpinski(13, coord)

# Boucle infinie qui attend l'événement QUIT pour terminer le programme
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


