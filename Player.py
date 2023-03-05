import pygame.draw

class Player:
  colour = ""
  positionArray = []
  positionInt = 0
  
  def __init__(self,colour):
    self.colour = colour
    self.positionArray = [0,0]
    self.positionInt = 0

  def move(self,num):
    self.positionInt += num 
    self.postitionArray[1] += num
    
    if (self.positionInt<=0):
      self.positionInt = 0
      self.positionArray = [0,0]
      
    if (self.positionArray[1]>=10):
      self.positionArray[0]+=1
      self.positionArray[1]-=10
  
    elif (self.positionArray[1]<0):
      self.positionArray[0]-=1;
      self.positionArray[1]+=10


  def drawPlayerPiece(self,surface):
    pygame.draw.circle(surface,(100,0,0),[(self.positionArray[0]+1)*60,(self.positionArray[1]+1)*60],15,0) 

  
  def getPosArray(self):
    return self.positionArray
  def getPosInt(self):
    return self.positionInt
  def getColour(self):
    return self.colour

  