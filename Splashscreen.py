#simultaneous execution of 2 turtles
import turtle
import os 
import time

#creating the object of turtle
t = turtle.Turtle()
p = turtle.Turtle()
t.speed(6)   #defining speed
p.speed(6)
ps=25
tspeed=6

#calling the splashscreen
s = turtle.Screen()
s.bgcolor("Black")

#defining the brush colours
c = ["aqua", "navy blue", "purple", "red", "magenta", "light green", "maroon"]
uk =  ['red','black']
a = 2
for i in range(a):
    #for printing Q
    ps=ps-6
    t.pensize(ps)
    #p.pensize(13)
    t.color(uk[i % 7])
   # p.color('black')
    t.penup()
    #p.penup()
    t.goto(-150, 0)
    #p.goto(-150,0)
    t.pendown()
   # p.pendown()
    t.circle(100)#
   # p.circle(100)
    
    #Printing 4
    t.penup()
    t.goto(-45,0)
    t.left(0)
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

#Printing M
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

 #Printing E   
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

#Printing the Underline   
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.speed(tspeed)
    t.right(45)
    t.forward(120)
    t.left(45)
    t.forward(150)
    t.speed(6)
    t.hideturtle()
    tspeed=tspeed-5

#Screen halt   
time.sleep(3)

#Terminating the splashscreen
turtle.bye()

#Calling the Login Page
os.system('python Login.py')
