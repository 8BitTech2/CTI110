# Conditional expression: Conditional assignment
# Using a conditional expression, a statement that increments num_users
# if update_direction is 3, otherwise decrements num_users.

num_users = int(input('enter # of users:'))
update_direction = int(input('enter udate direction #:'))

num_users = numb_users = num_users + 1 if update_direction == 3 else num_users - 1

print('New value is:', num_users)
