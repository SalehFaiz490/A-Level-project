import pygame

# Pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Directions for use in movement/collision
DIRECTIONS = {
    pygame.K_w: (0, -1, "up"),
    pygame.K_s: (0, 1, "down"),
    pygame.K_a: (-1, 0, "left"),
    pygame.K_d: (1, 0, "right")
}


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((167, 255, 100))
        self.image.set_colorkey((255, 100, 98))

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.velocity_x = 0
        self.velocity_y = 0
        self.moving = False
        self.blocked_dirs = set()

    def movement(self, vx, vy):
        self.velocity_x = vx
        self.velocity_y = vy
        self.moving = True


# Create sprites
sprite = Sprite("blue", 100, 100)
sprite.rect.x = 200
sprite.rect.y = 300

obstacle = Sprite("red", 400, 100)
obstacle.rect.x = 500
obstacle.rect.y = 500

# Group them
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(sprite)
all_sprites_list.add(obstacle)

speed = 700

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start movement if key is pressed and not already moving
        if event.type == pygame.KEYDOWN and not sprite.moving:
            if event.key in DIRECTIONS:
                dx, dy, dir_name = DIRECTIONS[event.key]
                if dir_name not in sprite.blocked_dirs:
                    sprite.movement(dx * speed * dt, dy * speed * dt)

    # Move the sprite
    if sprite.moving:
        sprite.rect.x += sprite.velocity_x
        sprite.rect.y += sprite.velocity_y

        # Collision handling
        collision = False
        blocked = set()

        # Wall collision
        if sprite.rect.left < 0:
            sprite.rect.left = 0
            blocked.add("left")
            collision = True
        if sprite.rect.right > 1280:
            sprite.rect.right = 1280
            blocked.add("right")
            collision = True
        if sprite.rect.top < 0:
            sprite.rect.top = 0
            blocked.add("up")
            collision = True
        if sprite.rect.bottom > 720:
            sprite.rect.bottom = 720
            blocked.add("down")
            collision = True

        print(blocked)
        # Object collision
        if sprite.rect.colliderect(obstacle.rect):
            collision = True
            # Determine direction blocked
            if sprite.velocity_y < 0:
                sprite.rect.top = obstacle.rect.bottom
                blocked.add("up")
            elif sprite.velocity_y > 0:
                sprite.rect.bottom = obstacle.rect.top
                blocked.add("down")
            if sprite.velocity_x < 0:
                sprite.rect.left = obstacle.rect.right
                blocked.add("left")
            elif sprite.velocity_x > 0:
                sprite.rect.right = obstacle.rect.left
                blocked.add("right")

        # Stop movement on collision and update blocked directions
        if collision:
            sprite.velocity_x = 0
            sprite.velocity_y = 0
            sprite.moving = False
            sprite.blocked_dirs = blocked
        else:
            sprite.blocked_dirs = set()

    # Draw everything
    screen.fill("white")
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
