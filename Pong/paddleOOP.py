from turtle import Turtle

# creating the paddle class
class Paddle(Turtle):
    def __init__(self, x, y, color_p):
        super().__init__()
        self.x = x
        self.y = y
        self.color_p = color_p
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.color(self.color_p)
        self.goto(self.x, self.y)

    def up(self):                       # method to move the paddle up
        if self.y < 150:
            self.y += 50
            self.goto(self.x, self.y)


    def down(self):                     # method to move the paddle down
        if self.y > -300:
            self.y -= 50
            self.goto(self.x, self.y)

