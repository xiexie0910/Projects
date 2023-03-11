from turtle import Turtle, Screen
from random import randint
import math
import numpy as np

import colorgram as cg
turtle = Turtle()
screen = Screen()

# turtle.color('blue')
# colours = ['red','orange','yellow','green','blue','indigo','violet','pink']
# # drawing a square
# for _ in range(4):
#      turtle.forward(100)
#      turtle.right(90)
# turtle.left(90)

# # drawing a dashed line
# for i in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# drawing different shapes
# def shapes(num_sides):
#      angle = 360/num_sides
#      for _ in range(num_sides):
#           turtle.forward(100)
#           turtle.right(angle)

# for sides in range(3,11):
#      turtle.color(colours[sides-3])
#      shapes(sides)

#  random walking turtle
# turtle.speed(8)
# turtle.pensize(10)
# turtle.forward(10)
# screen.colormode(255)
# for _ in range(200):
#      turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
#      num = randint(0,1)
#      if num == 0:
#           turtle.left(90)
#      else:
#           turtle.right(90)
#      turtle.forward(20)
#      screen.update()

# drawing the spirograph

# screen.colormode(255)
# for _ in range(180):
#      turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
#      turtle.circle(100)
#      turtle.setheading(turtle.heading()+2)



#### drawing a heart that beats ###

# setting up the background color and pensize
screen.bgcolor("black")
turtle.pensize(5)
# set tracer to False so that there is no drawing animation
screen.tracer(False) # together with screen.update() to cancel the drawing animation
# hide the turtle for better visualisation
turtle.hideturtle() 
# setting the color
turtle.color('LightPink2')
# finding the width and height of the screen
width, height = screen.window_width(), screen.window_height()


# defining the heart function 
def heart(d,downdistance):
     ''' 
     This function takes two input parameters and calculates the measurements required to draw the heart
     
     
     ----------
     Parameters
     ----------
     
     d = diameter of the circle used to draw the top portion of the heart
     downdistance = how much the turtle shifts down by to draw the tip of the heart
     
     -------
     Outputs
     -------
     
     This function will return one fully drawn heart
     
     '''
     
     # finding the radius to use for the circle() function in turtle
     r = d/math.tan(math.radians(67.5))
     # lift pen up 
     turtle.penup()
     # go to the tip of the heart
     turtle.goto(0,downdistance)
     # point towards required action to begin drawwing
     turtle.setheading(45)
     # pen down
     turtle.pendown()
     # do forward by the diameter
     turtle.fd(d)     
     # draw a circle upto the degree of 225 
     turtle.circle(r,225)
     # turn in the opposite direction
     turtle.left(180)
     # draw another circle 
     turtle.circle(r,225)
     # go forward by the diameter
     turtle.fd(d)     
        
# set the size to be increasing
size = 'increase'
# using a for loop to simulate the beating count (one increase and one decrease is one heartbeat)
for i in range(10):
     if size =='increase':
          # using another for loop to change the size of the diameter and sub into the heart function
          for d in range(200,301):
               # fill the heart 
               turtle.begin_fill()
               # calling the heart function
               heart(d,-d/2)  
               turtle.end_fill()
               # updating the screen everytime the heart function is called to simulate heart increasing in size without any animation
               screen.update()
               # clear the drawing 
               turtle.clear()
          # set the size to decrease once the for loop finishes
          size = 'decrease'
     else:
          # similar idea as when size =='increase' except now the size of the heart decreases
          for d in range(300,199,-1):
               turtle.begin_fill()
               heart(d,-d/2)
               turtle.end_fill()
               screen.update()
               turtle.clear()
          size = 'increase'
          




     
    
screen.exitonclick()
