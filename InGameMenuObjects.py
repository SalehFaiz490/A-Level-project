import GUI



game_state_menu = GUI.Menu(False)
pause_menu = GUI.Menu(False)
game_over_menu = GUI.Menu(False)


def activate_pause_menu():
    """
    Change current menu to pause menu, returns pause menu
    Unloads game_state_menu

    """
    game_state_menu.isLoaded = False
    pause_menu.isLoaded = True

    return pause_menu


def deactivate_pause_menu():
    """
    Reloads the game_state_menu and unloads the pause menu
    Current menu is now game_state_menu and is returned

    """
    pause_menu.isLoaded = False
    game_state_menu.isLoaded = True

    return game_state_menu

def return_to_main_menu():
    """

    Unloads the game over menu

    """
    game_over_menu.isLoaded = False


# Create pause button and add it to game state menu
game_state_menu.add_element(GUI.Button(1220, 0, "seguisym.ttf", "⚙️", "#00000000",
                                       "#FFFFC5", 50, 50, "#808080", 70, activate_pause_menu))

# Create Resume playing button and add it to pause menu
pause_menu.add_element(GUI.Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "Resume Playing", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, deactivate_pause_menu))

# Create exit to main menu button and add it to pause menu
exit_to_main_menu_button = (GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Exit to main menu", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, None))

pause_menu.add_element(exit_to_main_menu_button)

# Create "Game is paused" label and add it to pause menu
pause_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "Game is paused", 50,
                            "yellow"))

# declare score label
score_label = GUI.Label(1220, 30, "Grand9K Pixel.ttf", "Score: ", 30, "yellow")

# add score label to game_state_mene
game_state_menu.add_element(score_label)

# This function is called in main to update score
# It is needed to acess player.score outside main
def set_score(score):
    """
    Configures score label to new score

    Args:
        score: set in main to player.score to update score in real time

    """
    score_label.text = f"Score: {str(score)}"


# game over menu declratsiion
game_over_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "GAME OVER", 100,
                            "red"))

# re-add the score label to the gave over menu
game_over_menu.add_element(score_label)

# Adjust y pos of exit to main menu button then add it to game over menu
exit_to_main_menu_button.y_pos = 600
game_over_menu.add_element(exit_to_main_menu_button)
