from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.shape("circle")
        self.color("yellow")
        # self.speed("fastest")
        self.move_speed = 0.1 # 거북이 클래스에 이미 속도라는 메소드가 있기에 혼란을 주지 않으려고 'speed'라고 부르지 않음
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
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



