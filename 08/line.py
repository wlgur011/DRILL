import turtle
import random
import math

def stop():
    turtle.bye()

def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())

def draw_line():
    a = 70
    b = 100
    for i in range(0,600+1, 2):
        t = i / 10
        
        #x = (1-t) * x1 + t * x2
        #y = (1-t) * y1 + t * y2
        x = (a-b) * math.cos(t) + b * math.cos(t*(a/b - 1))
        y = (a-b) * math.sin(t) - b * math.sin(t*(a/b - 1))
        draw_point((x,y))
    pass


prepare_turtle_canvas()
turtle.speed(100)
draw_line()
# fill here

turtle.done()