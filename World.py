import tiles.Tile
import game_graphics.Sprite


class World:

    map_width = 100
    map_height = 100
    tiles_hash = []

    camera_x = 0
    camera_y = 0

    def __init__(self):
        self.objects = []
        World.tiles_hash = [[x for x in range(World.map_width)] for y in range(World.map_height)]
        for y in range(World.map_height):
            for x in range(World.map_width):
                World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass_sprite)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self, display):
        for y in range(display.height>> 5):
            for x in range(display.width >> 5):
                pass
