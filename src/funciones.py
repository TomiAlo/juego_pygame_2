import pygame
from pygame.locals import *
from config import *
import json
import sqlite3

def blit_background(screen, image_path, colour, position):
    """
    blit_background blitea en la superficie la imagen que recibe por parametro
    si imagine_path no tiene un path correcto blitea la pantalla de negro
    quien no depende de un path sino del archivo config.py
    
    recibe por parametros la surface, la variable con el path de la imagen, el color y la posicion
    no retorna nada
    """
    try:
        screen.blit(image_path, position)
    except FileNotFoundError:
        screen.blit(colour, position) 

def create_btn (text, size,coordenates ,font_color, color, font_size):

    """
    create_btn recibe por parametros un texto, un tamaño, coordenadas, el color del texto, color del boton, y el tamaño del texto

    esta funcion asigna los parametros recibidos a variables que luego se asignaran a un diccionario de un boton 

    retorna el diccionario con los parametros recibidos
    """
    font=pygame.font.Font("assets/Kanit-Regular.ttf",font_size)
    btn=pygame.Surface(size)
    sup_text= font.render(text, True, font_color)
    rect_text=sup_text.get_rect()
    rect_btn=btn.get_rect()
    rect_btn.center=coordenates
    rect_text.center=rect_btn.center
    
    rect_text.center=rect_btn.center
    btn.fill(color)
    
    return {"btn":btn,"rect": rect_btn,"sup_text":sup_text,"rect_text":rect_text ,"color": color}

def wait_click_start_menu(rect_btn):

    """
    
    """
    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    pygame.quit()
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn):
                    return 1    

def punto_en_rectangulo(punto, rect):
    x, y=punto
    return x>=rect.left and x<=rect.right and y>=rect.top and y<=rect.bottom

