from settings import *
from world import World



class Game:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Sprites Demo")

        self.clock = pygame.time.Clock()

        self.world_screen = World()


    def run(self):
        while True:
            fps = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()


            self.world_screen.run(fps)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()