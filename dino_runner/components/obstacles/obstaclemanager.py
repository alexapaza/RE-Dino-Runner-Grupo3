import random
import pygame
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.components.obstacles.large_cactus import LargeCactus




class ObstacleManger:
    def __init__(self):
        self.obstacles = []
        

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2):
                self.obstacles.append(Cactus(SMALL_CACTUS))
            
            elif random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

            #elif random.randint(0,2) == 2:
                #self.obstacles.append(Birds(BIRD))
                


      

       
       
       

        for obstacle in self.obstacles:
            obstacle.update( game.game_speed, self.obstacles )
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                #game.playing = False
                #game.death_count += 1
                #break
                
                if not game.player.shield:
                    self.obstacles = []
                    game.player_heart_manager.reduce_heart()

                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        #game.player_shield_time_up = start_time + 1000                   
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.obstacles.remove(obstacle)
                
            #if game.powerup.hammer.rect.colliderect(obstacle.rect):
                #if obstacle in self.obstacles:
                    #self.obstacles.remove(obstacle)



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []
