
################################################################
### Turtle Racing Game ###
################################################################

# you will bet with any color from the rainbow and if you bet the correct color of the turtle then you win

# import modules 
from turtle import Turtle,Screen
from random import randint
# initialize screen and screen size
screen=Screen()
screen.setup(width=500,height=500)
# asks for input
bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color from the rainbow: ")
# initialize the colors, positions and empty list
colors = ["red", "orange", "yellow", "green", "blue", "indigo",'violet']
y_positions =[240,170,100,30,-40,-110,-180]
all_turtles=[]

# creating the number of turtle instances equal to the number of colors  
for i in range(len(colors)):
     turtle = Turtle(shape="turtle")
     turtle.penup()
     turtle.color(colors[i])
     # set the initial position of each turtle instance
     turtle.goto(x=-230, y=y_positions[i])
     all_turtles.append(turtle)

# initialise racing variable
racing ='on'
while racing =='on':
     # loop through all the turtle instances
     for turtles in all_turtles:
          # if any of the turtle reaches the end of the screen
          if turtles.xcor() >=250:
               # stop racing
               racing = 'off'
               # return the result of the bet
               win =turtles.pencolor()
               if bet == win:
                    print(f"You won!!!\nYour bet is: {bet}")
                    print(f"The winning turtle is: {win}")
               else:
                    print(f"You lost!!!\nYour bet is: {bet}")
                    print(f"The winning turtle is: {win}")
          # the turtles will move forward by a random number of 10,20,30,40,50
          turtles.forward(randint(1,5)*5)

screen.exitonclick()