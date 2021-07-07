from turtle import Turtle
import random
UPPER_WALL = 230
LOWER_WALL = -230
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        random_y = random.randint(-230, 230)
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
        self.goto(0, random_y)

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= .8