import turtle
import math
q=turtle.Turtle()
turtle.bgcolor("black")
q.color("red","red")

q.hideturtle()
q.penup()
q.setpos(0,-200)
q.pendown()

q.speed(10)

q.begin_fill()
q.left(60)
q.forward(294)
for i in range(150):
    q.forward(2)
    q.right(math.tan(40))

q.right(90)
for i in range(150):
    q.forward(2)
    q.right(math.tan(40))
  
 
q.forward(295)   
q.end_fill()

q.left(180)
q.forward(200)
q.pencolor("white")
q.left(90)
q.forward(200)
q.left(90)
q.forward(20)
q.left(90)
q.forward(200)
q.penup()
q.forward(200)
q.pendown()
q.forward(200)
q.right(90)
q.forward(10)
q.left(120)
q.forward(40)
q.left(120)
q.forward(40)
q.left(120)
q.forward(10)
q.right(90)
q.forward(200)


turtle.done()