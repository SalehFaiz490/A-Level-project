import pygame
import main_menu

pygame.init()

start = main_menu.run_menus()
# returns true when the player presses play button

if start:

    game_running = True
    clock = pygame.time.Clock()
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Game")
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        screen.fill((0, 0, 0))

        pygame.display.flip()

        clock.tick(60)




else:
    pass

pygame.quit()












