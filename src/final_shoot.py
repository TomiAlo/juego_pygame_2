import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet

class FinalShoot(pygame.sprite.Sprite):
    def __init__(self, groups, coordenates) -> None:
        super().__init__(groups)
        self.image=pygame.image.load("assets/sprites/final_shot.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=coordenates)
        self.speed_x=5
    
    def update(self):
        
        self.rect.x+=self.speed_x