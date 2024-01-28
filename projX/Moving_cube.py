import pygame
from pygame.locals import *
import numpy as np
fps = 60
# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Cube")
clock = pygame.time.Clock()
# Define the vertices of a 3D cube
vertices = np.array([[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1], [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]])

# Define the edges of the cube
edges = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]])

# Define the initial position and rotation of the cube
x_angle, y_angle = 0, 0
x_pos, y_pos, z_pos = 0, 0, 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate and translate the cube
    rot_matrix = np.array([[1, 0, 0], [0, np.cos(x_angle), -np.sin(x_angle)], [0, np.sin(x_angle), np.cos(x_angle)]])
    rot_matrix = rot_matrix @ np.array([[np.cos(y_angle), 0, np.sin(y_angle)], [0, 1, 0], [-np.sin(y_angle), 0, np.cos(y_angle)]])
    rot_matrix = rot_matrix.T
    transformed_vertices = np.array([np.dot(rot_matrix, vertex) + np.array([x_pos, y_pos, z_pos]) for vertex in vertices])
    
    # Project the 3D coordinates onto 2D screen coordinates
    screen_coords = np.array([[400 + int(vertex[0]*100), 300 + int(vertex[1]*100)] for vertex in transformed_vertices])
    
    # Draw the edges of the cube
    for edge in edges:
        pygame.draw.line(screen, (255, 255, 255), screen_coords[edge[0]], screen_coords[edge[1]])

    # Update the angle and position of the cube
    x_angle += 0.05
    y_angle += 0.03
    # x_pos += 0.01
    # y_pos += 0.02
    # z_pos += 0.03

    # Update the display
    pygame.display.flip()

    # Wait for a while
    pygame.time.wait(10)

    clock.tick(fps)

# Close the Pygame window
