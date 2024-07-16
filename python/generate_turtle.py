import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Graphics")
wn.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Finish
turtle.done()

