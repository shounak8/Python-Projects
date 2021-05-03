from turtle import Turtle

# creating the ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_move = 0.8
        self.y_move = 0.8
        self.r_score = 0
        self.l_score = 0

    def move(self):                             # sets the ball moving
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)


    def bounce(self):                           # bouncing the ball off the wall
        self.y_move *= -1

    def pad_bounce(self):                       # bouncing the ball off the paddle
        self.x_move *= -1

    def reset_pos(self):                        # restarting the ball movement after a miss from either of the players
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1


