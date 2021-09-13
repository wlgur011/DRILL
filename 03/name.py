import turtle as t

t.penup()
t.left(150)
t.forward(400)

t.right(150)
t.pendown()
t.forward(100)
t.right(150)
t.forward(100)
t.left(180)
t.forward(50)
t.right(70)
t.forward(50)

t.penup()
t.left(40)
t.forward(50)
t.pendown()
t.left(90)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(50)

t.penup()
t.forward(50)
t.left(90)
t.forward(50)
t.pendown()
t.forward(50)
t.left(90)
t.pendown()
t.forward(100) # 전

t.penup() 
t.forward(100)
t.left(90)
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)
t.left(180)
t.forward(100)
t.right(90)

t.penup()
t.forward(30)
t.pendown()
t.right(45)
t.forward(50*(2**(1/2)))
t.right(90)
t.forward(50*(2**(1/2))) # 수

t.penup()
t.left(45)
t.forward(60)
t.pendown()
count = 4
while(count>0):
    t.forward(50)
    if(count>1): 
        t.left(90)
    count-=1

t.penup()
t.forward(50)
t.pendown()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.penup()
t.forward(100)

t.pendown()
t.forward(80) # 민


t.exitonclick()