import pygame
import json

json_file_path = 'assets/file/data.json'

with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)


WIDTH=data[0]["width"]
HEIGHT=data[1]["height"]
HEIGHT_PLAYER=data[2]["height_player"]
FPS =data[3]["fps"]
GRAVITY=data[4]["gravity"]

image_background_level= pygame.image.load("assets/images/background_level.png")
image_background_level_scale=pygame.transform.scale(image_background_level, (WIDTH, HEIGHT))

image_background_controls=pygame.image.load("assets/images/background_controls.jpg")
image_background_controls_scale = pygame.transform.scale(image_background_controls, (WIDTH, HEIGHT))

image_background_presentation=pygame.image.load("assets/images/image_presentation.png")
image_background_presentation_scale=pygame.transform.scale(image_background_presentation, (WIDTH, HEIGHT))

image_level_selector=pygame.image.load("assets/images/image_level_menu.png")
image_level_selector_scale=pygame.transform.scale(image_level_selector, (WIDTH, HEIGHT))

image_heart=pygame.image.load("assets/images/heart.png")

image_platform=pygame.image.load("assets/images/platform1.png")
image_platform_two=pygame.image.load("assets/images/platform2.png")

image_seed=pygame.image.load("assets/images/seed.png")

UpRight=9
DownRight=3
DownLeft=1
UpLeft=7

SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))

black=(0,0,0)
white=(255,255,255)
red =(255,0,0)
green=(34,139,34)
blue=(42,157,244)

origin=(0,0)



