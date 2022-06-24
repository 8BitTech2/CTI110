# Draw a Square and a Triangle using "for loops" to create a house

import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()    # Create a turtle, assign to t

# add some display options
t.pensize(1)            # increase pensize (takes integer)
t.pencolor("green")     # set pencolor (takes string)
t.shape("turtle")

#commands  
for i in range(4):
    t.forward(300)
    t.right(90)

t.penup()              # This moves the turtle, but no line is drawn 
t.left(90)
t.forward(10)     
t.pendown()

'''
Create a triangle
'''
# add some display options
t.pensize(5)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("triangle")

# triangle, sides are 360 / 3 = 120 degrees

for i in range(4):
    t.forward(300)
    t.left(120)

# end commands
win.mainloop()             # Wait for user to close window
