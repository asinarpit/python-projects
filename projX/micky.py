import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Mickey Mouse")

# Run the game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the head
    pygame.draw.circle(screen, (0, 0, 0), (350, 250), 100)

    # Draw the ears
    pygame.draw.circle(screen, (0, 0, 0), (250, 150), 40)
    pygame.draw.circle(screen, (0, 0, 0), (450, 150), 40)

    # Draw the eyes
    pygame.draw.circle(screen, (255, 255, 255), (300, 200), 20)
    pygame.draw.circle(screen, (255, 255, 255), (400, 200), 20)

    # Draw the pupils
    pygame.draw.circle(screen, (0, 0, 0), (290, 195), 10)
    pygame.draw.circle(screen, (0, 0, 0), (390, 195), 10)

    # Draw the nose
    pygame.draw.circle(screen, (255, 0, 0), (350, 250), 10)

    # Draw the mouth
    pygame.draw.circle(screen, (255, 255, 255), (350, 300), 30, 2)

    # Update the screen
    pygame.display.flip()

# Exit pygame
pygame.quit()
