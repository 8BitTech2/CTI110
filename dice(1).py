# CTI 110
# dice.py -- simulates rolling dice
# demonstrates import and the random module

# use the random module
import random

# set constant values for minimum, maximum (dice go from 1 to 6)
MIN = 1
MAX = 6

def main():
    # use a variable to control the loop
    again = 'y'

    # until the user is finished, repeat
    while again == 'y' or again == 'Y':
        # simulate rolling the dice
        print('Rolling two dice...')
        
        first = random.randint(MIN, MAX)
        second = random.randint(MIN, MAX)
        print('Their values are:', first, second)

        # roll again?
        again= input('Roll again? (y = yes): ')

# call the main() function
main()
