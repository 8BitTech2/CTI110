# enumerate in for loops

seasons = ['winter', 'spring', 'summer', 'fall']
for (position, season) in enumerate(seasons):
    print(position, season)
'''
0 winter
1 spring
2 summer
3 fall
'''
states = ['TX', 'FL', 'NY', 'CA']
for (position, state) in enumerate(states):
    print(state, position)
'''
TX 0
FL 1
NY 2
CA 3
'''
numbers = [-7, -6, 3, 2, 6]
for (position, number) in enumerate(numbers):
    if number < 0:
        print(position, 'x')
    else:
        print(position, number)
'''
The parentheses around a tuple on either side of an assignment statement are optional.
0 x
1 x
2 3
3 2
4 6
'''
