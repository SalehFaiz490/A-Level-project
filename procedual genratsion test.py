import pygame
import random

#Initialize Pygame
pygame.init()

#Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Procedural Generation in Pygame')

#Define the grid size
width, height = 500, 500
cell_size = 10

#Initialize the grid with random values
grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

#Define the rules for the cellular automaton
def update_grid(grid):
    new_grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            alive_neighbors = sum([grid[(y-1)%height][(x-1)%width], grid[(y-1)%height][x], grid[(y-1)%height][(x+1)%width],
            grid[y][(x-1)%width], grid[y][(x+1)%width],
            grid[(y+1)%height][(x-1)%width], grid[(y+1)%height][x], grid[(y+1)%height][(x+1)%width]])
            if grid[y][x] == 1 and 2 <= alive_neighbors <= 3:
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and alive_neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

#Update the grid for a set number of iterations
for _ in range(5):
    grid = update_grid(grid)

#Main game loop
running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         # Draw the grid
        for y in range(height):
            for x in range(width):
                color = (255, 255, 255) if grid[y][x] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (x, y , cell_size, cell_size))

     # Update the display
     pygame.display.flip()


pygame.quit()
