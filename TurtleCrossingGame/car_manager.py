from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # creating an empty arry
        self.all_cars =[]
        # using for loop to create 10 cars and initialise the functionality
        for i in range(15):
            car = Turtle()
            car.shape('square')
            car.color(choice(COLORS))
            car.penup()
            self.hideturtle()
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.goto(randint(300,800),randint(-220,260))
            self.all_cars.append(car)
            self.initialspeed = STARTING_MOVE_DISTANCE *0.1

    def move_x(self):
        '''the cars will move in a horizontal direction'''
        # loop through all the cars
        for car in self.all_cars:
            # move all the cars to the left by the initialspeed
            car.goto(car.xcor() - self.initialspeed,car.ycor())
            # when a car reaches the beyond the left end of the screen
            if car.xcor() <= -340:
                car.goto(randint(300,500),randint(-220,240))

    def level_up(self):
        '''increment the speed when level up'''
        self.initialspeed+=MOVE_INCREMENT * 0.01