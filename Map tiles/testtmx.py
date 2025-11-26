import pygame
from pytmx.util_pygame import load_pygame
import pyscroll
from pyscroll.data import MapAggregator, TiledMapData
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 704), pygame.RESIZABLE)
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("spike.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 250
        self.pos = pygame.Vector2(x, y)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x += 1

        if move.length() > 0:
            move = move.normalize() * self.speed * dt

        self.pos += move
        self.rect.center = self.pos


world_data = MapAggregator((32, 32))
y_offset = 0

map_filenames = ["spawn_segment2.tmx", "spawn_segment.tmx"]

for filename in map_filenames:
    tmx_data = load_pygame(filename)
    pyscroll_data = TiledMapData(tmx_data)
    world_data.add_map(pyscroll_data, (0, y_offset))
    y_offset += tmx_data.height * tmx_data.tileheight  # exact stacking


map_layer = pyscroll.BufferedRenderer(world_data, size=screen.get_size(), clamp_camera=True)
group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=0)


player = Player(400, 400)  # 400, 400 is inside top map
player.layer = 0
group.add(player)


while True:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            map_layer.set_size((event.w, event.h))

    group.update(dt)
    group.center(player.rect.center)
    group.draw(screen)
    pygame.display.flip()
