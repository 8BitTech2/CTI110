# loop body execute 4 times

import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Looping Alex")

alex = turtle.Turtle()       # Create alex
 

for x in range(10):       # Sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alex.forward(50)
    alex.left(90)

alex.penup()
alex.forward(100)     # This moves alex, but no line is drawn
alex.pendown()

# for i in range(4):      # Executes the body with i = 0, then 1, then 2, then 3    


for c in ["yellow", "red", "purple", "blue"]:  # changes color for each line
    alex.color(c)
    alex.forward(50)
    alex.left(90)

wn.mainloop()             # Wait for user to close window
