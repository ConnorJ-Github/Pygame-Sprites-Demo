from settings import *
from player import Player

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.character = Player()


    def run(self):
        self.display_surface.fill('grey')

        self.character.update(self.display_surface)
