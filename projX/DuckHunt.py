import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Duck Hunt")

# Load the images for the game
duck_image = pygame.image.load("duck.png")
gun_image = pygame.image.load("gun.png")

# Create a duck object
duck_rect = duck_image.get_rect(center=(350, 250))

# Create a gun object
gun_rect = gun_image.get_rect(center=(350, 450))

# Create a font for the score
font = pygame.font.Font(None, 30)

# Set the initial score
score = 0

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the duck was hit
            if duck_rect.collidepoint(event.pos):
                score += 1
                # Move the duck to a random position
                duck_rect.center = (random.randint(0, size[0]), random.randint(0, size[1]))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the duck
    screen.blit(duck_image, duck_rect)

    # Draw the gun
    screen.blit(gun_image, gun_rect)

    # Draw the score
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()
