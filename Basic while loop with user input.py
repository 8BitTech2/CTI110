# Basic while loop with user input
# expression that executes the loop body as
# long as the user enters a non-negative number.

user_num = int(input('Enter a number:'))
while user_num >= 0:
  print('Body')
  user_num = int(input())

print('Done.')
