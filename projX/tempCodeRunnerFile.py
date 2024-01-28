import pygame
import numpy as np

# in game variables
fps = 60
screen_x = 800
screen_y = 600
run = True 

# Game Window
pygame.init()
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("3D cube")
clock = pygame.time.Clock()