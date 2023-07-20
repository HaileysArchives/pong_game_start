# Create and move a paddle

# width = 20, height = 100, x_pos = 350, y_pos = 0
# up and down key move paddle 20 pixcels.

from turtle import Turtle 

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__() 
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20 # current position
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(), new_y)

    # Detect if the ball goes out of bounds at the edge of the screen. 
    # If yes, reset the ball's position to the center of the screen. 
    # The ball should then start moving towards the other player.
    


