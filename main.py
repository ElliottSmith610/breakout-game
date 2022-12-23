# Breakout
# Ball hits sides or top = bounce, hits bottom -1 life, 3 life total
# Block class, random colour gen
# Paddle uses block class

from turtle import Screen
from time import sleep
from breakout import Paddle, Board, UI, Score, Ball

WIDTH = 500
HEIGHT = 600

#
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("grey")
screen.tracer(0)
# Classes
paddle = Paddle(HEIGHT)
ui = UI(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT)
score = Score(WIDTH, HEIGHT)
ball = Ball()
#
screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

playing = True
while playing:
    sleep(0.06)
    screen.update()
    ball.move()

    # Check if ball hits wall
    if not -220 < ball.xcor() < 220:
        ball.bounce_x()

    # Check if ball hits top, to bounce
    if ball.ycor() > 270:
        ball.bounce_y()
    # Check if ball hits bottom, deduct heart and reset ball
    elif ball.ycor() < -290:
        score.life_lost()
        if score.no_life():
            playing = False
        else:
            ball.refresh()
            screen.update()
            sleep(1)

    if board.block_num == 0:
        score.game_over()
        playing = False

    if board.check_hit(ball):
        ball.bounce_y()

    if paddle.distance(ball) < 30:
        ball.bounce_y()


screen.exitonclick()
