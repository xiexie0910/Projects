### Snake Game ###


# import required functions and initial setups
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# initialize the screen and the size of the screen and background color
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
# set tracer to false so that there is no drawing animation
screen.tracer(False)
# creating all the required instances 
food = Food()
snake = Snake()
scoreboard = Scoreboard()

# listen out for keystrokes
screen.listen()
# listen out for the following keystrokes
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# title 
screen.title("My Snake Game")

# when the game is on, the snake will move
game_is_on = True
while game_is_on:
     screen.update()
     time.sleep(0.1)
     snake.move_snakes()

     # detect collision of food and snake
     if snake.head.distance(food) < 15:
          food.refresh()
          snake.extend()
          scoreboard.clear()
          scoreboard.write_score()

     # detect collision with wall
     if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
          scoreboard.game_over()
          snake.snake_reset()

     # detect tail collision
     for segments in snake.segments[1:]:
          if snake.head.distance(segments) < 10:
               snake.snake_reset()
               scoreboard.game_over()




screen.exitonclick()