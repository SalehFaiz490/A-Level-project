import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Map tiles/spike.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt, keys):

        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10




