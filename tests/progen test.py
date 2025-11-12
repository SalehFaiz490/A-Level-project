import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 400))


def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    stack = [(1, 1)]
    maze[1][1] = 0
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()
    return maze


def draw_maze(screen, maze):
    TILE = 20
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = (40, 40, 40) if cell == 1 else (230, 230, 230)
            pygame.draw.rect(screen, color, (x * TILE, y * TILE, TILE, TILE))


maze = generate_maze(20, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_maze(screen, maze)
    pygame.display.flip()

pygame.quit()
