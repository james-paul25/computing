import pygame
from pygame.locals import *
import sys

# this a file for game methods like moving objects, collision detection, etc.

def moveCircle(keys, circle_x, circle_y):
    # W -> up
    # S -> down
    # A -> left
    # D -> right
    if keys[K_w]:
        circle_y -= 1  # Move up
    elif keys[K_s]:
        circle_y += 1  # Move down
    elif keys[K_a]:
        circle_x -= 1  # Move left
    elif keys[K_d]:
        circle_x += 1  # Move right
    return circle_x, circle_y