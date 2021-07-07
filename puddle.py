from turtle import Turtle
class Puddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)


    def move_up(self):
        y_pos = self.ycor()
        self.goto(self.x, y_pos+20)

    def move_down(self):
        y_pos = self.ycor()
        self.goto(self.x, y_pos - 20)