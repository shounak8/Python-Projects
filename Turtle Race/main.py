# Importing Libraries
import turtle
import random

# Instantiating the objects
screen = turtle.Screen()
turtle.hideturtle()
screen.tracer(0)
turtle.colormode(255)           # this is used for using the RGB color scheme

turtle.speed('fastest')         # this is used to quicken the turtle animation

# creating the 7 turtles who will race each other
tut1 = turtle.Turtle('turtle')
tut2 = turtle.Turtle('turtle')
tut3 = turtle.Turtle('turtle')
tut4 = turtle.Turtle('turtle')
tut5 = turtle.Turtle('turtle')
tut6 = turtle.Turtle('turtle')
tut7 = turtle.Turtle('turtle')
tut0 = turtle.Turtle('turtle')

# this will draw the finish-line
tut0.hideturtle()
tut0.penup()
tut0.forward(300)
tut0.right(90)
tut0.forward(300)
tut0.pensize(10)
tut0.pendown()
tut0.color('cyan')
tut0.backward(600)

# list of the 7 competitor turtles & their colors
comp_list = [tut1, tut2, tut3, tut4, tut5, tut6, tut7]
color_tut = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


# designating color to the turtles
tut1.fillcolor('purple')
tut2.fillcolor('indigo')
tut3.fillcolor('blue')
tut4.fillcolor('green')
tut5.fillcolor('yellow')
tut6.fillcolor('orange')
tut7.fillcolor('red')


y = -300                # start position of the first turtle
for i in comp_list:
    i.penup()
    i.goto(-300,y)
    y = y + 100         # shifting the subsequent turtle by 100 above the current turtle


screen.update()         # updating the start screen directly without animation


# taking user choice as to which color user guess will win
choice = str(turtle.textinput('Choose the Color of the Turtle', 'Choose from\nPurple\nIndigo\nBlue\nGreen\nYellow'
                                                            '\nOrange\nRed')).lower()

# compiling the actual code
cont = True             # looping condition
color_tut = None        # placeholder
while cont:
    for tut in comp_list:
        tut.forward(random.randint(1,4))            # random number dictating the speed of turtle
        if tut.pos()[0] >= 300:
            cont = False
            color_tut = tut.color()[1]
            screen.update()
        screen.update()


# calculating the position of the turtles
posit = {}
dist = []
for turt in comp_list:
    posit[turt.color()[1]]=turt.pos()[0]
    dist.append(turt.pos()[0])

dist.sort(reverse=True)

indexer = dist.index(posit[choice])

result = 1+int(indexer)


# print final output
if choice == color_tut:
    turtle.write(f'you predicted correct.\nTurtle Position = {result} !\n{choice} turtle won', align='center')
else:
    turtle.write(f'{color_tut} turtle won.\nyour turtle did not win.\nyour turtle Position = {result} !', align='center')


screen.exitonclick()
