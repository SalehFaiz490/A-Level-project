import pyscroll
import pytmx


# Map setup

# Path to the Tiled map file (.tmx)
map_file = "Map tiles/map.tmx"

# Load the TMX map using pytmx
# This reads the map data, including tiles, layers, and object positions
tmx_data = pytmx.load_pygame(map_file)

# Convert TMX data into a format pyscroll can use for scrolling maps
map_data = pyscroll.TiledMapData(tmx_data)

# Create a renderer for the map, with buffering for performance
# The size matches the game window
map_layer = pyscroll.BufferedRenderer(map_data, (1280, 704))


