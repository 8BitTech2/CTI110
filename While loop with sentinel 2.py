# While loop with sentinel 2

total_sum = 0

entered_value = int(input('Type a list of numbers: '))

while entered_value > 0:
    total_sum = total_sum + entered_value
    entered_value = int(input())

print('Sum:', total_sum, end='')
