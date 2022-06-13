# Creating and modifying sets
# program that modifies the male_names set by removing a name and adding a different name.
# Sample output with inputs: 'Oliver' 'Atlas'
# { 'Atlas', 'Declan', 'Henry' }
# NOTE: Because sets are unordered, the order in which the names in male_names appear may differ.
# print = ('The top 3 most popular male names of 2017 are Oliver, Declan, and Henry') 
male_names = { 'Oliver', 'Declan', 'Henry' }
print(male_names)
name_to_remove = input('name to remove?')
name_to_add = input('name to add?')
male_names.remove(name_to_remove)
male_names.add(name_to_add)
print(male_names)
