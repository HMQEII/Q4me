import turtle
t = turtle.Turtle()
t.speed(6)
ps=25

s = turtle.Screen()
s.bgcolor("Black")

c = ["aqua", "navy blue", "purple", "red", "magenta", "light green", "maroon"]
uk =  ['red','white','black']
a = 100
for i in range(a):
    ps=ps-6
    t.pensize(ps)
    t.color(uk[i % 7])
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.right(45)
    t.forward(120)
    t.penup()
    t.goto(-45,0)
    t.left(45)
    t.pendown()

    t.left(90)
    t.forward(200)
    t.left(135)
    t.forward(150)
    t.left(135)
    t.forward(150)
    t.backward(50)
    t.penup()
    t.goto(-45,0)
    t.pendown()

    t.left(90)
    t.forward(200)
    t.right(135)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(200)
    t.penup()
    t.goto(96, 0)
    t.left(90)
    t.pendown()

    
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.forward(150)
    t.backward(150)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.hideturtle()
    

turtle.done()
