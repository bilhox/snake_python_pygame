import pygame
import random
import  time

class Snake:

     def __init__(self):
          self.lenght = 3
          self.score = -1
          self.list = []
          self.is_food_here = False
          self.move_side = "RIGHT"
          self.food = None

          surface = pygame.image.load("./img/snake_fragments/frag_8.png")
          surface.convert_alpha()
          self.list.append([surface,[9*32,9*32]])

     
     def move(self,screen ,game_screen):
          surface = pygame.image.load("./img/snake_fragments/frag_1.png")
          if self.move_side == "RIGHT":
               pos = [self.list[len(self.list)-1][1][0] +32 ,self.list[len(self.list)-1][1][1]]
          elif self.move_side == "LEFT":
               pos = [self.list[len(self.list)-1][1][0] -32 ,self.list[len(self.list)-1][1][1]]
          elif self.move_side == "DOWN":
               pos = [self.list[len(self.list)-1][1][0],self.list[len(self.list)-1][1][1] +32]
          elif self.move_side == "UP":
               pos = [self.list[len(self.list)-1][1][0],self.list[len(self.list)-1][1][1] -32]
          self.list.append([surface,pos])

          if len(self.list)-1>self.lenght-1:
               self.list[0][0].fill([215,255,215])
               game_screen.blit(self.list[0][0],self.list[0][1])
               self.list.remove(self.list[0])

          for a,i in enumerate(self.list):

               if i == self.list[len(self.list)-1]:
                    i[0].fill([215,255,215])
                    if(self.move_side == "RIGHT"): surf = pygame.image.load("./img/snake_fragments/frag_8.png")
                    elif(self.move_side == "LEFT"): surf = pygame.image.load("./img/snake_fragments/frag_10.png")
                    elif(self.move_side == "DOWN"): surf = pygame.image.load("./img/snake_fragments/frag_9.png")
                    elif(self.move_side == "UP"): surf = pygame.image.load("./img/snake_fragments/frag_11.png")
                    i[0].blit(surf,(0,0))
               elif i == self.list[0]:
                    if i[1][0] == self.list[1][1][0]-32:
                         i[0].fill([215,255,215])
                         i[0].blit(pygame.image.load("./img/snake_fragments/frag_7.png"),[0,0])
                    elif i[1][0] == self.list[1][1][0]+32:
                         i[0].fill([215,255,215])
                         i[0].blit(pygame.transform.rotate(pygame.image.load("./img/snake_fragments/frag_7.png"), 180),[0,0])
                    elif i[1][1] == self.list[1][1][1]+32:
                         i[0].fill([215,255,215])
                         i[0].blit(pygame.transform.rotate(pygame.image.load("./img/snake_fragments/frag_7.png"), 90),[0,0])
                    elif i[1][1] == self.list[1][1][1]-32:
                         i[0].fill([215,255,215])
                         i[0].blit(pygame.transform.rotate(pygame.image.load("./img/snake_fragments/frag_7.png"), -90),[0,0])
               elif (i[1][0] == self.list[a+1][1][0]-32 and i[1][0] == self.list[a-1][1][0]+32) or (i[1][0] == self.list[a-1][1][0]-32 and i[1][0] == self.list[a+1][1][0]+32):
                    i[0].fill([215,255,215])
                    surf = pygame.image.load("./img/snake_fragments/frag_1.png")
                    i[0].blit(surf,(0,0))
               elif (i[1][1] == self.list[a+1][1][1]-32 and i[1][1] == self.list[a-1][1][1]+32) or (i[1][1] == self.list[a-1][1][1]-32 and i[1][1] == self.list[a+1][1][1]+32):
                    i[0].fill([215,255,215])
                    surf = pygame.transform.rotate(pygame.image.load("./img/snake_fragments/frag_1.png"),90)
                    i[0].blit(surf,(0,0))
               elif (i[1][1] == self.list[a+1][1][1]+32 and i[1][0] == self.list[a-1][1][0]-32) or (i[1][1] == self.list[a-1][1][1]+32 and i[1][0] == self.list[a+1][1][0]-32):
                    i[0].fill([215,255,215])
                    surf = pygame.image.load("./img/snake_fragments/frag_4.png")
                    i[0].blit(surf,(0,0))
               elif (i[1][1] == self.list[a+1][1][1]-32 and i[1][0] == self.list[a-1][1][0]-32) or (i[1][1] == self.list[a-1][1][1]-32 and i[1][0] == self.list[a+1][1][0]-32):
                    i[0].fill([215,255,215])
                    surf = pygame.image.load("./img/snake_fragments/frag_5.png")
                    i[0].blit(surf,(0,0))
               elif (i[1][1] == self.list[a+1][1][1]+32 and i[1][0] == self.list[a-1][1][0]+32) or (i[1][1] == self.list[a-1][1][1]+32 and i[1][0] == self.list[a+1][1][0]+32):
                    i[0].fill([215,255,215])
                    surf = pygame.image.load("./img/snake_fragments/frag_3.png")
                    i[0].blit(surf,(0,0))
               elif (i[1][1] == self.list[a+1][1][1]-32 and i[1][0] == self.list[a-1][1][0]+32) or (i[1][1] == self.list[a-1][1][1]-32 and i[1][0] == self.list[a+1][1][0]+32):
                    i[0].fill([215,255,215])
                    surf = pygame.image.load("./img/snake_fragments/frag_6.png")
                    i[0].blit(surf,(0,0))

               game_screen.blit(i[0],i[1])
          
          if(not self.is_food_here):
               if self.food != None:
                    surface = pygame.Surface((32,32))
                    surface.fill([215,255,215])
                    game_screen.blit(surface,self.food[1])
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
               
          if not self.lenght >= 361:
               game_surface.blit(self.food[0],self.food[1])
               
          self.is_food_here = True

