import turtle

pen = turtle.Turtle()

def ring(color, rad):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()

pen.up()
pen.setpos(-35, 95)
pen.down()
ring('black', 15)

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

pen.up()
pen.setpos(-18, 75)
pen.down()
ring('black', 8)

pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(0, 55)
pen.down()
ring( "black", 5)

pen.up()
pen.setpos(0, 55)
pen.right(90)
pen.down()
pen.circle(5, 180)

pen.up()
pen.setpos(0, 55)
pen.right(360)
pen.down()
pen.circle(5, -180)

pen.hideturtle()

turtle.exitonclick()