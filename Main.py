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
import database
import registor


pygame.init()


MENU.current_menu = MENU.main_menu
game_running = True
screen = GUI.screen


lava_cap = 250
lava_multiplyer = 40

def load_game(lava_cap, lava_multiplyer):
    global player, wall_rects, spike_rects, coin_rects, lava, group, spawn_cords

    tmx_data = load_map.tmx_data
    spawn_cords = handle_map_collisions.get_spawn_cords(tmx_data)

    player = player_.Player(spawn_cords[0], spawn_cords[1])

    wall_rects = handle_map_collisions.wall_collisions(tmx_data)

    spike_rects = handle_map_collisions.spike_collisions(tmx_data)

    lava = lava_sprite.Lava(0, (spawn_cords[0], spawn_cords[1] + 100))

    # when game restarts lava object is recreated so to keep the same diffuclity pre-set
    # the attibutes must be set to the global variables

    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    lava.layer = 3

    group = pyscroll.PyscrollGroup(
        map_layer=load_map.map_layer,
        default_layer=1
    )

    player.layer = 1
    group.add(player)
    group.add(lava)

    coin_rects = handle_map_collisions.create_coins(tmx_data)

    for coin in coin_rects:
        group.add(coin)



# start game with medium pre-set
load_game(lava_cap, lava_multiplyer)

# special menu objects


def register_command():
    window = registor.Window()
    window.window.mainloop()

    if window.is_logged_in:
        player.username = window.username
        player.user_id = window.user_id

        scores = database.collect_scores(player.user_id)
        player.recent_score = scores[0]
        player.high_score = scores[1]

        display_recent_score.text = f"Your recent score: {str(player.recent_score)}"
        display_high_score.text = f"Your High score: {str(player.high_score)}"


mode_text = (GUI.Label((1280 / 2) + 600, 600, "Grand9K Pixel.ttf", f"Currently in {player.diffuclity_mode} mode", 20,
                     "yellow"))

MENU.options_menu.add_element(mode_text)

def easy_diffuculty_button():
    global lava_cap, lava_multiplyer
    lava_cap = 200
    lava_multiplyer = 30
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    player.diffuclity_mode = "Easy"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Reload the menu so to see the update, this is stupid
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True


def medium_diffuculty_button():
    global lava_cap, lava_multiplyer
    lava_cap = 250
    lava_multiplyer = 40
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    player.diffuclity_mode = "Medium"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Reload the menu so to see the update, this is stupid
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True


def hard_diffuculty_button():
    global lava_cap, lava_multiplyer
    lava_cap = 300
    lava_multiplyer = 50
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    player.diffuclity_mode = "Hard"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Reload the menu so to see the update, this is stupid
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True


display_recent_score = (GUI.Label((1280 / 2) + 1200, 650
                                  , "Grand9K Pixel.ttf", f"Your recent score: {str(player.recent_score)}", 20, "yellow"))


MENU.main_menu.add_element(display_recent_score)

display_high_score = (GUI.Label((1280 / 2) + 1200, 750
                                  , "Grand9K Pixel.ttf", "Login to see your high score", 20, "yellow"))


MENU.main_menu.add_element(display_high_score)


registor_button = (GUI.Button((1280 / 2) - 100, 600, "Grand9K Pixel.ttf", "Register Player", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, register_command))

MENU.leaderboard_menu.add_element(registor_button)

MENU.options_menu.add_element(GUI.Button((1280 / 2) - 400, 200, "Grand9K Pixel.ttf", "Easy Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, easy_diffuculty_button))

MENU.options_menu.add_element(GUI.Button((1280 / 2) - 100, 200, "Grand9K Pixel.ttf", "Medium Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, medium_diffuculty_button))

MENU.options_menu.add_element(GUI.Button((1280 / 2) + 200, 200, "Grand9K Pixel.ttf", "Hard Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, hard_diffuculty_button))





clock = pygame.time.Clock()
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")

start_game_loop = False

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
                # indicative of the play button being pressed
                InGameMenuObjects.game_state_menu.isLoaded = True
                start_game_loop = True

            elif MENU.current_menu == IN_GAME_MENU.pause_menu:
                # pause menu stops the game
                start_game_loop = False



            elif MENU.current_menu == "Start MainMenu":
                # game over or restarted
                load_game(lava_cap, lava_multiplyer)
                start_game_loop = False
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True


        # game logic, when game is running.
    if start_game_loop is True:

        group.update(dt)
        group.center(player.rect.center)
        group.draw(screen)

        keys = pygame.key.get_pressed()

        IN_GAME_MENU.set_score(player.score)

        if (player.pos != spawn_cords):
            # only grows the lava if the player has pressed a key
            # which is the say that the player is at the spawn position
            lava.update_size(dt)
            lava.update_rate(dt)

        player.update_score(coin_rects, group)
        player.check_player_living(lava.rect, spike_rects)

        if not player.moving:
            player.set_direction(keys)

        player.move_and_collide(dt, wall_rects)

        if not player.living:
            screen.fill("black")
            start_game_loop = False
            MENU.current_menu = IN_GAME_MENU.game_over_menu
            display_recent_score.text = f"Your recent score: {str(player.recent_score)}"
            IN_GAME_MENU.game_over_menu.isLoaded = True
            load_game(lava_cap, lava_multiplyer)

    MENU.current_menu.render()

    pygame.display.flip()


pygame.quit()








