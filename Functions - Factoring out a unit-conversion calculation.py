# Functions - Factoring out a unit-conversion calculation
'''
Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program:
miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print(f'Miles: {miles_traveled:f}')


Sample output with inputs: 70.0 100.0
Miles: 116.666667
'''
def mph_and_minutes_to_miles(miles_per_hour, minuted_traveled):
    hours_traveled = minutes_traveled / 60
    miles = (minutes_traveled / 60) * miles_per_hour
    return miles

miles_per_hour = float(input('MPH:'))
minutes_traveled = float(input('Minutes traveled:'))

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')
