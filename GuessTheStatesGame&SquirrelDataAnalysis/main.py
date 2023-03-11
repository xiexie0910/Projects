### Guessing The States Game ###

# importing modules 
import turtle
import pandas as pd 

# creating instances 
pen = turtle.Turtle()
screen = turtle.Screen()
# setting up the title and shapes
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
# initialising empty arrays for storing information
correct_answers =[]
states_to_learn=[]

data = pd.read_csv("50_states.csv")
# initialise score for incrementing the while loop
score = 0
while score <= 50:
     # asks user for input
     answer = screen.textinput(title=f"Guess The State. {score}/50",prompt="What's another state's name? ").title()
     # when the user wants to exit the game
     if answer == 'Exit':
          # loop through all the states and check if the state is already in the correct answers
          states_to_learn =[states for states in data['state'] if states not in correct_answers]

          # creating a csv file from that list
          states_to_learn = pd.DataFrame(states_to_learn).to_csv('states_to_learn.csv')
          break
     elif answer in set(data['state']):
          # get the x and y coordinates of the state
          x = data[data['state'] == answer]['x']
          y = data[data['state'] == answer]['y']
          pen.hideturtle()
          pen.penup()
          # get turtle to go to that position
          pen.goto(int(x),int(y))
          pen.pendown()
          pen.write(arg=answer,move=False,font=("Arial",10,'normal'))
          # add correct answer to the list
          correct_answers.append(answer)
          score+=1

