from turtle import Screen, Turtle
XVAL = 1220                 # XVAL is the horizontal length of the pong display screen
YVAL = 720                  # YVAL is the vertical length of the pong display screen

# creating the screen class
class PongScreen:
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.title('PONG')
        self.screen.setup(width=XVAL, height=YVAL)
        self.screen.tracer(0)
        self.start()
        self.ceil()
        self.screen.update()
    def start(self):                # displays the start screen
        tut1 = Turtle()
        tut1.hideturtle()
        tut1.penup()
        tut1.goto(0,340)
        tut1.setheading(270)
        tut1.color('cyan')
        for i in range(35):
            tut1.pendown()
            tut1.forward(10)
            tut1.penup()
            tut1.forward(10)

    def ceil(self):                # displays the vertical walls on the screen
        tut2 = Turtle()
        tut2.color('red')
        tut2.hideturtle()
        tut2.penup()
        tut2.goto(XVAL / 2,YVAL / 2 - 100)
        tut2.pendown()
        tut2.pensize(10)
        tut2.backward(XVAL)
        tut2.penup()
        tut2.goto(XVAL / 2, -YVAL / 2 + 10)
        tut2.pendown()
        tut2.pensize(10)
        tut2.backward(XVAL)

