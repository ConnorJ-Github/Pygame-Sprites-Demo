from settings import *
from sprite_loader import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        self.SPRITES = load_sprite_sheets("Characters","Archer",30,30, True) #Sprite Loading, Directory 1, Directory 2, Width, Height

        self.character = pygame.Rect(x,y, width,height)

        self.hitbox_colour = 'red'

        self.hitbox = pygame.Rect(x,y,width,height)

        self.sprite_mask = None

        self.character_direction = 'right'
        self.animation_frame = 0


        self.y_speed = 5
        self.x_speed = 5
    

    def movement(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.character.x -= self.x_speed
            self.hitbox.x -= self.x_speed
            self.character_direction = 'right'
            self.animation_frame = 0
        if key[pygame.K_d] == True:
            self.character.x += self.x_speed
            self.hitbox.x += self.x_speed
            self.character_direction = 'left'
            self.animation_frame = 0

    def animation(self, fps):
        pass
        # self.move(self.x_speed, self.y_speed)

    def load_sprite(self, display):
        # self.sprite = self.SPRITES['Idle_' + self.character_direction][0]
        # display.blit(self.sprite, (self.character.x, self.character.y))
        pygame.draw.rect(display, 'blue', self.character)
        pygame.draw.rect(display, self.hitbox_colour, self.hitbox, 1)


    def update(self, display):
        self.movement()
        self.load_sprite(display)