import pygame
import random

class Snake:

     def __init__(self):
          self.lenght = 3
          self.score = -1
          self.list = []
          self.is_food_here = False
          self.move_side = "RIGHT"
          self.food = None

          surface = pygame.Surface([32,32])
          surface.fill([255,0,0])
          self.list.append([surface,[9*32,9*32]])

     
     def move(self,screen ,game_screen):
          surface = pygame.Surface([32,32])
          if self.move_side == "RIGHT":
               pos = [self.list[len(self.list)-1][1][0] +32 ,self.list[len(self.list)-1][1][1]]
          elif self.move_side == "LEFT":
               pos = [self.list[len(self.list)-1][1][0] -32 ,self.list[len(self.list)-1][1][1]]
          elif self.move_side == "DOWN":
               pos = [self.list[len(self.list)-1][1][0],self.list[len(self.list)-1][1][1] +32]
          elif self.move_side == "UP":
               pos = [self.list[len(self.list)-1][1][0],self.list[len(self.list)-1][1][1] -32]
          surface.fill([255,255,255])
          self.list.append([surface,pos])

          if len(self.list)-1>self.lenght-1:
               self.list[0][0].fill([215,255,215])
               game_screen.blit(self.list[0][0],self.list[0][1])
               self.list.remove(self.list[0])

          for i in self.list:
               
               h = 191+(int(64 / self.lenght)*(self.list.index(i)+1))

               i[0].fill([h,0,0])

               game_screen.blit(i[0],i[1])
          
          if(not self.is_food_here):
               self.spawnFood(game_screen)
               self.score += 1
               surface = pygame.Surface((200,672+32))
               surface.fill([255,255,255])
               screen.blit(surface,(0,0))
               screen.blit(pygame.font.Font("./fonts/Urbanist.ttf", 30).render(f"SCORE : {self.score}", True, (0, 0, 0)), (20, 20))

          if self.food[1] == self.list[len(self.list)-1][1]:
               self.lenght += 1
               self.is_food_here = False
          

     
     def spawnFood(self,game_surface):
          food = pygame.image.load("./img/apple.png")
          food.convert_alpha()

          search = True
          while search:
               search = False
               self.food=[food,[random.randint(0,19)*32,random.randint(0,19)*32]]
               for n in self.list:
                    if self.food[1]==n[1]:
                         search = True
          game_surface.blit(self.food[0],self.food[1])
               
          self.is_food_here = True

