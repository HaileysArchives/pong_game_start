# 1. Create the screen (height = 600, width = 800) 

from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
# screen.tracer(0)의 정확한 의미는 코드들이 실행되는 과정을 스크린창에 출력하지 않는 것이기 때문입니다.

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on: # 위에서 tracer(0)만 작성했을 땐 No animation이었기 때문에 이렇게 while문을 사용해서 계속 업데이트 해주어야 한다.
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.increase_score()

    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
