from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.finish_line
        self.write_score()

    def write_score(self):
          '''writes the current level'''
          self.clear()
          self.finish_line()
          self.goto(-280,260)
          self.write(f"Level: {self.level}",False,align='left',font=('Arial','20','normal'))

    
    def finish_line(self):
          '''draws the finish line'''
          self.pensize(5)
          self.penup()
          self.goto(-300,280)
          while self.xcor() < 300:
               self.setheading(0)
               self.pendown()
               self.forward(20)
               self.penup()
               self.forward(20)
               
    def level_up(self):
        '''increments the level'''
        self.level +=1
        self.clear()
        self.finish_line()
        self.write_score()

    def game_over(self):
        '''announces game over'''
        self.goto(0,0)
        self.write(f"GAME OVER",False,align='center',font=('Arial','20','normal'))
        
        