from turtle import Turtle

# defining the constant values
XVal = (1200/2) - 20
YVal = (700/2) - 20
# font specific constants
ALIGN = 'center'
FONT = ('Arial',10,'normal')

# creating the scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,YVal)
        self.color('white')
        self.write(f'score: {self.score}', align=ALIGN, font=FONT)
        self.hideturtle()

    # method to show the increasing score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'score: {self.score}', align=ALIGN, font=FONT)

    # method to display the final score
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write(f'Game Over. Your score is {self.score}', align = ALIGN, font=('Book Antiqua',20,'bold'))
