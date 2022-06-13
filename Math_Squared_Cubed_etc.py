# A program can get an input value from the keyboard

user_num = int(input('Enter integer:\n'))

print('You entered:', user_num)
print(user_num, 'squared is', user_num * user_num)
print('And', user_num, 'cubed is', user_num * user_num * user_num,'!!')

user_num2 = int(input('Enter another integer:\n'))
user_num10 = user_num + user_num2
user_num11 = user_num * user_num2
print(user_num,'+', user_num2, 'is', user_num10)
print(user_num, '*', user_num2, 'is', user_num11)

