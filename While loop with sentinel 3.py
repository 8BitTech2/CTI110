# While loop with sentinel 3

curr_age = int(input('Type a list of numbers: '))

while (curr_age < 15 or curr_age > 40):
    if curr_age < 15:
        print('Very young')
    else:
         print('Grown up')
    curr_age = int(input())

print('Perfect match', end='')
