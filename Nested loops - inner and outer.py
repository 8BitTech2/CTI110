# Nested loops - inner and outer
'''
Given the following code, how many times will the inner loop body execute?
The outer loop will iterate 2 times for i = 0,1 while the inner loop will
iterate 3 times for j = 0,1,2. Therefore, 2 * 3 = 6.
'''
for i in range(2):
    for j in range(3):          # Inner loop body
        print (f'{i}{j}')
    
# Given the following code, how many times will the print statement execute?
# The outer loop will iterate 5 times for i = 0,1,2,3,4. The inner loop will
# iterate 2 times, for j = 10,11. Therefore 5 * 2 = 10.
for i in range(5):
    for j in range(10, 12):
        print(f'{i}{j}')
'''
What is the output of the following code?  aa ab ac 
Outer loop executes once ("a"). Inner loop executes three times ("a", "b", "c")
'''
c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print(f'{c1}{c2}', end = ' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)

# What is the output of the following code?
# 13 16 19 113 116 119 (space after last number too)
# outer loop: i1 = 1,11 inner loop: i2=3,6,9 i1 cannot exceed 19 so the outer
# loop only runs twice.  i2 cannot exceed 9 so the inner loop will run 3 timesi1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
    
