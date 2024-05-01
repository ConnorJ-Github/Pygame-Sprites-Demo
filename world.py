from settings import *


class World:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.character = pygame.Rect(HEIGHT/2,WIDTH/2, 25,25)
        self.character_colour = 'blue'

        self.y_speed = 5
        self.x_speed = 5

    def run(self):
        self.display_surface.fill('grey')

        pygame.draw.rect(self.display_surface, self.character_colour, self.character)

        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            self.character.x -= self.x_speed
        if key[pygame.K_d] == True:
            self.character.x += self.x_speed