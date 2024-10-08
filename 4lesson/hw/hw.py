import turtle
from random import randint

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(5)
turtle.pencolor('white')
turtle.title('ЧЕРЕПЕШЬИ ГОНКИ | ГОНЩИК НЕЛЕГАЛЬНЫЙ')

def finish():
    turtle.up()
    turtle.goto(300, 150)
    turtle.down()
    turtle.goto(300, -170)

def polosy(x, y):
    turtle.hideturtle()
    turtle.penup()
    for i in range(6):
        turtle.goto(x, y - i * 50)
        for j in range(10):
            turtle.pendown()
            turtle.forward(30)
            turtle.penup()
            turtle.forward(30)

def drawing():
    finish()
    polosy(-300, 120)

def createTurtle(name, y):
    name.up()
    name.goto(-300, y)
    name.shape('turtle')

    red = randint(50, 255)
    green = randint(50, 255)
    blue = randint(50, 255)

    name.color(red, green, blue)

drawing()

turtle.colormode(255)

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()

createTurtle(t1, 100)
createTurtle(t2, 50)
createTurtle(t3, 0)
createTurtle(t4, -50)
createTurtle(t5, -100)

steps = [randint(1, 10) for i in range(5)]

while t1.xcor() < 300 and t2.xcor() < 300 and t3.xcor() < 300 and t4.xcor() < 300:
    t1.forward(steps[0])
    t2.forward(steps[1])
    t3.forward(steps[2])
    t4.forward(steps[3])
    t5.forward(steps[4])

turtle.exitonclick()