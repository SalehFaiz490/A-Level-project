import pygame
import GUI
import InGameMenuObjects
import createMenuObjects as MENU
import InGameMenuObjects as IN_GAME_MENU


pygame.init()


MENU.current_menu = MENU.main_menu
game_running = True
screen = GUI.screen

clock = pygame.time.Clock()
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break

        if MENU.current_menu.handle_events(event) is not None:
            MENU.current_menu = MENU.current_menu.handle_events(event)

            if MENU.current_menu == IN_GAME_MENU.game_state_menu:
                InGameMenuObjects.game_state_menu.isLoaded = True

            if MENU.current_menu == "Start MainMenu":
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True



    screen.fill((0, 0, 0))

    MENU.current_menu.render()
    pygame.display.flip()

    clock.tick(60)

else:
    pass

pygame.quit()








