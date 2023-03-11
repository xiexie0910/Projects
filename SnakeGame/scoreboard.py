from turtle import Turtle
ALIGNMENT ='center'
FONT =('Arial','20','normal')
class Scoreboard(Turtle):
     
     def __init__(self):
          super().__init__()
          self.score = 0
          with open('data.txt', 'r') as file:
               data = []
               for i in file:
                    print(i)
                    data.append(int(i.removesuffix('\n')))
          
          self.highscore = data[-1]
          self.color('white')
          self.penup()
          self.goto(0,280)
          self.pendown()
          self.write(f"Score: {self.score} High Score: {self.highscore}",False,align=ALIGNMENT,font=FONT)
          self.hideturtle()
          
     def write_score(self):
          self.score +=1                     
          self.write(f"Score: {self.score} High Score: {self.highscore}",False,align=ALIGNMENT,font=FONT)

     def game_over(self):
          # self.goto(0,0)
          # self.write(f"GAME OVER",False,align='center',font=('Arial','20','normal'))
          if self.score > self.highscore:
               self.highscore = self.score
               with open('data.txt', 'a') as file:
                    file.write(f'\n{str(self.highscore)}')
          self.score = 0
          self.clear()
          self.write(f"Score: {self.score} High Score: {self.highscore}",False,align=ALIGNMENT,font=FONT)
          
          