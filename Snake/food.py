from turtle import Turtle
import random
XVal = (1200/2) - 20
YVal = (700/2) - 20


# creating the food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.shape('turtle')             # food pellet is in the form on YELLOW TURTLE
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.x = random.randint(-XVal+20,XVal-20)
        self.y = random.randint(-YVal+20, YVal-20)
        self.goto(self.x,self.y)
        self.refresh()

    # method by which the next food pellet is displayed on screen
    def refresh(self):
        self.x = random.randint(-XVal+20,XVal-20)
        self.y = random.randint(-YVal+20, YVal-20)
        self.goto(self.x,self.y)
