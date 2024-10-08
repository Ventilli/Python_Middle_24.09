import turtle 
 
tr = turtle.Turtle() 
 
def octogram(): 
    for i in range(8): 
        tr.forward(10000) 
        tr.left(135) 
         
        tr.forward(10000) 
        tr.left(90)

def star(): 
    for i in range(9): 
        tr.forward(100) 
        tr.left(160) 
        tr.forward(100) 
        tr.right(120) 

def circles(quantity, step = 10, speed = 10):
    tr.speed(speed)
    for i in range(quantity):
        tr.circle(i * step)
 
# star() 
 
# octogram() 

circles(10, 10, 10) 

turtle.exitonclick()