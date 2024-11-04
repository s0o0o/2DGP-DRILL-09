from pico2d import load_image
from game_world import world

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self, grass=None):
        self.image.draw(400, 60)


    def update(self):
        pass
