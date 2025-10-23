import pygame
from pygame.locals import *
import sys
import math

pygame.init()
font = pygame.font.SysFont("Arial",12, bold=True)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Activity 2 - Rotating Triangle")
green = (0, 255, 0)
black = (0, 0, 0)

angle = 0
clock = pygame.time.Clock()
center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Rotating triangle
    tri_radius = 60
    tri_points = []
    for i in range(3):
        theta = angle + i * (2 * math.pi / 3)
        x = int(center_x + tri_radius * math.cos(theta))
        y = int(center_y + tri_radius * math.sin(theta))
        tri_points.append((x, y))
    pygame.draw.polygon(screen, green, tri_points)

    # Display angle as text (in degrees)
    angle_deg = int(math.degrees(angle) % 360)
    angle_text = font.render(f"Angle: {angle_deg}°", True, black)
    screen.blit(angle_text, (10, 10))

    pygame.display.flip()
    angle += 0.03  # Increment angle for rotation
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()


