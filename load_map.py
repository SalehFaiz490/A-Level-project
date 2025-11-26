import pyscroll
import pytmx
import GUI

map_file = ["Map tiles\spawn_segment.tmx"]

tmx_data = pytmx.load_pygame(map_file[0])

map_data = pyscroll.TiledMapData(tmx_data)

screen = GUI.screen

map_layer = pyscroll.BufferedRenderer(map_data, (1280, 704))

group = pyscroll.PyscrollGroup(map_layer=map_layer)


