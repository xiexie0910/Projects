from turtle import Turtle
from random import randint
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
     def __init__(self,position):
          super().__init__()
          self.shape('square')
          self.color('white')
          self.penup()
          self.setposition(position)
          self.shapesize(stretch_len=1,stretch_wid=5)
          
     
     def up(self):
          '''controls the paddle to move up'''
          new_y = self.ycor() + 20
          self.goto(self.xcor(),new_y)
          
          
     def down(self):
          '''controls the paddle to move down'''
          new_y = self.ycor() - 20
          self.goto(self.xcor(),new_y)

