import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Interactive Space Pattern")

# Create a list to store the stars
stars = []

# Create a function to generate random stars
def generate_stars():
    for i in range(1000):
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        stars.append((x, y))

# Create a function to update the stars
def update_stars(speed):
    for i in range(len(stars)):
        x, y = stars[i]
        y += speed
        if y > size[1]:
            y = 0
        stars[i] = (x, y)

# Call the function to generate the initial stars
generate_stars()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current speed of the stars
    speed = pygame.mouse.get_pos()[1] / 500
    update_stars(speed)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the stars
    for x, y in stars:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()
