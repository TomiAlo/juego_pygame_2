import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from shoot_left import ShootLeft

class EnemyShooter(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet:SpriteSheet, y, x) -> None:
        super().__init__(groups)
        self.animations=sprite_sheet.get_animations_player(1)
        self.image = self.animations[1][1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (y, x)
        self.speed=1
        self.speed_x=1
        self.last_update=pygame.time.get_ticks()
    
    def update(self):
        self.image=self.animations[2][0]
    
    def shoot(self, game):
        ShootLeft([game.all_sprites, game.enemies_shoots], self.rect.midleft)


