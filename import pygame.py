import pygame

import random

# ініціалізувати Pygame

pygame.init()

# розміри вікна

width = 600

height = 600

# кольори

white = (255, 255, 255)

black = (0, 0, 0)

# створити вікно

screen = pygame.display.set_mode((width, height))

# розміри комірки

cell_size = 20

# розміри лабіринту

rows = height // cell_size

cols = width // cell_size

# створити порожній лабіринт

maze = [[{'left': True, 'right': True, 'up': True, 'down': True} for j in range(cols)] for i in range(rows)]

# встановити стіни на першому рядку та першому стовпці

for i in range(rows):

maze[i][0]['left'] = False

maze[i][cols-1]['right'] = False

for j in range(cols):

maze[0][j]['up'] = False

maze[rows-1][j]['down'] = False

# випадкова початкова комірка

current_cell = (random.randint(0, rows-1), random.randint(0, cols-1))

# стек відвіданих комірок