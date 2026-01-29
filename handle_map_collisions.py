import pygame
import handle_coin_logic


def wall_collisions(tiled_map):
    collision_rects = []
    layer_name = "wall_layer"

    for x, y, gid in tiled_map.get_layer_by_name(layer_name):
        tile = tiled_map.get_tile_image_by_gid(gid)
        if tile:
            rect = pygame.Rect(
                x * tiled_map.tilewidth,
                y * tiled_map.tileheight,
                tiled_map.tilewidth,
                tiled_map.tileheight
            )
            collision_rects.append(rect)

    return collision_rects

def create_coins(tiled_map):
    collision_rects = []
    layer_name = "Coin layer"
    for x, y, gid in tiled_map.get_layer_by_name(layer_name):
        tile = tiled_map.get_tile_image_by_gid(gid)
        if tile:
            px = x * tiled_map.tilewidth
            py = y * tiled_map.tileheight

            collision_rects.append(handle_coin_logic.Coin(px, py))


    return collision_rects

def spike_collisions(tiled_map):
    collision_rects = []
    layer_name = "spike_layer"
    for x, y, gid in tiled_map.get_layer_by_name(layer_name):
        tile = tiled_map.get_tile_image_by_gid(gid)
        if tile:
            rect = pygame.Rect(
                x * tiled_map.tilewidth,
                y * tiled_map.tileheight,
                tiled_map.tilewidth,
                tiled_map.tileheight
            )
            collision_rects.append(rect)

    return collision_rects


def get_spawn_cords(tiled_map):
    for obj in tiled_map.objects:
        if obj.name == "Spawn_block":
            return pygame.Vector2(obj.x, obj.y)


