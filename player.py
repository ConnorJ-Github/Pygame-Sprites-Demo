from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        self.SPRITES = load_sprite_sheets("Characters","Knight",38,20)


        self.character_colour = 'blue'
        self.character = pygame.Rect(x,y, width,height)

        self.sprite_mask = None

        self.character_direction = 'right'
        self.animation_frame = 0


        self.y_speed = 5
        self.x_speed = 5
    

    def movement(self):
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.character.x -= self.x_speed
            self.character_direction = 'right'
            self.animation_frame = 0
        if key[pygame.K_d] == True:
            self.character.x += self.x_speed
            self.character_direction = 'left'
            self.animation_frame = 0

    def animation(self, fps):
        pass
        # self.move(self.x_speed, self.y_speed)


    def update(self, display):
        self.sprite = self.SPRITES['Idle_' + self.character_direction][0]
        display.blit(self.sprite, (self.character.x, self.character.y))
        self.movement()