from turtle import Turtle

INITIAL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.going_up = True
        self.going_right1 = True
        self.step_x = 10
        self.step_y = 10
        self.move_speed = INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        self.step_y *= -1

    def bounce_on_paddle(self):
        self.step_x *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.step_x *= -1
        self.home()
        self.move_speed = INITIAL_SPEED


