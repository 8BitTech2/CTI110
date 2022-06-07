# A program can get an input value from the keyboard
# 6Jun2022
# CTI-110 P1HW1 - Output Code File
# Timothy Ingram

# Ask user to enter a number
user_num = int(input('Enter integer:\n'))

# Display the value inputted, the Square and Cube value of that input.
print('You entered:', user_num)
print(user_num, 'squared is', user_num * user_num)
print('And', user_num, 'cubed is', user_num * user_num * user_num,'!!')

# Ask user for another number
user_num2 = int(input('Enter another integer:\n'))
user_num10 = user_num + user_num2
user_num11 = user_num * user_num2

# Display the sum and times of both inputs
print(user_num,'+', user_num2, 'is', user_num10)
print(user_num, '*', user_num2, 'is', user_num11)
