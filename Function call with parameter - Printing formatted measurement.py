#  Function call with parameter - Printing formatted measurement.
'''
Define a function print_feet_inch_short(), with parameters num_feet and num_inches, that prints using ' and " shorthand. End with a newline. Remember that print() outputs a newline by default. Ex: print_feet_inch_short(5, 8) prints:
5' 8"
Hint: Use \" to print a double quote.
'''


def print_feet_inch_short(num_feet, num_inches):
    print(f"{num_feet}' {num_inches}\"")

user_feet = int(input('Feet:'))
user_inches = int(input('Inches:'))

print_feet_inch_short(user_feet, user_inches) # Will be run with (5, 8), then (4, 11)
