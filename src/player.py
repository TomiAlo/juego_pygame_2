import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from funciones import *
from shoot import Shoot

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet) -> None:
        """
        Inicializa la clase Player.

        Parameters:
        - groups: Grupos de sprites al que pertenece el jugador.
        - sprite_sheet: Instancia de SpriteSheet para gestionar las animaciones.
        """
        super().__init__(groups)
        self.animations = sprite_sheet.get_animations_player(1)
        self.image = self.animations[0][1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, HEIGHT_PLAYER)
        self.speed = 4
        self.jump_power = -10
        self.speed_y = 0
        self.speed_x = 0
        self.defense = False
        self.punch = False

    def update(self):
        """
        Actualiza la posición del jugador y gestiona eventos.
        """
        self.speed_y += GRAVITY
        self.rect.y += self.speed_y
            
        if self.rect.bottom >= HEIGHT_PLAYER:
            self.rect.bottom = HEIGHT_PLAYER
            self.speed_y = 0

        self.handle_events()

    def jump(self):
        """
        Realiza un salto si el jugador está en el suelo.
        """
        if self.rect.y >= 0:
            self.speed_y = self.jump_power
    
    def handle_events(self):
        """
        Gestiona eventos de teclado para controlar al jugador.
        """
        keys = pygame.key.get_pressed()

        if keys[K_d]:
            self.image = self.animations[0][2]
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                if keys[K_w]:
                    self.jump()
                
        elif keys[K_a]:
            self.image = self.animations[0][0]
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                if keys[K_w]:
                    self.jump()

        elif keys[K_w]:
            self.image = self.animations[1][1]
            self.jump()
        elif keys[K_s]:
            self.image = self.animations[1][0]
            self.defense = True

        elif keys[K_l]:
            self.image = self.animations[2][2]
        elif keys[K_j]:
            self.image = self.animations[1][2]
            self.punch = True

        else:
            self.speed_x = 0
            self.image = self.animations[0][1]
            self.defense = False
            self.punch = False
    
    def shoot(self, game):
        """
        Dispara un proyectil desde la posición del jugador.
        """
        Shoot([game.all_sprites, game.player_shoots], self.rect.midright)
    
    def life(self, game):
        """
        Dibuja corazones en la pantalla para representar vidas del jugador.
        """
        for life in range(game.lives):
            blit_background(SCREEN, image_heart, black, (life * 16, 0))
