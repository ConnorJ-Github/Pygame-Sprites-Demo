from settings import *
from player import Player

class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.character = Player(HEIGHT/2,WIDTH/2, 100,100)


    def run(self,fps):
        self.display_surface.fill('grey')
        self.character.update(self.display_surface, fps)
