# CTI-110
# P3HW2 - MealTipTax
# Timothy Ingram 
# 21Jun2022
#

# Ask user to enter the charge for food
charge_for_food = float(input('Please enter cost of meal: '))
print()

# Ask user to enter theTip for server
while True:
    try:
      tip_percentage = float(input('Enter Tip % amount of 15, 18, or 20: '))
      tip_list = [15, 18, 20]

      if (tip_percentage == 15) or (tip_percentage == 18) or (tip_percentage == 20):   # valid tip percentage
         break
      print ("Invalid percentage entered")
    except Exception as e:
     print (e)
     tip_percentage = tip_percentage
    else :
     tip_percentage = 20
     print ("invalid tip percentage")        # invalid percentage number
    
# calculate the amount of tip
tip_rate = (tip_percentage / 100)

# the Tax amount at 6 %
tax_percent = 6
tax_rate = (tax_percent /100)
print()

# Calculate tip and tax
tip = (charge_for_food * tip_rate)
sales_tax = (charge_for_food * tax_rate)
grand_total = charge_for_food + tip + sales_tax

# Display the following:
#   *Meal price
#   *Calculated tax
#   *Calculated tip
#   *Display total cost of meal ( food charge + tip+ tax)

print('Meal price:  ',format(charge_for_food, ',.1f'), sep='' )
print('Tax:  ', format(sales_tax, ',.1f'), sep='')
print('Tip:  ', format(tip, ',.1f'), sep='')
print('Total:  ', format(grand_total, ',.2f'), sep='', end='\n\n')


# Pseudocode
# Start
#    
# Asks the user to enter the charge for the meal
# Ask user to enter the tip percentage they would like to consider (15% or 18% or 20%),
# if user enters another percentage, the program is to display an error.
# When an accurate percentage is entered , the program is then going to calculate the tip
# and and 6 percent sales tax .
# The program is to display all of these amounts ( original food charge, tip, tax and total
# cost of meal (food charge + tip + tax)).
# Note - the tip and amount are to be requested from the user, the tax is hard coded (fixed amounts)#
#
# Stop

