import pygame


class Lava(pygame.sprite.Sprite):
    def __init__(self, size, starting_pos):
        super().__init__()
        self.size = size
        self.pos = starting_pos

        # Lava's image and appearance
        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")

        # changed with difficulty slider, to do with speed of lava
        self.rate = 10
        self.cap = 250
        self.multplyer = 50

    def update_size(self, dt):

        self.size = self.size + (self.rate * dt)
        # percentage increece of size scaled to frame rate

        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")

    def update_rate(self, dt):
        # while the rate is less than the max, update the rate
        # this accelerates the lavas growth over time
        if self.rate <= self.cap:
            # multiplier is used here to change the "acceleration" of the lava
            self.rate += (self.multplyer * dt)

        else:
            # if the rate is at the cap, don't increase the rate further
            self.rate = self.cap





