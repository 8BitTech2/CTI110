# This program will allow the user to enter the name and cost of an expense.
# 6Jun2022
# CTI-110 P1HW2 - Basic Math
# Timothy Ingram
#

# Calculations of the amount of Tax, Monthly charge and Annual charge.
# Ask user to enter the name of the expense.
print('Enter name of expense:', end=' ')
Expense_name = input()

# Ask user to enter how much they are charged for that expense/bill monthly (without tax).
print ('Enter monthly charge:', end=' ')
monthly_noTax = int(input())
  
# Calculate monthly tax
Tax_monthly = (monthly_noTax * 0.06)

# Calculate amount paid monthly
Monthly_Charge = monthly_noTax + Tax_monthly

# Calculate amount paid for entire year.
Annual_Charge = Monthly_Charge * 12
 
# Display results
print()
# Expense name and monthly charge before taxes
print('Bill:', Expense_name, '---------', 'Before Tax: ${:.2f}'.format (monthly_noTax))      
# Monthly Tax of inputed amount
print('Monthly Tax:     ${:.2f}'.format(Tax_monthly))
# Total monthly bill plus tax
print('Monthly Charge:  ${:.2f}'.format(Monthly_Charge))
# Total amount paid for the year
print('Annual Charge:   ${:.2f}'.format(Annual_Charge))
