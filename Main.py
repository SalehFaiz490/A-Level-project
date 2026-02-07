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

# start with the main menu loaded
MENU.current_menu = MENU.main_menu

# start main game loop
game_running = True

# initialize the screen
screen = GUI.screen

# Start game at medium mode pre-set
lava_cap = 250
lava_multiplyer = 40

def load_game(lava_cap, lava_multiplyer):
    """
    Initialises and loads all core game objects for a new game session.

    This function:
    - Loads map data and spawn coordinates
    - Creates the player, lava, and collision objects
    - Applies difficulty settings to the lava
    - Adds all relevant sprites to the Pyscroll rendering group

    Args:
        lava_cap (float): Maximum height/speed limit for the lava.
        lava_multiplyer (float): Difficulty scaling factor for lava speed.
    """

    # declare global variables to use them in global scope
    global player, wall_rects, spike_rects, coin_rects, lava, group, spawn_cords

    # Loads TMX map data
    tmx_data = load_map.tmx_data

    # Get starting spawn coordinates from the map
    spawn_cords = handle_map_collisions.get_spawn_cords(tmx_data)

    # Creates player and spawns them as the spawn location
    player = player_.Player(spawn_cords[0], spawn_cords[1])

    # Generates collision rect array from map
    wall_rects = handle_map_collisions.wall_collisions(tmx_data)
    spike_rects = handle_map_collisions.spike_collisions(tmx_data)

    # Create lava slightly below the player's spawn pos
    lava = lava_sprite.Lava(0, (spawn_cords[0], spawn_cords[1] + 100))

    # When game is restarted, lava is recreated.
    # to preserve selected difficulty, its attributes must be reinstated
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    # set lava rendering above all other layers
    lava.layer = 3

    # Create the Pyscroll sprite group for rendering and camera handling
    group = pyscroll.PyscrollGroup(
        map_layer=load_map.map_layer,
        default_layer=1
    )

    # Set player rendering layer and add sprites to the group
    player.layer = 1
    group.add(player)
    group.add(lava)

    # Create coin objects from the map and add them to the group
    coin_rects = handle_map_collisions.create_coins(tmx_data)
    for coin in coin_rects:
        group.add(coin)



# start game with medium pre-set
load_game(lava_cap, lava_multiplyer)

# special menu objects


def register_command():
    """
    Opens the registration/login window and updates the current player
    with account and score data upon successful authentication.

    If the user logs in successfully:
    - Player account details are stored
    - Previous scores are retrieved from the database
    - UI elements are updated to reflect the player's stats

    """

    # Create and display the registration/login window
    window = registor.Window()
    window.window.mainloop()

    # Continue only if the user successfully logged in
    if window.is_logged_in:
        # Store authenticated user details in the player object
        player.username = window.username
        player.user_id = window.user_id

        # Retrieve recent and high scores from the database
        scores = database.collect_scores(player.user_id)
        player.recent_score = scores[0]
        player.high_score = scores[1]

        # Update on-screen text to display player statistics
        display_recent_score.text = (
            f"Your recent score: {player.recent_score}"
        )
        display_high_score.text = (
            f"Your High score: {player.high_score}"
        )


# create label to show current game difficulty
mode_text = (GUI.Label((1280 / 2) + 600, 600, "Grand9K Pixel.ttf",
                       f"Currently in {player.diffuclity_mode} mode", 20,
                     "yellow"))

# Add above label to the optsions menu
MENU.options_menu.add_element(mode_text)

def easy_diffuculty_button():
    """
    Applies the 'Easy' difficulty preset by configuring lava behaviour
    and updating the UI to reflect the selected difficulty.
    """

    # Declare global difficulty variables so they persist across reloads
    global lava_cap, lava_multiplyer

    # Set lava difficulty parameters for easy mode
    lava_cap = 200
    lava_multiplyer = 30
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    # Update player difficulty state and on-screen text
    player.diffuclity_mode = "Easy"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Force the menu to reload so the updated difficulty is displayed.
    # This is a workaround due to the menu system not supporting live updates.
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True



def medium_diffuculty_button():
    """
    Applies the 'Medium' difficulty preset by configuring lava behaviour
    and updating the UI to reflect the selected difficulty.
    """

    # Declare global difficulty variables so they persist across reloads
    global lava_cap, lava_multiplyer

    # Set lava difficulty parameters for easy mode
    lava_cap = 250
    lava_multiplyer = 40
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    # Update player difficulty state and on-screen text
    player.diffuclity_mode = "Medium"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Force the menu to reload so the updated difficulty is displayed.
    # This is a workaround due to the menu system not supporting live updates.
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True


