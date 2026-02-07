import pygame


class Lava(pygame.sprite.Sprite):
    """
    Represents the rising lava hazard in the game.
    The lava grows over time and accelerates based on
    the selected difficulty.
    """
    def __init__(self, size, starting_pos):
        super().__init__()

        # Initial size and position of the lava
        self.size = size
        self.pos = starting_pos

        # Create the lava surface and collision rects
        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")

        # Lava growth behaviour (modified by difficulty settings)
        self.rate = 10          # Current growth speed
        self.cap = 250          # Maximum growth speed
        self.multplyer = 50     # Acceleration factor

    def update_size(self, dt):
        """
        Increases the size of the lava based on its current rate.
        Uses delta time to remain frame-rate independent.
        """
        # Increase lava height over time
        self.size += self.rate * dt

        # Recreate the surface to match the new size
        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")

    def update_rate(self, dt):
        """
        Gradually increases the lava's growth rate until it
        reaches the defined cap.
        """
        if self.rate <= self.cap:
            # Increase the growth rate over time (acceleration)
            self.rate += self.multplyer * dt
        else:
            # Prevent the growth rate from exceeding the cap
            self.rate = self.cap
