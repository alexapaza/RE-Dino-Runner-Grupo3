import pygame
import random
from dino_runner.utils.constants import BG,CLOUD,ICON,RUNNING,SCREEN_HEIGHT,SCREEN_WIDTH,TITLE,FPS
from dino_runner.components.dinosaur.dinosaur import dinosaur
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components.menu_score.text_utils import get_score_element, get_centered_message
from dino_runner.components.player_hearts.PlayerHeartManager  import PlayerHeartManager
from dino_runner.components.powerups.powerupmanager import PowerUpManager


class Game:
     def __init__ (self):
          pygame.init()
          pygame.display.set_caption(TITLE)
          pygame.display.set_icon(ICON)
          self.screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
          self.clock=pygame.time.Clock()
          self.color_bg=(33,33,33)
          # self.color_bg=(255,255,255)

          self.playing=False
          self.game_speed=20
          self.x_pos_bg=0
          self.y_pos_bg=380
          self.player=dinosaur()
          self.obstacle_manager=ObstacleManager()

          self.points=0
          self.running=True

          self.death_count=0
          self.player_heart_manager=PlayerHeartManager()
          self.power_up_manager=PowerUpManager()
     
     def run(self):
          self.obstacle_manager.reset_obstacles(self)
          self.player_heart_manager.reset_hearts()
          self.power_up_manager.reset_power_ups(self.points)
          self.playing=True
          while self.playing:
               self.events()
               self.updates()
               self.draw()
          # pygame.quit()
     
     def events(self):
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    self.playing=False
                    self.running=False
     def updates(self):
          user_input=pygame.key.get_pressed()
          self.player.update(user_input)
          self.obstacle_manager.update(self)
          self.power_up_manager.update(self.points,self.game_speed,self.player)

     def draw(self):
          self.clock.tick(FPS)
          self.screen.fill(self.color_bg)
          self.draw_background()
          self.player.draw(self.screen)
          self.obstacle_manager.draw(self.screen)
          self.score()
          self.player_heart_manager.draw(self.screen)
          self.power_up_manager.draw(self.screen)
          pygame.display.update()
          pygame.display.flip()

     def draw_background(self):
          image_with=BG.get_width()
          self.screen.blit(BG,(self.x_pos_bg,self.y_pos_bg))
          self.screen.blit(BG,(image_with+self.x_pos_bg,self.y_pos_bg))
          self.screen.blit(CLOUD,(image_with+self.x_pos_bg,100))
          if self.x_pos_bg<=-image_with:
               self.screen.blit(CLOUD,(image_with+self.x_pos_bg,100))
               self.screen.blit(BG,(image_with+self.x_pos_bg,150))
               self.x_pos_bg=0
          self.x_pos_bg-=self.game_speed

     def score(self):
          self.points+=1
          if self.points%100==0:
               self.game_speed+=1
          
          score,score_rect=get_score_element(self.points)
          self.screen.blit(score,score_rect)
          self.player.check_invincilibility(self.screen)

     def show_menu(self):
          self.running=True
          
          self.screen.fill((33,33,33))

          self.print_menu_elements(self.death_count)

          pygame.display.update()

          self.handle_key_events_on_menu()

     def print_menu_elements(self,death_count=0):
          half_screen_height=SCREEN_HEIGHT//2
          half_screen_width=SCREEN_WIDTH//2

          if death_count==0:
               text,text_rect=get_centered_message("press any key to start")
               self.screen.blit(text,text_rect)
          elif death_count>0:
               text,text_rect=get_centered_message("Press any key to Restart")
               score,score_rect=get_centered_message("Your score is: "+str(self.points),height=half_screen_height+50)
               
               self.screen.blit(score,score_rect)
               self.screen.blit(text,text_rect)
          self.screen.blit(RUNNING[0],(half_screen_width-20 ,half_screen_height-140))


     
     def handle_key_events_on_menu(self):
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    print("Dino: Good Bye")
                    self.runing=False
                    self.playing=False
                    pygame.display.quit()
                    pygame.quit()
                    exit()
               if event.type == pygame.KEYDOWN:
                    self.run()