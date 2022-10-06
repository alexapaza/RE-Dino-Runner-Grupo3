from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import HEART_COUNT

class PlayerHeartManager:
    def __init__(self):
        self.hearts_count = HEART_COUNT
    
    def reduce_heart(self):
        self.hearts_count-=1

    def draw (self,screen):
        x_position=10
        y_position=200
        for counter in range(self.hearts_count):
            heart=Heart(x_position,y_position)
            heart.draw(screen)
            x_position+=30
            
    def reset_hearts(self):
        self.hearts_count=HEART_COUNT