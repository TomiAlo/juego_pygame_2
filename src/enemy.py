import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from shoot import Shoot

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet:SpriteSheet, y, x) -> None:
        super().__init__(groups)
        self.animations=sprite_sheet.get_animations_player(1)
        self.image = self.animations[1][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (y, x)
        self.speed=1
        self.speed_x=1
        self.speed_y=0
        self.last_update=pygame.time.get_ticks()
    
    def update(self):
        self.rect.x += self.speed
        print(self.rect.x)
        self.speed_y+=GRAVITY
        self.rect.y+=self.speed_y
            
        if self.rect.bottom>=HEIGHT_PLAYER:
            self.rect.bottom=HEIGHT_PLAYER
            self.speed_y=0
    
            
        # Si el sprite alcanza el límite derecho
        if self.rect.right > WIDTH:
            self.speed = -self.speed  # Invertir la dirección para ir a la izquierda
            self.image = self.animations[0][2]  # Cambiar la imagen para que mire a la izquierda

        # Si el sprite alcanza el límite izquierdo
        elif self.rect.left < 0:
            self.speed = abs(self.speed)  # Mantener la dirección positiva para ir a la derecha
            self.image = self.animations[1][0]
        
        

            



