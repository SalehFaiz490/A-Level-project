import GUI



game_state_menu = GUI.Menu(False)
pause_menu = GUI.Menu(False)
game_over_menu = GUI.Menu(False)


def activate_pause_menu():
    game_state_menu.isLoaded = False
    pause_menu.isLoaded = True

    return pause_menu


def deactivate_pause_menu():
    pause_menu.isLoaded = False
    game_state_menu.isLoaded = True

    return game_state_menu

def return_to_main_menu():
    game_over_menu.isLoaded = False





game_state_menu.add_element(GUI.Button(1220, 0, "seguisym.ttf", "⚙️", "#00000000",
                                       "#FFFFC5", 50, 50, "#808080", 70, activate_pause_menu))

pause_menu.add_element(GUI.Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "Resume Playing", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, deactivate_pause_menu))

exit_to_main_menu_button = (GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Exit to main menu", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, None))

pause_menu.add_element(exit_to_main_menu_button)

pause_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "Game is paused", 50,
                            "yellow"))

score_label = GUI.Label(1220, 30, "Grand9K Pixel.ttf", "Score: ", 30, "yellow")

game_state_menu.add_element(score_label)

def set_score(score):
    score_label.text = f"Score: {str(score)}"



# game over menu declratsiion

game_over_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "GAME OVER", 100,
                            "red"))

#score_label.x_pos, score_label.y_pos = 1300, 500
game_over_menu.add_element(score_label)

exit_to_main_menu_button.y_pos = 600
game_over_menu.add_element(exit_to_main_menu_button)
