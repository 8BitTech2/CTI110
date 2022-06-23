# While loop with sentinel

entered_value = int(input('Enter a value, type 0 when done: '))

minimum_number = entered_value

while entered_value > 0:
    if entered_value < minimum_number:
        minimum_number = entered_value
    entered_value = int(input())

print('Min value:', minimum_number, end='')
