import pygame
from dino_runner.utils.constants import RUNNING,DUCKING,JUMPING,DEFAULT_TYPE,SHIELD_TYPE,DUCKING_SHIELD,RUNNING_SHIELD,JUMPING_SHIELD
from pygame.sprite import Sprite


class dinosaur(Sprite):
    X_POS=80
    Y_POS=310
    Y_POS_DUCK=340
    JUMP_LEVEL=8.5

    def  __init__(self):
        # self.image=RUNNING[0]
        self.duck_img={DEFAULT_TYPE:DUCKING,SHIELD_TYPE:DUCKING_SHIELD}
        self.run_img={DEFAULT_TYPE:RUNNING,SHIELD_TYPE:RUNNING_SHIELD}
        self.jump_img={DEFAULT_TYPE:JUMPING,SHIELD_TYPE:JUMPING_SHIELD}

        self.type=DEFAULT_TYPE
        self.image=self.run_img[self.type][0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index=0
        self.dino_run=True
        self.dino_duck=False
        self.dino_jump=False
        self.jump_level=self.JUMP_LEVEL
        self.shield=True

        self.setup_states_boolenas()
 
    def setup_states_boolenas(self):
        self.has_powerup=False
        self.shield=False
        self.show_text=False
        self.shield_time_up=0

    def update(self,user_input):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()
        
        if user_input[pygame.K_DOWN]and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=True
            self.dino_jump=False
        elif user_input[pygame.K_UP]and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=False
            self.dino_jump=True
        elif not self.dino_jump:
            self.dino_run=True
            self.dino_duck=False
            self.dino_jump=False
        
        if self.step_index>=10:
            self.step_index=0

    def run(self):
        # self.image=RUNNING[0] if self.step_index<5 else RUNNING[1]
        self.image=self.run_img[self.type][self.step_index//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index+=1
    def duck(self):
        self.image=self.duck_img[self.type][self.step_index//5]
        # self.image =DUCKING[0] if self.step_index<5 else DUCKING[1]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS_DUCK
        self.step_index+=1    
        # self.dino_duck=False
        # self.dino_run=True
    def jump(self):
        self.image=self.jump_img[self.type]
        # self.image =JUMPING
        if (self.dino_jump):
            self.dino_rect.y-=(self.jump_level*4)
            self.jump_level-=0.8
        if (self.jump_level<-self.JUMP_LEVEL):
            self.dino_rect.y=self.Y_POS
            self.dino_jump=False
            self.jump_level=self.JUMP_LEVEL

    def draw (self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
    
    def check_invincilibility(self,screen):
        if self.shield:
            time_to_show=round((self.shield_time_up - pygame.time.get_ticks())//1000,2)
            if time_to_show>0:
                if self.show_text:
                    fond=pygame.font.Font("freesansbold.ttf", 18)
                    text=fond.render(f"shield enable for{time_to_show}",True,(0,0,0))
                    text_rect=text.get_rect()
                    text_rect.center=(500,40)
                    screen.blit(text,text_rect)
            else:
                self.shied=False
                self.update_default(SHIELD_TYPE)
        
    def update_default(self,current_type):
        if self.type==current_type:
            self.type=DEFAULT_TYPE
