from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

P_RIGHT_X_COR = 350
P_LEFT_X_COR = -350
P_Y_COR = 0

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_right = Paddle((P_RIGHT_X_COR, P_Y_COR))
paddle_left = Paddle((P_LEFT_X_COR, P_Y_COR))
# print(P_LEFT_X_COR)
# print(paddle.shapesize())

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle_right.move_up, key="Up")
screen.onkey(fun=paddle_right.move_down, key="Down")
screen.onkey(fun=paddle_left.move_up, key="w")
screen.onkey(fun=paddle_left.move_down, key="s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 325 or ball.distance(paddle_left) < 50 and ball.xcor() < -325:
        # print("Collision with right paddle")
        ball.bounce_x()

    # Detect ball misses r paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
        paddle_right.reset_paddle_pos()
        paddle_left.reset_paddle_pos()

    # Detect ball misses l paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
        paddle_right.reset_paddle_pos()
        paddle_left.reset_paddle_pos()


screen.exitonclick()

