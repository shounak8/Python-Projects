# Importing necessary libraries and classes from neighboring files

from turtle import Screen
from screen import PongScreen
from paddleOOP import Paddle
from ball import Ball
from scoreboard import ScoreBoard


# defining the constants

XVAL = 1200                 # XVAL is the horizontal length of the pong display screen
YVAL = 700                  # YVAL is the vertical length of the pong display screen
blue_score = 0              # blue_score is the score used to track blue-player's score
red_score = 0               # red_score is the score used to track red-player's score


# Instantiating the OOPs objects

screen = Screen()           # creating screen object
pong_screen = PongScreen()  # creatng pong-screen object
score = ScoreBoard()        # creating scoreboard object
RPad = Paddle(580, 0, 'red')       # creating RED (right) paddle
LPad = Paddle(-590, 0, 'blue')     # creating BLUE (left) paddle
ball = Ball()               # creating the ball object

# for adding user interaction, we use the `listen` option to take user inputs that execute particular actions

screen.listen()
screen.onkey(LPad.up,'w',)          # Blue paddle up
screen.onkey(LPad.down,'s')         # Blue paddle down
screen.onkey(RPad.up,'8')           # Red paddle up
screen.onkey(RPad.down,'2')         # Red paddle down


# actual game code compilation
game_on = True        # Game loop condition

while game_on:
    ball.move()       # sets the ball in motion

# Get ball to bounce off wall
    if ball.ycor() > 250 or ball.ycor() < -340:
        ball.bounce()

# Get ball to bounce off pad
    if (ball.distance(RPad) < 20 and ball.xcor() > 580) or (ball.distance(LPad) < 20 and ball.xcor() < -590):
        ball.pad_bounce()

# Condition to stop the game with condition whoever reaches the score of 5 first
    if red_score == 5 or blue_score == 5:
        game_on = False
    else:
        if ball.xcor() > 600:
            score.red_miss()
            blue_score += 1
            ball.reset_pos()

        if ball.xcor() < -600:
            score.blue_miss()
            red_score += 1
            ball.reset_pos()

    screen.update()

score.final_score()             # Display the final score

screen.exitonclick()            # Exit the game-screen
