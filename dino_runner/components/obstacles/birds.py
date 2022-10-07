import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Birds(Obstacle):
    def __init___(self, image):
        self.type = 0
        
        super().__init__(image, self.type)
        self.rect.y = 260
        self.index = 0

    def draw(self, screen):
        if self.index >= 8:
            self.index= 0
        screen.blit(self.image[self.type//5], self.rect)
        self.index += 1



     