from turtle import Turtle
from random import choice
from math import atan,degrees
import time
class Ball(Turtle):
     def __init__(self):
          super().__init__()
          self.shape("circle")
          self.color('white')
          self.penup()
          self.goto(0,0)
          self.hideturtle
          self.x_move = 10
          self.y_move = 10
          self.time=0.09
          
     
     def move_ball(self):
          '''moves the ball to the top right corner'''
          new_x = self.xcor()+self.x_move 
          new_y = self.ycor()+self.y_move
          self.goto(new_x,new_y)
          
     
     def bounce_y(self):
          '''moves in the opposite direction vertically'''
          # increases the speed of the ball
          self.time*=0.9
          # move in the opposite direction 
          self.y_move*=-1
          
     def bounce_x(self):
          '''moves in the opposite direction horizontally'''
          # increases the speed of the ball
          self.time*=0.9
          # move in the opposite direction 
          self.x_move*=-1
          
     def reset_position(self):
          '''resets functionality of the ball '''
          # go back to the origin
          self.goto(0,0)
          # reset the speed
          self.time=0.11
          self.bounce_x()