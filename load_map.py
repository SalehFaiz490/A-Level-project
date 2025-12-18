import pyscroll
import pytmx

map_file = "Map tiles/map.tmx"

tmx_data = pytmx.load_pygame(map_file, pixelalpha=True)

map_data = pyscroll.TiledMapData(tmx_data)

map_layer = pyscroll.BufferedRenderer(map_data, (1280, 704))

group = pyscroll.PyscrollGroup(map_layer=map_layer)


