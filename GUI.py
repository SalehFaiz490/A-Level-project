import pygame

# set up pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((1280, 720))

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
        text_rect.center = (self.x_pos // 2, self.y_pos // 2)

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
        # slaps it all on the screen, first a box then a label on it so its one enity
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=8)
        render_font = pygame.font.Font(self.font, self.fontSize)
        text_surface = render_font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self):
        # this will return true if the mouse is inside of buttons rect and false otherwise
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered()
        # if the left mouse button (aka button 1) is pressed and if it is being hovered then statement is true

    def process_command(self):
        return self.command_code



        # returns a function call to specific command for that button




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
                command_code = element.process_command()  # collects the function call

                try:
                    return command_code()

                except TypeError:
                    return "Start MainMenu"

            elif isinstance(element, Button) and element.is_hovered():
                element.current_color = element.hoverColor

            elif isinstance(element, Button):
                element.current_color = element.init_color

