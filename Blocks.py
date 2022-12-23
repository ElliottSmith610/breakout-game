from turtle import Turtle
from random import choice

COLOURS = ["red", "orange", "yellow", "green", "blue", "cyan", "indigo", "violet"]


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
