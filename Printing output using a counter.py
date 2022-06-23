# Printing output using a counter.
# loop that prints from 1 to user_num, increasing by 1 each time.


num_stars = int(input('enter number: '))  # assume positive
i = 0
while i != num_stars:
    print('*')
    i += 1 # incrementation, if not you will have an infinite loop
