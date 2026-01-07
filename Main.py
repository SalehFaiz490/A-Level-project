import pygame
import GUI
import InGameMenuObjects
import createMenuObjects as MENU
import InGameMenuObjects as IN_GAME_MENU
import player_
import load_map
import pyscroll
import handle_map_collisions
import lava_sprite


pygame.init()


MENU.current_menu = MENU.main_menu
game_running = True
screen = GUI.screen

def load_game():
    global player, wall_rects, spike_rects, coin_rects, lava, group

    tmx_data = load_map.tmx_data
    spawn_cords = handle_map_collisions.get_spawn_cords(tmx_data)

    player = player_.Player(spawn_cords[0], spawn_cords[1])

    wall_rects = handle_map_collisions.wall_collisions(tmx_data)
    spike_rects = handle_map_collisions.spike_collisions(tmx_data)

    coin_rects = handle_map_collisions.coin_collisions(tmx_data)

    lava = lava_sprite.Lava(0, (spawn_cords[0], spawn_cords[1] + 100))
    print(type(lava))
    lava.layer = 3
    group = pyscroll.PyscrollGroup(
        map_layer=load_map.map_layer,
        default_layer=1
    )

    player.layer = 1
    group.add(player)
    group.add(lava)

    for coin in coin_rects:
        group.add(coin)


load_game()

clock = pygame.time.Clock()
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")

start_game_loop = False
dir_collide = None
wall_rect = None


while game_running:

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
                start_game_loop = True

            elif MENU.current_menu == IN_GAME_MENU.pause_menu:
                # pause menu stops the game
                start_game_loop = False



            elif MENU.current_menu == "Start MainMenu":
                # game over or restarted
                load_game()
                start_game_loop = False
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True


        # game logic
    if start_game_loop is True:

        keys = pygame.key.get_pressed()

        IN_GAME_MENU.set_score(player.score)

        group.update(dt)
        group.center(player.rect.center)
        group.draw(screen)

        lava.update_size(dt)
        lava.update_rate(dt)

        player.update_score(coin_rects, group)
        player.check_player_living(lava.rect, spike_rects)

        if not player.moving:
            player.set_direction(keys, screen)

        player.move_and_collide(dt, wall_rects)

        if not player.living:
            screen.fill("black")
            start_game_loop = False
            MENU.current_menu = IN_GAME_MENU.game_over_menu
            IN_GAME_MENU.game_over_menu.isLoaded = True
            load_game()

    MENU.current_menu.render()

    pygame.display.flip()


pygame.quit()








