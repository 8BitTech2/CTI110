# Assign a list to a variable

import turtle

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Looping Alex")

alex = turtle.Turtle()       # Create alex

clrs = ["yellow", "red", "purple", "blue"]
for c in clrs:
    alex.color(c)
    alex.forward(50)
    alex.left(90)

wn.mainloop()
