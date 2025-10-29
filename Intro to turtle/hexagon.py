import turtle

sc=turtle.Screen()
sc.bgcolor("White")
sc.setup(500,499)
sc.title("Screen setup")
canvas=turtle.Turtle()
canvas.pensize(4)
canvas.pencolor("red")

side=6
length=100

angle=360/side

for i in range(side):
    canvas.forward(length)
    canvas.right(angle)
    








sc.exitonclick()


