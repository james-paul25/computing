import pygame
from pygame.locals import *

def moveCircle(keys, circle_x, circle_y):
    
    if keys[K_LEFT]:
        circle_x -= 1  # Move left
    elif keys[K_RIGHT]: 
        circle_x += 1  # Move right
    elif keys[K_UP]:
        circle_y -= 1  # Move up
    elif keys[K_DOWN]:
        circle_y += 1  # Move down
    
    return circle_x, circle_y