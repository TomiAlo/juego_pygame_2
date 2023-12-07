import pygame
from pygame.locals import *
from config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,groups, rect:pygame.Rect) -> None:
        super().__init__(groups)
        self.image=pygame.Surface((rect[2],rect[3]))
        self.rect=self.image.get_rect(topleft=(rect[0],rect[1]))
        self.image=pygame.transform.scale(image_platform,(rect[2],rect[3]))