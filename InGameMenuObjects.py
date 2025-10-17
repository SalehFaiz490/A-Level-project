import GUI


game_state_menu = GUI.Menu(False)
pause_menu = GUI.Menu(False)


def activate_pause_menu():
    game_state_menu.isLoaded = False
    pause_menu.isLoaded = True

    return pause_menu


def deactivate_pause_menu():
    pause_menu.isLoaded = False
    game_state_menu.isLoaded = True

    return game_state_menu


game_state_menu.add_element(GUI.Button(1220, 0, "seguisym.ttf", "⚙️", "#00000000",
                                       "#FFFFC5", 50, 50, "#808080", 70, activate_pause_menu))

pause_menu.add_element(GUI.Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "Resume Playing", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, deactivate_pause_menu))

pause_menu.add_element(GUI.Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Exit to main menu", "yellow",
                     "#FFFFC5", 200, 50, "black", 20, None))

pause_menu.add_element(GUI.Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "Game is paused", 50,
                            "yellow"))
