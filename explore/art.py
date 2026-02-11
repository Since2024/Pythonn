import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest setting
turtle.tracer(10, 0) # Smooths out the drawing animation

# Create the pattern
for i in range(400):
    # This math creates a shifting rainbow effect
    color = colorsys.hsv_to_rgb(i/400, 1.0, 1.0)
    t.pencolor(color)
    
    t.forward(i)
    t.left(91) # Change this number to 59, 121, or 89 to see different shapes!
    t.width(i/100 + 1)

turtle.done()