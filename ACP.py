import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the speed of the turtle
pen.speed(0)  # 0 is the fastest speed

# Function to draw a square
def draw_square(side_length, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(side_length)
        pen.left(90)
    pen.end_fill()

# Set the background color
screen = turtle.Screen()
screen.bgcolor("lightblue")  # You can change this to any color you like

# Draw a square with a specific side length and color
draw_square(100, "red")  # Example: side length 100, color red

# Move the turtle to a different position
pen.penup()
pen.goto(150, 150)
pen.pendown()

# Draw another square with different properties
draw_square(75, "green")  # Example: side length 75, color green

# Keep the window open until it is closed manually
turtle.done()