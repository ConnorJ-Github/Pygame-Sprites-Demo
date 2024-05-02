from settings import *
from spriteloader import SpriteLoader

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):



        self.sprite_sheets = SpriteLoader()

        self.sprite_height = 100
        self.sprite_width = 100
        self.SPRITES = self.sprite_sheets.load_sprite_sheets("Characters","Archer",self.sprite_width,self.sprite_height, True) #Sprite Loading, Directory 1, Directory 2, Width, Height
                
        self.character = pygame.Rect(x, y, width, height)
        
        self.mask = None
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
        if key[pygame.K_a] and self.character.x + 75 > self.movement_speed: #Temp code to limit the character to the screen
            self.move_left(self.movement_speed)
        if key[pygame.K_d] and self.character.x <  400 - 125 - self.movement_speed: #temp code to limit the character to the screen
            self.move_right(self.movement_speed)


    def update_sprite(self):
        sprite_sheet = 'Idle'
        
        if self.x_speed != 0:
            sprite_sheet = 'Run'

        if self.y_speed != 0:
            sprite_sheet = 'Jump'

        sprite_sheet_name = sprite_sheet + "_" + self.character_direction
        sprites = self.SPRITES[sprite_sheet_name]

        sprite_index = (self.animation_frame // self.animation_delay) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_frame += 1
        self.sprite_mask()

    def sprite_mask(self): #Creates an accurate "Character" mask that improves the "collision" box of the character
        self.character = self.sprite.get_rect(topleft=(self.character.x, self.character.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def load_sprite(self, display):
       # pygame.draw.rect(display, 'blue', self.character)
        display.blit(self.sprite,(self.character.x, self.character.y))


    def update(self, display, fps):
        
        self.y_speed += min(1,(self.gravity_count / fps) * self.gravity_weight) #Increases the falling speed based of how long the player has been falling

        #self.gravity_count += 1

        self.move(self.x_speed, self.y_speed)
        self.movement()
        self.update_sprite()
        self.load_sprite(display)
