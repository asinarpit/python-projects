import pygame

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Eye Following Cursor")

# Create a surface for the eye
eye_image = pygame.Surface((100, 100))

# Fill the surface with white
eye_image.fill((255, 255, 255))

# Draw the iris of the eye as a black circle
pygame.draw.circle(eye_image, (0, 0, 0), (50, 50), 30)

# Draw the pupil of the eye as a smaller black circle
pygame.draw.circle(eye_image, (0, 0, 0), (50, 50), 10)

# Set the initial position of the eye
eye_rect = eye_image.get_rect(center=(350, 250))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Update the position of the eye to match the cursor's position
    eye_rect.center = mouse_pos

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the eye
    screen.blit(eye_image, eye_rect)

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()
