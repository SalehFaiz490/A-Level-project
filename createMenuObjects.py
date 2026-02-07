import pygame
import GUI
import InGameMenuObjects
import database



# Create diffrent menus

main_menu = GUI.Menu(True)
current_menu = main_menu

options_menu = GUI.Menu(False)
leaderboard_menu = GUI.Menu(False)
help_menu = GUI.Menu(False)


# Helper functsions for diffrent button commands
def play_button_command():
    # Main menu unloaded, in game menu loaded
    main_menu.isLoaded = False
    current_menu = InGameMenuObjects.game_state_menu

    return current_menu


def load_optsion_menu_command():
    # unload main menu then load optsions menu then switch current menu
    main_menu.isLoaded = False
    options_menu.isLoaded = True
    current_menu = options_menu

    return current_menu


def load_leaderboard_menu_command():
    # unload main menu then load leaderboard menu then switch current menu
    main_menu.isLoaded = False
    leaderboard_menu.isLoaded = True
    current_menu = leaderboard_menu

    return current_menu


def back_button_command():
    # unloads the current menu
    current_menu.isLoaded = False
    # back button will always return the user to main menu
    # so load main menu
    main_menu.isLoaded = True
    # the new menu is the main menu
    # cannot use current menu here as will override above logic
    new_menu = main_menu

    return new_menu

def load_help_menu():

    # unload the options menu, loads the help menu
    options_menu.isLoaded = False
    help_menu.isLoaded = True
    current_menu = help_menu

    return current_menu







recent_score = 0

# main menu items

# play button
main_menu.add_element(GUI.Button((1280 / 2) - 100, 200, "Grand9K Pixel.ttf", "Play", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, play_button_command))

# Tomb of the mask label
main_menu.add_element(GUI.Label((1280 / 2) + 650, 150, "Grand9K Pixel.ttf", "Tomb Of The Mask", 100,
                            "yellow"))


# By Saleh Faiz label
main_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "By Saleh Faiz", 10,
                            "yellow"))

# See leaderboard button
main_menu.add_element(GUI.Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "See Leaderboard", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, load_leaderboard_menu_command))

# Options button
main_menu.add_element(GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Options", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, load_optsion_menu_command))

# Quit button
main_menu.add_element(GUI.Button((1280 / 2) - 100, 500, "Grand9K Pixel.ttf", "Quit", "red",
                             "#FFFFC5", 200, 50, "black", 20, pygame.quit))

# Back button declaratsion
back_button = GUI.Button((1280 / 2) - 100, 500, "Grand9K Pixel.ttf", "Back", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, back_button_command)

# Add the back button to the diffrent menus
options_menu.add_element(back_button)

leaderboard_menu.add_element(back_button)

# Options menu items

# Settings label
options_menu.add_element(GUI.Label((1280 / 2) + 650, 200, "Grand9K Pixel.ttf", "Change setting here", 32, "yellow"))


# See help menu button
options_menu.add_element(GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "See Help Menu!", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, load_help_menu))

# help menu items

# declare the help back button, must have a diffrent y pos than defult back button
help_menu_back_button = GUI.Button((1280 / 2) - 100, 600, "Grand9K Pixel.ttf", "Back", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, back_button_command)

help_menu.add_element(help_menu_back_button)


help_string = """"
            ────────────── HELP ───────────────
        
            OBJECTIVE
            Reach the highest score possible by
            moving through the map, collecting
            coins, and avoiding hazards.
            
            RULES        
            • The player loses if they collide
              with the lava or a spike.
            • Coins increase the player’s score.
            • The game ends when the player
              dies.
            
            CONTROLS
            
            w   Move Up
            a   Move Down
            s   Move Left
            d   Move Right

            
            TIP
            Plan your movement carefully and
            react quickly to survive longer.
            ──────────────────────────────────
            """

# Create the help label
help_menu.add_element(GUI.Label((1280 / 2) + 650, 600, "seguisym.ttf", help_string, 15, "yellow"))



#leaderbaord menu items

# Leaderboard label
leaderboard_menu.add_element(GUI.Label((1280 / 2) + 650, 200, "Grand9K Pixel.ttf", "Leaderboard", 32,
                            "yellow"))

# Usernames label
leaderboard_menu.add_element(GUI.Label((1280 / 2) + 400, 350, "Grand9K Pixel.ttf", "Usernames", 17,
                            "yellow"))

# Highscores label
leaderboard_menu.add_element(GUI.Label((1280 / 2) + 900, 350, "Grand9K Pixel.ttf", "Highscores", 17,
                            "yellow"))

# Collect the leaderboard from DB
db_data = database.collect_leaderboard_data()


lb_range = 0

# determine the number of players shown in leaderboard, 5 is max
if len(db_data) < 5:
    lb_range = len(db_data) + 1
else:
    lb_range = 6

# Create username and score lables for top players in leaderboard.

for i in range(1, lb_range):
    count = str(i)
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 200, 400 + (i*100), "Grand9K Pixel.ttf", count, 17,
                                "yellow"))

    # Usernames
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 400, 400 + (i*100), "Grand9K Pixel.ttf", (db_data[i - 1][0]), 17,
                                "yellow"))

    # Scores
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 900, 400 + (i*100), "Grand9K Pixel.ttf", (str(db_data[i - 1][1])), 17,
                                "yellow"))



