import pygame

def run_menus():

    # set up pygame
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Main Menu")
    # Starts game clock
    running = True
    start_game = False

    class UIElement:
        def __init__(self, xpos, ypos, font):
            self.x_pos = xpos
            self.y_pos = ypos
            self.font = font

    class Label(UIElement):
        def __init__(self, x_pos, y_pos, font, text, font_size, color):
            super().__init__(x_pos, y_pos, font)
            self.text = text
            self.fontSize = font_size
            self.color = color

        def render(self):
            render_font = pygame.font.Font(self.font, self.fontSize)
            render_text = render_font.render(self.text, True, self.color)
            text_rect = render_text.get_rect()

            # slaps text in the middle
            text_rect.center = (self.x_pos//2, self.y_pos//2)

            # puts text on screen
            screen.blit(render_text, text_rect)

    class Button(UIElement):
        def __init__(self, x_pos, y_pos, font, label, init_color, hover_color, width, height, text_color, font_size,
                     command_code):

            super().__init__(x_pos, y_pos, font)
            self.label = label
            self.fontSize = font_size

            # needed to know what each button does
            self.command_code = command_code

            # need inti color so that it goes back to its inital color after hozered
            self.init_color = init_color
            self.hoverColor = hover_color

            # when we start we are og color
            self.current_color = self.init_color

            # text stats same color so no need for afromentioned logic
            self.text_color = text_color
            self.width = width
            self.height = height
            self.rect = pygame.Rect(x_pos, y_pos, width, height)

        def render(self):
            # slaps it all on the screen, first a box then a label on it so its like one enity
            pygame.draw.rect(screen, self.current_color, self.rect, border_radius=8)
            render_font = pygame.font.Font(self.font, self.fontSize)
            text_surface = render_font.render(self.label, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

        def is_hovered(self):
            return self.rect.collidepoint(pygame.mouse.get_pos())
            # this will return true if the mouse is inside of buttons rect and false otherwise

        def is_clicked(self, event):
            return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered()
            # if the left mouse button (aka button 1) is pressed and if it is being hovered then statement is true

        def process_command(self):
            return self.command_code

            # returns a functsion call to specific command for that button

    # Helper functsions for diffrent button commands
    def play_button_command():
        # No more menus :)
        main_menu.isLoaded = False

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
        # think i was on crack for this one
        current_menu.isLoaded = False
        main_menu.isLoaded = True
        new_menu = main_menu

        return new_menu

    class Menu:
        def __init__(self, is_loaded):
            self.elements = []
            self.isLoaded = is_loaded

        def add_element(self, element):
            self.elements.append(element)

        def render(self):
            if self.isLoaded:
                for i in self.elements:
                    i.render()

        def handle_events(self, event):
            for element in self.elements:
                if isinstance(element, Button) and element.is_clicked(event):
                    command_code = element.process_command() # becomes a functsion call itself
                    change = command_code()
                    return change

                elif isinstance(element, Button) and element.is_hovered():
                    element.current_color = element.hoverColor

                elif isinstance(element, Button):
                    element.current_color = element.init_color

    main_menu = Menu(True)
    current_menu = main_menu

    options_menu = Menu(False)
    leaderboard_menu = Menu(False)

    # main menu items
    main_menu.add_element(Button((1280 / 2) - 100, 200, "Grand9K Pixel.ttf", "Play", "yellow",
                    "#FFFFC5", 200, 50, "black", 20, play_button_command))

    main_menu.add_element(Label((1280 / 2) + 650, 150, "Grand9K Pixel.ttf", "Tomb Of The Mask", 100,
                           "yellow"))

    main_menu.add_element(Label((1280 / 2) + 650, 300, "Grand9K Pixel.ttf", "By Saleh Faiz", 10,
                           "yellow"))

    main_menu.add_element(Button((1280 / 2) - 100, 300, "Grand9K Pixel.ttf", "See Leaderboard", "yellow",
                            "#FFFFC5", 200, 50, "black", 20, load_leaderboard_menu_command))

    main_menu.add_element(Button((1280 / 2) - 100, 400, "Grand9K Pixel.ttf", "Options", "yellow",
                            "#FFFFC5", 200, 50, "black", 20, load_optsion_menu_command))

    # Back button declaratsion
    back_button = Button((1280 / 2) - 100, 500, "Grand9K Pixel.ttf", "Back", "yellow",
                    "#FFFFC5", 200, 50, "black", 20, back_button_command)

    options_menu.add_element(back_button)
    leaderboard_menu.add_element(back_button)

    # optsion menu items
    options_menu.add_element(Label((1280 / 2)+650, 200, "Grand9K Pixel.ttf", "Change setting here", 32,  "yellow"))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_menu.isLoaded is False:  # no menus means game go
                running = False
                start_game = True
                break

            current_menu.handle_events(event)  # constantly checks for an event and will return None if no event present
            if current_menu.handle_events(event) is not None:
                current_menu = current_menu.handle_events(event)  # if there is event update current menu acordnily


        screen.fill("black")

        current_menu.render()
        pygame.display.flip()
        pygame.display.update()

    return start_game



