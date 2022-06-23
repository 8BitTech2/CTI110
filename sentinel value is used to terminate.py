# sentinel value is used to terminate a loop's processing

'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

values_sum = 0
num_values = 0

curr_value = int(input('Type a list of 5 postive integers, type 0 when done: '))
   
while curr_value > 0: # Get values until 0 (or less)
    values_sum += curr_value
    num_values += 1
    curr_value = int(input())

print(f'Average: {values_sum / num_values:.0f}\n')
