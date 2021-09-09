import turtle as t
t.penup()
t.goto(-250,-250)
count=12
t.speed(100)
while(count>6):
    t.pendown()
    t.forward(500)
    (x,y) = t.pos()
    t.penup()
    if(count>7):
        t.goto(x-500, y+100)
    count-=1
t.right(90)

while(count>0):
    t.pendown()
    t.forward(500)
    (x,y) = t.pos()
    t.penup()
    t.goto(x-100, y+500)
    count-=1

t.exitonclick()