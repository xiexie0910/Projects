STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

        
    def up(self):
        '''controls the paddle to move up'''
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def level_up(self):
        '''takes the turtle back to starting position'''
        self.setposition(STARTING_POSITION)
        