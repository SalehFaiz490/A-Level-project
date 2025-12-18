import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = self.image = pygame.image.load("Map tiles/spike.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2(x, y)
        self.dir = pygame.Vector2(0, 0)  # direction persists
        self.speed = 5000
        self.moving = False
        self.score = 0

    def update_score(self, coin_rects, group):
        for coin in coin_rects:
            if self.rect.colliderect(coin):
                coin_rects.remove(coin)
                group.remove(coin)
                self.score += 1

    def set_direction(self, keys):
        # Only set direction when a key is pressed
        if keys[pygame.K_w]:
            self.dir = pygame.Vector2(0, -1)

        elif keys[pygame.K_s]:
            self.dir = pygame.Vector2(0, 1)

        elif keys[pygame.K_a]:
            self.dir = pygame.Vector2(-1, 0)

        elif keys[pygame.K_d]:
            self.dir = pygame.Vector2(1, 0)

    def move_and_collide(self, dt, walls):
        # --- Move along X ---

        self.pos.x += self.dir.x * self.speed * dt
        self.rect.x = int(self.pos.x)

        for wall in walls:
            if self.rect.colliderect(wall):
                # stop movement on X and snap
                if self.dir.x > 0:
                    self.rect.right = wall.left
                elif self.dir.x < 0:
                    self.rect.left = wall.right

                self.moving = False
                self.pos.x = self.rect.x
                self.dir.x = 0  # STOP X movement

        # --- Move along Y ---
        self.pos.y += self.dir.y * self.speed * dt
        self.rect.y = int(self.pos.y)

        for wall in walls:
            if self.rect.colliderect(wall):
                # stop movement on Y and snap
                if self.dir.y > 0:
                    self.rect.bottom = wall.top
                elif self.dir.y < 0:
                    self.rect.top = wall.bottom

                self.moving = False
                self.pos.y = self.rect.y
                self.dir.y = 0  # STOP Y movement

        if self.dir != (0, 0):
            self.moving = True


