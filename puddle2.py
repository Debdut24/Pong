from turtle import Turtle
COORDINATES = (-370, 0)
X_COR = -370
class Puddle2:
    def __init__(self):
        self.new_turtle = Turtle()
        self.new_turtle.color("white")
        self.new_turtle.shape("square")
        self.new_turtle.penup()
        self.new_turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.new_turtle.goto(COORDINATES)

    def move_up(self):
        y_pos = self.new_turtle.ycor()
        self.new_turtle.goto(X_COR, y_pos + 20)

    def move_down(self):
        y_pos = self.new_turtle.ycor()
        self.new_turtle.goto(X_COR, y_pos - 20)