# Python Snake Game

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define screen size and title
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Snake Game")

# Define clock and FPS
clock = pygame.time.Clock()
FPS = 10

# Define snake size and speed
snake_size = 20
snake_speed = 20

# Define snake head and body
snake_head = [200, 200]
snake_body = [[200, 200], [180, 200], [160, 200]]

# Define food position and score
food_x = random.randrange(0, screen_width - snake_size, snake_speed)
food_y = random.randrange(0, screen_height - snake_size, snake_speed)
food_pos = [food_x, food_y]
score = 0

# Define game over flag and font
game_over = False
font = pygame.font.SysFont("Arial", 40)

# Define direction flag
direction = "RIGHT"
change_to = direction

# Define a function to show score
def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Define a function to show game over message
def game_over_message():
    game_over_text_1 = font.render("Game Over!", True, WHITE)
    game_over_text_2 = font.render("Press Q to Quit or R to Restart", True, WHITE)
    screen.blit(game_over_text_1, [300, 250])
    screen.blit(game_over_text_2, [200, 300])

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handle key presses
        if event.type == pygame.KEYDOWN:
            # Quit game
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            # Restart game
            if event.key == pygame.K_r:
                snake_head = [200, 200]
                snake_body = [[200, 200], [180, 200], [160, 200]]
                food_x = random.randrange(0, screen_width - snake_size, snake_speed)
                food_y = random.randrange(0, screen_height - snake_size, snake_speed)
                food_pos = [food_x, food_y]
                score = 0
                direction = "RIGHT"
                change_to = direction
                game_over = False
            # Change direction
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"

    # Validate direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Update snake head position
    if direction == "UP":
        snake_head[1] -= snake_speed
    if direction == "DOWN":
        snake_head[1] += snake_speed
    if direction == "LEFT":
        snake_head[0] -= snake_speed
    if direction == "RIGHT":
        snake_head[0] += snake_speed

    # Check if snake is out of bounds
    if snake_head[0] < 0 or snake_head[0] > screen_width - snake_size:
        game_over = True
    if snake_head[1] < 0 or snake_head[1] > screen_height - snake_size:
        game_over = True

    # Check if snake eats food
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        # Generate new food position and increase score
        food_x = random.randrange(0, screen_width - snake_size, snake_speed)
        food_y = random.randrange(0, screen_height - snake_size, snake_speed)
        food_pos = [food_x, food_y]
        score += 1
        # Grow snake body
        snake_body.append([0, 0])
    
    # Check if snake collides with itself
    for block in snake_body[:-1]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            game_over = True

    # Update snake body position
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i][0] = snake_body[i - 1][0]
        snake_body[i][1] = snake_body[i - 1][1]
    snake_body[0][0] = snake_head[0]
    snake_body[0][1] = snake_head[1]

    # Fill screen with black color
    screen.fill(BLACK)

    # Draw snake body
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])

    # Draw food
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], snake_size, snake_size])

    # Show score
    show_score()

    # Show game over message
    if game_over:
        game_over_message()

    # Update screen
    pygame.display.update()

    # Set FPS
    clock.tick(FPS)
