from settings import *

class Player():
    def __init__(self):
        #Assets
        self.walking_sprites = []
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_1.png').convert_alpha)
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_2.png').convert_alpha)
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_2.png').convert_alpha)
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_2.png').convert_alpha)
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_2.png').convert_alpha)
        self.walking_sprites.append(pygame.image.load('Assets\Walking\walk_2.png').convert_alpha)

        self.jumping_sprites = []
        self.jumping_sprites.append(pygame.image.load('Assets\Jumping\jump_1.png').convert_alpha)
        self.jumping_sprites.append(pygame.image.load('Assets\Jumping\jump_2.png').convert_alpha)
        self.jumping_sprites.append(pygame.image.load('Assets\Jumping\jump_3.png').convert_alpha)
        self.jumping_sprites.append(pygame.image.load('Assets\Jumping\jump_4.png').convert_alpha)
        self.jumping_sprites.append(pygame.image.load('Assets\Jumping\jump_5.png').convert_alpha)

        self.idle_sprites = []
        self.idle_sprites.append(pygame.image.load('Assets\Idle\-ready_1.png').convert_alpha)
        self.idle_sprites.append(pygame.image.load('Assets\Idle\-ready_2.png').convert_alpha)
        self.idle_sprites.append(pygame.image.load('Assets\Idle\-ready_3.png').convert_alpha)

        self.character_colour = 'blue'
        self.character = pygame.Rect(HEIGHT/2,WIDTH/2, 25,25)

        self.y_speed = 5
        self.x_speed = 5


    def movement(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.character.x -= self.x_speed
        if key[pygame.K_d] == True:
            self.character.x += self.x_speed


    def update(self, display):
        pygame.draw.rect(display, self.character_colour, self.character)
        self.movement()