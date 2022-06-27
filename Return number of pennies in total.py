# Return number of pennies in total
'''Write a function number_of_pennies() that returns the total number of pennies given a number of dollars and (optionally) a number of pennies. Ex: If you have $5.06 then the input is 5 6, and if you have $4.00 then the input is 4.
Sample output with inputs: 5 6 4
506
400'''

def number_of_pennies(dollars=0, pennies=0):
    dollars = dollars * 100
    pennies = pennies
    total = dollars + pennies
    return total

print(number_of_pennies(int(input('# of dollars:')), int(input('# of pennies')))) # Both dollars and pennies
print(number_of_pennies(int(input('# of dollars:'))))               # Dollars only
