from turtle import Turtle
class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 210)


    def left_win(self):
        self.p2_score += 1
        self.display_score()

    def right_win(self):
        self.p1_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.p1_score} | {self.p2_score}", move=False, align="center", font=("Arial", 20, "bold"))

    def declare_winner(self, name):
        self.clear()
        self.goto(0, 0)
        self.write(f"{name} is the winner !", move=False, align="center", font=("Arial", 20, "bold"))