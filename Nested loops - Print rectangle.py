'''
Nested loops - Print rectangle
Given the number of rows and the number of columns,
write nested loops to print a rectangle.

Sample output with inputs: 2 3
* * * 
* * *
'''
num_rows = int(input('how long is the rectangle? '))
num_cols = int(input('how wide is the rectangle? '))
for i in range(num_rows):
    for i in range(num_cols):
        print('*', end=' ')
    print()
