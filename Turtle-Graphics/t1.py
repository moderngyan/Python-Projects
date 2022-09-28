import turtle
import math

modern = turtle.Turtle()

# modern.forward(100)
# modern.left(45)
# modern.forward(100)
# modern.right(90)
# modern.forward(100)

# squire
# modern.color("red","yellow")
# modern.begin_fill()
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.end_fill()

# modern.penup()
# modern.forward(100)
# modern.pendown()
# modern.begin_fill()
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.left(90)
# modern.forward(100)
# modern.end_fill()

# for i in range(2000):
#     modern.speed(10)
#     # modern.forward(math.sqrt(i)*10)
#     modern.forward(10)
#     modern.left(math.sin(i/10)*25)
#     modern.left(20)


modern.getscreen().bgcolor("black")
# for i in range(5):
#     modern.color("white")
#     modern.forward(200)
#     modern.left(216)
modern.penup()
modern.goto((-200, 100))
modern.pendown()
def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

star(modern, 360)
turtle.done()