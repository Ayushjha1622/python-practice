# python program
# import for turtle module
import turtle

# defining instance of turtle
pen = turtle.Turtle()
wn = turtle.Screen()

# this is for bigger triangle
pen.left(60)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(150)

# this for making three lines
# inside the bigger triangle
pen.forward(174)
pen.backward(174)
pen.left(16.5)
pen.forward(180)
pen.backward(180)
pen.right(31.5)
pen.forward(180)
pen.right(75)

# this is for making upper triangle1
pen.forward(53)
pen.left(120)
pen.forward(50)
pen.left(120)
pen.forward(50)

# this is for making upper triangle2
pen.right(120)
pen.forward(50)
pen.left(120)
pen.forward(50)

# this is for making upper triangle3				
pen.right(120)
pen.forward(50)
pen.left(120)
pen.forward(50)

# this is for making upper triangle1
pen.right(120)
pen.forward(50)
pen.left(120)
pen.forward(50)
pen.left(180)
pen.forward(50)

# this is for making line above all 4 small triangle
pen.left(300)
pen.forward(160)
