### Build Pong Game ###

from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
# initialize the screen, screen size, color 
screen = Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
# set tracer to False so that there is no drawing animation
screen.tracer(False)
# initialise all the required objects
leftpaddle = Paddle((-490,0))
rightpaddle = Paddle((480,0))
scoreboard = Scoreboard()
ball = Ball()
# listen out for keystrokes
screen.listen()
# listen out for the following keystrokes
screen.onkey(leftpaddle.up,"w")
screen.onkey(leftpaddle.down,"s")

screen.onkey(rightpaddle.up,"Up")
screen.onkey(rightpaddle.down,"Down")

# title   
screen.title("Build Pong Game")

# initialise the game is on variable
game_is_on = True
while game_is_on:
     time.sleep(ball.time)
     # update and move the ball on every iteration
     screen.update()
     ball.move_ball()
     
     # detect collision with the top wall
     if ball.ycor() >= 290 or ball.ycor() <= -290:
          ball.bounce_y()
     
     # if it goes out of bounds
     if ball.distance(rightpaddle)>55 and ball.xcor() > 480:
          ball.reset_position()
          scoreboard.score1 -= 1
          scoreboard.write_score()
     elif ball.distance(leftpaddle)>55 and ball.xcor() < -490:
          ball.reset_position()
          scoreboard.score2 -= 1
          scoreboard.write_score()
          
     # detect collision with the right paddle
     if ball.distance(rightpaddle)<55 and ball.xcor() > 460:
          ball.bounce_x()
          scoreboard.score1 += 1
          scoreboard.write_score()
     # detect collision with the left paddle
     elif ball.distance(leftpaddle)<55 and ball.xcor() < -470:
          ball.bounce_x()
          scoreboard.score2 += 1
          scoreboard.write_score()
          
     
          













screen.exitonclick()
