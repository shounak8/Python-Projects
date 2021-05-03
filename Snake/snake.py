from turtle import Turtle
from random import choice

# defining the constant values
START_POS = [(0,0), (-20,0), (-40,0)]       # starting position of snake
MOVE_DIST = 20                              # distance by which the snake moves
UP = 90                                     # 2D coordinate axis: to turn up
DOWN = 270                                  # 2D coordinate axis: to turn down
RIGHT = 0                                   # 2D coordinate axis: to turn right
LEFT = 180                                  # 2D coordinate axis: to turn left
COLOR = ['green','cyan','yellow']           # possible body colors of the snake


# creating the snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('white')

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle('square')
        new_seg.penup()
        new_seg.color(choice(COLOR))
        new_seg.goto(position)
        self.segments.append(new_seg)

    # method by which the snake grows in size based on the food pellets the snake eats
    def extend(self):
        self.add_segment(self.segments[-1].pos())

    # method by which the snake moves
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())

        self.segments[0].forward(MOVE_DIST)

    # method by which the snake turns up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # method by which the snake turns down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # method by which the snake turns right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # method by which the snake turns left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

