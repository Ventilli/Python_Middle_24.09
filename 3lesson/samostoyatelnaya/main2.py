import turtle

c = turtle.Turtle()
c.speed(10)


def body():
    c.pensize(20)

    c.fillcolor('red')
    c.begin_fill()

    c.right(90)
    c.forward(50)
    c.left(180)
    c.circle(40, -180)

    c.left(180)
    c.forward(200)
    c.left(180)
    c.circle(100, -180)

    c.back(20)
    c.left(15)
    c.circle(500, -20)

    c.back(20)
    c.circle(40, -180)
    c.left(7)
    c.back(50)

    c.penup()
    c.left(90)
    c.forward(10)
    c.right(90)
    c.pendown()
    c.right(240)
    c.circle(50, -70)
    c.end_fill()


def glass():

    c.penup()
    c.right(230)
    c.forward(100)
    c.left(90)
    c.forward(20)
    c.right(90)
    c.pendown()

    c.fillcolor('light blue')
    c.begin_fill()
    c.right(150)
    c.circle(90, -55)

    c.back(1)
    c.left(360)
    c.circle(10, -65)

    c.back(110)
    c.left(360)
    c.circle(50, -190)

    c.right(170)
    c.forward(80)
    c.left(170)
    c.circle(45, -30)

    c.end_fill()


def backpack():
    c.penup()
    c.right(60)
    c.forward(100)
    c.right(90)
    c.forward(75)

    c.fillcolor('red')
    c.begin_fill()
    c.pendown()

    c.forward(30)
    c.right(255)
    c.circle(300, -30)
    c.right(260)
    c.forward(30)

    c.end_fill()


body()
glass()
backpack()

turtle.exitonclick()