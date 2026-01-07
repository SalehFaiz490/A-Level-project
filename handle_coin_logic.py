import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Map tiles/coil.png").convert_alpha()
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center=self.pos)




