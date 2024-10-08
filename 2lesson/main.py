import turtle
from random import randint

tr = turtle.Turtle()
turtle.bgcolor("black")
turtle.title('О боже какой код)))))')
tr.speed(0)
tr.shapesize(1)
tr.shape('turtle')
tr.pensize(1)
tr.color("white")
tr.fillcolor('cyan')

def polygon(n, size = 30):
    if n > 2:
        angle = 360 / n

        for i in range(n):
            tr.forward(size)
            tr.left(angle)

def spiral(n, size = 30):
    colors = ['red', 'yellow', 'green', 'blue', 'white', 'brown', 'cyan']

    for i in range(n):
        tr.color(colors[randint(1, 6)])
        polygon(randint(3, 10), size=size)
        tr.left(30)

def spiral_circles(n, size=100):
    colors = ['red', 'yellow', 'green', 'blue', 'white', 'brown', 'cyan']

    for i in range(n):
        tr.color(colors[randint(1,6)])
        tr.circle(size)
        tr.right(randint(13, 101))

def japan_flag():
    turtle.bgcolor("white")
    tr.speed(0)
    tr.color("red")
    tr.fillcolor('red')
    tr.goto(0, -50)
    tr.begin_fill()
    tr.circle(100)
    tr.end_fill()

japan_flag()

turtle.exitonclick()