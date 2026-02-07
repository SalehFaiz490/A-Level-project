import pygame

# Initialise pygame and its modules
pygame.init()

# Create the main game window
screen = pygame.display.set_mode((1280, 704))


class UIElement:
    """
    Base class for all UI elements.
    Stores shared positional and font information.
    """
    def __init__(self, xpos, ypos, font):
        self.x_pos = xpos
        self.y_pos = ypos
        self.font = font


class Label(UIElement):
    """
    Simple text label displayed on the screen.
    """
    def __init__(self, x_pos, y_pos, font, text, font_size, color):
        super().__init__(x_pos, y_pos, font)
        self.text = text
        self.fontSize = font_size
        self.color = color

    def render(self):
        # Create the font and render the text surface
        render_font = pygame.font.Font(self.font, self.fontSize)
        render_text = render_font.render(self.text, True, self.color)
        text_rect = render_text.get_rect()

        # Centre the text based on the given position
        text_rect.center = (self.x_pos // 2, self.y_pos // 2)

        # Draw the text to the screen
        screen.blit(render_text, text_rect)


class Button(UIElement):
    """
    Clickable button with hover effects and an associated command.
    """
    def __init__(
        self, x_pos, y_pos, font, label, init_color, hover_color,
        width, height, text_color, font_size, command_code
    ):
        super().__init__(x_pos, y_pos, font)

        self.label = label
        self.fontSize = font_size

        # Stores the function or command triggered when the button is clicked
        self.command_code = command_code

        # Colours used for normal and hover states
        self.init_color = init_color
        self.hoverColor = hover_color
        self.current_color = self.init_color

        # Text and button dimensions
        self.text_color = text_color
        self.width = width
        self.height = height

        # Rect used for collision and rendering
        self.rect = pygame.Rect(x_pos, y_pos, width, height)

    def render(self):
        # Draw button background
        pygame.draw.rect(
            screen, self.current_color, self.rect, border_radius=8
        )

        # Render and centre button label
        render_font = pygame.font.Font(self.font, self.fontSize)
        text_surface = render_font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self):
        # Returns True if the mouse cursor is over the button
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self, event):
        # True if left mouse button is pressed while hovering
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered())

    def process_command(self):
        # Returns the stored command for execution
        return self.command_code


class Menu:
    """
    Represents a menu containing multiple UI elements.
    """
    def __init__(self, is_loaded):
        self.elements = []
        self.isLoaded = is_loaded

    def add_element(self, element):
        # Add a UI element (button or label) to the menu
        self.elements.append(element)

    def render(self):
        # Only render the menu if it is active
        if self.isLoaded:
            for element in self.elements:
                element.render()

    def handle_events(self, event):
        # Process input events for all menu elements
        for element in self.elements:

            if isinstance(element, Button) and element.is_clicked(event):
                # Execute the button’s assigned command
                command_code = element.process_command()

                try:
                    return command_code()
                except TypeError:
                    # Used for commands that return control flow instead of a function
                    return "Start MainMenu"

            elif isinstance(element, Button) and element.is_hovered():
                # Change colour when hovered
                element.current_color = element.hoverColor

            elif isinstance(element, Button):
                # Reset colour when not hovered
                element.current_color = element.init_color
