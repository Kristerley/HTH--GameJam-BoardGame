import pygame
import pygame.draw
import random
import sys

import Player

# Initializing pygame
pygame.init()

# Board Title 
pygame.display.set_caption("Snakes and Ladders")

# Size of the display
surface = pygame.display.set_mode((720,600))

fps = 60
fpsClock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 10)

objects = []
#classes go here:

      
# Initializing Color
GREEN = (0,190,0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (255,0,0)
# Drawing Rectangle
square_num = 100
while True:
  print("Hello world")
  zxc = input("P")
  if  zxc == "P":
    break
for i in range(10):
  for j in range(10):
    switch = 0
    if (j+1)%2==0 and ((i+1)%2)==0:
      pygame.draw.rect(surface, GREEN, pygame.Rect((j*60), (i*60), 60, 60))
      top_left_num = font.render(str(square_num), True, BLACK)
      surface.blit(top_left_num, (j*60 +10, i*60 +10))
    elif((j+1)%2!=0 and ((i+1)%2)==0):
      pygame.draw.rect(surface, WHITE, pygame.Rect((j*60), (i*60), 60, 60))
      top_left_num = font.render(str(square_num), True, BLACK)
      surface.blit(top_left_num, (j*60 +10, i*60 +10))
    elif (j+1)%2==0 and ((i+1)%2)!=0:
      pygame.draw.rect(surface, WHITE, pygame.Rect((j*60), (i*60), 60, 60))
      top_left_num = font.render(str(square_num), True, BLACK)
      surface.blit(top_left_num, (j*60 +10, i*60 +10))
    elif((j+1)%2!=0 and ((i+1)%2)!=0):
      pygame.draw.rect(surface, GREEN, pygame.Rect((j*60), (i*60), 60, 60))
      top_left_num = font.render(str(square_num), True, BLACK)
      surface.blit(top_left_num, (j*60 +10, i*60 +10))
    square_num-=1

# Drawing row of black tiles for buttons etc
for k in range(10):
  pygame.draw.rect(surface, BLACK, pygame.Rect((660), (k*60), 60, 60))

# Dice roller randomized number
diceroller = random.randint(1,6)
print(diceroller)



# Ladders can bring you up 3 or 5 tiles
class Ladder:
  def __inti__(self):
    #side1 = 
    pass
  
def Snake():
  imp = pygame.image.load("snake.png").convert()
  # Using blit to copy content from one surface to other
  surface.blit(imp, (0, 0))

p1 = Player(BLUE)
p1.drawPlayerPiece()
  
# This is what draws everything onto the surface
pygame.display.flip()