# loop body rainbow box

import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Looping Alex")

alex = turtle.Turtle()       # Create alex
 

for c in ["yellow", "red", "purple", "blue"]:  # changes color for each line
    alex.color(c)
    alex.forward(50)
    alex.left(90)
