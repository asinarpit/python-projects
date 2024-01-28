import pygame
import math

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Interactive Moving Eye")

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

# Set the initial position of the pupil
pupil_rect = pygame.Rect(40, 40, 20, 20)

# Set the initial position of the iris
iris_rect = pygame.Rect(35, 35, 30, 30)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Calculate the angle between the center of the eye and the mouse
    angle = math.atan2(mouse_pos[1] - eye_rect.centery, mouse_pos[0] - eye_rect.centerx)

    # Move the pupil and iris according to the angle
    pupil_rect.center = (
        eye_rect.centerx + math.cos(angle) * 20,
        eye_rect.centery + math.sin(angle) * 20
    )
    iris_rect.center = (
        eye_rect.centerx + math.cos(angle) * 35,
        eye_rect.centery + math.sin(angle) * 35
    )

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the eye
    screen.blit(eye_image, eye_rect)

    # Draw the iris
    pygame.draw.circle(screen, (0, 0, 0), iris_rect.center, iris_rect.width//2)

    # Draw the pupil
    pygame.draw.circle(screen, (0, 0, 0), pupil_rect.center, pupil_rect.width//2)

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()
