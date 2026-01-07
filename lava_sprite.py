import pygame


class Lava(pygame.sprite.Sprite):
    def __init__(self, size, starting_pos):
        super().__init__()
        self.size = size
        self.pos = starting_pos

        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")
        self.rate = 10


    def update_size(self, dt):

        self.size = self.size + (self.rate * dt)
        # percentage increece of size scaled to frame rate

        self.image = pygame.Surface([1400, self.size])
        self.rect = self.image.get_rect(center=self.pos)
        self.image.fill("red")

    def update_rate(self, dt):
        if self.rate <= 250:
            self.rate += (50 * dt)

        else:
            self.rate = 250





