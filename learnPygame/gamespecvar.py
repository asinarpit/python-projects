import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Game specific variables
exit_game = False #returns true when player quit the game 
game_over = False  #returns true when the 'game over'

