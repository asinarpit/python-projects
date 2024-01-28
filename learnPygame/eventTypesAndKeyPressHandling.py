import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game - Blank")

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True    #game exit kr dega 

        if event.type == pygame.KEYDOWN:                  #ye syntax follow krna hai direct event.key
            if event.key == pygame.K_RIGHT:               #error throw krega
                print("You have pressed right arrow key")

pygame.quit()
quit()
