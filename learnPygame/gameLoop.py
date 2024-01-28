

import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:    #it will show not responding as the events are not handled for now and the loop is infinite 
    pass

pygame.quit()   #game loop ke end hote hi game ko quit krdega 
quit()          


