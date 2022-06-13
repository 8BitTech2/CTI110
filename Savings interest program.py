# Savings interest program
# Blank print statements are used to go to the next line after reading pre-entered input.

import math

base = float(input('Enter initial savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print ('Savings after', years, 'years is', f'{total:.2f}') 
