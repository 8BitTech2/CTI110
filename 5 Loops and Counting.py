# 5 Loops and Counting
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.width(4)
tina.penup()
tina.goto(0,60)
tina.pendown()
tina.color("green")

tommy = turtle.Turtle()
tommy.penup()
tommy.shape("turtle")
tommy.goto(-50,-90)
tommy.left(90)

for i in range(5):
    tina.right(120)
    tina.forward(130)
    tina.right(120)
    tina.forward(130)
    tina.right(120)
    tina.forward(130)
    tommy.write("%d done, %d to go!" %(i+1, 4-i), None, None, "12pt bold")
    tommy.backward(15)
    tina.right(72)

tommy.goto(-55,-175)
tommy.write("Great job, Tina!", None, None, "16pt bold")
tina.color("purple")
tommy.goto(-75,-175)
tina.penup()
tina.forward(40)
tina.write("Thanks!", None, None, "16pt bold")
tina.backward(40)
