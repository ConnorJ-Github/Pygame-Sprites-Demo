from settings import *
from spriteloader import SpriteLoader

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        self.sprite_sheets = SpriteLoader()
        self.SPRITES = self.sprite_sheets.load_sprite_sheets("Characters","Archer",100,100, True) #Sprite Loading, Directory 1, Directory 2, Width, Height

        self.character = pygame.Rect(x - 50, y-50, width, height)

        self.sprite_mask = None
        self.character_direction = 'right'
        self.animation_frame = 0

        self.BLACK = (0,0,0)

        self.movement_speed = 5

        self.y_speed = 0
        self.x_speed = 0

        self.gravity_count = 0 #Used to record how long the player has been falling
        self.gravity_weight = 1

        self.moving = False

        self.animation_delay = 5

    def move(self, dx, dy):
        self.character.x += dx
        self.character.y += dy

    def move_left(self,speed):
        self.x_speed = - speed
        if self.character_direction != 'left':
            self.character_direction = 'left'
            self.animation_count = 0

    def move_right(self, speed):
        self.x_speed = speed
        if self.character_direction != 'right':
            self.character_direction = 'right'
            self.animation_count = 0

    def movement(self):
        
        self.x_speed = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.move_left(self.movement_speed)
            self.character_direction = 'left'
        if key[pygame.K_d] == True:
            self.move_right(self.movement_speed)
            self.character_direction = 'right'



    def update_sprite(self):
        sprite_sheet = 'Idle'
        
        if self.x_speed != 0:
            sprite_sheet = 'Run'

        sprite_sheet_name = sprite_sheet + "_" + self.character_direction
        sprites = self.SPRITES[sprite_sheet_name]

        sprite_index = (self.animation_frame // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_frame += 1

    def load_sprite(self, display):
        # pygame.draw.rect(display, 'blue', self.character)

        #self.sprite = self.SPRITES["Idle_" + self.character_direction][0]
        display.blit(self.sprite,(self.character.x, self.character.y))


    def update(self, display, fps):
        
        self.y_speed += min(1,(self.gravity_count / fps) * self.gravity_weight) #Increases the falling speed based of how long the player has been falling
        self.move(self.x_speed, self.y_speed)
        self.movement()
        self.update_sprite()
        self.load_sprite(display)
