import pygame
import GUI
import InGameMenuObjects
import createMenuObjects as MENU
import InGameMenuObjects as IN_GAME_MENU
import player_
import load_map
import pyscroll


pygame.init()


MENU.current_menu = MENU.main_menu
game_running = True
screen = GUI.screen

player = player_.Player(200, 200 )

clock = pygame.time.Clock()
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")

group = pyscroll.PyscrollGroup(map_layer=load_map.map_layer, default_layer=0)
player.layer = 0
group.add(player)
start_game = False


while game_running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break

        if MENU.current_menu.handle_events(event) is not None:
            MENU.current_menu = MENU.current_menu.handle_events(event)
            # this sets the current menu to the command_code to switch between menus

            if MENU.current_menu == IN_GAME_MENU.game_state_menu:
                InGameMenuObjects.game_state_menu.isLoaded = True
                start_game = True

            elif MENU.current_menu == "Start MainMenu":
                start_game = False
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True
                screen.fill((0, 0, 0))

        if start_game is True:
            group.update(dt, pygame.key.get_pressed())
            group.center(player.rect.center)
            group.draw(screen)

    MENU.current_menu.render()


    pygame.display.flip()

    clock.tick(60)

else:
    pass

pygame.quit()








