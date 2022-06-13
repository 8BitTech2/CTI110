# String indexing
#  program that looks up the indices of letters in the alphabet.
# Try entering a negative value like -1, or -25.
# string starts on left using 0 as the first location

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_number = int(input('Enter number to use as index: '))
print()

print('\nThe letter at index', user_number, 'of the alphabet is', alphabet[user_number])

#
# Reading multiple data types
person_name = input('Person Name:')
person_age = int(input('Person Age:'))


print('In 5 years', person_name, 'will be', person_age + 5)
