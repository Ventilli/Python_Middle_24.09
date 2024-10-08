import turtle

tr = turtle.Turtle()
turtle.bgcolor("black")
turtle.title('О боже какой код)))))')
tr.speed(10)
tr.shapesize(1)
tr.shape('turtle')
tr.pensize(1)
tr.color("white")
tr.fillcolor('cyan')


def draw_triangle(length):
    for i in range(3):
        tr.forward(length)
        tr.right(120)

colors = ['red', 'yellow', 'green', 'blue', 'white', 'brown', 'cyan']


def sdfgh():
    tr.penup()
    tr.goto(-500, 0)
    for i in range(50):
        tr.forward(10)
        tr.penup()
        tr.forward(10)
        tr.pendown()



# for i in range(50):
#     draw_triangle(i * 15)
#     tr.right(i + 30)
#     tr.color(colors[i % 7])

# turtle.mainloop()
turtle.exitonclick()