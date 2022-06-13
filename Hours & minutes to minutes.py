# Hours & minutes to minutes

# The program below reads in the number of hours & minutes entered by a user.
# The program then converts the number to just minutes.

hours = int(input('Enter # of hours:'))
minutes = int(input('Enter # of minutes:'))


print (hours, 'hours &', minutes, 'minutes is', end=' ')
hours = hours * 60
minutes_remaining = minutes % 60 + hours
print(minutes_remaining, 'minutes.\n', end=' ')
