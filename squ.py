import turtle

screen = turtle.Screen()

screen.bgcolor("lightblue")

t = turtle.Turtle()

t.color("black")
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()