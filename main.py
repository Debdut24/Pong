from turtle import Screen
from puddle import Puddle
from scorecard import ScoreCard
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)

screen.tracer(0)
r_paddle = Puddle(360, 0)
l_paddle = Puddle(-370, 0)
ball = Ball()
score = ScoreCard()
screen.update()
player1_name = screen.textinput("Player 1:", "Name of first player:")
player2_name = screen.textinput("Player 2:", "Name of second player:")
target = screen.numinput("Score", "Target Score:", 1000, minval=2, maxval=100)
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
condition = True
scores = [5, 10, 15, 20, 25, 30, 40]
speed = 0.1
while condition:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.display_score()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            score.right_win()
            ball = Ball()
            ball.bounce_x()
        if ball.xcor() < -400:
            score.left_win()
            ball = Ball()
    if score.p1_score == target:
        score.declare_winner(player1_name)
        condition = False
    if score.p2_score == target:
        score.declare_winner(player2_name)
        condition = False


screen.exitonclick()
