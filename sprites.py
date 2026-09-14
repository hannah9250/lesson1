import pygame

import random

# Initialize Pygame

pygame.init()

# Create the game window

WIDTH = 800

HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sprite Collision Game")

# Create a clock to control the game speed

clock = pygame.time.Clock()

# Create the player

player = pygame.Rect(100, 250, 50, 50)

# Create the target

target = pygame.Rect(

random.randint(100, 700),

random.randint(100, 500),

40,

40

)

# Create a font

font = pygame.font.SysFont("Arial", 60)

# Initially, the player has not won

won = False

# Game loop

running = True

while running:

# Check events

   for event in pygame.event.get():

# Close the game

if event.type == pygame.QUIT:

running = False

# Get keyboard input

keys = pygame.key.get_pressed()

# Move the player

if keys[pygame.K_LEFT]:

player.x -= 5

if keys[pygame.K_RIGHT]:

player.x += 5

if keys[pygame.K_UP]:

player.y -= 5

if keys[pygame.K_DOWN]:

player.y += 5

# Keep the player inside the screen

player.x = max(0, min(player.x, WIDTH - player.width))

player.y = max(0, min(player.y, HEIGHT - player.height))

# Check for collision

if player.colliderect(target):

won = True

# Draw the background

screen.fill((30, 30, 30))

# Draw the player

pygame.draw.rect(screen, (0, 100, 255), player)

# Draw the target if the player has not won

if not won:

pygame.draw.rect(screen, (255, 200, 0), target)

# Display winning message

if won:

text = font.render("YOU WIN!", True, (255, 255, 255))

# Find the center position

x = (WIDTH - text.get_width()) // 2

y = (HEIGHT - text.get_height()) // 2

# Display the message

screen.blit(text, (x, y))

# Update the display

pygame.display.flip()

# Keep the game running at 60 FPS

clock.tick(60)

# Close Pygame

pygame.quit()