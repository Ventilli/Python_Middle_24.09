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

for i in range(1, 501):
    tr.circle(i*1, 180)

turtle.exitonclick()