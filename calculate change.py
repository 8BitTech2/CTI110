# Compute change
# A cashier distributes change using the maximum number of five-dollar bills,
# followed by one-dollar bills.

# Determine how much the consumer is using to make change
amount_to_change = int(input('How much is given for currency conversion? '))

num_fives = amount_to_change // 5
num_ones = amount_to_change % 5

                             
# display
print()
print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')
             
