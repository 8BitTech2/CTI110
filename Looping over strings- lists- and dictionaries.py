# Looping over strings, lists, and dictionaries

cities = {
    'Chicago': 550,
    'London': 3435,
    'Toronto': 5259,
    'Nairobi': 982,
    'Austin': 584,
    'Rome': 309,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)

''' Each iteration assigns city with another key in cities.
When cities[city] > distance, best and distance are assigned with new values.

Toronto 5259

'''
numbers = [3, 7, 5]
for number in numbers:
    print(number)
'''The for loop iterates over the list numbers.
The first iteration assigns number with 3, the second iteration assigns number
with 7, and so on.  The loop ends after iterating over each number in numbers.

3
7
5

'''
word = 'Data'
for char in word:
    print(char, end=',')
print()
''' Each iteration assigns char with the next character in word.
A string is a sequence type, so a for loop can iterate over a string.
D,a,t,a,
'''
weights = [4, 1, 8]
result = 0
for weight in weights:
    result -= weight
print(result)
''' Each loop body execution subtracts weight from result.
-13

'''
numbers = [6, 8, 3, 7]
for number in reversed(numbers):
    print(number)

''' The for loop uses reversed() to iterate over numbers in reverse order.
7
3
8
6

'''



