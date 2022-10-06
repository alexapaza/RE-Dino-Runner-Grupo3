import pygame
from dino_runner.utils.constants import HEART 

class Heart:
    def __init__(self, x_position, y_position, x_velocity,):
        self.image=HEART
        self.rect=HEART.get_rect()
        self.rect_x=x_position
        self.rect_y=y_position

    def draw(self, screen):
        screen.blit(self.image, self.rect)