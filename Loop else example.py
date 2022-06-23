# Loop else example

x = 0
y = 5
z = 10
while x < y:
    if x == z:
        print('x == z')
        break
    x += 1 
else:
    print('x == y')

'''
What is the output of the code if z is 10?   x == y 
The loop counts to 5 and then terminates normally,
causing the loop else clause to execute.

What is the output of the code if z is 3?  x == z
The if statement is taken once x is assigned with 3 and a break
causes the loop to end.
Because of the break statement, the loop else clause is not executed.
