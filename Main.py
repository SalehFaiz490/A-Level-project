import pygame
import GUI
import InGameMenuObjects
import createMenuObjects as MENU
import InGameMenuObjects as IN_GAME_MENU
import player_
import load_map
import pyscroll
import handle_map_collisions


pygame.init()


MENU.current_menu = MENU.main_menu
game_running = True
screen = GUI.screen


tmx_data = load_map.tmx_data

spawn_crods = handle_map_collisions.get_spawn_cords(tmx_data)
player = player_.Player(spawn_crods[0], spawn_crods[1])

wall_rects = handle_map_collisions.wall_collisions(tmx_data)
coins = handle_map_collisions.coin_collisions(tmx_data)


clock = pygame.time.Clock()
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")



map_layer = load_map.map_layer
group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
player.layer = 1
group.add(player)

for coin in coins:
    group.add(coin)

start_game = False
dir_collide = None
wall_rect = None




while game_running:

    camera_offset = player.rect.center - pygame.Vector2(1280 // 2, 704 // 2)

    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break

        action = MENU.current_menu.handle_events(event)
        if action is not None:
            screen.fill((0, 0, 0))
            MENU.current_menu = action
            # this sets the current menu to the command_code to switch between menus

            if MENU.current_menu == IN_GAME_MENU.game_state_menu:
                InGameMenuObjects.game_state_menu.isLoaded = True
                start_game = True

            elif MENU.current_menu == IN_GAME_MENU.pause_menu:
                # pause menu stops the game
                start_game = False

            elif MENU.current_menu == "Start MainMenu":
                start_game = False
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True
                screen.fill((0, 0, 0))


        # game logic
    if start_game is True:

        keys = pygame.key.get_pressed()

        IN_GAME_MENU.set_score(player.score)

        group.update(dt)
        group.center(player.rect.center)
        group.draw(screen)

        player.update_score(coins, group)

        if not player.moving:
            player.set_direction(keys)

        player.move_and_collide(dt, wall_rects)

    MENU.current_menu.render()

    pygame.display.flip()


pygame.quit()








