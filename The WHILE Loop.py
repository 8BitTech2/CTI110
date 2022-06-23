# The WHILE Loop expression - some statement over and over again
# repeat an operation until a Boolian expression is TRUE
# Loop is a construct that causes 1 or more statements to repeatedly execute
# while expression:  then statement indented below this line

# First, execute count=0, then step through while, print, count+1, then start over
# 1 is less than 3, so print, count+1, start over
# 2 is less than 3 ...
# 3 is NOT less than 3, loop stops, go to next line of code
count = 0
while count < 3:
    print('Hello')
    count = count + 1

# don't create an infinite loop (executes forever)
count = 0
while count < 3: # this Boolian expression will always be true because the count won't change
        print('Hello')
        
# ctrl C will stop the program
       count = count + 1

       
while expression:  # Loop expression
    # Loop body: Sub-statements to execute
    # if the loop expression evaluates to True

# Statements to execute after the expression evaluates to False
curr_power = 2
user_char = 'y'

while user_char == 'y':
    print(curr_power)
    curr_power = curr_power * 2
    user_char = input()

print('Done')

