from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(self)
        self.score = 0
        self.color("white")
        self.penup()
    