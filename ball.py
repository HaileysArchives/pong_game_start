from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Detect collision with wall and bounce!
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1



