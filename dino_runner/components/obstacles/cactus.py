import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import (LARGE_CACTUS)
""" aqui agregar una instancia de obstacle manager para asi poner mi if """



class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        if self.image == LARGE_CACTUS:
            self.rect.y = 300
        else:
            self.rect.y = 320

        
    
        