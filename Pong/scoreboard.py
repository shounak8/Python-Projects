from turtle import Turtle

# creating the scoreboard class
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.blue = 0
        self.red = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-25, 300)
        self.write(f'Blue: {self.blue}              Red: {self.red}', align='center',font=('Ariel',40,'bold'))


    def red_miss(self):                 # updates scoreboard when red misses
        self.blue += 1
        self.goto(-25, 300)
        self.clear()
        self.write(f'Blue: {self.blue}              Red: {self.red}', align='center',font=('Ariel',40,'bold'))


    def blue_miss(self):                 # updates scoreboard when blue misses
        self.red += 1
        self.goto(-25, 300)
        self.clear()
        self.write(f'Blue: {self.blue}              Red: {self.red}', align='center',font=('Ariel',40,'bold'))

    def final_score(self):               # displays final scoreboard
        if self.blue > self.red:
            self.goto(0, 0)
            self.clear()
            self.color('blue')
            self.write(f'Blue Wins !\nBlue: {self.blue}\nRed: {self.red}', align='center', font=('Ariel', 40, 'bold'))
        else:
            self.goto(0, 0)
            self.clear()
            self.color('red')
            self.write(f'Red Wins !\nBlue: {self.blue}\nRed: {self.red}', align='center', font=('Ariel', 40, 'bold'))
