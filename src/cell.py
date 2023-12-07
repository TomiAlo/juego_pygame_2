import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from final_shoot_left import FinalShootLeft
from funciones import *
from shoot_left import ShootLeft


class Cell(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet:SpriteSheet, y, x) -> None:
        super().__init__(groups)
        self.animations=sprite_sheet.get_animations_player(1)
        self.image = self.animations[0][0]
        self.rect = self.image.get_rect()
        self.current_sprite_col=0
        self.rect.topleft = (y, x)
        self.speed=1
        self.speed_x=0
        self.speed_y=0
        self.last_update=pygame.time.get_ticks()
        self.time_animation=300
        self.jump_power=-20
    
    def update(self):
        self.rect.y -= self.speed
        self.handle_events()
        if self.rect.top < 0:
            self.speed = -self.speed  # Invertir la dirección para ir a la izquierda

        # Si el sprite alcanza el límite izquierdo
        elif self.rect.bottom >HEIGHT:
            self.speed = abs(self.speed)  # Mantener la dirección positiva para ir a la derecha

        
    def handle_events(self):
        
        current_time=pygame.time.get_ticks()
        if current_time - self.last_update >= self.time_animation:
            self.current_sprite_col+=1
            self.image=self.animations[0][self.current_sprite_col]
            if self.current_sprite_col==2:
                self.current_sprite_col=0

            self.last_update=current_time
            
        self.defense=False
        self.punch=False
    
    def jump(self):
        if self.rect.y >= 0:
            self.speed_y=self.jump_power
    
    def shoot(self, game):
        ShootLeft([game.all_sprites, game.enemies_shoots], self.rect.midleft)
    
    def life(self, game):
        for life in range(game.lives_cell):
            blit_background(SCREEN, image_heart, black, (life*16+900,0))

    def final_shot(self, game):
        FinalShootLeft([game.all_sprites, game.enemies_shoots], self.rect.bottomleft)

