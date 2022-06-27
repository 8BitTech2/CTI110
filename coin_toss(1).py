# CTI 110
# coin_toss.py -- simulates coin tosses
# demonstrates import and the random module

# use the random module
import random

# set constant values
HEADS = 1
TAILS = 2

def main():
    times = int(input('Number of times to flip the coin? '))
    for flip in range(times):
        # simulate coin toss
        coin = random.randint(HEADS, TAILS)
        # print the result
        if coin == HEADS:
            print('Heads')
        else:
            print('Tails')


# call the main() function
main()
