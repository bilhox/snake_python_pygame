import pygame
import time
from snake import *
from pygame.locals import *

pygame.init()

win_size = [640,640]
screen = pygame.display.set_mode(win_size)
run = True
grid_size = 50
clock = pygame.time.Clock()
snake = Snake()
interval=0

while run:

     keys = pygame.key.get_pressed()

     if interval % 30 == 0 and interval != 0:
          snake.move(screen)
          for n in snake.list:
               if n[1]==snake.list[len(snake.list)-1][1] and n != snake.list[len(snake.list)-1]:
                    screen.fill([0,0,0])
                    snake = Snake()
                    snake.move_side = "RIGHT"
               elif n[1][0] < 0 or n[1][1] < 0 or n[1][0] > win_size[0] or n[1][1] > win_size[1]:
                    screen.fill([0,0,0])
                    snake = Snake()
                    snake.move_side = "RIGHT"
     
     if (keys[K_RIGHT]-keys[K_LEFT] == 1):
          snake.move_side =  'RIGHT'
     elif (keys[K_RIGHT]-keys[K_LEFT] == -1):
          snake.move_side =  'LEFT'
     elif (keys[K_UP]-keys[K_DOWN] == 1):
          snake.move_side =  'UP'
     elif (keys[K_UP]-keys[K_DOWN] == -1):
          snake.move_side =  'DOWN'

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False

     pygame.display.flip()
     clock.tick(200)

     interval += 1