# importing necessary libraries and classes
import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# defining the constant values
XVal = (1200/2) - 20
YVal = (700/2) - 20
SCORE = 0

# instantiating the screen object
screen = Screen()
screen.setup(width=1200, height=700)            # display size
screen.bgcolor('black')                         # backgroun
screen.title('Snake Game')                      # title
screen.tracer(0)

snake = Snake()             # instantiating the snake object
food = Food()               # instantiating the food object
score = Scoreboard()        # instantiating the scoreboard object

# For controlling the movement of Snake using user inputs, we use the `listen` function
screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.left,'a')
screen.onkey(snake.down,'s')
screen.onkey(snake.right,'d')

# compiling the code

# selecting the game difficulty
input_check = True          # loop active condition till correct difficulty is selected
while input_check:
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0,0)
    diff = str(turtle.textinput('CHOOSE DIFFICULTY','Choose Difficulty: E:easy, M:moderate, H:hard')).lower()
    if diff == 'e':
        difficulty = 0.09
        input_check = False
    elif diff == 'm':
        difficulty = 0.07
        input_check = False
    elif diff == 'h':
        difficulty = 0.05
        input_check = False
    else:
        turtle.write('Wrong Input. Start over again')


# compiling the actual snake game
game_on = True          # loop active condition
while game_on:
    screen.update()
    time.sleep(difficulty)    # controlling the pace of snake based on difficulty

    snake.move()              # triggering the movement of snake

    #detecting contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > XVal or snake.head.ycor() > YVal or snake.head.xcor() < -XVal or snake.head.ycor() < -YVal:
        game_on = False
        score.game_over()

    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
