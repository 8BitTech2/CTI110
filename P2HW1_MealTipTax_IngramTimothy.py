# The program is to that calculate the total amount of a meal purchased at a restaurant.
# 12Jun2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Timothy Ingram
#
# Pseudocode
# Start
#    Declare variables charge_for_food,tip_percentage, tax_percent,grand_total
#    Display "Enter Food Cost: "   (user types a number)
#    Blank line
#    Read charge_for_food
#    Display "Enter Tip Percentage: " (user types a number)
#    Set tip_rate = tip_percent divided by 100 
#    Display "Enter Tax Percentage: "  (user types a number)
#    Blank line
#    Set tax_rate =  tax_percent divided by 100 
#    Set tip = charge_for_food times tip_rate
#    Set sales_tax = charge_for_food times tax_rate
#    Set grand_total = charge_for_food + tip +sales_tax
#    Display "Calculated tip: " + (tip)
#    Display "Calculated tax: " + (sales_tax)
#    Blank line
#    Display "Total cost including tip and tax = " + (grand_total)
# Stop


# Ask user to enter the charge for food
charge_for_food = float(input('Enter Food Cost: '))
print()

# Ask user to enter theTip for server 
tip_percentage = float(input('Enter Tip Percentage: '))
tip_rate = (tip_percentage / 100)

# Ask user to enter the Tax amount 
tax_percent = float(input('Enter Tax Percentage: '))
tax_rate = (tax_percent /100)
print()

# Calculate tip and tax
tip = (charge_for_food * tip_rate)
sales_tax = (charge_for_food * tax_rate)
grand_total = charge_for_food + tip + sales_tax

# Display the following:
#   *Calculated tip
#   *Calculated tax
#   *Display total cost of meal ( food charge + tip+ tax)
print('Calculated Tip:  ', format(tip, ',.1f'), sep='')
print('Calculated Tax:  ', format(sales_tax, ',.1f'), sep='')
print()
print('Total cost including tip and tax:  ', format(grand_total, ',.2f'), sep='', end='\n\n')

# the tip , tax and amount are to be requested from the user, they are NOT hard coded (fixed amounts)


