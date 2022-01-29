from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")

scoreboard = ScoreBoard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()








    # if ball.xcor() < 0:
    #     ball.backward(20)
    # else:
    #     ball.forward(20)





screen.exitonclick()