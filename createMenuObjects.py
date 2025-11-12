import pygame
import registor
import GUI
import InGameMenuObjects
import database


# Create diffrent menus
main_menu = GUI.Menu(True)
current_menu = main_menu

options_menu = GUI.Menu(False)
leaderboard_menu = GUI.Menu(False)

# Helper functsions for diffrent button commands
def play_button_command():
    # No more menus :)
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
    current_menu.isLoaded = False
    main_menu.isLoaded = True
    new_menu = main_menu

    return new_menu

def register_command():
    return registor.create_window()

recent_score = 0

# main menu items
main_menu.add_element(GUI.Button((1280 / 2) - 100, 200, "Grand9K Pixel.ttf", "Play", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, play_button_command))

main_menu.add_element(GUI.Label((1280 / 2) + 650, 150, "Grand9K Pixel.ttf", "Tomb Of The Mask", 100,
                            "yellow"))

main_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "By Saleh Faiz", 10,
                            "yellow"))

main_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", f"your recent score: {recent_score}", 10,
                            "yellow"))

main_menu.add_element(GUI.Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "See Leaderboard", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, load_leaderboard_menu_command))

main_menu.add_element(GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Options", "yellow",
                             "#FFFFC5", 200, 50, "black", 20, load_optsion_menu_command))

main_menu.add_element(GUI.Button((1280 / 2) - 100, 500, "Grand9K Pixel.ttf", "Quit", "red",
                             "#FFFFC5", 200, 50, "black", 20, pygame.quit))

# Back button declaratsion
back_button = GUI.Button((1280 / 2) - 100, 500, "Grand9K Pixel.ttf", "Back", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, back_button_command)


options_menu.add_element(back_button)
leaderboard_menu.add_element(back_button)

# optsion menu items
options_menu.add_element(GUI.Label((1280 / 2) + 650, 200, "Grand9K Pixel.ttf", "Change setting here", 32, "yellow"))


#leaderbaord menu items

leaderboard_menu.add_element(GUI.Label((1280 / 2) + 650, 200, "Grand9K Pixel.ttf", "Leaderboard", 32,
                            "yellow"))

leaderboard_menu.add_element(GUI.Label((1280 / 2) + 400, 350, "Grand9K Pixel.ttf", "Username", 17,
                            "yellow"))

leaderboard_menu.add_element(GUI.Label((1280 / 2) + 900, 350, "Grand9K Pixel.ttf", "Highscore", 17,
                            "yellow"))


db = database.collect_leaderboard_data()

lb_range = 0

if len(db) < 5:
    lb_range = len(db)+1
else:
    lb_range = 6


for i in range(1, lb_range):
    count = str(i)
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 200, 400 + (i*100), "Grand9K Pixel.ttf", count, 17,
                                "yellow"))


    # usernames
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 400, 400 + (i*100), "Grand9K Pixel.ttf", (db[i-1][0]), 17,
                                "yellow"))

    # scores
    leaderboard_menu.add_element(GUI.Label((1280 / 2) + 900, 400 + (i*100), "Grand9K Pixel.ttf", (str(db[i-1][1])), 17,
                                "yellow"))


leaderboard_menu.add_element(GUI.Button((1280 / 2) - 100, 600, "Grand9K Pixel.ttf", "Register Player", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, register_command))
