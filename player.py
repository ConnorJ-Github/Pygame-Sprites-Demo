from settings import *
from spriteloader import SpriteLoader

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        self.sprite_sheets = SpriteLoader()
        self.SPRITES = self.sprite_sheets.load_sprite_sheets("Characters","Archer",100,100, True) #Sprite Loading, Directory 1, Directory 2, Width, Height

        self.character = pygame.Rect(x - 50, y-50, width, height)

        self.hitbox_colour = 'red'
        self.hitbox = pygame.Rect(x, y , width, height)

        self.sprite_mask = None

        self.character_direction = 'right'
        self.animation_frame = 0

        self.BLACK = (0,0,0)

        self.y_speed = 5
        self.x_speed = 5

        self.moving = False

        self.animation_delay = 5


    def movement(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.character.x -= self.x_speed
            self.hitbox.x -= self.x_speed
            self.character_direction = 'left'
            self.moving = True
            self.animation_frame = 0
        if key[pygame.K_d] == True:
            self.character.x += self.x_speed
            self.hitbox.x += self.x_speed
            self.character_direction = 'right'
            self.moving = True
            self.animation_frame = 0


    def update_sprite(self):
        sprite_sheet = 'Idle'
        
        if self.moving:
            sprite_sheet = 'Run'

        sprite_sheet_name = sprite_sheet + "_" + self.character_direction
        sprites = self.SPRITES[sprite_sheet_name]

        sprite_index = (self.animation_frame // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_frame += 1



    def load_sprite(self, display):
        # pygame.draw.rect(display, 'blue', self.character)
        pygame.draw.rect(display, self.hitbox_colour, self.hitbox, 1)

        self.sprite = self.SPRITES["Idle_" + self.character_direction][0]
        display.blit(self.sprite,(self.character.x, self.character.y))


    def update(self, display):
        self.movement()
        self.load_sprite(display)
        self.update_sprite()
