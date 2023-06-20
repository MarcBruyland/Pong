from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((WIDTH / 2 - 50, 0))
l_paddle = Paddle((- WIDTH / 2 + 50, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen(xdummy=None, ydummy=None)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "w")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with the wall
    if ball.ycor() > (HEIGHT / 2) - 20 or ball.ycor() < -(HEIGHT / 2) + 20:
        ball.bounce_on_wall()

    # detect collision with paddle
    if (ball.xcor() > WIDTH / 2 - 50 - 30 and ball.distance(r_paddle) < 50) or \
       (ball.xcor() < -WIDTH / 2 + 50 + 30 and ball.distance(l_paddle) < 50):
        ball.bounce_on_paddle()

    # detect out of bound at the right side
    if ball.xcor() > WIDTH / 2 - 20:
        ball.reset_position()
        scoreboard.increase_l_score()

    # detect out of bound at the left side
    if ball.xcor() < -WIDTH / 2 + 20:
        ball.reset_position()
        scoreboard.increase_r_score()

    screen.update()


screen.exitonclick()