def hard_diffuculty_button():
    """
    Applies the 'Hard' difficulty preset by configuring lava behaviour
    and updating the UI to reflect the selected difficulty.
    """

    # Declare global difficulty variables so they persist across reloads
    global lava_cap, lava_multiplyer

    # Set lava difficulty parameters for easy mode
    lava_cap = 300
    lava_multiplyer = 50
    lava.cap = lava_cap
    lava.multplyer = lava_multiplyer

    # Update player difficulty state and on-screen text
    player.diffuclity_mode = "Hard"
    mode_text.text = f"Currently in {player.diffuclity_mode} mode"

    # Force the menu to reload so the updated difficulty is displayed.
    # This is a workaround due to the menu system not supporting live updates.
    MENU.current_menu.isLoaded = False
    screen.fill("black")
    MENU.current_menu.isLoaded = True


# Create a label to show recent score and add it to main menu
display_recent_score = (GUI.Label((1280 / 2) + 1200, 650
                                  , "Grand9K Pixel.ttf",
                                  f"Your recent score: {str(player.recent_score)}", 20, "yellow"))

MENU.main_menu.add_element(display_recent_score)


# Create a label to show high score and add it to main menu
display_high_score = (GUI.Label((1280 / 2) + 1200, 750
                                  , "Grand9K Pixel.ttf", "Login to see your high score", 20, "yellow"))

MENU.main_menu.add_element(display_high_score)

# Create the register button and add it to the leaderboard menu
registor_button = (GUI.Button((1280 / 2) - 100, 600, "Grand9K Pixel.ttf", "Register Player", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, register_command))

MENU.leaderboard_menu.add_element(registor_button)

# Easy button declaration
MENU.options_menu.add_element(GUI.Button((1280 / 2) - 400, 200, "Grand9K Pixel.ttf", "Easy Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, easy_diffuculty_button))

# Medium button declaration
MENU.options_menu.add_element(GUI.Button((1280 / 2) - 100, 200, "Grand9K Pixel.ttf", "Medium Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, medium_diffuculty_button))

# Hard button declaration
MENU.options_menu.add_element(GUI.Button((1280 / 2) + 200, 200, "Grand9K Pixel.ttf", "Hard Mode", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, hard_diffuculty_button))


# Initialise clock to control frame rate
clock = pygame.time.Clock()

# Set up display surface and window title
pygame.display.get_surface()
pygame.display.set_caption("Tomb of the Mask")

# Flag used to control whether gameplay logic should run
start_game_loop = False

# Main application loop
while game_running:

    # Delta time ensures frame-rate independent movement
    dt = clock.tick(60) / 1000.0

    # Handle all input events (keyboard, mouse, window events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break

        # Pass event to the current menu and check for menu actions
        action = MENU.current_menu.handle_events(event)
        if action is not None:
            screen.fill((0, 0, 0))
            MENU.current_menu = action
            # Switch the active menu based on user interaction

            if MENU.current_menu == IN_GAME_MENU.game_state_menu:
                # Play button pressed – start gameplay
                InGameMenuObjects.game_state_menu.isLoaded = True
                start_game_loop = True

            elif MENU.current_menu == IN_GAME_MENU.pause_menu:
                # Pause menu disables gameplay updates
                start_game_loop = False

            elif MENU.current_menu == "Start MainMenu":
                # Game over or restart selected
                # Reload game objects and return to the main menu
                load_game(lava_cap, lava_multiplyer)
                start_game_loop = False
                MENU.current_menu = MENU.main_menu
                MENU.main_menu.isLoaded = True

    # Run core game logic only when the game is active
    if start_game_loop is True:

        # Update and render all game sprites
        group.update(dt)
        group.center(player.rect.center)
        group.draw(screen)

        # Get current keyboard state
        keys = pygame.key.get_pressed()

        # Update in-game score display
        IN_GAME_MENU.set_score(player.score)

        if player.pos != spawn_cords:
            # Lava only increases once the player has moved
            # This prevents instant death at spawn
            lava.update_size(dt)
            lava.update_rate(dt)

        # Update score based on collected coins
        player.update_score(coin_rects, group)

        # Check collisions with lava and spikes
        player.check_player_living(lava.rect, spike_rects)

        # Update player direction if not already moving
        if not player.moving:
            player.set_direction(keys)

        # Move player and resolve wall collisions
        player.move_and_collide(dt, wall_rects)

        if not player.living:
            # Handle player death:
            # - Stop gameplay
            # - Switch to game over menu
            # - Update score display
            # - Reload game state
            screen.fill("black")
            start_game_loop = False
            MENU.current_menu = IN_GAME_MENU.game_over_menu
            display_recent_score.text = (
                f"Your recent score: {player.recent_score}"
            )
            IN_GAME_MENU.game_over_menu.isLoaded = True
            load_game(lava_cap, lava_multiplyer)

    # Render the active menu on top of the game state
    MENU.current_menu.render()

    # Update the display
    pygame.display.flip()

# Cleanly exit pygame
pygame.quit()









