# Set theory methods
# The following program includes fictional sets of the top 10 male and female baby names for the current year.
# Write a program that creates:

# 1. A set all_names that contains all of the top 10 male and all of the top 10 female names.
# 2. A set neutral_names that contains only names found in both male_names and female_names.
# 3. A set specific_names that contains only gender specific names.
# Sample output for all_names:
# {'Michael', 'Henry', 'Jayden', 'Bailey', 'Lucas', 'Chuck', 'Aiden', 'Khloe', 'Elizabeth', 'Maria', 'Veronica',
#    'Meghan', 'John', 'Samuel', 'Britney', 'Charlie', 'Kim'}
# NOTE: Because sets are unordered, they are printed using the sorted() function here for comparison

male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.
all_names = (male_names.union(female_names))
neutral_names = (male_names.intersection(male_names,female_names))
specific_names = (male_names.symmetric_difference(female_names))
                  

print ('all names:', sorted(all_names))
print ()
print ('all neutral names:', sorted(neutral_names))
print ()
print ('all gender specific names:', sorted(specific_names))
