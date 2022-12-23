from turtle import Turtle
from random import choice
ORIGIN = (0, 0)
SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.x_move = -SPEED
        self.y_move = SPEED
        #self.refresh()

    def refresh(self):
        self.goto(ORIGIN)
        self.x_move = choice([-10, 10])
        #self.setheading(randint(0, 360))

    def move(self):
        #self.forward(SPEED)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
