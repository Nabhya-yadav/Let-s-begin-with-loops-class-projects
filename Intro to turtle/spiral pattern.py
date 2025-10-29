import turtle

sc=turtle.Screen()
sc.bgcolor("White")
sc.setup(500,499)
sc.title("Screen setup")

n = 10

# creating instance of turtle

pen = turtle.Turtle()

# loop to draw a side

for i in range(n * 4):

# drawing side of

# length i*10

     pen.forward(i * 10)

# changing direction of pen

# by 90 degree in clockwise

     pen.right(90)

# closing the instance



sc.exitonclick()