# program reads in a floating-point value from a user and
# calculates the time to drive and fly the distance.
# Note the use of the built-in function float() when reading
#the input to convert the input string into a float.

miles = float(input('Enter a distance in miles: '))
hours_to_fly = miles / 500.0
hours_to_drive = miles / 60.0

print(miles, 'miles would take:')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')
