import random
from dino_runner.utils.constants import SCREEN_HEIGHT
from pygame.sprite import Sprite
import pygame

class PowerUp(Sprite):
    def __init__(self,image,tipe):
        self.image = image
        self.rect=image.get_rect()
        self.type=tipe
        self.rect.x=SCREEN_HEIGHT+random.randint(800,1000)
        self.rect.y=random.randint(100,150)
        print(self.rect)

        self.start_time=0

        self.width=self.image.get_width()

    def update(self,game_speed,powerups):
        self.rect.x=self.rect.x-game_speed

        if self.rect.x<-self.width:
            powerups.pop()
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect))
