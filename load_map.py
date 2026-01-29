import pyscroll
import pytmx

map_file = "Map tiles/map.tmx"

tmx_data = pytmx.load_pygame(map_file)


map_data = pyscroll.TiledMapData(tmx_data)


map_layer = pyscroll.BufferedRenderer(map_data, (1280, 704))



