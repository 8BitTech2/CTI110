# drawing a rectangle

import turtle             # Allows us to use turtles

wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.shape("turtle")      # arrow, blank, circle, classic, square, triangle, turtle

alex.forward(80)          # Tell alex to move forward by 50 units
alex.left(90)             # Tell alex to turn by 90 degrees
alex.pensize(3)           # Change thickness of line

alex.forward(50)          # Complete the second side of a rectangle
alex.left(90)             # Tell alex to turn by 90 degrees
alex.color("purple")      # Change line color  
alex.forward(80)          # Tell alex to move forward by 50 units
alex.left(90)             # Tell alex to turn by 90 degrees
alex.forward(50)          # Complete the forth side of a rectangle
alex.speed(10)            # Change speed


# for i in [0,1,2,3]:         # "repeating pattern” of statements option
#    alex.forward(50)
#    alex.left(90)

alex.penup()
alex.forward(100)     # This moves alex, but no line is drawn
alex.pendown()

for i in range(4):     # Executes the body with i = 0, then 1, then 2, then 3
    alex.forward(150)
    alex.left(90)
