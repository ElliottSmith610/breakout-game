from turtle import Turtle

FONT = ('Courier', 16, 'bold')


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
