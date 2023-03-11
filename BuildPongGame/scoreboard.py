from turtle import Turtle

class Scoreboard(Turtle):
     def __init__(self):
          super().__init__()
          self.score1 = 0
          self.score2 = 0
          self.color('white')
          self.center_lines()
          self.write_score()
          self.hideturtle()
          
     def center_lines(self):
          '''draws the center line'''
          self.pensize(5)
          self.penup()
          self.goto(0,300)
          while self.ycor() > -300:
               self.setheading(270)
               self.pendown()
               self.forward(20)
               self.penup()
               self.forward(20)

     def write_score(self):
          '''writes the score for both sides'''
          self.clear()
          self.center_lines()
          self.goto(100,280)
          self.write(f"Score: {self.score1}",False,align='center',font=('Arial','20','normal'))
          self.goto(-100,280)
          self.write(f"Score: {self.score2}",False,align='center',font=('Arial','20','normal'))
          
     def game_over(self):
          '''announces game over'''
          self.goto(0,0)
          self.write(f"GAME OVER",False,align='center',font=('Arial','20','normal'))