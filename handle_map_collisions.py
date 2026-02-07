import pygame
import handle_coin_logic


# Wall collisions
def wall_collisions(tiled_map):
    """
    Reads the 'wall_layer' from the TMX map and returns
    a list of pygame.Rect objects representing solid walls
    for collision detection.
    """
    collision_rects = []
    layer_name = "wall_layer"

    for x, y, gid in tiled_map.get_layer_by_name(layer_name):
        tile = tiled_map.get_tile_image_by_gid(gid)
        if tile:
            # Create a rect that matches the tile's position and size
            rect = pygame.Rect(
                x * tiled_map.tilewidth,
                y * tiled_map.tileheight,
                tiled_map.tilewidth,
                tiled_map.tileheight
            )
            collision_rects.append(rect)

    return collision_rects


# Coin creation
def create_coins(tiled_map):
    """
    Reads the 'Coin layer' and creates Coin objects
    at the correct positions. Returns a list of Coin sprites.
    """
    collision_rects = []
    layer_name = "Coin layer"

    for x, y, gid in tiled_map.get_layer_by_name(layer_name):
        tile = tiled_map.get_tile_image_by_gid(gid)
        if tile:
            px = x * tiled_map.tilewidth
            py = y * tiled_map.tileheight

            # Spawn a Coin object at this tile
            collision_rects.append(handle_coin_logic.Coin(px, py))

    return collision_rects


# Spike collisions
def spike_collisions(tiled_map):
    """
    Reads the 'spike_layer' and returns a list of pygame.Rects
    representing spike positions.
    """
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


# Player spawn
def get_spawn_cords(tiled_map):
    """
    Finds the spawn position by looking for an object
    named 'Spawn_block' in the map objects.
    Returns a pygame.Vector2 of the spawn coordinates.
    """
    for obj in tiled_map.objects:
        if obj.name == "Spawn_block":
            return pygame.Vector2(obj.x, obj.y)
