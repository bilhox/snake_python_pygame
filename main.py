import pygame
from snake import *
from pygame.locals import *
import management

management.main()
while management.run:
     pass

pygame.init()

interval=0
win_size = [672+32,672+32]
gs_surface = [640,640]
velocity = management.velocity
screen = pygame.display.set_mode(win_size)
screen.fill([34, 107, 14])
game_surface = pygame.Surface([640,640])
game_surface.fill([215,255,215])
clock = pygame.time.Clock()
run = True
run_game = True
snake = Snake()

def events():
     global run
     global run_game
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                    run = False
                    run_game = False

while run:

     events()

     keys = pygame.key.get_pressed()

     if interval % velocity == 0 and interval != 0:
          snake.move(screen,game_surface)
          for n in snake.list:
               if n[1]==snake.list[len(snake.list)-1][1] and n != snake.list[len(snake.list)-1]:
                    game_surface.fill([215,255,215])
                    snake = Snake()
                    snake.move_side = "RIGHT"
               elif n[1][0] < 0 or n[1][1] < 0 or n[1][0] > gs_surface[0]-32 or n[1][1] > gs_surface[1]-32:
                    game_surface.fill([215,255,215])
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
          
     screen.blit(game_surface,[32,32])
     pygame.display.flip()
     clock.tick(200)

     interval += 1