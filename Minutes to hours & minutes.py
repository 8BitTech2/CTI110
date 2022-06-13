# Minutes to hours & minutes

# The program below reads in the number of minutes entered by a user.
# The program then converts the number of minutes to hours and minutes.

minutes = int(input('Enter minutes:\n'))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')
