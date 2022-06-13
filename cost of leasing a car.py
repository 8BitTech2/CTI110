# Computes the total cost of leasing a car given the down payment,
# monthly rate, and number of months

down_payment = int(input('Enter down payment: '))
payment_per_month = int(input('Enter monthly payment: '))
num_months = int(input('Enter number of months: '))

total_cost = down_payment + (payment_per_month * num_months)

print ('Total cost:', total_cost)