def create_level_btn_one():
    vertical_offset = 50  # Puedes ajustar este valor según tus necesidades
    button_width, button_height = 150, 40

    # Crear botones de selección de niveles
    btn_level1_background = create_btn("LEVEL 1", (button_width, button_height), (WIDTH // 4, HEIGHT // 2 + vertical_offset), white, (0, 56, 192), 15)

    # Mostrar botones en la pantalla
    SCREEN.blit(btn_level1_background["btn"], btn_level1_background["rect"])
    x_level1 = btn_level1_background["sup_text"].get_rect()
    x_level1.center = (WIDTH // 4, HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_level1_background["sup_text"], x_level1)
    pygame.display.flip()

    return btn_level1_background

def create_level_btn_two():
    vertical_offset = 50  # Puedes ajustar este valor según tus necesidades
    button_width, button_height = 150, 40
    btn_level2_background = create_btn("LEVEL 2", (button_width, button_height), (WIDTH // 4, HEIGHT // 2 + vertical_offset + button_height + 10), white, (0, 56, 192), 15)

    SCREEN.blit(btn_level2_background["btn"], btn_level2_background["rect"])
    x_level2 = btn_level2_background["sup_text"].get_rect()
    x_level2.center = (WIDTH // 4, HEIGHT // 2 + vertical_offset + button_height + 10)
    SCREEN.blit(btn_level2_background["sup_text"], x_level2)
    pygame.display.flip()

    return btn_level2_background
    
def create_level_btn_three():
    vertical_offset = 50  # Puedes ajustar este valor según tus necesidades
    button_width, button_height = 150, 40
    
    btn_level3_background = create_btn("LEVEL 3", (button_width, button_height), (WIDTH // 4, HEIGHT // 2 + vertical_offset + 2 * (button_height + 10)), white, (0, 56, 192), 15)
    
    SCREEN.blit(btn_level3_background["btn"], btn_level3_background["rect"])
    x_level3 = btn_level3_background["sup_text"].get_rect()
    x_level3.center = (WIDTH // 4, HEIGHT // 2 + vertical_offset + 2 * (button_height + 10))
    SCREEN.blit(btn_level3_background["sup_text"], x_level3)
    pygame.display.flip()

    return btn_level3_background


def create_start_menu():
    vertical_offset = 50  # Puedes ajustar este valor según tus necesidades

    btn_play_background = create_btn("PLAY", (150, 40), (WIDTH // 4, HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)
    btn_options_background = create_btn("OPTIONS", (150, 40), (WIDTH // 2, HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)
    btn_exit_background = create_btn("EXIT", (150, 40), (3 * (WIDTH // 4), HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)

    SCREEN.blit(btn_play_background["btn"], btn_play_background["rect"])
    x = btn_play_background["sup_text"].get_rect()
    x.center = (WIDTH // 4, HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_play_background["sup_text"], x)

    SCREEN.blit(btn_options_background["btn"], btn_options_background["rect"])
    y_options = btn_options_background["sup_text"].get_rect()
    y_options.center = (WIDTH // 2, HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_options_background["sup_text"], y_options)

    SCREEN.blit(btn_exit_background["btn"], btn_exit_background["rect"])
    y_exit = btn_exit_background["sup_text"].get_rect()
    y_exit.center = (3 * (WIDTH // 4), HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_exit_background["sup_text"], y_exit)

    pygame.display.flip()
    
    return btn_play_background,btn_options_background,btn_exit_background

def create_option_menu():
    vertical_offset = 50  # Puedes ajustar este valor según tus necesidades

    btn_sound_on = create_btn("SOUND ON", (150, 40), (WIDTH // 4, HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)
    btn_sound_off = create_btn("SOUND OFF", (150, 40), (WIDTH // 2, HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)
    btn_back = create_btn("BACK", (150, 40), (3 * (WIDTH // 4), HEIGHT // 2 + vertical_offset), white, (0,56,192), 15)

    SCREEN.blit(btn_sound_on["btn"], btn_sound_on["rect"])
    x = btn_sound_on["sup_text"].get_rect()
    x.center = (WIDTH // 4, HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_sound_on["sup_text"], x)

    SCREEN.blit(btn_sound_off["btn"], btn_sound_off["rect"])
    y_options = btn_sound_off["sup_text"].get_rect()
    y_options.center = (WIDTH // 2, HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_sound_off["sup_text"], y_options)

    SCREEN.blit(btn_back["btn"], btn_back["rect"])
    y_exit = btn_back["sup_text"].get_rect()
    y_exit.center = (3 * (WIDTH // 4), HEIGHT // 2 + vertical_offset)
    SCREEN.blit(btn_back["sup_text"], y_exit)

    pygame.display.flip()
    
    return btn_sound_on,btn_sound_off,btn_back

def wait_click_menu_level_one(btn_level_one):

    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    return 0
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_one):
                    return 1
            

def wait_click_menu_level_two(btn_level_one, btn_level_two):

    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    return 0
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_one):
                    return 1
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_two):
                    return 2


def wait_click_menu_level_three(btn_level_one, btn_level_two, btn_level_three):

    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    return 0
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_one):
                    return 1
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_two):
                    return 2
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, btn_level_three):
                    return 3

def wait_click_menu(rect_btn_play, rect_btn_option, rect_btn_exit):

    """
    
    """
    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    pygame.quit()
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_play):
                    return 1
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_option):
                    return 2
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_exit):
                    return 3

def wait_click_menu_option(rect_btn_sound_on, rect_btn_sound_off,rect_btn_back):
    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    pygame.quit()
            if e.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_sound_on):
                    return 1
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_sound_off):
                    return 2
            if e.type ==MOUSEBUTTONDOWN:
                if punto_en_rectangulo(e.pos, rect_btn_back):
                    return 

def wait_user():
    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    pygame.quit()
                return

def show_message(surface, text, coordenates, font_color, background, font_size):
    """
    show_message recibe por parametros la surface del juego, un text, coordenadas, el color del texto,
    el color del fondo, y el tamaño del texto

    esta funcion creara un texto con las configuraciones que recibe por parametro,
    y tambien "blitea" el texto

    no retorna nada
    """
    font=pygame.font.Font("assets/Kanit-Regular.ttf",font_size)
    sup_text= font.render(text, True, font_color, background)
    rect_text = sup_text.get_rect()
    rect_text.center = coordenates
    surface.blit(sup_text, rect_text)


def build_rect(left=150, top=150, width=50, height=50, color=(250,250,250), border=0, radius=-1):
    return {"rect":pygame.Rect(left,top,width,height),"color":color, "borde":border, "radio":radius}

def wait_user_pause():
    
    blit_background(SCREEN, image_background_controls_scale,black,origin)
    pygame.display.flip()
    running=True
    while running:
        for e in pygame.event.get():
            if e.type==QUIT:
                running=False
            if e.type==KEYDOWN:
                return
        
def load_json(json_file_path):
    """
    load_json se encarga de verificar que haya un archivo json
    si no existe crea uno y guarda default_data
    
    recibe como parametros el path del archivo json y el contenido por default que deberia llevar el json
    retorna el contenido del json en data 

    """

    with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    

    return data

def update_json(json_file_path, name_player, count_player, data):
    """
    update_json agrega a la lista el puntaje que retorno el json y reescribe el json con el nuevo ganador
    
    recibe como parametros el path del json, los datos de los jugadores y el contenido del json
    """
    winner = {'winner': name_player, 'score': count_player}

    data.append(winner)

    with open(json_file_path, "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)
    
def connect_to_database():
    connection = sqlite3.connect('sqlite.db')
    return connection

def create_scores_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            player_name TEXT,
            score INTEGER
        )
    ''')
    connection.commit()

def save_score(self):
    cursor = self.connection.cursor()
    data=cursor.execute("SELECT * FROM scores")
    print(data.fetchall())
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (self.name_player, self.puntaje))
    self.connection.commit()
    

def close_database_connection(self):
    self.connection.close()

def show_top_scores(self, limit=3):
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    return cursor.fetchall()