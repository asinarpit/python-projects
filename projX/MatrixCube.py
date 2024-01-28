import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Matrix Cube")

# Create a 2D list to represent the cube
cube = [[0 for x in range(5)] for y in range(5)]

# Create a function to draw the cube
def draw_cube():
    for y, row in enumerate(cube):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(screen, (0, 255, 0), (x*100, y*100, 100, 100))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click hit a cube
            x, y = event.pos
            x //= 100
            y //= 100
            if 0 <= x < 5 and 0 <= y < 5:
                cube[y][x] ^= 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the cube
    draw_cube()

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()
