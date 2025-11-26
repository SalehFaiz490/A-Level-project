import pygame
from pytmx.util_pygame import load_pygame
import pyscroll
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 704))
clock = pygame.time.Clock()

# -----------------------------------------
# Player Sprite
# -----------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("spike.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


# -----------------------------------------
# Load a single TMX map chunk with offset
# -----------------------------------------
def load_chunk(filename, index, screen_size):
    tmx = load_pygame(filename)

    map_data = pyscroll.TiledMapData(tmx)
    chunk_height = tmx.height * tmx.tileheight

    # Offset the entire map upwards by chunk_height * index
    offset_y = -index * chunk_height
    map_data.origin_y = offset_y

    renderer = pyscroll.BufferedRenderer(map_data, screen_size)

    return {
        "tmx": tmx,
        "map_data": map_data,
        "renderer": renderer,
        "height": chunk_height,
        "offset": offset_y,
        "index": index
    }


# -----------------------------------------
# Setup Game
# -----------------------------------------
chunks = {}
map_layers = []

# Load first map chunk at index 0
chunks[0] = load_chunk("spawn_segment.tmx", 0, screen.get_size())
map_layers.append(chunks[0]["renderer"])

# Player
player = Player(300, 300)

# Build initial group
group = pyscroll.PyscrollGroup(map_layer=map_layers[0], default_layer=0)
group.add(player)

current_chunk = 0


# -----------------------------------------
# Game Loop
# -----------------------------------------
while True:
    dt = clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player
    player.update()

    chunk_height = chunks[current_chunk]["height"]

    # If player goes above the top of the current chunk -> load next
    if player.rect.y < chunks[current_chunk]["offset"] - 200:
        current_chunk += 1

        if current_chunk not in chunks:
            # Load new chunk
            chunks[current_chunk] = load_chunk(
                "spawn_segment.tmx",
                current_chunk,
                screen.get_size()
            )

            map_layers.append(chunks[current_chunk]["renderer"])
            print(f"Loaded chunk index: {current_chunk}")

            # ----------------------------
            # REBUILD GROUP (important!)
            # ----------------------------
            group = pyscroll.PyscrollGroup(
                map_layer=map_layers[0],
                default_layer=0
            )
            group.add(player)

            for layer in map_layers[1:]:
                group.add_layer(layer)

    # Center camera
    group.center(player.rect.center)

    # Draw
    group.draw(screen)
    pygame.display.flip()
