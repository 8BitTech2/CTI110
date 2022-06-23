# While loop with sentinel 4
entered_age = int(input('Type your age: '))

while (entered_age < 18 or entered_age > 35):
    if entered_age < 18:
        print('Too young')
    else:
         print('Grown up')
    entered_age = int(input())

print('Perfect fit', end='')
