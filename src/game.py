import pygame
from player import *
from config import *
from funciones import *
from sprite_sheet import *
from enemy import *
from platforms import Platform
from platform_trap import PlatformTrap
from seed import Seed
from enemy_shooter import EnemyShooter
from final_player import FinalPlayer
from cell import Cell

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen=SCREEN
        pygame.display.set_caption("Dragon ball: Saga Cell")
        pygame.display.set_icon(pygame.image.load("assets/images/esfera_del_dragon.png"))
        self.font=pygame.font.Font("assets/Kanit-Regular.ttf",30)
        
        self.sound_effect_punch=pygame.mixer.Sound("assets/sounds/golpe.mp3")
        self.sound_effect_punch.set_volume(0.10)
        
        self.sound_effect_shot=pygame.mixer.Sound("assets/sounds/shot.mp3")
        self.sound_effect_shot.set_volume(0.10)
        
        self.sound_effect_kamehameha=pygame.mixer.Sound("assets/sounds/kamehameha.mp3")
        self.sound_effect_kamehameha.set_volume(0.50)
        
        self.clock=pygame.time.Clock()
        
        self.json_file_path = 'assets/file/winners.json'
        default_data = [{"winner": "tomas", "score": 1}]

        self.data = load_json(self.json_file_path, default_data)
        
        self.puntaje=0
        
        self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
        self.rect_score_player = self.text_score_player.get_rect()
        self.rect_score_player.center=(WIDTH/2,30)
        
        self.name_player="player"
        
        self.all_sprites=pygame.sprite.Group()
        self.all_enemies=pygame.sprite.Group()
        self.all_enemies_shooters=pygame.sprite.Group()
        self.enemies_shoots=pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()
        self.platforms_two=pygame.sprite.Group()
        self.player_shoots=pygame.sprite.Group()
        self.player_final_shoot=pygame.sprite.Group()
        self.cell_final_shoot=pygame.sprite.Group()
        self.final_player_shoots=pygame.sprite.Group()
        
        self.seeds=pygame.sprite.Group()
        
        self.sprite_sheet_player_movement=SpriteSheet(pygame.image.load("./assets/sprites/gohan_movement.png").convert_alpha(),3,3,66,86)
        self.sprite_sheet_enemy_movement=SpriteSheet(pygame.image.load("./assets/sprites/celljr.png").convert_alpha(),3,3,70,70)
        self.sprite_sheet_final_player_movement=SpriteSheet(pygame.image.load("./assets/sprites/gohan_movement_ssj2.png").convert_alpha(),11,3,128,112)
        self.sprite_sheet_cell=SpriteSheet(pygame.image.load("./assets/sprites/cell.png").convert_alpha(),7,3,128,112)
        self.lives_cell=12
        self.lives=3
        
        
        self.flag_level_one=False
        self.flag_level_two=False
        self.flag_level_three=False
        self.flag_sound=True
    
    def run(self):
        while True:
            
            blit_background(SCREEN, image_background_presentation_scale, black, origin)
            
            show_message(SCREEN, "PRESIONE CUALQUIER TECLA", (WIDTH/2,350),white, (0,56,192), 15)
            pygame.display.flip()
            wait_user()
            
            while True:
                blit_background(SCREEN, image_background_presentation_scale,black,origin)
                btn_play,btn_option,btn_exit=create_start_menu()
                pygame.display.flip()
                start_menu_selected=wait_click_menu(btn_play["rect"], btn_option["rect"],btn_exit["rect"])
                
                if start_menu_selected==3:
                    pygame.quit()
                elif start_menu_selected==2:
                    blit_background(SCREEN, image_background_presentation_scale,black,origin)
                    btn_sound_on,btn_sound_off,btn_back=create_option_menu()
                    pygame.display.flip()
                    option_menu_selected=wait_click_menu_option(btn_sound_on["rect"], btn_sound_off["rect"],btn_back["rect"])
                    if option_menu_selected==1:
                        self.flag_sound=True
                    elif option_menu_selected==2:
                        self.flag_sound=False
                    
                elif start_menu_selected==1:
                    running=True
                    while running:
                        
                        blit_background(SCREEN, image_level_selector_scale,black,origin)
                        SCREEN.blit(self.text_score_player, self.rect_score_player)
                        if self.lives==0:
                            self.puntaje=0
                            self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                            show_message(SCREEN, "Has perdido todas las vidas...",(WIDTH // 4, HEIGHT // 2 + 50 + 3 * (40 + 10)),white,(63, 164, 250),15)
                        pygame.display.flip()
                        
                        if self.flag_level_one==False:
                            btn_level_one=create_level_btn_one()
                            
                            option_menu_level_selected=wait_click_menu_level_one(btn_level_one["rect"])
                            
                            if option_menu_level_selected==0:
                                running=False
                            
                        elif self.flag_level_one==True and self.flag_level_two==False:
                            btn_level_one=create_level_btn_one()
                            btn_level_two=create_level_btn_two()
                            option_menu_level_selected=wait_click_menu_level_two(btn_level_one["rect"], btn_level_two["rect"])
                            if option_menu_level_selected==0:
                                running=False
                            
                        elif self.flag_level_one==True and self.flag_level_two==True:
                            btn_level_one=create_level_btn_one()
                            btn_level_two=create_level_btn_two()
                            btn_level_three=create_level_btn_three()
                            option_menu_level_selected=wait_click_menu_level_three(btn_level_one["rect"], btn_level_two["rect"],btn_level_three["rect"])
                            if option_menu_level_selected==0:
                                running=False
                            
                        if option_menu_level_selected==1:
                            self.lives=3
                            self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                            self.run_level_one()

                        elif option_menu_level_selected==2:
                            self.lives=3            
                            self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                            self.run_level_two()

                        elif option_menu_level_selected==3:
                            self.lives=3
                            self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                            self.run_level_three()
                            

    def draw(self):
        SCREEN.blit(image_background_level_scale, origin)
        self.all_sprites.draw(self.screen)
        SCREEN.blit(self.text_score_player, self.rect_score_player)
        self.all_enemies.draw(self.screen)
        self.all_enemies_shooters.draw(self.screen)
        self.player.life(self)

    def update(self):
        self.all_sprites.update()
        self.all_enemies.update()
        pygame.display.flip()

    def close(self):
        pygame.quit()
    
    def detect_collisions_shoots(self):
        #pygame.sprite.groupcollide(self.all_enemies, self.player_shoots,True, True)
        hits=pygame.sprite.groupcollide(self.all_enemies_shooters, self.player_shoots,True, True)
        for hit in hits:
            self.puntaje+=200
        self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)

    
    def detect_collisions(self):
        
        hits=pygame.sprite.spritecollide(self.player, self.all_enemies,True)
        for hit in hits:
            self.lives-=1
            if self.lives==0:
                self.player.kill()
                return 0
    
    def detect_collisions_enemies_shooters(self):
        hits=pygame.sprite.spritecollide(self.player, self.enemies_shoots,True)
        for hit in hits:
            self.lives-=1
            if self.lives==0:
                self.player.kill()
                return 0
    
    def detect_collision_cell_shoot(self):
        hits=pygame.sprite.spritecollide(self.cell, self.player_shoots, True)
        for hit in hits:
            self.lives_cell-=1
            if self.lives_cell==0:
                self.cell.kill()
                self.puntaje=self.puntaje+1000
                self.flag_level_three=True
                self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                update_json(self.json_file_path, self.name_player, self.puntaje, self.data)
                return 0
        hits=pygame.sprite.spritecollide(self.cell, self.final_player_shoots, True)
        for hit in hits:
            self.lives_cell-=2
            if self.lives_cell<=0:
                self.cell.kill()
                self.puntaje=self.puntaje+1000
                self.flag_level_three=True
                self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)
                update_json(self.json_file_path, self.name_player, self.puntaje, self.data)
                return 0
        
        
    def detect_collision_platform(self):
        
        platforms_collide=pygame.sprite.spritecollide(self.player, self.platforms, False)
        
        for platform in platforms_collide:
            if self.player.rect.bottom>=platform.rect.top and self.player.speed_y>0:
                self.player.rect.bottom=platform.rect.top
                self.player.speed_y=0
        
    def detect_collision_platform_two(self):
        
        hits=pygame.sprite.spritecollide(self.player, self.platforms_two, True)
        
        if hits:
            self.lives-=1
            if self.lives==0:
                self.player.kill()
                return 0

    def detect_collision_seed(self):
        
        hits=pygame.sprite.spritecollide(self.player, self.seeds, True)
        if hits:
            self.lives+=1
        
    def detect_collisions_punch(self):
        hits=pygame.sprite.spritecollide(self.player, self.all_enemies,True)
        for hit in hits:
            self.puntaje+=100
            self.text_score_player=self.font.render(f"score: {self.puntaje}",True,white)


    def run_level_one(self):
        
        #Platform([self.all_sprites, self.platforms],(0,400,100,20))   #x,y,width,height    
        Platform([self.all_sprites, self.platforms],(900,200,100,20))
        Platform([self.all_sprites, self.platforms],(300,300,100,20))
        
        PlatformTrap([self.all_sprites, self.platforms_two],(0,400,100,20))
        
        Seed([self.all_sprites, self.seeds],(300,250,30,30))

        self.player = Player([self.all_sprites],self.sprite_sheet_player_movement)
        self.enemies= [Enemy([self.all_sprites,self.all_enemies],self.sprite_sheet_enemy_movement,900,470)]
        self.enemies_shooters=[EnemyShooter([self.all_sprites,self.all_enemies_shooters],self.sprite_sheet_enemy_movement,900,130)] 
        
        running=True
        EVENT_SHOOT_ENEMY = pygame.USEREVENT + 1 
        pygame.time.set_timer(EVENT_SHOOT_ENEMY, 2000)
        
        EVENT_ADD_ENEMY = pygame.USEREVENT + 2
        pygame.time.set_timer(EVENT_ADD_ENEMY, 5000)
        
        while running:
            for event in pygame.event.get():
                self.clock.tick(FPS)
                if event.type == pygame.QUIT:
                    running=False
                    self.player.kill()
                    self.end_enemies_player()
                    self.end_sprites()
                        
                if event.type == EVENT_ADD_ENEMY:
                    self.enemies.append(Enemy([self.all_sprites,self.all_enemies],self.sprite_sheet_enemy_movement,900,470))
                if event.type == EVENT_SHOOT_ENEMY and self.all_enemies_shooters:
                    for enemy_shooter in self.enemies_shooters:
                        enemy_shooter.shoot(self)
                if event.type ==KEYDOWN:
                    if event.key==K_l:
                        self.sound_effect_shot.play()
                        self.player.shoot(self)
                    if event.key==K_s:
                        self.player.defense=True
                    if event.key==K_j:
                        self.player.punch=True
                        self.sound_effect_punch.play()
                    if event.key==K_p:
                        wait_user_pause()

            self.update()
            self.detect_collision_platform()
            self.detect_collisions_shoots()
            self.detect_collision_seed()
            if not self.player.defense and not self.player.punch:
                if self.detect_collisions()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
                if self.detect_collisions_enemies_shooters()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
                if self.detect_collision_platform_two()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
            elif self.player.punch:
                self.detect_collisions_punch()

            self.draw()
            if not self.all_enemies_shooters and  not self.all_enemies:
                self.player.kill()
                self.end_sprites()
                self.flag_level_one=True
                running=False
    
    def run_level_two(self):
        
        Platform([self.all_sprites, self.platforms],(0,200,100,20))
        Platform([self.all_sprites, self.platforms],(900,200,100,20))
        Platform([self.all_sprites, self.platforms],(200,400,100,20))
        
        PlatformTrap([self.all_sprites, self.platforms_two],(400,300,100,20))
        
        Seed([self.all_sprites, self.seeds],(0,180,30,30))

        self.player = Player([self.all_sprites],self.sprite_sheet_player_movement)
        self.enemies= [Enemy([self.all_sprites,self.all_enemies],self.sprite_sheet_enemy_movement,900,470)]
        self.enemies_shooters=[EnemyShooter([self.all_sprites,self.all_enemies_shooters],self.sprite_sheet_enemy_movement,900,130),
                            EnemyShooter([self.all_sprites,self.all_enemies_shooters],self.sprite_sheet_enemy_movement,900,450)] 
        
        running=True
        EVENT_SHOOT_ENEMY = pygame.USEREVENT + 1 
        pygame.time.set_timer(EVENT_SHOOT_ENEMY, 2000)
        
        EVENT_ADD_ENEMY = pygame.USEREVENT + 2
        pygame.time.set_timer(EVENT_ADD_ENEMY, 10000)
        
        while running:
            for event in pygame.event.get():
                self.clock.tick(FPS)
                if event.type == pygame.QUIT:
                    running=False
                    self.player.kill()
                    self.end_enemies_player()
                    self.end_sprites()
                        
                if event.type == EVENT_ADD_ENEMY:
                    self.enemies.append(Enemy([self.all_sprites,self.all_enemies],self.sprite_sheet_enemy_movement,600,130))
                if event.type == EVENT_SHOOT_ENEMY and self.all_enemies_shooters:
                    for enemy_shooter in self.enemies_shooters:
                        if enemy_shooter.alive():
                            enemy_shooter.shoot(self)
                if event.type ==KEYDOWN:
                    if event.key==K_l:
                        if self.flag_sound:
                            self.sound_effect_shot.play()
                        self.player.shoot(self)
                    if event.key==K_s:
                        self.player.defense=True
                    if event.key==K_j:
                        if self.flag_sound:
                            self.sound_effect_punch.play()
                        self.player.punch=True
                    if event.key==K_p:
                        wait_user_pause()

            self.update()
            self.detect_collision_platform()
            self.detect_collisions_shoots()
            self.detect_collision_seed()
            if not self.player.defense and not self.player.punch:
                if self.detect_collisions()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
                if self.detect_collisions_enemies_shooters()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
                if self.detect_collision_platform_two()==0:
                    self.end_sprites()
                    self.end_enemies_player()
                    running=False
            elif self.player.punch:
                self.detect_collisions_punch()

            self.draw()
            if not self.all_enemies_shooters and not self.all_enemies:
                self.player.kill()
                self.flag_level_two=True
                self.end_sprites()
                running=False

    def run_level_three(self):
        EVENT_SHOOT_CELL = pygame.USEREVENT + 3 
        pygame.time.set_timer(EVENT_SHOOT_CELL, 2000)
        
        EVENT_JUMP_CELL = pygame.USEREVENT + 4
        pygame.time.set_timer(EVENT_JUMP_CELL, 4000)
        
        EVENT_DEFENSE_CELL = pygame.USEREVENT + 5 
        pygame.time.set_timer(EVENT_DEFENSE_CELL, 5000)

        self.player=FinalPlayer([self.all_sprites],self.sprite_sheet_final_player_movement,self)
        self.cell=Cell([self.all_enemies],self.sprite_sheet_cell,870,300)
        running=True
        while running:
            for event in pygame.event.get():
                self.clock.tick(FPS)
                if event.type == pygame.QUIT:
                    running=False
                    self.player.kill()
                    self.cell.kill()
                    self.end_sprites()
                if event.type ==KEYDOWN:
                    if event.key==K_l:
                        if self.flag_sound:
                            self.sound_effect_shot.play()
                        self.player.shoot(self)
                    if event.key==K_s:
                        self.player.defense=True
                        self.cell.defense=True
                    if event.key==K_j:
                        if self.flag_sound:
                            self.sound_effect_punch.play()
                        self.player.punch=True
                    if event.key==K_k:
                        if self.flag_sound:
                            self.sound_effect_kamehameha.play()
                    if event.key==K_p:
                        wait_user_pause()
                if event.type==EVENT_SHOOT_CELL:
                    self.cell.shoot(self)
                    
                # if event.type==EVENT_JUMP_CELL:
                #     self.cell.jump()
                    
            self.update()
            self.detect_collisions_shoots()
            if self.detect_collision_cell_shoot()==0:
                    running=False
                    self.end_sprites()
                    self.player.kill()
                    self.cell.kill()
            self.detect_collision_cell_shoot()
            if not self.player.defense and not self.player.punch:
                if self.detect_collisions()==0:
                    running=False
                    self.end_sprites()
                    self.player.kill()
                    self.cell.kill()
                if self.detect_collisions_enemies_shooters()==0:
                    running=False
                    self.end_sprites()
                    self.player.kill()
                    self.cell.kill()
                
            elif self.player.punch:
                self.detect_collisions_punch()
            self.update()
            self.draw()
            self.cell.life(self)
    
    def end_sprites(self):
        for platform in self.platforms:
            platform.kill()
        self.all_sprites=pygame.sprite.Group()
    
    def end_enemies_player(self):
        for enemy_shooter in self.enemies_shooters:
            enemy_shooter.kill()
        for enemy in self.enemies:
            enemy.kill()