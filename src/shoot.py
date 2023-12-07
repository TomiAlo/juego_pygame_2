import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet

class Shoot(pygame.sprite.Sprite):
    def __init__(self, groups, coordenates) -> None:
        super().__init__(groups)
        self.image=pygame.transform.scale(pygame.image.load("assets/sprites/shoot_gohan.png").convert_alpha(),(40,20))
        self.rect=self.image.get_rect(midbottom=coordenates)
        self.speed_x=5
    
    def update(self):
        
        self.rect.x+=self.speed_x
        
        if self.rect.right >= WIDTH:
            self.kill()