from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake:

     def __init__(self):
          self.segments=[]
          self.create_snakes()
          self.head = self.segments[0]
          
     def create_snakes(self):
          for i in range(3):
               turtle=Turtle("square")
               turtle.color("white")
               self.segments.append(turtle)
               turtle.penup()
               turtle.setposition(-i*20,0)
               
     def move_snakes(self):
          for segnum in range(len(self.segments)-1,0,-1):
               new_x = self.segments[segnum-1].xcor()
               new_y = self.segments[segnum-1].ycor()
               self.segments[segnum].goto(new_x,new_y)
               
          self.head.forward(MOVE_DISTANCE)
          
     def up(self):
          if self.head.heading() != DOWN:
               self.head.setheading(UP)

          
     def down(self):
          if self.head.heading() != UP:
               self.head.setheading(DOWN)

          
     def left(self):
          if self.head.heading() != RIGHT:
               self.head.setheading(LEFT)
          
     def right(self):
          if self.head.heading() != LEFT:
               self.head.setheading(RIGHT)
               
     def extend(self):
          # adds a new segment to the snake
          turtle=Turtle("square")
          turtle.color("white")
          self.segments.append(turtle)
          turtle.penup()
          turtle.setposition(self.segments[-1].position())

     def snake_reset(self):
          for seg in self.segments:
               seg.goto(1000,1000)
          self.segments.clear()
          self.create_snakes()
          self.head = self.segments[0]