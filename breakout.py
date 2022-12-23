from turtle import Turtle
from random import choice
FONT = ('Courier', 16, 'bold')
COLOURS = ["red", "orange", "yellow", "green", "blue", "cyan", "indigo", "violet"]
ORIGIN = (0, 0)
SPEED = 10


class UI(Turtle):

    def __init__(self, width, height):
        super(UI, self).__init__()
        self.width = width
        self.height = height
        self.bottom_left = None
        self.top_left = None
        self.top_right = None
        self.bottom_right = None
        self.set_attributes()
        self.draw_border()

    def set_attributes(self):
        self.penup()
        self.hideturtle()
        self.pensize(5)
        self.pencolor("black")


    def draw_border(self):
        left_x = (self.width / 2) * -1 + 20
        right_x = (self.width / 2) - 20
        top_y = (self.height / 2) - 20
        bottom_y = (self.height / 2) * -1 + 20
        self.bottom_left = (left_x, bottom_y)
        self.top_left = (left_x, top_y)
        self.top_right = (right_x, top_y)
        self.bottom_right = (right_x, bottom_y)
        self.goto(self.bottom_left)
        self.pendown()
        self.goto(self.top_left)
        self.goto(self.top_right)
        self.goto(self.bottom_right)
        self.penup()


class Score(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.width = width
        self.height = height
        self.hearts = 3
        self.life_bar()

    def life_bar(self):
        x, y = -self.width / 2, -self.height / 2
        self.goto(x / 1.15, y / 1.1)
        self.refresh_life()

    def refresh_life(self):
        self.write(f"Life:{self.hearts * '❤'}", font=FONT, align='left', move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align='center', move=False)

    def life_lost(self):
        self.hearts -= 1
        self.clear()
        self.refresh_life()

    def no_life(self):
        if self.hearts < 0:
            self.game_over()
            return True


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 1, 0)
        self.penup()
        self.goto(0, 0)


class Paddle(Block):
    # TODO: Rather than 1 block, create a paddle consisting of 3 blocks that follow one another
    #  for a more accurate hit
    def __init__(self, height):
        super().__init__()
        self.color("white")
        self.shapesize(0.5, 3, 0)
        bottom_y = height / 2 * -1 + 70
        self.goto(0, bottom_y)

    def go_left(self):
        if not self.xcor() <= -200:
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())

    def go_right(self):
        if not self.xcor() >= 200:
            new_x = self.xcor() + 40
            self.goto(new_x, self.ycor())


class Board:

    def __init__(self, width, height):
        self.blocks = []
        self.block_num = 0
        block_size = 60
        max_line_w = (width - 100)
        max_line_h = (height / 2) - 50
        self.create_blocks(max_line_w, max_line_h)

    def create_blocks(self, width, height):
        one_side_width = int(width / 2)
        x_positive = []
        print(one_side_width)
        print(width)
        # for _ in range(one_side_width):
        #     x_positive.append((_ * 50 + 90))
        # x_negative = []
        # for _ in x_positive:
        #     x_negative.append(_ * -1)
        # x_positions = x_negative[::-1] + [0] + x_positive

        for i in range(-195, 196, 25):
            x_positive.append(i)
        print(x_positive)
        for h in range(int(height / 30)):
            # print(f"H {h}")
            for x_pos in x_positive:
                block = Block()
                block.color(COLOURS[h])
                self.blocks.append(block)
                y_pos = height - (h * 25)
                block.goto(x_pos, y_pos)
        self.block_num = len(self.blocks)

    def check_hit(self, ball: Turtle):
        for block in self.blocks:
            if ball.distance(block) < 20:
                block.goto(0, 400)
                self.block_num -= 1
                return True

    def block_num(self):
        return self.block_num


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.x_move = -SPEED
        self.y_move = SPEED
        #self.refresh()

    def refresh(self):
        self.goto(ORIGIN)
        self.x_move = choice([-10, 10])
        #self.setheading(randint(0, 360))

    def move(self):
        #self.forward(SPEED)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1