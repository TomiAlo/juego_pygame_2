import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from funciones import *
from final_shoot import FinalShoot
from shoot import Shoot

class FinalPlayer(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet:SpriteSheet, game) -> None:
        # Inicializa la clase base y configura las propiedades del jugador final
        super().__init__(groups)
        self.animations = sprite_sheet.get_animations_player(1)
        self.image = self.animations[1][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 450)
        self.speed = 4
        self.current_sprite_col = 0
        self.current_sprite_row = 0
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 300
        self.speed_y = 0
        self.speed_x = 0
        self.flag = False
        self.jump_power = -10
        self.speed_y = 0
        self.speed_x = 0
        self.defense = False
        self.punch = False
        self.row = 7
        self.game = game
    
    def update(self):
        # Actualiza la posición del jugador final y maneja eventos
        self.speed_y += GRAVITY
        self.rect.y += self.speed_y

        if self.rect.bottom >= HEIGHT_PLAYER:
            self.rect.bottom = HEIGHT_PLAYER
            self.speed_y = 0
        self.handle_events(self.game)

    def handle_events(self, game):
        # Maneja los eventos de teclado para controlar las acciones del jugador final
        keys = pygame.key.get_pressed()
        
        if keys[K_d]:
            # Movimiento hacia la derecha
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[2][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                if keys[K_w]:
                    self.jump()
                
        elif keys[K_a]:
            # Movimiento hacia la izquierda
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[0][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                if keys[K_w]:
                    self.jump()

        elif keys[K_w]:
            # Salto
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[5][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
            self.jump()
        elif keys[K_s]:
            # Defensa
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[4][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
            self.defense = True

        elif keys[K_l]:
            # Disparo normal
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[3][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
        elif keys[K_j]:
            # Puñetazo
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[6][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
            self.punch = True

        elif keys[K_k]:
            # Disparo final
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[self.row][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0
                    if self.row < 10:
                        self.row += 1
                    else:
                        FinalShoot([game.all_sprites, game.player_shoots], self.rect.bottomright)
                        self.current_sprite_col = 0
                        self.row = 7
                self.last_update = current_time

            
        else:
            # Estado neutral
            self.row = 7
            self.speed_x = 0
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite_col += 1
                self.image = self.animations[1][self.current_sprite_col]
                if self.current_sprite_col == 2:
                    self.current_sprite_col = 0

                self.last_update = current_time
                
            self.defense = False
            self.punch = False
    
    def jump(self):
        # Realiza un salto si el jugador final no ha alcanzado la parte superior de la pantalla
        if self.rect.y >= 0:
            self.speed_y = self.jump_power

    def shoot(self, game):
        # Realiza un disparo normal
        Shoot([game.all_sprites, game.player_shoots], self.rect.midright)
        
    def final_shot(self, game):
        # Realiza un disparo final
        FinalShoot([game.all_sprites, game.final_player_shoots], self.rect.bottomright)
    
    def life(self, game):
        # Muestra las vidas del jugador final en la pantalla
        for live in range(game.lives):
            blit_background(SCREEN, image_heart, black, (live * 16, 0))
