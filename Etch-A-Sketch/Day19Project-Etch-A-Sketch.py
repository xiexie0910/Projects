from turtle import Turtle,Screen

tim = Turtle()
screen=Screen()

def move_forwards():
     '''move forward'''
     tim.forward(10)

def move_backwards():
     '''move backwards'''
     tim.backward(10)

def move_left():
     '''move left'''
     tim.setheading(tim.heading()+10)
     
def move_right():
     '''move right'''
     tim.setheading(tim.heading()-10)
     
def clear():
     '''clears the screen'''
     tim.penup()
     tim.clear()
     tim.home()
     tim.pendown()
     
# tell the screen to listen out for key strokes
screen.listen()
# listen out for the keystrokes belows
screen.onkey(fun=move_forwards,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=move_left,key="a")
screen.onkey(fun=move_right,key="d")
screen.onkey(fun=clear,key="c")


screen.exitonclick()                    