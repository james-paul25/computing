import pygame
from pygame.locals import *
import sys
import random

pygame.init()

# Window setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("October 3, 2025")

# Circle setup
circleX, circleY = 250, 0
circleRadius = 20
circleDy = 3  # Falling speed

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle setup
paddleWidth, paddleHeight = 100, 10
paddleX, paddleY = (WIDTH - paddleWidth) // 2, HEIGHT - 50
paddleSpeed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 30, bold=True)

# Game state
game_over = False

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if not game_over:  # Allow movement only when playing
        if keys[K_LEFT] and paddleX > 0:
            paddleX -= paddleSpeed
        if keys[K_RIGHT] and paddleX < WIDTH - paddleWidth:
            paddleX += paddleSpeed

    if not game_over:
        # Move circle
        circleY += circleDy

        # Ball missed -> Game Over
        if circleY - circleRadius > HEIGHT:
            game_over = True
            

        # Collision with paddle
        if (paddleY < circleY + circleRadius < paddleY + paddleHeight) and (paddleX < circleX < paddleX + paddleWidth):
            score += 1
            circleY = 0
            circleX = random.randint(circleRadius, WIDTH - circleRadius)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (circleX, circleY), circleRadius)
    pygame.draw.rect(screen, GREEN, (paddleX, paddleY, paddleWidth, paddleHeight))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:
        over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)  # FPS
    
pygame.quit()
sys.exit()
