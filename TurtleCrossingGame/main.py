import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# initialising the screen instance and setting up the dimensions of the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating a player object 
player = Player()
car = CarManager()
scoreboard = Scoreboard()
# listen out for keystrokes 
screen.listen()
# listen out for the following keystrokes   
screen.onkey(player.up,"Up")


# title   
screen.title("Turtle Crossing Game")

# initialise the game is on variable 
game_is_on = True
while game_is_on:   
    time.sleep(0.1)
    screen.update()
    # using a for loop to move every car forward by a set distance 
    for i in range(len(car.all_cars)):
        car.move_x()
    
    # when the player reaches beyond the finish line 
    if player.ycor() >= 280:
        player.level_up()
        scoreboard.level_up()
        car.level_up()
    
    # loop over all the cars
    for item in car.all_cars:   
        # when the player collides with a car
        if player.distance(item)<=25 :
            game_is_on = False
            scoreboard.game_over()
        
        
screen.exitonclick()